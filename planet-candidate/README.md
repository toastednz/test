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
