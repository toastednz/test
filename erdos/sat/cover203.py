"""Erdos #203: find m with (m,6)=1 such that 2^k 3^l m + 1 is composite
for all k,l >= 0.  Strategy: cover Z^2 (exponent pairs (k,l)) by sets
S_p = {(k,l): 2^k 3^l ≡ t_p  (mod p)} for a finite set of primes p and
choices t_p in <2,3> ≤ F_p^*.  Each S_p is a shift of the base lattice-mask
M_p = {(k,l): 2^k 3^l ≡ 1 (mod p)}, periodic with (o2(p), o3(p)).
If the masks cover the torus Z_A x Z_B (o2|A, o3|B for all chosen p),
then CRT determines m with m ≡ -(2^{k}3^{l})^{-1} realized per prime.
Phase 1 (this script): choose torus + prime pool, anneal shifts to cover.
"""
import sys, json, math, time, random
import numpy as np
from sympy import primerange
from sympy.ntheory.residue_ntheory import n_order

A = int(sys.argv[1]) if len(sys.argv) > 1 else 5040
B = int(sys.argv[2]) if len(sys.argv) > 2 else 5040
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 1
TIME = float(sys.argv[4]) if len(sys.argv) > 4 else 2400.0
PMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 3_000_000

rng = random.Random(SEED)

# pool: primes with o2|A, o3|B
pool = []
for p in primerange(5, PMAX):
    o2 = n_order(2, p)
    if A % o2 != 0:
        continue
    o3 = n_order(3, p)
    if B % o3 != 0:
        continue
    idx = (o2 * o3) // math.gcd(o2, o3)
    pool.append((p, o2, o3, idx))
pool.sort(key=lambda t: t[3])
mass = sum(1.0 / t[3] for t in pool)
print(f"torus {A}x{B}: pool={len(pool)} primes, mass={mass:.4f}", flush=True)
for t in pool[:40]:
    print("   p=%d o2=%d o3=%d index=%d" % t, flush=True)
if mass < 1.02:
    print("insufficient mass; abort")
    sys.exit(0)

# base masks: for each p, list of (k mod o2, l mod o3) with 2^k 3^l = 1 mod p
masks = {}
for (p, o2, o3, idx) in pool:
    pow2 = [pow(2, k, p) for k in range(o2)]
    log3 = {}
    v = 1
    for l in range(o3):
        log3.setdefault(v, l)
        v = (v * 3) % p
    base = []
    for k in range(o2):
        inv = pow(pow2[k], p - 2, p)
        l = log3.get(inv)
        if l is not None:
            base.append((k, l))
    masks[p] = (o2, o3, base)

# precompute cell lists per prime for shift (0,0); shifting = roll
def cells(p, sa, sb):
    o2, o3, base = masks[p]
    ks = []
    ls = []
    for (k0, l0) in base:
        kk = (k0 + sa) % o2
        ll = (l0 + sb) % o3
        ks.append(np.arange(kk, A, o2))
        ls.append(np.arange(ll, B, o3))
    return [(K, L) for K, L in zip(ks, ls)]

hits = np.zeros((A, B), dtype=np.int16)
shift = {}
for (p, o2, o3, idx) in pool:
    sa, sb = rng.randrange(o2), rng.randrange(o3)
    shift[p] = (sa, sb)
    for K, L in cells(p, sa, sb):
        hits[np.ix_(K, L)] += 1

cur = int((hits == 0).sum())
best = cur
print("random-init uncovered:", cur, "of", A * B, flush=True)

t0 = time.time()
T0, T1 = 40.0, 0.2
it = 0
order = [t[0] for t in pool]
while time.time() - t0 < TIME and cur > 0:
    it += 1
    frac = (time.time() - t0) / TIME
    T = T0 * math.exp(math.log(T1 / T0) * frac)
    p = order[rng.randrange(len(order))]
    o2, o3, base = masks[p]
    old = shift[p]
    new = (rng.randrange(o2), rng.randrange(o3))
    if new == old:
        continue
    delta = 0
    oldcells = cells(p, *old)
    newcells = cells(p, *new)
    exposed = 0
    for K, L in oldcells:
        sub = hits[np.ix_(K, L)]
        exposed += int((sub == 1).sum())
    gained = 0
    for K, L in newcells:
        sub = hits[np.ix_(K, L)]
        gained += int((sub == 0).sum())
    delta = exposed - gained
    if delta <= 0 or rng.random() < math.exp(-delta / max(T, 1e-9)):
        for K, L in oldcells:
            hits[np.ix_(K, L)] -= 1
        for K, L in newcells:
            hits[np.ix_(K, L)] += 1
        shift[p] = new
        cur += delta
        if cur < best:
            best = cur
            if best < 5000 and (best % 100 == 0 or best < 60):
                print(f"it={it} best={best} T={T:.2f} t={time.time()-t0:.0f}s", flush=True)

print("final uncovered:", cur, flush=True)
state = {"A": A, "B": B, "shift": {str(p): list(s) for p, s in shift.items()},
         "uncovered": cur}
json.dump(state, open(f"cover203_state_{A}x{B}_{SEED}.json", "w"))
if cur == 0:
    print("TORUS COVERED — proceed to CRT phase for explicit m!", flush=True)
