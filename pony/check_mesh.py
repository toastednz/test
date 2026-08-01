#!/usr/bin/env python3
"""Sanity-check an STL before printing: closed, manifold, outward normals.

    python3 check_mesh.py sitting_pony.stl
"""

import sys
from collections import Counter

import numpy as np


def read_stl(path):
    with open(path, "rb") as fh:
        fh.read(80)
        n = int(np.frombuffer(fh.read(4), "<u4")[0])
        rec = np.frombuffer(fh.read(n * 50), dtype=np.dtype([
            ("n", "<f4", 3), ("v", "<f4", (3, 3)), ("attr", "<u2")]))
    return rec["v"].astype(np.float64)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "sitting_pony.stl"
    tris = read_stl(path)

    # weld vertices so shared edges can be matched
    keys = np.round(tris.reshape(-1, 3), 3)   # weld within a micron
    uniq, idx = np.unique(keys, axis=0, return_inverse=True)
    faces = idx.reshape(-1, 3)

    ok = True
    degenerate = int(((faces[:, 0] == faces[:, 1]) |
                      (faces[:, 1] == faces[:, 2]) |
                      (faces[:, 0] == faces[:, 2])).sum())

    edges = Counter()
    for a, b, c in faces:
        for u, v in ((a, b), (b, c), (c, a)):
            edges[(u, v) if u < v else (v, u)] += 1
    counts = Counter(edges.values())
    boundary = counts.get(1, 0)
    nonmanifold = sum(n for c, n in counts.items() if c > 2)

    a, b, c = tris[:, 0], tris[:, 1], tris[:, 2]
    volume = float(np.einsum("ij,ij->i", a, np.cross(b, c)).sum() / 6.0)
    area = float(np.linalg.norm(np.cross(b - a, c - a), axis=1).sum() / 2.0)
    lo, hi = tris.reshape(-1, 3).min(axis=0), tris.reshape(-1, 3).max(axis=0)

    print(f"file            {path}")
    print(f"triangles       {len(faces)}")
    print(f"vertices        {len(uniq)}")
    print(f"bounding box    {hi[0]-lo[0]:.2f} x {hi[1]-lo[1]:.2f} x "
          f"{hi[2]-lo[2]:.2f} mm")
    print(f"sits on bed     z min = {lo[2]:.3f} mm")
    print(f"volume          {volume/1000:.2f} cm3")
    print(f"surface area    {area/100:.2f} cm2")
    print(f"euler x         {len(uniq) - len(edges) + len(faces)}")
    print(f"degenerate      {degenerate}")
    print(f"boundary edges  {boundary}   (0 = watertight)")
    print(f"non-manifold    {nonmanifold}   (0 = good)")

    for label, bad in (("boundary edges", boundary),
                       ("non-manifold edges", nonmanifold),
                       ("degenerate triangles", degenerate)):
        if bad:
            print(f"FAIL: {bad} {label}")
            ok = False
    if volume <= 0:
        print("FAIL: normals point inward")
        ok = False
    print("OK" if ok else "PROBLEMS FOUND")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
