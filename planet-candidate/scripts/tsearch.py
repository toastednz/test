#!/usr/bin/env python3
"""Transit search core: download TESS 2-min SPOC light curves, detrend, BLS sweep.

Usage (batch):  tsearch.py DATA_DIR TARGET_CSV OUT_CSV [--workers N] [--limit N] [--keep]
TARGET_CSV must have columns ID, sectors (comma list).  Results appended to OUT_CSV (one row/star).
"""
import os, sys, re, glob, time, json, argparse, warnings, traceback
import numpy as np
import pandas as pd
import requests
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
from astropy.stats import sigma_clip

warnings.filterwarnings("ignore")
MAST = "https://mast.stsci.edu/api/v0.1/Download/file/?uri=mast:TESS/product/"
# lightkurve default quality bitmask (AttitudeTweak|SafeMode|CoarsePoint|EarthPoint|Desat|ManualExclude|ImpulsiveOutlier|...)
DEFAULT_BITMASK = 1 | 2 | 4 | 8 | 32 | 128 | 1024 | 2048 | 8192 | 32768 | 65536
DURATIONS_H = np.array([0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0])


def build_filemap(data_dir):
    """TIC -> list of (sector, filename) from MAST bulk-download scripts."""
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
        q = d["QUALITY"]
        sec = h[0].header.get("SECTOR", -1)
    m = np.isfinite(t) & np.isfinite(f) & np.isfinite(e) & ((q & DEFAULT_BITMASK) == 0)
    t, f, e = t[m], f[m], e[m]
    if len(t) < 500:
        return None
    med = np.nanmedian(f)
    return t, f / med, e / med, np.full(len(t), sec)


def detrend(t, f, e, window=0.6):
    from wotan import flatten
    flat, trend = flatten(t, f, method="biweight", window_length=window, edge_cutoff=0.1,
                          break_tolerance=0.3, return_trend=True)
    m = np.isfinite(flat)
    t, flat, e = t[m], flat[m], e[m] / trend[m]
    # clip positive outliers (flares) only
    resid = flat - 1.0
    mad = np.nanmedian(np.abs(resid - np.nanmedian(resid))) * 1.4826
    keep = resid < 3.0 * mad
    return t[keep], flat[keep], e[keep], mad


def bin_lc(t, f, e, dt=10.0 / 1440.0):
    idx = np.floor((t - t[0]) / dt).astype(int)
    uniq, inv, cnt = np.unique(idx, return_inverse=True, return_counts=True)
    tb = np.bincount(inv, weights=t) / cnt
    fb = np.bincount(inv, weights=f) / cnt
    eb = np.sqrt(np.bincount(inv, weights=e ** 2)) / cnt
    return tb, fb, eb


def period_grid(baseline, pmin=0.5, pmax=None, oversample=3.0, dur1=0.045):
    """Ofir-style grid: df = dur(P)/ (oversample*baseline), dur ∝ P^(1/3) with dur(1 d)=dur1 (days)."""
    if pmax is None:
        pmax = baseline / 2.0
    fmax, fmin = 1.0 / pmin, 1.0 / pmax
    A = dur1 / (oversample * baseline)   # df = A * f^(2/3)
    # integrate: d(3 f^(1/3)) = f^(-2/3) df  -> uniform in u = 3 f^(1/3) with step A
    u0, u1 = 3 * fmin ** (1 / 3), 3 * fmax ** (1 / 3)
    n = int(np.ceil((u1 - u0) / A))
    u = np.linspace(u0, u1, n)
    f = (u / 3) ** 3
    return 1.0 / f[::-1]


def count_transits(t, P, t0, dur):
    n = np.round((t - t0) / P)
    intr = np.abs(t - (t0 + n * P)) < 0.5 * dur
    return len(np.unique(n[intr]))


def search_star(tic, files, cache_dir, keep=False, pmax_cap=None):
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
    t = np.concatenate([p[0] for p in parts]); f = np.concatenate([p[1] for p in parts])
    e = np.concatenate([p[2] for p in parts]); s = np.concatenate([p[3] for p in parts])
    o = np.argsort(t); t, f, e, s = t[o], f[o], e[o], s[o]
    nsec = len(np.unique(s))
    t, f, e, mad = detrend(t, f, e)
    tb, fb, eb = bin_lc(t, f, e)
    baseline = tb[-1] - tb[0]
    pmax = baseline / 2.0
    if pmax_cap is not None:
        pmax = min(pmax, pmax_cap)
    pmax = max(pmax, 1.0)
    periods = period_grid(baseline, 0.5, pmax)
    durs = DURATIONS_H / 24.0
    durs = durs[durs < 0.5 * 0.8]
    bls = BoxLeastSquares(tb, fb, dy=eb)
    res = bls.power(periods, durs, objective="snr", method="fast")
    pw = np.asarray(res.power)
    # SDE from the SNR periodogram, after removing slow trend in period
    pw_med = pd.Series(pw).rolling(2001, center=True, min_periods=50).median().values
    resid_pw = pw - pw_med
    sde_all = resid_pw / np.nanstd(resid_pw)
    out = dict(tic=tic, status="ok", nsec=nsec, npts2min=len(t), npts=len(tb), baseline=round(baseline, 2),
               rms_ppm=round(1e6 * np.nanstd(fb), 1), mad2min_ppm=round(1e6 * mad, 1), nperiods=len(periods),
               pmax=round(pmax, 2))
    # top 3 distinct peaks (separated by >2% in period)
    order = np.argsort(pw)[::-1]
    picked = []
    for i in order:
        P = periods[i]
        if all(abs(P / q - 1) > 0.02 and abs(P / q - 2) > 0.02 and abs(P / q - 0.5) > 0.01 for q in picked):
            picked.append(P)
            k = len(picked)
            st = bls.compute_stats(P, res.duration[i], res.transit_time[i])
            ntr = count_transits(tb, P, res.transit_time[i], res.duration[i])
            odd, even = st["depth_odd"], st["depth_even"]
            oe_sig = abs(odd[0] - even[0]) / np.sqrt(odd[1] ** 2 + even[1] ** 2 + 1e-30)
            out.update({f"P{k}": round(P, 6), f"t0_{k}": round(res.transit_time[i], 5), f"dur{k}_h": round(res.duration[i] * 24, 3),
                        f"depth{k}_ppm": round(1e6 * res.depth[i], 1), f"snr{k}": round(float(pw[i]), 2),
                        f"sde{k}": round(float(sde_all[i]), 2), f"ntr{k}": int(ntr),
                        f"oe{k}": round(float(oe_sig), 2),
                        f"sec_depth{k}_ppm": round(1e6 * float(st["depth_phased"][0]), 1),
                        f"sec_sig{k}": round(float(st["depth_phased"][0] / (st["depth_phased"][1] + 1e-30)), 2)})
        if len(picked) >= 3:
            break
    out["runtime_s"] = round(time.time() - t0w, 1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir"); ap.add_argument("targets"); ap.add_argument("out")
    ap.add_argument("--workers", type=int, default=4); ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--keep", action="store_true"); ap.add_argument("--pmax", type=float, default=None)
    a = ap.parse_args()
    fmap = build_filemap(a.data_dir)
    targets = pd.read_csv(a.targets)
    if a.limit:
        targets = targets.head(a.limit)
    done = set()
    if os.path.exists(a.out):
        try: done = set(pd.read_csv(a.out).tic.astype(int))
        except Exception: pass
    cache = os.path.join(a.data_dir, "lc_cache"); os.makedirs(cache, exist_ok=True)
    jobs = [(int(r.ID), fmap.get(int(r.ID), []), cache, a.keep, a.pmax) for r in targets.itertuples() if int(r.ID) not in done]
    print(f"{len(jobs)} stars to search ({len(done)} already done)", flush=True)
    from multiprocessing import Pool
    first = not os.path.exists(a.out) or os.path.getsize(a.out) == 0
    with Pool(a.workers) as pool, open(a.out, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(_worker, jobs)):
            df = pd.DataFrame([r])
            df.to_csv(fh, header=first, index=False); first = False; fh.flush()
            if i % 10 == 0:
                print(i, r.get("tic"), r.get("status"), r.get("snr1"), r.get("sde1"), r.get("runtime_s"), flush=True)


def _worker(args):
    tic, files, cache, keep, pmax = args
    try:
        return search_star(tic, files, cache, keep, pmax)
    except Exception as ex:
        return dict(tic=tic, status="error:" + repr(ex)[:200])


if __name__ == "__main__":
    main()
