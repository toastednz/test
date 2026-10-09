#!/usr/bin/env python3
"""Iterative multi-signal analysis of one HARPS RVBank star.

Model: per-instrument-epoch offsets (pre/post 2015-06 fibre upgrade) + linear trend + N circular
Keplerians. Signals are added one at a time from the floating-offset GLS periodogram of the
residuals (1.2-5000 d) while the Baluev FAP of the new peak is < --fapmax; after each addition all
periods/amplitudes/phases are re-fitted jointly (scipy least_squares). For each signal the 1-day and
1-year alias periods and their relative periodogram power are listed, and m sin i is computed for
--mstar. Output: multisignal.json and multisignal.png in OUTDIR.

Usage: 17_rv_multisignal.py RVBANK_DIR NAME OUTDIR [--mstar 1.0] [--nmax 6] [--fapmax 1e-3]
"""
import os, sys, re, json, argparse, warnings
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from astropy.timeseries import LombScargle
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("rvdir"); ap.add_argument("name"); ap.add_argument("outdir")
ap.add_argument("--mstar", type=float, default=1.0); ap.add_argument("--nmax", type=int, default=6); ap.add_argument("--fapmax", type=float, default=1e-3)
ap.add_argument("--jitter", type=float, default=1.0); ap.add_argument("--csv", default="", help="alternative input CSV with BJD, DRVmlcnzp, e_DRVmlcnzp, Flag"); ap.add_argument("--periods", default="", help="skip the iterative search and evaluate these fixed periods (comma list); one extra residual-search stage is still run"); ap.add_argument("--pmin", type=float, default=1.2); ap.add_argument("--pmax", type=float, default=5000.0)
a = ap.parse_args(); os.makedirs(a.outdir, exist_ok=True)

# ---- load
rd = open(os.path.join(a.rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]
cols = {}
for line in rd.splitlines():
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
    if m:
        g = m.groups()
        if len(g) == 4: cols[g[3]] = (int(g[0]) - 1, int(g[1]))
        else: cols[g[2]] = (int(g[0]) - 1, int(g[0]))
want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "Flag"]
rows = []
with open(os.path.join(a.rvdir, "rvbank.dat")) as f:
    for line in f:
        if line[cols["Name"][0]:cols["Name"][1]].strip() == a.name:
            rows.append([line[cols[w][0]:cols[w][1]] for w in want])
g = pd.DataFrame(rows, columns=want)
for c in want[1:]: g[c] = pd.to_numeric(g[c], errors="coerce")
if a.csv: g = pd.read_csv(a.csv)
g = g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp) & np.isfinite(g.e_DRVmlcnzp) & (g.DRVmlcnzp > -9e6)]
t = g.BJD.values; y = g.DRVmlcnzp.values; e = np.sqrt(g.e_DRVmlcnzp.values ** 2 + a.jitter ** 2)
night = np.floor(t - 0.5); nb = pd.DataFrame(dict(night=night, t=t, y=y, w=1 / e ** 2)); gb = nb.groupby("night")
tB = (gb.apply(lambda d: np.sum(d.t * d.w) / np.sum(d.w))).values; yB = (gb.apply(lambda d: np.sum(d.y * d.w) / np.sum(d.w))).values; eB = (gb.apply(lambda d: 1 / np.sqrt(np.sum(d.w)))).values
med = np.median(yB); mad = 1.4826 * np.median(np.abs(yB - med)); k = np.abs(yB - med) < 5 * max(mad, 1.0); tB, yB, eB = tB[k], yB[k], eB[k]
grp = (tB > 2457174.5).astype(int); tref = tB.mean(); n = len(tB)
G = np.column_stack([(grp == 0).astype(float), (grp == 1).astype(float)]); G = G[:, G.sum(0) > 0]
W = 1 / eB

def design(periods, tt=None):
    tt = tB if tt is None else tt
    X = [G if tt is tB else np.column_stack([(tt * 0 + 1)]), (tt - tref)[:, None] / 365.25]
    for P in periods: X += [np.cos(2 * np.pi * tt / P)[:, None], np.sin(2 * np.pi * tt / P)[:, None]]
    return np.hstack(X)
def linfit(periods):
    X = design(periods); coef = np.linalg.lstsq(X * W[:, None], yB * W, rcond=None)[0]; r = yB - X @ coef; return coef, r, float(np.sum((r * W) ** 2))
def resid_fun(p, nsig):
    periods = np.exp(p[:nsig]); _, r, _ = linfit(periods); return r * W
def gls(resid):
    fmin, fmax = 1 / a.pmax, 1 / a.pmin; nf = int(min(max(20 * (tB.max() - tB.min()) * (fmax - fmin), 5000), 200000))
    f = np.linspace(fmin, fmax, nf); c0 = np.sum((resid * W) ** 2); pw = np.empty(nf)
    base = np.column_stack([G])
    for i, fi in enumerate(f):
        X = np.column_stack([base, np.cos(2 * np.pi * fi * tB), np.sin(2 * np.pi * fi * tB)])
        coef = np.linalg.lstsq(X * W[:, None], resid * W, rcond=None)[0]; rr = resid - X @ coef; pw[i] = 1 - np.sum((rr * W) ** 2) / c0
    return f, pw
def fap(resid, P):
    ls = LombScargle(tB, resid, eB); pwr = ls.power(np.array([1 / P]))[0]
    return float(ls.false_alarm_probability(pwr, method="baluev", minimum_frequency=1 / a.pmax, maximum_frequency=1 / a.pmin))

signals = []; stages = []
coef, resid, chi2 = linfit([])
chi2_0 = chi2
if a.periods:
    periods = [float(x) for x in a.periods.split(",")]
    p0 = np.log(np.array(periods)); sol = least_squares(resid_fun, p0, args=(len(p0),), method="lm")
    periods = list(np.exp(sol.x)); coef, resid, chi2 = linfit(periods); signals = [dict(P=float(Pj)) for Pj in periods]
    off = G.shape[1] + 1
    for j, s_ in enumerate(signals):
        A, B = coef[off + 2 * j], coef[off + 2 * j + 1]; s_["K_ms"] = float(np.hypot(A, B)); s_["phase"] = float(np.arctan2(B, A))
    f, pw = gls(resid); i = int(np.argmax(pw)); P = 1 / f[i]; stages.append(dict(stage=len(periods) + 1, P=float(P), power=float(pw[i]), fap=fap(resid, P), f=f, pw=pw))
for it in range(0 if a.periods else a.nmax):
    f, pw = gls(resid); i = int(np.argmax(pw)); P = 1 / f[i]; fp = fap(resid, P)
    stages.append(dict(stage=it + 1, P=float(P), power=float(pw[i]), fap=fp, f=f, pw=pw))
    if fp > a.fapmax: break
    # joint nonlinear refit of all periods
    p0 = np.log(np.array([s["P"] for s in signals] + [P]))
    sol = least_squares(resid_fun, p0, args=(len(p0),), method="lm")
    periods = list(np.exp(sol.x)); coef, resid, chi2 = linfit(periods)
    signals = [dict(P=float(Pj)) for Pj in periods]
    # amplitudes from coef
    off = G.shape[1] + 1
    for j, s in enumerate(signals):
        A, B = coef[off + 2 * j], coef[off + 2 * j + 1]; s["K_ms"] = float(np.hypot(A, B)); s["phase"] = float(np.arctan2(B, A))
    stages[-1]["chi2_after"] = chi2
# significance of each signal in the final model: drop-one FAP and dchi2
final = []
for j, s in enumerate(signals):
    others = [q["P"] for q in signals if q is not s]; _, r_wo, chi2_wo = linfit(others)
    fp = fap(r_wo, s["P"]); f_, pw_ = gls(r_wo); 
    # alias powers
    P = s["P"]; al = {}
    for lab, fa in (("1d-", 1 - 1 / P), ("1d+", 1 + 1 / P), ("1yr-", 1 / P - 1 / 365.25), ("1yr+", 1 / P + 1 / 365.25)):
        if 1 / a.pmax < fa < 1 / a.pmin:
            Pa = 1 / fa; k = np.argmin(np.abs(f_ - fa)); al[lab] = dict(P=float(Pa), power=float(pw_[max(0, k - 3):k + 4].max()))
    kpk = np.argmin(np.abs(f_ - 1 / P)); own = float(pw_[max(0, kpk - 3):kpk + 4].max())
    msini = s["K_ms"] / 0.0895 * (P / 365.25) ** (1 / 3) * a.mstar ** (2 / 3)
    rms_wo = float(np.std(r_wo))
    final.append(dict(P=P, K_ms=s["K_ms"], msini_earth=float(msini), a_au=float((P / 365.25) ** (2 / 3) * a.mstar ** (1 / 3)),
                      fap_drop_one=fp, dchi2_drop_one=float(chi2_wo - chi2), power_own=own, aliases=al))
out = dict(name=a.name, n_nights=int(n), baseline_d=float(tB.max() - tB.min()), rms_raw_ms=float(np.std(yB)), rms_final_ms=float(np.std(resid)),
           chi2_null=chi2_0, chi2_final=chi2, trend_ms_per_yr=float(coef[G.shape[1]]), mstar=a.mstar, signals=final,
           stages=[{k: v for k, v in s.items() if k not in ("f", "pw")} for s in stages])
json.dump(out, open(os.path.join(a.outdir, "multisignal.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "stages"}, indent=1)); print("stages:", out["stages"])
# ---- figure
ns = len(stages); fig, axes = plt.subplots(ns + len(final), 1, figsize=(12, 2.4 * (ns + len(final))))
axes = np.atleast_1d(axes)
for i, s in enumerate(stages):
    ax = axes[i]; ax.semilogx(1 / s["f"], s["pw"], lw=0.6, color="k"); ax.set_ylabel(f"stage {s['stage']}")
    ax.set_title(f"peak P={s['P']:.4f} d  power={s['power']:.3f}  FAP={s['fap']:.1e}", fontsize=9)
    for q in final: ax.axvline(q["P"], color="r", alpha=0.3)
for j, s in enumerate(final):
    ax = axes[ns + j]; others = [q["P"] for q in final if q is not s]; _, r_wo, _ = linfit(others)
    ph = (tB / s["P"]) % 1; ax.errorbar(ph, r_wo, eB, fmt=".", ms=3, alpha=0.6); ax.errorbar(ph + 1, r_wo, eB, fmt=".", ms=3, alpha=0.6, color="C0")
    xx = np.linspace(0, 2, 200); 
    A = s["K_ms"] * np.cos(2 * np.pi * xx + np.arctan2(*[0, 1]) * 0)
    coef_, _, _ = linfit([q["P"] for q in final]); off = G.shape[1] + 1; jj = [q["P"] for q in final].index(s["P"])
    Ac, Bc = coef_[off + 2 * jj], coef_[off + 2 * jj + 1]; ax.plot(xx, Ac * np.cos(2 * np.pi * xx) + Bc * np.sin(2 * np.pi * xx), "r-")
    ax.set_title(f"P={s['P']:.4f} d  K={s['K_ms']:.2f} m/s  m sin i={s['msini_earth']:.1f} Me  FAP(drop-one)={s['fap_drop_one']:.1e}", fontsize=9); ax.set_xlabel("phase")
plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "multisignal.png"), dpi=110)
