#!/usr/bin/env python3
"""Extend a candidate's baseline with QLP / TESS-SPOC full-frame-image light curves from MAST and
re-measure the signal: per-sector depth at the candidate ephemeris, combined SNR, and a local BLS.

Usage: 10_ffi_extend.py DATA_DIR CAND_CSV OUT_JSON    (CAND_CSV columns: tic,P,t0,dur_h)
"""
import os, sys, json, warnings
import numpy as np, pandas as pd, lightkurve as lk
from astropy.timeseries import BoxLeastSquares
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import tsearch2 as ts
warnings.filterwarnings("ignore")
DATA, CAND, OUT = sys.argv[1:4]
cands = pd.read_csv(CAND); res = {}
for r in cands.itertuples():
    tic, P, t0, dur = int(r.tic), float(r.P), float(r.t0), float(r.dur_h) / 24
    try:
        sr = lk.search_lightcurve(f"TIC {tic}")
    except Exception as ex:
        res[tic] = {"error": repr(ex)[:200]}; continue
    tab = sr.table.to_pandas()
    authors = tab.author.value_counts().to_dict()
    sec_spoc = sorted(set(int(str(m).split()[-1]) for m, a in zip(tab.mission, tab.author) if a == "SPOC"))
    sec_ffi = sorted(set(int(str(m).split()[-1]) for m, a in zip(tab.mission, tab.author) if a in ("QLP", "TESS-SPOC")))
    new_secs = [s for s in sec_ffi if s not in sec_spoc]
    out = dict(P=P, t0=t0, dur_h=dur * 24, authors=authors, sectors_2min=sec_spoc, sectors_ffi=sec_ffi, ffi_only_sectors=new_secs, per_sector={})
    T, F, E = [], [], []
    try:
        sel = sr[(sr.author == "QLP") | (sr.author == "TESS-SPOC")]
        lcs = sel.download_all(download_dir=os.path.join(DATA, "hlsp_ext"))
    except Exception as ex:
        res[tic] = dict(out, error=repr(ex)[:200]); continue
    for lc in lcs or []:
        try:
            sec = int(lc.meta["SECTOR"]); auth = lc.meta.get("AUTHOR", "")
            lc = lc.remove_nans(); col = "det_flux" if "det_flux" in lc.columns else ("kspsap_flux" if "kspsap_flux" in lc.columns else ("pdcsap_flux" if "pdcsap_flux" in lc.columns else "flux"))
            t = lc.time.value; f = np.asarray(lc[col].value, float); q = np.asarray(lc["quality"].value) if "quality" in lc.columns else np.zeros(len(t), int)
            m = np.isfinite(t) & np.isfinite(f) & (q == 0); t, f = t[m], f[m] / np.nanmedian(f[m])
            if len(t) < 200: continue
            t2, f2, e2, mad = ts.detrend(t, f, np.full(len(t), np.nanstd(f)), window=max(0.6, 3 * dur))
            n = np.round((t2 - t0) / P); ph = t2 - (t0 + n * P); intr = np.abs(ph) < 0.5 * dur; oot = (np.abs(ph) > 0.75 * dur) & (np.abs(ph) < 3 * dur)
            if intr.sum() < 3: continue
            d = 1e6 * (np.median(f2[oot]) - np.median(f2[intr])); err = 1e6 * 1.2533 * np.std(f2[oot]) / np.sqrt(intr.sum())
            out["per_sector"][f"S{sec}_{auth}"] = dict(cadence_min=round(float(np.median(np.diff(t)) * 1440), 1), npts=int(len(t2)), rms_ppm=round(1e6 * mad), n_in=int(intr.sum()), n_transits=int(len(np.unique(n[intr]))), depth_ppm=round(d), err_ppm=round(err), snr=round(d / err, 1))
            if sec not in sec_spoc:
                T.append(t2); F.append(f2); E.append(e2)
        except Exception as ex:
            out["per_sector"][f"err_{len(out['per_sector'])}"] = repr(ex)[:120]
    if T:
        t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); o = np.argsort(t); t, f, e = t[o], f[o], e[o]
        n = np.round((t - t0) / P); ph = t - (t0 + n * P); intr = np.abs(ph) < 0.5 * dur; oot = (np.abs(ph) > 0.75 * dur) & (np.abs(ph) < 3 * dur)
        d = 1e6 * (np.median(f[oot]) - np.median(f[intr])); err = 1e6 * 1.2533 * np.std(f[oot]) / np.sqrt(max(intr.sum(), 1))
        out["ffi_only_combined"] = dict(npts=int(len(t)), n_transits=int(len(np.unique(n[intr]))), depth_ppm=round(d), err_ppm=round(err), snr=round(d / err, 1))
        # local BLS in FFI-only data around P (+-2%) to see if an independent detection exists
        bls = BoxLeastSquares(t, f, dy=e); grid = np.linspace(P * 0.98, P * 1.02, 3000)
        rr = bls.power(grid, [dur * 0.7, dur, dur * 1.3], objective="snr"); i = int(np.argmax(rr.power))
        out["ffi_only_local_bls"] = dict(P=round(float(grid[i]), 5), snr=round(float(rr.power[i]), 1), depth_ppm=round(1e6 * float(rr.depth[i])))
    res[tic] = out
    print(tic, json.dumps({k: v for k, v in out.items() if k in ("sectors_2min", "ffi_only_sectors", "ffi_only_combined", "ffi_only_local_bls")}), flush=True)
json.dump(res, open(OUT, "w"), indent=1)
