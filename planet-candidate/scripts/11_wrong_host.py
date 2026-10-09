#!/usr/bin/env python3
"""Mine SPOC TCEs whose difference-image centroid is significantly offset from the target: the
signal may belong to a neighbouring star on which it could be planet-sized and uncatalogued.

Steps: read all dvr-tcestats files (planet-like cuts), keep TCEs with offset/err >= 3 and
5" < offset < 90", locate the neighbour with a TIC cone search around the offset position, compute the
dilution-corrected depth on the neighbour, drop cases where either star is a TOI/CTOI host or has a
TOI/CTOI within 1', rank by neighbour planet radius.

Usage: 11_wrong_host.py DATA_DIR OUT_CSV [--max N]
"""
import os, sys, glob, json, time, argparse, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from astroquery.mast import Catalogs
ap = argparse.ArgumentParser(); ap.add_argument("data_dir"); ap.add_argument("out"); ap.add_argument("--max", type=int, default=400); ap.add_argument("--sort", default="snr", choices=["snr", "depth"]); ap.add_argument("--maxdepth", type=float, default=30000); a = ap.parse_args()
D = a.data_dir
cols = ["tceid", "ticid", "sectors", "tce_period", "tce_time0bt", "tce_depth", "tce_duration", "tce_model_snr", "tce_prad", "tce_num_transits",
        "tce_dicco_mra", "tce_dicco_mra_err", "tce_dicco_mdec", "tce_dicco_mdec_err", "tce_dicco_msky", "tce_dicco_msky_err", "tce_steff", "tce_sradius", "tce_ntoi"]
frames = []
for f in sorted(glob.glob(os.path.join(D, "tce", "*_dvr-tcestats.csv"))):
    df = pd.read_csv(f, comment="#", low_memory=False)
    keep = [c for c in cols if c in df.columns]
    df = df[keep]
    df = df[(df.tce_model_snr >= 9) & (df.tce_depth < a.maxdepth) & (df.tce_depth > 300) & (df.tce_num_transits >= 3) & (df.tce_period > 0.5)]
    if "tce_dicco_msky" in df.columns:
        df = df[(df.tce_dicco_msky > 5) & (df.tce_dicco_msky < 90) & (df.tce_dicco_msky / df.tce_dicco_msky_err.replace(0, np.nan) >= 3)]
        frames.append(df)
t = pd.concat(frames, ignore_index=True)
print("TCEs with significant centroid offset and planet-like parameters:", len(t), "on", t.ticid.nunique(), "stars", flush=True)
# keep the highest-SNR TCE per star & period (rounded)
t["pkey"] = t.tce_period.round(2); t = t.sort_values("tce_model_snr", ascending=False).drop_duplicates(["ticid", "pkey"])
# exclusions: TOI/CTOI hosts and known planets
toi = pd.read_csv(f"{D}/catalogs/toi.csv", low_memory=False); ctoi = pd.read_csv(f"{D}/catalogs/ctoi.csv", low_memory=False)
def ra_deg(s): h, m, sec = [float(x) for x in str(s).split(":")]; return 15 * (h + m / 60 + sec / 3600)
def dec_deg(s): s = str(s); sign = -1 if s.strip().startswith("-") else 1; d, m, sec = [abs(float(x)) for x in s.split(":")]; return sign * (d + m / 60 + sec / 3600)
toi["ra_deg"] = toi.RA.apply(ra_deg); toi["dec_deg"] = toi.Dec.apply(dec_deg); ctoi["ra_deg"] = pd.to_numeric(ctoi.RA, errors="coerce"); ctoi["dec_deg"] = pd.to_numeric(ctoi.Dec, errors="coerce")
claimed = set(toi["TIC ID"]) | set(ctoi["TIC ID"])
t = t[~t.ticid.isin(claimed)]
print("after removing TOI/CTOI hosts:", len(t), flush=True)
t = (t.sort_values("tce_depth", ascending=True) if a.sort == "depth" else t.sort_values("tce_model_snr", ascending=False)).head(a.max)
rows = []
for i, r in enumerate(t.itertuples()):
    try:
        tgt = Catalogs.query_criteria(catalog="Tic", ID=int(r.ticid)).to_pandas().iloc[0]
    except Exception as ex:
        continue
    ra0, dec0 = float(tgt.ra), float(tgt.dec)
    ra_off = ra0 + r.tce_dicco_mra / 3600 / np.cos(np.radians(dec0)); dec_off = dec0 + r.tce_dicco_mdec / 3600
    try:
        near = Catalogs.query_region(f"{ra_off} {dec_off}", radius=max(3 * r.tce_dicco_msky_err, 8) / 3600, catalog="Tic").to_pandas()
    except Exception as ex:
        continue
    near = near[near.ID.astype(str) != str(int(r.ticid))]
    if not len(near): continue
    near = near.sort_values("Tmag")
    nb = near.iloc[0]
    # flux fraction: how much of the target aperture flux is the neighbour's? approximate from Tmag difference (both fully in aperture)
    dT = float(nb.Tmag) - float(tgt.Tmag); frac_nb = 10 ** (-0.4 * dT) / (1 + 10 ** (-0.4 * dT))
    # SPOC depth is already corrected assuming the target hosts it (CROWDSAP) -> approximate raw aperture depth = depth * (1 - contratio_target/(1+contratio))
    cr = float(tgt.contratio) if np.isfinite(tgt.contratio) else 0.0
    raw_depth = r.tce_depth / (1 + cr)
    depth_on_nb = raw_depth / max(frac_nb, 1e-3)
    rp_nb = np.sqrt(depth_on_nb / 1e6) * (float(nb.rad) if np.isfinite(nb.rad) else np.nan) * 109.1
    # TOI/CTOI within 1' of the neighbour?
    dra = (toi.ra_deg - float(nb.ra)) * np.cos(np.radians(float(nb.dec))); ddec = toi.dec_deg - float(nb.dec)
    drc = (ctoi.ra_deg - float(nb.ra)) * np.cos(np.radians(float(nb.dec))); ddc = ctoi.dec_deg - float(nb.dec)
    n_claim = int((np.sqrt(dra ** 2 + ddec ** 2) * 60 < 1).sum() + (np.sqrt(drc ** 2 + ddc ** 2) * 60 < 1).sum())
    rows.append(dict(tceid=r.tceid, tic=int(r.ticid), sectors=r.sectors, P=r.tce_period, t0=r.tce_time0bt, depth_ppm=r.tce_depth, dur_h=r.tce_duration, snr=r.tce_model_snr, ntr=r.tce_num_transits,
                     offset_arcsec=r.tce_dicco_msky, offset_sig=r.tce_dicco_msky / r.tce_dicco_msky_err, tgt_Tmag=float(tgt.Tmag), tgt_Teff=float(tgt.Teff) if np.isfinite(tgt.Teff) else np.nan, tgt_rad=float(tgt.rad) if np.isfinite(tgt.rad) else np.nan,
                     nb_tic=int(nb.ID), nb_sep_from_offset_arcsec=float(nb.dstArcSec), nb_Tmag=float(nb.Tmag), nb_Teff=float(nb.Teff) if np.isfinite(nb.Teff) else np.nan, nb_rad=float(nb.rad) if np.isfinite(nb.rad) else np.nan,
                     nb_d_pc=float(nb.d) if np.isfinite(nb.d) else np.nan, nb_lumclass=str(nb.lumclass), nb_flux_frac=round(frac_nb, 3), depth_on_nb_ppm=round(depth_on_nb), rp_on_nb_re=round(rp_nb, 2) if np.isfinite(rp_nb) else np.nan,
                     nb_claimed_within_1arcmin=n_claim, nb_is_toi_ctoi=int(nb.ID) in claimed))
    if i % 20 == 0:
        print(i, rows[-1]["tic"], "->", rows[-1]["nb_tic"], "rp_nb", rows[-1]["rp_on_nb_re"], flush=True)
        pd.DataFrame(rows).to_csv(a.out, index=False)
out = pd.DataFrame(rows); out.to_csv(a.out, index=False)
good = out[(~out.nb_is_toi_ctoi) & (out.nb_claimed_within_1arcmin == 0) & (out.rp_on_nb_re < 12) & (out.nb_lumclass != "GIANT")].sort_values("snr", ascending=False)
pd.set_option("display.width", 250)
print("neighbour-host candidates (planet-sized on neighbour, neither star claimed):", len(good))
print(good[["tic", "nb_tic", "P", "depth_ppm", "snr", "ntr", "offset_arcsec", "offset_sig", "tgt_Tmag", "nb_Tmag", "nb_Teff", "nb_rad", "nb_d_pc", "nb_flux_frac", "depth_on_nb_ppm", "rp_on_nb_re"]].head(40).round(2).to_string(index=False))
