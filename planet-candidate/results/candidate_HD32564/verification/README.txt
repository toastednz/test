HD 32564 (HIP 23575, TIC 213078996) - verification package
===========================================================
Claim: four coherent radial-velocity signals (P = 2.5566, 11.064, 23.61, 49.13 d; K = 4.0, 3.3, 2.9, 1.9 m/s; the 1.635-d peak of a single-signal periodogram is the alias of 2.5566 d)
in public HARPS data of a very inactive G6V star, consistent with a compact system of 7-12 Earth-mass
(minimum mass) planets. Unpublished in the refereed literature as of 2026-10-09.

Files
- HD32564_rv_nightly_binned.csv : the 191 nightly-binned SERVAL NZP-corrected velocities (m/s) used in the analysis
  (HARPS RVBank, Trifonov et al. 2020, CDS J/A+A/636/A74). Columns: bjd, rv_ms, err_ms (+1 m/s jitter floor in quadrature), n_spectra.
- HD32564_harps_rvbank2024_all_spectra.csv : all 205 individual spectra from the 2024 corrected release
  (Perdelwitz et al. 2024, CDS J/A+A/683/A125, table4) with both pipelines (SERVAL 'DRVmlcnzp', DRS 'RVdrsnzp')
  and activity indicators (CRX, dLW, Halpha, NaD1/2, FWHM, Contrast, BIS).
- candidate_summary.json / .md : stellar parameters, Keplerian solution, derived quantities, all tests.
- keplerian.json, multisignal.json, activity_check.json : raw outputs of the fits and tests.
- tess_*_fullbls.json : TESS (sectors 5, 32) BLS transit checks at 1.635 d, 2.575 d (daily alias) and 11.06 d: no transit.
- *.png : periodogram stages, phase-folded Keplerian fits, single-signal vetting figure.

How to check independently (any tool):
1. Fit offsets (pre/post 2015-06-01) + linear trend; compute a generalised Lomb-Scargle periodogram of rv_ms vs bjd
   between 1.2 and 5000 d. Expect the highest single-signal peak at 1.6350 d (power ~0.40, FAP ~1e-17); after modelling the 11.06, 23.6 and 49.1-d signals jointly, its alias 2.5566 d fits far better (chi2 302 vs 404).
2. Subtract a sinusoid at 1.6350 d; the residual periodogram should peak at 11.06 d, then 23.6 d, then 49.0 d.
3. Compare the inner-signal aliases 1.635, 1.6423, 2.5566 and 2.575 d with the other three signals fixed: 2.5566 d wins (chi2 302, 404, 769, 964 respectively).
4. Check indicators (CRX, dLW, Halpha, FWHM, BIS) show no power at any of the four periods.
5. Split the data by season: K and phase of the 1.635-d and 11.06-d signals should agree season to season.
Known caveats: single instrument; the HARPS GTO team (PI Udry) owns/observed the data and re-observed the star in
2022-2025; a 2023 DeviantArt illustration by a hobbyist mentions a multi-planet system around this star.
