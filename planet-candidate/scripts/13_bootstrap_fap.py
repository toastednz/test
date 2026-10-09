#!/usr/bin/env python3
"""Empirical false-alarm test for a candidate: repeat the fully coherent BLS on light curves whose
sectors are circularly shifted by random offsets (destroying any coherent periodic signal while
keeping the noise properties), and record the maximum SDE of each trial.

Usage: 13_bootstrap_fap.py DATA_DIR TIC P_CAND OUT_JSON [--ntrials N] [--mask spec] [--pmin] [--pmax]
"""
import os, sys, json, argparse, warnings
import numpy as np
from astropy.timeseries import BoxLeastSquares
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tsearch2 as ts
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("data_dir"); ap.add_argument("tic", type=int); ap.add_argument("P", type=float); ap.add_argument("out")
ap.add_argument("--ntrials", type=int, default=8); ap.add_argument("--mask", default=""); ap.add_argument("--pmin", type=float, default=0.5); ap.add_argument("--pmax", type=float, default=70.0); ap.add_argument("--workers", type=int, default=3)
a = ap.parse_args()
fmap = ts.build_filemap(a.data_dir); cache = os.path.join(a.data_dir, "lc_cache")
SEC = []
for sec, fname in sorted(fmap.get(a.tic, [])):
    p = ts.download(fname, cache); r = ts.load_sector(p) if p else None
    if r is None: continue
    t, f, e, s = r; t, f, e = ts.bin_lc(t, f, e); t, f, e, mad = ts.detrend(t, f, e)
    for spec in [x for x in a.mask.split(";") if x]:
        Pm, t0m, dm = [float(v) for v in spec.split(":")]; phm = ((t - t0m + 0.5 * Pm) % Pm) - 0.5 * Pm; keep = np.abs(phm) > max(dm / 24, 0.06); t, f, e = t[keep], f[keep], e[keep]
    SEC.append((t, f, e))
t_all = np.concatenate([x[0] for x in SEC]); baseline = t_all.max() - t_all.min()
periods = ts.period_grid(baseline, a.pmin, min(a.pmax, baseline / 2), oversample=2.0)
durs = np.array([0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]) / 24
def run(seed):
    rng = np.random.default_rng(seed); T, F, E = [], [], []
    for t, f, e in SEC:
        if seed >= 0:   # circular shift of the flux within the sector (keeps noise, destroys coherence)
            k = rng.integers(len(f) // 10, len(f) - len(f) // 10); f = np.roll(f, k); e = np.roll(e, k)
        T.append(t); F.append(f); E.append(e)
    t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); o = np.argsort(t); t, f, e = t[o], f[o], e[o]
    bls = BoxLeastSquares(t, f, dy=e); res = bls.power(periods, durs, objective="snr", method="fast", oversample=4); pw = np.asarray(res.power)
    sde = (pw - np.nanmean(pw)) / np.nanstd(pw); i = int(np.nanargmax(pw))
    win = np.abs(periods / a.P - 1) < 0.01; ic = int(np.argmax(np.where(win, pw, -np.inf)))
    return dict(seed=int(seed), max_sde=float(sde[i]), max_P=float(periods[i]), cand_sde=float(sde[ic]))
with Pool(a.workers) as pool:
    res = pool.map(run, [-1] + list(range(a.ntrials)))
real = res[0]; trials = res[1:]
out = dict(tic=a.tic, P=a.P, nperiods=len(periods), baseline=float(baseline), real=real, trials=trials,
           n_trials=len(trials), max_trial_sde=max(x["max_sde"] for x in trials), n_trials_exceeding_real=sum(1 for x in trials if x["max_sde"] >= real["cand_sde"]))
json.dump(out, open(a.out, "w"), indent=1); print(json.dumps({k: v for k, v in out.items() if k != "trials"}, indent=1)); print("trial max SDEs:", [round(x["max_sde"], 1) for x in trials])
