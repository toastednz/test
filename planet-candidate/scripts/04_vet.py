#!/usr/bin/env python3
"""Vet one candidate: TLS fit on 2-min data near the BLS period, diagnostics and figures.

Usage: 04_vet.py DATA_DIR TIC P T0 DUR_H OUTDIR [--window 0.6] [--tls]
"""
import os, sys, json, argparse, warnings
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tsearch2 as ts
from astropy.timeseries import BoxLeastSquares
warnings.filterwarnings("ignore")

ap = argparse.ArgumentParser()
ap.add_argument("data_dir"); ap.add_argument("tic", type=int); ap.add_argument("P", type=float); ap.add_argument("t0", type=float)
ap.add_argument("dur_h", type=float); ap.add_argument("outdir"); ap.add_argument("--window", type=float, default=0.6)
ap.add_argument("--tls", action="store_true"); ap.add_argument("--mask", default="", help="P:t0:dur_h of other signals to mask, ;-separated")
a = ap.parse_args()
os.makedirs(a.outdir, exist_ok=True)
cache = os.path.join(a.data_dir, "lc_cache"); os.makedirs(cache, exist_ok=True)
fmap = ts.build_filemap(a.data_dir)
files = fmap.get(a.tic, [])
raw, det, sapd = [], [], []
for sec, fname in sorted(files):
    p = ts.download(fname, cache)
    if p is None: continue
    r = ts.load_sector(p)
    if r is None: continue
    t, f, e, s = r
    raw.append((t, f, e, s))
    try:   # raw SAP flux and background, for the PDC-artifact check
        from astropy.io import fits as _fits
        with _fits.open(p, memmap=False) as h:
            d_ = h[1].data; tt_ = d_["TIME"].astype(float); sap_ = d_["SAP_FLUX"].astype(float); bkg_ = d_["SAP_BKG"].astype(float); q_ = d_["QUALITY"]
        m_ = np.isfinite(tt_) & np.isfinite(sap_) & ((q_ & ts.DEFAULT_BITMASK) == 0)
        sapd.append((tt_[m_], sap_[m_] / np.nanmedian(sap_[m_]), bkg_[m_], s))
    except Exception:
        pass
    td, fd, ed, mad = ts.detrend(t, f, e, window=a.window)
    det.append((td, fd, ed, np.full(len(td), s)))
t = np.concatenate([d[0] for d in det]); f = np.concatenate([d[1] for d in det]); e = np.concatenate([d[2] for d in det]); s = np.concatenate([d[3] for d in det])
o = np.argsort(t); t, f, e, s = t[o], f[o], e[o], s[o]
for spec in [x for x in a.mask.split(";") if x]:
    Pm, t0m, dm = [float(v) for v in spec.split(":")]
    ph = ((t - t0m + 0.5 * Pm) % Pm) - 0.5 * Pm
    keep = np.abs(ph) > 1.0 * dm / 24
    t, f, e, s = t[keep], f[keep], e[keep], s[keep]
P, t0, dur = a.P, a.t0, a.dur_h / 24
# refine t0/P with BLS on 2-min data in a narrow window
bls = BoxLeastSquares(t, f, dy=e)
baseline = t[-1] - t[0]
halfw = max(3 * dur * P / 27.0, 0.003 * P); dP = dur * P / (4.0 * baseline)
grid = np.linspace(P - halfw, P + halfw, min(int(2 * halfw / dP) + 1, 40000))
durs = np.clip(dur * np.array([0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0]), 0.5 / 24, 8 / 24)
res = bls.power(grid, durs, objective="snr", method="fast"); i = int(np.argmax(res.power))
P, t0, dur, depth, snr = float(grid[i]), float(res.transit_time[i]), float(res.duration[i]), float(res.depth[i]), float(res.power[i])
st = bls.compute_stats(P, dur, t0)
summary = dict(tic=a.tic, P=P, t0=t0, dur_h=dur * 24, depth_ppm=1e6 * depth, depth_err_ppm=1e6 * float(res.depth_err[i]), bls_snr=snr,
               depth_odd_ppm=1e6 * st["depth_odd"][0], depth_odd_err=1e6 * st["depth_odd"][1], depth_even_ppm=1e6 * st["depth_even"][0],
               depth_even_err=1e6 * st["depth_even"][1], depth_half_ppm=1e6 * st["depth_half"][0], depth_half_err=1e6 * st["depth_half"][1],
               depth_phased_ppm=1e6 * st["depth_phased"][0], depth_phased_err=1e6 * st["depth_phased"][1],
               harmonic_delta_log_likelihood=float(st["harmonic_delta_log_likelihood"]), npts=len(t), nsec=len(np.unique(s)), baseline=baseline)
# per-transit stats
n = np.round((t - t0) / P); ph = t - (t0 + n * P); intr = np.abs(ph) < 0.5 * dur
per = []
for k in np.unique(n[intr]):
    m = intr & (n == k); win = (np.abs(ph) < 3 * dur) & (n == k) & ~intr
    if m.sum() < 5 or win.sum() < 10: continue
    d = 1e6 * (np.mean(f[win]) - np.mean(f[m])); err = 1e6 * np.std(f[win]) / np.sqrt(m.sum())
    per.append(dict(epoch=int(k), time=float(t0 + k * P), sector=int(np.median(s[m])), depth_ppm=round(d, 1), err_ppm=round(err, 1), snr=round(d / err, 2), nin=int(m.sum())))
# PDC-artifact check: depth in raw SAP flux at the same epochs, and background level in transit vs. sector median
if sapd:
    tS = np.concatenate([x[0] for x in sapd]); fS = np.concatenate([x[1] for x in sapd]); bS = np.concatenate([x[2] for x in sapd]); oS = np.argsort(tS); tS, fS, bS = tS[oS], fS[oS], bS[oS]
    tS2, fS2, _, _ = ts.detrend(tS, fS, np.full(len(tS), 1e-3), window=a.window)
    nS = np.round((tS2 - t0) / P); phS = tS2 - (t0 + nS * P); iS = np.abs(phS) < 0.5 * dur; oSo = (np.abs(phS) > 0.75 * dur) & (np.abs(phS) < 3 * dur)
    sap_depth = 1e6 * (np.median(fS2[oSo]) - np.median(fS2[iS])) if iS.sum() > 5 and oSo.sum() > 10 else np.nan
    sap_err = 1e6 * 1.2533 * np.std(fS2[oSo]) / np.sqrt(max(iS.sum(), 1)) if iS.sum() > 5 else np.nan
    nB = np.round((tS - t0) / P); phB = tS - (t0 + nB * P); iB = np.abs(phB) < 0.5 * dur
    summary["sap_depth_ppm"] = float(sap_depth); summary["sap_depth_err_ppm"] = float(sap_err)
    summary["sap_over_pdc_depth"] = float(sap_depth / depth / 1e6) if depth > 0 and np.isfinite(sap_depth) else None
    summary["bkg_in_transit_over_median"] = float(np.median(bS[iB]) / np.median(bS)) if iB.sum() > 5 else None
summary["per_transit"] = per
summary["n_transits"] = len(per); summary["n_transits_positive"] = sum(1 for p in per if p["depth_ppm"] > 0)
if per:
    dd = np.array([p["depth_ppm"] for p in per]); ee = np.array([p["err_ppm"] for p in per]); ss = dd / ee
    wmean = np.sum(dd / ee ** 2) / np.sum(1 / ee ** 2)
    summary["depth_wmean_ppm"] = float(wmean); summary["depth_wmean_err_ppm"] = float(1 / np.sqrt(np.sum(1 / ee ** 2)))
    summary["chi2_red_depths"] = float(np.sum((dd - wmean) ** 2 / ee ** 2) / max(len(dd) - 1, 1))
    summary["snr_combined"] = float(wmean / (1 / np.sqrt(np.sum(1 / ee ** 2))))
    k = int(np.argmax(ss)); keep = np.ones(len(dd), bool); keep[k] = False
    if keep.sum() > 0:
        w2 = np.sum(dd[keep] / ee[keep] ** 2) / np.sum(1 / ee[keep] ** 2); summary["snr_without_strongest"] = float(w2 * np.sqrt(np.sum(1 / ee[keep] ** 2)))
    else:
        summary["snr_without_strongest"] = 0.0
    summary["n_transits_snr_gt2"] = int(np.sum(ss > 2)); summary["max_single_snr"] = float(ss.max())
summary["sectors_with_transits"] = sorted(set(p["sector"] for p in per))
# TLS
if a.tls:
    from transitleastsquares import transitleastsquares
    from astroquery.mast import Catalogs
    try:
        cat = Catalogs.query_criteria(catalog="Tic", ID=a.tic).to_pandas().iloc[0]
        R, M = float(cat["rad"]), float(cat["mass"])
    except Exception:
        R, M = 0.4, 0.4
    # restrict to sectors containing transits if the baseline is long (keeps TLS tractable), wide period range for a meaningful SDE
    secs_tr = set(p["sector"] for p in per)
    mt = np.isin(s, list(secs_tr)) if baseline > 120 and secs_tr else np.ones(len(t), bool)
    tt_, ff_, ee_ = t[mt], f[mt], e[mt]
    bl_t = tt_[-1] - tt_[0]
    if bl_t < 120 and P < bl_t / 2:
        pmin_t, pmax_t = 0.5, min(bl_t / 2, 60.0)
    else:
        pmin_t, pmax_t = P * 0.99, P * 1.01
    model = transitleastsquares(tt_, ff_, ee_)
    tlsr = model.power(period_min=pmin_t, period_max=pmax_t, R_star=R, M_star=M, R_star_min=0.1, R_star_max=max(3.0, 2.0 * R_star), M_star_min=0.1, M_star_max=max(3.0, 2.0 * M_star),
                       oversampling_factor=5, duration_grid_step=1.05, use_threads=4, show_progress_bar=False)
    summary["tls"] = dict(P=float(tlsr.period), t0=float(tlsr.T0), SDE=float(tlsr.SDE), snr=float(tlsr.snr), depth=float(tlsr.depth),
                          rp_rs=float(tlsr.rp_rs), duration_h=float(tlsr.duration) * 24, odd_even_mismatch=float(tlsr.odd_even_mismatch),
                          transit_count=int(tlsr.transit_count), distinct_transit_count=int(tlsr.distinct_transit_count),
                          per_transit_depths=[float(x) for x in tlsr.transit_depths if np.isfinite(x)], R_star=R, M_star=M,
                          snr_per_transit=[float(x) for x in tlsr.snr_per_transit if np.isfinite(x)], period_range=[pmin_t, pmax_t], npts_used=int(mt.sum()),
                          tls_matches_bls=bool(abs(float(tlsr.period) / P - 1) < 0.01 or abs(float(tlsr.period) / P - 2) < 0.01 or abs(float(tlsr.period) / P - 0.5) < 0.01))
json.dump(summary, open(os.path.join(a.outdir, "summary.json"), "w"), indent=1, default=float)
# ---- figures
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
ax = axes[0, 0]
ax.plot(t, f, ".", ms=1, color="0.6"); tt = t0 + np.arange(np.floor((t[0] - t0) / P), np.ceil((t[-1] - t0) / P) + 1) * P
for x in tt: ax.axvline(x, color="r", lw=0.3, alpha=0.4)
ax.set_title(f"TIC {a.tic} detrended 2-min flux, transits marked"); ax.set_xlabel("BTJD")
def fold(t, P, t0): return ((t - t0 + 0.5 * P) % P) - 0.5 * P
ph = fold(t, P, t0); ax = axes[0, 1]; m = np.abs(ph) < 4 * dur
ax.plot(ph[m] * 24, f[m], ".", ms=1.5, color="0.6", alpha=0.5)
bins = np.linspace(-4 * dur, 4 * dur, 65); idx = np.digitize(ph[m], bins)
bx = [0.5 * (bins[i - 1] + bins[i]) * 24 for i in range(1, len(bins))]; by = [np.mean(f[m][idx == i]) if (idx == i).sum() > 0 else np.nan for i in range(1, len(bins))]
ax.plot(bx, by, "o-", color="C3", ms=3); ax.axvspan(-0.5 * dur * 24, 0.5 * dur * 24, color="C0", alpha=0.1)
ax.set_title(f"Phase fold P={P:.5f} d, depth={1e6*depth:.0f} ppm, SNR={snr:.1f}"); ax.set_xlabel("hours from mid-transit")
ax = axes[1, 0]
for lab, sel, col in [("odd", (n % 2 == 1), "C0"), ("even", (n % 2 == 0), "C1")]:
    mm = m & sel; idx2 = np.digitize(ph[mm], bins)
    by2 = [np.mean(f[mm][idx2 == i]) if (idx2 == i).sum() > 0 else np.nan for i in range(1, len(bins))]
    ax.plot(bx, by2, "o-", color=col, ms=3, label=lab)
ax.legend(); ax.set_title(f"odd {summary['depth_odd_ppm']:.0f}±{summary['depth_odd_err']:.0f} / even {summary['depth_even_ppm']:.0f}±{summary['depth_even_err']:.0f} ppm"); ax.set_xlabel("hours")
ax = axes[1, 1]; ph5 = fold(t, P, t0 + 0.5 * P); m5 = np.abs(ph5) < 4 * dur; idx5 = np.digitize(ph5[m5], bins)
by5 = [np.mean(f[m5][idx5 == i]) if (idx5 == i).sum() > 0 else np.nan for i in range(1, len(bins))]
ax.plot(ph5[m5] * 24, f[m5], ".", ms=1.5, color="0.6", alpha=0.5); ax.plot(bx, by5, "o-", color="C2", ms=3)
ax.set_title(f"Phase 0.5 (secondary): {summary['depth_phased_ppm']:.0f}±{summary['depth_phased_err']:.0f} ppm"); ax.set_xlabel("hours")
ax = axes[2, 0]
if per:
    ax.errorbar([p["epoch"] for p in per], [p["depth_ppm"] for p in per], yerr=[p["err_ppm"] for p in per], fmt="o", ms=4)
    ax.axhline(1e6 * depth, color="r", lw=1); ax.axhline(0, color="k", lw=0.5)
ax.set_title("per-transit depth (ppm) vs epoch"); ax.set_xlabel("epoch")
ax = axes[2, 1]
# full-range BLS periodogram for context (binned data)
tb, fb, eb = ts.bin_lc(t, f, e); pg = ts.period_grid(tb[-1] - tb[0], 0.5, min(60, (tb[-1] - tb[0]) / 2)) if False else None
ax.set_title("per-sector depth (ppm)")
if per:
    df = pd.DataFrame(per); g = df.groupby("sector").apply(lambda d: pd.Series(dict(depth=np.average(d.depth_ppm, weights=1 / d.err_ppm ** 2), err=1 / np.sqrt((1 / d.err_ppm ** 2).sum()), n=len(d))))
    ax.errorbar(g.index.astype(str), g.depth, yerr=g.err, fmt="s", ms=5); ax.axhline(1e6 * depth, color="r", lw=1); ax.axhline(0, color="k", lw=0.5)
    for i, (sec, row) in enumerate(g.iterrows()): ax.annotate(f"n={int(row.n)}", (i, row.depth), fontsize=7, xytext=(3, 3), textcoords="offset points")
ax.set_xlabel("sector")
plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "vetting.png"), dpi=110); plt.close()
# individual transit stamps
if per:
    npl = min(len(per), 24); ncol = 6; nrow = int(np.ceil(npl / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(3 * ncol, 2.4 * nrow), squeeze=False)
    for k, p in enumerate(per[:npl]):
        ax = axes[k // ncol, k % ncol]; mm = (n == p["epoch"]) & (np.abs(ph) < 3 * dur)
        ax.plot(ph[mm] * 24, f[mm], ".", ms=2, color="0.5")
        bb = np.linspace(-3 * dur, 3 * dur, 25); ii = np.digitize(ph[mm], bb)
        ax.plot([0.5 * (bb[j - 1] + bb[j]) * 24 for j in range(1, len(bb))], [np.mean(f[mm][ii == j]) if (ii == j).sum() else np.nan for j in range(1, len(bb))], "o-", color="C3", ms=3)
        ax.axvspan(-0.5 * dur * 24, 0.5 * dur * 24, color="C0", alpha=0.1); ax.set_title(f"S{p['sector']} ep{p['epoch']} {p['depth_ppm']:.0f}±{p['err_ppm']:.0f}", fontsize=8)
    plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "transits.png"), dpi=100); plt.close()
print(json.dumps({k: (v if k != "tls" else {kk: vv for kk, vv in v.items() if not isinstance(vv, list)}) for k, v in summary.items() if k != "per_transit"}, indent=1, default=float))
print("per-transit (sector, depth, snr):", [(p["sector"], round(p["depth_ppm"]), round(p["snr"], 1)) for p in per])
