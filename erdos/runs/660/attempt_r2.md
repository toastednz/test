STATUS: BLOCKED

## Result

The proposed local deletion recurrence cannot work as stated. I proved exact deletion bookkeeping, a full-dimensional low-degree deletion ordering, and a structural reduction showing that any fixed-gap counterexample would admit linearly many consecutive deletions of bounded-degree vertices without losing a single distance value. However, even the asymptotically sharp regular-pyramid family admits \(\Theta(n)\) consecutive degree-\(3\), distance-neutral deletions, and no set of one or two removable vertices destroys any distance value. Thus planarity and low degree alone do not supply the required recurrence. The remaining necessary statement is a global amortized rigidity theorem controlling long neutral deletion runs; proving it would essentially settle the original problem and remains unproved.

## Complete Argument

### 1. Heredity and dimension-preserving deletion

Let \(X=V(P)\).

#### Lemma 1.1: Convex position is hereditary

Every subset \(Y\subseteq X\) is in convex position.

**Proof.** For each \(x\in X\), since \(x\notin\operatorname{conv}(X\setminus\{x\})\), strict separation gives a vector \(u_x\) such that

\[
u_x\cdot x>u_x\cdot y\qquad(y\in X\setminus\{x\}).
\]

The same inequality holds after restricting to any subset containing \(x\). Hence every point of \(Y\) is exposed, and therefore a vertex of \(\operatorname{conv}Y\). ∎

Call \(v\in X\) **dimension-essential** if \(X\setminus\{v\}\) is coplanar.

#### Lemma 1.2: There is at most one dimension-essential vertex when \(|X|\ge5\)

**Proof.** Suppose distinct vertices \(v,w\) were both dimension-essential. Because \(X\setminus\{v\}\) contains at least four vertices in convex position, its affine hull cannot have dimension at most one; thus it lies in a plane \(H_v\). Similarly, \(X\setminus\{w\}\) spans a plane \(H_w\).

The planes cannot coincide, since then all of \(X\) would be coplanar. Therefore \(H_v\cap H_w\) is a line. Every point of \(X\setminus\{v,w\}\) lies on this line. There are at least three such points, so one lies between two others and is not extreme in \(\operatorname{conv}X\), contradicting that all points of \(X\) are vertices. ∎

#### Lemma 1.3: Every three-polytope has at least four vertices of degree at most \(5\)

**Proof.** Let \(G\) be its \(1\)-skeleton, with \(N\) vertices and \(E\) edges. By Steinitz’s theorem, \(G\) is planar and \(3\)-connected. Hence every degree is at least \(3\), and

\[
E\le 3N-6.
\]

Therefore

\[
\sum_{v\in V(G)}(6-\deg v)=6N-2E\ge12.
\]

A vertex of degree at least \(6\) contributes at most zero, while a vertex of degree \(3,4,\) or \(5\) contributes at most \(3\). Thus at least four vertices have degree at most \(5\). ∎

Combining Lemmas 1.2 and 1.3 gives:

#### Corollary 1.4: Low-degree deletion ordering

Every three-dimensional convex polytope can be successively reduced to a tetrahedron so that, at every step, the removed vertex:

1. has degree at most \(5\) in the current polytope; and
2. leaves a three-dimensional convex hull.

This holds for nonsimplicial and nonsimple polytopes as well.

---

### 2. Exact distance-deletion bookkeeping

For each distance \(d\in\Delta(P)\), let \(G_d\) be the graph on \(X\) whose edges are precisely the pairs at distance \(d\).

#### Lemma 2.1: Deletion and vertex covers

For any \(S\subseteq X\),

\[
D(P)-D(P-S)
=
\bigl|\{d\in\Delta(P):S\text{ is a vertex cover of }G_d\}\bigr|.
\]

Here \(P-S\) denotes the convex hull of \(X\setminus S\), provided at least two points remain.

**Proof.** The value \(d\) disappears after deleting \(S\) exactly when every pair at distance \(d\) has at least one endpoint in \(S\). This is precisely the assertion that \(S\) meets every edge of \(G_d\). ∎

For a vertex \(v\), write

\[
t(v)=D(P)-D(P-v).
\]

Thus \(t(v)\) is the number of distance graphs \(G_d\) whose every edge is incident with \(v\).

#### Lemma 2.2: Private-distance bound

If \(s=D(P)\), then

\[
\sum_{v\in X}t(v)\le 2s.
\]

Consequently at least \(n-2s\) vertices satisfy \(t(v)=0\).

**Proof.** Fix a distance \(d\).

- If \(G_d\) has a single edge \(xy\), then deleting either \(x\) or \(y\) destroys \(d\), so this distance contributes \(2\) to \(\sum_v t(v)\).
- If \(G_d\) has at least two edges and all of them share a common endpoint, that common endpoint is unique, so \(d\) contributes \(1\).
- Otherwise \(d\) contributes \(0\).

Thus every distance contributes at most \(2\), proving the first assertion. Since every vertex with \(t(v)>0\) contributes at least \(1\), there are at most \(2s\) such vertices. ∎

This is a purely combinatorial bound. It does not exploit convexity, and regular pyramids show it cannot by itself prove the conjecture: in those examples \(t(v)=0\) for every vertex once the base is sufficiently large.

---

### 3. A full-dimensional distance kernel

#### Lemma 3.1: Distance-kernel lemma

Every three-dimensional \(n\)-vertex polytope with \(s\) distances has a subset \(W\subseteq V(P)\) such that

\[
|W|\le 2s+2,\qquad
\dim\operatorname{conv}W=3,\qquad
\Delta(W)=\Delta(P).
\]

**Proof.** For every distance \(d\in\Delta(P)\), choose one pair \(\{x_d,y_d\}\) realizing \(d\), and let \(U\) be the union of all chosen endpoints. Then

\[
|U|\le 2s
\]

and every distance in \(\Delta(P)\) is already realized within \(U\). Since \(U\subseteq V(P)\),

\[
\Delta(U)=\Delta(P).
\]

The set \(U\) contains at least two distinct points, so its affine dimension is at least \(1\). Since \(V(P)\) spans dimension \(3\), at most two additional vertices can be adjoined to obtain a set \(W\) of affine dimension \(3\). Adding them introduces no distance outside \(\Delta(P)\), while all original distance values remain represented by the selected pairs in \(U\). Thus \(\Delta(W)=\Delta(P)\) and \(|W|\le2s+2\). By Lemma 1.1, every member of \(W\) remains a vertex. ∎

This shows that if \(2s\le(1-\varepsilon)n\), at least \(\varepsilon n-O(1)\) vertices can be deleted simultaneously without changing the distance set or losing full dimension.

---

### 4. What a fixed-gap counterexample would have to contain

The distance kernel can be combined with planar graph degree bounds.

#### Theorem 4.1: Bounded-degree neutral peeling

Fix \(0<\varepsilon\le1\), and put

\[
K=\left\lceil\frac{16}{\varepsilon}\right\rceil.
\]

Suppose \(P\) has \(n\) vertices and \(s=D(P)\) with

\[
2s\le(1-\varepsilon)n.
\]

For all sufficiently large \(n\), there are nested full-dimensional polytopes

\[
P=P_0\supset P_1\supset\cdots\supset P_L,
\qquad
L=\left\lfloor\frac{\varepsilon n}{4}\right\rfloor,
\]

such that, for every \(0\le r<L\),

1. \(P_{r+1}\) is obtained by deleting one vertex \(v_r\) from \(P_r\);
2. \(v_r\) has degree at most \(K\) in the \(1\)-skeleton of \(P_r\);
3. \(D(P_{r+1})=D(P_r)=s\).

**Proof.** Choose a full-dimensional distance kernel \(W\) as in Lemma 3.1. Then

\[
|W|\le2s+2\le(1-\varepsilon)n+2.
\]

We retain \(W\) throughout the deletion process.

After \(r<L\) deletions, the current polytope has \(N=n-r\) vertices, of which at least

\[
N-|W|
\ge n-r-(2s+2)
\ge \varepsilon n-r-2
> \frac{3\varepsilon n}{4}-2
\]

lie outside \(W\).

The current \(1\)-skeleton is planar. Hence its total degree is at most \(6N-12<6n\). Therefore the number of vertices of degree greater than \(K\) is less than

\[
\frac{6n}{K+1}<\frac{3\varepsilon n}{8}.
\]

For \(n>16/(3\varepsilon)\),

\[
\frac{3\varepsilon n}{4}-2>\frac{3\varepsilon n}{8}.
\]

Thus some vertex outside \(W\) has degree at most \(K\). Delete it. Since \(W\) remains, the new hull is still three-dimensional and still realizes every distance in \(\Delta(P)\). By heredity, all remaining points are vertices.

The same argument applies at every one of the first \(L\) stages. ∎

Thus a disproof with a fixed gap below \(n/2\) cannot merely have occasional distance-redundant vertices. It must contain a linear sequence of bounded-degree additions/deletions, none of which changes the global distance palette.

This is a genuine structural reduction, but it does not by itself lead to a contradiction.

---

### 5. The local recurrence is defeated by regular pyramids

The obstruction already occurs in the sharpness construction.

Let \(m=2q\ge6\). Let

\[
v_j=
\left(
R\cos\frac{2\pi j}{2q},
R\sin\frac{2\pi j}{2q},
0
\right),
\qquad 0\le j<2q,
\]

and let

\[
a=(0,0,\sqrt3R).
\]

The base chord with cyclic separation \(k\) has squared length

\[
c_k^2
=4R^2\sin^2\frac{\pi k}{2q},
\qquad 1\le k\le q.
\]

These \(q\) values are pairwise distinct. Moreover,

\[
\|a-v_j\|^2=R^2+3R^2=4R^2=c_q^2.
\]

Hence the resulting pyramid \(P_q\) has

\[
n=2q+1,\qquad D(P_q)=q=\frac{n-1}{2}.
\]

All points are vertices, and the hull is three-dimensional.

#### Proposition 5.1: No one- or two-vertex deletion destroys a distance

For every \(S\subseteq V(P_q)\) with \(|S|\le2\),

\[
D(P_q-S)=D(P_q)=q.
\]

If \(S\) does not contain the apex, then \(P_q-S\) remains three-dimensional.

**Proof.** For \(1\le k<q\), the base pairs at chord separation \(k\) form a \(2\)-regular graph with \(2q\) edges. Deleting two base vertices removes at most four of these edges, so at least one remains.

For \(k=q\), the base pairs form the matching of \(q\) antipodal pairs. Deleting two base vertices destroys at most two matching edges, and \(q\ge3\), so at least one remains.

Thus every one of the \(q\) base chord values survives deletion of any two base vertices. If the apex is deleted, at most one base vertex is also deleted, and the same conclusion holds. Since all apex distances were already equal to \(c_q\), there were no further distance values.

If the apex remains, at least \(2q-2\ge4\) base vertices remain; any three distinct points on their circle are noncollinear. The resulting hull is therefore three-dimensional. ∎

Equivalently, every distance graph \(G_{c_k}\) in this family has vertex-cover number greater than \(2\). Thus no choice of one or two removable vertices produces the proposed \(+1\) recurrence.

There is a stronger sequential obstruction.

For \(3\le L\le2q\), let \(Q_L\) be the pyramid consisting of the apex and the consecutive base vertices

\[
v_0,v_1,\dots,v_{L-1}.
\]

The base distance labels are

\[
\left\{\min(d,2q-d):1\le d\le L-1\right\}.
\]

Therefore

\[
D(Q_L)=
\begin{cases}
q,&q\le L\le2q,\\[2mm]
L,&3\le L\le q.
\end{cases}
\]

Indeed, when \(L\ge q+1\), separations \(1,\dots,q\) all occur. For \(L=q\), the base supplies \(1,\dots,q-1\), while the apex supplies label \(q\). For \(L<q\), the base supplies \(1,\dots,L-1\), and the apex supplies the distinct label \(q\).

Consequently one may delete

\[
v_{2q-1},v_{2q-2},\dots,v_q
\]

—exactly \(q=\Theta(n)\) vertices—without losing any distance value. Every deleted vertex has degree \(3\) in the current pyramid.

Only after this linear neutral run do subsequent deletions begin destroying one distance at a time.

This refutes both of the following possible local lemmas:

1. every sufficiently large polytope has one or two removable vertices whose deletion destroys a distance;
2. distance-neutral deletion of bounded-degree vertices can occur only \(o(n)\) times.

Regular pyramids do satisfy the desired lower bound: more generally, any pyramid over a convex \(m\)-gon has at least \(\lfloor m/2\rfloor\) distances, by Altman’s planar theorem applied to its base. Thus the obstruction is compatible with the conjecture, but it demands a global rather than local amortization argument.

---

### 6. The exact missing statement

Take any low-degree deletion ordering supplied by Corollary 1.4:

\[
P_n\supset P_{n-1}\supset\cdots\supset P_4,
\]

where \(P_i\) has \(i\) vertices. Define

\[
\tau_i=D(P_i)-D(P_{i-1})\ge0,
\qquad 5\le i\le n.
\]

Let

\[
T=\sum_{i=5}^n\tau_i
   =D(P_n)-D(P_4),
\]

and let \(Z\) be the number of indices with \(\tau_i=0\). The number \(A\) of positive-decrement steps satisfies \(A\le T\), since the \(\tau_i\) are nonnegative integers. Hence

\[
n-4=Z+A\le Z+T.
\]

A theorem of the form

\[
Z\le T+o(n)
\tag{*}
\]

for some suitable low-degree deletion ordering would imply

\[
n-4\le2T+o(n)\le2D(P_n)+o(n),
\]

which is precisely the desired asymptotic lower bound.

Regular pyramids make \((*)\) essentially sharp: their initial neutral deletions must later be charged against distance-destroying deletions.

On the other hand, if

\[
2D(P_n)\le(1-\varepsilon)n,
\]

then for every deletion ordering,

\[
Z-T
=n-4-A-T
\ge n-4-2T
\ge n-4-2D(P_n)
\ge\varepsilon n-4.
\]

Thus any fixed-gap counterexample would violate \((*)\) by a linear amount. Establishing \((*)\) therefore requires exactly the kind of global geometric restriction missing from the present route. Planarity of the \(1\)-skeleton controls which vertices can be deleted, but the distance graphs \(G_d\) are complete-graph color classes and need not have any relation to local polyhedral degrees.

This is the precise block.

## Self-Audit

1. **The bounded-degree neutral-peeling theorem is only a necessary condition for a counterexample.** It gives no contradiction: regular pyramids themselves have long neutral degree-\(3\) runs. I believe the theorem is correct because the retained distance kernel simultaneously certifies full dimension and preservation of all distance values, while the bounded-degree choice follows directly from the planar degree sum.

2. **The regular-pyramid obstruction rules out local recurrence arguments, not every conceivable deletion induction.** A global classification could recognize a pyramid-like neutral run and finish by Altman’s theorem. The obstruction nevertheless holds exactly: every chord class retains an edge after any two base deletions, and the consecutive-deletion spectrum is computed combinatorially.

3. **The missing amortized inequality \(Z\le T+o(n)\) has no proof here.** It is not presented as a lemma. I regard it as the correct diagnosis because it would immediately imply the target, while every fixed-gap counterexample would force a linear violation. Proving it appears to require a new rigidity or charging principle of comparable strength to the original problem.

## Computations To Verify

The regular-pyramid claims can be checked using exact integer chord labels; no floating-point trigonometry is needed.

```python
from itertools import combinations

APEX = -1

def pyramid_spectrum(m, vertices):
    """
    m must be even.
    Label k means squared chord length
       4 R^2 sin^2(pi*k/m), 1 <= k <= m/2.
    Apex-base distances are assigned label m/2.
    """
    assert m % 2 == 0
    q = m // 2
    vertices = set(vertices)
    out = set()

    for x, y in combinations(vertices, 2):
        if x == APEX or y == APEX:
            out.add(q)
        else:
            d = (x - y) % m
            out.add(min(d, m - d))
    return frozenset(out)

def verify_two_deletion_obstruction(max_q=100):
    for q in range(3, max_q + 1):
        m = 2 * q
        V = list(range(m)) + [APEX]
        full = pyramid_spectrum(m, V)
        assert full == frozenset(range(1, q + 1))

        for r in (1, 2):
            for S in combinations(V, r):
                remaining = [v for v in V if v not in S]
                assert pyramid_spectrum(m, remaining) == full

def verify_long_neutral_run(max_q=100):
    for q in range(3, max_q + 1):
        m = 2 * q
        for L in range(3, m + 1):
            V = list(range(L)) + [APEX]
            actual = len(pyramid_spectrum(m, V))
            expected = q if L >= q else L
            assert actual == expected

        # q consecutive deletions, from 2q base vertices down to q,
        # are all distance-neutral.
        for L in range(2*q, q, -1):
            before = pyramid_spectrum(m, list(range(L)) + [APEX])
            after = pyramid_spectrum(m, list(range(L-1)) + [APEX])
            assert before == after

verify_two_deletion_obstruction()
verify_long_neutral_run()
print("Regular-pyramid checks passed.")
```

Exact verification of Lemma 2.2 for rational coordinates:

```python
from fractions import Fraction
from collections import defaultdict
from itertools import combinations

def sqdist(p, q):
    return sum((Fraction(a) - Fraction(b))**2 for a, b in zip(p, q))

def distance_classes(points):
    classes = defaultdict(list)
    for i, j in combinations(range(len(points)), 2):
        classes[sqdist(points[i], points[j])].append((i, j))
    return classes

def deletion_losses(points):
    classes = distance_classes(points)
    losses = [0] * len(points)

    for edges in classes.values():
        for v in range(len(points)):
            if all(i == v or j == v for i, j in edges):
                losses[v] += 1

    assert sum(losses) <= 2 * len(classes)
    return losses

# Example: rational square pyramid
pts = [
    (0, 0, 1),
    (1, 1, 0),
    (1, -1, 0),
    (-1, 1, 0),
    (-1, -1, 0),
]
print(distance_classes(pts))
print(deletion_losses(pts))
```

The missing global amortization claim can be searched on rational polytopes with SageMath. This dynamic program minimizes \(Z-T\) over low-degree, dimension-preserving deletion orderings.

```python
# SageMath pseudocode / executable with minor version-dependent
# adjustments to Polyhedron.vertex_graph().

from functools import lru_cache
from itertools import combinations

pts = [
    vector(QQ, (t, t*t, t*t*t))
    for t in range(1, 11)
]  # rational moment-curve example

def spectrum(mask):
    I = [i for i in range(len(pts)) if (mask >> i) & 1]
    return frozenset(
        sum((pts[i][k] - pts[j][k])**2 for k in range(3))
        for i, j in combinations(I, 2)
    )

def polyhedron_data(mask):
    I = [i for i in range(len(pts)) if (mask >> i) & 1]
    P = Polyhedron(vertices=[pts[i] for i in I])
    if P.dim() != 3:
        return None

    coord_to_index = {tuple(pts[i]): i for i in I}
    G = P.vertex_graph()
    degree = {}

    for vv in G.vertices(sort=False):
        i = coord_to_index[tuple(vv.vector())]
        degree[i] = G.degree(vv)

    return P, degree

@lru_cache(None)
def best_score(mask):
    """
    Minimum possible Z-T from this state down to a tetrahedron.
    A neutral deletion contributes +1.
    A deletion destroying d>0 values contributes -d.
    """
    N = mask.bit_count()
    if N == 4:
        data = polyhedron_data(mask)
        return 0 if data is not None else Infinity

    data = polyhedron_data(mask)
    if data is None:
        return Infinity

    P, degree = data
    S = spectrum(mask)
    ans = Infinity

    for i, deg in degree.items():
        if deg > 5:
            continue
        newmask = mask & ~(1 << i)
        if polyhedron_data(newmask) is None:
            continue

        dec = len(S) - len(spectrum(newmask))
        contribution = 1 if dec == 0 else -dec
        ans = min(ans, contribution + best_score(newmask))

    return ans

fullmask = (1 << len(pts)) - 1
print("minimum Z-T:", best_score(fullmask))
```

Useful finite searches are:

1. run the dynamic program on prisms, antiprisms, stacked rational polytopes, and rational cyclic polytopes;
2. search for families where the minimum possible \(Z-T\) grows linearly;
3. compute the distance graphs \(G_d\) and their vertex-cover numbers;
4. test whether long neutral runs force a large coplanar subset or a persistent universal apex.

A linear \(Z-T\) family with \(D/n<1/2-\delta\) would be a disproof; a linear \(Z-T\) family at ratio \(1/2+o(1)\), such as regular pyramids, is only an obstruction to overly local proofs.

## Route Diagnosis

**Proved lemmas**

- Convex position is hereditary under vertex deletion.
- At most one vertex can be dimension-essential when \(n\ge5\).
- Every three-polytope has at least four vertices of degree at most \(5\), yielding a full low-degree deletion ordering.
- Exact distance-loss/vertex-cover identity.
- \(\sum_v(D(P)-D(P-v))\le2D(P)\).
- Every distance set has a full-dimensional kernel of at most \(2D(P)+2\) vertices.
- A fixed-gap counterexample would admit \(\Omega_\varepsilon(n)\) consecutive bounded-degree, distance-neutral deletions.
- Regular pyramids admit \(\Theta(n)\) consecutive degree-\(3\), distance-neutral deletions, and no one- or two-vertex deletion loses a distance.

**Plausible but unproved**

- Some global deletion ordering may satisfy
  \[
  Z\le T+o(n),
  \]
  where \(Z\) counts neutral steps and \(T\) counts distance values lost with multiplicity over the ordering.
- Long neutral runs not supported by a large planar facet may force many distinct distances by a separate rigidity mechanism.
- A stability theorem might classify near-extremal neutral chains as asymptotically pyramidal or dihedral.

**Dead ends**

- **Immediate recurrence \(m_3(n)\ge m_3(n-2)+1\):** false as a deletion mechanism, even for arbitrarily large regular pyramids.
- **“Only \(o(n)\) neutral low-degree deletions”:** false; regular pyramids have \(n/2+O(1)\) such deletions.
- **Private-distance averaging:** too weak; regular pyramids can have no private distance at any vertex.
- **Distance kernel plus planar degree alone:** reduces a counterexample to bounded-degree neutral extensions but supplies no bound on how many such extensions are geometrically possible.
- **Local vertex-figure arguments:** the vertex figure has bounded size, while repetition of an incident distance is a global property of the complete distance graph.

The deletion route is therefore blocked at a precise global amortization/classification problem. A fresh attempt should either prove that neutral deletion chains with palette size \(s\) have at most \(2s+o(s)\) total vertices, or show that every long neutral chain produces a facet containing \(n-o(n)\) vertices, where Altman’s theorem applies. Without such a new geometric rigidity principle, low degree and planarity do not approach the required constant.