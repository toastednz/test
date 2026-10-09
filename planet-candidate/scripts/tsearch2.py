#!/usr/bin/env python3
"""Two-stage transit search on TESS 2-min SPOC light curves.

Stage A: for each contiguous block of sectors, detrend (wotan biweight), bin to 10 min, run a Box Least
         Squares sweep (astropy, SNR objective) over 0.5 d .. min(60 d, baseline/2) with an Ofir-style grid.
Stage B: refine every block peak (SNR>=5) on the FULL multi-sector data with a fine local grid around
         P, P/2 and 2P; record full-data SNR, number of transits, odd/even and secondary-eclipse statistics.

Usage: tsearch2.py DATA_DIR TARGET_CSV OUT_CSV [--workers N] [--limit N] [--keep]
TARGET_CSV needs column ID.  Rows are appended to OUT_CSV (one row per star; JSON blob with peaks).
"""
import os, sys, re, glob, time, json, argparse, warnings
import numpy as np
import pandas as pd
import requests
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares

warnings.filterwarnings("ignore")
MAST = "https://mast.stsci.edu/api/v0.1/Download/file/?uri=mast:TESS/product/"
DEFAULT_BITMASK = 1 | 2 | 4 | 8 | 32 | 128 | 1024 | 2048 | 8192 | 32768 | 65536
DURATIONS_H = np.array([0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0])
BIN_MIN = 10.0


def build_filemap(data_dir):
    rx = re.compile(r"(tess\d+-s(\d{4})-(\d{16})-\d{4}-[sa]_lc\.fits)")
    fmap = {}
    for f in sorted(glob.glob(os.path.join(data_dir, "lclists", "tesscurl_sector_*_lc.sh"))):
        with open(f) as fh:
            for line in fh:
                m = rx.search(line)
                if m and int(m.group(2)) < 200:
                    fmap.setdefault(int(m.group(3)), []).append((int(m.group(2)), m.group(1)))
    return fmap


def download(fname, cache_dir, retries=4):
    path = os.path.join(cache_dir, fname)
    if os.path.exists(path) and os.path.getsize(path) > 100000:
        return path
    for i in range(retries):
        try:
            r = requests.get(MAST + fname, timeout=120)
            if r.status_code == 200 and len(r.content) > 100000:
                with open(path, "wb") as fh:
                    fh.write(r.content)
                return path
        except Exception:
            pass
        time.sleep(2 ** i)
    return None


def load_sector(path):
    with fits.open(path, memmap=False) as h:
        d = h[1].data
        t = d["TIME"].astype(float); f = d["PDCSAP_FLUX"].astype(float); e = d["PDCSAP_FLUX_ERR"].astype(float)
        q = d["QUALITY"]; sec = h[0].header.get("SECTOR", -1)
    m = np.isfinite(t) & np.isfinite(f) & np.isfinite(e) & ((q & DEFAULT_BITMASK) == 0)
    t, f, e = t[m], f[m], e[m]
    if len(t) < 500:
        return None
    med = np.nanmedian(f)
    return t, f / med, e / med, int(sec)


def detrend(t, f, e, window=0.6):
    from wotan import flatten
    flat, trend = flatten(t, f, method="biweight", window_length=window, edge_cutoff=0.1,
                          break_tolerance=0.3, return_trend=True)
    m = np.isfinite(flat)
    t, flat, e = t[m], flat[m], e[m] / trend[m]
    resid = flat - 1.0
    mad = np.nanmedian(np.abs(resid - np.nanmedian(resid))) * 1.4826
    keep = resid < 3.0 * mad          # clip flares (positive outliers) only
    return t[keep], flat[keep], e[keep], mad


def bin_lc(t, f, e, dt=BIN_MIN / 1440.0):
    idx = np.floor((t - t[0]) / dt).astype(int)
    uniq, inv, cnt = np.unique(idx, return_inverse=True, return_counts=True)
    tb = np.bincount(inv, weights=t) / cnt
    fb = np.bincount(inv, weights=f) / cnt
    eb = np.sqrt(np.bincount(inv, weights=e ** 2)) / cnt
    return tb, fb, eb


def period_grid(baseline, pmin=0.5, pmax=None, oversample=3.0, dur1=0.045):
    if pmax is None:
        pmax = baseline / 2.0
    fmax, fmin = 1.0 / pmin, 1.0 / pmax
    A = dur1 / (oversample * baseline)
    u0, u1 = 3 * fmin ** (1 / 3), 3 * fmax ** (1 / 3)
    n = max(int(np.ceil((u1 - u0) / A)), 10)
    u = np.linspace(u0, u1, n)
    return 1.0 / ((u / 3) ** 3)[::-1]


def count_transits(t, P, t0, dur):
    n = np.round((t - t0) / P)
    intr = np.abs(t - (t0 + n * P)) < 0.5 * dur
    return len(np.unique(n[intr]))


def blocks_from_sectors(t, s):
    """Group sectors into contiguous blocks (time gap between consecutive sectors < 40 d)."""
    secs = np.unique(s)
    starts = {sec: t[s == sec].min() for sec in secs}; ends = {sec: t[s == sec].max() for sec in secs}
    blocks, cur = [], [int(secs[0])]
    for a, b in zip(secs[:-1], secs[1:]):
        if starts[b] - ends[a] < 40:
            cur.append(int(b))
        else:
            blocks.append(cur); cur = [int(b)]
    blocks.append(cur)
    return blocks


def peaks_from_power(periods, pw, k=5):
    order = np.argsort(pw)[::-1]
    picked = []
    for i in order:
        P = periods[i]
        if all(abs(P / q - 1) > 0.02 for q in [p[0] for p in picked]):
            picked.append((P, i))
        if len(picked) >= k:
            break
    return picked


def stage_a(tb, fb, eb):
    baseline = tb[-1] - tb[0]
    pmax = max(min(baseline / 2.0, 60.0), 1.0)
    periods = period_grid(baseline, 0.5, pmax)
    durs = DURATIONS_H / 24.0
    bls = BoxLeastSquares(tb, fb, dy=eb)
    res = bls.power(periods, durs, objective="snr", method="fast", oversample=4)
    pw = np.asarray(res.power)
    sde = (pw - np.nanmean(pw)) / np.nanstd(pw)
    out = []
    for P, i in peaks_from_power(periods, pw, 5):
        out.append(dict(P=float(P), t0=float(res.transit_time[i]), dur=float(res.duration[i]), depth=float(res.depth[i]),
                        snr=float(pw[i]), sde=float(sde[i]), ntr=int(count_transits(tb, P, res.transit_time[i], res.duration[i]))))
    return out, len(periods), baseline


def stage_b(tb, fb, eb, P0, dur0, bl_block):
    """Refine around P0 (and aliases) on the full data set."""
    baseline = tb[-1] - tb[0]
    bls = BoxLeastSquares(tb, fb, dy=eb)
    best = None
    for mult in (1.0, 0.5, 2.0):
        P = P0 * mult
        if P < 0.5 or P > baseline / 1.5:
            continue
        halfw = max(3 * dur0 * P / bl_block, 0.002 * P)
        dP = dur0 * P / (3.0 * baseline)
        n = min(int(2 * halfw / dP) + 1, 6000)
        grid = np.linspace(P - halfw, P + halfw, n)
        durs = np.unique(np.clip(dur0 * np.array([0.6, 0.8, 1.0, 1.25, 1.5]), 0.5 / 24, 8 / 24))
        res = bls.power(grid, durs, objective="snr", method="fast", oversample=4)
        pw = np.asarray(res.power); i = int(np.argmax(pw))
        if best is None or pw[i] > best["snr"]:
            st = bls.compute_stats(grid[i], res.duration[i], res.transit_time[i])
            odd, even = st["depth_odd"], st["depth_even"]
            oe = abs(odd[0] - even[0]) / np.sqrt(odd[1] ** 2 + even[1] ** 2 + 1e-30)
            sec = st["depth_phased"]
            ntr = count_transits(tb, grid[i], res.transit_time[i], res.duration[i])
            n_ = np.round((tb - res.transit_time[i]) / grid[i]); phs = tb - (res.transit_time[i] + n_ * grid[i])
            intr = np.abs(phs) < 0.5 * res.duration[i]; oot = (np.abs(phs) > 0.75 * res.duration[i]) & (np.abs(phs) < 3.0 * res.duration[i])
            ptd, pte = {}, {}
            for k in np.unique(n_[intr]):
                mm = intr & (n_ == k); mo = oot & (n_ == k)
                if mm.sum() >= 2 and mo.sum() >= 6:
                    ptd[int(k)] = round(float(1e6 * (np.mean(fb[mo]) - np.mean(fb[mm]))), 1)
                    pte[int(k)] = round(float(1e6 * np.std(fb[mo]) / np.sqrt(mm.sum())), 1)
            # red-noise-aware statistics from per-transit depths (local baselines)
            if len(ptd) >= 2:
                dd = np.array([ptd[k] for k in ptd]); ee = np.array([max(pte[k], 1e-3) for k in ptd])
                w = 1 / ee ** 2; wm = np.sum(dd * w) / np.sum(w)
                snr_comb = float(wm * np.sqrt(np.sum(w))); chi2 = float(np.sum((dd - wm) ** 2 * w) / max(len(dd) - 1, 1))
                j = int(np.argmax(dd / ee)); keep = np.ones(len(dd), bool); keep[j] = False
                snr_wo = float(np.sum(dd[keep] * w[keep]) / np.sum(w[keep]) * np.sqrt(np.sum(w[keep]))) if keep.sum() else 0.0
                n_sig = int(np.sum(dd / ee > 2))
            else:
                snr_comb, chi2, snr_wo, n_sig = np.nan, np.nan, np.nan, 0
            best = dict(P=float(grid[i]), t0=float(res.transit_time[i]), dur=float(res.duration[i]), depth=float(res.depth[i]),
                        depth_err=float(res.depth_err[i]), snr=float(pw[i]), ntr=int(ntr), mult=mult, oe_sig=float(oe),
                        sec_depth=float(sec[0]), sec_sig=float(sec[0] / (sec[1] + 1e-30)), per_transit_ppm=ptd, per_transit_err=pte,
                        snr_comb=snr_comb, chi2_depths=chi2, snr_wo_max=snr_wo, n_transits_sig=n_sig)
    return best


def search_star(tic, files, cache_dir, keep=False, masks=None):
    t0w = time.time()
    parts = []
    for sec, fname in sorted(files):
        p = download(fname, cache_dir)
        if p is None:
            continue
        try:
            r = load_sector(p)
        except Exception:
            r = None
        if not keep:
            try: os.remove(p)
            except OSError: pass
        if r is not None:
            parts.append(r)
    if not parts:
        return dict(tic=tic, status="nodata")
    T, F, E, S, MAD = [], [], [], [], []
    for (t, f, e, sec) in parts:
        t, f, e = bin_lc(t, f, e)
        t, f, e, mad = detrend(t, f, e)
        T.append(t); F.append(f); E.append(e); S.append(np.full(len(t), sec)); MAD.append(mad)
    t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); s = np.concatenate(S)
    o = np.argsort(t); t, f, e, s = t[o], f[o], e[o], s[o]
    nmasked = 0
    for (Pm, t0m, durm) in (masks or []):   # mask known transits (+-1 full duration around each transit)
        phm = ((t - t0m + 0.5 * Pm) % Pm) - 0.5 * Pm
        keepm = np.abs(phm) > 1.0 * durm
        nmasked += int((~keepm).sum()); t, f, e, s = t[keepm], f[keepm], e[keepm], s[keepm]
    if len(t) < 500:
        return dict(tic=tic, status="nodata_after_mask")
    tb_all, fb_all, eb_all, sb = t, f, e, s
    blocks = blocks_from_sectors(tb_all, sb)
    out = dict(tic=tic, status="ok", nsec=len(np.unique(s)), npts=len(tb_all), baseline=round(tb_all[-1] - tb_all[0], 2),
               rms10_ppm=round(1e6 * np.nanstd(fb_all), 1), mad2_ppm=round(1e6 * np.median(MAD), 1), nblocks=len(blocks), nmasked=nmasked)
    block_peaks = []
    for bi, bsecs in enumerate(blocks):
        m = np.isin(sb, bsecs)
        if m.sum() < 500:
            continue
        pk, nper, bl = stage_a(tb_all[m], fb_all[m], eb_all[m])
        for p in pk:
            p.update(block=bi, sectors=",".join(map(str, bsecs)), bl=round(bl, 1))
        block_peaks.extend(pk)
    refined, seen = [], []
    for p in sorted(block_peaks, key=lambda x: -x["snr"]):
        if p["snr"] < 5.0:
            continue
        if any(abs(p["P"] / q - 1) < 0.01 or abs(p["P"] / q - 2) < 0.01 or abs(p["P"] / q - 0.5) < 0.005 for q in seen):
            continue
        seen.append(p["P"])
        r = stage_b(tb_all, fb_all, eb_all, p["P"], p["dur"], p["bl"])
        if r is not None:
            r["from_block"] = p["block"]; r["block_snr"] = p["snr"]; r["block_sde"] = p["sde"]; r["block_P"] = p["P"]
            refined.append(r)
        if len(seen) >= 5:
            break
    refined.sort(key=lambda x: -x["snr"])
    if refined:
        b = refined[0]
        out.update(P=round(b["P"], 6), t0=round(b["t0"], 5), dur_h=round(b["dur"] * 24, 3), depth_ppm=round(1e6 * b["depth"], 1),
                   snr=round(b["snr"], 2), ntr=b["ntr"], oe_sig=round(b["oe_sig"], 2), sec_sig=round(b["sec_sig"], 2),
                   block_snr=round(b["block_snr"], 2), block_sde=round(b["block_sde"], 2), from_block=b["from_block"],
                   snr_comb=round(b.get("snr_comb", np.nan), 2), chi2_depths=round(b.get("chi2_depths", np.nan), 2), snr_wo_max=round(b.get("snr_wo_max", np.nan), 2))
    else:
        out.update(P=np.nan, snr=np.nan)
    out["best_block_snr"] = round(max([p["snr"] for p in block_peaks], default=np.nan), 2)
    out["best_block_sde"] = round(max([p["sde"] for p in block_peaks], default=np.nan), 2)
    out["peaks_json"] = json.dumps(dict(blocks=block_peaks, refined=refined))
    out["runtime_s"] = round(time.time() - t0w, 1)
    return out


def _worker(args):
    tic, files, cache, keep, masks = args
    try:
        return search_star(tic, files, cache, keep, masks)
    except Exception as ex:
        return dict(tic=tic, status="error:" + repr(ex)[:300])


COLS = ["tic", "status", "nsec", "npts", "baseline", "rms10_ppm", "mad2_ppm", "nblocks", "P", "t0", "dur_h", "depth_ppm",
        "snr", "ntr", "oe_sig", "sec_sig", "block_snr", "block_sde", "from_block", "best_block_snr", "best_block_sde", "snr_comb", "chi2_depths", "snr_wo_max", "nmasked", "runtime_s", "peaks_json"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir"); ap.add_argument("targets"); ap.add_argument("out")
    ap.add_argument("--workers", type=int, default=4); ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--keep", action="store_true"); ap.add_argument("--mask-file", default=None, help="CSV with columns tic,P,t0,dur_d of known transits to mask")
    a = ap.parse_args()
    maskmap = {}
    if a.mask_file:
        mdf = pd.read_csv(a.mask_file)
        for r in mdf.itertuples():
            maskmap.setdefault(int(r.tic), []).append((float(r.P), float(r.t0), float(r.dur_d)))
    fmap = build_filemap(a.data_dir)
    targets = pd.read_csv(a.targets)
    if a.limit:
        targets = targets.head(a.limit)
    done = set()
    if os.path.exists(a.out) and os.path.getsize(a.out) > 0:
        try: done = set(pd.read_csv(a.out, usecols=["tic"]).tic.astype(int))
        except Exception: pass
    cache = os.path.join(a.data_dir, "lc_cache"); os.makedirs(cache, exist_ok=True)
    jobs = [(int(r.ID), fmap.get(int(r.ID), []), cache, a.keep, maskmap.get(int(r.ID), [])) for r in targets.itertuples() if int(r.ID) not in done]
    print(f"{len(jobs)} stars to search ({len(done)} already done)", flush=True)
    from multiprocessing import Pool
    first = len(done) == 0
    with Pool(a.workers) as pool, open(a.out, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(_worker, jobs, chunksize=1)):
            df = pd.DataFrame([r]).reindex(columns=COLS)
            df.to_csv(fh, header=first, index=False); first = False; fh.flush()
            if i % 10 == 0:
                print(i, r.get("tic"), r.get("status"), "snr", r.get("snr"), "P", r.get("P"), "bsde", r.get("best_block_sde"), r.get("runtime_s"), "s", flush=True)


if __name__ == "__main__":
    main()
