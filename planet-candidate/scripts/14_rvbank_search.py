#!/usr/bin/env python3
"""Search the public HARPS RVBank (CDS J/A+A/636/A74) for periodic RV signals on stars with no known planets.

For each star with >= NMIN usable RVs: linear trend + two instrument offsets (pre/post 2015 fibre upgrade)
removed by a floating-offset least-squares periodogram over 1.2-5000 d; Baluev FAP; activity-indicator
periodograms (CRX, dLW, Halpha, FWHM, BIS); alias checks against 1 d, 1 yr, and the window function;
cross-match with the NASA Exoplanet Archive (coordinates within 60", name) to flag known hosts.

Usage: 14_rvbank_search.py RVBANK_DIR ARCHIVE_CSV OUT_CSV [--nmin 40]
"""
import os, sys, re, json, argparse, warnings
import numpy as np, pandas as pd
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("rvdir"); ap.add_argument("archive"); ap.add_argument("out"); ap.add_argument("--nmin", type=int, default=40); a = ap.parse_args()
# --- parse ReadMe for column byte ranges of rvbank.dat
rd = open(os.path.join(a.rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]
cols = {}
for line in rd.splitlines():
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
    if m:
        g = m.groups()
        if len(g) == 4: cols[g[3]] = (int(g[0]) - 1, int(g[1]))
        else: cols[g[2]] = (int(g[0]) - 1, int(g[0]))
want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "CRX", "dLW", "Halpha", "Flag", "FWHMDRS"] + [k for k in cols if "BIS" in k.upper()][:1]
want = [w for w in want if w in cols]
print("columns found:", want, flush=True)
df = pd.read_fwf(os.path.join(a.rvdir, "rvbank.dat"), colspecs=[cols[w] for w in want], names=want, header=None)
for c in want[1:]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.replace(-9999999, np.nan)
lst = pd.read_fwf(os.path.join(a.rvdir, "list.dat"), colspecs=[(0, 15), (16, 18), (19, 21), (22, 29), (30, 31), (31, 33), (34, 36), (37, 43), (44, 64), (65, 71), (79, 85), (93, 100)],
                  names=["Name", "RAh", "RAm", "RAs", "sign", "DEd", "DEm", "DEs", "SpType", "Teff", "Vmag", "Dist"], header=None)
lst["ra"] = 15 * (lst.RAh + lst.RAm / 60 + lst.RAs / 3600); lst["dec"] = np.where(lst.sign.astype(str).str.strip() == "-", -1, 1) * (lst.DEd + lst.DEm / 60 + lst.DEs / 3600)
lst["Name"] = lst.Name.astype(str).str.strip(); lst = lst.set_index("Name")
arch = pd.read_csv(a.archive)
def known_planets(name, ra, dec):
    d = np.sqrt(((arch.ra - ra) * np.cos(np.radians(dec))) ** 2 + (arch.dec - dec) ** 2) * 3600
    sel = arch[(d < 60)]
    return list(zip(sel.pl_name, sel.pl_orbper.round(3), sel.discoverymethod))
def periodogram(t, y, e, groups, fmin, fmax, n):
    """Floating-offset (per group) generalized least-squares periodogram. Returns freqs, power (1 - chi2/chi2_0)."""
    f = np.linspace(fmin, fmax, n); w = 1 / e ** 2
    G = np.column_stack([(groups == g).astype(float) for g in np.unique(groups)])
    # null model: offsets only
    W = np.sqrt(w)[:, None]
    def chi2(X):
        A = X * W; b = y * np.sqrt(w); coef, res, rk, sv = np.linalg.lstsq(A, b, rcond=None); r = b - A @ coef; return float(r @ r)
    c0 = chi2(G); pw = np.empty(n)
    for i, fi in enumerate(f):
        X = np.column_stack([G, np.cos(2 * np.pi * fi * t), np.sin(2 * np.pi * fi * t)]); pw[i] = 1 - chi2(X) / c0
    return f, pw, c0
def fap_baluev(pmax, n, fmax, baseline, nparams_null=2):
    # Baluev 2008 approximation for floating-mean GLS: FAP ~ W * exp(-z) * ... use astropy's formula style
    z = pmax * (n - nparams_null - 2) / 2.0 / (1 - pmax) if pmax < 1 else np.inf   # not exact; use tau bound below
    from astropy.timeseries import LombScargle
    return None
from astropy.timeseries import LombScargle
rows = []; names = df.Name.astype(str).str.strip().unique()
for name in names:
    g = df[df.Name.astype(str).str.strip() == name]; g = g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp) & np.isfinite(g.e_DRVmlcnzp)]
    if len(g) < a.nmin: continue
    t = g.BJD.values; y = g.DRVmlcnzp.values; e = np.sqrt(g.e_DRVmlcnzp.values ** 2 + 1.0 ** 2)  # 1 m/s jitter floor
    # nightly binning to suppress intra-night noise and reduce N
    night = np.floor(t - 0.5); nb = pd.DataFrame(dict(night=night, t=t, y=y, w=1 / e ** 2))
    gb = nb.groupby("night"); tB = (gb.apply(lambda d: np.sum(d.t * d.w) / np.sum(d.w))).values; yB = (gb.apply(lambda d: np.sum(d.y * d.w) / np.sum(d.w))).values; eB = (gb.apply(lambda d: 1 / np.sqrt(np.sum(d.w)))).values
    if len(tB) < 25: continue
    # 5-sigma outlier clip
    med = np.median(yB); mad = 1.4826 * np.median(np.abs(yB - med)); k = np.abs(yB - med) < 5 * max(mad, 1.0); tB, yB, eB = tB[k], yB[k], eB[k]
    groups = (tB > 2457174.5).astype(int)   # HARPS fibre upgrade 2015-06-01
    # remove linear trend (with offsets) first
    X = np.column_stack([(groups == 0).astype(float), (groups == 1).astype(float), tB - tB.mean()]); W = 1 / eB
    coef = np.linalg.lstsq(X * W[:, None], yB * W, rcond=None)[0]; trend = coef[2]; yR = yB - X @ coef + np.where(groups == 0, coef[0], coef[1])
    baseline = tB.max() - tB.min(); fmin, fmax = 1 / min(5000.0, 2 * baseline), 1 / 1.2; n = int(min(20 * baseline * (fmax - fmin), 200000)); n = max(n, 2000)
    f, pw, c0 = periodogram(tB, yR, eB, groups, fmin, fmax, n)
    i = int(np.nanargmax(pw)); P = 1 / f[i]
    # Baluev FAP via astropy LombScargle on offset-corrected residuals (approximation)
    ls = LombScargle(tB, yR - np.where(groups == 0, np.average(yR[groups == 0], weights=1 / eB[groups == 0] ** 2) if (groups == 0).any() else 0, np.average(yR[groups == 1], weights=1 / eB[groups == 1] ** 2) if (groups == 1).any() else 0), eB)
    p_ls = ls.power(f); fap = float(ls.false_alarm_probability(np.nanmax(p_ls), method="baluev", minimum_frequency=fmin, maximum_frequency=fmax))
    # semi-amplitude
    Xs = np.column_stack([(groups == 0).astype(float), (groups == 1).astype(float), np.cos(2 * np.pi * f[i] * tB), np.sin(2 * np.pi * f[i] * tB)])
    cs = np.linalg.lstsq(Xs * W[:, None], yR * W, rcond=None)[0]; K = float(np.hypot(cs[2], cs[3])); rms_resid = float(np.std(yR - Xs @ cs))
    # activity indicators periodograms (nightly means)
    act = {}
    for ind in ["CRX", "dLW", "Halpha", "FWHMDRS"] + [k for k in g.columns if "BIS" in k.upper()]:
        if ind not in g.columns: continue
        v = g[ind].values; ok = np.isfinite(v)
        if ok.sum() < 25: continue
        nbA = pd.DataFrame(dict(night=night[ok], t=t[ok], v=v[ok])).groupby("night").mean()
        if len(nbA) < 25: continue
        lsA = LombScargle(nbA.t.values, nbA.v.values); pA = lsA.power(f); j = int(np.nanargmax(pA))
        act[ind] = dict(P=round(1 / f[j], 3), power=round(float(pA[j]), 3), fap=float(lsA.false_alarm_probability(pA[j], method="baluev", minimum_frequency=fmin, maximum_frequency=fmax)), power_at_rvP=round(float(pA[i]), 3))
    # activity match: any indicator with a significant peak within 5% of P (or aliases)
    def near(P1, P2, tol=0.05): return abs(P1 / P2 - 1) < tol
    def aliases(P):
        out = []
        for base in (1.0, 365.25, 29.53):
            for s in (+1, -1):
                fa = 1 / P + s / base
                if fa > 0: out.append(1 / fa)
        return out
    act_match = [k for k, v in act.items() if v["fap"] < 0.01 and (near(v["P"], P) or any(near(v["P"], q) for q in aliases(P)))]
    sysflag = any(near(P, q, 0.02) for q in (1.0, 0.5, 365.25, 182.6, 29.53, 27.3))
    # window function peak near P?
    lsw = LombScargle(tB, np.ones_like(tB), fit_mean=False, center_data=False); pwin = lsw.power(f); jw = int(np.nanargmax(pwin[1:]) + 1)
    star = None
    if name in lst.index:
        star = lst.loc[name]; star = star.iloc[0] if isinstance(star, pd.DataFrame) else star
    def sval(k, cast=float):
        try: return cast(star[k]) if star is not None else (np.nan if cast is float else "")
        except Exception: return np.nan if cast is float else ""
    kp = known_planets(name, sval("ra"), sval("dec")) if star is not None and np.isfinite(sval("ra")) else []
    known_match = [q for q in kp if np.isfinite(q[1]) and (near(P, q[1]) or near(P, q[1] / 2) or near(P, 2 * q[1]))]
    rows.append(dict(name=name, n_rv=int(len(g)), n_nights=int(len(tB)), baseline_d=round(baseline, 1), rms_ppm=None, rv_rms_ms=round(float(np.std(yR)), 2), trend_ms_per_yr=round(trend * 365.25, 2),
                     P_d=round(P, 4), power=round(float(pw[i]), 3), fap_baluev=fap, K_ms=round(K, 2), resid_rms_ms=round(rms_resid, 2), sys_alias=sysflag, window_peak_P=round(1 / f[jw], 2), window_power=round(float(pwin[jw]), 3),
                     activity_match=";".join(act_match), activity=json.dumps(act), known_planets=";".join(f"{q[0]}({q[1]} d,{q[2]})" for q in kp), known_match=";".join(q[0] for q in known_match), n_known=len(kp),
                     SpType=str(sval("SpType", str)).strip(), Teff=sval("Teff"), Vmag=sval("Vmag"), Dist=sval("Dist")))
    if len(rows) % 25 == 0:
        print(len(rows), name, "P", round(P, 2), "K", round(K, 1), "fap", f"{fap:.1e}", "known", len(kp), flush=True); pd.DataFrame(rows).to_csv(a.out, index=False)
out = pd.DataFrame(rows); out.to_csv(a.out, index=False)
print("stars searched:", len(out))
