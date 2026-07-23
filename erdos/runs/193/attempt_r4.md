STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #193. I obtained a rigorous refinement of Route 4: it suffices to construct an injective bounded-step planar walk whose **chronologically ordered collinear triples** form a uniformly sparse hypergraph. More precisely, bounded backward multiplicity, or even bounded hypergraph degeneracy, permits a bounded-increment integer height assignment producing a genuine counterexample in \(\mathbb Z^3\). I also proved several obstructions: recurrent visits with bounded gaps to any planar line defeat every bounded-increment lift; the natural digital linear lifts \((n,\lfloor\alpha n\rfloor,\lfloor\beta n\rfloor)\) always contain a three-term arithmetic progression under rational independence; and independent height increments with a positive probability of zero almost surely fail for every fixed planar step set. The route is blocked at the planar sparsity lemma: I cannot construct, or prove impossible, a fixed-step planar walk with bounded degeneracy of its forward-collinearity hypergraph.

## Complete Argument

Throughout, indices begin at \(0\), which is immaterial.

### 1. Only chronologically compatible projected triples are dangerous

Let \(b_n\in\mathbb Z^2\) be pairwise distinct, and let
\[
a_n=(b_n,z_n)\in\mathbb Z^3
\]
with
\[
z_0<z_1<z_2<\cdots.
\]

For \(i<j<k\), call \((i,j,k)\) a **forward-collinear triple** of the planar walk if
\[
b_k-b_j=\lambda(b_j-b_i)
\]
for some \(\lambda>0\). Thus the projected points are collinear and occur in their geometric order.

**Lemma 1.** If \(a_i,a_j,a_k\) are collinear, then \((i,j,k)\) is a forward-collinear triple of \(b\).

**Proof.** Put
\[
U=a_j-a_i=(b_j-b_i,z_j-z_i),\qquad
V=a_k-a_j=(b_k-b_j,z_k-z_j).
\]
Collinearity gives \(V=\lambda U\) for some nonzero real \(\lambda\). Since both vertical coordinates \(z_j-z_i\) and \(z_k-z_j\) are positive,
\[
\lambda=\frac{z_k-z_j}{z_j-z_i}>0.
\]
Consequently
\[
b_k-b_j=\lambda(b_j-b_i),
\]
as required. \(\square\)

Thus a strictly increasing height automatically destroys every projected collinear triple whose chronological order disagrees with its geometric order.

Define the 3-uniform hypergraph
\[
\mathcal H^+(b)
\]
on \(\mathbb N\), whose edges are the forward-collinear triples.

For \(k\ge2\), define its backward multiplicity
\[
P_k^+(b)=
\#\{(i,j):0\le i<j<k,\ (i,j,k)\in\mathcal H^+(b)\}.
\]

---

### 2. A bounded-backward-multiplicity planar walk would give a counterexample

**Theorem 2.** Let \(T\subseteq\mathbb Z^2\) be finite, and let \(b_n\) be an injective infinite \(T\)-walk. Suppose that
\[
P_k^+(b)\le B
\qquad\text{for every }k.
\]
Then there is a bounded-increment integer height sequence \(z_n\) for which
\[
a_n=(b_n,z_n)
\]
is an infinite bounded-step walk in \(\mathbb Z^3\) containing no three collinear points.

**Proof.** Set
\[
q=B+1.
\]
We recursively choose colors
\[
c_n\in\{0,1,\dots,B\}
\]
and define
\[
z_n=qn+c_n.
\]
Then
\[
z_{n+1}-z_n=q+c_{n+1}-c_n\in\{1,2,\dots,2B+1\},
\]
so the heights are strictly increasing and have increments in a fixed finite set.

Suppose \(c_0,\dots,c_{k-1}\) have already been selected. Consider one forward-collinear triple \((i,j,k)\). Since \(b_i,b_j,b_k\) are three distinct points on a planar line, choose an affine coordinate \(t\) on that line and write their parameters as \(t_i,t_j,t_k\). The lifted points are collinear exactly when
\[
(t_j-t_i)(z_k-z_i)=(t_k-t_i)(z_j-z_i).
\]
The coefficient of \(z_k\) is \(t_j-t_i\ne0\). Hence, once \(z_i,z_j\) are fixed, this equation forbids at most one real value of \(z_k\), and therefore at most one color \(c_k\).

There are at most \(P_k^+(b)\le B\) relevant pairs \((i,j)\). They therefore forbid at most \(B\) of the \(B+1\) possible colors. Choose an un-forbidden value for \(c_k\).

This constructs the sequence recursively. By construction, no edge of \(\mathcal H^+(b)\) lifts to a collinear triple. Lemma 1 shows that no other triple can be collinear because the heights are strictly increasing.

Finally,
\[
a_{n+1}-a_n
=
\bigl(b_{n+1}-b_n,\ z_{n+1}-z_n\bigr)
\in
T\times\{1,\dots,2B+1\},
\]
a fixed finite step set. The walk is injective because \(z_n\) is strictly increasing. \(\square\)

This reduces a disproof to the following concrete planar target:

> Find a fixed finite \(T\subseteq\mathbb Z^2\) and an infinite injective \(T\)-walk \(b_n\) with \(\sup_k P_k^+(b)<\infty\).

This target is strictly weaker than asking the planar walk to have no collinear triples.

There is also a useful compactness version.

**Corollary 3.** Fix \(T\) and \(B\). If for every \(N\) there is an injective \(T\)-walk
\[
b_0,\dots,b_{N-1}
\]
with \(P_k^+(b)\le B\) for all \(k<N\), then Erdős Problem #193 has a negative answer.

**Proof.** These finite walks form a finitely branching prefix tree. Arbitrarily large depth gives an infinite branch by König’s infinity lemma. Apply Theorem 2. \(\square\)

Thus, unlike searches whose step set changes with the length, an arbitrary-depth search for one fixed pair \((T,B)\) would suffice.

---

### 3. Bounded degeneracy is enough; bounded degree is unnecessary

The natural order need not have bounded backward multiplicity. A weaker hereditary sparsity condition also suffices.

For a finite set \(F\subseteq\mathbb N\), let \(\mathcal H^+(b)[F]\) denote the induced hypergraph. Say \(\mathcal H^+(b)\) is **\(B\)-degenerate** if every nonempty finite induced subhypergraph contains a vertex of degree at most \(B\).

**Theorem 4.** If \(b_n\) is an injective bounded-step planar walk and \(\mathcal H^+(b)\) is \(B\)-degenerate, then \(b_n\) has a bounded-increment triple-free lift to \(\mathbb Z^3\).

**Proof.** Again put \(q=B+1\) and seek
\[
z_n=qn+c_n,\qquad c_n\in\{0,\dots,B\}.
\]

For each edge \(e=\{i,j,k\}\) of \(\mathcal H^+(b)\), collinearity of the corresponding lifted points is one nontrivial linear equation in \(z_i,z_j,z_k\), with all three coefficients nonzero. Hence, given the colors at any two vertices of an edge, at most one color is forbidden at the third.

First consider a finite induced hypergraph on \(F\). Repeatedly remove a vertex of degree at most \(B\), obtaining an elimination order. Color in the reverse order. When a vertex is colored, at most \(B\) edges have both their other vertices already colored. Each such edge forbids at most one color, while \(B+1\) colors are available. Therefore all constraints on \(F\) can be avoided.

It follows that every finite collection of the collinearity-avoidance constraints is satisfiable. Compactness of the product space
\[
\{0,\dots,B\}^{\mathbb N}
\]
then gives a simultaneous assignment avoiding every edge. The resulting heights are strictly increasing with increments in \(\{1,\dots,2B+1\}\). Lemma 1 completes the proof. \(\square\)

The unresolved planar lemma can therefore be weakened further:

> It would suffice to construct an injective bounded-step planar walk for which the hypergraph of forward-collinear triples has finite degeneracy.

I found no proof or counterexample to this statement.

---

### 4. A necessary obstruction: bounded-gap recurrence to a line

A large class of natural planar bases cannot work, regardless of how their heights are chosen.

**Lemma 5.** Let \(a_n=(b_n,z_n)\) be any bounded-step lift with \(b_n\) pairwise distinct. Suppose there is a planar affine line \(L\) and indices
\[
n_1<n_2<\cdots
\]
such that

1. \(b_{n_r}\in L\) for every \(r\);
2. \(n_{r+1}-n_r\le G\) for a fixed \(G\).

Then the lifted walk contains three collinear points.

**Proof.** All \(a_{n_r}\) lie in the affine plane
\[
P=L\times\mathbb R.
\]
Because \(L\) contains infinitely many lattice points, its direction is rational, and \(P\cap\mathbb Z^3\) is an affine rank-two lattice.

If the original step set is \(S\), then
\[
a_{n_{r+1}}-a_{n_r}
\]
is a sum of at most \(G\) elements of \(S\). Hence the subsequence \((a_{n_r})\) has a fixed finite step set. It is injective because the \(b_{n_r}\) are distinct. It is therefore an infinite bounded-step walk in a rank-two lattice. The Gerver–Ramsey planar theorem gives three collinear points in this subsequence. \(\square\)

For example, the ladder walk
\[
b_{2m}=(m,0),\qquad b_{2m+1}=(m,1)
\]
cannot be lifted successfully: the line \(y=0\) is visited every two steps.

Therefore a successful base must visit every line either finitely often or with unbounded gaps.

---

### 5. The obvious digital-linear lift always fails

A natural attempt is
\[
a_n=(n,\lfloor\alpha n\rfloor,\lfloor\beta n\rfloor).
\]
Its steps lie in a fixed finite set. Nevertheless it always has a three-term arithmetic progression under the generic rational-independence hypothesis.

**Lemma 6.** If \(1,\alpha,\beta\) are linearly independent over \(\mathbb Q\), then there exists \(n\) such that
\[
a_n+a_{n+2}=2a_{n+1}.
\]

**Proof.** Fix an irrational real number \(\theta\), write
\[
\theta=m+r,\qquad m\in\mathbb Z,\quad 0<r<1,
\]
and let \(x=\{n\theta\}\). The increment
\[
\lfloor(n+1)\theta\rfloor-\lfloor n\theta\rfloor
\]
equals \(m\) or \(m+1\), according to whether \(x<1-r\) or \(x\ge1-r\).

A direct calculation shows that two consecutive increments are equal precisely on the following nonempty open interval:
\[
I_\theta=
\begin{cases}
(0,\,1-2r),&0<r<\tfrac12,\\[2mm]
(2-2r,\,1),&\tfrac12<r<1.
\end{cases}
\]
The case \(r=\tfrac12\) cannot occur for irrational \(\theta\).

Since \(1,\alpha,\beta\) are rationally independent, Kronecker’s density theorem gives density of
\[
\bigl(\{n\alpha\},\{n\beta\}\bigr)
\]
in the two-torus. Hence, for some \(n\),
\[
\{n\alpha\}\in I_\alpha,\qquad
\{n\beta\}\in I_\beta.
\]
At this \(n\), both floor sequences have equal consecutive increments. The first coordinate always has increment \(1\). Therefore
\[
a_{n+1}-a_n=a_{n+2}-a_{n+1},
\]
which is the asserted three-term arithmetic progression. \(\square\)

For the concrete choice \(\alpha=\sqrt2,\beta=\sqrt3\), one can take \(n=5\):
\[
a_5=(5,7,8),\quad
a_6=(6,8,10),\quad
a_7=(7,9,12).
\]

Thus quasi-periodic digital straight lines do not provide the required lift.

---

### 6. Strict convexity cannot coexist with integer bounded increments

Another tempting idea is to use a strictly convex height coordinate, since points
\[
(n,*,f_n)
\]
cannot be collinear if \(f_n\) lies strictly below every chord.

**Lemma 7.** There is no integer sequence \(f_n\) with bounded increments satisfying
\[
f_{n+2}-2f_{n+1}+f_n>0
\qquad\text{for every }n.
\]

**Proof.** Put \(d_n=f_{n+1}-f_n\). The hypothesis says
\[
d_{n+1}>d_n.
\]
Since the \(d_n\) are integers,
\[
d_n\ge d_0+n.
\]
Thus the increments are unbounded. \(\square\)

Consequently, the most direct “curvature in one integer coordinate” mechanism is unavailable.

---

### 7. Naive independent centered heights almost surely fail

Route 4 suggests random increments, for example independent choices from \([-M,M]\). The atom at zero creates a rigorous obstruction.

**Lemma 8.** Fix a finite planar step set \(T\) and an infinite injective \(T\)-walk \(b_n\). Let
\[
z_{n+1}-z_n=\delta_n
\]
where the \(\delta_n\) are independent and
\[
\mathbb P(\delta_n=0)=\rho>0.
\]
Then almost surely the lifted walk \((b_n,z_n)\) contains three collinear points.

**Proof.** By the planar Gerver–Ramsey theorem and König compactness, there exists \(N=N(T)\) such that every injective \(T\)-walk of \(N\) vertices contains a planar collinear triple. Indeed, otherwise arbitrarily long planar triple-free \(T\)-walks would have an infinite triple-free branch.

Partition the base walk into disjoint blocks of \(N\) vertices. For each block, select one projected collinear triple. Let \(E_r\) be the event that all \(N-1\) height increments internal to the \(r\)-th block are zero. Then
\[
\mathbb P(E_r)=\rho^{N-1}>0,
\]
and the \(E_r\) are independent. Almost surely infinitely many \(E_r\) occur.

On \(E_r\), all lifted points in that block have the same height, so the selected planar collinear triple remains collinear in the corresponding horizontal plane. \(\square\)

This does not rule out carefully correlated or strictly positive random heights, but it eliminates the most direct i.i.d. experiment with increments in \([-M,M]\).

---

### 8. Precise point of blockage

Theorem 2 would settle the problem negatively if the following could be proved:

\[
\exists\,T\subseteq\mathbb Z^2\text{ finite},\ \exists B<\infty,\ 
\exists\text{ an infinite injective \(T\)-walk }b
\]
such that
\[
P_k^+(b)\le B\quad\text{for every }k.
\]

Theorem 4 shows that finite degeneracy of \(\mathcal H^+(b)\) is enough.

The planar Gerver–Ramsey theorem does not settle this auxiliary question. It forces unordered planar collinear triples in every sufficiently long fixed-\(T\) walk, but those triples may occur in the wrong chronological order and hence be automatically harmless under a strictly increasing height. Even if forward triples are unavoidable, the theorem gives no lower bound on their multiplicity or degeneracy.

I was unable either to construct such a sparse-forward-collinearity walk or to prove that none exists. Establishing its existence would essentially finish the disproof, while proving its impossibility appears to require a new ordered strengthening of the planar Gerver–Ramsey theorem. This is the decisive block.

## Self-Audit

1. **The central planar sparsity hypothesis is unproved.**  
   This is not a technical omission: without an infinite planar walk of bounded forward multiplicity or degeneracy, Theorems 2 and 4 do not resolve the problem. I believe the conditional lifting theorems themselves are correct because each projected triple forbids at most one height color, and all compactness and bounded-step details are explicit.

2. **The degeneracy argument uses infinite compactness.**  
   The possible concern is that independently colorable finite induced hypergraphs might not yield one global assignment. Here each constraint depends on only three coordinates and defines a closed cylinder condition in the compact product \(\{0,\dots,B\}^{\mathbb N}\). Every finite family is satisfiable by the elimination-order argument, so the finite intersection property applies.

3. **Several obstructions rely on the planar Gerver–Ramsey theorem and Kronecker density rather than reproving them.**  
   Gerver–Ramsey is part of the supplied brief, and Kronecker’s theorem is a standard exact density theorem under the stated rational-independence condition. The deductions from them—bounded-gap planar subsequences and simultaneous equal floor increments—are elementary and fully spelled out.

## Computations To Verify

The most valuable search is for a fixed planar step set \(T\) and fixed \(B\) admitting arbitrarily long injective paths with \(P_k^+\le B\).

```python
from typing import List, Tuple, Optional

P2 = Tuple[int, int]
P3 = Tuple[int, int, int]

def add2(a: P2, b: P2) -> P2:
    return (a[0] + b[0], a[1] + b[1])

def sub2(a: P2, b: P2) -> P2:
    return (a[0] - b[0], a[1] - b[1])

def det2(u: P2, v: P2) -> int:
    return u[0] * v[1] - u[1] * v[0]

def dot2(u: P2, v: P2) -> int:
    return u[0] * v[0] + u[1] * v[1]

def forward_pair_count(path: List[P2], q: P2) -> int:
    """
    Number of i<j<k, with q the proposed kth point, for which
    q-path[j] is a positive scalar multiple of path[j]-path[i].
    Assumes q is not already in path.
    """
    k = len(path)
    ans = 0
    for i in range(k):
        for j in range(i + 1, k):
            u = sub2(path[j], path[i])
            v = sub2(q, path[j])
            if det2(u, v) == 0 and dot2(u, v) > 0:
                ans += 1
    return ans

def search_planar_base(
    T: List[P2], B: int, target: int
) -> Optional[List[P2]]:
    path = [(0, 0)]
    used = {(0, 0)}

    def dfs() -> Optional[List[P2]]:
        if len(path) == target:
            return path.copy()

        candidates = []
        for s in T:
            q = add2(path[-1], s)
            if q in used:
                continue
            pcount = forward_pair_count(path, q)
            if pcount <= B:
                candidates.append((pcount, q))

        # Heuristic: first try candidates creating fewer forward triples.
        candidates.sort(key=lambda x: x[0])

        for _, q in candidates:
            path.append(q)
            used.add(q)
            result = dfs()
            if result is not None:
                return result
            used.remove(q)
            path.pop()

        return None

    return dfs()

# Suggested initial step sets:
T4 = [(1,0), (-1,0), (0,1), (0,-1)]
T8 = [
    (x,y)
    for x in (-1,0,1)
    for y in (-1,0,1)
    if (x,y) != (0,0)
]

# Example:
# path = search_planar_base(T8, B=2, target=100)
# print(path)
```

If such a planar prefix is found, the height colors from Theorem 2 can be constructed exactly as follows.

```python
def cross3(u: P3, v: P3) -> P3:
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def sub3(a: P3, b: P3) -> P3:
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def collinear3(a: P3, b: P3, c: P3) -> bool:
    return cross3(sub3(b, a), sub3(c, a)) == (0, 0, 0)

def greedy_lift(path: List[P2], B: int) -> List[P3]:
    q = B + 1
    lifted: List[P3] = []

    for k, b in enumerate(path):
        chosen = None
        for color in range(q):
            candidate = (b[0], b[1], q*k + color)
            bad = False
            for i in range(k):
                for j in range(i + 1, k):
                    if collinear3(lifted[i], lifted[j], candidate):
                        bad = True
                        break
                if bad:
                    break
            if not bad:
                chosen = candidate
                break

        if chosen is None:
            raise AssertionError(
                "No color found: either P_k^+ > B or there is a bug."
            )
        lifted.append(chosen)

    return lifted
```

To measure the weaker degeneracy criterion:

```python
def forward_edges(path: List[P2]):
    edges = []
    n = len(path)
    for i in range(n):
        for j in range(i + 1, n):
            u = sub2(path[j], path[i])
            for k in range(j + 1, n):
                v = sub2(path[k], path[j])
                if det2(u, v) == 0 and dot2(u, v) > 0:
                    edges.append((i, j, k))
    return edges

def hypergraph_degeneracy(n: int, edges) -> int:
    remaining = set(range(n))
    degeneracy = 0

    while remaining:
        active_edges = [
            e for e in edges if all(v in remaining for v in e)
        ]
        degree = {v: 0 for v in remaining}
        for e in active_edges:
            for v in e:
                degree[v] += 1

        v = min(remaining, key=lambda x: degree[x])
        degeneracy = max(degeneracy, degree[v])
        remaining.remove(v)

    return degeneracy
```

The digital-linear obstruction can be checked without floating-point arithmetic:

```python
from math import isqrt

def floor_n_sqrt_d(n: int, d: int) -> int:
    return isqrt(d * n * n)

def digital_point(n: int) -> P3:
    return (
        n,
        floor_n_sqrt_d(n, 2),
        floor_n_sqrt_d(n, 3),
    )

for n in range(100):
    a = digital_point(n)
    b = digital_point(n + 1)
    c = digital_point(n + 2)
    if tuple(a[r] + c[r] for r in range(3)) == \
       tuple(2*b[r] for r in range(3)):
        print("First 3-AP starts at", n, a, b, c)
        break

# Expected:
# First 3-AP starts at 5
# (5, 7, 8), (6, 8, 10), (7, 9, 12)
```

For any promising morphic planar base, the decisive computation should record:

1. maximum \(P_k^+\) over substitution levels;
2. degeneracy of \(\mathcal H^+\);
3. whether every newly appearing forward triple reduces to finitely many cross-block types;
4. exact greedy lift colors and the first actual lifted collinearity, if any.

## Route Diagnosis

**Proved ledger.**

- Strictly increasing heights make chronologically reversed projected triples harmless.
- Uniformly bounded backward forward-collinearity multiplicity gives a counterexample by a greedy \(B+1\)-color height assignment.
- Finite degeneracy of the forward-collinearity hypergraph also suffices, by finite elimination and compactness.
- Arbitrarily long fixed-\((T,B)\) planar prefixes would suffice by König’s lemma.
- Bounded-gap recurrence to a planar line makes every bounded-increment lift fail.
- Digital linear/quasiperiodic lifts \((n,\lfloor\alpha n\rfloor,\lfloor\beta n\rfloor)\) fail under rational independence.
- Strict discrete convexity cannot be maintained by a bounded-increment integer coordinate.
- I.i.d. height increments with a positive atom at zero almost surely fail.

**Plausible but unproved.**

- There may exist a fixed-step planar walk with bounded degeneracy, or bounded backward multiplicity, of forward-collinear triples.
- A substitution or hierarchical turning walk may be capable of ensuring that all forward triples are confined to finitely many local configurations.

**Dead ends.**

- Finite-width ladder bases fail by bounded-gap line recurrence.
- Quasiperiodic floor codings contain explicit arithmetic progressions.
- Direct strict-convexity constructions force unbounded increments.
- Naive centered random increments fail almost surely.
- The ordinary planar theorem alone does not control chronological orientation or multiplicity of its triples.

**Precise block.** Route 4 has been reduced to a new ordered planar extremal problem, but that problem remains unproved and appears comparable in difficulty to constructing the desired lift. The most promising fresh attempt is a fixed-\((T,B)\) search for long planar paths with bounded \(P_k^+\), followed by extraction of a substitution or finite-state invariant. On the affirmative side, one should seek an ordered strengthening of Gerver–Ramsey proving that the forward-collinearity hypergraph of every bounded-step planar walk has unbounded degeneracy; no such strengthening follows from the existing planar theorem.