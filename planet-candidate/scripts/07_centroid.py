#!/usr/bin/env python3
"""Pixel-level test: difference image (out-of-transit minus in-transit) from the SPOC target pixel file.

Usage: 07_centroid.py DATA_DIR TIC SECTOR P T0 DUR_H OUTDIR
Outputs: difference-image figure, per-pixel depth map, centroid offset (pixels, arcsec) in centroid.json
"""
import os, sys, json, warnings
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tsearch2 as ts
warnings.filterwarnings("ignore")
DATA, tic, sector, P, t0, dur_h, outdir = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), sys.argv[7]
os.makedirs(outdir, exist_ok=True); dur = dur_h / 24
fmap = ts.build_filemap(DATA)
lcname = [f for s, f in fmap[tic] if s == sector][0]; tpname = lcname.replace("_lc.fits", "_tp.fits")
cache = os.path.join(DATA, "tpf_cache"); os.makedirs(cache, exist_ok=True)
path = ts.download(tpname, cache)
with fits.open(path, memmap=False) as h:
    d = h[1].data; t = d["TIME"].astype(float); flux = d["FLUX"].astype(float); q = d["QUALITY"]; ap = h[2].data
    hdr1 = h[1].header; hdr0 = h[0].header; wcs = WCS(h[2].header)
    ra_obj, dec_obj = hdr0.get("RA_OBJ"), hdr0.get("DEC_OBJ")
good = np.isfinite(t) & ((q & ts.DEFAULT_BITMASK) == 0) & np.isfinite(flux).all(axis=(1, 2))
t, flux = t[good], flux[good]
ph = ((t - t0 + 0.5 * P) % P) - 0.5 * P
intr = np.abs(ph) < 0.5 * dur
oot = (np.abs(ph) > 0.75 * dur) & (np.abs(ph) < 2.0 * dur)
n = np.round((t - t0) / P)
epochs = np.unique(n[intr])
# build per-transit difference images using local out-of-transit windows (removes slow trends)
diffs, weights = [], []
for k in epochs:
    mi = intr & (n == k); mo = oot & (n == k)
    if mi.sum() < 5 or mo.sum() < 10: continue
    diffs.append(np.nanmean(flux[mo], axis=0) - np.nanmean(flux[mi], axis=0)); weights.append(mi.sum())
if not diffs:
    raise SystemExit("no usable transits in this sector")
diff = np.average(np.array(diffs), axis=0, weights=np.array(weights))
direct = np.nanmean(flux[oot], axis=0)
# noise estimate for the diff image: scatter of per-epoch diffs / sqrt(N) (or from random-phase 'fake' transits)
rng = np.random.default_rng(1)
fakes = []
for i in range(40):
    off = rng.uniform(0.15, 0.85) * P
    phf = ((t - (t0 + off) + 0.5 * P) % P) - 0.5 * P; fi = np.abs(phf) < 0.5 * dur; fo = (np.abs(phf) > 0.75 * dur) & (np.abs(phf) < 2.0 * dur)
    nf = np.round((t - (t0 + off)) / P); dd, ww = [], []
    for k in np.unique(nf[fi]):
        mi = fi & (nf == k); mo = fo & (nf == k)
        if mi.sum() < 5 or mo.sum() < 10: continue
        dd.append(np.nanmean(flux[mo], axis=0) - np.nanmean(flux[mi], axis=0)); ww.append(mi.sum())
    if dd: fakes.append(np.average(np.array(dd), axis=0, weights=np.array(ww)))
noise = np.nanstd(np.array(fakes), axis=0) if fakes else np.full_like(diff, np.nan)
snr_img = diff / noise
# centroids
yy, xx = np.mgrid[0:diff.shape[0], 0:diff.shape[1]]
inap = (ap & 2) > 0
def centroid(img, mask):
    w = np.where(mask & np.isfinite(img) & (img > 0), img, 0.0)
    return (np.sum(w * xx) / np.sum(w), np.sum(w * yy) / np.sum(w)) if np.sum(w) > 0 else (np.nan, np.nan)
cx_d, cy_d = centroid(direct, inap); cx_f, cy_f = centroid(diff, inap)
# wider window for diff centroid (all pixels with snr>3)
cx_f2, cy_f2 = centroid(diff, snr_img > 3) if np.isfinite(snr_img).any() else (np.nan, np.nan)
# target pixel position from WCS
try:
    px, py = wcs.all_world2pix(ra_obj, dec_obj, 0); px, py = float(px), float(py)
except Exception:
    px, py = np.nan, np.nan
# per-pixel transit depth (fractional) for pixels in aperture
depth_map = np.full(diff.shape, np.nan)
for (j, i) in zip(*np.where(inap | (direct > 0.2 * np.nanmax(direct)))):
    pix = flux[:, j, i]
    if np.nanmean(pix[oot]) > 0:
        depth_map[j, i] = 1e6 * (np.nanmean(pix[oot]) - np.nanmean(pix[intr])) / np.nanmean(pix[oot])
res = dict(tic=tic, sector=sector, n_transits_used=len(diffs), target_pix=[px, py], direct_centroid=[cx_d, cy_d], diff_centroid_in_aperture=[cx_f, cy_f],
           diff_centroid_snr3=[cx_f2, cy_f2], offset_pix=float(np.hypot(cx_f - cx_d, cy_f - cy_d)), offset_arcsec=float(21 * np.hypot(cx_f - cx_d, cy_f - cy_d)),
           offset_from_target_pix=float(np.hypot(cx_f - px, cy_f - py)) if np.isfinite(px) else None,
           max_diff_snr=float(np.nanmax(snr_img)), diff_peak_pix=[int(v) for v in np.unravel_index(np.nanargmax(np.where(np.isfinite(snr_img), snr_img, -np.inf)), snr_img.shape)][::-1],
           direct_peak_pix=[int(v) for v in np.unravel_index(np.nanargmax(direct), direct.shape)][::-1],
           total_depth_in_aperture_ppm=float(1e6 * np.nansum(diff[inap]) / np.nansum(direct[inap])))
json.dump(res, open(os.path.join(outdir, f"centroid_s{sector}.json"), "w"), indent=1)
fig, axes = plt.subplots(1, 4, figsize=(18, 4.5))
for ax, img, title in [(axes[0], direct, "direct (out-of-transit) image"), (axes[1], diff, "difference image (out - in)"), (axes[2], snr_img, "difference SNR"), (axes[3], depth_map, "per-pixel depth (ppm)")]:
    im = ax.imshow(img, origin="lower", cmap="viridis"); plt.colorbar(im, ax=ax, fraction=0.046)
    ax.contour(inap.astype(float), levels=[0.5], colors="w", linewidths=1)
    if np.isfinite(px): ax.plot(px, py, "r+", ms=14, mew=2)
    ax.plot(cx_d, cy_d, "wx", ms=10, mew=2); ax.plot(cx_f, cy_f, "mo", ms=8, mfc="none", mew=2)
    ax.set_title(title, fontsize=10)
fig.suptitle(f"TIC {tic} S{sector}  P={P:.4f}  n_tr={len(diffs)}  red + = target (WCS), white x = direct centroid, magenta o = difference centroid; offset={res['offset_arcsec']:.1f}\"")
plt.tight_layout(); plt.savefig(os.path.join(outdir, f"centroid_s{sector}.png"), dpi=110)
print(json.dumps(res, indent=1))
