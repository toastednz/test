"""Download and cache the public Stats NZ source files.

Everything the model needs is published as flat files with each release:
  - Selected price indexes (monthly): full Infoshare-style CSV time series
  - Consumers price index (quarterly): "index numbers" CSV, all levels
  - CPI review 2024 tables (xlsx): expenditure weights by group/subgroup/class

Release-asset URLs follow a predictable pattern; we probe backwards from the
current month until we find the most recent published file.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import requests

from . import config

CACHE_DIR = Path(__file__).resolve().parent.parent / "data"

HEADERS = {"User-Agent": "nz-cpi-bottom-up-nowcast/1.0 (research use)"}


def _download(url: str, dest: Path) -> bool:
    resp = requests.get(url, headers=HEADERS, timeout=120)
    if resp.status_code != 200 or len(resp.content) < 1000:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(resp.content)
    return True


def _probe_monthly(template: str, prefix: str, start: dt.date, tries: int,
                   step_months: int, refresh: bool) -> Path:
    """Walk back month by month (or quarter by quarter) until a URL exists."""
    y, m = start.year, start.month
    for _ in range(tries):
        month = config.MONTH_NAMES[m - 1]
        url = template.format(Month=month.capitalize(), month=month, year=y)
        dest = CACHE_DIR / f"{prefix}-{y}-{m:02d}.csv"
        if dest.exists() and not refresh:
            return dest
        if _download(url, dest):
            return dest
        m -= step_months
        while m < 1:
            m += 12
            y -= 1
    raise RuntimeError(f"No {prefix} file found probing back from {start}")


def fetch_spi_csv(refresh: bool = False) -> Path:
    """Latest monthly Selected Price Indexes time-series CSV."""
    return _probe_monthly(config.SPI_CSV_TEMPLATE, "spi", dt.date.today(),
                          tries=14, step_months=1, refresh=refresh)


def fetch_cpi_csv(refresh: bool = False) -> Path:
    """Latest quarterly CPI index-numbers CSV."""
    today = dt.date.today()
    # CPI releases are for quarter-end months (Mar/Jun/Sep/Dec)
    qm = ((today.month - 1) // 3) * 3
    if qm == 0:
        start = dt.date(today.year - 1, 12, 1)
    else:
        start = dt.date(today.year, qm, 1)
    return _probe_monthly(config.CPI_CSV_TEMPLATE, "cpi", start,
                          tries=6, step_months=3, refresh=refresh)


def fetch_weights_xlsx(refresh: bool = False) -> Path:
    """CPI review 2024 tables workbook (expenditure weights)."""
    dest = CACHE_DIR / "consumers-price-index-review-2024-tables.xlsx"
    if dest.exists() and not refresh:
        return dest
    if not _download(config.WEIGHTS_TABLES_URL, dest):
        raise RuntimeError("Could not download CPI review 2024 tables")
    return dest
