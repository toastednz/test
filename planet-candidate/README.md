# Searching TESS data for an uncatalogued transiting-planet candidate

This directory contains a from-scratch transit search over public TESS 2-minute-cadence light
curves, aimed at finding a planet candidate that is **not** in any existing catalogue
(TESS Objects of Interest, Community TOIs, or the NASA Exoplanet Archive).

> Results, the candidate, its vetting evidence and caveats are in the sections below the
> method description (filled in at the end of the run).

## Data and catalogues used (all public, all fetched live on 2026-10-08)

| Source | What | Why |
|---|---|---|
| MAST / SPOC | TESS 2-min PDCSAP light curves, sectors 1–108 | the photometry searched |
| MAST / SPOC | Target pixel files for selected sectors | pixel-level (centroid) vetting |
| MAST | Per-sector 2-min target lists (bulk-download scripts) | which stars have data in which sectors |
| MAST | SPOC Threshold Crossing Event (TCE) tables, all single- and multi-sector runs through sector 107 | to tell whether a signal was already seen by the NASA pipeline |
| ExoFOP | TOI and CTOI lists (downloaded today) | exclusion of claimed candidates |
| NASA Exoplanet Archive | `pscomppars` (confirmed planets) | exclusion of known planet hosts |
| MAST | TESS Input Catalog v8.2 | stellar radii/temperatures for target selection and planet-radius estimates |
| Gaia DR3, SIMBAD | neighbours, binarity flags, identifiers | contamination / known-object checks |

## Target selection

The best chance of a *new* small-planet signal is around small stars (deeper transits for a given
planet) with data the catalogues have not caught up with. The TIC was queried for cool dwarfs
(T_eff 2700–4000 K, R < 0.65 R_sun, T_mag < 12.5): 41,022 stars, of which 24,103 have 2-min data.
After removing every star that is a TOI, CTOI or confirmed-planet host, 23,705 remain. These were
prioritised into:

* **G3** – 75 stars observed only in sectors ≥ 103 (2026), where no TOI releases exist yet.
* **G1** – 1,341 stars with 2–12 sectors including at least one sector ≥ 97 (data newer than the
  last SPOC multi-sector run).
* **G4** – 2,186 dwarfs of any temperature (R < 1.2 R_sun, T_mag < 13.5) whose *first* 2-min data
  arrived in sectors 103–107.
* A parallel track: SPOC TCEs on the clean cool-dwarf sample that were never promoted to TOIs,
  filtered to physically plausible transit durations.

## Search method (`scripts/tsearch2.py`)

1. Download every 2-min SPOC light curve for the star; keep PDCSAP flux with the default
   quality bitmask; normalise each sector.
2. Bin to 10 minutes; detrend each sector with a biweight filter (window 0.6 d, `wotan`);
   clip flares (positive outliers only).
3. **Stage A** – group sectors into contiguous blocks and run a Box Least Squares search
   (astropy, SNR objective) on each block over 0.5 d to min(60 d, baseline/2) with an
   Ofir-style period grid (duration-scaled frequency spacing, oversampling 3) and durations
   0.5–6 h.
4. **Stage B** – refine each block peak (SNR ≥ 5) on the *full* multi-year data set with a fine
   local grid around P, P/2 and 2P; record SNR, number of transits, odd/even depth difference,
   secondary-eclipse depth at phase 0.5 and per-transit depths.

The pipeline was validated on L 98-59 (TIC 307210830): it recovers planet c at P = 3.6907 d
with SNR 146 in 71 s for 27 sectors.

## Triage (`scripts/03_triage.py`)

Signals need SNR ≥ 7, ≥ 3 transits, 150 ppm < depth < 15 %, odd/even difference < 3σ,
|secondary| < 4σ, and a duration below 2.5× the maximum central-transit duration for the star's
density. Each signal is cross-matched against every SPOC TCE on the same star (P, P/2, 2P, P/3, 3P)
and against TOIs within 3 arcmin (contamination), and flagged if it sits near the 13.7-day TESS
orbital period or its harmonics.

## Vetting (`scripts/04_vet.py`, `06_context.py`, `07_centroid.py`)

* Re-fit on 2-min data; odd/even depths; secondary eclipse; per-transit and per-sector depths;
  chi-square of per-transit depths; SNR with the single strongest event removed; Transit Least
  Squares over a wide period range (meaningful SDE) with stellar parameters from the TIC.
* Gaia DR3 neighbours within 1′ (flux contamination), RUWE and non-single-star flags; SIMBAD;
  nearby TOIs; all SPOC TCEs on the star.
* Difference imaging from the target pixel file: out-of-transit minus in-transit image, per-pixel
  depth map, difference-image centroid versus the star's WCS position, with a noise estimate
  from random-phase fake transits.

## Results so far (updated as runs complete)

### Track A – SPOC TCEs on cool dwarfs that were never promoted to TOIs

15,923 TCEs sit on the 23,705 clean cool dwarfs. Filtering to SNR ≥ 8, R_p < 5 R_⊕, ≥ 3 transits and
a physically plausible duration leaves 566 TCEs on 406 stars. The 24 strongest planet-like ones were
re-vetted on the 2-min data:

| Outcome | Count | Examples |
|---|---|---|
| Eclipsing binary (secondary eclipse at phase 0.5, ≥ 5σ) | 7 | TIC 290003896, 238872494, 311188656, 181015118, 256324377 |
| Ellipsoidal / rotational variable (brightening at phase 0.5, inconsistent depths) | 6 | TIC 402980664, 189565557, 237286849, 140045538 |
| Single deep event with aliases (per-transit depths inconsistent, χ²_red ≫ 3) | 9 | TIC 272550631, 359313701, 289726188, 593228 |
| Flare-like dip + brightening | 1 | TIC 401283888 |
| **Transit-like and clean, but already claimed** | 1 | TIC 293689266 = GJ 237 A: P = 14.81 d, 1.0–1.5 ppt, 12 transits over 7 years, no secondary. The companion GJ 237 B (TIC 293689267, 7″ away, blended) carries **CTOI 293689267.01** at this period (submitted 2019). Not new. |

Lesson applied to the pipeline: a signal must be checked against TOIs/CTOIs of *every* star within
the photometric aperture, not just the searched TIC ID.

### Track B – blind search, run 1 (G3 + G1: 1,416 cool dwarfs, 2–12 sectors each, data through sector 108)

* 1,416 stars searched; 403 stars have at least one BLS peak with SNR ≥ 7; 138 stars pass the physical
  cuts; after requiring per-transit repeatability (≥ 4 measured transits, ≥ 75 % positive, no single
  event > 3× the median) 7 signals on 7 stars remained, all shallow (0.2–1.3 ppt, 0.5–1.6 R_⊕ if real)
  at combined SNR 7–10.
* The decisive test, a fully coherent BLS periodogram over the star's entire multi-year baseline
  (2–3 × 10⁵ trial periods), rejects all seven: candidate SDE 3.6–6.2, never the global maximum
  (`results/vet_blind_fast/*/fullbls.json`). Their "transits" are consistent with noise selected by
  the search.

| TIC | Star | P (d) | depth (ppm) | transits | SNR w/o strongest | χ²_red | coherent SDE / rank |
|---|---|---|---|---|---|---|---|
| 231055581 | L 173-19, M2.0Ve, 8.2 pc, T=9.3 | 18.50 | 245 | 9 | 8.0 | 2.6 | 3.6 / 9 |
| 245949052 | LP 475-1699, M1, 47 pc | 19.17 | 691 | 5 | 7.9 | 1.2 | 4.0 / 9 |
| 220524896 | | 12.11 | 606 | 13 | 9.0 | 4.4 | 4.0 / 9 |
| 332286707 | T=9.0 | 25.95 | 228 | 7 | 9.4 | 6.5 | 5.1 / 2 |
| 435905591 | | 46.78 | 587 | 4 | 7.8 | 3.9 | 4.3 / 9 |
| 456894306 | | 24.51 | 1258 | 8 | 8.3 | 3.4 | 5.0 / 9 |
| 423211395 | | 6.004 | 1093 | 31 | 7.1 | 1.5 | 6.2 / 5 |

* Signals that the box search ranked highest by raw SNR (up to SNR 70) were without exception
  stellar: spotted rapid rotators, flares, and single scattered-light dips, caught by the per-transit
  χ² and the secondary-eclipse test.

After the full run 1 triage (1,416 stars), a second fast consistency pass over the next 80 ranked
signals found 11 more repeatable ones; the 8 that were not variability or SPOC-known were put through
the coherent periodogram test and all failed (candidate SDE 2.5–5.0; `results/vet_blind_fast/*/fullbls.json`).
The two best-looking of these were also checked at pixel level and in Gaia: TIC 77840675 (24.06 d,
1.2 ppt, 4 transits) sits 53″ from a star 2.4 mag brighter (contamination ratio 1.8, RUWE 2.0) and
its difference image peaks on that neighbour; TIC 364979563 (BD−07 184 AB, 6.8″ binary, 25.4 d,
0.7 ppt, 3 transits) shows no transit in its sector-97 difference image. Neither is credible.

### Track C – the one uncatalogued, persistent, on-sky-localised eclipse signal: TIC 404664386 (TYC 8377-835-1)

**What was found.** The blind search flagged TIC 404664390 (an M dwarf, T = 12.4, 78 pc) with a
~1 % deep signal at P = 0.6533 d in its sector-104 2-min data (32 transits, all positive,
χ²_red = 1.9, TLS SDE = 20). SPOC's pipeline recorded the same signal as a raw TCE on this M dwarf in
July 2026; it is not a TOI, not a CTOI, not in the Exoplanet Archive, and neither star returns any
literature hit. Pixel-level difference imaging (`results/vet_blind/404664390_P3.268/centroid_s104.png`)
puts the dimming source on the **brighter background G dwarf 14″ away, TIC 404664386** (TYC 8377-835-1,
T = 11.5, T_eff = 5612 K, R = 0.91 R_⊙, 241 pc), whose own QLP full-frame-image light curves show the
signal in **2019 (S13), 2025 (S94) and 2026 (S104)** with a constant depth
(`results/candidate_TIC404664386/candidate_folds.png`):

| Data set | depth (ppm) | odd / even (ppm) | secondary at phase 0.5 (ppm) |
|---|---|---|---|
| TIC 404664386 QLP S13 (2019, 30-min) | 8840 ± 326 | 9241 ± 467 / 8829 ± 447 | 196 ± 329 |
| TIC 404664386 QLP S94 (2025, 200-s) | 8560 ± 140 | 8898 ± 191 / 8191 ± 199 | −91 ± 142 |
| TIC 404664386 QLP S104 (2026, 200-s) | 8848 ± 134 | 9305 ± 185 / 8379 ± 187 | 9 ± 136 |
| TIC 404664390 SPOC 2-min S104 (blended aperture) | 10111 ± 186 | 10868 ± 259 / 9355 ± 259 | 491 ± 179 |

TLS on S94+S104: P = 0.653279 ± 0.000056 d, SDE = 99, 63 distinct transits, r_p/R_⋆ = 0.088.
Period from the 7-year baseline: 0.6532993 d (alias spacing 1.1 × 10⁻⁵ d).

**Planet or binary?** Taken at face value the occulter is 0.78 R_Jup on a 0.65-day orbit around a
G dwarf (T_eq ≈ 2100 K), which would be the shortest-period giant planet known (TOI-2109 b: 0.672 d).
Three independent tests were run (`results/candidate_TIC404664386/`, `results/vet_blind/404664390_P0.653/`):

1. *Mass from the phase curve.* A BEER fit to the out-of-eclipse QLP photometry (S94+S104, 13,139
   points) gives an ellipsoidal amplitude of 10 ± 29 ppm. At a/R_⋆ = 3.5 the expected amplitude is
   34 ppm per Jupiter mass, 450 ppm for 13 M_Jup and 3600 ppm for a 0.1 M_⊙ star, so **any companion
   orbiting the G dwarf itself is < 3 M_Jup** (3σ). A brown dwarf or M-dwarf companion *to the G dwarf*
   is excluded.
2. *Eclipse shape.* A trapezoid fit gives T_23/T_14 = 0.15 ± 0.02 (T_14 = 1.45 h): the eclipse is
   **V-shaped**. A non-grazing 0.088 R_⋆ planet would give T_23/T_14 = 0.7–0.8; a grazing planet would
   be V-shaped but only ≈ 1.0 h long.
3. *Odd/even depths.* Odd eclipses are 8–10 % deeper than even ones in S94 (2.6σ), S104 (3.5σ) and
   the SPOC data (4.1σ, same photons as QLP S104), with consistent parity: ≈ 4σ combined.

Points 2 and 3 are the signature of an eclipsing binary whose true period is 1.3066 d with two
slightly unequal, partial (V-shaped) eclipses, diluted by the G dwarf's light. Point 1 shows the
binary is not the G dwarf plus a stellar companion; the simplest picture is a **fainter near-twin
eclipsing binary blended within a few arcsec of TYC 8377-835-1** (the difference-image centroid is
within 0.1–0.2 pixel of it). A grazing giant planet is not strictly excluded but requires the
odd/even asymmetry to be a systematic.

**Verdict.** A genuine, uncatalogued, seven-year-stable eclipse signal on a star that no catalogue
lists, but on the TESS evidence it is more likely an eclipsing binary than a planet. It is reported
here as an eclipsing-binary-or-planet candidate needing ground-based follow-up (seeing-limited
photometry to separate the two stars, and radial velocities of the G dwarf), not as a planet claim.

### Track B – blind search, run 2 (G4 + G1b: 2,309 stars; dwarfs first observed in sectors 103–107 plus long-baseline cool dwarfs)

2,309 stars searched; 854 have a peak with SNR ≥ 7; 258 pass the physical cuts; 69 stars carry a
repeatable (red-noise-aware) signal that is not claimed by any TOI/CTOI. The strongest "planet-like"
one, TIC 142884338 (LEHPM 3325 A, K4–5 dwarf, T = 10.3, 67 pc, co-moving M-dwarf companion 9″ away;
~600 ppm, 22 "transits" at 2.008 d, no SPOC TCE), turned out on closer inspection to have a true
period of 0.4015 d (9.6 h) with a broad, asymmetric, quasi-sinusoidal modulation rather than a
box-shaped transit (`results/candidate_TIC142884338/alias_folds.png`): stellar variability or an
ellipsoidal/contact binary in the blend, not a planet. Its 2.008-d and 0.803-d detections were 5:1
and 2:1 harmonics of that modulation. The remaining repeatable signals were fast-vetted and the
survivors put through the coherent-periodogram test (results appended below).

Run-2 coherent-periodogram results for the ten repeatable, unclaimed, non-TCE survivors
(`results/vet_blind_run2/*/fullbls.json`): candidate SDE 2.2–5.4, none a significant global maximum.
In every case the star's true dominant periodicity is a short-period (0.4–0.8 d) variability of which
the "transit" period was a harmonic. One survivor (TIC 161098507) shows a 5σ secondary eclipse
(eclipsing binary); another (TIC 153125761) is already a SPOC TCE at the true 0.52-d period.

## Bottom line

| | Stars / signals examined | Credible new planet candidate |
|---|---|---|
| Track A: unpromoted SPOC TCEs on cool dwarfs | 566 TCEs filtered, 24 re-vetted | none (7 EBs, 6 variables, 9 single events, 1 flare, 1 already a CTOI on a blended companion) |
| Track B, run 1: 1,416 cool dwarfs, 2–12 sectors incl. 2026 data | 793 stars with SNR ≥ 7 peaks, 15 fully vetted | none (all fail the coherent-periodogram test; 2 are blends) |
| Track B, run 2: 2,309 dwarfs first observed in 2026 + long-baseline cool dwarfs | 854 stars with SNR ≥ 7 peaks, 20 fast-vetted, 10 coherent-tested | none |
| Track C: the one persistent, pixel-localised, uncatalogued eclipse | TIC 404664386 / TYC 8377-835-1, P = 0.6533 d, 7-year baseline | **eclipsing-binary-or-planet candidate; EB favoured** (V-shaped, 4σ odd/even asymmetry), companion to the G dwarf itself < 3 M_Jup |

**No signal found in this search can honestly be called a new planet candidate.** The clearest
genuinely uncatalogued object is the 0.6533-day eclipse signal on TYC 8377-835-1, which the NASA
pipeline attributed to the wrong (M-dwarf) star and which no catalogue lists; the TESS data favour a
blended eclipsing binary over a planet, and ground-based photometry at ~1″ resolution plus a radial-velocity
check of the G dwarf would settle it. Everything else that looked planet-like at the box-search stage was
stellar activity, flares, scattered light, eclipsing binaries, or statistically insignificant once the full
multi-year periodogram was computed.

Why this is the expected outcome: the 2-min TESS targets have been searched by the SPOC pipeline
(single- and multi-sector) and by many groups for seven years; the residual discovery space for small
stars is dominated by low-SNR signals (SNR 7–10), where the false-alarm rate from red noise is high.
A search with a better chance of success would need either data the pipelines have not combined yet
(the 2026 sectors were included here, but SPOC single-sector runs already cover them), or systematic
re-processing with detrending tuned to active M dwarfs, or the full-frame-image stars fainter than the
QLP magnitude limit.

## Reproducing

```
python3 -m venv venv && venv/bin/pip install numpy scipy astropy matplotlib pandas lightkurve astroquery transitleastsquares wotan requests
DATA=/path/to/data   # ~1 GB of catalogues, light curves are streamed and deleted
venv/bin/python scripts/01_query_tic.py $DATA/catalogs/tic_cool_dwarfs.csv
# download MAST bulk lc scripts into $DATA/lclists, TCE tables into $DATA/tce, TOI/CTOI/pscomppars into $DATA/catalogs (see README top)
venv/bin/python scripts/02_build_sample.py $DATA
venv/bin/python scripts/tsearch2.py $DATA targets.csv results/search.csv --workers 4
venv/bin/python scripts/03_triage.py $DATA results/search.csv results/triage.csv
venv/bin/python scripts/05_vet_batch.py $DATA results/triage.csv results/vet --n 20 [--tls]
venv/bin/python scripts/08_fullbls.py $DATA <TIC> <P> results/vet/<dir>       # coherent periodogram
venv/bin/python scripts/07_centroid.py $DATA <TIC> <sector> <P> <t0> <dur_h> <outdir>   # pixel test
venv/bin/python scripts/06_context.py $DATA <TIC> [P]                           # Gaia/SIMBAD/TOI/TCE
```

All search outputs are in `results/` (`search_run1.csv`, `search_run2.csv`, `triage_run*.csv`, the
per-candidate vetting directories, and `candidate_TIC404664386/` for the one object worth following up).

## Second round: different approaches (2026-10-09)

### D. Adding full-frame-image light curves to the marginal candidates

The 14 best marginal blind-search signals were re-measured in every QLP / TESS-SPOC full-frame-image
sector not already used (`scripts/10_ffi_extend.py`, `results/ffi_extend.json`). The deep, long-duration
ones (TIC 248285521, 161098507, 153125761, 76673558) do persist in 2019–2023 data at high SNR but
remain eclipsing-binary-like; every shallow planet-like signal disappears in the independent data
(e.g. BD−07 184: nothing at the ephemeris in S30/S97 QLP). TIC 143951327 (13.34 d, 1.3–2 ppt,
4 events) kept a 4σ hint in FFI data, but its events exist only in the PDC-corrected flux, not in the
raw aperture flux, and coincide with elevated background: a correction artifact. Lesson added to the
vetting: compare raw (SAP) and corrected (PDCSAP) depths and check the background at transit times.

### E. Mining SPOC's own centroid statistics for signals on the wrong star

11,018 planet-like TCEs carry a significant difference-image centroid offset. For the 500 shallowest
on unclaimed stars the neighbour at the offset position was identified in the TIC and its own light
curves folded at the TCE ephemeris (`scripts/11_wrong_host.py`, `12_neighbour_check.py`,
`results/wrong_host_tces_shallow.csv`, `results/neighbour_check.json`). 22 neighbours would host a
planet-sized signal; on their own light curves 18 show a secondary eclipse or a brightening at phase
0.5 (eclipsing binaries, like TYC 8377-835-1), the rest are too faint or ambiguous. No planet.

### F. Residual search around 275 known transiting-planet hosts  → **one credible new candidate**

Known TOI/CTOI transits (358 ephemerides) were masked and the two-stage search re-run on the cool-dwarf
hosts (`results/search_hosts.csv`, `triage_hosts.csv`). Fifteen repeatable signals do not match any
known period; four were fully vetted with the known planets masked, a raw-flux check and a masked,
fully coherent periodogram (`results/vet_hosts/`):

| Host | new P (d) | depth (ppm) | transits | coherent SDE (masked) | verdict |
|---|---|---|---|---|---|
| **TIC 286763141 = TOI-6284 (L 463-104, M3, 21 pc, T=9.7)** | **7.3493** | **403 ± 31** | **20 / 20 positive** | **11.1, global max** | **new Earth-sized candidate** |
| TIC 275083922 (M dwarf, 43 pc, crowded field) | 2.9263 | 1543 (PDC) / 1025 (raw) | 23 | 12.1, global max | real signal, SPOC-known since 2019 but never promoted; pixel centroid offset 9–11″ in two sectors and a crowded field → host ambiguous |
| TIC 422217860 = TOI-5662 | 4.9921 | 1657 | 8 | 8.0, global max | marginal (SNR 8) |
| TIC 277634430 = TOI-771 | 4.1846 | 806 | 35 | 6.7, rank 7 | not significant |

**TOI-6284 candidate c (unofficial), `results/candidate_TOI6284/`:**

* 20 transits across sectors 9, 62, 63, 89, 90, 99 (2019–2026), every one positive, per-sector depths
  385–495 ppm (χ²_red = 1.0), combined SNR 15.0 (13.7 without the strongest event), identical with
  and without masking the known 3.45-d candidate.
* Fully coherent BLS over the 7-year baseline (167,000 periods, 0.5–70 d, known candidate masked):
  the 7.349-d peak is the global maximum, SDE = 11.1; the next unrelated peak has SDE 7.4.
  TLS on the sectors with transits: SDE 16.
* Odd 315 ± 49 / even 463 ± 40 ppm (2.3σ); secondary at phase 0.5: −75 ± 34 ppm (none).
* Raw SAP depth / PDCSAP depth = 1.08 and normal background during transit: not a correction artifact.
* Host isolated: contamination ratio 0.02, nearest Gaia source 8 mag fainter at 13″; RUWE 1.19.
* SPOC's pipeline detected the same signal (TCE 00286763141-01, SNR 11.2, 19 transits, multi-sector
  run through sector 96, 2025); it is not a TOI, not a CTOI, not in the Exoplanet Archive, and a
  literature search returns nothing.
* Implied planet: R_p ≈ 1.0 R_⊕ (0.95–1.02), P = 7.3493 d, a = 0.058 au, a/R_⋆ = 26, T_eq ≈ 490 K,
  ≈ 9.5 × Earth's insolation; transit duration 1.5–1.6 h implies b ≈ 0.7. Period ratio to TOI-6284.01
  is 2.13, just wide of 2:1, as is common in compact multi-planet systems.

Caveats: SNR ~14 is modest (a few per cent of such signals are red-noise artifacts even after these
tests); the pixel test cannot localise a 400-ppm transit; and the odd/even difference is 2.3σ. The
natural follow-up is to request a TESS DV report check, submit it as a CTOI, and obtain ground-based
confirmation (the 3.45-d candidate TOI-6284.01 is itself still a PC).

### Follow-up checks on the TOI-6284 candidate (2026-10-09, second pass)

* **SPOC's own data-validation report** (`results/candidate_TOI6284/spoc_dv_summary_tce01_s0001-s0096.pdf`,
  run s0001–s0096, generated 2025-12-25, "TOI 6284: No Ephemeris Match"): MES 10.2, SNR 11.2,
  depth 469 ± 48 ppm, 19 transits, odd/even difference 0.65σ, weak-secondary MES 2.5 (none),
  bootstrap false-alarm probability 2 × 10⁻²⁵, difference-image centroid 5.7 ± 3.9″ from the target
  (1.5σ, i.e. on target, 5/5 sectors usable), ghost diagnostic negative, R_p = 1.14 ± 0.25 R_⊕,
  b = 0.84 ± 0.39, T_eq = 447 ± 20 K. The pipeline's second TCE on the star is the known
  TOI-6284.01. No red flags.
* **Independent data never used before**: TESS-SPOC and QLP full-frame-image light curves of sectors
  35 and 36 (2021) show the transit at the predicted ephemeris, 423 ± 100 and 467 ± 136 ppm
  (TESS-SPOC), combined FFI-only 541 ± 64 ppm (8.5σ, 6 transits); every FFI pipeline reproduces
  the depth in each 2-min sector (`results/candidate_TOI6284/ffi_extend.json`). Total: 26 transits in
  8 sectors from 2019 to 2026.
* **Empirical false-alarm test** (`scripts/13_bootstrap_fap.py`, `results/candidate_TOI6284/bootstrap_fap.json`):
  the fully coherent masked search (343,000 periods, 0.5–70 d) repeated on nine light curves whose sectors were
  circularly shifted by random offsets (same noise, no coherent signal). The strongest peak anywhere in those
  nine periodograms reached SDE 5.0–6.3; the real 7.349-d peak has SDE 11.1. Zero of nine trials come close.
* **Numbers for follow-up** (`results/candidate_TOI6284/next_steps_numbers.json`): RV semi-amplitude
  ≈ 0.6 m/s for 1.1 M_⊕ (below current precision for an M3 dwarf, so a mass is not realistic);
  TSM ≈ 54 (J = 8.33), ESM ≈ 1.2 (K = 7.46); next transits every 7.3493 d with ±0.1 h ephemeris
  uncertainty (list in the JSON, starting 2026-10-16 09:37 UTC); **TESS will re-observe the star in
  sectors 110–113**, which should add ~16 transits and push the SNR past 20.
* `results/candidate_TOI6284/ctoi_submission_table.csv` holds the parameters in ExoFOP's CTOI format.

**Recommended next steps, in order**

1. Submit it as a Community TOI on ExoFOP (needs a registered account; the table above has the
   values) so the claim is on record before the SPOC s1–s96 TOI release, which will probably alert
   this TCE within months.
2. Ask for CHEOPS time (the only facility besides TESS that detects 400 ppm on a T = 9.7 star in a
   single transit) at one of the predicted times to confirm the depth and sharpen the ephemeris.
3. Rule out blends: seeing-limited photometry of the Gaia neighbours at a predicted transit time
   (any eclipsing binary within ~30″ would need a ≥ 50 % eclipse to mimic 400 ppm), and speckle or
   adaptive-optics imaging for companions inside 1″.
4. Reconnaissance spectroscopy (one or two spectra) to confirm a single, slowly rotating M3 dwarf
   and refine R_⋆, which sets R_p.
5. Statistical validation (TRICERATOPS/VESPA-style false-positive probability) with the TESS data,
   the DV centroid result and the imaging constraints; this is how Earth-sized TESS planets around M
   dwarfs are usually confirmed when a mass is out of reach.
6. Wait for sectors 110–113 (2027), re-run the coherent search and a joint two-planet fit; check
   for transit-timing variations between the 3.45-d and 7.35-d signals (period ratio 2.13).

### Correction after independent verification (2026-10-09)

An independent re-analysis by a second AI (from the verification package, using the original MAST
FITS files) **reproduces the detection**: strongest blind peak at 7.3493 d, 445 ± 36 ppm in both SAP and
PDCSAP, 20 of 20 baselined events positive, no secondary at phase 0.5, odd/even 2.1σ, radius ≈ 1.08 R_⊕.
It also corrected four of my statements, all accepted:

* SAP/PDCSAP depth ratio is ≈ 1.00, not 1.08 (my SAP measurement used a cruder baseline).
* "Centroid on target" overstates a 5.7 ± 3.9″ offset; the pixel data do not localise a 400-ppm dip.
* Three predicted events are not usable: the sector-9 first event lacks baseline, the sector-63 epoch-200
  event starts at mid-transit with background structure, and the sector-99 epoch-342 event falls in a gap.
* A weak feature near phase 0.73 (~150 ppm) has p ≈ 0.05 after accounting for the phase search; not a
  detection, but to be re-tested with sectors 110–113.

**Literature status, and it changes the headline.** The verifier found a preprint my web searches had
missed: Tschudi (2026), arXiv:2607.23781, *A uniform transit survey of 461 ExoFOP M-dwarf TOI hosts*,
submitted 26 July 2026. Checked directly: it reports TOI-6284 as "a candidate three-planet chain", with
two new blind detections beside TOI-6284.01: **P = 5.24 d (SDE 23.8, 33 events) and P = 7.35 d
(SDE 24.0, 26 events)**, Gemini speckle imaging of the field, and a ground-based nearby-eclipsing-binary
check. So the 7.349-d signal was reported publicly ten weeks before this search, and the 5.24-d
feature the verifier flagged is its second candidate. My pipeline recovers that one too once both known
signals are masked (`results/candidate_TOI6284/third_signal_5p24d_check.json`: global maximum, SDE 8.2,
26/26 events positive, 335 ± 34 ppm, χ²_red = 1.2, odd/even consistent, no secondary).

What this work therefore is: an **independent confirmation** of both Tschudi (2026) candidates from a
different pipeline, with additional evidence (sector-99 data, sector 35/36 FFI transits, a masked coherent
periodogram, a sector-shuffle false-alarm test, SPOC's DV report), plus one substantive point for the
author and the TESS follow-up group: the verifier showed that the archived LCO-SAAO nearby-eclipsing-binary
observation (BJD 2460325.36–2460325.52) falls at phase 0.32–0.34 of the 7.349-d ephemeris, so it does not
clear the field for this signal, contrary to the preprint's use of it. A CTOI submission by us would be a
duplicate under ExoFOP's rules; the useful contributions are a confirmation note and that correction.

## Third round: a different data set – archival radial velocities (2026-10-09)

### G. Blind search of the public HARPS RVBank for unpublished periodic signals

The user asked for "other avenues". Transit photometry had been exhausted, so the search moved to the
other main discovery channel: 18 years of public HARPS radial velocities, re-reduced homogeneously in the
HARPS RVBank (Trifonov et al. 2020, CDS J/A+A/636/A74; cross-checked with the 2024 corrected release,
Perdelwitz et al. 2024, J/A+A/683/A125). `scripts/14_rvbank_search.py` runs, for each of the 543 stars with
≥ 40 usable spectra: nightly binning, 5σ clipping, removal of a linear trend and of the pre/post-2015 fibre
offset, a floating-offset generalised Lomb–Scargle periodogram over 1.2–5000 d, a Baluev false-alarm
probability, the same periodogram of the SERVAL/DRS activity indicators (CRX, dLW, Hα, Na D, FWHM, BIS,
contrast), and checks against the 1-day, 1-year and window-function aliases. `scripts/15_rv_vet.py` then
vets the best signals (sector-shuffle bootstrap FAP, first/second-half and pre/post-2015 amplitude and
phase consistency, residual second signal, indicator correlation and power at the period).

**Known-planet matching had to be rebuilt.** The first pass matched hosts to the NASA Exoplanet Archive by
coordinates only and missed (a) high-proper-motion stars (ε Indi A) and (b) the 2011 HARPS planets that
the NASA archive does not list because their paper was never refereed. `scripts/16_rv_known_match.py` now
matches by HD/HIP/GJ/TIC name against exoplanet.eu and the NASA archive and by position within 3′
(`results/rvbank_search_matched.csv`): 218 of the 543 stars have known planets and 131 of the detected
signals are known planets. That is the validation of the method: it recovers, blind, e.g. HD 157172 b
(105 d), HD 150433 b (1096 d), HD 215456 b (192 d) and c, all from Mayor et al. (2011), and GJ 3822 b
(Tuomi et al. 2019 candidate, 661 d) at the right periods and amplitudes.

**Literature check of every survivor** (`results/rv_survivor_bibliography.csv`, SIMBAD bibliography of each
star, plus targeted reading): HD 41248's 25.6-d signal is the known activity-driven false planet
(Faria et al. 2020); ζ Tuc's 267-d signal is the 1-yr alias of its ~950-d activity cycle; HD 3964's
3.1-yr signal is tied to its magnetic cycle (Frensch et al. 2023); HD 13060's 2800-d signal is a cycle
(its rotation is 34 d, Yu et al. 2024, and the signal correlates with CRX, dLW, FWHM, BIS); GJ 479's 11.3-d
signal is the Tuomi et al. (2019) candidate; HD 297396's 4.27-d signal was posted as a candidate on Zenodo
on 2026-10-08 by an independent researcher (Fraser 2026b, doi:10.5281/zenodo.23249329), one day before
this analysis. All survivors with a Baluev FAP < 10⁻⁴, no alias or indicator flag in the first pass and no known planet
(35 stars) were vetted individually (`results/rv_candidates/*/rv_vet.json`, `multisignal.json`,
`activity_check.json`, `keplerian.json`):

| star | P (d) | K (m/s) | nights | verdict |
|---|---|---|---|---|
| HD 157172 | 105.1 | 4.8 | 123 | known: HD 157172 b (Mayor+2011); eccentric, harmonic at 52 d |
| HIP 112414 = HD 215456 | 194 (+2156) | 2.9 | 143 | known: HD 215456 b, c (Mayor+2011) |
| GJ 634.1 = HD 150433 | 1022 | 3.1 | 113 | known: HD 150433 b (Mayor+2011) |
| GJ 3822 | 619 | 6.0 | 66 | known candidate (Tuomi+2019, 661 d) |
| GJ 479 | 11.30 | 4.3 | 57 | known candidate (Tuomi+2019, 11.292 d) |
| HD 297396 = TOI-6263 | 4.268 | 5.5 | 101 | claimed 2026-10-08 in a Zenodo preprint (Fraser 2026b) |
| HD 41248 | 25.6 | 2.9 | 164 | known activity signal (Faria+2020) |
| ζ Tuc (GJ 17) | 267 | 1.0 | 276 | 1-yr alias of the ~950-d activity cycle |
| HD 3964 | 1136 | 8.6 | 45 | magnetic cycle (Frensch+2023) |
| HD 13060 | 2835 | 3.3 | 92 | cycle; correlates with CRX, dLW, FWHM, BIS |
| GJ 3436, HD 95456, GJ 838, HD 200633, GJ 1085 | 1400–3700 | 2–8 | 45–172 | long-period, indicator-correlated or amplitude unstable: cycles/trends |
| GJ 787, GJ 9592, GJ 224, GJ 204, GJ 472, GJ 656, HD 125881, GJ 9527, HD 78286, GJ 579.2, HD 36152, GJ 616 (18 Sco), GJ 812.1, HD 114853, HD 45346 | 5.6–102 | 0.7–12 | 37–438 | same period or correlation in activity indicators, or K not stable between halves: rotation/activity |
| GJ 845 = ε Indi A | 16.5 | 4.0 | 123 | amplitude 1.7 vs 4.3 m/s between halves, dLW/Na D: activity (known Jovian at 25 000 d not in range) |
| HD 32564 | 1.635, 11.06, 23.62, 48.97 | 4.2, 3.4, 2.9, 2.0 | 191 | **unexplained, coherent, four signals – section H** |
| HD 144628 (GJ 613) | 15.73 | 1.1 | 168 | weak possible: no indicator counterpart (rotation is 38.5 d, seen in dLW/FWHM/BIS at 40 d), ΔBIC 27, but period not stable in the joint fit (15.73 → 15.83 d) |
| HD 17970 (GJ 3187) | 72.3 | 1.7 | 74 | weak possible: no indicator counterpart, ΔBIC 30, K 1.3 vs 2.3 m/s between halves |
| HD 71334 (GJ 9263) | 88.9 | 3.0 | 66 | possible but suspect: ΔBIC 47, no literature, yet CRX anti-correlates (ρ = −0.31) with the signal |

The three "possible" rows are noted for completeness only; none passes every test the way HD 32564 does.

### H. The result: HD 32564, an apparently unpublished four-signal system  → **best candidate of the project**

HD 32564 (HIP 23575, TIC 213078996; G6V, V = 8.6, T_eff = 5574 K, R = 0.94 R_⊙, M = 0.98 M_⊙, 48.5 pc,
log R'_HK = −5.03, Gaia RUWE 0.97, single) was observed on 191 nights (205 spectra) between 2009 and 2016,
almost all under the HARPS GTO high-precision programme 183.C-0972 (PI Udry). It is in no planet paper, no
catalogue, and no arXiv listing. Its velocities contain four coherent signals
(`scripts/17_rv_multisignal.py`, `19_rv_keplerian.py`; `results/candidate_HD32564/`):

| signal | P (d) | K (m/s) | m sin i (M_⊕) | a (AU) | insolation (S_⊕) | T_eq (K) | drop-one FAP | ΔBIC |
|---|---|---|---|---|---|---|---|---|
| b | 1.6350 | 4.22 ± 0.17 | 7.3 ± 0.3 | 0.026 | 1100 | 1470 | 6e−39 | 62 |
| c | 11.0627 ± 0.0017 | 3.37 ± 0.15 | 11.1 ± 0.5 | 0.095 | 86 | 780 | 3e−27 | 84 |
| d | 23.622 ± 0.014 | 2.86 ± 0.15 | 12.1 ± 0.6 | 0.157 | 31 | 600 | 2e−23 | 65 |
| e | 48.97 ± 0.07 | 2.02 ± 0.15 | 10.9 ± 0.8 | 0.255 | 12 | 470 | 1e−7 | 58 |

The raw scatter of 4.8 m/s drops to 2.1 m/s (fitted jitter 1.0 m/s); eccentricities converge to zero;
no fifth signal (next peak FAP 0.009). Checks, all passed (`candidate_summary.json`):

* **Aliases.** The daily alias of b (2.575 d) has a third of the power; the yearly alias (1.6423 d) is
  disfavoured by Δln L = 38. The three longer periods are not aliases of each other.
* **Coherence.** Season by season (2009–10, 10–11, 11–12, 12–13) signal b keeps K = 3.3–4.7 m/s and phase
  −119 … −125°, signal c K = 3.0–3.4 m/s and phase −162 … −177°. Stellar activity does not hold phase for
  four years; planets do. Sector-shuffle bootstrap FAP for b: 0/300.
* **Activity.** The star is as quiet as the Sun at minimum (log R'_HK = −5.03, expected rotation 30–40 d,
  none detected by Yu et al. 2024). After removing long-term trends no indicator (CRX, dLW, Hα, Na D,
  FWHM, contrast, BIS) has power above 0.06 at any of the four periods (`activity_check.json`).
  Period ratios d/c = 2.14 and e/d = 2.07 sit just wide of 2:1, as in Kepler's compact systems, not at the
  exact harmonics a rotation signal would produce.
* **Independence from the reduction.** The same four periods and amplitudes come out of the 2024
  corrected RVBank release and of the separate HARPS DRS pipeline velocities (`rvbank2024/`, `drs_pipeline/`).
* **TESS.** Sectors 5 and 32 (2-min) show no transit at 1.635 d, 2.575 d or 11.06 d down to ~60 ppm
  (a 7 M_⊕ planet would give 300–900 ppm), so b does not transit (prior probability ~17 %).

Prior claims: none refereed. A hobbyist's illustration on DeviantArt (2023-09-06) is captioned as a
five-planet system "recently found" by that user in HARPS data of this star, and the HARPS GTO team
re-observed the star in 2022–2025 (programmes 108.22KV, 112.25YG), so the data owners are presumably
aware of it. Neither constitutes a publication. What can honestly be said: **a compact system of four
7–12 M_⊕ (minimum-mass) planet candidates around HD 32564 is present in public data and unreported in
the literature as of 2026-10-09.** `results/candidate_HD32564/HD32564_candidate_verification_package.zip`
contains the nightly velocities, all 205 spectra with both pipelines and indicators, the fits and tests, and
a recipe for independent checking.

### I. Masked residual search around 1,115 K/G/F TOI hosts  → **TOI-669 c, an unreported second transiting planet candidate**

Track F (section above) searched the cool-dwarf TOI hosts; this run extends it to every non-M TOI host with
2-min data (`targets_hosts_fgk.csv`, 1,115 stars, 1,858 known ephemerides masked). Triage needed two
changes for host stars (`03_triage.py`, host mode): a nearby TOI only counts as "claiming" a signal if its
period matches, and harmonic matching now covers ratios up to 6:1 and 3:2-type fractions, because the
residuals of imperfectly masked deep eclipses (FP/APC eclipsing binaries with 5–20 mmag eclipses) leak into
exactly those multiples. Stars carrying an FP/FA or > 3 mmag TOI were set aside. The survivors
(`results/triage_hosts_fgk_clean*.csv`) were vetted with `05_vet_batch.py` (`results/vet_hosts_fgk/`).

**TOI-669 (TIC 124573851)** — a G dwarf (T_eff 5600 K, 0.99 R_⊙, 0.90 M_⊙, T = 10.2) with the confirmed
sub-Neptune TOI-669 b (3.945 d, 2.6 R_⊕, 9.8 M_⊕; Akana Murphy et al. 2023). With b masked, the four
sectors (9, 35, 62, 89; 2019–2025) contain a second transit signal (`results/candidate_TOI669/`):

| quantity | value |
|---|---|
| period / epoch | 9.52922 d / BTJD 1550.991 (SPOC: 9.52925 ± 0.00004) |
| depth, duration | 414 ± 44 ppm, 2.4 h (SPOC 501 ± 59 ppm, 2.9 h, b = 0.90) |
| radius | 2.2 R_⊕ (SPOC 2.59 ± 0.35) at a = 0.085 AU, T_eq ≈ 840 K |
| transits | 10, all positive, χ²_red 1.6, combined SNR 12.1 (10.8 without the strongest) |
| odd / even | 428 ± 68 / 405 ± 56 ppm |
| secondary (phase 0.5) | 7 ± 53 ppm |
| masked coherent periodogram | global maximum, SDE 10.3; the only competing peaks are P/2, 2P, 3P |
| TLS | same period, SDE 12.7 |
| sector-shuffle bootstrap | 0 of 8 trials reach the real SDE (trial maxima 4.3–5.5) |
| SAP / PDC depth, background | 0.98, 1.00 |
| centroids | within 0.4–0.8 pixel of the target in all four sectors (low SNR); SPOC joint offset 8.9″ (1.8σ) |

SPOC's own s1–s96 data-validation run (Dec 2025) lists this as TCE 2 of 2 on the star: MES 7.6, odd/even
0.14σ, weak-secondary MES 2.9, bootstrap false-alarm 6 × 10⁻¹⁵, ghost diagnostic clean, "No Ephemeris
Match" — i.e. SPOC found it and nobody has yet turned it into a TOI (ExoFOP, live: TOI-669.01 only, no CTOI).
Independently, the TESS-Keck Survey paper on this system (Akana Murphy et al. 2023) notes "a less significant
peak near 9.6 d … in the periodogram of the RV residuals" and a two-planet fit giving m sin i = 5.0 ± 2.6 M_⊕
at 9.61 ± 0.52 d, which they could not distinguish from the window function and did not claim. A transit
ephemeris at 9.529 d fixes that period and makes the RV hint a plausible mass measurement in waiting.
P_c/P_b = 2.415. Verification package: `results/candidate_TOI669/TOI669c_candidate_verification_package.zip`.

**The other 24 vetted host signals** (`results/vet_hosts_fgk_summary.csv`, deep tests in `results/vet_hosts_fgk_deep/`):
15 fail quick vetting (depth mismatch between raw and corrected flux, odd/even differences, inconsistent per-transit
depths, negative transits, or a secondary eclipse: TOI-1824, 2080-like FPs, TOI-4299's 0.59-d signal with an 86 ± 24 ppm
secondary, TOI-7060's 12.7-d signal with a 143 ± 34 ppm secondary, …). Ten went through the full deep vetting
(masked coherent periodogram over all sectors, TLS, sector-shuffle bootstrap, per-sector difference-image centroids):

| host | P (d) | depth (ppm) | transits | coherent-periodogram rank / SDE | bootstrap | verdict |
|---|---|---|---|---|---|---|
| TOI-4298 (TIC 146282666) | 9.995 | 180 ± 15 | 13/13 | 1 / 10.2 | 0/6 | **possible** 1.7 R_⊕ candidate; TLS odd/even 0.2σ but box-fit odd/even 139 vs 228 ppm (2.9σ), per-sector depths χ²_red 2.4; centroids on target (low SNR); SPOC has no TCE at this period |
| TOI-6555 (TIC 259606227) | 1.0638 | 159 ± 12 | 56/61 | 1 / 10.7 | 0/6 | **possible** 2.6 R_⊕ ultra-short-period candidate around an evolved F star (R = 1.9 R_⊙); odd/even 164/154, no secondary, per-sector depths consistent, no sinusoidal variability at P; TLS prefers 2P |
| TOI-2289 (TIC 82452140) | 14.678 | 346 ± 37 | 10/10 | 1 / 8.2 | 0/6 | **possible** 2.0 R_⊕ candidate; odd/even and secondary clean, TLS SDE 10.9, but SAP/PDC depth 1.31, background in transit 0.64 × median and one sector's difference image peaks 1 pixel off target |
| TOI-1777 (TIC 29191624) | 6.410 | 215 ± 27 | 7/7 | 1 / 5.4 | 0/6 (max trial 4.9) | marginal; SAP/PDC 1.5 |
| TOI-2427 (TIC 142937186) | 22.20 | 628 ± 61 | 4/4 | 9 / 5.0 | – | rejected: not significant once the whole light curve is searched coherently |
| TOI-5392 (TIC 198512478) | 25.32 | 171 ± 21 | 7/7 | 4 / 4.9 | 6/6 | rejected |
| TOI-2091 (TIC 219778329) | 54.8 | 133 ± 19 | 14/15 | 9 / 3.7 | 6/6 | rejected (0.6-h "transits" at 55 d are also physically implausible) |
| TOI-6075 (TIC 424388628) | 14.73 | 153 ± 24 | 35/43 | 9 / 3.9 | 6/6 | rejected |
| TOI-6729 (TIC 426032475) | 37.6 | 158 ± 22 | 6/6 | 8 / 4.5 | 4/6 | rejected |
| TOI-7910 (TIC 270619211) | 6.527 | 133 ± 18 | 16/19 | 9 / 4.2 | 6/6 | rejected |

The three "possible" rows are weaker than TOI-669 c (no SPOC confirmation, no RV hint, one caveat each) and are listed
for completeness; they would need pixel-level and ground-based checks before any claim. The final triage of all 1,115
hosts (`results/triage_hosts_fgk_clean.csv`) produced no further clean signals beyond these 26 stars.

### J. TOI-1117 c: a published "non-transiting" RV planet that does transit

The same host search flagged a 4.579-d signal on **TOI-1117** (TIC 295541511, Sun-like, 1.05 R_⊙). The
NASA archive cross-match (now part of host-mode triage) showed why it looked unclaimed: Lockley et al.
(2025, arXiv:2506.05521) published this system as transiting sub-Neptune b (2.228 d) plus **two
non-transiting RV planets, c at 4.579 ± 0.004 d (m sin i = 8.78 M_⊕) and d at 8.665 d**, using only TESS
sectors 13 and 39. With b masked, five 2-min sectors (2019–2025) show transits at exactly planet c's period
(`results/candidate_TOI1117c/`): P = 4.57866 d, 451 ± 40 ppm, 1.5 h, 22 of 23 transits positive
(χ²_red 1.6, combined SNR 11.9), odd/even 519 ± 56 / 378 ± 57 ppm, no secondary (−4 ± 39 ppm), SAP/PDC
0.95, masked coherent periodogram global maximum (SDE 9.9, only harmonics compete), 0 of 6 sector-shuffle
trials reach it. Radius ≈ 2.3 R_⊕; with the published mass this gives a density of ≈ 4 g cm⁻³.

The decisive test used the paper's own HARPS table (133 velocities, extracted from the arXiv source):
fitting b at its transit ephemeris (K_b = 4.4 m/s recovered) and c at the transit period, the RV-predicted
inferior conjunction of c lands **+0.03 ± 0.03 in phase (+3 h) from the transit times**, 149 orbits away
(Δχ² = 0.8 at the transit phase, 29 at anti-phase). So the 4.579-d signal is planet c, and planet c
transits. This is not a new planet, but it is new: the paper, ExoFOP (no TOI-1117.02, no CTOI) and the
archive (`tran_flag = 0`) all list c as non-transiting, and a transiting 8.8 M_⊕, 2.3 R_⊕ planet at 4.58 d
next to a 2.46 R_⊕, 8.9 M_⊕ planet at 2.23 d (period ratio 2.055) is a measurable, dynamically interesting
pair. Package: `results/candidate_TOI1117c/TOI1117c_transit_verification_package.zip`.

**Revised bottom line for the whole project:** three results came out of the "other avenues": (1) **HD 32564**,
four coherent radial-velocity signals (1.635, 11.06, 23.6, 49.0 d; 7–12 M_⊕ minimum masses) in public HARPS data
(section H), unpublished; (2) **TOI-669 c**, a 2.2–2.6 R_⊕ transit candidate at 9.529 d around a confirmed-planet
host (section I), found independently by SPOC in Dec 2025 but never promoted to a TOI, matching a weak RV hint in
the published Keck data; (3) **TOI-1117 c transits** (section J): a published RV planet, listed everywhere as
non-transiting, shows 22 transits at its RV period and phase, which turns it into a planet with both mass and
radius. In the earlier pure-transit searches nothing new survived (TOI-6284's 7.35-d candidate was first reported
by Tschudi 2026).