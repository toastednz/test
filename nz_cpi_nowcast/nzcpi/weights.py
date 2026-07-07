"""Parse CPI expenditure weights (Table 1 of the CPI review 2024 tables).

Table 1 lays the classification out as an indented hierarchy: column A holds
group labels, column B subgroups, column C classes. Weights (percent of the
all-groups basket at the base quarter) are in fixed columns for the Sep-2017,
Jun-2020, and Dec-2024 base quarters.

We take the *leaves* of the hierarchy (a row with no deeper row following it
in its branch) as the aggregation partition — for most branches that's the
class level; for single-class subgroups Stats NZ collapses the two into one
row. Leaf weights sum to ~100 in every regime (checked at load time).
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

import openpyxl

from . import config


def normalise(label: str) -> str:
    s = unicodedata.normalize("NFKC", str(label)).strip().lower()
    s = s.replace("–", "-").replace("�", "")
    s = s.replace(", and ", " and ").replace(",", "")
    s = re.sub(r"\(\d\)", "", s)          # footnote markers
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_leaf_weights(xlsx_path: Path, class_names_to_codes: dict[str, str]) -> list[dict]:
    """Return leaf rows: {name, code, w2017, w2020, w2024} (percent)."""
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    rows = [list(r) for r in wb["Table 1"].iter_rows(values_only=True)]

    entries = []
    for r in rows[9:]:  # data starts after the two header blocks
        label, level = None, None
        for i in (0, 1, 2):
            if r[i] not in (None, ""):
                label, level = str(r[i]).strip(), i
                break
        if label is None:
            continue
        if normalise(label).startswith(("all groups", "footnote", "symbol",
                                        "published", "source")):
            continue
        weights = {key: float(r[col]) for col, key in
                   ((4, "w2017"), (6, "w2020"), (8, "w2024"))
                   if isinstance(r[col], (int, float))}
        if not weights:
            continue
        entries.append({"label": label, "level": level, **weights})

    leaves = []
    for i, e in enumerate(entries):
        next_level = entries[i + 1]["level"] if i + 1 < len(entries) else -1
        if next_level <= e["level"]:
            leaves.append(e)

    out = []
    for e in leaves:
        key = normalise(e["label"])
        code = class_names_to_codes.get(key) or config.WEIGHT_NAME_ALIASES.get(key)
        if code is None:
            raise ValueError(f"Weight row {e['label']!r} has no matching CPI class series")
        out.append({
            "name": e["label"],
            "code": code,
            "w2017": e.get("w2017"),
            "w2020": e.get("w2020"),
            "w2024": e.get("w2024"),
        })

    for key in ("w2017", "w2020", "w2024"):
        total = sum(e[key] or 0.0 for e in out)
        if not 99.5 <= total <= 100.5:
            raise ValueError(f"{key} leaf weights sum to {total:.2f}, expected ~100")
    return out
