"""Erdos problem #617 (Erdos-Gyarfas): any r-coloring of E(K_{r^2+1}) has an
(r+1)-clique missing a color. Proved r=3,4. Attempt falsification at r=5:
find a 5-coloring of E(K_26) such that EVERY 6-subset sees all 5 colors.
SAT: vars x[e][c]; exactly-one per edge; for each 6-subset S and color c:
   OR_{e in S} x[e][c].
If SAT -> disproof of the conjecture (machine-checkable witness).
"""
import sys, itertools, json, time
from pysat.solvers import Cadical195 as Solver
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

r = int(sys.argv[1]) if len(sys.argv) > 1 else 5
n = r * r + 1
V = list(range(n))
E = list(itertools.combinations(V, 2))
pool = IDPool()
def x(e, c):
    return pool.id(('x', e, c))

cnf = []
# exactly one color per edge
for e in E:
    lits = [x(e, c) for c in range(r)]
    cnf.append(lits)  # at least one
    for a in range(r):
        for b in range(a + 1, r):
            cnf.append([-lits[a], -lits[b]])
# every (r+1)-subset sees every color
cnt = 0
for S in itertools.combinations(V, r + 1):
    edges = [tuple(sorted(p)) for p in itertools.combinations(S, 2)]
    for c in range(r):
        cnf.append([x(e, c) for e in edges])
    cnt += 1
print(f"r={r} n={n} edges={len(E)} subsets={cnt} clauses={len(cnf)}", flush=True)

# symmetry breaking: fix colors on a star at vertex 0: edge (0,i) gets color (i-1)%r ?
# careful: too-strong breaking can lose solutions. Use mild: edge (0,1)=color0,
# and (0,2) in {0,1}, (0,3) in {0,1,2} -- standard color symmetry breaking only.
cnf.append([x((0, 1), 0)])
cnf.append([x((0, 2), 0), x((0, 2), 1)])
if r > 3:
    cnf.append([x((0, 3), 0), x((0, 3), 1), x((0, 3), 2)])
if r > 4:
    cnf.append([x((0, 4), 0), x((0, 4), 1), x((0, 4), 2), x((0, 4), 3)])

s = Solver(bootstrap_with=cnf)
t0 = time.time()
budget = int(sys.argv[2]) if len(sys.argv) > 2 else 3000  # seconds
# cadical in pysat: no native timeout; use solve_limited with conflict budget loop
s.conf_budget(10**7)
res = None
while time.time() - t0 < budget:
    res = s.solve_limited(expect_interrupt=False)
    if res is not None:
        break
    s.conf_budget(10**7)
print("elapsed", round(time.time() - t0, 1), "result:", res, flush=True)
if res:
    m = set(l for l in s.get_model() if l > 0)
    coloring = {}
    for e in E:
        for c in range(r):
            if x(e, c) in m:
                coloring[str(e)] = c
    json.dump(coloring, open(f'sat617_r{r}_solution.json', 'w'))
    print("SAT!!! coloring written — CONJECTURE #617 DISPROVED (verify independently)")
    # independent verification
    bad = 0
    for S in itertools.combinations(V, r + 1):
        cols = set(coloring[str(tuple(sorted(p)))] for p in itertools.combinations(S, 2))
        if len(cols) < r:
            bad += 1
    print("verification: bad subsets =", bad)
elif res is False:
    print(f"UNSAT — conjecture #617 VERIFIED for r={r} (new partial result if r>=5)")
else:
    print("UNDECIDED within budget")
