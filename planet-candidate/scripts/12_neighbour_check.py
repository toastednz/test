#!/usr/bin/env python3
"""For centroid-offset TCEs, test the proposed neighbour host with its OWN light curves: fold every
available light curve (SPOC 2-min, QLP, TESS-SPOC) of both the target and the neighbour at the TCE
ephemeris; measure depth, odd/even and secondary on each. If the neighbour hosts the signal its depth
must be larger than the target's by ~1/flux_fraction.

Usage: 12_neighbour_check.py DATA_DIR CAND_CSV OUT_JSON [--n N]
"""
import os, sys, json, argparse, warnings
import numpy as np, pandas as pd, lightkurve as lk
from astropy.timeseries import BoxLeastSquares
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tsearch2 as ts
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("data_dir"); ap.add_argument("cands"); ap.add_argument("out"); ap.add_argument("--n", type=int, default=22); a = ap.parse_args()
c = pd.read_csv(a.cands)
good = c[(~c.nb_is_toi_ctoi) & (c.nb_claimed_within_1arcmin == 0) & (c.rp_on_nb_re < 12) & (c.nb_lumclass != "GIANT")].sort_values("snr", ascending=False).head(a.n)
HL = os.path.join(a.data_dir, "hlsp_nb"); os.makedirs(HL, exist_ok=True)
def measure(tic, P, t0, dur):
    out = {}
    try:
        sr = lk.search_lightcurve(f"TIC {tic}")
        sr = sr[np.isin(sr.author, ["SPOC", "QLP", "TESS-SPOC"])]
        lcs = sr.download_all(download_dir=HL)
    except Exception as ex:
        return {"error": repr(ex)[:150]}
    T, F, E = [], [], []
    for lc in lcs or []:
        try:
            sec = int(lc.meta["SECTOR"]); auth = lc.meta.get("AUTHOR", ""); lc = lc.remove_nans()
            col = "pdcsap_flux" if "pdcsap_flux" in lc.columns else ("det_flux" if "det_flux" in lc.columns else ("kspsap_flux" if "kspsap_flux" in lc.columns else "flux"))
            t = lc.time.value; f = np.asarray(lc[col].value, float); q = np.asarray(lc["quality"].value) if "quality" in lc.columns else np.zeros(len(t), int)
            m = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[m], f[m] / np.nanmedian(f[m])
            if len(t) < 200: continue
            t2, f2, e2, mad = ts.detrend(t, f, np.full(len(t), np.nanstd(f)), window=max(0.6, 3 * dur))
            T.append(t2); F.append(f2); E.append(e2)
        except Exception:
            pass
    if not T: return {"error": "no light curves"}
    t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); o = np.argsort(t); t, f, e = t[o], f[o], e[o]
    # refine P/t0 locally (ephemeris drift over years)
    bls = BoxLeastSquares(t, f, dy=e); bl = t[-1] - t[0]; halfw = max(0.002 * P, 3 * dur * P / 27); dP = dur * P / (4 * bl)
    grid = np.linspace(P - halfw, P + halfw, min(int(2 * halfw / dP) + 1, 20000)); r = bls.power(grid, [dur * 0.7, dur, dur * 1.4], objective="snr"); i = int(np.argmax(r.power))
    Pb, t0b, durb = float(grid[i]), float(r.transit_time[i]), float(r.duration[i]); st = bls.compute_stats(Pb, durb, t0b)
    n = np.round((t - t0b) / Pb); ph = t - (t0b + n * Pb); intr = np.abs(ph) < 0.5 * durb
    return dict(nsec=len(T), npts=int(len(t)), rms_ppm=round(1e6 * np.std(f)), P=round(Pb, 6), t0=round(t0b, 4), dur_h=round(24 * durb, 2), snr=round(float(r.power[i]), 1),
                depth_ppm=round(1e6 * float(r.depth[i])), depth_err=round(1e6 * float(r.depth_err[i])), odd=round(1e6 * st["depth_odd"][0]), odd_err=round(1e6 * st["depth_odd"][1]),
                even=round(1e6 * st["depth_even"][0]), even_err=round(1e6 * st["depth_even"][1]), sec=round(1e6 * st["depth_phased"][0]), sec_err=round(1e6 * st["depth_phased"][1]), n_transits=int(len(np.unique(n[intr]))))
res = {}
for r in good.itertuples():
    P, t0, dur = float(r.P), float(r.t0), float(r.dur_h) / 24
    tg = measure(int(r.tic), P, t0, dur); nb = measure(int(r.nb_tic), P, t0, dur)
    ratio = (nb.get("depth_ppm", np.nan) / tg["depth_ppm"]) if tg.get("depth_ppm") else np.nan
    res[f"{r.tic}->{r.nb_tic}"] = dict(tce=dict(P=P, t0=t0, depth_ppm=r.depth_ppm, snr=r.snr, offset_arcsec=r.offset_arcsec, offset_sig=r.offset_sig, nb_flux_frac=r.nb_flux_frac, expected_ratio=round(1 / max(r.nb_flux_frac, 1e-3), 1), rp_on_nb_re=r.rp_on_nb_re, nb_Tmag=r.nb_Tmag, nb_Teff=r.nb_Teff, nb_rad=r.nb_rad, nb_d_pc=r.nb_d_pc),
                                       target=tg, neighbour=nb, depth_ratio_nb_over_tgt=round(ratio, 2) if np.isfinite(ratio) else None)
    print(f"{r.tic}->{r.nb_tic} P={P:.4f}: target depth {tg.get('depth_ppm')}±{tg.get('depth_err')} (snr {tg.get('snr')}, {tg.get('nsec')} lcs) | neighbour depth {nb.get('depth_ppm')}±{nb.get('depth_err')} (snr {nb.get('snr')}, {nb.get('nsec')} lcs, odd/even {nb.get('odd')}/{nb.get('even')}, sec {nb.get('sec')}±{nb.get('sec_err')}) | ratio {res[f'{r.tic}->{r.nb_tic}']['depth_ratio_nb_over_tgt']} expected ~{round(1 / max(r.nb_flux_frac, 1e-3), 1)}", flush=True)
    json.dump(res, open(a.out, "w"), indent=1, default=float)
