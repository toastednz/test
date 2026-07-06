#!/usr/bin/env python3
"""
rule_of_two_screen.py
======================
Find medicines approved by TWO OR MORE recognised overseas regulators within the
last N years -- i.e. the candidate pool for New Zealand's Medsafe "consent by
verification" (rule-of-two) pathway.

Recognised regulators (Medsafe list): US-FDA, Health Canada, EU-EMA, SG-HSA,
UK-MHRA, AU-TGA. This script implements the four with clean programmatic feeds:

  US  - FDA            openFDA "Drugs@FDA" bulk JSON            [runs as-is]
  SG  - HSA            data.gov.sg datastore REST API           [runs as-is*]
  EU  - EMA            EPAR human-medicines table (.xlsx)        [confirm 1 URL + cols]
  CA  - Health Canada  Drug Product Database (DPD) extract       [confirm col indices]

  (AU-TGA = manual CSV export; UK-MHRA = scrape only -- not automated here.)

*HSA's open dataset may not carry a registration DATE. The script handles that:
 a molecule with 2 dated in-window approvals is Tier A; a molecule that needs
 Singapore's date confirmed is Tier B. See combine().

IMPORTANT -- this is a CANDIDATE list, not a qualification decision.
Medsafe also requires: the NZ product identical in all material respects to the
overseas one; authorisations current (not withdrawn/refused/suspended); no older
than 4 years; etc. This is the TOP OF THE FUNNEL. Confirm each candidate by hand,
then subtract whatever is already registered in NZ.

USAGE
  python rule_of_two_screen.py --selftest        # validate matching logic offline
  python rule_of_two_screen.py --inspect fda     # print raw fields of one source
  python rule_of_two_screen.py --run             # fetch all + write candidates.csv
  python rule_of_two_screen.py --run --years 4   # approval window (default 4)

DEPENDENCIES (only for --run / --inspect):
  pip install requests pandas openpyxl
"""

import argparse
import csv
import io
import json
import re
import sys
import zipfile
from datetime import date, datetime, timedelta

# ---------------------------------------------------------------------------
# ENDPOINTS  -- verify the two marked "CONFIRM" before a real run; gov URLs drift.
# ---------------------------------------------------------------------------
FDA_DRUGSFDA_ZIP = "https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip"

# data.gov.sg CKAN datastore resource id for "Listing of Registered Therapeutic Products"
SG_RESOURCE_ID = "d_767279312753558cbf19d48344577084"
SG_DATASTORE = "https://data.gov.sg/api/action/datastore_search"

# EMA "medicines output" report (all human + veterinary medicines, regenerated nightly).
# Verified live 2026-07-06. Source page: https://www.ema.europa.eu/en/medicines/download-medicine-data
# NB: the .xlsx has banner rows above the real header -- fetch_ema() detects it dynamically.
EMA_XLSX_URL = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx"

# CONFIRM: current Health Canada DPD "all files" extract (headerless CSVs).
# Get it from https://open.canada.ca/data/en/dataset/bf55e42a-63cb-4556-bfd8-44f26e5a36fe
CA_DPD_ZIP = ("https://open.canada.ca/data/dataset/bf55e42a-63cb-4556-bfd8-44f26e5a36fe/"
              "resource/b05ae610-0366-478f-993f-b4afbdaadbc6/download/allfiles.zip")

# Health Canada DPD files are HEADERLESS. Column positions below are from the Read Me:
# https://www.canada.ca/.../read-file-drug-product-database-data-extract.html
# VERIFY these indices against the current Read Me before trusting Canada output.
CA_COLS = {
    "drug_file":       "drug.txt",   # QRYM_DRUG_PRODUCT
    "drug_code_idx":   0,            # DRUG_CODE (join key)
    "brand_idx":       4,            # BRAND_NAME
    "ingr_file":       "ingred.txt", # QRYM_ACTIVE_INGREDIENTS
    "ingr_code_idx":   0,            # DRUG_CODE
    "ingr_name_idx":   3,            # INGREDIENT
    "status_file":     "status.txt", # QRYM_STATUS
    "status_code_idx": 0,            # DRUG_CODE
    "status_flag_idx": 1,            # CURRENT_STATUS_FLAG (Y/N)
    "status_name_idx": 2,            # STATUS text
    "status_date_idx": 3,            # HISTORY_DATE
    "comp_file":       "comp.txt",   # QRYM_COMPANIES
    "comp_code_idx":   0,
    "comp_name_idx":   3,
}

# ---------------------------------------------------------------------------
# INGREDIENT NORMALISATION -- the heart of cross-regulator matching.
# Same molecule is written differently in each jurisdiction, so we reduce every
# name to a canonical key: strip salts/strengths, apply INN synonyms, sort combos.
# ---------------------------------------------------------------------------
_SALT_TOKENS = {
    "hydrochloride", "hcl", "sodium", "potassium", "calcium", "magnesium",
    "sulfate", "sulphate", "mesylate", "besylate", "besilate", "maleate",
    "tartrate", "succinate", "citrate", "acetate", "phosphate", "hydrobromide",
    "bromide", "chloride", "fumarate", "malate", "nitrate", "oxalate",
    "pamoate", "stearate", "valerate", "propionate", "dipropionate", "furoate",
    "xinafoate", "tosylate", "hemifumarate", "bitartrate", "gluconate",
    "lactate", "monohydrate", "dihydrate", "trihydrate", "anhydrous",
    "hydrate", "sesquihydrate", "base", "salt", "as",
}
_UNIT_TOKENS = {"mg", "mcg", "ug", "g", "ml", "l", "iu", "unit", "units", "%", "w", "v"}

# Map jurisdiction-specific names to a single canonical (mostly international INN).
# US spellings are the usual culprits. Extend this map as you find collisions.
_SYNONYMS = {
    "acetaminophen": "paracetamol",
    "albuterol": "salbutamol",
    "meperidine": "pethidine",
    "epinephrine": "adrenaline",
    "norepinephrine": "noradrenaline",
    "glyburide": "glibenclamide",
    "lignocaine": "lidocaine",
    "cholecalciferol": "vitamin d3",
    "rifampin": "rifampicin",
    "sulfamethoxazole trimethoprim": "sulfamethoxazole + trimethoprim",
    "phenobarbital": "phenobarbitone",
}


def canon_ingredient(raw: str) -> str:
    """Reduce a raw active-ingredient string to a canonical, order-independent key."""
    if not raw:
        return ""
    raw = str(raw).lower()
    # split multi-ingredient products on common separators
    parts = re.split(r"[;/+]| and |,\s+", raw)
    norm = []
    for p in parts:
        p = re.sub(r"[^a-z0-9 ]", " ", p)
        tokens = [t for t in p.split()
                  if t and not t.isdigit()
                  and t not in _SALT_TOKENS and t not in _UNIT_TOKENS]
        base = " ".join(tokens).strip()
        base = _SYNONYMS.get(base, base)
        if base:
            norm.append(base)
    norm = sorted(set(norm))
    return " + ".join(norm)


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------
def _parse_date(s, fmt):
    try:
        return datetime.strptime(str(s).strip(), fmt).date()
    except (ValueError, TypeError):
        return None


def _parse_date_flex(s):
    if s is None:
        return None
    s = str(s).strip()
    if not s or s.lower() in ("nan", "none", "nat"):
        return None
    for fmt in ("%Y-%m-%d", "%Y%m%d", "%d/%m/%Y", "%d-%m-%Y", "%m/%d/%Y",
                "%d %b %Y", "%d %B %Y", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d"):
        d = _parse_date(s, fmt)
        if d:
            return d
    m = re.search(r"(\d{4})[-/](\d{2})[-/](\d{2})", s)  # last-ditch ISO-ish
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    return None


def _http_get(url, **kw):
    import requests
    r = requests.get(url, timeout=120, **kw)
    r.raise_for_status()
    return r


# ---------------------------------------------------------------------------
# ADAPTERS -- each returns list[dict] with the common schema:
#   {source, raw_name, ingredient_key, approval_date (date|None), brand, applicant}
# ---------------------------------------------------------------------------
def fetch_fda():
    r = _http_get(FDA_DRUGSFDA_ZIP)
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        name = z.namelist()[0]
        data = json.loads(z.read(name).decode("utf-8"))
    out = []
    for app in data.get("results", []):
        sponsor = app.get("sponsor_name", "")
        # original approval = earliest "AP" submission date
        appr = None
        for s in app.get("submissions", []):
            if s.get("submission_status") == "AP":
                d = _parse_date(s.get("submission_status_date"), "%Y%m%d")
                if d and (appr is None or d < appr):
                    appr = d
        for prod in app.get("products", []):
            ings = "; ".join(ai.get("name", "") for ai in prod.get("active_ingredients", []))
            key = canon_ingredient(ings)
            if not key:
                continue
            out.append({"source": "FDA", "raw_name": ings, "ingredient_key": key,
                        "approval_date": appr, "brand": prod.get("brand_name", ""),
                        "applicant": sponsor})
    return out


def _datastore_all(resource_id, page=1000):
    offset, total, out = 0, None, []
    while True:
        r = _http_get(SG_DATASTORE, params={"resource_id": resource_id,
                                            "limit": page, "offset": offset})
        res = r.json().get("result", {})
        recs = res.get("records", [])
        out.extend(recs)
        total = res.get("total", len(out)) if total is None else total
        offset += len(recs)
        if not recs or offset >= total:
            break
    return out


def fetch_singapore():
    recs = _datastore_all(SG_RESOURCE_ID)
    out = []
    for r in recs:
        low = {k.lower(): v for k, v in r.items()}
        ing = low.get("active_ingredients") or low.get("active_ingredient") or ""
        brand = low.get("product_name") or low.get("product") or ""
        applicant = (low.get("company_name") or low.get("licence_holder")
                     or low.get("registrant") or low.get("manufacturer") or "")
        datestr = (low.get("registration_date") or low.get("date_of_registration")
                   or low.get("approval_date") or low.get("first_registration_date") or "")
        key = canon_ingredient(ing)
        if not key:
            continue
        out.append({"source": "HSA", "raw_name": ing, "ingredient_key": key,
                    "approval_date": _parse_date_flex(datestr),
                    "brand": brand, "applicant": applicant})
    return out


def _find_col(cols_lower, needles):
    for n in needles:
        for lc, orig in cols_lower.items():
            if n in lc:
                return orig
    return None


def _read_ema_table():
    """Download the EMA report and return a DataFrame with the real header.

    The EMA 'medicines output' .xlsx carries several banner rows (title,
    generation timestamp, blanks) before the actual column header, so a plain
    read_excel() treats the banner as column names and matches nothing. Find
    the header row dynamically -- its height drifts as EMA regenerates the file.
    """
    import pandas as pd
    content = _http_get(EMA_XLSX_URL).content
    probe = pd.read_excel(io.BytesIO(content), header=None, nrows=40)
    header_row = 0
    for i, row in probe.iterrows():
        cells = {str(v).strip().lower() for v in row.tolist()}
        if "name of medicine" in cells or "category" in cells:
            header_row = i
            break
    return pd.read_excel(io.BytesIO(content), header=header_row)


def fetch_ema():
    df = _read_ema_table()
    cl = {str(c).lower(): c for c in df.columns}
    # keep human medicines only (the file also carries veterinary rows)
    catcol = _find_col(cl, ["category"])
    if catcol:
        df = df[df[catcol].astype(str).str.strip().str.lower() == "human"]
    inn = _find_col(cl, ["inn", "active substance", "common name"])
    dcol = _find_col(cl, ["marketing authorisation date", "authorisation date",
                          "decision date", "date of issue", "start date"])
    ncol = _find_col(cl, ["name of medicine", "medicine name", "product name", "name"])
    mcol = _find_col(cl, ["marketing authorisation holder", "holder", "applicant"])
    scol = _find_col(cl, ["authorisation status", "status"])
    out = []
    for _, row in df.iterrows():
        if scol:
            st = str(row.get(scol, "")).strip().lower()
            if st and st not in ("authorised", "authorized"):
                continue  # drop withdrawn/refused/suspended
        ing = str(row.get(inn, "")) if inn else ""
        key = canon_ingredient(ing)
        if not key:
            continue
        out.append({"source": "EMA", "raw_name": ing, "ingredient_key": key,
                    "approval_date": _parse_date_flex(row.get(dcol)) if dcol else None,
                    "brand": str(row.get(ncol, "")) if ncol else "",
                    "applicant": str(row.get(mcol, "")) if mcol else ""})
    return out


def _read_ca_file(zf, fname):
    """Read one headerless DPD CSV into a list of token-lists."""
    with zf.open(fname) as fh:
        text = io.TextIOWrapper(fh, encoding="latin-1", newline="")
        return list(csv.reader(text))


def fetch_health_canada():
    r = _http_get(CA_DPD_ZIP)
    zf = zipfile.ZipFile(io.BytesIO(r.content))
    names = {n.split("/")[-1].lower(): n for n in zf.namelist()}

    def grab(key):
        f = CA_COLS[key]
        return names.get(f.lower())

    c = CA_COLS
    # ingredients by drug_code
    ings = {}
    if grab("ingr_file"):
        for row in _read_ca_file(zf, grab("ingr_file")):
            if len(row) <= max(c["ingr_code_idx"], c["ingr_name_idx"]):
                continue
            ings.setdefault(row[c["ingr_code_idx"]], []).append(row[c["ingr_name_idx"]])
    # status/date by drug_code (keep current, approved-ish rows)
    status = {}
    if grab("status_file"):
        for row in _read_ca_file(zf, grab("status_file")):
            if len(row) <= max(c["status_code_idx"], c["status_date_idx"]):
                continue
            flag = row[c["status_flag_idx"]] if len(row) > c["status_flag_idx"] else ""
            if flag.strip().upper() not in ("Y", ""):
                continue
            status[row[c["status_code_idx"]]] = _parse_date_flex(row[c["status_date_idx"]])
    # company by drug_code
    comp = {}
    if grab("comp_file"):
        for row in _read_ca_file(zf, grab("comp_file")):
            if len(row) > max(c["comp_code_idx"], c["comp_name_idx"]):
                comp.setdefault(row[c["comp_code_idx"]], row[c["comp_name_idx"]])
    out = []
    for row in _read_ca_file(zf, grab("drug_file")):
        if len(row) <= max(c["drug_code_idx"], c["brand_idx"]):
            continue
        code = row[c["drug_code_idx"]]
        ing = "; ".join(ings.get(code, []))
        key = canon_ingredient(ing)
        if not key:
            continue
        out.append({"source": "HealthCanada", "raw_name": ing, "ingredient_key": key,
                    "approval_date": status.get(code), "brand": row[c["brand_idx"]],
                    "applicant": comp.get(code, "")})
    return out


ADAPTERS = {
    "fda": fetch_fda,
    "sg": fetch_singapore,
    "ema": fetch_ema,
    "ca": fetch_health_canada,
}

# ---------------------------------------------------------------------------
# MATCHING
# ---------------------------------------------------------------------------
def combine(records, years=4):
    cutoff = date.today() - timedelta(days=round(365.25 * years))
    by_key = {}
    for r in records:
        k = r["ingredient_key"]
        d = r["approval_date"]
        e = by_key.setdefault(k, {})
        cur = e.get(r["source"])
        info = {"date": d, "in_window": bool(d and d >= cutoff),
                "brand": r["brand"], "applicant": r["applicant"]}
        # keep the most-recent-dated record per (molecule, regulator)
        if cur is None or (d and (cur["date"] is None or d > cur["date"])):
            e[r["source"]] = info

    rows = []
    for k, srcmap in by_key.items():
        in_win = {s: i for s, i in srcmap.items() if i["in_window"]}
        unknown = {s: i for s, i in srcmap.items() if i["date"] is None}
        n_conf = len(in_win)
        # Tier A: >=2 regulators with a dated, in-window approval.
        # Tier B: only >=2 once you count date-unknown sources (needs a date check).
        if n_conf >= 2:
            tier = "A: 2+ dated in-window"
        elif n_conf >= 1 and (n_conf + len(unknown)) >= 2:
            tier = "B: confirm date(s)"
        else:
            continue
        regs = {**in_win, **unknown}
        reg_str = "; ".join(
            f"{s}({i['date'].isoformat() if i['date'] else 'no-date'})"
            for s, i in sorted(regs.items()))
        brands = "; ".join(sorted({i["brand"] for i in regs.values() if i["brand"]}))[:200]
        appls = "; ".join(sorted({i["applicant"] for i in regs.values() if i["applicant"]}))[:200]
        newest = max([i["date"] for i in regs.values() if i["date"]], default=None)
        rows.append({
            "ingredient": k,
            "tier": tier,
            "n_regulators_in_window": n_conf,
            "regulators": reg_str,
            "example_brands": brands,
            "applicants": appls,
            "most_recent_approval": newest.isoformat() if newest else "",
        })

    rows.sort(key=lambda x: (x["tier"].startswith("B"),
                             -x["n_regulators_in_window"],
                             x["most_recent_approval"]), reverse=False)
    # secondary: newest first within group
    rows.sort(key=lambda x: (x["tier"], -x["n_regulators_in_window"],
                             x["most_recent_approval"]), reverse=False)
    return rows


def write_csv(rows, path="candidates.csv"):
    fields = ["ingredient", "tier", "n_regulators_in_window", "regulators",
              "most_recent_approval", "example_brands", "applicants"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return path


# ---------------------------------------------------------------------------
# RUN / INSPECT / SELFTEST
# ---------------------------------------------------------------------------
def run(years=4):
    all_recs = []
    for name, fn in ADAPTERS.items():
        try:
            recs = fn()
            print(f"  {name:12s} {len(recs):>7,} product records")
            all_recs.extend(recs)
        except Exception as e:  # keep going if one source is down / URL moved
            print(f"  {name:12s}   FAILED: {type(e).__name__}: {e}")
    rows = combine(all_recs, years=years)
    path = write_csv(rows)
    a = sum(r["tier"].startswith("A") for r in rows)
    b = len(rows) - a
    print(f"\n{len(rows)} candidate molecules  (Tier A: {a}  Tier B: {b})")
    print(f"written to {path}")
    for r in rows[:15]:
        print(f"  [{r['tier'][0]}] {r['ingredient']:<32} {r['regulators']}")


def inspect(source):
    fn = ADAPTERS.get(source)
    if not fn:
        print(f"unknown source '{source}'. choose: {', '.join(ADAPTERS)}")
        return
    recs = fn()
    print(f"{source}: {len(recs)} records. First 5 normalised:")
    for r in recs[:5]:
        print(" ", {k: r[k] for k in ("raw_name", "ingredient_key",
                                      "approval_date", "brand")})


def selftest():
    # -- normaliser --
    assert canon_ingredient("Acetaminophen") == canon_ingredient("Paracetamol") == "paracetamol"
    assert canon_ingredient("Metoprolol Tartrate") == canon_ingredient("Metoprolol") == "metoprolol"
    a = canon_ingredient("Amoxicillin; Clavulanate Potassium")
    b = canon_ingredient("Clavulanate Potassium / Amoxicillin")
    assert a == b == "amoxicillin + clavulanate", a
    assert canon_ingredient("Albuterol Sulfate 90 mcg") == "salbutamol"
    print("normaliser ....... OK")

    # -- matching -- build post-adapter records directly
    recent = date.today() - timedelta(days=60)
    older = date.today() - timedelta(days=200)
    too_old = date.today() - timedelta(days=5 * 365)
    recs = [
        # paracetamol: two dated in-window regulators -> Tier A
        {"source": "FDA", "raw_name": "Acetaminophen", "ingredient_key": "paracetamol",
         "approval_date": recent, "brand": "TYLENOL-X", "applicant": "AcmePharma"},
        {"source": "EMA", "raw_name": "Paracetamol", "ingredient_key": "paracetamol",
         "approval_date": older, "brand": "ParaEU", "applicant": "EuroPharma"},
        # ibuprofen: one dated in-window + one date-unknown -> Tier B
        {"source": "FDA", "raw_name": "Ibuprofen", "ingredient_key": "ibuprofen",
         "approval_date": recent, "brand": "IbuUS", "applicant": "AcmePharma"},
        {"source": "HSA", "raw_name": "Ibuprofen", "ingredient_key": "ibuprofen",
         "approval_date": None, "brand": "IbuSG", "applicant": "SGDist"},
        # amoxi+clav: one OLD + one unknown -> NOT a candidate (no in-window pair)
        {"source": "FDA", "raw_name": "Amoxicillin; Clavulanate Potassium",
         "ingredient_key": "amoxicillin + clavulanate", "approval_date": too_old,
         "brand": "AugX", "applicant": "AcmePharma"},
        {"source": "HSA", "raw_name": "Amoxicillin; Clavulanate",
         "ingredient_key": "amoxicillin + clavulanate", "approval_date": None,
         "brand": "AugSG", "applicant": "SGDist"},
        # lonely: single regulator -> NOT a candidate
        {"source": "FDA", "raw_name": "Rosuvastatin", "ingredient_key": "rosuvastatin",
         "approval_date": recent, "brand": "RosuUS", "applicant": "AcmePharma"},
    ]
    rows = combine(recs, years=4)
    keys = {r["ingredient"]: r["tier"] for r in rows}
    assert keys.get("paracetamol", "").startswith("A"), keys
    assert keys.get("ibuprofen", "").startswith("B"), keys
    assert "amoxicillin + clavulanate" not in keys, keys
    assert "rosuvastatin" not in keys, keys
    print("matching ......... OK")
    print(f"\nself-test passed. sample output ({len(rows)} candidates):")
    for r in rows:
        print(f"  [{r['tier'][0]}] {r['ingredient']:<28} {r['regulators']}")


def main():
    ap = argparse.ArgumentParser(description="Rule-of-two overseas-approval screen for NZ Medsafe verification pathway")
    ap.add_argument("--run", action="store_true", help="fetch live data and write candidates.csv")
    ap.add_argument("--inspect", metavar="SOURCE", help="print raw fields of one source (fda|sg|ema|ca)")
    ap.add_argument("--selftest", action="store_true", help="validate matching logic offline")
    ap.add_argument("--years", type=int, default=4, help="approval window in years (default 4)")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    elif args.inspect:
        inspect(args.inspect)
    elif args.run:
        run(years=args.years)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
