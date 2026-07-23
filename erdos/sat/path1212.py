"""Erdos #1212: construct an infinite path in the coprime graph, both coords >1,
never both prime. Scheme: corridor of rows Y..Y+2 all composite; coprimality
constraints periodic in x with period L = lcm(radical(Y(Y+1)(Y+2))).
Find a simple path from (x0, Y) to (x0+L, Y) inside the corridor -> periodic
extension gives an infinite path. Certificate = the segment.
"""
from math import gcd
from collections import deque
import json, sys

Y = int(sys.argv[1]) if len(sys.argv) > 1 else 119

rows = [Y, Y + 1, Y + 2]
def radical_primes(n):
    ps = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            ps.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ps.add(n)
    return ps

allp = set()
for r in rows:
    allp |= radical_primes(r)
L = 1
for p in allp:
    L *= p
print("rows:", rows, "primes:", sorted(allp), "period L =", L)

def composite(n):
    if n < 4: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return True
        d += 1
    return False

assert all(composite(r) for r in rows), "rows must be composite"

def okv(x, y):
    return x >= 2 and gcd(x, y) == 1

# BFS from (x0, Y) to (x0+L, Y), x in [x0, x0+L] inclusive corridor
x0 = None
# pick x0 coprime to row Y and to neighbors' needs, near 2L to keep x>=2 margin
for c in range(5, 5 + 200):
    if okv(c, Y):
        x0 = c
        break
XMAX = x0 + L
start = (x0, 0)  # row index 0 => Y
target = (x0 + L, 0)

def nbrs(v):
    x, ri = v
    y = rows[ri]
    out = []
    if ri + 1 < 3:
        out.append((x, ri + 1))
    if ri - 1 >= 0:
        out.append((x, ri - 1))
    out.append((x + 1, ri))
    out.append((x - 1, ri))
    res = []
    for (nx, nri) in out:
        if nx < 2 or nx > XMAX + 2:
            continue
        if okv(nx, rows[nri]):
            res.append((nx, nri))
    return res

if not okv(*[x0, Y][0:1] + [Y]) :
    pass
prev = {start: None}
dq = deque([start])
found = False
while dq:
    v = dq.popleft()
    if v == target:
        found = True
        break
    for w in nbrs(v):
        if w not in prev:
            prev[w] = v
            dq.append(w)

print("path found:", found)
if found:
    path = []
    v = target
    while v is not None:
        path.append(v)
        v = prev[v]
    path.reverse()
    seg = [(x, rows[ri]) for (x, ri) in path]
    print("segment length:", len(seg), "from", seg[0], "to", seg[-1])
    # validate: unit steps, coprime, composite condition, simplicity
    seen = set()
    okall = True
    for i, (x, y) in enumerate(seg):
        if (x, y) in seen: okall = False; print("REPEAT", x, y); break
        seen.add((x, y))
        if gcd(x, y) != 1: okall = False; print("GCD FAIL", x, y); break
        if not (composite(x) or composite(y)): okall = False; print("COMP FAIL", x, y); break
        if x < 2 or y < 2: okall = False; break
        if i > 0:
            px, py = seg[i-1]
            if abs(px - x) + abs(py - y) != 1: okall = False; print("STEP FAIL"); break
    print("segment valid:", okall)
    # check translate-compatibility: seg starts at (x0,Y) ends (x0+L,Y);
    # ensure interior x stay within (x0- L? ) we need translates disjoint:
    xs = [x for (x, y) in seg]
    print("x range:", min(xs), max(xs), " (need max-min <= ~2L and controlled)")
    json.dump({"rows": rows, "L": L, "segment": seg[:], "x0": x0},
              open(f"path1212_certificate_Y{Y}.json", "w"))
    print("certificate written")
