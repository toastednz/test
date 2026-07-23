"""Erdos #273: covering system with all moduli of the form p-1, p>=5 prime,
distinct moduli. Search: pick N (highly composite), pool = {p-1 : p prime>=5,
(p-1)|N}; greedily choose residues maximizing fresh coverage of Z_N, with
randomized restarts + final brute-force patching over remaining holes.
A found cover is verified exactly and dumped as JSON certificate.
"""
import numpy as np, json, sys, random
from sympy import isprime

def usable_divisors(N):
    divs = [d for d in range(4, N + 1) if N % d == 0 and isprime(d + 1)]
    return sorted(divs)

def try_cover(N, pool, rng, greedy_top=4):
    # covered: bool array over Z_N
    covered = np.zeros(N, dtype=bool)
    choice = {}
    pool = list(pool)
    # process moduli mostly smallest-first (greedy), with randomization
    pool.sort()
    remaining = pool[:]
    while remaining:
        best = []
        m = None
        # pick next modulus: usually the smallest unused, sometimes random among first 3
        idx = 0 if rng.random() < 0.7 else rng.randrange(min(3, len(remaining)))
        m = remaining.pop(idx)
        arr = (~covered).reshape(N // m, m).sum(axis=0)  # fresh count per residue
        mx = arr.max()
        if mx == 0:
            continue
        # choose among top residues randomly
        cand = np.flatnonzero(arr >= mx - max(0, int(mx * 0.02)))
        r = int(cand[rng.randrange(len(cand))])
        choice[m] = r
        covered[np.arange(r, N, m)] = True
        if covered.all():
            return choice
    return None

def verify(N, choice):
    covered = np.zeros(N, dtype=bool)
    for m, r in choice.items():
        covered[np.arange(r % m, N, m)] = True
    return bool(covered.all())

def main():
    candidates_N = [
        332640,    # 2^5 3^3 5 7 11
        665280,    # 2^6 3^3 5 7 11
        1081080,   # 2^3 3^3 5 7 11 13
        2162160,   # 2^4 3^3 5 7 11 13
        4324320,   # 2^5 3^3 5 7 11 13
        720720, 1441440, 2882880,
        831600, 1663200,           # 2^4 3^3 5^2 7 11
        60480, 120960, 241920, 110880, 221760, 55440,
    ]
    rng = random.Random(12345)
    best_deficit = None
    for N in candidates_N:
        pool = usable_divisors(N)
        mass = sum(1.0 / m for m in pool)
        print(f"N={N}: pool={len(pool)} moduli, mass={mass:.4f}", flush=True)
        if mass < 1.0:
            continue
        print("   pool:", pool, flush=True)
        for attempt in range(400):
            res = try_cover(N, pool, rng)
            if res:
                assert verify(N, res)
                out = {str(m): int(r) for m, r in res.items()}
                json.dump({"N": N, "cover": out,
                           "primes": {str(m): m + 1 for m in res}},
                          open("cover273_SOLUTION.json", "w"), indent=1)
                print("FOUND COVERING SYSTEM!!!", out, flush=True)
                return
        # report best deficit for insight
        covered = np.zeros(N, dtype=bool)
        for m in pool:
            arr = (~covered).reshape(N // m, m).sum(axis=0)
            r = int(arr.argmax())
            covered[np.arange(r, N, m)] = True
        print(f"   greedy leaves {int((~covered).sum())} uncovered of {N}", flush=True)
    print("no cover found in these universes")

if __name__ == "__main__":
    main()
