#!/usr/bin/env python3
"""Fully coherent multi-sector BLS periodogram for one star, to measure how significant a candidate
period is against the whole periodogram (SDE) and whether it is the global maximum.

Usage: 08_fullbls.py DATA_DIR TIC P_CAND OUTDIR [--pmin 1] [--pmax 70]
"""
import os, sys, json, argparse, warnings
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from astropy.timeseries import BoxLeastSquares
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tsearch2 as ts
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser()
ap.add_argument("data_dir"); ap.add_argument("tic", type=int); ap.add_argument("P", type=float); ap.add_argument("outdir")
ap.add_argument("--pmin", type=float, default=1.0); ap.add_argument("--pmax", type=float, default=70.0); ap.add_argument("--oversample", type=float, default=2.0)
a = ap.parse_args(); os.makedirs(a.outdir, exist_ok=True)
cache = os.path.join(a.data_dir, "lc_cache"); os.makedirs(cache, exist_ok=True)
fmap = ts.build_filemap(a.data_dir)
T, F, E = [], [], []
for sec, fname in sorted(fmap.get(a.tic, [])):
    p = ts.download(fname, cache)
    if p is None: continue
    r = ts.load_sector(p)
    if r is None: continue
    t, f, e, s = r
    t, f, e = ts.bin_lc(t, f, e)
    t, f, e, mad = ts.detrend(t, f, e)
    T.append(t); F.append(f); E.append(e)
t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); o = np.argsort(t); t, f, e = t[o], f[o], e[o]
baseline = t[-1] - t[0]
periods = ts.period_grid(baseline, a.pmin, min(a.pmax, baseline / 2), oversample=a.oversample)
durs = np.array([0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]) / 24
bls = BoxLeastSquares(t, f, dy=e)
res = bls.power(periods, durs, objective="snr", method="fast", oversample=4)
pw = np.asarray(res.power)
mean, std = np.nanmean(pw), np.nanstd(pw)
sde = (pw - mean) / std
i_best = int(np.nanargmax(pw))
# candidate peak: max within +-1% of P
win = np.abs(periods / a.P - 1) < 0.01
i_c = int(np.argmax(np.where(win, pw, -np.inf)))
# distinct top peaks
order = np.argsort(pw)[::-1]; peaks = []
for i in order:
    if all(abs(periods[i] / q - 1) > 0.02 for q, _, _ in peaks):
        peaks.append((float(periods[i]), float(pw[i]), float(sde[i])))
    if len(peaks) >= 8: break
rank = 1 + sum(1 for q, s_, _ in peaks if s_ > pw[i_c] and abs(q / periods[i_c] - 1) > 0.02)
out = dict(tic=a.tic, P_cand=a.P, npts=len(t), baseline=float(baseline), nperiods=len(periods), pmin=a.pmin, pmax=float(periods.max()),
           cand_P=float(periods[i_c]), cand_snr=float(pw[i_c]), cand_sde=float(sde[i_c]), cand_is_global_max=bool(abs(periods[i_c] / periods[i_best] - 1) < 0.02),
           cand_rank=rank, global_P=float(periods[i_best]), global_snr=float(pw[i_best]), global_sde=float(sde[i_best]), top_peaks=peaks,
           cand_depth_ppm=float(1e6 * res.depth[i_c]), cand_dur_h=float(24 * res.duration[i_c]), cand_t0=float(res.transit_time[i_c]))
json.dump(out, open(os.path.join(a.outdir, "fullbls.json"), "w"), indent=1)
fig, ax = plt.subplots(2, 1, figsize=(13, 7))
ax[0].plot(periods, sde, lw=0.4, color="0.3"); ax[0].axvline(a.P, color="r", lw=1, alpha=0.6); ax[0].set_xscale("log"); ax[0].set_xlabel("period [d]"); ax[0].set_ylabel("SDE (SNR periodogram)")
ax[0].set_title(f"TIC {a.tic}: coherent BLS over {baseline:.0f} d, {len(periods)} periods. candidate P={a.P:.4f}: SDE={out['cand_sde']:.1f}, rank {rank}; global max P={out['global_P']:.4f} SDE={out['global_sde']:.1f}")
m = np.abs(periods / a.P - 1) < 0.03; ax[1].plot(periods[m], sde[m], lw=0.6); ax[1].axvline(a.P, color="r", lw=1, alpha=0.6); ax[1].set_xlabel("period [d] (zoom)"); ax[1].set_ylabel("SDE")
plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "fullbls.png"), dpi=110)
print(json.dumps({k: v for k, v in out.items() if k != "top_peaks"}, indent=1)); print("top peaks:", [(round(p, 4), round(s, 1), round(d, 1)) for p, s, d in peaks])
