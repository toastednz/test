STATUS: BLOCKED

## Result

I did not determine \(K\), nor find a finite obstruction for the first open target \(k=6\). I established several rigorous Route-1 reductions. Most importantly: (i) any \(A(k)\)-coloring canonically produces a proper \(k\)-coloring of the unit-distance graph; (ii) a finite unit-distance graph of chromatic number \(>k\) yields an explicit finite obstruction to \(A(k)\); and (iii) a finite uniquely \(k\)-colorable unit-distance graph yields a stronger explicit finite obstruction to \(A(k)\) through a “countdown propagation” gadget. The latter construction is completely finite and exact. However, for \(k=6\) this mechanism already requires a \(6\)-chromatic unit-distance graph, whose existence is an unresolved Hadwiger–Nelson issue. I also proved that configurations with only rational coordinates can never be obstructions, and that configurations confined to the triangular lattice can never obstruct \(A(k)\) for \(k\ge3\). Thus several natural exact-SAT search spaces are structurally incapable of reaching \(k=6\).

## Complete Argument

### 1. The window-coloring lemma

Fix \(k\ge2\), and suppose \(R\subseteq\mathbb R^2\) satisfies the two conditions in \(A(k)\). Fix a unit vector \(u\). Define
\[
f_u(x)=\min\{i\in\{0,\ldots,k-1\}:x+iu\in R\}.
\]
This is well-defined because every unit-step \(k\)-progression meets \(R\).

#### Lemma 1
For every fixed unit vector \(u\), the map
\[
f_u:\mathbb R^2\longrightarrow\{0,\ldots,k-1\}
\]
is a proper \(k\)-coloring of the unit-distance graph.

#### Proof
Let \(\|x-y\|_2=1\). If \(f_u(x)=f_u(y)=i\), then both
\[
x+iu,\qquad y+iu
\]
are red. Their difference is \(x-y\), so they are exactly unit distance apart, contradicting red independence. Hence \(f_u(x)\ne f_u(y)\). ∎

Thus:

#### Corollary 2
If \(A(k)\) holds, then
\[
\chi(\mathbb R^2)\le k.
\]

In particular, an \(A(6)\)-construction would also improve the current upper bound in the Hadwiger–Nelson problem from \(7\) to \(6\).

The maps \(f_u\) satisfy an additional exact transition rule:
\[
f_u(x)>0\quad\Longrightarrow\quad f_u(x+u)=f_u(x)-1.
\]
Indeed, if \(f_u(x)=j>0\), then
\[
x+u,\ldots,x+(j-1)u
\]
are blue and \(x+ju\) is red. Therefore the first red point in the window starting at \(x+u\) occurs at index \(j-1\).

If \(f_u(x)=0\), then \(x\) is red, so \(x+u\) is blue, and hence
\[
f_u(x+u)\in\{1,\ldots,k-1\}.
\]

This countdown rule is the main extra information beyond ordinary proper \(k\)-colorability.

---

### 2. A finite chromatic obstruction

The preceding argument has a direct finite form.

#### Lemma 3
Let \(H=(W,E)\) be a finite unit-distance graph embedded in \(\mathbb R^2\), and suppose \(\chi(H)>k\). Then there is an explicit finite obstruction to \(A(k)\).

#### Proof
Fix any unit vector \(u\). For every \(w\in W\), include the progression
\[
P_w=\{w,w+u,\ldots,w+(k-1)u\}.
\]
For every edge \(ww'\in E\) and every \(i\in\{0,\ldots,k-1\}\), include the unit pair
\[
\{w+iu,w'+iu\}.
\]
These are unit pairs because
\[
\|(w+iu)-(w'+iu)\|_2=\|w-w'\|_2=1.
\]

Suppose a red/blue assignment satisfied all these finite constraints. Each \(P_w\) contains a red point; select one red index
\[
h(w)\in\{0,\ldots,k-1\}
\]
such that \(w+h(w)u\) is red.

If \(ww'\in E\), then \(h(w)\ne h(w')\), because otherwise the corresponding red points would be one of the selected unit pairs. Therefore \(h\) is a proper \(k\)-coloring of \(H\), contradicting \(\chi(H)>k\). ∎

This recovers the implication \(A(k)\Rightarrow\chi(\mathbb R^2)\le k\) using only a finite witness. In particular, the existence of a finite \(5\)-chromatic unit-distance graph gives a finite obstruction to \(A(4)\). It does not address \(A(5)\) or \(A(6)\).

There is also a sharp limitation to this construction. If \(H\) is \(k\)-colorable and only the corresponding-layer unit pairs are used, choose a proper coloring
\[
h:W\to\{0,\ldots,k-1\}
\]
and color exactly \(w+h(w)u\) red in the chain over \(w\). This satisfies every progression clause and every corresponding-layer edge clause.

Even if all unit pairs among the resulting points are included, a generic choice of \(u\) preserves this assignment. Indeed, a possible red-red unit equality has the form
\[
\|w-w'+(h(w)-h(w'))u\|_2=1.
\]
For fixed \(w,w'\) and nonzero \(h(w)-h(w')\), this imposes one linear condition on \(u\cdot(w-w')\), hence excludes at most two points of \(S^1\). There are only finitely many pairs. If the index difference is zero, properness of \(h\) handles all unit pairs in \(W\). Thus a generic \(u\) avoids every unwanted red-red unit pair.

Consequently, merely stacking parallel \(k\)-chains over a \(k\)-colorable unit graph cannot obstruct \(A(k)\). Deliberately engineered cross-layer incidences are essential.

---

### 3. A finite propagation gadget from unique colorability

A stronger finite construction uses the countdown transition.

Call an embedded finite unit-distance graph \(H=(W,E)\) **uniquely \(k\)-colorable** if \(\chi(H)=k\) and any two proper maps \(W\to\{0,\ldots,k-1\}\) differ by a permutation of the \(k\) colors.

Fix a distinguished vertex \(w_0\in W\).

#### Lemma 4: finite countdown propagation
Let \(r\in\mathbb R^2\) and let \(u\) be a unit vector. Translate \(H\) so that \(w_0\) is at \(r\). For each translated vertex \(w\), include the two progressions
\[
\{w,w+u,\ldots,w+(k-1)u\}
\]
and
\[
\{w+u,w+2u,\ldots,w+ku\}.
\]
For each edge \(ww'\in E\) and each \(i=0,\ldots,k\), include the unit pair
\[
\{w+iu,w'+iu\}.
\]

In every satisfying coloring of these finite constraints,
\[
r\in R\quad\Longrightarrow\quad r+ku\in R.
\]

#### Proof
For each vertex \(w\), define
\[
a(w)=\min\{i\in\{0,\ldots,k-1\}:w+iu\in R\},
\]
and
\[
b(w)=\min\{i\in\{0,\ldots,k-1\}:w+(i+1)u\in R\}.
\]
Both are well-defined by the two progression clauses.

If \(ww'\in E\) and \(a(w)=a(w')=i\), then \(w+iu\) and \(w'+iu\) are red endpoints of a selected unit pair, impossible. Thus \(a\) is a proper \(k\)-coloring of \(H\). The same argument shows that \(b\) is a proper \(k\)-coloring.

By unique \(k\)-colorability, there is a permutation \(\pi\) of \(\{0,\ldots,k-1\}\) such that
\[
b=\pi\circ a.
\]

If \(a(w)=j>0\), then the definition of the first red point gives
\[
b(w)=j-1.
\]
Because \(\chi(H)=k\), the coloring \(a\) uses all \(k\) colors. Therefore, for every \(j=1,\ldots,k-1\),
\[
\pi(j)=j-1.
\]
Since \(\pi\) is a permutation, its only remaining value is
\[
\pi(0)=k-1.
\]

If \(r\) is red, then \(a(w_0)=0\), so
\[
b(w_0)=k-1.
\]
By the definition of \(b\), this means precisely that \(r+ku\) is red. ∎

This propagation lemma yields a completely explicit finite obstruction.

#### Theorem 5
If there exists a finite uniquely \(k\)-colorable unit-distance graph, then \(A(k)\) fails. Moreover, the failure has an explicit finite geometric obstruction.

#### Proof
Choose unit vectors
\[
a=(1,0),
\]
and
\[
b=\left(\frac{2k^2-1}{2k^2},
\frac{\sqrt{4k^2-1}}{2k^2}\right).
\]
Both are unit vectors, since
\[
(2k^2-1)^2+(4k^2-1)=4k^4.
\]
Furthermore,
\[
\|k(a-b)\|_2^2
=
k^2\left(
\frac{1}{4k^4}
+
\frac{4k^2-1}{4k^4}
\right)=1.
\]
Hence
\[
\|ka-kb\|_2=1.
\]

Start with one unit-step \(k\)-progression
\[
P_0=\{r_0,r_1,\ldots,r_{k-1}\}.
\]
For each candidate \(r_j\), attach two copies of the propagation gadget from Lemma 4:

- one with distinguished point \(r_j\) and direction \(a\);
- one with distinguished point \(r_j\) and direction \(b\).

Finally include the unit pair
\[
\{r_j+ka,r_j+kb\}.
\]

Suppose all finite constraints were satisfiable. The initial progression \(P_0\) contains some red point \(r_j\). Lemma 4 then forces both
\[
r_j+ka\in R
\quad\text{and}\quad
r_j+kb\in R.
\]
But these two points are exactly unit distance apart, contradicting the final unit-pair clause.

Thus the finite system is unsatisfiable. ∎

If \(H\) has \(n\) vertices, this construction uses at most
\[
k+2kn(k+1)
\]
points before identifications, so it is finite and effective. If the coordinates of \(H\) are algebraic, every coordinate in the obstruction is algebraic and all incidences can be checked exactly.

For \(k=3\), the unit equilateral triangle is uniquely \(3\)-colorable, so this gives a finite obstruction to \(A(3)\). The value for Route 1 is the general mechanism, especially for testing candidate uniquely colorable graphs.

---

### 4. Why this mechanism is blocked at \(k=6\)

Unique colorability is stronger than necessary. Define a graph \(H\) to be **countdown-rigid at \(k\)** if, whenever \(a,b\) are proper \(k\)-colorings satisfying
\[
a(v)>0\implies b(v)=a(v)-1,
\]
one necessarily has
\[
a(v)=0\implies b(v)=k-1.
\]
Lemma 4 only needs countdown rigidity, not full unique colorability.

However, this still encounters a sharp chromatic barrier.

#### Lemma 6
If a nonempty graph \(H\) is countdown-rigid at \(k\) and is \(k\)-colorable, then \(\chi(H)=k\).

#### Proof
Suppose instead that \(H\) has a proper \(q\)-coloring with \(q<k\). Label its colors
\[
0,1,\ldots,q-1
\]
and call the resulting coloring \(a\). Define
\[
b(v)=a(v)-1\pmod q.
\]
This is also a proper coloring, because it is obtained by permuting the \(q\) color classes. If \(a(v)>0\), then \(b(v)=a(v)-1\), as required. But if \(a(v)=0\), then
\[
b(v)=q-1\ne k-1.
\]
Thus countdown rigidity fails. ∎

Therefore a countdown-rigid unit-distance graph for \(k=6\) would in particular be a finite \(6\)-chromatic unit-distance graph. No such graph is currently known; producing one would prove
\[
\chi(\mathbb R^2)\ge6.
\]
Thus the cleanest propagation implementation of Route 1 is blocked by an unresolved problem of comparable strength.

This does not prove that every Route-1 obstruction to \(A(6)\) requires a \(6\)-chromatic unit-distance graph. A more sophisticated gadget could use progression clauses internally rather than reduce to two ordinary proper colorings. Such a mixed progression/unit-distance gadget is the remaining viable SAT target.

---

### 5. Rational-coordinate configurations cannot be obstructions

The suggested use of Pythagorean unit vectors has a serious structural defect.

#### Lemma 7
The unit-distance graph on \(\mathbb Q^2\) is bipartite.

#### Proof
Let \((a,b)\in\mathbb Q^2\) satisfy
\[
a^2+b^2=1.
\]
Write
\[
a=\frac AC,\qquad b=\frac BC
\]
with integers \(A,B,C\), \(C>0\), and \(\gcd(A,B,C)=1\). Then
\[
A^2+B^2=C^2.
\]
For a primitive Pythagorean triple, \(C\) is odd and exactly one of \(A,B\) is odd. Thus both \(a,b\) have odd denominator when viewed as \(2\)-adic integers, and their reductions modulo \(2\) satisfy
\[
\bar a+\bar b=1\in\mathbb F_2.
\]

Consider a cycle in the rational unit-distance graph, with oriented edge vectors
\[
(a_1,b_1),\ldots,(a_m,b_m).
\]
Their sum is zero. Reducing both coordinate sums modulo \(2\) gives
\[
\sum_{i=1}^m \bar a_i=0,\qquad
\sum_{i=1}^m \bar b_i=0.
\]
Hence
\[
m
=\sum_{i=1}^m(\bar a_i+\bar b_i)
=0\pmod2.
\]
Every cycle is even, so the graph is bipartite. ∎

#### Corollary 8
No finite configuration contained in \(\mathbb Q^2\) can be an obstruction to \(A(k)\), for any \(k\ge2\).

#### Proof
Choose one side of each bipartite component to be red. Every rational unit edge then has exactly one red endpoint. Consequently every rational unit-step progression alternates colors, so every progression of length at least \(2\) contains a red point. ∎

Thus an exact SAT search using only rational coordinates and rational Pythagorean directions is guaranteed to remain satisfiable.

---

### 6. The triangular lattice also cannot supply an obstruction

Let
\[
a=(1,0),\qquad b=\left(\frac12,\frac{\sqrt3}{2}\right),
\]
and let
\[
\Lambda=\{ma+nb:m,n\in\mathbb Z\}.
\]

The squared norm of \(ma+nb\) is
\[
m^2+mn+n^2.
\]
The integer solutions of
\[
m^2+mn+n^2=1
\]
are exactly
\[
(\pm1,0),\quad(0,\pm1),\quad(1,-1),\quad(-1,1).
\]
Thus the only unit directions in \(\Lambda\) are
\[
\pm a,\quad\pm b,\quad\pm(a-b).
\]

Define
\[
\phi(ma+nb)=m+2n\pmod3
\]
and color a point red exactly when \(\phi=0\). Each of the six unit vectors has \(\phi\)-value \(1\) or \(2\), so no unit edge has two red endpoints. Along every unit direction, \(\phi\) cycles through all three residues. Therefore every three consecutive unit-spaced lattice points contain exactly one red point.

#### Corollary 9
No finite configuration contained in the triangular lattice can obstruct \(A(k)\) for any \(k\ge3\).

This explains why equilateral-triangle and rhombus closures that never leave the triangular lattice stabilize into a simple \(3\)-periodic SAT solution.

More generally, if an additive point group \(\Gamma\) admits a homomorphism
\[
\phi:\Gamma\to\mathbb Z/m\mathbb Z
\]
such that every unit difference under consideration maps to an element of order \(m\), then the red set \(\phi^{-1}(0)\) is unit-distance independent and meets every unit-step \(m\)-progression. Such homomorphic certificates should be searched for whenever a finite SAT family repeatedly remains satisfiable.

## Self-Audit

1. **The strongest obstruction theorem is conditional.**  
   I did not produce a uniquely \(6\)-colorable or countdown-rigid \(6\)-chromatic unit-distance graph. Thus Theorem 5 is a rigorous obstruction mechanism, not a resolution of \(A(6)\). I believe the theorem itself is sound because the proof is a finite clause-by-clause argument, including an explicit exact endpoint unit-distance calculation.

2. **The chromatic blockage only rules out a class of gadgets.**  
   Lemma 6 does not show that every finite obstruction to \(A(6)\) would imply \(\chi(\mathbb R^2)\ge6\). A mixed gadget with progression clauses internal to the forcing mechanism could evade it. I have stated the conclusion only for countdown-rigid graph gadgets, where the modular counterexample proves the limitation exactly.

3. **No SAT experiment or certificate is being represented as completed.**  
   The proposed computations below are discovery and verification procedures; I have not run them on a sufficiently rich \(k=6\) configuration and do not claim an unsatisfiable instance. Any future UNSAT result would still require an LRAT/DRAT certificate and exact algebraic incidence verification.

## Computations To Verify

The following code builds the complete unit-pair and contained-progression CNF for a finite point set in one exact algebraic number field.

```python
from itertools import combinations, permutations
from pysat.formula import CNF
from pysat.solvers import Solver

# K should be a SymPy AlgebraicField, for example:
#
# from sympy import QQ, sqrt
# K = QQ.algebraic_field(sqrt(3), sqrt(11), sqrt(143))
#
# Convert every coordinate with K.from_sympy(expr).

def padd(p, q):
    return (p[0] + q[0], p[1] + q[1])

def psub(p, q):
    return (p[0] - q[0], p[1] - q[1])

def smul(n, p):
    return (n * p[0], n * p[1])

def norm2(p):
    return p[0] * p[0] + p[1] * p[1]

def exact_cnf(points, k, K):
    """
    Adds:
      * every unit-distance pair among points;
      * every unit-step k-chain entirely contained in points.
    All comparisons occur in the exact algebraic field K.
    """
    points = list(dict.fromkeys(points))
    index = {p: i + 1 for i, p in enumerate(points)}
    cnf = CNF()

    # All exact unit pairs.
    for i, j in combinations(range(len(points)), 2):
        if norm2(psub(points[i], points[j])) == K.one:
            cnf.append([-(i + 1), -(j + 1)])

    # All contained unit-step k-progressions.
    progression_clauses = set()
    for i, j in permutations(range(len(points)), 2):
        u = psub(points[j], points[i])
        if norm2(u) != K.one:
            continue
        chain = []
        for t in range(k):
            q = padd(points[i], smul(t, u))
            if q not in index:
                break
            chain.append(index[q])
        if len(chain) == k:
            # Clause order is irrelevant.
            progression_clauses.add(tuple(sorted(chain)))

    for clause in progression_clauses:
        cnf.append(list(clause))

    return points, cnf

def solve_cnf(cnf):
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        sat = solver.solve()
        model = solver.get_model() if sat else None
    return sat, model
```

A canonical backtracking test for unique \(k\)-colorability is:

```python
def proper_color_partitions(n, edges, k):
    """
    Enumerates proper set partitions into at most k color classes,
    quotienting out permutations of color names via restricted-growth form.
    Suitable only for modest graphs.
    """
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    color = [-1] * n
    out = []

    def rec(v, used):
        if v == n:
            out.append(tuple(color))
            return

        # Existing colors 0,...,used-1, plus at most one new color.
        for c in range(min(used + 1, k)):
            if all(color[w] != c for w in adj[v] if w < v):
                color[v] = c
                rec(v + 1, max(used, c + 1))
                color[v] = -1

    rec(0, 0)
    return out

def uniquely_k_colorable(n, edges, k):
    parts = proper_color_partitions(n, edges, k)
    if len(parts) != 1:
        return False
    return len(set(parts[0])) == k
```

Countdown rigidity can be checked directly by SAT. Let \(A_{v,j}\) and \(B_{v,j}\) encode two proper \(k\)-colorings. Add:

```python
from pysat.formula import CNF, IDPool

def pairwise_exactly_one(cnf, variables):
    cnf.append(list(variables))
    for x, y in combinations(variables, 2):
        cnf.append([-x, -y])

def countdown_counterexample_cnf(n, edges, k):
    """
    SAT means there are proper colorings A,B satisfying countdown on
    positive A-colors but violating 0 -> k-1 at some vertex.
    UNSAT means the graph is countdown-rigid at k.
    """
    pool = IDPool()
    cnf = CNF()

    A = lambda v, j: pool.id(("A", v, j))
    B = lambda v, j: pool.id(("B", v, j))

    for v in range(n):
        pairwise_exactly_one(cnf, [A(v, j) for j in range(k)])
        pairwise_exactly_one(cnf, [B(v, j) for j in range(k)])

    for u, v in edges:
        for j in range(k):
            cnf.append([-A(u, j), -A(v, j)])
            cnf.append([-B(u, j), -B(v, j)])

    # Positive colors count down.
    for v in range(n):
        for j in range(1, k):
            cnf.append([-A(v, j), B(v, j - 1)])

    # At least one vertex violates A=0 => B=k-1.
    bad = []
    for v in range(n):
        z = pool.id(("bad", v))
        bad.append(z)
        cnf.append([-z, A(v, 0)])
        cnf.append([-z, -B(v, k - 1)])
    cnf.append(bad)

    return cnf
```

To build the finite obstruction from Theorem 5, given exact coordinates `H` and a distinguished index `h0`:

```python
def unique_coloring_obstruction_points(H, h0, k, K):
    """
    Produces all points needed for Theorem 5.
    exact_cnf() then adds all unit edges and all contained k-chains.
    """
    one = K.one
    zero = K.zero

    a = (one, zero)

    # K must contain sqrt(4*k*k - 1).
    # Replace radical_expr by K.from_sympy(sqrt(4*k*k - 1)).
    from sympy import sqrt, Rational
    bx = K.from_sympy(Rational(2*k*k - 1, 2*k*k))
    by = K.from_sympy(sqrt(4*k*k - 1) / (2*k*k))
    b = (bx, by)

    assert norm2(a) == one
    assert norm2(b) == one
    assert norm2(smul(k, psub(a, b))) == one

    points = set()

    # Initial k-chain.
    initial = [smul(j, a) for j in range(k)]
    points.update(initial)

    w0 = H[h0]

    for r in initial:
        for u in (a, b):
            shift = psub(r, w0)
            for w in H:
                base = padd(shift, w)
                # Union of the windows starting at base and base+u.
                for layer in range(k + 1):
                    points.add(padd(base, smul(layer, u)))

    return list(points)
```

Concrete search program:

1. Import exact coordinates of candidate finite unit-distance graphs.
2. Verify all squared distances in a declared algebraic field.
3. Test unique colorability and countdown rigidity.
4. Build the propagation obstruction if either test succeeds.
5. Run exact geometric CNF generation.
6. If UNSAT, emit a DRAT/LRAT proof with a proof-producing solver and verify it independently.
7. For direct \(k=6\) searches, generate mixed-direction configurations—not rational-only or triangular-lattice-only ones—and add every contained six-term chain.

## Route Diagnosis

**Proved ledger**

- \(A(k)\Rightarrow\chi(\mathbb R^2)\le k\).
- Every finite unit-distance graph with chromatic number \(>k\) gives an explicit finite obstruction to \(A(k)\).
- A finite uniquely \(k\)-colorable unit-distance graph gives an explicit finite obstruction to \(A(k)\) through the countdown gadget.
- Countdown rigidity at \(k\) requires chromatic number at least \(k\).
- Rational-coordinate configurations can never obstruct \(A(k)\).
- Triangular-lattice configurations can never obstruct \(A(k)\) for \(k\ge3\).
- Generic parallel-chain lifts of a \(k\)-colorable graph are satisfiable and therefore cannot be the needed obstruction.

**Plausible but unproved targets**

- A finite mixed-direction progression gadget might obstruct \(A(6)\) without containing a \(6\)-chromatic unit-distance graph.
- Unsatisfiable cores for the known \(k=5\) theorem may reveal a reusable forcing operation that can be amplified to \(k=6\).

**Dead ends**

- Rational/Pythagorean-coordinate SAT search: blocked by bipartiteness.
- Pure triangular-lattice search: blocked by the explicit mod-\(3\) coloring.
- Parallel copies of ordinary unit-distance graphs: blocked unless the base graph has chromatic number \(>k\).
- Unique-coloring or countdown-rigidity search for \(k=6\): blocked by the unresolved existence of a finite \(6\)-chromatic unit-distance graph.

The best fresh Route-1 attempt is therefore to reconstruct an explicit finite obstruction underlying Tsaturian’s \(k=5\) theorem, extract its smallest exact UNSAT core, and search for a substitution or composition rule that lengthens the progression clauses from \(5\) to \(6\). Direct \(k=6\) SAT generation should deliberately combine several algebraically unrelated unit directions and progression overlaps, while checking for modular/homomorphic colorings that explain persistent satisfiability.