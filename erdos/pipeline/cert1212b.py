"""#1212 certificate search v2: digraph on nodes (d, x mod M), M even,
strip = contiguous [1, dmax] with all primes <= dmax dividing M.
Vertex (d, x) admissible iff:
  - for all p | d: x % p != 0                     [gcd(x,d)=1, since rad(d)|M]
  - if d even: exists p | M with x%p==0 or (x+d)%p==0    [cond 4]
Edges: N: (d,x)->(d+1,x)  E: (d,x)->(d-1,(x+1)%M)
Any directed cycle -> periodic monotone admissible ray (Lemma 7, verified).
"""
import sys
from math import gcd

def primes_of(n):
    ps = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: ps.append(n)
    return ps

def run(M, dmax):
    Mp = primes_of(M)
    dprimes = {d: primes_of(d) for d in range(1, dmax + 1)}
    # ensure strip contiguity
    for d in range(1, dmax + 1):
        assert all(p in Mp for p in dprimes[d]), (d, Mp)

    N = dmax * M
    def nid(d, x):
        return (d - 1) * M + x

    adm = bytearray(N)
    for x in range(M):
        for d in range(1, dmax + 1):
            if any(x % p == 0 for p in dprimes[d]):
                continue
            if d % 2 == 0:
                ok = False
                for p in Mp:
                    if x % p == 0 or (x + d) % p == 0:
                        ok = True
                        break
                if not ok:
                    continue
            adm[nid(d, x)] = 1

    print(f"M={M} dmax={dmax}: admissible {sum(adm)}/{N}", flush=True)

    # iterative DFS cycle detection on admissible subgraph
    WHITE, GRAY, BLACK = 0, 1, 2
    color = bytearray(N)
    parent = {}
    def edges(v):
        d = v // M + 1
        x = v % M
        out = []
        if d + 1 <= dmax:
            w = nid(d + 1, x)
            if adm[w]: out.append(w)
        if d - 1 >= 1:
            w = nid(d - 1, (x + 1) % M)
            if adm[w]: out.append(w)
        return out

    sys.setrecursionlimit(10000)
    for s in range(N):
        if not adm[s] or color[s]:
            continue
        stack = [(s, 0)]
        color[s] = GRAY
        while stack:
            v, ei = stack[-1]
            es = edges(v)
            if ei < len(es):
                stack[-1] = (v, ei + 1)
                w = es[ei]
                if color[w] == WHITE:
                    color[w] = GRAY
                    parent[w] = v
                    stack.append((w, 0))
                elif color[w] == GRAY:
                    # cycle w ... v
                    cyc = [v]
                    u = v
                    while u != w:
                        u = parent[u]
                        cyc.append(u)
                    cyc.reverse()
                    return cyc
            else:
                color[v] = BLACK
                stack.pop()
    return None

if __name__ == "__main__":
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 30030
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    cyc = run(M, dmax)
    if cyc:
        print("CYCLE FOUND, length", len(cyc))
        import json
        out = [(v // M + 1, v % M) for v in cyc]
        json.dump({"M": M, "dmax": dmax, "cycle_d_x": out},
                  open(f"cert1212_cycle_M{M}.json", "w"))
        print("first 30 (d, x mod M):", out[:30])
    else:
        print("no cycle — strip/M insufficient")
