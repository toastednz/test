"""Scan corridors [Y, Y+h] (all rows composite) with small constraint period L;
BFS for a period-crossing path. First success = certificate for #1212."""
from math import gcd
from collections import deque
import json, sys

def is_comp(n):
    if n < 4: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return True
        d += 1
    return False

def radp(n):
    ps = set(); d = 2
    while d * d <= n:
        if n % d == 0:
            ps.add(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: ps.add(n)
    return ps

def try_corridor(Y, h, Lcap=1_500_000, verbose=False):
    rows = list(range(Y, Y + h + 1))
    if not all(is_comp(r) for r in rows):
        return None
    allp = set()
    for r in rows: allp |= radp(r)
    L = 1
    for p in sorted(allp):
        L *= p
        if L > Lcap: return None
    x0 = None
    for c in range(3, 500):
        if gcd(c, rows[0]) == 1:
            x0 = c; break
    XMAX = x0 + L + 2
    start = (x0, 0); target = (x0 + L, 0)
    prev = {start: None}
    dq = deque([start])
    found = False
    R = len(rows)
    while dq:
        v = dq.popleft()
        if v == target:
            found = True; break
        x, ri = v
        cands = []
        if ri + 1 < R: cands.append((x, ri + 1))
        if ri > 0: cands.append((x, ri - 1))
        cands.append((x + 1, ri)); cands.append((x - 1, ri))
        for w in cands:
            if w in prev: continue
            nx, nri = w
            if nx < 2 or nx > XMAX: continue
            if gcd(nx, rows[nri]) != 1: continue
            prev[w] = v; dq.append(w)
    if not found:
        if verbose:
            mx = max(x for (x, ri) in prev)
            print(f"  Y={Y} h={h} L={L}: blocked, max x reached {mx} (of {x0+L})")
        return None
    # extract and validate
    path = []; v = target
    while v is not None:
        path.append(v); v = prev[v]
    path.reverse()
    seg = [(x, rows[ri]) for (x, ri) in path]
    seen = set()
    for i, (x, y) in enumerate(seg):
        assert (x, y) not in seen; seen.add((x, y))
        assert gcd(x, y) == 1 and (is_comp(x) or is_comp(y)) and x >= 2 and y >= 2
        if i:
            px, py = seg[i - 1]
            assert abs(px - x) + abs(py - y) == 1
    return {"Y": Y, "h": h, "rows": rows, "L": L, "x0": x0, "segment": seg}

if __name__ == "__main__":
    # consecutive-composite runs with small radicals: prefer rows sharing primes
    tried = 0
    for Y in range(25, 20000, 2):
        for h in (2, 3, 4, 5):
            res = try_corridor(Y, h)
            tried += 1
            if res:
                print(f"SUCCESS: Y={res['Y']} h={res['h']} L={res['L']} seglen={len(res['segment'])}")
                json.dump(res, open(f"path1212_cert_Y{res['Y']}_h{res['h']}.json", "w"))
                sys.exit(0)
    print("no corridor found in range")
