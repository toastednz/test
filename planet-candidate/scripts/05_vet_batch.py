#!/usr/bin/env python3
"""Vet the top triaged signals (best signal per star), writing results/vet/<tic>_P<period>/.

Usage: 05_vet_batch.py DATA_DIR TRIAGE_CSV OUT_ROOT [--n N] [--include-tce] [--tls]
"""
import sys, os, subprocess, argparse, json
import pandas as pd
ap = argparse.ArgumentParser()
ap.add_argument("data_dir"); ap.add_argument("triage"); ap.add_argument("out_root")
ap.add_argument("--n", type=int, default=5); ap.add_argument("--include-tce", action="store_true"); ap.add_argument("--tls", action="store_true")
ap.add_argument("--tics", default="")
a = ap.parse_args()
c = pd.read_csv(a.triage)
c = c[c.pass_phys & ~c.claimed_nearby]
if not a.include_tce:
    c = c[~c.has_tce_match]
if a.tics:
    c = c[c.tic.isin([int(x) for x in a.tics.split(",")])]
c = c.sort_values("snr", ascending=False).drop_duplicates("tic").head(a.n)
here = os.path.dirname(os.path.abspath(__file__))
rows = []
for r in c.itertuples():
    out = os.path.join(a.out_root, f"{r.tic}_P{r.P:.3f}")
    if os.path.exists(os.path.join(out, "summary.json")):
        pass
    else:
        cmd = [sys.executable, "-I", os.path.join(here, "04_vet.py"), a.data_dir, str(r.tic), str(r.P), str(r.t0), str(r.dur_h), out] + (["--tls"] if a.tls else [])
        print("vetting", r.tic, r.P, flush=True)
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        s = json.load(open(os.path.join(out, "summary.json")))
    except Exception as ex:
        print("  failed", r.tic, ex); continue
    tls = s.get("tls", {})
    rows.append(dict(tic=r.tic, P=round(s["P"], 5), depth_ppm=round(s["depth_ppm"]), bls_snr=round(s["bls_snr"], 1), ntr=s["n_transits"], ntr_pos=s["n_transits_positive"],
                     snr_comb=round(s.get("snr_combined", float("nan")), 1), snr_wo_max=round(s.get("snr_without_strongest", float("nan")), 1), chi2=round(s.get("chi2_red_depths", float("nan")), 1),
                     tls_P=round(tls.get("P", float("nan")), 4), tls_match=tls.get("tls_matches_bls", None),
                     sectors=",".join(map(str, s["sectors_with_transits"])), odd=round(s["depth_odd_ppm"]), even=round(s["depth_even_ppm"]),
                     sec=f"{s['depth_phased_ppm']:.0f}±{s['depth_phased_err']:.0f}", tls_sde=round(tls.get("SDE", float("nan")), 1), tls_snr=round(tls.get("snr", float("nan")), 1),
                     tls_oe=round(tls.get("odd_even_mismatch", float("nan")), 2), per_transit=[(p["sector"], round(p["depth_ppm"]), round(p["snr"], 1)) for p in s["per_transit"]]))
pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 120)
df = pd.DataFrame(rows)
if len(df): df = df.sort_values("snr_wo_max", ascending=False)
print(df.to_string(index=False))
df.to_csv(os.path.join(a.out_root, "vet_summary.csv"), index=False)
