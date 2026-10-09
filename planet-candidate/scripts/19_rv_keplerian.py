#!/usr/bin/env python3
"""Joint Keplerian fit (eccentric orbits) to one HARPS RVBank star with per-epoch offsets, linear
trend and a fitted white-noise jitter, starting from the circular multi-signal solution.
Uncertainties from the Jacobian covariance at the optimum (approximate, 1 sigma). Also compares the
fit with the 1-yr alias period of signal 1 if --alias1 is given.

Usage: 19_rv_keplerian.py RVBANK_DIR NAME P1,P2,... OUTDIR [--mstar 1.0] [--alias1 P] [--csv file]
"""
import os, sys, re, json, argparse, warnings
import numpy as np, pandas as pd
from scipy.optimize import least_squares, minimize
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("rvdir"); ap.add_argument("name"); ap.add_argument("periods"); ap.add_argument("outdir")
ap.add_argument("--mstar", type=float, default=1.0); ap.add_argument("--alias1", type=float, default=0.0); ap.add_argument("--csv", default="")
ap.add_argument("--circular", action="store_true")
a = ap.parse_args(); os.makedirs(a.outdir, exist_ok=True); P0 = [float(x) for x in a.periods.split(",")]

def load_rvbank(rvdir, name):
    rd = open(os.path.join(rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]; cols = {}
    for line in rd.splitlines():
        m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
        if m:
            g = m.groups()
            if len(g) == 4: cols[g[3]] = (int(g[0]) - 1, int(g[1]))
            else: cols[g[2]] = (int(g[0]) - 1, int(g[0]))
    want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "Flag"]; rows = []
    with open(os.path.join(rvdir, "rvbank.dat")) as f:
        for line in f:
            if line[cols["Name"][0]:cols["Name"][1]].strip() == name: rows.append([line[cols[w][0]:cols[w][1]] for w in want])
    g = pd.DataFrame(rows, columns=want)
    for c in want[1:]: g[c] = pd.to_numeric(g[c], errors="coerce")
    return g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp) & np.isfinite(g.e_DRVmlcnzp) & (g.DRVmlcnzp > -9e6)]
if a.csv:
    g = pd.read_csv(a.csv); g = g[np.isfinite(g.DRVmlcnzp)]
    if "e_DRVmlcnzp" not in g: g["e_DRVmlcnzp"] = 1.0
else:
    g = load_rvbank(a.rvdir, a.name)
t = g.BJD.values; y = g.DRVmlcnzp.values; e = np.sqrt(g.e_DRVmlcnzp.values ** 2)
night = np.floor(t - 0.5); w = 1 / np.maximum(e, 0.3) ** 2
nb = pd.DataFrame(dict(night=night, t=t, y=y, w=w)).groupby("night")
tB = nb.apply(lambda d: np.sum(d.t * d.w) / np.sum(d.w)).values; yB = nb.apply(lambda d: np.sum(d.y * d.w) / np.sum(d.w)).values; eB = nb.apply(lambda d: 1 / np.sqrt(np.sum(d.w))).values
med = np.median(yB); mad = 1.4826 * np.median(np.abs(yB - med)); k = np.abs(yB - med) < 5 * max(mad, 1.0); tB, yB, eB = tB[k], yB[k], eB[k]
grp = (tB > 2457174.5).astype(int); ngrp = len(np.unique(grp)); tref = np.round(tB.mean()); n = len(tB); npl = len(P0)

def kepler_E(M, ecc):
    E = M.copy() if ecc < 0.8 else np.pi * np.ones_like(M)
    for _ in range(50):
        dE = (E - ecc * np.sin(E) - M) / (1 - ecc * np.cos(E)); E -= dE
        if np.max(np.abs(dE)) < 1e-12: break
    return E
def rv_kep(tt, P, K, ecc, om, tp):
    M = 2 * np.pi * ((tt - tp) / P % 1.0); E = kepler_E(M, ecc)
    nu = 2 * np.arctan2(np.sqrt(1 + ecc) * np.sin(E / 2), np.sqrt(1 - ecc) * np.cos(E / 2))
    return K * (np.cos(nu + om) + ecc * np.cos(om))
# parameter vector: per planet [lnP, K, sqrt(e)cos w, sqrt(e)sin w, tp_phase]; then offsets(ngrp), trend, lnjit
def unpack(p):
    pl = []
    for j in range(npl):
        lnP, K, sc, ss, ph = p[5 * j:5 * j + 5]; ecc = min(sc ** 2 + ss ** 2, 0.95); om = np.arctan2(ss, sc); P = np.exp(lnP)
        pl.append((P, K, ecc, om, tref + ph * P))
    off = p[5 * npl:5 * npl + ngrp]; tr = p[5 * npl + ngrp]; jit = np.exp(p[5 * npl + ngrp + 1]); return pl, off, tr, jit
def model(p, tt=None, which=None):
    tt = tB if tt is None else tt; pl, off, tr, jit = unpack(p); m = np.zeros_like(tt)
    for j, (P, K, ecc, om, tp) in enumerate(pl):
        if which is None or j in which: m += rv_kep(tt, P, K, ecc, om, tp)
    if which is None: m += off[grp if tt is tB else 0] + tr * (tt - tref) / 365.25
    return m
def nll(p):
    pl, off, tr, jit = unpack(p); s2 = eB ** 2 + jit ** 2; r = yB - model(p)
    if a.circular and any(pp[2] > 1e-6 for pp in pl): return 1e30
    return 0.5 * np.sum(r ** 2 / s2 + np.log(2 * np.pi * s2))
def fit(periods):
    global npl
    npl_save = npl; npl = len(periods)
    # start: circular linear solution for K, phase
    p = []
    for P in periods:
        X = np.column_stack([np.ones(n), (tB - tref) / 365.25, np.cos(2 * np.pi * tB / P), np.sin(2 * np.pi * tB / P)])
        c = np.linalg.lstsq(X / eB[:, None], yB / eB, rcond=None)[0]; K = np.hypot(c[2], c[3]); ph = np.arctan2(c[3], c[2])
        # cos(2pi t/P + ...) -> tp where RV max: 2pi(t-tp)/P = -ph  => tp = tref + ph*P/(2pi)   (circular: om=0, nu=M)
        p += [np.log(P), K, 0.0 if not a.circular else 0.0, 0.0, (-ph / (2 * np.pi)) % 1.0]
    p += [np.median(yB)] * ngrp + [0.0, np.log(1.0)]
    p = np.array(p)
    bounds = []
    for j in range(npl): bounds += [(np.log(periods[j] * 0.97), np.log(periods[j] * 1.03)), (0, 50), (-0.9, 0.9), (-0.9, 0.9), (-1, 2)]
    bounds += [(-100, 100)] * ngrp + [(-20, 20), (np.log(0.05), np.log(20))]
    if a.circular:
        for j in range(npl): bounds[5 * j + 2] = (0, 0); bounds[5 * j + 3] = (0, 0)
    best = None
    for trial in range(3):
        p_try = p.copy()
        if trial: p_try[[5 * j + 2 for j in range(npl)]] = np.random.uniform(-0.3, 0.3, npl); p_try[[5 * j + 3 for j in range(npl)]] = np.random.uniform(-0.3, 0.3, npl)
        if a.circular: p_try[[5 * j + 2 for j in range(npl)]] = 0; p_try[[5 * j + 3 for j in range(npl)]] = 0
        r = minimize(nll, p_try, method="L-BFGS-B", bounds=bounds, options=dict(maxiter=5000))
        if best is None or r.fun < best.fun: best = r
    npl = npl_save
    return best
np.random.seed(1)
res = fit(P0); p = res.x; pl, off, tr, jit = unpack(p)
# covariance via numerical Hessian of nll
def hess(f, x, h=1e-4):
    nx = len(x); H = np.zeros((nx, nx)); f0 = f(x)
    for i in range(nx):
        for j in range(i, nx):
            xi = x.copy(); xi[i] += h; xj = x.copy(); xj[j] += h; xij = x.copy(); xij[i] += h; xij[j] += h
            H[i, j] = H[j, i] = (f(xij) - f(xi) - f(xj) + f0) / h ** 2
    return H
free = [i for i in range(len(p)) if not (a.circular and i % 5 in (2, 3) and i < 5 * npl)]
H = hess(lambda x: nll(np.array([x[free.index(i)] if i in free else p[i] for i in range(len(p))])), p[free])
try: cov = np.linalg.inv(H); err = np.sqrt(np.maximum(np.diag(cov), 0))
except Exception: err = np.full(len(free), np.nan)
efull = np.full(len(p), np.nan); efull[free] = err
r = yB - model(p); s2 = eB ** 2 + jit ** 2; chi2 = float(np.sum(r ** 2 / s2)); lnL = -res.fun
out = dict(name=a.name, n_nights=int(n), baseline_d=float(tB.max() - tB.min()), mstar=a.mstar, jitter_ms=float(jit), trend_ms_per_yr=float(tr), offsets=list(map(float, off)),
           chi2=chi2, lnL=float(lnL), bic=float(-2 * lnL + len(free) * np.log(n)), rms_resid_ms=float(np.std(r)), planets=[])
for j, (P, K, ecc, om, tp) in enumerate(pl):
    eP = P * efull[5 * j]; eK = efull[5 * j + 1]
    sc, ss = p[5 * j + 2], p[5 * j + 3]; esc, ess = efull[5 * j + 2], efull[5 * j + 3]
    e_ecc = float(np.hypot(2 * sc * esc, 2 * ss * ess)) if np.isfinite(esc) else float("nan")
    msini = K / 0.0895 * (P / 365.25) ** (1 / 3) * a.mstar ** (2 / 3) * np.sqrt(1 - ecc ** 2)
    out["planets"].append(dict(P=float(P), eP=float(eP), K_ms=float(K), eK_ms=float(eK), e=float(ecc), e_err=e_ecc, omega_deg=float(np.degrees(om)), tp_bjd=float(tp),
                               msini_earth=float(msini), emsini_earth=float(msini * np.hypot(eK / max(K, 1e-6), eP / P / 3)), a_au=float((P / 365.25) ** (2 / 3) * a.mstar ** (1 / 3))))
# null and (N-1)-planet comparisons
def lnL_of(periods):
    rr = fit(periods); return float(-rr.fun), rr
comps = {}
for j in range(npl):
    others = [P0[i] for i in range(npl) if i != j]; l, _ = lnL_of(others); comps[f"without_{P0[j]:.4f}"] = dict(lnL=l, dlnL=float(lnL - l), dBIC=float((-2 * l + (len(free) - 5) * np.log(n)) - out["bic"]))
l0, _ = lnL_of([]); comps["null"] = dict(lnL=l0, dlnL=float(lnL - l0))
out["model_comparison"] = comps
if a.alias1:
    la, ra = lnL_of([a.alias1] + P0[1:]); out["alias1"] = dict(P=a.alias1, lnL=la, dlnL_vs_best=float(lnL - la))
json.dump(out, open(os.path.join(a.outdir, "keplerian.json"), "w"), indent=1)
print(json.dumps(out, indent=1))
# figure
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, axes = plt.subplots(npl + 1, 1, figsize=(11, 2.6 * (npl + 1)))
axes[0].errorbar(tB - 2450000, yB - off[grp] - tr * (tB - tref) / 365.25, np.sqrt(s2), fmt=".", ms=3, alpha=0.6); tt = np.linspace(tB.min(), tB.max(), 20000)
axes[0].plot(tt - 2450000, model(p, tt, which=list(range(npl))), "r-", lw=0.4, alpha=0.7); axes[0].set_title(f"{a.name}: {npl}-Keplerian fit, jitter={jit:.2f} m/s, rms={np.std(r):.2f} m/s", fontsize=9); axes[0].set_xlabel("BJD-2450000")
for j, (P, K, ecc, om, tp) in enumerate(pl):
    ax = axes[j + 1]; others = [i for i in range(npl) if i != j]; rr = yB - off[grp] - tr * (tB - tref) / 365.25 - model(p, which=others) if others else yB - off[grp] - tr * (tB - tref) / 365.25
    ph = ((tB - tp) / P) % 1; ax.errorbar(ph, rr, np.sqrt(s2), fmt=".", ms=3, alpha=0.6); ax.errorbar(ph + 1, rr, np.sqrt(s2), fmt=".", ms=3, alpha=0.6, color="C0")
    xx = np.linspace(0, 2, 400); ax.plot(xx, rv_kep(tp + xx * P, P, K, ecc, om, tp), "r-")
    pj = out["planets"][j]; ax.set_title(f"P={P:.4f}±{pj['eP']:.4f} d  K={K:.2f}±{pj['eK_ms']:.2f} m/s  e={ecc:.2f}  m sin i={pj['msini_earth']:.1f}±{pj['emsini_earth']:.1f} Me", fontsize=9); ax.set_xlabel("orbital phase")
plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "keplerian.png"), dpi=110)
