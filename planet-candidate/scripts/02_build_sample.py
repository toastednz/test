#!/usr/bin/env python3
"""Build the search sample.

Inputs (all under DATA):
  catalogs/tic_cool_dwarfs.csv   - TIC query output (script 01)
  lclists/tesscurl_sector_*_lc.sh - MAST bulk-download scripts; one line per 2-min light curve file
  tce/*_dvr-tcestats.csv          - SPOC TCE statistics (single- and multi-sector runs)
  catalogs/toi.csv, ctoi.csv, pscomppars.csv - known candidates / planets

Outputs (under DATA/catalogs):
  tic_sectors.csv  - TIC ID -> list of sectors with 2-min SPOC light curves
  tce_all.csv      - concatenated TCE table (subset of columns)
  sample.csv       - cool dwarfs with 2-min data, flags for TOI/CTOI/known planet/TCE
"""
import glob, os, re, sys
import pandas as pd

DATA = sys.argv[1]
# 1. TIC -> sectors
rx = re.compile(r"-s(\d{4})-(\d{16})-\d{4}-[sa]_lc\.fits")
rows = {}
for f in sorted(glob.glob(os.path.join(DATA, "lclists", "tesscurl_sector_*_lc.sh"))):
    with open(f) as fh:
        for line in fh:
            m = rx.search(line)
            if m:
                sec, tic = int(m.group(1)), int(m.group(2))
                rows.setdefault(tic, set()).add(sec)
tic_sec = pd.DataFrame({"ID": list(rows.keys()),
                        "sectors": [",".join(map(str, sorted(v))) for v in rows.values()],
                        "nsec": [len(v) for v in rows.values()]})
tic_sec.to_csv(os.path.join(DATA, "catalogs", "tic_sectors.csv"), index=False)
print("TIC IDs with 2-min data:", len(tic_sec), "max sector:", max(max(v) for v in rows.values()))

# 2. TCEs
keep = ["tceid", "ticid", "tce_plnt_num", "sectors", "tce_period", "tce_time0bt", "tce_depth",
        "tce_duration", "tce_model_snr", "tce_prad", "tce_num_transits", "tce_ntoi"]
tces = []
for f in sorted(glob.glob(os.path.join(DATA, "tce", "*_dvr-tcestats.csv"))):
    df = pd.read_csv(f, comment="#", low_memory=False)
    df = df[[c for c in keep if c in df.columns]]
    df["file"] = os.path.basename(f)
    tces.append(df)
tce = pd.concat(tces, ignore_index=True)
tce.to_csv(os.path.join(DATA, "catalogs", "tce_all.csv"), index=False)
print("TCEs:", len(tce), "unique TICs with a TCE:", tce.ticid.nunique())

# 3. Sample
cd = pd.read_csv(os.path.join(DATA, "catalogs", "tic_cool_dwarfs.csv"))
cd = cd.merge(tic_sec, on="ID", how="inner")
toi = pd.read_csv(os.path.join(DATA, "catalogs", "toi.csv"), low_memory=False)
ctoi = pd.read_csv(os.path.join(DATA, "catalogs", "ctoi.csv"), low_memory=False)
ps = pd.read_csv(os.path.join(DATA, "catalogs", "pscomppars.csv"))
ps_tic = set(int(x.replace("TIC", "").strip()) for x in ps.tic_id.dropna() if str(x).strip().startswith("TIC"))
cd["is_toi"] = cd.ID.isin(set(toi["TIC ID"]))
cd["is_ctoi"] = cd.ID.isin(set(ctoi["TIC ID"]))
cd["is_known_planet_host"] = cd.ID.isin(ps_tic)
cd["has_tce"] = cd.ID.isin(set(tce.ticid))
cd.to_csv(os.path.join(DATA, "catalogs", "sample.csv"), index=False)
print("cool dwarfs with 2-min data:", len(cd))
print("  TOI hosts:", cd.is_toi.sum(), " CTOI hosts:", cd.is_ctoi.sum(), " known planet hosts:", cd.is_known_planet_host.sum(), " with any TCE:", cd.has_tce.sum())
clean = cd[~cd.is_toi & ~cd.is_ctoi & ~cd.is_known_planet_host]
print("clean (no TOI/CTOI/known planet):", len(clean))
print(clean.nsec.describe())
print("nsec histogram:"); print(clean.nsec.value_counts().sort_index().to_string())
