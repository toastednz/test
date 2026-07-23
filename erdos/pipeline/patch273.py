"""Endgame for #273: freeze small-modulus residues from an anneal state,
exact-cover the remaining holes with the large moduli via CP-SAT."""
import json, sys, numpy as np
from sympy import isprime
from ortools.sat.python import cp_model

state_fn = sys.argv[1]
SPLIT = int(sys.argv[2]) if len(sys.argv) > 2 else 150   # moduli >= SPLIT are re-chosen
TLIMIT = float(sys.argv[3]) if len(sys.argv) > 3 else 600.0

st = json.load(open(state_fn))
N = st["N"]
res = {int(m): int(r) for m, r in st["res"].items()}
pool = sorted(res)
small = [m for m in pool if m < SPLIT]
large = [m for m in pool if m >= SPLIT]
print(f"N={N} small(frozen)={len(small)} large(free)={len(large)}")

hits = np.zeros(N, dtype=np.int32)
for m in small:
    hits[np.arange(res[m] % m, N, m)] += 1
holes = np.flatnonzero(hits == 0)
print("holes after frozen small part:", len(holes))

model = cp_model.CpModel()
y = {}
holeset = {}
for m in large:
    residues = sorted(set(int(h % m) for h in holes))
    for r in residues:
        y[(m, r)] = model.NewBoolVar(f"y_{m}_{r}")
    model.AddAtMostOne(y[(m, r)] for r in residues)
for h in holes:
    lits = []
    for m in large:
        key = (m, int(h % m))
        if key in y:
            lits.append(y[key])
    model.AddBoolOr(lits)
print("vars:", len(y))

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = TLIMIT
solver.parameters.num_search_workers = 3
status = solver.Solve(model)
print("status:", solver.StatusName(status))
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    newres = {m: res[m] for m in small}
    used = set(small)
    for (m, r), var in y.items():
        if solver.Value(var):
            newres[m] = r
            used.add(m)
    # unused large moduli: keep old residues (harmless) or drop them
    cov = np.zeros(N, dtype=bool)
    for m, r in newres.items():
        cov[np.arange(r % m, N, m)] = True
    assert cov.all(), "verification failed!"
    out = {"N": N, "cover": {str(m): int(r) for m, r in sorted(newres.items())},
           "primes": {str(m): m + 1 for m in newres}}
    for m in out["cover"]:
        assert isprime(int(m) + 1)
    json.dump(out, open("cover273_SOLUTION.json", "w"), indent=1)
    print("*** COVERING SYSTEM FOUND AND VERIFIED -> cover273_SOLUTION.json ***")
    print("moduli used:", sorted(newres))
else:
    print("no exact cover with this split; try different SPLIT/seed/state")
