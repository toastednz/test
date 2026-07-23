STATUS: BLOCKED

## Result

Route 1 yields several rigorous finite forcing gadgets, but not a uniform obstruction for arbitrary noncongruent triangles. I prove: (i) every non-equilateral triangle \(T\) has an explicitly derived right triangle \(R(T;d)\) such that \(T\) and \(R(T;d)\) admit a finite \(12\)-vertex NAE obstruction; (ii) the two isosceles triangle types occurring among vertices of a regular pentagon form a \(5\)-vertex obstruction; (iii) the scalene non-right triangle with angles \(\pi/7,2\pi/7,4\pi/7\) is individually unavoidable, via a regular-heptagon realization of the Fano plane; and (iv) any finite obstruction must have a \(2\)-shadow of chromatic number at least \(5\). The universal route is blocked because the useful gadgets rely on special metric coincidences. For the explicit generic-looking pair \((4,6,7)\), \((5,8,10)\), the natural deterministic completion propagation provably stops after one round.

## Complete Argument

### 1. Finite-obstruction equivalence

For fixed triangles \(T,U\), let \(\mathcal E\) be the family of all congruent copies of either triangle in the plane. For each \(e=\{p,q,r\}\in\mathcal E\), impose
\[
\operatorname{NAE}(\chi(p),\chi(q),\chi(r)).
\]

If every finite subfamily of these constraints is satisfiable, then the corresponding clopen subsets of
\[
\{0,1\}^{\mathbb R^2}
\]
have the finite intersection property. By Boolean compactness, equivalently compactness of this product, their total intersection is nonempty. Hence there is a coloring avoiding both triangles.

Therefore:

> No coloring avoids both \(T\) and \(U\) if and only if some finite collection of copies of \(T,U\) is already not 2-colorable.

This justifies Route 1, but does not construct the required obstruction.

---

### 2. A uniform completion gadget for a triangle and a derived right triangle

Let \(T\) have side lengths \(d,r,s\), where \(r\ne s\), and let \(\Delta>0\) be its area. Define
\[
X=\frac{|r^2-s^2|}{d},\qquad
Y=\frac{4\Delta}{d},\qquad
Z=\sqrt{2r^2+2s^2-d^2}.
\]

Since
\[
Z^2=X^2+Y^2,
\]
these are the side lengths of a nondegenerate right triangle, denoted \(R(T;d)\).

To verify the identity, place a segment \(AB\) of length \(d\) with midpoint \(M\), unit tangent vector \(e\), and unit normal \(n\). Put
\[
\xi=\frac{r^2-s^2}{2d},
\qquad
h=\frac{2\Delta}{d}.
\]
The points
\[
C_1=M+\xi e+hn,\qquad
C_2=M-\xi e+hn,\qquad
C_3=M+\xi e-hn
\]
are all completions of \(AB\) to a copy of \(T\): changing the sign of \(\xi\) swaps the distances \(r,s\), while changing the sign of \(h\) reflects the triangle.

Moreover,
\[
|C_1C_2|=2|\xi|=X,\qquad
|C_1C_3|=2h=Y,
\]
and
\[
|C_2C_3|^2=4(\xi^2+h^2)=2r^2+2s^2-d^2=Z^2.
\]
Thus \(\{C_1,C_2,C_3\}\) is congruent to \(R(T;d)\).

#### Finite obstruction

Take an equilateral triangle \(A_0A_1A_2\) of side \(d\). For each of its three edges \(A_iA_j\), add the three completion points \(C_1,C_2,C_3\) above. Include:

- the three copies \(\{A_i,A_j,C_k\}\) of \(T\);
- the copy \(\{C_1,C_2,C_3\}\) of \(R(T;d)\).

This gives at most \(12\) vertices and exactly \(12\) selected triangle constraints.

Suppose a coloring had no monochromatic selected copy of either \(T\) or \(R(T;d)\). Two vertices of the equilateral seed have the same color; say
\[
\chi(A_i)=\chi(A_j)=c.
\]
For each associated completion point \(C_k\), the triple
\[
\{A_i,A_j,C_k\}
\]
is a copy of \(T\). It cannot be monochromatic, so, because there are only two colors,
\[
\chi(C_1)=\chi(C_2)=\chi(C_3)=1-c.
\]
But these three points form a copy of \(R(T;d)\), now monochromatic, a contradiction.

Hence:

> **Completion-gadget theorem.**  
> If \(T\) has a side \(d\) for which its other two side lengths are unequal, then every plane 2-coloring contains a monochromatic copy of \(T\) or of the explicitly determined right triangle
> \[
> R(T;d)=
> \left(
> \frac{|r^2-s^2|}{d},
> \frac{4\Delta}{d},
> \sqrt{2r^2+2s^2-d^2}
> \right).
> \]
> This conclusion has a finite obstruction with at most \(12\) vertices.

Every non-equilateral triangle has such a choice of \(d\). For a scalene triangle every side works; for an isosceles but non-equilateral triangle, choose one of the equal sides as \(d\).

This does not solve the general problem because the second triangle produced by the construction is necessarily right.

---

### 3. Necessary structure of every finite obstruction

For a 3-uniform hypergraph \(H\), its \(2\)-shadow \(G(H)\) is the graph in which two vertices are adjacent whenever they occur together in some hyperedge.

#### Lemma

If \(G(H)\) is 4-colorable, then \(H\) is 2-colorable in the NAE sense.

#### Proof

Take a proper coloring
\[
f:V(H)\to\{1,2,3,4\}.
\]
Recolor vertices \(1,2\) red and vertices \(3,4\) blue. The three vertices of every hyperedge are pairwise adjacent in \(G(H)\), so they receive three distinct \(f\)-colors. Three distinct colors cannot all lie in \(\{1,2\}\) or all lie in \(\{3,4\}\). Therefore every hyperedge contains both red and blue. ∎

Consequently:

> Every finite obstruction for a pair of triangles has a \(2\)-shadow of chromatic number at least \(5\).

In particular, a gadget whose shadow is planar cannot work, by the Four Color Theorem. This rules out many naive constructions obtained by gluing triangle faces into a planar complex.

#### Five-vertex classification

A 3-uniform hypergraph on at most four vertices is always 2-colorable: split its vertices into two classes of size at most two.

On five vertices, a 3-uniform hypergraph is non-2-colorable if and only if it is \(K_5^{(3)}\), containing all ten triples. Indeed, for any three-element subset \(S\), color \(S\) red and its two-element complement blue. If the hypergraph is non-2-colorable, \(S\) itself must be an edge, since the blue class has fewer than three vertices. Thus every triple is an edge. The converse follows from the pigeonhole principle.

Hence any five-point geometric obstruction must have the property that every one of its ten triples is congruent to one of the two prescribed triangles.

---

### 4. The regular-pentagon obstruction

Let \(P_0,\dots,P_4\) be the vertices of a regular pentagon with side length \(s\), and let
\[
\varphi=\frac{1+\sqrt5}{2}.
\]
Its diagonals have length \(\varphi s\).

Every three-element subset of the five vertices has, up to cyclic permutation and reflection, one of the two gap patterns
\[
(1,1,3)\quad\text{or}\quad(1,2,2).
\]
Therefore every triangle determined by three pentagon vertices has one of the two side-length triples
\[
T_s=(s,s,\varphi s),
\qquad
U_s=(s,\varphi s,\varphi s).
\]
These are noncongruent.

Every 2-coloring of five vertices has a color class of size at least three. Those three vertices form a monochromatic copy of either \(T_s\) or \(U_s\). Thus:

> For every \(s>0\), the pair
> \[
> (s,s,\varphi s),\qquad (s,\varphi s,\varphi s)
> \]
> has a five-vertex finite obstruction.

By the preceding classification, this obstruction is smallest possible by number of vertices.

---

### 5. A non-right triangle that is individually unavoidable

Let \(P_0,\dots,P_6\) be the vertices of a regular heptagon, indexed modulo \(7\). Define seven triples
\[
L_i=\{P_i,P_{i+1},P_{i+3}\},
\qquad i\in\mathbb Z/7\mathbb Z.
\]

All seven triangles are congruent, since \(L_i\) is obtained from \(L_0\) by a rotation.

The index sets
\[
\{i,i+1,i+3\}
\]
form the Fano plane. Indeed, for \(D=\{0,1,3\}\), the six nonzero ordered differences between distinct elements of \(D\) are
\[
1,2,3,4,5,6 \pmod 7.
\]
Thus every unordered pair of vertices occurs in exactly one \(L_i\).

We now prove that the seven triples are not 2-colorable. Suppose otherwise, and let red be the smaller color class, of size \(r\le3\).

- If \(r\le2\), there are at least five blue vertices. Their at least
  \[
  \binom52=10
  \]
  blue pairs must lie among the seven lines. Since no line is monochromatic blue, a line contains at most two blue vertices and hence at most one blue pair. Seven lines cannot accommodate ten blue pairs, a contradiction.

- Let \(r=3\). If the three red vertices form a line, that line is monochromatic. Otherwise, their three pairs lie on three distinct lines, each containing two red vertices. These lines account for six red-line incidences. Every point lies on three lines, so the total number of red-line incidences is \(3\cdot3=9\). The remaining three incidences can meet at most three of the other four lines. Hence at least one line contains no red point and is monochromatic blue.

Thus some \(L_i\) is monochromatic.

If the circumradius is \(R\), the side lengths of \(L_i\) are
\[
2R\sin\frac{\pi}{7},\qquad
2R\sin\frac{2\pi}{7},\qquad
2R\sin\frac{3\pi}{7}.
\]
Its angles are
\[
\frac{\pi}{7},\qquad \frac{2\pi}{7},\qquad \frac{4\pi}{7},
\]
so it is scalene, obtuse, and non-right.

Therefore:

> Every 2-coloring of the plane contains a monochromatic congruent copy of the triangle with angles
> \[
> \pi/7,\ 2\pi/7,\ 4\pi/7
> \]
> at every prescribed scale.

This is a genuine Route 1 obstruction for one fixed non-right shape.

A related abstract gadget is obtained by deleting one Fano line \(L\). Every proper coloring of the remaining six lines must color all three vertices of \(L\) identically; otherwise the missing line would also be NAE and the full Fano plane would be properly colored. Conversely, coloring \(L\) red and its four-point complement blue properly colors the six remaining lines. Thus the Fano plane minus one line is an exact “force three terminals equal” NAE gadget. The unresolved difficulty is realizing a suitably flexible version using arbitrary prescribed triangle shapes.

---

### 6. A cyclic finite-gadget schema

More generally, let \(P_0,\dots,P_{n-1}\) be a regular \(n\)-gon. For finitely many triples
\[
D_1,\dots,D_k\subset\mathbb Z/n\mathbb Z,
\]
form the cyclic hypergraph with edges
\[
D_j+i,\qquad i\in\mathbb Z/n\mathbb Z,\ 1\le j\le k.
\]
If this finite hypergraph is not 2-colorable, then every plane coloring has a monochromatic triangle whose type is one of the congruence classes represented by the \(D_j\).

This follows simply by restricting the plane coloring to the regular \(n\)-gon. The pentagon and heptagon constructions above are the cases \(n=5\) and \(n=7\).

This schema is computationally useful, but it only produces triangles whose central angles are rational multiples of \(\pi\). It therefore does not cover arbitrary triangle parameters.

---

### 7. Exact failure of the simplest completion propagation on a generic pair

Consider
\[
T=(4,6,7),\qquad U=(5,8,10).
\]
Both are non-right and noncongruent.

For a triangle with sides \(d,r,s\), the monochromatic completion rectangle over a monochromatic base of length \(d\) has pair distances \(X,Y,Z\) satisfying
\[
X^2=\frac{(r^2-s^2)^2}{d^2},\qquad
Y^2=\frac{16\Delta^2}{d^2},\qquad
Z^2=2r^2+2s^2-d^2.
\]

For \(T=(4,6,7)\),
\[
16\Delta_T^2=2295,
\]
and the three choices of base give
\[
\begin{array}{c|ccc}
d & X^2 & Y^2 & Z^2\\ \hline
4 & 169/16 & 2295/16 & 154\\
6 & 121/4 & 255/4 & 94\\
7 & 400/49 & 2295/49 & 55
\end{array}
\]

For \(U=(5,8,10)\),
\[
16\Delta_U^2=6279,
\]
and
\[
\begin{array}{c|ccc}
d & X^2 & Y^2 & Z^2\\ \hline
5 & 1296/25 & 6279/25 & 303\\
8 & 5625/64 & 6279/64 & 186\\
10 & 1521/100 & 6279/100 & 78.
\end{array}
\]

The squared side lengths available to serve as another base are
\[
16,25,36,49,64,100.
\]
None appears in either table.

Therefore the following restricted propagation mechanism stops after one round for this pair:

1. obtain a monochromatic pair whose distance is a side of \(T\) or \(U\);
2. force all completion vertices to have the opposite color;
3. use a pair among those completion vertices as the base of another copy of \(T\) or \(U\).

This is not a proof that no finite obstruction exists. It is an exact counterexample to the hope that repeated monochromatic-base completion alone gives a uniform argument.

## Self-Audit

1. **The principal missing step is the whole arbitrary-parameter case.** The pentagon, heptagon, and completion gadgets occupy special algebraic families; nothing here proves that an arbitrary pair admits any comparable incidence pattern. I therefore mark the route blocked rather than claiming a solution.

2. **The “propagation stops” conclusion is deliberately narrow.** It only concerns propagation through monochromatic completion pairs whose distances must equal prescribed side lengths. More complicated SAT gadgets can exploit conditional NAE constraints even when no such equality occurs. The narrow claim itself is exact because all relevant squared distances were enumerated algebraically.

3. **Geometric coincidences between different books in the completion gadget were not classified.** They do not affect the proof: on the activated seed edge, its three completion points are internally distinct because \(r\ne s\) and \(\Delta>0\), and their colors are forced regardless of whether they coincide with points belonging to another attachment.

## Computations To Verify

The following code exhaustively checks the abstract pentagon, Fano, Fano-minus-line, and \(12\)-vertex completion gadgets.

```python
from itertools import combinations

def property_B(n, edges):
    edges = [tuple(e) for e in edges]
    for mask in range(1 << n):
        good = True
        for a, b, c in edges:
            ca = (mask >> a) & 1
            cb = (mask >> b) & 1
            cc = (mask >> c) & 1
            if ca == cb == cc:
                good = False
                break
        if good:
            return True
    return False

# K_5^(3): the regular-pentagon abstract obstruction
K5_3 = list(combinations(range(5), 3))
assert not property_B(5, K5_3)

# Fano plane as cyclic translates of {0,1,3}
D = (0, 1, 3)
fano = sorted({
    tuple(sorted((i + x) % 7 for x in D))
    for i in range(7)
})
assert len(fano) == 7
assert not property_B(7, fano)

# Fano minus one line is satisfiable but forces the missing line monochromatic
for missing in fano:
    remaining = [e for e in fano if e != missing]
    assert property_B(7, remaining)

    for mask in range(1 << 7):
        if all(
            not (((mask >> a) & 1) ==
                 ((mask >> b) & 1) ==
                 ((mask >> c) & 1))
            for a, b, c in remaining
        ):
            vals = [((mask >> v) & 1) for v in missing]
            assert vals[0] == vals[1] == vals[2]

# Abstract 12-vertex completion gadget:
# seed vertices 0,1,2; three apexes for each seed edge.
edges = []
next_vertex = 3
for u, v in [(0, 1), (1, 2), (2, 0)]:
    apex = [next_vertex, next_vertex + 1, next_vertex + 2]
    next_vertex += 3
    for a in apex:
        edges.append((u, v, a))       # a copy of T
    edges.append(tuple(apex))         # a copy of R(T;d)

assert next_vertex == 12
assert len(edges) == 12
assert not property_B(12, edges)
```

Exact verification of the completion-distance tables:

```python
from fractions import Fraction

def derived_right_data(sides, base_index):
    q = [Fraction(x) for x in sides]
    d = q[base_index]
    r, s = [q[i] for i in range(3) if i != base_index]

    d2, r2, s2 = d*d, r*r, s*s

    # 16 Delta^2
    area16 = (
        2*(d2*r2 + d2*s2 + r2*s2)
        - (d2*d2 + r2*r2 + s2*s2)
    )

    X2 = (r2 - s2)**2 / d2
    Y2 = area16 / d2
    Z2 = 2*r2 + 2*s2 - d2

    assert X2 + Y2 == Z2
    return X2, Y2, Z2

T = (4, 6, 7)
U = (5, 8, 10)

table_T = [derived_right_data(T, i) for i in range(3)]
table_U = [derived_right_data(U, i) for i in range(3)]

assert table_T == [
    (Fraction(169, 16), Fraction(2295, 16), Fraction(154)),
    (Fraction(121, 4), Fraction(255, 4), Fraction(94)),
    (Fraction(400, 49), Fraction(2295, 49), Fraction(55)),
]

assert table_U == [
    (Fraction(1296, 25), Fraction(6279, 25), Fraction(303)),
    (Fraction(5625, 64), Fraction(6279, 64), Fraction(186)),
    (Fraction(1521, 100), Fraction(6279, 100), Fraction(78)),
]

available_side_squares = {
    Fraction(x*x) for x in set(T + U)
}
for row in table_T + table_U:
    assert all(x not in available_side_squares for x in row)
```

A useful regular-polygon search for further one- and two-orbit obstructions is:

```python
from collections import defaultdict
from itertools import combinations

def chord_type(triple, n):
    ans = []
    for a, b in combinations(triple, 2):
        d = (a - b) % n
        ans.append(min(d, n - d))
    return tuple(sorted(ans))

def regular_polygon_orbits(n):
    groups = defaultdict(list)
    for tri in combinations(range(n), 3):
        groups[chord_type(tri, n)].append(tri)
    return groups

for n in range(5, 31):
    groups = regular_polygon_orbits(n)
    keys = list(groups)

    for key in keys:
        if not property_B(n, groups[key]):
            print("single orbit obstruction:", n, key)

    for k1, k2 in combinations(keys, 2):
        edges = groups[k1] + groups[k2]
        if not property_B(n, edges):
            print("two orbit obstruction:", n, k1, k2)
```

Any promising output should then be converted from chord indices \(k\) to exact side lengths
\[
2R\sin\frac{k\pi}{n}
\]
and independently checked for duplicate congruence types.

## Route Diagnosis

**Proved ledger**

- Pairwise avoidance is equivalent, pair by pair, to absence of a finite NAE obstruction.
- Every non-equilateral \(T\) has an explicit finite obstruction together with a derived right triangle \(R(T;d)\).
- Every finite obstruction has a \(2\)-shadow of chromatic number at least \(5\).
- The golden pair of pentagon isosceles triangles has a minimal five-vertex obstruction.
- The heptagon triangle with angles \(\pi/7,2\pi/7,4\pi/7\) is individually unavoidable.
- Fano-minus-one-line is an abstract gadget forcing three terminals to have the same color.
- Simple monochromatic-base propagation stalls exactly for the displayed pair \((4,6,7),(5,8,10)\).

**Plausible but unproved**

- A flexible geometric realization of an equality gadget such as Fano-minus-one-line, with its six clauses assigned to arbitrary \(T,U\), could settle the problem.
- A monochromatic right-triangle seed, supplied by Shader’s theorem, may make such a gadget geometrically realizable with fewer coincidences.
- Regular-polygon searches may reveal an abstract UNSAT core that admits a positive-dimensional deformation rather than only isolated rational-angle realizations.

**Dead ends or blocked mechanisms**

- Regular-polygon orbit gadgets only cover special rational-angle shapes and offer no evident deformation to arbitrary pairs.
- Gluing triangles as faces of a planar complex cannot work: its shadow is 4-colorable.
- Deterministic propagation from a monochromatic side pair produces only a right completion triangle; for generic pairs its new distances do not return to the original side set.
- Compactness does not advance the construction: asserting a finite obstruction for every pair is equivalent to the original problem.

The precise block is the absence of a parameter-uniform way to geometrically realize a non-property-B NAE hypergraph using arbitrary prescribed \(T,U\). A fresh Route 1 attempt should search specifically for **flexible** UNSAT frameworks—ones having enough continuous degrees of freedom to cover open sets of the six side parameters—rather than rigid regular-polygon or reflection-closure gadgets. The most promising controlled switch is Route 3: prescribe a monochromatic right-triangle seed, then search exact SAT closures for a deformable attachment pattern.