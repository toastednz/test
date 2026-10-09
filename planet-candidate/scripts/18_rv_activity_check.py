#!/usr/bin/env python3
"""Activity-indicator test for a multi-signal RV model of one HARPS RVBank star.

For each candidate period P (comma list) and each SERVAL/DRS indicator (CRX, dLW, Halpha, NaD1, NaD2,
FWHMDRS, Contrast, BIS): floating-offset GLS power of the indicator at P (and the max within +-2% of P),
the indicator's own best period/power/FAP over 1.2-5000 d, and the Spearman correlation between the
indicator and the RV residuals with all *other* signals removed (so that a planet signal would show
no correlation, while an activity signal would). Output: activity_check.json

Usage: 18_rv_activity_check.py RVBANK_DIR NAME P1,P2,... OUTDIR
"""
import os, sys, re, json, warnings
import numpy as np, pandas as pd
from scipy.stats import spearmanr
from astropy.timeseries import LombScargle
warnings.filterwarnings("ignore")
rvdir, name, plist, outdir = sys.argv[1:5]; periods = [float(x) for x in plist.split(",")]; os.makedirs(outdir, exist_ok=True)
rd = open(os.path.join(rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]
cols = {}
for line in rd.splitlines():
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
    if m:
        g = m.groups()
        if len(g) == 4: cols[g[3]] = (int(g[0]) - 1, int(g[1]))
        else: cols[g[2]] = (int(g[0]) - 1, int(g[0]))
inds = [c for c in ["CRX", "dLW", "Halpha", "NaD1", "NaD2", "FWHMDRS", "Contrast", "BIS"] if c in cols]
want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "Flag"] + inds
rows = []
with open(os.path.join(rvdir, "rvbank.dat")) as f:
    for line in f:
        if line[cols["Name"][0]:cols["Name"][1]].strip() == name:
            rows.append([line[cols[w][0]:cols[w][1]] for w in want])
g = pd.DataFrame(rows, columns=want)
for c in want[1:]: g[c] = pd.to_numeric(g[c], errors="coerce")
g = g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp) & (g.DRVmlcnzp > -9e6)]
g = g.replace(-9999999, np.nan)
g["night"] = np.floor(g.BJD - 0.5)
nb = g.groupby("night").agg({"BJD": "mean", "DRVmlcnzp": "mean", "e_DRVmlcnzp": lambda x: np.sqrt(np.sum(x ** 2)) / len(x), **{c: "mean" for c in inds}}).reset_index()
t = nb.BJD.values; y = nb.DRVmlcnzp.values; e = np.sqrt(nb.e_DRVmlcnzp.values ** 2 + 1.0)
med = np.median(y); mad = 1.4826 * np.median(np.abs(y - med)); k = np.abs(y - med) < 5 * max(mad, 1.0); nb = nb[k]; t, y, e = t[k], y[k], e[k]
grp = (t > 2457174.5).astype(int); G = np.column_stack([(grp == 0).astype(float), (grp == 1).astype(float)]); G = G[:, G.sum(0) > 0]
tref = t.mean()
def design(ps, tt):
    X = [G, ((tt - tref) / 365.25)[:, None]]
    for P in ps: X += [np.cos(2 * np.pi * tt / P)[:, None], np.sin(2 * np.pi * tt / P)[:, None]]
    return np.hstack(X)
def fit_resid(ps, yy, ee):
    X = design(ps, t); W = 1 / ee; coef = np.linalg.lstsq(X * W[:, None], yy * W, rcond=None)[0]; return yy - X @ coef
def gls(yy, ee, fgrid):
    W = 1 / ee; c0 = np.sum(((yy - np.average(yy, weights=W ** 2)) * W) ** 2); pw = np.empty(len(fgrid))
    for i, fi in enumerate(fgrid):
        X = np.column_stack([G, np.cos(2 * np.pi * fi * t), np.sin(2 * np.pi * fi * t)]); coef = np.linalg.lstsq(X * W[:, None], yy * W, rcond=None)[0]
        pw[i] = 1 - np.sum(((yy - X @ coef) * W) ** 2) / c0
    return pw
base = t.max() - t.min(); fgrid = np.linspace(1 / 5000, 1 / 1.2, int(min(max(20 * base * (1 / 1.2 - 1 / 5000), 5000), 100000)))
out = dict(name=name, n_nights=int(len(t)), periods=periods, indicators={})
rv_resid_each = {P: fit_resid([q for q in periods if q != P], y, e) for P in periods}
for c in inds:
    v = nb[c].values.astype(float); ok = np.isfinite(v)
    if ok.sum() < 20: continue
    vv = v[ok]; m = np.median(vv); s = 1.4826 * np.median(np.abs(vv - m)); good = np.abs(vv - m) < 5 * max(s, 1e-12)
    tt = t[ok][good]; vv = vv[good]; ee = np.full(len(vv), max(np.std(vv), 1e-12))
    Gi = G[ok][good]
    # prewhiten long-period (>300 d) variability + linear trend from the indicator so that cycles/trends do not dominate
    longP = []
    for _ in range(3):
        fl = np.linspace(1 / 5000, 1 / 300, 3000); Wl = 1 / ee
        c0 = np.sum(((vv - vv.mean()) * Wl) ** 2); pwl = np.empty(len(fl))
        for i, fi in enumerate(fl):
            X = np.column_stack([Gi, (tt - tref) / 365.25, np.cos(2 * np.pi * fi * tt), np.sin(2 * np.pi * fi * tt)]); coef = np.linalg.lstsq(X * Wl[:, None], vv * Wl, rcond=None)[0]
            pwl[i] = 1 - np.sum(((vv - X @ coef) * Wl) ** 2) / c0
        ib_ = int(np.argmax(pwl)); lsl = LombScargle(tt, vv)
        if float(lsl.false_alarm_probability(lsl.power(fl[ib_]), method="baluev", minimum_frequency=fl[0], maximum_frequency=fl[-1])) > 1e-3: break
        P_ = 1 / fl[ib_]; X = np.column_stack([Gi, (tt - tref) / 365.25, np.cos(2 * np.pi * tt / P_), np.sin(2 * np.pi * tt / P_)]); coef = np.linalg.lstsq(X * Wl[:, None], vv * Wl, rcond=None)[0]
        vv = vv - X @ coef + vv.mean(); longP.append(float(P_))
    ee = np.full(len(vv), max(np.std(vv), 1e-12))
    def gls_i(fg):
        W = 1 / ee; c0 = np.sum(((vv - vv.mean()) * W) ** 2); pw = np.empty(len(fg))
        for i, fi in enumerate(fg):
            X = np.column_stack([Gi, np.cos(2 * np.pi * fi * tt), np.sin(2 * np.pi * fi * tt)]); coef = np.linalg.lstsq(X * W[:, None], vv * W, rcond=None)[0]
            pw[i] = 1 - np.sum(((vv - X @ coef) * W) ** 2) / c0
        return pw
    pw = gls_i(fgrid); ib = int(np.argmax(pw)); ls = LombScargle(tt, vv)
    fapb = float(ls.false_alarm_probability(ls.power(fgrid[ib]), method="baluev", minimum_frequency=fgrid[0], maximum_frequency=fgrid[-1]))
    res = dict(n=int(len(vv)), prewhitened_longP=longP, best_P=float(1 / fgrid[ib]), best_power=float(pw[ib]), best_fap=fapb, at_P={})
    for P in periods:
        win = np.abs(fgrid * P - 1) < 0.02; pP = float(pw[win].max()) if win.any() else float("nan")
        fp = float(ls.false_alarm_probability(ls.power(1 / P), method="baluev", minimum_frequency=fgrid[0], maximum_frequency=fgrid[-1]))
        r = rv_resid_each[P][ok][good]; rho, pval = spearmanr(r, vv)
        res["at_P"][f"{P:.4f}"] = dict(power=pP, fap_at_P=fp, spearman_rho_vs_rv_resid=float(rho), spearman_p=float(pval))
    out["indicators"][c] = res
json.dump(out, open(os.path.join(outdir, "activity_check.json"), "w"), indent=1)
for c, r in out["indicators"].items():
    print(f"{c:9s} n={r['n']} longP={[round(x) for x in r['prewhitened_longP']]} bestP={r['best_P']:.1f} pow={r['best_power']:.3f} fap={r['best_fap']:.1e} | " + " ".join(f"P{P}: pow={q['power']:.3f} rho={q['spearman_rho_vs_rv_resid']:+.2f}(p={q['spearman_p']:.2f})" for P, q in r["at_P"].items()))
