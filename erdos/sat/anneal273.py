"""Simulated annealing for #273 covering: minimize uncovered count over
residue assignments r_m for all usable moduli m | N (m = p-1, p prime).
Incremental cover counts via a hit-multiplicity array."""
import numpy as np, json, random, sys, math, time
from sympy import isprime

N = int(sys.argv[1]) if len(sys.argv) > 1 else 332640
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 1
TIME = float(sys.argv[3]) if len(sys.argv) > 3 else 1500.0

pool = [d for d in range(4, N + 1) if N % d == 0 and isprime(d + 1)]
print(f"N={N} pool={len(pool)} mass={sum(1/m for m in pool):.4f}", flush=True)

rng = random.Random(SEED)
np.random.seed(SEED)

# initial: greedy
hits = np.zeros(N, dtype=np.int16)
res = {}
for m in sorted(pool):
    fresh = (hits == 0).reshape(N // m, m).sum(axis=0)
    r = int(fresh.argmax())
    res[m] = r
    hits[np.arange(r, N, m)] += 1

def uncovered():
    return int((hits == 0).sum())

cur = uncovered()
best = cur
print("greedy uncovered:", cur, flush=True)
t0 = time.time()
it = 0
T0, T1 = 30.0, 0.3
while time.time() - t0 < TIME and cur > 0:
    it += 1
    frac = (time.time() - t0) / TIME
    T = T0 * math.exp(math.log(T1 / T0) * frac)
    m = pool[rng.randrange(len(pool))]
    old = res[m]
    # candidate: residue hitting most currently-uncovered points
    if rng.random() < 0.6:
        zero_mask = (hits == 0).reshape(N // m, m).sum(axis=0)
        new = int(zero_mask.argmax())
        if new == old:
            new = rng.randrange(m)
    else:
        new = rng.randrange(m)
    if new == old:
        continue
    idx_old = np.arange(old, N, m)
    idx_new = np.arange(new, N, m)
    # delta uncovered: removing old may expose hits==1 cells; adding new covers hits==0 cells
    exposed = int((hits[idx_old] == 1).sum())
    gained = int((hits[idx_new] == 0).sum())
    delta = exposed - gained
    if delta <= 0 or rng.random() < math.exp(-delta / max(T, 1e-9)):
        hits[idx_old] -= 1
        hits[idx_new] += 1
        res[m] = new
        cur += delta
        if cur < best:
            best = cur
            if best % 500 == 0 or best < 2000:
                print(f"it={it} best={best} T={T:.2f} t={time.time()-t0:.0f}s", flush=True)
    if cur == 0:
        break

print("final uncovered:", cur, "best:", best, flush=True)
if cur == 0:
    check = np.zeros(N, dtype=bool)
    for m, r in res.items():
        check[np.arange(r, N, m)] = True
    assert check.all()
    json.dump({"N": N, "cover": {str(m): int(r) for m, r in res.items()},
               "primes": {str(m): m + 1 for m in res}},
              open(f"cover273_SOLUTION_{N}.json", "w"), indent=1)
    print("FOUND AND VERIFIED COVERING SYSTEM — #273 SOLVED (pending distinctness/def checks)")
else:
    # save best hole structure for analysis
    holes = np.flatnonzero(hits == 0)
    json.dump({"N": N, "uncovered": int(cur), "holes_sample": holes[:200].tolist(),
               "res": {str(m): int(r) for m, r in res.items()}},
              open(f"anneal273_state_{N}_{SEED}.json", "w"))
