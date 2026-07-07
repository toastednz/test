# Bottom-up NZ CPI nowcast

Reconstructs the quarterly New Zealand Consumers Price Index (CPI) movement
from the underlying component data that Stats NZ publishes **before** the
quarterly CPI release, aggregated the same way the official measure is
(chained Laspeyres with published expenditure weights). This is not a
forecasting model — it re-assembles the official number from its public
inputs, and only falls back to an assumption for basket items that have no
public monthly source.

## How much of the data is public?

**About 47% of the CPI basket (by expenditure weight) is published monthly**
by Stats NZ in the Selected Price Indexes (SPI) release, which lands roughly
two weeks after each month — so all three months of a quarter are public
about a week before that quarter's CPI. These are the *same collections*
that feed the CPI:

| Component (CPI class) | Weight (Dec-2024 basket) | Monthly since |
|---|---|---|
| Food (14 classes, full food price index) | 18.5% | 1960 (classes 2006) |
| Actual rentals for housing (stock measure) | 11.2% | 2006 |
| Petrol + other vehicle fuels (diesel) | 4.0% | 2011 |
| Electricity + gas | 3.4% | 2011 |
| Alcoholic beverages (beer/wine/spirits) + cigarettes and tobacco | 4.9% | 2011 |
| Domestic + international air transport | 1.7% | 2015 |
| Domestic + overseas accommodation services | 1.0% | 2017 |

The remaining ~53% of the basket (purchase of new housing, local-authority
rates, vehicles, household contents, health, communication, recreation,
education, insurance, ...) is priced only quarterly and first appears in the
CPI release itself. There is no public monthly source for these, so the model
applies a transparent assumption (see below).

Everything needed is downloadable without registration:

- **Selected price indexes** (monthly, full Infoshare-format CSV attached to
  each release): https://www.stats.govt.nz/topics/price-indexes/
- **CPI index numbers** (quarterly CSV, all 108 level-3 classes back decades):
  attached to each CPI release, e.g.
  https://www.stats.govt.nz/topics/consumers-price-index/
- **Expenditure weights** by group/subgroup/class for the Sep-2017, Jun-2020
  and Dec-2024 link quarters: Table 1 of the
  [CPI review 2024 tables](https://www.stats.govt.nz/methods/consumers-price-index-review-2024/)
  (committed at `data/consumers-price-index-review-2024-tables.xlsx`).

## Method

For the target quarter *T* the headline movement is built exactly as a
chained Laspeyres index aggregates:

```
%ΔCPI(T) = Σᵢ wᵢ(T−1) · %ΔIᵢ(T)
wᵢ(T−1) ∝ wᵢ(base) · Iᵢ(T−1) / Iᵢ(base)      (price-updated weights)
```

with the base (link) quarter and weight set determined by the regime in
force (2017 weights for movements 2017Q4–2020Q2, 2020 weights for
2020Q3–2024Q4, 2024 weights from 2025Q1). The 107 aggregation leaves are the
class-level rows of the published weights table.

Per-component quarterly movement `%ΔIᵢ(T)`:

- **Monthly-covered (src `spi`)** — day-weighted average of the monthly index
  over the three months of *T*, relative to the same average over *T−1*,
  applied to the official class index at *T−1*. Stats NZ itself averages
  monthly prices over the quarter with day weighting, so this reproduces the
  official class movements to within a few hundredths of a point (food group:
  mean 0.04pp, electricity 0.02pp over 2015–2026).
- **Uncovered (src `seasonal`, default)** — median of the class's own
  same-quarter movements over the previous 5 years. This captures the strong
  administered-price timing in the uncovered half (local-authority rates
  move only in Q3, education fees and excise in Q1, etc.).
- **Uncovered alternative (`--uncovered carry`)** — assume unchanged (0%).

## Accuracy (backtest, 2018Q1–2026Q1, 33 quarters)

Estimated vs published quarterly headline change, re-estimated for every
quarter using only prior-quarter official levels plus the monthly series
(`output/backtest_seasonal.csv` for the full table):

| | seasonal rule | carry rule |
|---|---|---|
| Mean absolute error | **0.24 pp** | 0.43 pp |
| RMSE | 0.36 pp | 0.54 pp |
| Max error | 0.94 pp | 1.21 pp |
| MAE, last 8 quarters (2024Q2–2026Q1) | **0.10 pp** | 0.38 pp |

In calm periods the estimate is usually within ±0.1pp of the official
quarterly rate. The large errors are concentrated in 2021–2022, when the
*uncovered* half of the basket (construction costs, vehicles, household
contents) inflated far faster than any seasonal rule could assume — an
irreducible limitation of nowcasting from the public 47%.

## Usage

```bash
pip install -r requirements.txt

# Estimate the first unpublished quarter (auto-detected), e.g. 2026Q2
python -m nzcpi nowcast

# Specific quarter, full component table to CSV
python -m nzcpi nowcast --quarter 2026Q2 --csv output/nowcast.csv

# Re-run the accuracy backtest
python -m nzcpi backtest --start 2018Q1

# Force re-download of the latest Stats NZ files (run after each SPI release)
python -m nzcpi nowcast --refresh
```

Source files are cached in `data/` (the two big CSVs are git-ignored and
re-downloaded on demand; URLs are auto-discovered by probing the Stats NZ
release-asset naming pattern back from the current month).

The nowcast flags partial quarters: e.g. run in early July, 2026Q2 uses only
April+May SPI (day-weighted over available months); rerun after the June SPI
(mid-July) for the complete estimate a few days ahead of the CPI release.

## Caveats

- Movements for covered items replicate, not duplicate, the official
  calculation: Stats NZ aggregates from region×outlet price quotes with
  day-weighting inside the quarter; averaging the published monthly indexes
  reproduces that to ~0.01–0.3pp at class level depending on the item.
- The published headline % change is computed from rounded index numbers, so
  even a perfect reconstruction can differ by ±0.05pp.
- Weight regimes are hard-coded through the 2024 review (movements from
  2025Q1). When Stats NZ implements its next review, add the new column to
  `config.WEIGHT_REGIMES` and the weights workbook.
- The rent component uses the *stock* measure (`CPIM.SE9041S`), matching the
  CPI's "actual rentals for housing" class.
