"""Small signed-distance-field toolkit used to build the pony model.

Every primitive takes an (N, 3) array of points and returns an (N,) array of
signed distances (negative inside).  Distances are exact for spheres, capsules
and round cones; the ellipsoid uses the usual bounded approximation, which is
accurate enough for surface extraction.
"""

import numpy as np

FLOAT = np.float32


# --------------------------------------------------------------------------
# combination operators
# --------------------------------------------------------------------------
def smin(a, b, k):
    """Polynomial smooth minimum (smooth union)."""
    if k <= 0.0:
        return np.minimum(a, b)
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return b + (a - b) * h - k * h * (1.0 - h)


def smax(a, b, k):
    """Polynomial smooth maximum (smooth intersection)."""
    return -smin(-a, -b, k)


def union(a, b, k=0.0):
    return smin(a, b, k)


def subtract(a, b, k=0.0):
    """Remove solid ``b`` from solid ``a``."""
    return smax(a, -b, k)


def intersect(a, b, k=0.0):
    return smax(a, b, k)


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------
def sphere(p, c, r):
    d = p - np.asarray(c, FLOAT)
    return np.sqrt(np.einsum("ij,ij->i", d, d)) - r


def ellipsoid(p, c, radii):
    r = np.asarray(radii, FLOAT)
    q = (p - np.asarray(c, FLOAT)) / r
    k0 = np.sqrt(np.einsum("ij,ij->i", q, q))
    q2 = q / r
    k1 = np.sqrt(np.einsum("ij,ij->i", q2, q2))
    return k0 * (k0 - 1.0) / np.maximum(k1, 1e-9)


def round_cone(p, a, b, r1, r2):
    """Cone with spherical caps of radius r1 at a and r2 at b (iq's formula)."""
    a = np.asarray(a, FLOAT)
    b = np.asarray(b, FLOAT)
    ba = b - a
    l2 = float(ba @ ba)
    rr = float(r1 - r2)
    a2 = l2 - rr * rr
    il2 = 1.0 / l2

    pa = p - a
    y = pa @ ba
    z = y - l2
    x_ = pa * l2 - ba[None, :] * y[:, None]
    x2 = np.einsum("ij,ij->i", x_, x_)
    y2 = y * y * l2
    z2 = z * z * l2

    k = np.sign(rr) * rr * rr * x2
    cap_b = np.sqrt(np.maximum(x2 + z2, 0.0)) * il2 - r2
    cap_a = np.sqrt(np.maximum(x2 + y2, 0.0)) * il2 - r1
    side = (np.sqrt(np.maximum(x2 * a2 * il2, 0.0)) + y * rr) * il2 - r1

    d = np.where(np.sign(y) * a2 * y2 < k, cap_a, side)
    d = np.where(np.sign(z) * a2 * z2 > k, cap_b, d)
    return d


def capsule(p, a, b, r):
    return round_cone(p, a, b, r, r)


def plane_above(p, z0):
    """Solid half space z >= z0."""
    return z0 - p[:, 2]


# --------------------------------------------------------------------------
# helpers for placing detail on a surface
# --------------------------------------------------------------------------
def ellipsoid_point(c, radii, direction, scale=1.0):
    """Point on (or near) an ellipsoid along a unit-sphere direction."""
    d = np.asarray(direction, FLOAT)
    d = d / np.linalg.norm(d)
    return np.asarray(c, FLOAT) + np.asarray(radii, FLOAT) * d * scale


def ellipsoid_front(c, radii, x, z, offset=0.0):
    """Project (x, z) onto the +y face of an ellipsoid, pushed out by offset."""
    c = np.asarray(c, FLOAT)
    r = np.asarray(radii, FLOAT)
    u = (x - c[0]) / r[0]
    w = (z - c[2]) / r[2]
    v = np.sqrt(max(0.0, 1.0 - u * u - w * w))
    pt = np.array([x, c[1] + r[1] * v, z], FLOAT)
    n = np.array([u / r[0], v / r[1], w / r[2]], FLOAT)
    n /= np.linalg.norm(n)
    return pt + n * offset
