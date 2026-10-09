"""Name- and position-based cross-match of HARPS RVBank search signals against
exoplanet.eu (which includes unrefereed candidates such as Mayor et al. 2011)
and the NASA Exoplanet Archive pscomppars table.

Fixes the coordinate-only miss for high-proper-motion stars (e.g. eps Ind A)
by (a) matching normalised catalogue names and (b) using a 3-arcmin radius.

usage: python 16_rv_known_match.py DATA_DIR results/rvbank_search.csv results/rvbank_search_matched.csv
"""
import sys, re, json
import numpy as np, pandas as pd

data_dir, fin, fout = sys.argv[1:4]
rv = pd.read_csv(fin)
eu = pd.read_csv(f"{data_dir}/rvbank/exoplanet_eu_all.csv", low_memory=False)
na = pd.read_csv(f"{data_dir}/catalogs/pscomppars.csv", low_memory=False)
lst = pd.read_fwf(f"{data_dir}/rvbank/list.dat", header=None) if False else None

def norm(s):
    if not isinstance(s, str): return ""
    s = s.strip().upper().replace(" ", "")
    s = re.sub(r"^\*", "", s)
    return s

# --- build name -> planet list from exoplanet.eu
eu_names = {}
for _, r in eu.iterrows():
    names = [r.get("star_name", "")]
    alt = r.get("star_alternate_names", "")
    if isinstance(alt, str):
        names += [a for a in alt.split(",")]
    for n in names:
        n = norm(n)
        if n:
            eu_names.setdefault(n, []).append((r["name"], r["orbital_period"], r["planet_status"]))
eu_ra = pd.to_numeric(eu["ra"], errors="coerce").values
eu_dec = pd.to_numeric(eu["dec"], errors="coerce").values

na_names = {}
for _, r in na.iterrows():
    for col in ("hostname", "hd_name", "hip_name", "tic_id", "gaia_id"):
        n = norm(r.get(col, ""))
        if n:
            na_names.setdefault(n, []).append((r["pl_name"], r["pl_orbper"], "NASA"))

# RVBank list.dat gives RA/Dec per star; reuse what 14_ wrote if present
coords = {}
try:
    lst = pd.read_csv(f"{data_dir}/rvbank/list_coords.csv")
    coords = {norm(a): (b, c) for a, b, c in zip(lst["name"], lst["ra"], lst["dec"])}
except Exception:
    pass

def aliases(name):
    n = norm(name)
    out = {n}
    m = re.match(r"^(HD|HIP|GJ|GL|HR|BD|CD|LHS|LTT|LP|WOLF|ROSS|TYC|TIC)(.*)$", n)
    if m:
        pre, rest = m.groups()
        out.add(pre + rest.lstrip("0"))
        if pre == "GL": out.add("GJ" + rest)
        if pre == "GJ": out.add("GL" + rest)
    return out

rows = []
for _, r in rv.iterrows():
    name = r["name"]
    hits = []
    for a in aliases(name):
        hits += eu_names.get(a, [])
        hits += na_names.get(a, [])
    # coordinate match within 3 arcmin if coords known
    if name in coords or norm(name) in coords:
        ra, dec = coords.get(name, coords.get(norm(name)))
        d = np.hypot((eu_ra - ra) * np.cos(np.radians(dec)), eu_dec - dec) * 60.0
        for i in np.where(d < 3.0)[0]:
            hits.append((eu.iloc[i]["name"], eu.iloc[i]["orbital_period"], eu.iloc[i]["planet_status"] + "/coord"))
    # dedupe by planet name
    seen = {}
    for h in hits:
        seen.setdefault(h[0], h)
    hits = list(seen.values())
    P = float(r["P_d"])
    match = None
    for pl, per, st in hits:
        try:
            per = float(per)
        except Exception:
            continue
        if np.isfinite(per) and (abs(P / per - 1) < 0.05 or abs(P / per - 2) < 0.05 or abs(P / per - 0.5) < 0.05):
            match = f"{pl} P={per:.4g} ({st})"
    rows.append(dict(name=name, P_d=P, n_known_any=len(hits),
                     known_any="; ".join(f"{pl} P={per} ({st})" for pl, per, st in hits)[:300],
                     known_P_match=match))
m = pd.DataFrame(rows)
out = rv.merge(m, on=["name", "P_d"], how="left")
out.to_csv(fout, index=False)
print("stars:", len(out), "with any known planet (name/coord):", (out.n_known_any > 0).sum(),
      "signal matches known period:", out.known_P_match.notna().sum())
