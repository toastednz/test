STATUS: BLOCKED

## Result

Route 1 does not currently reach the required classification. I prove a rigorous lower bound
\[
h(n)\ge
1+\left\lceil
\frac{\binom n2-n}{\lfloor 3n/2\rfloor}
\right\rceil
\qquad(n\ge3),
\]
using the degree-three bound for each distance graph together with the theorem that a planar diameter graph has at most \(n\) edges. This is only \(n/3+O(1)\), far short of the needed \(h(n)\ge n\). I also show that the coefficient \(3/2\) in the per-distance bound is genuinely sharp, even for arbitrarily large general-position sets, so no argument based only on bounding each distance multiplicity can close the factor-three gap. As a secondary consequence of the exact spectrum, every putative example with \(n\ge9\) must contain at least
\[
\frac{n(n-1)(n-8)}6
\]
pairs of equal-length disjoint segments. No upper bound strong enough to contradict this is obtained.

## Complete Argument

### 1. A sharp local bound for one distance class

For a distance \(r\), let \(G_r\) be the graph on \(P\) whose edges are pairs at distance \(r\).

#### Lemma 1
Every vertex of \(G_r\) has degree at most \(3\). Consequently,
\[
\mu_P(r)=|E(G_r)|\le \left\lfloor\frac{3n}{2}\right\rfloor.
\]

#### Proof
If \(p\in P\) had four distinct neighbors \(q_1,\dots,q_4\) in \(G_r\), then all four \(q_i\) would lie on the circle centered at \(p\) with radius \(r\), contradicting the assumption that no four points of \(P\) are concyclic. The edge bound follows from the handshaking lemma:
\[
2|E(G_r)|=\sum_{p\in P}\deg_{G_r}(p)\le 3n.
\]
\(\square\)

The coefficient \(3/2\) cannot be lowered using the two general-position assumptions alone.

#### Lemma 2
There are six points in general position for which one distance occurs exactly nine times. More generally, for every \(k\ge1\), there is a general-position set of \(6k\) points in which one distance occurs \(9k=3(6k)/2\) times.

#### Proof
Let
\[
E=\{a_0,a_1,a_2\}
\]
be the vertices of an equilateral triangle of side \(1\). For \(t\in S^1\), consider
\[
P_t=E\cup(E+t).
\]
The three edges within each copy of \(E\), together with the three pairs
\[
\{a_i,a_i+t\},\qquad i=0,1,2,
\]
give nine unit pairs.

We show that for all but finitely many \(t\in S^1\), the six points are distinct, no three are collinear, and no four are concyclic.

Distinctness fails only when \(t=a_i-a_j\), giving finitely many possibilities.

For collinearity, a triple contained in one copy of \(E\) is noncollinear. A mixed triple has either two fixed points and one translated point, or vice versa. Its collinearity determinant is a nonzero affine function of \(t\), and hence has at most two zeros on \(S^1\).

For concyclicity:

- A quadruple with three points from one triangle and one from the other is concyclic only when the remaining translated point belongs to the fixed circumcircle of \(E\). As \(t\) varies on \(S^1\), that point moves on a unit circle whose center is a vertex of \(E\). This unit circle is not the circumcircle of \(E\), whose radius is \(1/\sqrt3\), so there are at most two bad values of \(t\).

- For a quadruple having two points from each copy, regard the two selected pairs as unit segments. If the two segments are parallel, their four endpoints form a translated parallelogram; it is cyclic only when it is a rectangle, which imposes one linear condition on \(t\). If the segment directions are different, their perpendicular bisectors meet in a unique point. The four endpoints are cyclic precisely when that intersection has equal distances from the two segment midpoints. This again imposes a nontrivial algebraic condition on \(t\), with only finitely many points on \(S^1\).

Thus only finitely many \(t\) are bad. Choose any other \(t\). The resulting \(P_t\) is in general position and has at least nine unit pairs. By Lemma 1, it has at most nine, hence exactly nine.

For \(k>1\), take \(k\) congruent copies of such a six-point configuration. Place them inductively sufficiently far apart that all inter-copy distances exceed \(1\). At each placement, avoid the finitely many proper algebraic loci on the translation parameter where a mixed collinear triple or mixed concyclic quadruple occurs. These loci cannot cover an open set, so a sufficiently distant admissible placement exists. The unit-distance graph is then the disjoint union of the \(k\) nine-edge unit-distance graphs, and has \(9k\) edges. \(\square\)

Thus the estimate in Lemma 1 is asymptotically and exactly sharp along \(n\equiv0\pmod 6\).

---

### 2. The diameter class is smaller

We next prove the classical planar diameter bound self-containedly.

#### Lemma 3: Convex chord lemma
Let \(X\) be \(h\) points in strictly convex position. If \(\mathcal F\) is a family of segments with endpoints in \(X\) such that every two members of \(\mathcal F\) meet, either at a common endpoint or at a proper crossing, then
\[
|\mathcal F|\le h.
\]

#### Proof
We induct on \(h\). If some vertex has degree at most \(1\) in the graph formed by \(\mathcal F\), delete that vertex and its at most one incident segment. Induction gives
\[
|\mathcal F|\le (h-1)+1=h.
\]

It remains to consider the case in which every vertex has degree at least \(2\). We claim that no vertex can have degree at least \(3\). Suppose \(v\) has three neighbors \(a,b,c\), occurring in that order around the boundary after \(v\). Since \(b\) has degree at least \(2\), it has an incident edge \(bw\) with \(w\ne v\).

For \(bw\) to cross \(va\), the endpoint \(w\) must lie in the boundary arc from \(v\) to \(a\) not containing \(b\). For \(bw\) to cross \(vc\), it must lie in the boundary arc from \(c\) to \(v\) not containing \(b\). These arcs are disjoint. The exceptional choices \(w=a\) or \(w=c\) also fail to meet one of \(vc\) or \(va\), respectively. This contradicts the pairwise-meeting property.

Therefore every vertex has degree exactly \(2\). By the handshaking lemma,
\[
2|\mathcal F|=2h,
\]
so \(|\mathcal F|=h\). \(\square\)

#### Lemma 4: Diameter bound
Among \(n\) planar points with no three collinear, at most \(n\) pairs realize the diameter.

#### Proof
Let the diameter be \(D\).

First, every endpoint of a diameter pair is a vertex of the convex hull. Indeed, if
\[
a=\sum_i\lambda_i v_i,\qquad \lambda_i>0,\quad \sum_i\lambda_i=1
\]
were a nontrivial convex combination of other points, then for a diameter neighbor \(b\),
\[
D=\|a-b\|
=\left\|\sum_i\lambda_i(v_i-b)\right\|
\le\sum_i\lambda_i\|v_i-b\|
\le D.
\]
Equality in the strict triangle inequality forces all vectors \(v_i-b\) with positive coefficient to be identical, contrary to the combination being nontrivial.

Second, any two diameter segments meet. Suppose two diameter segments \(AB\) and \(CD\), with four distinct endpoints, did not meet. Their endpoints are in convex position, and the two segments are opposite sides of the resulting convex quadrilateral. If \(AC\) and \(BD\) are its diagonals and \(O\) is their intersection, then
\[
AB<AO+OB,\qquad CD<CO+OD,
\]
so
\[
AB+CD<AC+BD.
\]
The left side is \(2D\), whereas each diagonal has length at most \(D\), a contradiction.

The diameter segments therefore form a pairwise-meeting family of chords on the convex hull. Lemma 3 gives at most \(h\le n\) of them. \(\square\)

---

### 3. The resulting lower bound for \(h(n)\)

#### Theorem 5
For every \(n\ge3\),
\[
h(n)\ge
1+\left\lceil
\frac{\binom n2-n}{\lfloor3n/2\rfloor}
\right\rceil.
\]

#### Proof
Let \(P\) be a general-position \(n\)-point set with \(m\) distinct distances. One distance is the diameter, and by Lemma 4 its multiplicity is at most \(n\). Each of the remaining \(m-1\) distances has multiplicity at most
\[
C_n=\left\lfloor\frac{3n}{2}\right\rfloor
\]
by Lemma 1. Hence
\[
\binom n2
=\sum_{r\in\Delta(P)}\mu_P(r)
\le n+(m-1)C_n.
\]
Rearranging and using integrality,
\[
m\ge
1+\left\lceil
\frac{\binom n2-n}{C_n}
\right\rceil.
\]
Taking the minimum over all \(P\) proves the result. \(\square\)

For example,
\[
h(9)\ge1+\left\lceil\frac{36-9}{13}\right\rceil=4.
\]
Asymptotically, however, Theorem 5 gives only
\[
h(n)\ge \frac n3+O(1).
\]
The desired Route 1 conclusion would be \(h(n)\ge n\), so a factor of approximately three remains.

Lemma 2 shows why merely improving the multiplicity estimate for each individual distance cannot solve this: the upper bound \(3n/2\) is attained in general position for arbitrarily large \(n\). A successful Route 1 proof must therefore control several distance classes simultaneously.

---

### 4. Perpendicular bisectors and isosceles triangles

The general-position assumptions also give a useful exact structural fact.

#### Lemma 6
Distinct pairs of points of \(P\) have distinct perpendicular bisectors.

#### Proof
Suppose distinct pairs \(\{a,b\}\) and \(\{c,d\}\) had the same perpendicular bisector \(L\). They cannot share exactly one endpoint, since reflection in \(L\) would send that endpoint to both of the other endpoints. Thus the four points are distinct.

Choose coordinates in which \(L\) is the \(x\)-axis. Then
\[
a=(u,v),\quad b=(u,-v),\qquad
c=(w,z),\quad d=(w,-z),
\]
with \(v,z\ne0\).

If \(u=w\), at least three of the points lie on the vertical line \(x=u\), contradicting no three collinear.

If \(u\ne w\), choose \(h\) satisfying
\[
(u-h)^2+v^2=(w-h)^2+z^2.
\]
This is a linear equation in \(h\) and has a unique solution. The circle centered at \((h,0)\) through \(a,b\) then also passes through \(c,d\), contradicting no four concyclic. \(\square\)

Let
\[
A(P)=
\sum_{r\in\Delta(P)}
\sum_{p\in P}\binom{\deg_{G_r}(p)}2.
\]
This counts equal-length edge pairs sharing a vertex, with an equilateral triangle contributing three.

#### Lemma 7
\[
A(P)\le 2\binom n2=n(n-1).
\]

#### Proof
Fix a possible base pair \(\{q,s\}\). An apex \(p\) satisfying
\[
\|p-q\|=\|p-s\|
\]
must lie on the perpendicular bisector of \(qs\). Since no three points of \(P\) are collinear, this line contains at most two points of \(P\). Summing over all \(\binom n2\) bases proves the claim. \(\square\)

---

### 5. Consequence for a hypothetical target-spectrum configuration

Assume now that the multiplicity spectrum is \(1,2,\dots,n-1\). Let \(Q\) count unordered pairs of distinct edges of \(K_n\) having equal length. Then
\[
Q=\sum_r\binom{\mu_P(r)}2
=\sum_{i=1}^{n-1}\binom i2
=\binom n3.
\]

Split \(Q=A+B\), where \(A\) counts equal edge pairs sharing a vertex and \(B\) counts equal disjoint edge pairs. Lemma 7 gives
\[
B\ge \binom n3-n(n-1)
=\frac{n(n-1)(n-8)}6.
\]

Thus:

#### Corollary 8
Every hypothetical target-spectrum configuration with \(n\ge9\) contains at least
\[
\frac{n(n-1)(n-8)}6
\]
unordered pairs of equal-length disjoint segments.

For \(n=9\), at least \(12\) such pairs are required.

There is also a simple upper bound per four-point subset.

#### Lemma 9
Among four points in general position with no four concyclic, at most two of
\[
AB=CD,\qquad AC=BD,\qquad AD=BC
\]
can hold.

#### Proof
Suppose all three hold. Choose the largest of the three common lengths and relabel so that
\[
AD=BC
\]
is that largest length. Then \(AD\) and \(BC\) are diameter segments of the four-point set, so by the argument in Lemma 4 they cross. Hence the convex boundary order is \(A,B,D,C\).

In this quadrilateral,
\[
AB=DC,\qquad BD=CA,
\]
so both pairs of opposite sides are equal. It is therefore a parallelogram. Its diagonals \(AD\) and \(BC\) are also equal, so it is a rectangle. The four points are consequently concyclic, contrary to hypothesis. \(\square\)

Hence
\[
B\le2\binom n4.
\]
Unfortunately,
\[
\frac{n(n-1)(n-8)}6\le2\binom n4
\]
for all relevant \(n\), so this does not yield a contradiction.

For completeness, the spectrum itself also forces a lower bound on \(A\). In a graph with \(i\) edges and degrees \(d_v\),
\[
\sum_v\binom{d_v}{2}\ge\max(0,2i-n),
\]
because \(\binom d2\ge d-1\). Therefore
\[
A\ge\sum_{i=1}^{n-1}\max(0,2i-n)
=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
\]
This remains far below the geometric upper bound \(n(n-1)\).

## Self-Audit

1. **The generic-placement argument in Lemma 2 is the least explicit part.**  
   In particular, the mixed two-old/two-new concyclicity condition must define a proper algebraic locus rather than the entire translation plane. It is proper because two fixed segments are not concyclic in every relative translation: using their perpendicular bisectors, one can translate the second midpoint along its segment direction while keeping the bisectors incident, and equality of the two resulting radii holds for at most two parameter values. Thus each forbidden locus has empty interior.

2. **The diameter theorem depends critically on the convex chord lemma.**  
   The potentially delicate step is that if \(v\) has neighbors \(a,b,c\) in cyclic order, a second edge at \(b\) cannot meet both \(va\) and \(vc\). This follows directly from the alternating-endpoint criterion for crossing chords of a convex polygon: the two required locations for its other endpoint lie in disjoint boundary arcs.

3. **The moment argument gives only a necessary condition, not an obstruction.**  
   The lower bound on equal disjoint segments is rigorous, but the available upper bound is of order \(n^4\), whereas the forced count is only of order \(n^3\). I do not claim this approaches a contradiction; it identifies precisely where Route 2 would need a substantially stronger geometric estimate.

## Computations To Verify

The following exact SymPy program checks a concrete six-point triangular-prism instance with
\[
t=\left(\frac35,\frac45\right).
\]
It verifies all collinearity and concyclicity determinants and counts unit pairs.

```python
import sympy as sp
from itertools import combinations
from collections import defaultdict

s = sp.sqrt(3)
t = sp.Matrix([sp.Rational(3,5), sp.Rational(4,5)])

E = [
    sp.Matrix([0, 0]),
    sp.Matrix([1, 0]),
    sp.Matrix([sp.Rational(1,2), s/2]),
]
P = E + [p + t for p in E]

def is_zero(expr):
    return sp.simplify(expr) == 0

def col_det(indices):
    M = sp.Matrix([
        [P[i][0], P[i][1], 1] for i in indices
    ])
    return sp.simplify(M.det())

def cyc_det(indices):
    M = sp.Matrix([
        [
            sp.expand(P[i][0]**2 + P[i][1]**2),
            P[i][0], P[i][1], 1
        ]
        for i in indices
    ])
    return sp.simplify(M.det())

bad_triples = [
    (I, col_det(I))
    for I in combinations(range(6), 3)
    if is_zero(col_det(I))
]

bad_quads = [
    (I, cyc_det(I))
    for I in combinations(range(6), 4)
    if is_zero(cyc_det(I))
]

assert not bad_triples, bad_triples
assert not bad_quads, bad_quads

sqdist = {}
for i, j in combinations(range(6), 2):
    d = sp.simplify(sum((P[i][k] - P[j][k])**2 for k in range(2)))
    sqdist[(i, j)] = d

unit_pairs = [e for e, d in sqdist.items() if is_zero(d - 1)]
assert len(unit_pairs) == 9, unit_pairs

print("All general-position checks passed.")
print("Unit pairs:", unit_pairs)
print("Squared distances:", sqdist)
```

The convex chord lemma can be checked combinatorially for small \(h\) by finding the largest clique in the chord-intersection graph:

```python
import networkx as nx
from itertools import combinations

def between(a, b, x, n):
    # x is in the open clockwise arc from a to b
    dab = (b - a) % n
    dax = (x - a) % n
    return 0 < dax < dab

def chords_meet(e, f, n):
    a, b = e
    c, d = f
    if len({a, b, c, d}) < 4:
        return True
    return between(a, b, c, n) != between(a, b, d, n)

for n in range(3, 13):
    chords = list(combinations(range(n), 2))
    G = nx.Graph()
    G.add_nodes_from(chords)
    for e, f in combinations(chords, 2):
        if chords_meet(e, f, n):
            G.add_edge(e, f)
    omega = nx.algorithms.clique.graph_clique_number(G)
    assert omega <= n
    print(n, omega)
```

The lower bounds from Theorem 5 can be tabulated as follows:

```python
from math import comb, floor, ceil

def route1_lower_bound(n):
    C = floor(3*n/2)
    return 1 + ceil((comb(n, 2) - n) / C)

for n in range(3, 31):
    print(n, route1_lower_bound(n))
```

An exact checker for the adjacent/disjoint split in any proposed configuration is:

```python
def equal_pair_split(points):
    n = len(points)
    classes = defaultdict(list)

    for i, j in combinations(range(n), 2):
        d = sp.simplify(sum(
            (points[i][k] - points[j][k])**2 for k in range(2)
        ))
        classes[d].append((i, j))

    adjacent = 0
    disjoint = 0

    for edges in classes.values():
        for e, f in combinations(edges, 2):
            if set(e) & set(f):
                adjacent += 1
            else:
                disjoint += 1

    multiplicities = sorted(len(edges) for edges in classes.values())
    return multiplicities, adjacent, disjoint

# For a target example:
# mult, A, B = equal_pair_split(points)
# assert mult == list(range(1, len(points)))
# assert A + B == comb(len(points), 3)
# assert A <= len(points) * (len(points) - 1)
```

## Route Diagnosis

Route 1 succeeds only in giving a linear lower bound with leading constant \(1/3\). The local circle restriction yields \(\mu(r)\le3n/2\), and Lemma 2 shows this is sharp for arbitrarily large general-position sets. The diameter theorem improves only one distance class and therefore changes the lower bound by at most a constant. Perpendicular-bisector incidence counting likewise controls adjacent equal-edge pairs but leaves the dominant disjoint equal-segment contribution untouched.

The precise block is this: one needs a **collective** theorem saying that a decomposition of all \(\binom n2\) pairs into Euclidean distance graphs cannot have average class size near \(n/2\) or larger under the two general-position assumptions. None of the local constraints—maximum degree three, \(K_{2,3}\)-freeness, distinct perpendicular bisectors, or the diameter bound—provides such a theorem, and dense individual distance graphs genuinely occur.

A fresh attempt should therefore not seek a better universal bound on a single distance multiplicity. The most promising alternatives are:

1. bound the number of disjoint equal-segment pairs sharply enough to confront Corollary 8;
2. exploit algebraic dependencies between several distance classes through the Euclidean distance matrix or rigidity stresses;
3. enumerate \(n=9\) colorings satisfying the graph constraints and test exact realizability, looking for a reusable forbidden metric pattern.

At present the key Route 1 assertion \(h(n)\ge n\) remains an unproved statement of essentially the same difficulty as the stated open obstruction, so this route is BLOCKED.