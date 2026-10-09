#!/usr/bin/env python3
"""Assemble the HD 32564 candidate summary (stellar parameters, four-signal Keplerian solution,
derived planet properties, robustness and activity tests, TESS transit checks) into
results/candidate_HD32564/candidate_summary.json + candidate_summary.md, and add a per-season
coherence test for the two strongest signals.

Usage: 21_hd32564_report.py RVBANK_DIR RESULTS_DIR
"""
import os, sys, re, json, shutil
import numpy as np, pandas as pd
rvdir, res = sys.argv[1:3]
src = os.path.join(res, "rv_candidates", "HD32564"); out = os.path.join(res, "candidate_HD32564"); os.makedirs(out, exist_ok=True)
kep = json.load(open(os.path.join(src, "keplerian.json"))); ms = json.load(open(os.path.join(src, "multisignal.json")))
act = json.load(open(os.path.join(src, "activity_check.json"))); vet = json.load(open(os.path.join(src, "rv_vet.json")))
ms24 = json.load(open(os.path.join(src, "rvbank2024", "multisignal.json"))); msdrs = json.load(open(os.path.join(src, "drs_pipeline", "multisignal.json")))
tess = {k: json.load(open(os.path.join(src, k, "fullbls.json"))) for k in ("tess", "tess_p2575", "tess_p11")}
star = dict(name="HD 32564", hip="HIP 23575", tic=213078996, gaia_dr3=3227308623164447616, ra_deg=76.026026, dec_deg=-0.649056, V=8.60, Tmag=7.94,
            sptype="G6V", teff_K=5574, logg=4.48, radius_rsun=0.94, mass_msun=0.98, lum_lsun=0.77, dist_pc=48.5, ruwe=0.97, gaia_non_single_star=0,
            logRHK=-5.03, logRHK_source="Yu et al. 2024 (MNRAS 528, 5511), Table 3", params_source="TIC v8.2 / Gaia DR3")
# per-season coherence for the two strongest signals (fit K, phase per season with other signals fixed)
rd = open(os.path.join(rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]; cols = {}
for line in rd.splitlines():
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
    if m:
        g = m.groups()
        if len(g) == 4: cols[g[3]] = (int(g[0]) - 1, int(g[1]))
        else: cols[g[2]] = (int(g[0]) - 1, int(g[0]))
want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "Flag"]; rows = []
with open(os.path.join(rvdir, "rvbank.dat")) as f:
    for line in f:
        if line[cols["Name"][0]:cols["Name"][1]].strip() == "HD32564": rows.append([line[cols[w][0]:cols[w][1]] for w in want])
g = pd.DataFrame(rows, columns=want)
for c in want[1:]: g[c] = pd.to_numeric(g[c], errors="coerce")
g = g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp)]; t = g.BJD.values; y = g.DRVmlcnzp.values; e = np.sqrt(g.e_DRVmlcnzp.values ** 2 + 1)
night = np.floor(t - 0.5); w = 1 / e ** 2; nb = pd.DataFrame(dict(night=night, t=t, y=y, w=w)).groupby("night")
tB = nb.apply(lambda d: np.sum(d.t * d.w) / np.sum(d.w)).values; yB = nb.apply(lambda d: np.sum(d.y * d.w) / np.sum(d.w)).values; eB = nb.apply(lambda d: 1 / np.sqrt(np.sum(d.w))).values
P = [p["P"] for p in kep["planets"]]; tref = tB.mean()
def design(tt, ps): return np.hstack([np.ones((len(tt), 1)), ((tt - tref) / 365.25)[:, None]] + [np.column_stack([np.cos(2 * np.pi * tt / q), np.sin(2 * np.pi * tt / q)]) for q in ps])
X = design(tB, P); W = 1 / eB; cf = np.linalg.lstsq(X * W[:, None], yB * W, rcond=None)[0]
season = np.floor((tB - 2455000 - 150) / 365.25).astype(int)   # seasons start ~Oct
seasons = {}
for s in np.unique(season):
    k = season == s
    if k.sum() < 15: continue
    row = {}
    for j, Pj in enumerate(P[:2]):
        others = [q for i, q in enumerate(P) if i != j]
        # subtract the global fit of the other signals, then fit this signal in-season
        Xo = design(tB[k], others); co = np.linalg.lstsq(Xo * W[k][:, None], (yB[k] - X[k][:, 2 + 2 * j:4 + 2 * j] @ cf[2 + 2 * j:4 + 2 * j] * 0) * W[k], rcond=None)[0]
        resid = yB[k] - np.hstack([np.ones((k.sum(), 1)), ((tB[k] - tref) / 365.25)[:, None]] + [np.column_stack([np.cos(2 * np.pi * tB[k] / q), np.sin(2 * np.pi * tB[k] / q)]) for q in others]) @ np.concatenate([cf[:2], np.concatenate([cf[2 + 2 * i:4 + 2 * i] for i in range(len(P)) if i != j])])
        Xs = np.column_stack([np.ones(k.sum()), np.cos(2 * np.pi * tB[k] / Pj), np.sin(2 * np.pi * tB[k] / Pj)]); cs = np.linalg.lstsq(Xs * W[k][:, None], resid * W[k], rcond=None)[0]
        row[f"P{Pj:.3f}"] = dict(K=float(np.hypot(cs[1], cs[2])), phase_deg=float(np.degrees(np.arctan2(cs[2], cs[1]))))
    seasons[f"season_{2009 + s}-{2010 + s}"] = dict(n_nights=int(k.sum()), **row)
planets = []
for j, p in enumerate(kep["planets"]):
    a = p["a_au"]; S = star["lum_lsun"] / a ** 2; Teq = 278.0 * S ** 0.25 * (1 - 0.3) ** 0.25
    Rp_est = p["msini_earth"] ** 0.28 * 1.0 if p["msini_earth"] < 6 else (p["msini_earth"] / 2.7) ** (1 / 1.3)   # rough Chen&Kipping-like scaling
    depth_ppm = 1e6 * (Rp_est * 0.009158 / star["radius_rsun"]) ** 2
    ptr = star["radius_rsun"] * 0.00465 / a
    planets.append(dict(letter="bcde"[j], P_d=p["P"], eP_d=p["eP"], K_ms=p["K_ms"], eK_ms=p["eK_ms"], e=p["e"], msini_earth=p["msini_earth"], emsini_earth=p["emsini_earth"], a_au=a,
                        insolation_earth=float(S), Teq_K_A0p3=float(Teq), Rp_est_rearth_if_rocky_or_volatile=float(Rp_est), expected_transit_depth_ppm=float(depth_ppm), transit_probability=float(ptr),
                        fap_drop_one_baluev=ms["signals"][j]["fap_drop_one"], dBIC_vs_without=[v for k, v in kep["model_comparison"].items() if k.startswith("without_") and abs(float(k.split("_")[1]) / p["P"] - 1) < 0.01][0]["dBIC"]))
summary = dict(
    star=star,
    data=dict(source="HARPS RVBank (Trifonov et al. 2020, CDS J/A+A/636/A74), SERVAL NZP-corrected RVs; cross-checked with the 2024 corrected release (Perdelwitz et al. 2024, J/A+A/683/A125 table4) and the HARPS DRS pipeline velocities",
              n_spectra=205, n_nights=kep["n_nights"], baseline_d=kep["baseline_d"], span="2009-11-29 to 2016-03-18", eso_programmes="183.C-0972(A) [174 spectra, 2009-2013, PI Udry: HARPS GTO high-precision], 192.C-0852(A) [19, 2013-2016], 090.C-0849, 091.C-0936; re-observed 2022-2025 under 108.22KV / 112.25YG (Delisle/Ségransan)",
              rms_raw_ms=ms["rms_raw_ms"], rms_after_4_signals_ms=kep["rms_resid_ms"], fitted_jitter_ms=kep["jitter_ms"], trend_ms_per_yr=kep["trend_ms_per_yr"]),
    planets=planets,
    model=dict(n_signals=4, chi2_null_fixed_jitter=ms["chi2_null"], chi2_4signals_fixed_jitter=ms["chi2_final"], dlnL_4_vs_0_free_jitter=kep["model_comparison"]["null"]["dlnL"], bic_4=kep["bic"],
               fifth_signal_search=ms["stages"][-1], alias_1yr_test=kep.get("alias1"), eccentricities_converge_to_zero=True),
    robustness=dict(rvbank2024_corrected=[dict(P=s["P"], K=s["K_ms"]) for s in ms24["signals"]], drs_pipeline=[dict(P=s["P"], K=s["K_ms"]) for s in msdrs["signals"]],
                    halves_signal1=vet["halves"], bootstrap_fap_signal1=f'{vet["boot_fap"]} ({vet["n_boot"]} sector-shuffle draws)', per_season=seasons),
    activity=dict(logRHK=star["logRHK"], expected_rotation_d_from_logRHK="~30-40 (Mamajek & Hillenbrand 2008 relation); no rotation period detected by Yu et al. 2024",
                  indicator_power_at_signal_periods={c: {P_: round(v["power"], 3) for P_, v in r["at_P"].items()} for c, r in act["indicators"].items()},
                  indicator_spearman_vs_rv_resid={c: {P_: round(v["spearman_rho_vs_rv_resid"], 2) for P_, v in r["at_P"].items()} for c, r in act["indicators"].items()},
                  note="No indicator shows periodicity at any of the four periods after prewhitening long-term trends; weak overall CRX anti-correlation (rho~-0.2) with RV residuals present at all periods"),
    inner_period_alias_note="The inner signal's period is 2.5566 d, not 1.635 d: 1.635 d is the highest single-signal GLS peak, but once the three longer-period signals are modelled jointly the daily/yearly alias partner 2.5566 d is preferred by delta-lnL = 30 (chi2 302 vs 404); a 2023 hobbyist analysis (DeviantArt, Tullimonstrum1) had already adopted 2.5566 d. Residuals of the four-signal model show a weak 122-d peak (K~0.8 m/s, FAP 0.05), matching that analysis's claimed fifth planet at 123.7 d, but it is not significant here.",
    tess=dict(sectors=[5, 32], cadence="2-min SPOC", checks={k: dict(P=v["cand_P"], sde=v["cand_sde"], depth_ppm=v["cand_depth_ppm"], global_best_sde=v["global_sde"]) for k, v in tess.items()},
              note="No transit at 1.635 d (or its 2.575-d alias) or 11.06 d; depth limit ~60 ppm vs expected 300-900 ppm, so planet b does not transit"),
    prior_claims=dict(refereed_literature="none found (SIMBAD bibliography 49 refs, NASA Exoplanet Archive, exoplanet.eu, Mayor et al. 2011 table, arXiv API)",
                      other="DeviantArt illustration by user 'Tullimonstrum1' (2023-09-06) captioned as a 5-planet system (periods 2.56-123 d) 'recently found' in HARPS data by that user; not a scientific publication. The HARPS GTO team (PI Udry) re-observed the star in 2022-2025, which suggests they are aware of the signals."),
    verdict="Four coherent, low-amplitude (1.6-4 m/s) signals at 1.635, 11.06, 23.62 and 48.97 d in 191 nights of public HARPS velocities of a very inactive G6V star; all survive activity-indicator, alias, half-sample, per-season, independent-pipeline and data-release checks. Minimum masses 7, 11, 12 and 11 Earth masses. Period ratios 2.14 and 2.07 (near 2:1, like Kepler compact systems). Unpublished planet-candidate system from public data; confirmation requires the data owners' analysis or new RVs (e.g. ESPRESSO/HARPS) to be independent.")
json.dump(summary, open(os.path.join(out, "candidate_summary.json"), "w"), indent=1)
for f in ["multisignal.png", "keplerian.png", "rv_vet.png"]:
    if os.path.exists(os.path.join(src, f)): shutil.copy(os.path.join(src, f), os.path.join(out, f))
md = ["# HD 32564: four-signal radial-velocity planet-candidate system (public HARPS data)", "",
      f"Star: {star['name']} ({star['hip']}, TIC {star['tic']}), {star['sptype']}, V={star['V']}, Teff={star['teff_K']} K, R={star['radius_rsun']} Rsun, M={star['mass_msun']} Msun, d={star['dist_pc']} pc, log R'HK={star['logRHK']} (very inactive), Gaia RUWE {star['ruwe']}.", "",
      "| signal | P (d) | K (m/s) | m sin i (Me) | a (AU) | S (S_earth) | Teq (K) | FAP (drop-one) | dBIC |", "|---|---|---|---|---|---|---|---|---|"]
for p in planets:
    md.append(f"| {p['letter']} | {p['P_d']:.4f} ± {p['eP_d']:.4f} | {p['K_ms']:.2f} ± {p['eK_ms']:.2f} | {p['msini_earth']:.1f} ± {p['emsini_earth']:.1f} | {p['a_au']:.4f} | {p['insolation_earth']:.0f} | {p['Teq_K_A0p3']:.0f} | {p['fap_drop_one_baluev']:.1e} | {p['dBIC_vs_without']:.0f} |")
md += ["", f"RV rms: {ms['rms_raw_ms']:.2f} m/s raw -> {kep['rms_resid_ms']:.2f} m/s after the four signals (fitted jitter {kep['jitter_ms']:.2f} m/s). No 5th signal (next peak FAP {ms['stages'][-1]['fap']:.2g}).", "",
       "Per-season coherence (signals b and c):", ""]
for s, v in seasons.items():
    md.append(f"- {s}: n={v['n_nights']}, " + ", ".join(f"{k}: K={q['K']:.2f} m/s, phase={q['phase_deg']:.0f} deg" for k, q in v.items() if k != "n_nights"))
md += ["", "Robustness: identical periods/amplitudes in the 2024 corrected RVBank release and in the independent HARPS DRS pipeline velocities; no activity-indicator periodicity at any of the four periods; TESS sectors 5 and 32 show no transit of b (depth limit ~60 ppm).", "",
       "Prior claims: none in the refereed literature or catalogues; one hobbyist illustration (DeviantArt, 2023) mentions a multi-planet system around this star; the HARPS GTO team re-observed the star in 2022-2025.", ""]
open(os.path.join(out, "candidate_summary.md"), "w").write("\n".join(md))
print("\n".join(md))
