#!/usr/bin/env python3
"""Triage search results: apply candidate cuts, cross-match with SPOC TCEs and nearby TOIs, rank.

Usage: 03_triage.py DATA_DIR RESULTS_CSV OUT_CSV
"""
import sys, json
import numpy as np, pandas as pd

DATA, RES, OUT = sys.argv[1:4]
r = pd.read_csv(RES)
r = r[r.status == "ok"].copy()
print("stars searched:", len(r))
tce = pd.read_csv(f"{DATA}/catalogs/tce_all.csv")
toi = pd.read_csv(f"{DATA}/catalogs/toi.csv", low_memory=False)
ctoi = pd.read_csv(f"{DATA}/catalogs/ctoi.csv", low_memory=False)
sample = pd.read_csv(f"{DATA}/catalogs/sample.csv").set_index("ID")

def ra_deg(s):
    h, m, sec = [float(x) for x in str(s).split(":")]; return 15 * (h + m / 60 + sec / 3600)
def dec_deg(s):
    s = str(s); sign = -1 if s.strip().startswith("-") else 1
    d, m, sec = [abs(float(x)) for x in s.split(":")]; return sign * (d + m / 60 + sec / 3600)
toi["ra_deg"] = toi.RA.apply(ra_deg); toi["dec_deg"] = toi.Dec.apply(dec_deg)
ctoi["ra_deg"] = pd.to_numeric(ctoi.RA, errors="coerce"); ctoi["dec_deg"] = pd.to_numeric(ctoi.Dec, errors="coerce")
ctoi["Period (days)"] = pd.to_numeric(ctoi["Period (days)"], errors="coerce")

def period_match(P, Q, tol=0.01):
    for a, b in [(1, 1), (1, 2), (2, 1), (1, 3), (3, 1)]:
        if abs((P * a) / (Q * b) - 1) < tol:
            return f"{a}:{b}"
    return None

rows = []
for x in r.itertuples():
    if not np.isfinite(x.snr):
        continue
    tic = int(x.tic)
    pk = json.loads(x.peaks_json)
    # consider all refined peaks, not only the best, so aliases don't hide a second real signal
    for ref in pk["refined"]:
        P, snr = ref["P"], ref["snr"]
        if snr < 7 or ref["ntr"] < 2:
            continue
        depth = ref["depth"] * 1e6
        if depth <= 0 or ref["dur"] * 24 > 8:
            continue
        # TCE match on same TIC
        tm = tce[tce.ticid == tic]
        tce_match = [(row.tceid, period_match(P, row.tce_period), row.tce_ntoi) for row in tm.itertuples() if period_match(P, row.tce_period)]
        # nearby TOIs/CTOIs within 3 arcmin with matching period (contamination)
        st = sample.loc[tic]
        dra = (toi.ra_deg - st.ra) * np.cos(np.radians(st.dec)); ddec = toi.dec_deg - st.dec
        near = toi[np.sqrt(dra ** 2 + ddec ** 2) * 60 < 3]
        near_match = [(row.TOI, period_match(P, row._34 if False else row[toi.columns.get_loc("Period (days)") + 1])) for row in near.itertuples()]
        near_match = [(t, m) for t, m in near_match if m]
        # CTOIs within 3 arcmin (blended companions carry their own TIC IDs)
        dra_c = (ctoi.ra_deg - st.ra) * np.cos(np.radians(st.dec)); ddec_c = ctoi.dec_deg - st.dec
        near_c = ctoi[np.sqrt(dra_c ** 2 + ddec_c ** 2) * 60 < 3]
        near_match += [(f"CTOI{row.CTOI}", period_match(P, row._25)) for row in near_c.itertuples() if np.isfinite(row._25) and period_match(P, row._25)]
        n_near_1arcmin = int((np.sqrt(dra ** 2 + ddec ** 2) * 60 < 1).sum() + (np.sqrt(dra_c ** 2 + ddec_c ** 2) * 60 < 1).sum())
        # TESS orbital systematics
        sysflag = any(abs(P / (13.7 / n) - 1) < 0.02 for n in (1, 2, 3, 4)) or any(abs(P / (13.7 * n) - 1) < 0.02 for n in (1, 2))
        ptd = ref.get("per_transit_ppm", {})
        rows.append(dict(tic=tic, Tmag=st.Tmag, Teff=st.Teff, rad=st.rad, nsec=x.nsec, baseline=x.baseline,
                         P=round(P, 5), t0=round(ref["t0"], 4), dur_h=round(ref["dur"] * 24, 2), depth_ppm=round(depth, 0),
                         rp_re=round(np.sqrt(depth / 1e6) * st.rad * 109.1, 2) if np.isfinite(st.rad) else np.nan,
                         snr=round(snr, 1), ntr=ref["ntr"], oe_sig=round(ref["oe_sig"], 1), sec_sig=round(ref["sec_sig"], 1),
                         block_snr=round(ref["block_snr"], 1), block_sde=round(ref["block_sde"], 1), alias=ref["mult"],
                         n_tce_same_star=len(tm), tce_match=";".join(f"{a}({b},ntoi={c})" for a, b, c in tce_match),
                         has_tce_match=bool(tce_match), nearby_toi_match=";".join(f"{a}({b})" for a, b in near_match),
                         n_nearby_toi=len(near), n_toi_ctoi_within_1arcmin=n_near_1arcmin, sys13_7=sysflag, rms10_ppm=x.rms10_ppm,
                         n_pos_transits=sum(1 for v in ptd.values() if v > 0), n_transits_measured=len(ptd)))
c = pd.DataFrame(rows)
c["frac_pos"] = c.n_pos_transits / c.n_transits_measured.clip(lower=1)
# maximum central transit duration for a circular orbit around this star (hours)
def tmax_h(P, R, M):
    a_rsun = 215.03 * (M * (P / 365.25) ** 2) ** (1 / 3)
    return 24 * P * R / (np.pi * a_rsun)
c["tmax_h"] = [tmax_h(P, R if np.isfinite(R) else 0.5, 0.9 * (R if np.isfinite(R) else 0.5)) for P, R in zip(c.P, c.rad)]
c["dur_ratio"] = c.dur_h / c.tmax_h
c["claimed_nearby"] = (c.nearby_toi_match != "") | (c.n_toi_ctoi_within_1arcmin > 0)
c["pass_phys"] = (c.dur_ratio < 2.5) & (c.oe_sig < 3) & (c.sec_sig.abs() < 4) & (c.depth_ppm > 150) & (c.depth_ppm < 150000) & (c.ntr >= 3)
c = c.sort_values(["pass_phys", "snr"], ascending=[False, False])
c.to_csv(OUT, index=False)
print("passing physical cuts:", c.pass_phys.sum(), "signals on", c[c.pass_phys].tic.nunique(), "stars;  of which no TCE match:", (c.pass_phys & ~c.has_tce_match).sum(), "; claimed by nearby TOI/CTOI:", (c.pass_phys & c.claimed_nearby).sum())
print("signals passing SNR>=7:", len(c), " on", c.tic.nunique(), "stars")
print(" with TCE match:", c.has_tce_match.sum(), " with nearby TOI period match:", (c.nearby_toi_match != "").sum())
cols = ["tic", "Tmag", "Teff", "rad", "nsec", "P", "dur_h", "dur_ratio", "depth_ppm", "rp_re", "snr", "ntr", "oe_sig", "sec_sig", "block_sde", "has_tce_match", "nearby_toi_match", "claimed_nearby", "sys13_7", "frac_pos"]
pd.set_option("display.width", 250)
print(c[c.pass_phys][cols].head(60).round(2).to_string(index=False))
