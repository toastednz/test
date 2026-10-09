#!/usr/bin/env python3
"""Vet an RV periodogram candidate from HARPS RVBank: nightly RVs, periodograms of RV and indicators,
RV-indicator correlations, half-sample consistency, bootstrap FAP, phase-fold figure.

Usage: 15_rv_vet.py RVBANK_DIR NAME P OUTDIR [--nboot 300]
"""
import os, sys, re, json, argparse, warnings
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(); ap.add_argument("rvdir"); ap.add_argument("name"); ap.add_argument("P", type=float); ap.add_argument("outdir"); ap.add_argument("--nboot", type=int, default=300); a = ap.parse_args()
os.makedirs(a.outdir, exist_ok=True)
rd = open(os.path.join(a.rvdir, "ReadMe")).read().split("Byte-by-byte Description of file: rvbank.dat")[1]
cols = {}
for line in rd.splitlines():
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line) or re.match(r"\s+(\d+)\s+[A-Z]\d+(\.\d+)?\s+\S+\s+(\S+)", line)
    if m:
        g = m.groups(); cols[g[3] if len(g) == 4 else g[2]] = (int(g[0]) - 1, int(g[1])) if len(g) == 4 else (int(g[0]) - 1, int(g[0]))
want = ["Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "CRX", "dLW", "Halpha", "NaD1", "NaD2", "Flag", "FWHMDRS"] + [k for k in cols if "BIS" in k.upper()][:1] + [k for k in cols if "CONTRAST" in k.upper()][:1]
want = [w for w in want if w in cols]
df = pd.read_fwf(os.path.join(a.rvdir, "rvbank.dat"), colspecs=[cols[w] for w in want], names=want, header=None)
for c in want[1:]: df[c] = pd.to_numeric(df[c], errors="coerce")
df = df.replace(-9999999, np.nan); g = df[df.Name.astype(str).str.strip() == a.name]; g = g[(g.Flag == 0) & np.isfinite(g.DRVmlcnzp)]
t = g.BJD.values; y = g.DRVmlcnzp.values; e = np.sqrt(g.e_DRVmlcnzp.values ** 2 + 1.0)
night = np.floor(t - 0.5); nb = pd.DataFrame(dict(night=night, t=t, y=y, w=1 / e ** 2)); gb = nb.groupby("night")
tB = (gb.apply(lambda d: np.sum(d.t * d.w) / np.sum(d.w))).values; yB = (gb.apply(lambda d: np.sum(d.y * d.w) / np.sum(d.w))).values; eB = (gb.apply(lambda d: 1 / np.sqrt(np.sum(d.w)))).values
med = np.median(yB); mad = 1.4826 * np.median(np.abs(yB - med)); k = np.abs(yB - med) < 5 * max(mad, 1.0); tB, yB, eB = tB[k], yB[k], eB[k]
grp = (tB > 2457174.5).astype(int); X = np.column_stack([(grp == 0).astype(float), (grp == 1).astype(float), tB - tB.mean()]); W = 1 / eB
coef = np.linalg.lstsq(X * W[:, None], yB * W, rcond=None)[0]; yR = yB - X @ coef
baseline = tB.max() - tB.min(); fmin, fmax = 1 / min(5000.0, 2 * baseline), 1 / 1.2; f = np.linspace(fmin, fmax, 60000)
ls = LombScargle(tB, yR, eB); p = ls.power(f); i = int(np.argmax(p)); Pbest = 1 / f[i]
fapb = float(ls.false_alarm_probability(p[i], method="baluev", minimum_frequency=fmin, maximum_frequency=fmax))
# bootstrap FAP: shuffle residuals, keep times
rng = np.random.default_rng(1); mx = []
for _ in range(a.nboot):
    ys = rng.permutation(yR); mx.append(float(np.max(LombScargle(tB, ys, eB).power(f))))
boot_fap = float(np.mean(np.array(mx) >= p[i]))
# sinusoid fit at the candidate period (fixed P from search) and at Pbest
def sinfit(P):
    Xs = np.column_stack([np.ones_like(tB), np.cos(2 * np.pi * tB / P), np.sin(2 * np.pi * tB / P)]); cs = np.linalg.lstsq(Xs * W[:, None], yR * W, rcond=None)[0]
    K = float(np.hypot(cs[1], cs[2])); phase = float(np.arctan2(cs[2], cs[1])); resid = yR - Xs @ cs; return K, phase, float(np.std(resid)), resid
K, ph, rms_res, resid = sinfit(a.P)
# half-sample consistency
h1 = tB < np.median(tB); out_half = {}
for lab, sel in [("first_half", h1), ("second_half", ~h1), ("pre2015", grp == 0), ("post2015", grp == 1)]:
    if sel.sum() < 15: continue
    Xs = np.column_stack([np.ones(sel.sum()), np.cos(2 * np.pi * tB[sel] / a.P), np.sin(2 * np.pi * tB[sel] / a.P)]); cs = np.linalg.lstsq(Xs * W[sel][:, None], yR[sel] * W[sel], rcond=None)[0]
    out_half[lab] = dict(n=int(sel.sum()), K=round(float(np.hypot(cs[1], cs[2])), 2), phase_deg=round(float(np.degrees(np.arctan2(cs[2], cs[1]))), 1))
# second periodogram on residuals after removing candidate
ls2 = LombScargle(tB, resid, eB); p2 = ls2.power(f); i2 = int(np.argmax(p2))
# indicators: periodogram power at P, best period, correlation with RV (nightly)
ind = {}
for c in [w for w in want if w not in ("Name", "BJD", "DRVmlcnzp", "e_DRVmlcnzp", "Flag")]:
    v = g[c].values; ok = np.isfinite(v)
    if ok.sum() < 20: continue
    nbI = pd.DataFrame(dict(night=night[ok], t=t[ok], v=v[ok])).groupby("night").agg(t=("t", "mean"), v=("v", "mean"))
    # align to RV nights
    common = np.intersect1d(np.round(nbI.t.values, 3), np.round(tB, 3))
    if len(common) < 15: continue
    vI = nbI.set_index(np.round(nbI.t.values, 3)).loc[common, "v"].values; rI = pd.Series(yR, index=np.round(tB, 3)).loc[common].values
    r = float(np.corrcoef(vI, rI)[0, 1]) if np.std(vI) > 0 else np.nan
    lsI = LombScargle(nbI.t.values, nbI.v.values); pI = lsI.power(f); jI = int(np.argmax(pI))
    ind[c] = dict(n=int(len(nbI)), corr_with_rv=round(r, 3), best_P=round(1 / f[jI], 2), best_power=round(float(pI[jI]), 3), best_fap=float(lsI.false_alarm_probability(pI[jI], method="baluev", minimum_frequency=fmin, maximum_frequency=fmax)), power_at_P=round(float(pI[int(np.argmin(np.abs(f - 1 / a.P)))]), 3))
res = dict(name=a.name, n_rv=int(len(g)), n_nights=int(len(tB)), baseline_d=round(baseline, 1), rv_rms_ms=round(float(np.std(yR)), 2), trend_ms_per_yr=round(float(coef[2] * 365.25), 2), offset_post_minus_pre_ms=round(float(coef[1] - coef[0]), 2),
           P_search=a.P, P_best_gls=round(Pbest, 4), power_best=round(float(p[i]), 3), fap_baluev=fapb, boot_fap=boot_fap, n_boot=a.nboot, boot_max_power_95=round(float(np.percentile(mx, 95)), 3),
           K_ms=round(K, 2), resid_rms_ms=round(rms_res, 2), halves=out_half, second_signal=dict(P=round(1 / f[i2], 3), power=round(float(p2[i2]), 3), fap=float(ls2.false_alarm_probability(p2[i2], method="baluev", minimum_frequency=fmin, maximum_frequency=fmax))),
           aliases_1d=[round(1 / (1 / a.P + s), 3) for s in (1, -1) if (1 / a.P + s) > 0], aliases_1yr=[round(1 / (1 / a.P + s / 365.25), 3) for s in (1, -1) if (1 / a.P + s / 365.25) > 0], indicators=ind)
json.dump(res, open(os.path.join(a.outdir, "rv_vet.json"), "w"), indent=1, default=float)
fig, ax = plt.subplots(2, 2, figsize=(14, 8))
ax[0, 0].errorbar(tB - 2450000, yR, eB, fmt=".", ms=3); ax[0, 0].set_xlabel("BJD - 2450000"); ax[0, 0].set_ylabel("RV [m/s] (offsets+trend removed)"); ax[0, 0].set_title(f"{a.name}: {len(tB)} nights, rms {np.std(yR):.1f} m/s")
ax[0, 1].plot(1 / f, p, lw=0.6); ax[0, 1].set_xscale("log"); ax[0, 1].axvline(a.P, color="r", alpha=0.5); ax[0, 1].axhline(np.percentile(mx, 99), color="k", ls=":", lw=0.8); ax[0, 1].set_xlabel("period [d]"); ax[0, 1].set_title(f"GLS: best P={Pbest:.3f} d, FAP(Baluev)={fapb:.1e}, bootstrap FAP={boot_fap:.3f} (dotted: 99% of {a.nboot} shuffles)")
phs = (tB / a.P) % 1.0; o = np.argsort(phs); xx = np.linspace(0, 1, 200); Xs = np.column_stack([np.ones_like(tB), np.cos(2 * np.pi * tB / a.P), np.sin(2 * np.pi * tB / a.P)]); cs = np.linalg.lstsq(Xs * W[:, None], yR * W, rcond=None)[0]
ax[1, 0].errorbar(phs, yR, eB, fmt=".", ms=3, alpha=0.6); ax[1, 0].plot(xx, cs[0] + cs[1] * np.cos(2 * np.pi * xx) + cs[2] * np.sin(2 * np.pi * xx), "r-"); ax[1, 0].set_xlabel(f"phase (P={a.P} d)"); ax[1, 0].set_title(f"K = {K:.2f} m/s, residual rms {rms_res:.2f} m/s")
for c, v in ind.items(): ax[1, 1].bar(c, v["power_at_P"], color="C0"); 
ax[1, 1].set_ylabel("indicator GLS power at P"); ax[1, 1].set_title("activity indicators at the RV period (corr with RV in JSON)"); ax[1, 1].tick_params(axis="x", rotation=30)
plt.tight_layout(); plt.savefig(os.path.join(a.outdir, "rv_vet.png"), dpi=110)
print(json.dumps({k: v for k, v in res.items() if k != "indicators"}, default=float)); print("indicators:", {k: (v["corr_with_rv"], v["best_P"], v["power_at_P"]) for k, v in ind.items()})
