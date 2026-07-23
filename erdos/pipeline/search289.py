"""#289: find an exact representation 1 = sum of interval harmonic sums,
intervals length>=2, pairwise non-adjacent (gap >= 2 between intervals).
Denominator-directed DFS: kill largest prime power in the deficit's
denominator using intervals whose weight has matching valuation.
"""
from fractions import Fraction
from math import gcd
import sys, json
sys.setrecursionlimit(100000)

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
MAXLEN = int(sys.argv[2]) if len(sys.argv) > 2 else 8

# candidate starting blocks: [2, B]
def H(a, b):
    return sum(Fraction(1, n) for n in range(a, b + 1))

def prime_factors(n):
    fs = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs[d] = fs.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs

def largest_prime_power(q):
    fs = prime_factors(q)
    p = max(fs)
    return p, fs[p]

found = []

def try_start(B0):
    base = H(2, B0)
    if base >= 1:
        return None
    deficit = 1 - base
    intervals = [(2, B0)]
    minpos = B0 + 2

    def dfs(deficit, minpos, intervals, depth):
        if deficit == 0:
            return list(intervals)
        if depth == 0:
            return None
        q = deficit.denominator
        p, e = largest_prime_power(q)
        # choose an interval [a, b] with p^e | denominator structure to cancel:
        # simplest: intervals containing exactly one multiple of p^e, i.e.
        # a <= m*p^e <= b with tight windows. Try m*p^e near a with small length.
        cands = []
        # multiples of p^e >= minpos
        m0 = (minpos + p**e - 1) // p**e
        for m in range(m0, m0 + 60):
            c = m * p**e
            if gcd(m, p) == 0:
                pass
            if c < minpos or c > NMAX:
                continue
            for L in range(2, MAXLEN + 1):
                for a in range(max(minpos, c - L + 1), c + 1):
                    b = a + L - 1
                    if b > NMAX:
                        continue
                    if not (a <= c <= b):
                        continue
                    # exactly one multiple of p in [a,b] preferred
                    w = H(a, b)
                    if w <= deficit:
                        cands.append((w, a, b))
        # also plain greedy dimers if p-power small
        if p**e <= 4:
            a = max(minpos, int(2 / deficit) - 1)
            for aa in range(a, min(a + 80, NMAX - 1)):
                w = H(aa, aa + 1)
                if w <= deficit:
                    cands.append((w, aa, aa + 1))
                    break
        cands.sort(key=lambda t: -t[0])
        for (w, a, b) in cands[:25]:
            nd = deficit - w
            if nd == 0 or nd >= Fraction(1, NMAX * NMAX):
                res = dfs(nd, b + 2, intervals + [(a, b)], depth - 1)
                if res:
                    return res
        return None

    return dfs(deficit, minpos, intervals, 14)

for B0 in range(3, 60):
    if H(2, B0) >= 1:
        break
    res = try_start(B0)
    if res:
        total = sum(H(a, b) for (a, b) in res)
        assert total == 1
        ok = all(res[i+1][0] - res[i][1] >= 2 for i in range(len(res)-1))
        assert all(b - a >= 1 for (a, b) in res)
        print("SOLUTION k =", len(res), ":", res, "nonadjacent:", ok, flush=True)
        found.append(res)
        json.dump([list(map(int, iv)) for iv in res], open("sol289.json", "w"))
        break
print("done", len(found))
