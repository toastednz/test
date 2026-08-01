#!/usr/bin/env python3
"""Generate a 3D-printable STL of the sitting cartoon pony.

The shape is defined as a signed distance field built from smooth-blended
primitives, sampled on a regular grid and polygonised with marching cubes.
That guarantees a single watertight manifold shell, which is what a slicer
wants.

    python3 generate_pony.py                 # 0.5 mm voxels -> sitting_pony.stl
    python3 generate_pony.py --voxel 1.5     # quick draft
    python3 generate_pony.py --height 150    # scale the finished model

Dimensions below are in millimetres, with +y pointing forward (towards the
muzzle) and +z up.  The figure is 100 mm tall by default and sits flat on z=0.
"""

import argparse
import math
import time

import numpy as np
from skimage import measure

import sdf as S

FLOAT = np.float32

# --------------------------------------------------------------------------
# proportions (mm)
# --------------------------------------------------------------------------
BODY_C, BODY_R = (0.0, -4.0, 19.0), (26.0, 24.0, 26.0)
HEAD_C, HEAD_R = (0.0, 2.0, 66.0), 22.5
MUZZLE_C, MUZZLE_R = (0.0, 21.0, 48.0), (17.5, 19.0, 17.0)

EYE_DIR = (0.50, 0.85, 0.22)      # direction from the head centre
EYE_DIST, EYE_R = 20.5, 5.0

EAR_BASE, EAR_TIP = (11.0, -1.0, 78.0), (19.5, -4.0, 98.0)
EAR_R1, EAR_R2 = 8.0, 3.0

# mane tufts: (x, tip y, tip z, base radius)
MANE = [(-8.5, 14.0, 88.0, 4.6), (-3.0, 16.5, 90.5, 5.2),
        (3.0, 16.5, 90.5, 5.2), (8.5, 14.0, 88.0, 4.6)]

HAUNCH_A, HAUNCH_B = (20.0, -12.0, 14.0), (21.0, 10.0, 11.0)
HAUNCH_R1, HAUNCH_R2 = 12.0, 11.5
PAW_A, PAW_B = (14.0, 5.0, 7.5), (14.5, 20.0, 7.0)
PAW_R1, PAW_R2 = 8.0, 7.2

TAIL_A, TAIL_B = (0.0, -22.0, 24.0), (0.0, -27.0, 10.0)
TAIL_R1, TAIL_R2 = 6.0, 5.0

TEXT = "STL"
TEXT_CENTRE_Z = 10.0
TEXT_SIZE = (2.6, 5.0)            # letter width, height
TEXT_PITCH = 3.8
TEXT_STROKE = 0.6
TEXT_RELIEF = 0.6                # how far the stroke axis sits proud

# blocky strokes in a 0..1 x 0..1 letter box
GLYPHS = {
    "S": [((0, 1), (1, 1)), ((0, 1), (0, 0.55)), ((0, 0.55), (1, 0.55)),
          ((1, 0.55), (1, 0)), ((0, 0), (1, 0))],
    "T": [((0, 1), (1, 1)), ((0.5, 1), (0.5, 0))],
    "L": [((0, 1), (0, 0)), ((0, 0), (1, 0))],
}

BOUNDS_MIN = (-38.0, -40.0, -2.0)
BOUNDS_MAX = (38.0, 46.0, 104.0)


def _mirrored(pt, sign):
    return (sign * pt[0], pt[1], pt[2])


def _smile_points(n=15):
    """Arc of unit directions that dips in the middle and lifts at the ends."""
    pts = []
    for i in range(n):
        t = -1.0 + 2.0 * i / (n - 1)
        d = np.array([math.sin(0.78 * t), 0.72, -0.60 + 0.33 * t * t], FLOAT)
        pts.append(S.ellipsoid_point(MUZZLE_C, MUZZLE_R, d, 0.985))
    return pts


def _text_strokes():
    """World-space capsule endpoints for the embossed STL badge."""
    w, h = TEXT_SIZE
    strokes = []
    x0 = -TEXT_PITCH * (len(TEXT) - 1) / 2.0
    for i, ch in enumerate(TEXT):
        cx = x0 + i * TEXT_PITCH
        for (u0, v0), (u1, v1) in GLYPHS[ch]:
            a = S.ellipsoid_front(BODY_C, BODY_R, cx + (u0 - 0.5) * w,
                                  TEXT_CENTRE_Z + (v0 - 0.5) * h, TEXT_RELIEF)
            b = S.ellipsoid_front(BODY_C, BODY_R, cx + (u1 - 0.5) * w,
                                  TEXT_CENTRE_Z + (v1 - 0.5) * h, TEXT_RELIEF)
            strokes.append((a, b))
    return strokes


SMILE = _smile_points()
STROKES = _text_strokes()


def model(p):
    """Signed distance to the pony at points p, shape (N, 3)."""
    # ---- body, haunches, paws, tail ------------------------------------
    d = S.ellipsoid(p, BODY_C, BODY_R)
    for s in (1, -1):
        d = S.union(d, S.round_cone(p, _mirrored(HAUNCH_A, s),
                                    _mirrored(HAUNCH_B, s),
                                    HAUNCH_R1, HAUNCH_R2), 6.0)
        d = S.union(d, S.round_cone(p, _mirrored(PAW_A, s),
                                    _mirrored(PAW_B, s),
                                    PAW_R1, PAW_R2), 3.5)
    d = S.union(d, S.round_cone(p, TAIL_A, TAIL_B, TAIL_R1, TAIL_R2), 6.0)

    # ---- head and muzzle ------------------------------------------------
    head = S.sphere(p, HEAD_C, HEAD_R)
    d = S.union(d, head, 7.0)
    d = S.union(d, S.ellipsoid(p, MUZZLE_C, MUZZLE_R), 4.0)

    # ---- ears (with a scooped inner face) -------------------------------
    for s in (1, -1):
        ear = S.round_cone(p, _mirrored(EAR_BASE, s), _mirrored(EAR_TIP, s),
                           EAR_R1, EAR_R2)
        ear = S.subtract(ear, S.ellipsoid(p, (s * 15.0, 1.5, 89.0),
                                          (2.8, 3.2, 7.0)), 1.0)
        d = S.union(d, ear, 2.5)

    # ---- mane tufts -----------------------------------------------------
    for x, ty, tz, r in MANE:
        d = S.union(d, S.round_cone(p, (x, 2.0, 79.0), (x * 1.15, ty, tz),
                                    r, r * 0.60), 2.5)

    # ---- eyes -----------------------------------------------------------
    for s in (1, -1):
        c = np.asarray(HEAD_C, FLOAT) + np.asarray(
            (s * EYE_DIR[0], EYE_DIR[1], EYE_DIR[2]), FLOAT) / np.linalg.norm(
            EYE_DIR) * EYE_DIST
        d = S.union(d, S.sphere(p, c, EYE_R), 1.4)

    # ---- embossed badge -------------------------------------------------
    for a, b in STROKES:
        d = S.union(d, S.capsule(p, a, b, TEXT_STROKE), 0.4)

    # ---- carved detail --------------------------------------------------
    for s in (1, -1):                                   # nostrils
        c = S.ellipsoid_point(MUZZLE_C, MUZZLE_R,
                              (s * 0.30, 0.74, 0.60), 0.96)
        d = S.subtract(d, S.ellipsoid(p, c, (1.8, 2.4, 2.6)), 1.0)

    for i in range(len(SMILE) - 1):                     # smile groove
        d = S.subtract(d, S.capsule(p, SMILE[i], SMILE[i + 1], 1.15), 0.6)

    for s in (1, -1):                                   # toe line on each paw
        # both ends sit on the paw's spherical cap, so the groove stays a
        # shallow surface cut instead of plunging through the shell
        cap = (s * PAW_B[0], PAW_B[1], PAW_B[2])
        a = S.ellipsoid_point(cap, (PAW_R2,) * 3, (0.0, 0.25, 0.97))
        b = S.ellipsoid_point(cap, (PAW_R2,) * 3, (0.0, 0.78, 0.63))
        d = S.subtract(d, S.capsule(p, a, b, 0.7), 0.5)

    # ---- flat base ------------------------------------------------------
    return S.intersect(d, S.plane_above(p, 0.0))


def sample(voxel):
    # nudge the lattice off round numbers so the isosurface never passes
    # exactly through a sample point (that yields zero-area triangles)
    lo = np.asarray(BOUNDS_MIN, FLOAT) - FLOAT(0.137) * voxel
    hi = np.asarray(BOUNDS_MAX, FLOAT)
    dims = np.maximum(np.ceil((hi - lo) / voxel).astype(int) + 1, 2)
    xs = lo[0] + np.arange(dims[0], dtype=FLOAT) * voxel
    ys = lo[1] + np.arange(dims[1], dtype=FLOAT) * voxel
    zs = lo[2] + np.arange(dims[2], dtype=FLOAT) * voxel

    vol = np.empty(tuple(dims), FLOAT)
    gx, gy = np.meshgrid(xs, ys, indexing="ij")
    flat = np.empty((dims[0] * dims[1], 3), FLOAT)
    flat[:, 0] = gx.ravel()
    flat[:, 1] = gy.ravel()
    for k, z in enumerate(zs):
        flat[:, 2] = z
        vol[:, :, k] = model(flat).reshape(dims[0], dims[1])

    # push samples off zero so no crossing lands on a lattice point; this
    # keeps marching-cubes vertices well separated (shifts the surface by at
    # most eps, i.e. a hundredth of a voxel)
    eps = FLOAT(0.01) * voxel
    np.copyto(vol, np.where(vol < 0, -eps, eps), where=np.abs(vol) < eps)
    return vol, lo, voxel


def mesh(voxel):
    vol, lo, step = sample(voxel)
    # keep the isosurface away from the grid edges so the shell stays closed
    vol = np.pad(vol, 1, mode="constant", constant_values=step)
    verts, faces, _, _ = measure.marching_cubes(vol, level=0.0,
                                                spacing=(step, step, step))
    verts += lo - step
    for _ in range(4):                       # weld/drop until nothing changes
        n = len(faces)
        verts, faces = clean(verts, faces)
        if len(faces) == n:
            break
    return verts, faces


def clean(verts, faces, tol=1e-4):
    """Weld coincident vertices and drop the resulting zero-area triangles.

    Marching cubes emits a separate vertex per grid edge, so a surface that
    grazes a lattice point produces several vertices at the same coordinate.
    Welding them turns those triangles degenerate; dropping a degenerate
    triangle removes a self-edge plus a cancelling pair, so the shell stays
    watertight.
    """
    quant = np.round(verts / tol).astype(np.int64)
    _, first, inverse = np.unique(quant, axis=0, return_index=True,
                                  return_inverse=True)
    faces = inverse.reshape(-1)[faces]
    keep = ((faces[:, 0] != faces[:, 1]) & (faces[:, 1] != faces[:, 2]) &
            (faces[:, 0] != faces[:, 2]))
    faces = faces[keep]

    verts = verts[first]
    used, faces = np.unique(faces.reshape(-1), return_inverse=True)
    return verts[used], faces.reshape(-1, 3)


def signed_volume(verts, faces):
    a, b, c = verts[faces[:, 0]], verts[faces[:, 1]], verts[faces[:, 2]]
    return float(np.einsum("ij,ij->i", a, np.cross(b, c)).sum() / 6.0)


def write_stl(path, verts, faces, name="pony"):
    tris = verts[faces].astype("<f4")
    n = np.cross(tris[:, 1] - tris[:, 0], tris[:, 2] - tris[:, 0])
    ln = np.linalg.norm(n, axis=1, keepdims=True)
    n = (n / np.where(ln == 0, 1.0, ln)).astype("<f4")

    rec = np.zeros(len(faces), dtype=np.dtype([("n", "<f4", 3),
                                               ("v", "<f4", (3, 3)),
                                               ("attr", "<u2")]))
    rec["n"] = n
    rec["v"] = tris
    with open(path, "wb") as fh:
        fh.write(name.encode()[:80].ljust(80, b" "))
        fh.write(np.uint32(len(faces)).tobytes())
        fh.write(rec.tobytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voxel", type=float, default=0.5,
                    help="grid resolution in mm (default 0.5)")
    ap.add_argument("--height", type=float, default=None,
                    help="uniformly scale so the model is this tall in mm")
    ap.add_argument("-o", "--output", default="sitting_pony.stl")
    args = ap.parse_args()

    t0 = time.time()
    verts, faces = mesh(args.voxel)

    if signed_volume(verts, faces) < 0:          # make normals point outward
        faces = faces[:, ::-1]

    if args.height:
        verts *= args.height / (verts[:, 2].max() - verts[:, 2].min())
    verts[:, 2] -= verts[:, 2].min()             # rest exactly on the bed

    write_stl(args.output, verts, faces)
    size = verts.max(axis=0) - verts.min(axis=0)
    print(f"{args.output}: {len(faces)} triangles, "
          f"{size[0]:.1f} x {size[1]:.1f} x {size[2]:.1f} mm, "
          f"volume {signed_volume(verts, faces) / 1000:.1f} cm3, "
          f"{time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
