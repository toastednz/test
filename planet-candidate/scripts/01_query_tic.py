#!/usr/bin/env python3
"""Query the TESS Input Catalog (TIC v8.2 at MAST) for cool dwarf stars.

Selection: Teff 2700-4000 K, radius < 0.65 Rsun, Tmag < 12.5, flagged as dwarfs.
Output: CSV with TIC ID, coordinates, Tmag, Teff, radius, mass, distance, contamination ratio.
"""
import sys, time
import pandas as pd
from astroquery.mast import Catalogs

out = sys.argv[1]
frames = []
# Query in declination strips to keep each request small enough for MAST
for dec_lo in range(-90, 90, 10):
    dec_hi = dec_lo + 10
    for attempt in range(4):
        try:
            t = Catalogs.query_criteria(catalog="Tic", Teff=[2700, 4000], rad=[0.05, 0.65],
                                        Tmag=[0, 12.5], objType="STAR", lumclass="DWARF",
                                        dec=[dec_lo, dec_hi])
            break
        except Exception as e:
            print("retry", dec_lo, e, file=sys.stderr); time.sleep(5 * (attempt + 1))
    else:
        raise SystemExit("failed strip %d" % dec_lo)
    df = t.to_pandas()
    print(dec_lo, dec_hi, len(df), flush=True)
    frames.append(df)
df = pd.concat(frames, ignore_index=True)
cols = ["ID", "ra", "dec", "Tmag", "Teff", "rad", "mass", "d", "contratio", "Vmag", "GAIA", "pmRA", "pmDEC", "logg", "lum"]
df = df[[c for c in cols if c in df.columns]]
df.to_csv(out, index=False)
print("total", len(df))
