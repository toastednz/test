#!/usr/bin/env python3
"""Search TESS 2-min light curves for transits of known NON-transiting planets (RV, TTV, ... planets from the
NASA Exoplanet Archive) at their published periods.

For each planet: load every 2-min SPOC sector of the host (cached), 10-min bins, biweight detrend, mask the
transits of any known transiting sibling, then run a box search restricted to periods within max(3 sigma_P,
0.2%) of the published period, all epochs, durations 0.3-1.4 x the central-transit duration. Records the best
box (P, t0, depth, duration, SNR, number of transits), the periodogram SDE of that peak against a wide
0.5-100 d reference search, the expected depth from a mass-radius relation, the per-transit noise (hence the
expected SNR if the planet transited), and the predicted conjunction time and its uncertainty from
(P, T_peri, omega, e) when available, with the phase offset between the detected box and the prediction.

Usage: 22_rv_planet_transits.py DATA_DIR PLANETS_CSV OUT_CSV [--workers 3] [--only name1,name2]
"""
import os, sys, json, argparse, warnings, traceback
import numpy as np, pandas as pd
from astropy.timeseries import BoxLeastSquares
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tsearch2 as ts
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("data_dir"); ap.add_argument("planets"); ap.add_argument("out")
ap.add_argument("--workers", type=int, default=3); ap.add_argument("--only", default=""); ap.add_argument("--max-sectors", type=int, default=40); ap.add_argument("--rerun-errors", default="", help="previous results CSV: rerun only planets whose status is not ok")
a = ap.parse_args()
D = a.data_dir; cache = os.path.join(D, "lc_cache"); os.makedirs(cache, exist_ok=True)
pl = pd.read_csv(a.planets); pl = pl[pl.nsec_2min > 0].copy()
if a.only: pl = pl[pl.pl_name.isin(a.only.split(","))]
if a.rerun_errors:
    prev = pd.read_csv(a.rerun_errors); pl = pl[pl.pl_name.isin(prev[prev.status != "ok"].pl_name)]
try: sib = pd.read_csv(os.path.join(D, "catalogs", "rv_planets_transiting_siblings.csv"))
except Exception: sib = pd.DataFrame(columns=["hostname", "pl_orbper", "pl_tranmid", "pl_trandur"])
fmap = ts.build_filemap(D)

def baseline_guard(t):
    return (t.max() - t.min()) > 3.0
def conj_time(P, Tp, om_deg, e):
    """time of inferior conjunction from periastron time, argument of periastron (star's orbit, deg) and e"""
    if not (np.isfinite(Tp) and np.isfinite(om_deg)): return np.nan
    e = 0.0 if not np.isfinite(e) else float(e); om = np.radians(om_deg)
    nu = np.pi / 2 - om                     # true anomaly at inferior conjunction (planet in front)
    E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    M = E - e * np.sin(E)
    return Tp + (M / (2 * np.pi)) * P

def one(row):
    try:
        tic = int(row["tic"]); P = float(row["pl_orbper"]); eP = np.nanmax([abs(float(row.get("pl_orbpererr1", np.nan))), abs(float(row.get("pl_orbpererr2", np.nan))), 1e-5])
        files = sorted(fmap.get(tic, []))[-a.max_sectors:]
        T, F, E, S = [], [], [], []
        for sec, fname in files:
            p = ts.download(fname, cache)
            if p is None: continue
            r = ts.load_sector(p)
            if r is None: continue
            t, f, e, s = r; t, f, e = ts.bin_lc(t, f, e); t, f, e, mad = ts.detrend(t, f, e)
            T.append(t); F.append(f); E.append(e); S.append(np.full(len(t), sec))
        if not T: return dict(pl_name=row["pl_name"], status="no_data")
        t = np.concatenate(T); f = np.concatenate(F); e = np.concatenate(E); s = np.concatenate(S); o = np.argsort(t); t, f, e, s = t[o], f[o], e[o], s[o]
        # mask transiting siblings
        for q in sib[sib.hostname == row["hostname"]].itertuples():
            if np.isfinite(q.pl_orbper) and np.isfinite(q.pl_tranmid):
                dur = (q.pl_trandur if np.isfinite(q.pl_trandur) else 3.0) / 24
                ph = ((t - (q.pl_tranmid - 2457000) + 0.5 * q.pl_orbper) % q.pl_orbper) - 0.5 * q.pl_orbper
                keep = np.abs(ph) > max(1.0 * dur, 0.06); t, f, e, s = t[keep], f[keep], e[keep], s[keep]
        if len(t) < 500 or not np.isfinite(t).any(): return dict(pl_name=row["pl_name"], status="too_few_points")
        Rs = float(row["st_rad"]); Ms = float(row["st_mass"]) if np.isfinite(row["st_mass"]) else 1.0
        a_rs = 215.03 * (Ms * (P / 365.25) ** 2) ** (1 / 3) / Rs
        tdur = P / np.pi / a_rs                      # central transit duration (days)
        durs = np.clip(tdur * np.array([0.3, 0.5, 0.75, 1.0, 1.4]), 0.5 / 24, min(1.0, 0.25 * P)); durs = np.unique(durs)
        if baseline_guard(t) is False: return dict(pl_name=row["pl_name"], status="short_baseline")
        baseline = t.max() - t.min()
        # period window: +-max(3 sigma_P, 0.2%) but at least a few grid steps; frequency step from duration/baseline
        dP = max(3 * eP, 0.002 * P); step = P * (durs.min() / 3) / baseline; nP = int(min(max(20, 2 * dP / step), 20000))
        periods = np.linspace(P - dP, P + dP, nP)
        bls = BoxLeastSquares(t, f, dy=e)
        res = bls.power(periods, durs, objective="snr", method="fast", oversample=3)
        i = int(np.nanargmax(res.power)); Pb, t0b, depb, durb, snrb = float(periods[i]), float(res.transit_time[i]), float(1e6 * res.depth[i]), float(24 * res.duration[i]), float(res.power[i])
        # reference: how does this SNR compare with the distribution over a wide period search (same durations)?
        pmin_ref = max(0.5, 1.5 * float(durs.max())); ref_periods = ts.period_grid(baseline, pmin_ref, max(min(100.0, baseline / 2), 2 * pmin_ref), oversample=1.5)
        rp = bls.power(ref_periods, durs, objective="snr", method="fast", oversample=2).power
        sde = float((snrb - np.nanmean(rp)) / np.nanstd(rp)); ref_max = float(np.nanmax(rp))
        try: ntr = int(ts.count_transits(t, Pb, t0b, durb / 24))
        except Exception: ntr = -1
        # expected depth / SNR
        m = row["pl_bmasse"] if np.isfinite(row["pl_bmasse"]) else row["pl_msinie"]
        rpl = m ** 0.279 if m < 2.04 else (1.23 * m ** 0.589 if m < 131 else 11.1 * (m / 318) ** -0.044)
        depth_est = 1e6 * (rpl * 0.009158 / Rs) ** 2
        rms = float(np.nanmedian(np.abs(f - np.nanmedian(f))) * 1.4826); npts_in = max(tdur / (10 / 1440), 1)
        ntr_exp = max(int(baseline / P), 1); snr_exp = depth_est / (1e6 * rms) * np.sqrt(npts_in * ntr_exp * 0.75)
        # predicted conjunction
        Tc = conj_time(P, float(row["pl_orbtper"]) if np.isfinite(row["pl_orbtper"]) else np.nan, float(row["pl_orblper"]) if np.isfinite(row["pl_orblper"]) else np.nan, float(row["pl_orbeccen"]) if np.isfinite(row["pl_orbeccen"]) else 0.0)
        pred_phase = np.nan; pred_sigma_phase = np.nan; depth_at_pred = np.nan
        if np.isfinite(Tc):
            Tc_b = Tc - 2457000; n = np.round((t0b - Tc_b) / P); pred = Tc_b + n * P
            pred_phase = float(((t0b - pred) / P + 0.5) % 1 - 0.5)
            eTp = np.nanmax([abs(float(row.get("pl_orbtpererr1", np.nan))), abs(float(row.get("pl_orbtpererr2", np.nan))), 0.0])
            ncyc = abs((t.mean() - Tc_b) / P); pred_sigma_phase = float(np.sqrt((ncyc * eP) ** 2 + eTp ** 2) / P)
            # depth at the predicted ephemeris (box of central duration)
            try:
                st = bls.compute_stats(P, min(max(tdur, 0.5 / 24), 12 / 24), Tc_b); depth_at_pred = float(1e6 * st["depth"][0])
            except Exception:
                depth_at_pred = np.nan
        return dict(pl_name=row["pl_name"], hostname=row["hostname"], tic=tic, status="ok", nsec=len(files), npts=len(t), baseline=round(baseline, 1), P_pub=P, eP_pub=eP, P_best=Pb, t0_best=round(t0b, 4), depth_ppm=round(depb, 1), dur_h=round(durb, 2), tdur_central_h=round(24 * tdur, 2),
                    snr=round(snrb, 2), sde_vs_wide=round(sde, 2), wide_max_snr=round(ref_max, 2), ntr=ntr, depth_est_ppm=round(depth_est, 1), rms_ppm=round(1e6 * rms, 0), snr_expected=round(snr_exp, 1), ptransit=round(1 / a_rs, 3),
                    Tc_pred_btjd=round(Tc - 2457000, 3) if np.isfinite(Tc) else np.nan, pred_phase_offset=round(pred_phase, 3) if np.isfinite(pred_phase) else np.nan, pred_sigma_phase=round(pred_sigma_phase, 3) if np.isfinite(pred_sigma_phase) else np.nan, depth_at_pred_ppm=round(depth_at_pred, 1) if np.isfinite(depth_at_pred) else np.nan,
                    disc_year=row["disc_year"], tmag=row["sy_tmag"])
    except Exception as ex:
        return dict(pl_name=row["pl_name"], status="error: " + str(ex)[:120])

if __name__ == "__main__":
    rows = [r for _, r in pl.iterrows()]
    out = []
    with Pool(a.workers) as pool:
        for k, r in enumerate(pool.imap_unordered(one, rows)):
            out.append(r); print(k + 1, r.get("pl_name"), r.get("status"), "snr", r.get("snr"), "sde", r.get("sde_vs_wide"), "exp", r.get("snr_expected"), flush=True)
            if (k + 1) % 10 == 0: pd.DataFrame(out).to_csv(a.out, index=False)
    pd.DataFrame(out).to_csv(a.out, index=False); print("done", len(out))
