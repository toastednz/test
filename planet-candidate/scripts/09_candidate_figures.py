#!/usr/bin/env python3
"""Final figures and TLS statistics for the TIC 404664386 / TIC 404664390 blended candidate.

Usage: 09_candidate_figures.py DATA_DIR OUTDIR
"""
import os, sys, json, glob, warnings
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import lightkurve as lk
from wotan import flatten
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tsearch2 as ts
warnings.filterwarnings("ignore")
DATA, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
P, t0, dur = 0.6532993, 4179.8715, 1.0 / 24
HL = os.path.join(DATA, "hlsp_404664390")

def load_qlp(tic):
    sr = lk.search_lightcurve(f"TIC {tic}", author="QLP"); lcs = sr.download_all(download_dir=HL); out = {}
    for lc in lcs:
        sec = int(lc.meta["SECTOR"]); lc = lc.remove_nans()
        col = "kspsap_flux" if "kspsap_flux" in lc.columns else "det_flux"
        t = lc.time.value; f = np.asarray(lc[col].value, float); q = np.asarray(lc["quality"].value)
        m = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[m], f[m] / np.nanmedian(f[m])
        t2, f2, e2, mad = ts.detrend(t, f, np.full(len(t), np.nanstd(f)), window=0.5)
        out[sec] = (t2, f2, e2, col, mad)
    return out
G = load_qlp(404664386); M = load_qlp(404664390)
# SPOC 2-min (M-dwarf aperture)
fm = ts.build_filemap(DATA); fn = [f for s, f in fm[404664390] if s == 104][0]; p = ts.download(fn, os.path.join(DATA, "lc_cache"))
t, f, e, s = ts.load_sector(p); tS, fS, eS, madS = ts.detrend(t, f, e, window=0.5)

def fold(t, f, P, t0):
    return ((t - t0 + 0.5 * P) % P) - 0.5 * P
def binned(ph, f, nb=60, w=0.5):
    bins = np.linspace(-w, w, nb + 1); idx = np.digitize(ph, bins)
    x = 0.5 * (bins[1:] + bins[:-1]); y = np.array([np.nanmedian(f[idx == i]) if (idx == i).sum() > 2 else np.nan for i in range(1, nb + 1)])
    ye = np.array([1.2533 * np.nanstd(f[idx == i]) / np.sqrt((idx == i).sum()) if (idx == i).sum() > 2 else np.nan for i in range(1, nb + 1)])
    return x, y, ye
stats = {}
fig, axes = plt.subplots(2, 3, figsize=(16, 8.5))
panels = [(axes[0, 0], G[13], "TIC 404664386 (G dwarf) QLP S13 2019, 30-min"), (axes[0, 1], G[94], "TIC 404664386 QLP S94 2025, 200-s"), (axes[0, 2], G[104], "TIC 404664386 QLP S104 2026, 200-s"),
          (axes[1, 0], M[13], "TIC 404664390 (M dwarf aperture) QLP S13"), (axes[1, 1], (tS, fS, eS, "SPOC PDCSAP 2-min", madS), "TIC 404664390 aperture, SPOC 2-min S104")]
for ax, (tt, ff, ee, col, mad), title in panels:
    ph = fold(tt, P, t0) * 24; m = np.abs(ph) < 6
    ax.plot(ph[m], ff[m], ".", ms=2, color="0.6", alpha=0.5)
    x, y, ye = binned(ph[m] / 24, ff[m], nb=48, w=0.25); ax.errorbar(x * 24, y, ye, fmt="o", color="C3", ms=3)
    bls = BoxLeastSquares(tt, ff, dy=ee); st = bls.compute_stats(P, dur, t0)
    d = 1e6 * st["depth"][0]; de = 1e6 * st["depth"][1]
    stats[title] = dict(column=col, depth_ppm=round(d), depth_err=round(de), odd=round(1e6 * st["depth_odd"][0]), odd_err=round(1e6 * st["depth_odd"][1]), even=round(1e6 * st["depth_even"][0]), even_err=round(1e6 * st["depth_even"][1]),
                        secondary=round(1e6 * st["depth_phased"][0]), secondary_err=round(1e6 * st["depth_phased"][1]), rms_ppm=round(1e6 * mad), npts=int(len(tt)))
    ax.set_title(f"{title}\ndepth {d:.0f}±{de:.0f} ppm ({col})", fontsize=9); ax.set_xlabel("hours from mid-transit"); ax.axvspan(-0.5 * dur * 24, 0.5 * dur * 24, color="C0", alpha=0.08)
# secondary eclipse panel, G dwarf S94+S104 combined
ax = axes[1, 2]; tt = np.concatenate([G[94][0], G[104][0]]); ff = np.concatenate([G[94][1], G[104][1]])
ph = fold(tt, P, t0 + 0.5 * P) * 24; m = np.abs(ph) < 6; ax.plot(ph[m], ff[m], ".", ms=2, color="0.6", alpha=0.5)
x, y, ye = binned(ph[m] / 24, ff[m], nb=48, w=0.25); ax.errorbar(x * 24, y, ye, fmt="o", color="C2", ms=3); ax.set_ylim(0.994, 1.006)
ax.set_title("TIC 404664386 QLP S94+S104 at phase 0.5 (secondary eclipse)", fontsize=9); ax.set_xlabel("hours from phase 0.5")
plt.tight_layout(); plt.savefig(os.path.join(OUT, "candidate_folds.png"), dpi=110); plt.close()
# TLS on the G dwarf QLP S94+S104 (wide range) for a proper SDE
from transitleastsquares import transitleastsquares
tt = np.concatenate([G[94][0], G[104][0]]); ff = np.concatenate([G[94][1], G[104][1]]); ee = np.concatenate([G[94][2], G[104][2]])
o = np.argsort(tt); tt, ff, ee = tt[o], ff[o], ee[o]
model = transitleastsquares(tt, ff, ee)
r = model.power(period_min=0.3, period_max=15, R_star=0.907, M_star=0.99, R_star_min=0.5, R_star_max=1.5, M_star_min=0.5, M_star_max=1.5, oversampling_factor=3, duration_grid_step=1.07, use_threads=4, show_progress_bar=False)
stats["tls_Gdwarf_S94_S104"] = dict(P=float(r.period), P_err=float(r.period_uncertainty), t0=float(r.T0), SDE=float(r.SDE), snr=float(r.snr), depth=float(r.depth), rp_rs=float(r.rp_rs), duration_h=24 * float(r.duration),
                                     odd_even_mismatch=float(r.odd_even_mismatch), transit_count=int(r.transit_count), distinct_transit_count=int(r.distinct_transit_count), FAP=float(r.FAP) if r.FAP is not None else None,
                                     rp_rearth=float(r.rp_rs) * 0.907 * 109.1, rp_rjup=float(r.rp_rs) * 0.907 * 109.1 / 11.21)
fig, ax = plt.subplots(2, 1, figsize=(12, 7))
ax[0].plot(r.periods, r.power, lw=0.5, color="0.3"); ax[0].axvline(P, color="r", alpha=0.5); ax[0].set_xscale("log"); ax[0].set_xlabel("period [d]"); ax[0].set_ylabel("TLS SDE"); ax[0].set_title(f"TIC 404664386 QLP S94+S104: TLS SDE={r.SDE:.1f} at P={r.period:.5f} d, rp/rs={r.rp_rs:.3f}, {r.distinct_transit_count} transits")
ax[1].plot(r.folded_phase, r.folded_y, ".", ms=2, color="0.6"); ax[1].plot(r.model_folded_phase, r.model_folded_model, color="r"); ax[1].set_xlim(0.45, 0.55); ax[1].set_xlabel("phase"); ax[1].set_ylabel("rel. flux")
plt.tight_layout(); plt.savefig(os.path.join(OUT, "candidate_tls.png"), dpi=110); plt.close()
# planet parameter estimates
R, Mst, T = 0.907, 0.99, 5612.0
a_rsun = 215.03 * (Mst * (P / 365.25) ** 2) ** (1 / 3); aR = a_rsun / R
stats["derived"] = dict(a_au=round(a_rsun / 215.03, 5), a_over_rstar=round(aR, 2), T_eq_K_full_redistribution=round(T * np.sqrt(1 / (2 * aR))), max_central_duration_h=round(24 * P / np.pi * (1 + float(r.rp_rs)) / aR, 2),
                        ellipsoidal_ppm_per_Mjup=round(1.5 * (1 / 1047.6) / Mst * (1 / aR) ** 3 * 1e6, 1))
json.dump(stats, open(os.path.join(OUT, "candidate_stats.json"), "w"), indent=1)
print(json.dumps(stats, indent=1))
