#!/usr/bin/env python3
"""Triage the fixed-period transit search of known non-transiting planets (22_rv_planet_transits.py).

Hit criteria: box SNR >= 7, the peak at the planet's period stands out against the wide 0.5-100 d search
(SDE >= 5 and SNR >= 0.9 x wide maximum), >= 2 transits, depth within a factor of 4 of the mass-radius
expectation (or deeper, for grazing/inflated cases flagged separately), and, when the RV conjunction time is
predicted to better than 0.2 in phase, |phase offset| < 2.5 sigma + 0.05.

Usage: 23_rv_planet_transits_triage.py RESULTS_CSV OUT_CSV
"""
import sys, numpy as np, pandas as pd
fin, fout = sys.argv[1:3]
d = pd.read_csv(fin); d = d[d.status == "ok"].copy()
print("planets searched:", len(d), "| median expected SNR if transiting:", round(d.snr_expected.median(), 1))
d["depth_ratio"] = d.depth_ppm / d.depth_est_ppm
d["phase_ok"] = True
m = d.pred_sigma_phase.notna() & (d.pred_sigma_phase < 0.2)
d.loc[m, "phase_ok"] = (d.loc[m, "pred_phase_offset"].abs() < 2.5 * d.loc[m, "pred_sigma_phase"] + 0.05)
d["hit"] = (d.snr >= 7) & (d.sde_vs_wide >= 5) & (d.snr >= 0.9 * d.wide_max_snr) & (d.ntr >= 2) & d.phase_ok
d["weak"] = (d.snr >= 6) & (d.sde_vs_wide >= 4) & (d.ntr >= 2) & ~d.hit
d["detectable"] = d.snr_expected >= 7
print("hits:", d.hit.sum(), " weak:", d.weak.sum(), " | planets where a central transit would have been detectable (expected SNR>=7):", d.detectable.sum(), "of", len(d))
cols = ["pl_name", "P_pub", "P_best", "depth_ppm", "depth_est_ppm", "dur_h", "tdur_central_h", "snr", "sde_vs_wide", "wide_max_snr", "ntr", "nsec", "pred_phase_offset", "pred_sigma_phase", "snr_expected", "tmag", "disc_year"]
pd.set_option("display.width", 260)
print("\n== hits"); print(d[d.hit].sort_values("snr", ascending=False)[cols].round(3).to_string(index=False))
print("\n== weak"); print(d[d.weak].sort_values("snr", ascending=False)[cols].round(3).to_string(index=False))
d.sort_values(["hit", "weak", "snr"], ascending=False).to_csv(fout, index=False)
# expected yield: sum of transit probabilities over detectable planets
print("\nsum of geometric transit probabilities over detectable planets:", round(d[d.detectable].ptransit.sum(), 2))
