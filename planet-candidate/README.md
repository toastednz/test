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
