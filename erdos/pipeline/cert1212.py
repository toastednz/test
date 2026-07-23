"""#1212 finite certificate search via (verified) Lemma 7:
T even; monotone NE path with vertex conditions, periodic with period (T,T).
State: (d, e mod T) where d = y-x in allowed T-smooth strip, e = number of E
steps so far (x = a0 + e). Vertex admissible iff:
  - d in strip (d>=1, rad(d) | T)
  - for all p | d: p does not divide (a0+e)          [gcd(x,d)=1]
  - if d even: exists prime p | T dividing (a0+e) or (a0+e+d)   [cond 4]
Moves: N: (d,e) -> (d+1, e); E: (d,e) -> (d-1, e+1).
Any directed cycle in the admissible digraph = certificate (period kT).
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

def search(T, dmax):
    Tp = primes_of(T)
    strip = [d for d in range(1, dmax + 1) if all(p in Tp for p in primes_of(d))]
    stripset = set(strip)
    for a0 in range(T):
        # admissible states
        adm = {}
        for d in strip:
            for e in range(T):
                x = (a0 + e) % T
                # gcd(x, d) = 1 in terms of primes of d (all divide T so x mod T decides)
                if any((x % p) == 0 for p in primes_of(d)):
                    continue
                if d % 2 == 0:
                    y = (x + d) % T
                    if not any((x % p) == 0 or (y % p) == 0 for p in Tp):
                        continue
                adm[(d, e)] = []
        # edges
        for (d, e) in adm:
            if (d + 1, e) in adm:
                adm[(d, e)].append((d + 1, e))
            if (d - 1, (e + 1) % T) in adm:
                adm[(d, e)].append((d - 1, (e + 1) % T))
        # find a directed cycle (iterative DFS, colors)
        color = {s: 0 for s in adm}
        parent = {}
        for s0 in adm:
            if color[s0]: continue
            stack = [(s0, iter(adm[s0]))]
            color[s0] = 1
            while stack:
                v, it = stack[-1]
                adv = False
                for w in it:
                    if color[w] == 0:
                        color[w] = 1
                        parent[w] = v
                        stack.append((w, iter(adm[w])))
                        adv = True
                        break
                    elif color[w] == 1:
                        # cycle found: w .. v
                        cyc = [v]
                        u = v
                        while u != w:
                            u = parent[u]
                            cyc.append(u)
                        cyc.reverse()
                        return a0, cyc
                if not adv:
                    color[v] = 2
                    stack.pop()
    return None

for T in (30, 60, 90, 120, 210, 420, 630, 840, 1050, 1260, 2310):
    dmax = 12
    res = search(T, dmax)
    print(f"T={T}: {'CYCLE FOUND' if res else 'none'}", flush=True)
    if res:
        a0, cyc = res
        print("a0 =", a0, "cycle length:", len(cyc))
        print("cycle states (d, e mod T):", cyc[:40])
        import json
        json.dump({"T": T, "a0": a0, "cycle": cyc}, open("cert1212_cycle.json", "w"))
        break
