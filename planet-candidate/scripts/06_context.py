#!/usr/bin/env python3
"""Context for a candidate host: TIC entry, Gaia DR3 neighbours (contamination), SIMBAD, nearby TOIs.

Usage: 06_context.py DATA_DIR TIC [P] > context.json
"""
import sys, json, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
from astroquery.mast import Catalogs
from astroquery.gaia import Gaia
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u

DATA, tic = sys.argv[1], int(sys.argv[2]); P = float(sys.argv[3]) if len(sys.argv) > 3 else None
out = {"tic": tic}
cat = Catalogs.query_criteria(catalog="Tic", ID=tic).to_pandas().iloc[0]
keys = ["ra", "dec", "pmRA", "pmDEC", "Tmag", "Vmag", "Jmag", "Kmag", "GAIA", "Teff", "logg", "rad", "mass", "rho", "lum", "d", "plx", "contratio", "disposition", "objType", "lumclass", "numcont", "gaiabp", "gaiarp"]
out["tic"] = {k: (None if pd.isna(cat[k]) else (float(cat[k]) if isinstance(cat[k], (int, float, np.floating, np.integer)) else str(cat[k]))) for k in keys if k in cat}
ra, dec = float(cat["ra"]), float(cat["dec"])
# Gaia DR3 cone 1 arcmin
try:
    job = Gaia.launch_job(f"""SELECT source_id, ra, dec, phot_g_mean_mag, phot_bp_mean_mag, phot_rp_mean_mag, parallax, pmra, pmdec, ruwe,
        non_single_star, DISTANCE(POINT('ICRS', ra, dec), POINT('ICRS', {ra}, {dec}))*3600 AS sep_arcsec
        FROM gaiadr3.gaia_source WHERE 1=CONTAINS(POINT('ICRS', ra, dec), CIRCLE('ICRS', {ra}, {dec}, 1.0/60.0)) ORDER BY sep_arcsec""")
    g = job.get_results().to_pandas()
    out["gaia_neighbours_1arcmin"] = g.round(4).to_dict("records")
    tgt = g.iloc[0] if len(g) else None
    if tgt is not None:
        others = g.iloc[1:]
        # flux ratio of neighbours relative to target (G band, rough TESS proxy)
        out["neighbour_flux_fraction_within_1arcmin"] = float(np.sum(10 ** (-0.4 * (others.phot_g_mean_mag - tgt.phot_g_mean_mag)))) if len(others) else 0.0
        out["brightest_neighbour"] = None if not len(others) else dict(sep_arcsec=float(others.sep_arcsec.min()), dG=float((others.phot_g_mean_mag - tgt.phot_g_mean_mag).min()))
        out["target_ruwe"] = float(tgt.ruwe) if pd.notna(tgt.ruwe) else None
        out["target_non_single_star_flag"] = int(tgt.non_single_star) if pd.notna(tgt.non_single_star) else None
except Exception as ex:
    out["gaia_error"] = repr(ex)[:300]
# SIMBAD
try:
    Simbad.add_votable_fields("otype", "sp_type", "ids") if hasattr(Simbad, "add_votable_fields") else None
    r = Simbad.query_region(SkyCoord(ra * u.deg, dec * u.deg), radius=20 * u.arcsec)
    out["simbad"] = None if r is None else [{k.lower(): str(row[k]) for k in r.colnames if k.lower() in ("main_id", "otype", "sp_type", "ids", "otype_txt")} for row in r]
except Exception as ex:
    out["simbad_error"] = repr(ex)[:300]
# nearby TOIs / CTOIs within 3 arcmin
toi = pd.read_csv(f"{DATA}/catalogs/toi.csv", low_memory=False)
def ra_deg(s):
    h, m, sec = [float(x) for x in str(s).split(":")]; return 15 * (h + m / 60 + sec / 3600)
def dec_deg(s):
    s = str(s); sign = -1 if s.strip().startswith("-") else 1
    d, m, sec = [abs(float(x)) for x in s.split(":")]; return sign * (d + m / 60 + sec / 3600)
toi["ra_deg"] = toi.RA.apply(ra_deg); toi["dec_deg"] = toi.Dec.apply(dec_deg)
sep = np.sqrt(((toi.ra_deg - ra) * np.cos(np.radians(dec))) ** 2 + (toi.dec_deg - dec) ** 2) * 60
near = toi[sep < 3].copy(); near["sep_arcmin"] = sep[sep < 3]
out["nearby_tois_3arcmin"] = near[["TIC ID", "TOI", "Period (days)", "Depth (ppm)", "TFOPWG Disposition", "sep_arcmin"]].round(4).to_dict("records")
tce = pd.read_csv(f"{DATA}/catalogs/tce_all.csv"); tt = tce[tce.ticid == tic]
out["spoc_tces_this_star"] = tt[["tceid", "sectors", "tce_period", "tce_depth", "tce_model_snr", "tce_num_transits", "tce_ntoi"]].round(5).to_dict("records")
if P:
    out["tce_period_match"] = [r for r in out["spoc_tces_this_star"] if any(abs(P * a / (r["tce_period"] * b) - 1) < 0.01 for a, b in [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)])]
sample = pd.read_csv(f"{DATA}/catalogs/sample.csv").set_index("ID")
out["sectors_2min"] = str(sample.loc[tic, "sectors"]) if tic in sample.index else None
print(json.dumps(out, indent=1, default=str))
