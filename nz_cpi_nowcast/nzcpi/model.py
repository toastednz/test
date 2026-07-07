"""Bottom-up reconstruction of the quarterly NZ CPI from public component data.

Method
------
The CPI is a chained Laspeyres-type index: within a weight regime, the
all-groups movement between quarters is a fixed-basket weighted average of
class-level movements, with expenditure weights fixed at the link (base)
quarter. Equivalently, the quarter-on-quarter change is

    dCPI(T) = sum_i  w_i(T-1) * dI_i(T),

where w_i(T-1) is the base-quarter weight *price-updated* to T-1:
w_i(T-1) proportional to w_i(base) * I_i(T-1) / I_i(base).

For each of the ~107 leaf components we estimate dI_i(T) from:
  * 'spi'      — the matching monthly Selected Price Index series, averaged
                 over the quarter with day weighting (Stats NZ averages
                 monthly prices over the quarter, weighting by days). This is
                 real measured price data for the target quarter — the same
                 collections that feed the official CPI.
  * 'seasonal' — for components with no monthly source: the median of that
                 class's own same-quarter movements over the previous N years
                 (captures administered/seasonal timing: local-authority
                 rates in Q3, education fees in Q1, excise in Q1, ...).
  * 'carry'    — alternatively, assume no change (0%).

The quarterly average of the monthly index is taken relative to the same
average for T-1 and applied to the official class index level at T-1, so any
base/rounding differences between the monthly and quarterly series cancel.
"""

from __future__ import annotations

import calendar
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from . import config, fetch, weights


def _read_series_csv(path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"Period": str}, encoding="utf-8",
                     encoding_errors="replace")
    df.columns = [c.strip() for c in df.columns]
    return df


def _prev_quarter(qp: str) -> str:
    y, m = int(qp[:4]), int(qp[5:7])
    return f"{y - 1}.12" if m == 3 else f"{y}.{m - 3:02d}"


def _quarter_months(qp: str) -> list[str]:
    y, m = int(qp[:4]), int(qp[5:7])
    return [f"{y}.{mm:02d}" for mm in (m - 2, m - 1, m)]


def quarter_label(qp: str) -> str:
    return f"{qp[:4]}Q{int(qp[5:7]) // 3}"


def parse_quarter(label: str) -> str:
    """Accept '2026Q2', '2026.06', '2026-06' and return 'YYYY.MM'."""
    label = label.strip().upper().replace("-", ".")
    if "Q" in label:
        y, q = label.split("Q")
        return f"{int(y)}.{int(q) * 3:02d}"
    y, m = label.split(".")
    if int(m) not in (3, 6, 9, 12):
        raise ValueError(f"{label!r} is not a quarter-end period")
    return f"{int(y)}.{int(m):02d}"


@dataclass
class NowcastResult:
    quarter: str                 # 'YYYY.MM' quarter-end period
    qoq_pct: float               # estimated quarterly headline change, %
    annual_pct: float | None     # estimated annual change, % (needs T-4 level)
    actual_qoq_pct: float | None # official change if already published
    covered_weight_pct: float    # share of basket priced from monthly data
    months_available: int        # min months of SPI data in target quarter
    detail: pd.DataFrame = field(repr=False, default=None)


class BottomUpCPI:
    def __init__(self, refresh: bool = False):
        cpi = _read_series_csv(fetch.fetch_cpi_csv(refresh=refresh))
        spi = _read_series_csv(fetch.fetch_spi_csv(refresh=refresh))

        self.Q = (cpi.pivot_table(index="Period", columns="Series_reference",
                                  values="Data_value", aggfunc="first")
                     .replace(0, np.nan))
        self.M = spi.pivot_table(index="Period", columns="Series_reference",
                                 values="Data_value", aggfunc="first")

        classes = cpi[cpi["Group"] == "CPI Level 3 Classes for New Zealand"]
        name_map = {}
        for _, row in classes[["Series_reference", "Series_title_1"]].drop_duplicates().iterrows():
            name_map.setdefault(weights.normalise(row.Series_title_1),
                                row.Series_reference)
        self.leaves = weights.load_leaf_weights(fetch.fetch_weights_xlsx(refresh=refresh),
                                                name_map)

    # ------------------------------------------------------------------
    def last_published_quarter(self) -> str:
        pub = self.Q[config.ALL_GROUPS].dropna()
        return pub.index.max()

    def next_quarter(self) -> str:
        last = self.last_published_quarter()
        y, m = int(last[:4]), int(last[5:7])
        return f"{y + 1}.03" if m == 12 else f"{y}.{m + 3:02d}"

    def _regime(self, qp: str) -> tuple[str, str]:
        for wkey, base_q, first_move in config.WEIGHT_REGIMES:
            if qp >= first_move:
                return wkey, base_q
        raise ValueError(f"No weight regime covers movements ending {qp} "
                         "(model supports Dec-2017 quarter onwards)")

    def _quarter_avg(self, series: pd.Series, qp: str) -> tuple[float, int]:
        """Day-weighted average of monthly index values within a quarter."""
        vals, wts = [], []
        for p in _quarter_months(qp):
            v = series.get(p)
            if v is not None and pd.notna(v):
                vals.append(v)
                wts.append(calendar.monthrange(int(p[:4]), int(p[5:7]))[1])
        if not vals:
            return np.nan, 0
        return float(np.average(vals, weights=wts)), len(vals)

    def _seasonal_qoq(self, code: str, qp: str, hist_years: int) -> float | None:
        y, m = int(qp[:4]), qp[5:7]
        ratios = []
        for k in range(1, hist_years + 1):
            t = f"{y - k}.{m}"
            t_1 = _prev_quarter(t)
            if t in self.Q.index and t_1 in self.Q.index:
                a, b = self.Q.at[t, code], self.Q.at[t_1, code]
                if pd.notna(a) and pd.notna(b):
                    ratios.append(a / b)
        if not ratios:
            return None
        return float(np.median(ratios)) - 1.0

    # ------------------------------------------------------------------
    def estimate(self, quarter: str | None = None, uncovered: str = "seasonal",
                 hist_years: int = 5) -> NowcastResult:
        """Bottom-up estimate of the CPI movement for one quarter.

        quarter: 'YYYY.MM' quarter-end period (default: first unpublished).
        uncovered: 'seasonal' or 'carry' — treatment of components with no
                   monthly source.
        """
        qp = quarter or self.next_quarter()
        pq = _prev_quarter(qp)
        wkey, base_q = self._regime(qp)
        if pq not in self.Q.index:
            raise ValueError(f"No official class indexes for {pq}; can only "
                             "estimate one quarter past the published data")

        rows = []
        for leaf in self.leaves:
            code, w_base = leaf["code"], leaf[wkey]
            if not w_base:
                continue
            i_prev = self.Q.at[pq, code] if code in self.Q.columns else np.nan
            i_base = self.Q.at[base_q, code] if code in self.Q.columns else np.nan
            if pd.isna(i_prev) or pd.isna(i_base):
                continue
            w_pu = w_base * i_prev / i_base  # price-updated to T-1

            qoq, src, n_months = None, None, 0
            spi_ref = config.CLASS_TO_SPI.get(code)
            if spi_ref and spi_ref in self.M.columns:
                avg_t, n_t = self._quarter_avg(self.M[spi_ref], qp)
                avg_p, n_p = self._quarter_avg(self.M[spi_ref], pq)
                if n_t > 0 and n_p == 3:
                    qoq, src, n_months = avg_t / avg_p - 1.0, "spi", n_t
            if src is None:
                if uncovered == "seasonal":
                    s = self._seasonal_qoq(code, qp, hist_years)
                    qoq, src = (s, "seasonal") if s is not None else (0.0, "carry")
                else:
                    qoq, src = 0.0, "carry"

            rows.append({"code": code, "name": leaf["name"], "source": src,
                         "months": n_months, "weight_pct": w_pu,
                         "qoq_pct": qoq * 100.0})

        detail = pd.DataFrame(rows)
        detail["weight_pct"] *= 100.0 / detail["weight_pct"].sum()
        detail["contribution_pp"] = detail["weight_pct"] * detail["qoq_pct"] / 100.0
        detail = detail.sort_values("contribution_pp", key=abs, ascending=False)

        qoq_est = detail["contribution_pp"].sum()

        actual = None
        if qp in self.Q.index and pd.notna(self.Q.at[qp, config.ALL_GROUPS]):
            actual = (self.Q.at[qp, config.ALL_GROUPS]
                      / self.Q.at[pq, config.ALL_GROUPS] - 1.0) * 100.0

        annual = None
        t4 = qp
        for _ in range(4):
            t4 = _prev_quarter(t4)
        if t4 in self.Q.index and pd.notna(self.Q.at[t4, config.ALL_GROUPS]):
            level_est = self.Q.at[pq, config.ALL_GROUPS] * (1.0 + qoq_est / 100.0)
            annual = (level_est / self.Q.at[t4, config.ALL_GROUPS] - 1.0) * 100.0

        spi_rows = detail[detail["source"] == "spi"]
        return NowcastResult(
            quarter=qp,
            qoq_pct=qoq_est,
            annual_pct=annual,
            actual_qoq_pct=actual,
            covered_weight_pct=spi_rows["weight_pct"].sum(),
            months_available=int(spi_rows["months"].min()) if len(spi_rows) else 0,
            detail=detail.reset_index(drop=True),
        )

    # ------------------------------------------------------------------
    def backtest(self, start: str = "2018.03", uncovered: str = "seasonal",
                 hist_years: int = 5) -> pd.DataFrame:
        """Re-estimate every published quarter from `start` and compare."""
        pub = self.Q[config.ALL_GROUPS].dropna()
        quarters = [p for p in pub.index if p >= start]
        recs = []
        for qp in quarters:
            pq = _prev_quarter(qp)
            if pq not in pub.index:
                continue
            try:
                r = self.estimate(qp, uncovered=uncovered, hist_years=hist_years)
            except ValueError:
                continue
            recs.append({
                "quarter": quarter_label(qp),
                "est_qoq_pct": round(r.qoq_pct, 3),
                "actual_qoq_pct": round(r.actual_qoq_pct, 3),
                "error_pp": round(r.qoq_pct - r.actual_qoq_pct, 3),
                "covered_weight_pct": round(r.covered_weight_pct, 1),
            })
        return pd.DataFrame(recs)
