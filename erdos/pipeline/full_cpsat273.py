"""Full CP-SAT attack on #273 for universe N: choose residue r_m for every
usable modulus m (m = p-1, p prime, m | N) such that all of Z_N is covered."""
import sys, json
import numpy as np
from sympy import isprime
from ortools.sat.python import cp_model

N = int(sys.argv[1]) if len(sys.argv) > 1 else 332640
TLIMIT = float(sys.argv[2]) if len(sys.argv) > 2 else 3000.0
pool = [d for d in range(4, N + 1) if N % d == 0 and isprime(d + 1)]
print(f"N={N} pool={len(pool)} mass={sum(1/m for m in pool):.4f}", flush=True)

model = cp_model.CpModel()
y = {}
for m in pool:
    for r in range(m):
        y[(m, r)] = model.NewBoolVar(f"y{m}_{r}")
    model.AddExactlyOne(y[(m, r)] for r in range(m))
print("vars:", len(y), flush=True)
for x in range(N):
    model.AddBoolOr([y[(m, x % m)] for m in pool])
print("model built", flush=True)

solver = cp_model.CpSolver()
solver.parameters.max_time_in_seconds = TLIMIT
solver.parameters.num_search_workers = 3
solver.parameters.log_search_progress = False
status = solver.Solve(model)
print("status:", solver.StatusName(status), flush=True)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    resd = {}
    for m in pool:
        for r in range(m):
            if solver.Value(y[(m, r)]):
                resd[m] = r
                break
    cov = np.zeros(N, dtype=bool)
    for m, r in resd.items():
        cov[np.arange(r, N, m)] = True
    assert cov.all()
    json.dump({"N": N, "cover": {str(m): r for m, r in sorted(resd.items())},
               "primes": {str(m): m + 1 for m in resd}},
              open(f"cover273_SOLUTION_N{N}.json", "w"), indent=1)
    print("*** #273 COVERING SYSTEM FOUND AND VERIFIED ***", flush=True)
elif status == cp_model.INFEASIBLE:
    print(f"INFEASIBLE: no covering system within universe N={N} with this pool", flush=True)
