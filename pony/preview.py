#!/usr/bin/env python3
"""Render quick shaded previews of an STL so the shape can be eyeballed.

    python3 preview.py sitting_pony.stl preview.png
"""

import sys

import numpy as np
from PIL import Image, ImageDraw

VIEWS = [("front", 0), ("three-quarter", 35), ("side", 90), ("back", 180)]
if __import__("os").environ.get("PREVIEW_VIEWS"):
    VIEWS = [(n, y) for n, y in VIEWS
             if n in __import__("os").environ["PREVIEW_VIEWS"].split(",")]
SIZE = int(__import__("os").environ.get("PREVIEW_SIZE", 420))
LIGHT = np.array([-0.45, 0.62, 0.62])
LIGHT = LIGHT / np.linalg.norm(LIGHT)


def read_stl(path):
    with open(path, "rb") as fh:
        fh.read(80)
        n = int(np.frombuffer(fh.read(4), "<u4")[0])
        rec = np.frombuffer(fh.read(n * 50), dtype=np.dtype([
            ("n", "<f4", 3), ("v", "<f4", (3, 3)), ("attr", "<u2")]))
    return rec["v"].astype(np.float64)


def render(tris, yaw_deg, tilt_deg=-12.0):
    a = np.radians(yaw_deg)
    ry = np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0],
                   [0, 0, 1.0]])
    b = np.radians(tilt_deg)
    rx = np.array([[1, 0, 0], [0, np.cos(b), -np.sin(b)],
                   [0, np.sin(b), np.cos(b)]])
    p = tris.reshape(-1, 3) @ ry.T @ rx.T
    p = p.reshape(-1, 3, 3)

    normals = np.cross(p[:, 1] - p[:, 0], p[:, 2] - p[:, 0])
    ln = np.linalg.norm(normals, axis=1, keepdims=True)
    normals /= np.where(ln == 0, 1, ln)
    shade = np.clip(normals @ LIGHT, 0, 1) * 0.75 + 0.25

    lo, hi = p.reshape(-1, 3).min(axis=0), p.reshape(-1, 3).max(axis=0)
    scale = (SIZE * 0.86) / max(hi[0] - lo[0], hi[2] - lo[2])
    cx, cz = (lo[0] + hi[0]) / 2, (lo[2] + hi[2]) / 2
    sx = (p[:, :, 0] - cx) * scale + SIZE / 2
    sy = SIZE / 2 - (p[:, :, 2] - cz) * scale

    img = Image.new("RGB", (SIZE, SIZE), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    for i in np.argsort(p[:, :, 1].mean(axis=1)):     # painter's algorithm
        c = int(215 * shade[i]) + 40
        draw.polygon(list(zip(sx[i], sy[i])), fill=(c, int(c * 0.93),
                                                    int(c * 0.80)))
    return img


def main():
    tris = read_stl(sys.argv[1])
    out = sys.argv[2] if len(sys.argv) > 2 else "preview.png"
    sheet = Image.new("RGB", (SIZE * len(VIEWS), SIZE), (245, 245, 245))
    for i, (_, yaw) in enumerate(VIEWS):
        sheet.paste(render(tris, yaw), (i * SIZE, 0))
    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
