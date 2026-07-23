STATUS: BLOCKED

## Result

Route 2 yields a sharp rigorous criterion: if an optimal configuration has a non-diametral point whose unit-contact vectors do not positively span the plane, then that point moves along an actual finite feasible arc while a different pair preserves the optimal diameter; consequently \(h(n)=\infty\). More generally, an entire subset can be translated if its cross-contact vectors fail to positively span. Thus, if \(h(n)<\infty\), every boundary point of every optimizer must be a diameter endpoint, every interior point must be surrounded by at least three unit contacts, and every subset of non-diameter points must have cross-contact vectors positively spanning \(\mathbb R^2\). These are strong necessary conditions, but they are compatible with large jammed triangular-type frameworks. I found no argument forcing an optimal configuration to violate them for every sufficiently large \(n\). The route is therefore blocked at precisely the global existence of a rattler or flexible subframework in an exact optimizer.

## Complete Argument

### 1. A fixed-core rattler gives infinitely many minimizers

Let \(X\in\mathcal M_n\), let \(D=D_n\), and choose \(p\in X\). Put
\[
Y=X\setminus\{p\}
\]
and define the feasible region of \(p\) relative to the fixed core \(Y\) by
\[
R_p(X)=\left\{q\in\mathbb R^2:
1\le \|q-y\|\le D\quad\text{for every }y\in Y
\right\}.
\]

#### Lemma 1
Suppose \(Y\) contains a pair at distance \(D\). If \(p\) is a non-isolated point of \(R_p(X)\), then \(h(n)=\infty\).

#### Proof
For every \(q\in R_p(X)\), the set
\[
X_q=Y\cup\{q\}
\]
is feasible and has diameter at most \(D\). Since \(Y\) contains a pair at distance \(D\), its diameter is exactly \(D\). Therefore \(X_q\in\mathcal M_n\).

The set \(R_p(X)\) is bounded and semialgebraic. A non-isolated semialgebraic set has positive semialgebraic dimension and hence cardinality continuum.

It remains to show that these continuum many points do not collapse to finitely many congruence classes. Fix \(q_0\in R_p(X)\), and let \(S\) be the finite set of pairwise distances occurring in \(X_{q_0}\). If \(X_q\) is congruent to \(X_{q_0}\), then for every fixed \(y\in Y\),
\[
\|q-y\|\in S.
\]
Choose two distinct points \(y_1,y_2\in Y\). Thus \(q\) lies in
\[
\bigcup_{r_1,r_2\in S}
\bigl\{q:\|q-y_1\|=r_1,\ \|q-y_2\|=r_2\bigr\}.
\]
Each intersection of two circles with distinct centers has at most two points. Hence every congruence class meets the family \(\{X_q:q\in R_p(X)\}\) in only finitely many members. Since \(R_p(X)\) has cardinality continuum, there are continuum many congruence classes. Therefore \(h(n)=\infty\). ∎

This completely certifies the basic rattler mechanism, including the unordered-congruence issue.

---

### 2. Exact local criterion for a non-diameter point

For \(p\in X\), let
\[
C(p)=\{y\in X\setminus\{p\}:\|p-y\|=1\}
\]
be its contact neighbors. Define the cone
\[
K(p)=\left\{v\in\mathbb R^2:
(p-y)\cdot v\ge 0\quad\text{for all }y\in C(p)
\right\}.
\]

The contact vectors are said to positively span \(\mathbb R^2\) if
\[
\operatorname{cone}\{p-y:y\in C(p)\}=\mathbb R^2.
\]
By elementary polar-cone duality, this is equivalent to \(K(p)=\{0\}\).

#### Lemma 2
Let \(X\) be feasible of diameter \(D>1\), and suppose \(p\) is not an endpoint of any diameter pair. Then \(p\) is non-isolated in \(R_p(X)\) if and only if
\[
K(p)\ne\{0\}.
\]
Equivalently, \(p\) is locally fixed while all other points remain stationary if and only if its contact vectors positively span \(\mathbb R^2\).

#### Proof

**If \(K(p)\ne\{0\}\).**  
Choose \(0\ne v\in K(p)\). For any contact neighbor \(y\),
\[
\|p+tv-y\|^2
=1+2t(p-y)\cdot v+t^2\|v\|^2
\ge 1
\]
for every \(t\ge0\).

For every non-contact neighbor, the lower bound is initially strict. Because \(p\) is not a diameter endpoint, every upper bound involving \(p\) is also initially strict:
\[
1<\|p-y\|<D
\]
unless \(y\) is a contact neighbor, in which case \(1<D\). Since there are only finitely many points, continuity supplies \(\varepsilon>0\) such that
\[
1\le \|p+tv-y\|\le D
\]
for all \(y\ne p\) and \(0\le t\le\varepsilon\). Hence \(p\) is non-isolated.

**If \(K(p)=\{0\}\).**  
Let
\[
A=\{p-y:y\in C(p)\}.
\]
For every unit vector \(u\), some \(a\in A\) has \(a\cdot u<0\). Compactness of the unit circle and finiteness of \(A\) therefore give a constant \(c>0\) such that for every unit \(u\), some \(a\in A\) satisfies
\[
a\cdot u\le -c.
\]

Take any nonzero displacement \(w=ru\), where \(\|u\|=1\) and \(0<r<2c\). For the corresponding contact neighbor,
\[
\|p+w-y\|^2
=1+2r a\cdot u+r^2
\le 1-2cr+r^2<1.
\]
Thus no sufficiently small nonzero displacement of \(p\) is feasible. Hence \(p\) is isolated in \(R_p(X)\). ∎

#### Corollary 3
Let \(X\in\mathcal M_n\), \(n\ge4\), and let \(p\) not be a diameter endpoint. If the contact vectors at \(p\) fail to positively span \(\mathbb R^2\), then
\[
h(n)=\infty.
\]

#### Proof
Because \(p\) is not a diameter endpoint, every diameter pair of \(X\) lies in \(X\setminus\{p\}\). Lemma 2 gives a nontrivial arc in \(R_p(X)\), and Lemma 1 applies. ∎

In particular, an optimal non-diameter point with at most two contact neighbors is a rattler. Three contacts are necessary, though not sufficient: their directions must surround the point rather than lie in a closed semicircle.

---

### 3. Consequences for the convex hull

#### Lemma 4
Every endpoint of a diameter pair is an exposed vertex of the convex hull.

#### Proof
Suppose \(\|x-y\|=D=\operatorname{diam}(X)\). For any \(z\in X\),
\[
\|z-y\|^2\le D^2=\|x-y\|^2.
\]
Writing \(u=x-y\), this gives
\[
\|u+(z-x)\|^2\le \|u\|^2,
\]
and therefore
\[
2u\cdot(z-x)+\|z-x\|^2\le0.
\]
If \(z\ne x\), then
\[
u\cdot(z-x)<0.
\]
Thus the linear functional \(w\mapsto u\cdot w\) is uniquely maximized on \(X\), and hence on \(\operatorname{conv}(X)\), at \(x\). Therefore \(x\) is exposed. ∎

#### Lemma 5
Let \(X\in\mathcal M_n\), \(n\ge4\). If \(p\in X\cap\partial\operatorname{conv}(X)\) is not a diameter endpoint, then \(h(n)=\infty\).

#### Proof
There is a nonzero supporting vector \(v\) at \(p\) such that
\[
(p-y)\cdot v\ge0
\qquad\text{for every }y\in X.
\]
In particular, this holds for every contact neighbor. Hence \(v\in K(p)\setminus\{0\}\), and Corollary 3 applies. ∎

We consequently obtain the following strong necessary condition.

#### Theorem 6
If \(h(n)<\infty\) for some \(n\ge4\), then every optimal configuration \(X\in\mathcal M_n\) satisfies:

1. every point of \(X\cap\partial\operatorname{conv}(X)\) is a diameter endpoint;
2. every such boundary point is in fact an exposed hull vertex;
3. every non-hull point has at least three unit contacts whose contact vectors positively span \(\mathbb R^2\);
4. each non-hull point lies in the interior of the convex hull of its contact neighbors.

#### Proof
If a boundary point were not a diameter endpoint, Lemma 5 would give \(h(n)=\infty\). Thus every boundary point is a diameter endpoint and is exposed by Lemma 4.

Any non-hull point cannot be a diameter endpoint, again by Lemma 4. Corollary 3 therefore shows that its contact vectors must positively span \(\mathbb R^2\). At least three vectors are required to positively span the plane. Finally,
\[
0\in\operatorname{int}\operatorname{conv}\{p-y:y\in C(p)\}
\]
is equivalent, after translating and changing signs, to
\[
p\in\operatorname{int}\operatorname{conv}C(p).
\]
∎

Thus finite multiplicity forces a very rigid division: all upper-diameter constraints occur on the hull, while all interior points are trapped by surrounding unit contacts.

---

### 4. A collective translation criterion

The individual-point test extends to subframeworks.

Let \(S\subset X\) be nonempty. Orient every cross-contact from \(S\) to \(X\setminus S\), and set
\[
A_S=
\{x-y:x\in S,\ y\notin S,\ \|x-y\|=1\}.
\]

#### Lemma 7
Let \(X\in\mathcal M_n\). Suppose \(S\) contains no diameter endpoint. If
\[
\operatorname{cone}(A_S)\ne\mathbb R^2,
\]
then \(h(n)=\infty\).

#### Proof
Since the finitely generated cone \(\operatorname{cone}(A_S)\) is proper, there is a nonzero \(v\) satisfying
\[
a\cdot v\ge0\qquad(a\in A_S).
\]
Translate every point of \(S\) by \(tv\), leaving \(X\setminus S\) fixed.

Distances within \(S\) and within its complement do not change. For a cross-contact \(x,y\),
\[
\|x+tv-y\|^2
=1+2t(x-y)\cdot v+t^2\|v\|^2\ge1.
\]
All other cross lower bounds are initially strict. Since \(S\) contains no diameter endpoint, every cross upper bound is initially strict. Thus all inequalities remain valid for sufficiently small \(t>0\).

Every original diameter pair lies in \(X\setminus S\), so the diameter remains exactly \(D_n\).

Finally, the resulting configurations are not confined to finitely many congruence classes. For any cross pair \(x\in S,y\notin S\),
\[
\|x+tv-y\|^2
=\|x-y\|^2+2t(x-y)\cdot v+t^2\|v\|^2
\]
is a nonconstant quadratic polynomial in \(t\). In any fixed congruence class it could take only values from a fixed finite pairwise-distance set, and hence only finitely many \(t\) are possible. Therefore the arc contains continuum many congruence classes. ∎

#### Corollary 8
If \(h(n)<\infty\), then for every nonempty subset \(S\) containing no diameter endpoint,
\[
\operatorname{cone}(A_S)=\mathbb R^2.
\]
In particular, every such \(S\) has at least three cross-contact edges whose oriented directions are not contained in a closed semicircle.

This is a contact-cut condition resembling three-edge connectivity, but planar triangulated clusters can satisfy it.

---

### 5. Exact flexible families exist, but are not globally optimal

Let
\[
e_1=(1,0),\qquad e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\]
and for \(m\ge2\) define the triangular-lattice patch
\[
T_m=\{ie_1+je_2:i,j\ge0,\ i+j\le m\}.
\]
It has
\[
|T_m|=\frac{(m+1)(m+2)}2.
\]

All distinct lattice points have distance at least \(1\). Its convex hull is the equilateral triangle with vertices \(0,me_1,me_2\), so
\[
\operatorname{diam}(T_m)=m.
\]

Choose
\[
p=ke_1,\qquad 1\le k\le m-1.
\]
The point \(p\) is not a diameter endpoint: its distances to the three vertices are
\[
k,\qquad m-k,\qquad \sqrt{m^2-mk+k^2},
\]
all strictly smaller than \(m\). It lies on a supporting edge of the convex hull. Moving it a small distance directly outward from that edge increases its distances to its interior contact neighbors, while its distances to its two collinear contact neighbors increase quadratically. A fixed pair such as \(0,me_2\) continues to have distance \(m\). Lemma 5 therefore gives a continuum of feasible, pairwise incongruent configurations of the same diameter \(m\).

However these configurations are not optimal for sufficiently large \(m\). If
\[
n_m=\frac{(m+1)(m+2)}2,
\]
then the known asymptotic gives
\[
D_{n_m}
=\sqrt{\frac{2\sqrt3}{\pi}}\sqrt{n_m}+O(1)
=\sqrt{\frac{\sqrt3}{\pi}}\,m+O(1).
\]
Since
\[
\sqrt{\frac{\sqrt3}{\pi}}<1,
\]
we have \(D_{n_m}<m\) for all sufficiently large \(m\).

This is an exact illustration of the obstruction: producing rattlers at a prescribed diameter is easy; proving that diameter globally optimal is the entire difficulty.

---

### 6. Large feasible configurations need not have individual rattlers

A size-only rattler theorem is false, even locally.

For even \(m\ge4\), let \(P_m\) be a regular \(m\)-gon with side length \(1\). Its circumradius is
\[
R=\frac1{2\sin(\pi/m)}
\]
and its diameter is \(D=2R\).

Consider the vertex \(p=(R,0)\). Its two neighboring vertices are at angles \(\pm\theta\), where \(\theta=2\pi/m\), and its opposite vertex is \((-R,0)\). The active lower-constraint vectors are
\[
a_\pm
=R(1-\cos\theta,\mp\sin\theta),
\]
while the active upper-constraint vector is
\[
b=(2R,0).
\]
A first-order feasible displacement \(v=(v_x,v_y)\) must satisfy
\[
a_+\cdot v\ge0,\qquad a_-\cdot v\ge0,\qquad b\cdot v\le0.
\]
Adding the first two inequalities gives \(v_x\ge0\), while the last gives \(v_x\le0\). Thus \(v_x=0\). The first two inequalities then respectively imply \(v_y\le0\) and \(v_y\ge0\), so \(v=0\).

This zero tangent cone implies local isolation. Indeed, if feasible nonzero displacements \(w_j\to0\) existed, a convergent subsequence of \(w_j/\|w_j\|\) would give a nonzero vector satisfying the displayed linearized inequalities, a contradiction.

By symmetry, every vertex is locally isolated while the others are fixed. Thus arbitrarily large feasible configurations can have no individual rattler. These polygons are far from globally optimal—their diameter is of order \(m\), rather than order \(\sqrt m\)—but they disprove any purely cardinality-based version of Route 2.

---

### 7. The exact block

The preceding results would solve the problem affirmatively, and in fact prove \(h(n)=\infty\) eventually, if one could prove any one of the following for every sufficiently large \(n\):

1. some optimizer has a boundary point that is not a diameter endpoint;
2. some optimizer has a non-diameter point whose contact vectors do not positively span;
3. some optimizer has a nonempty subset of non-diameter points whose cross-contact vectors do not positively span;
4. more generally, some optimizer has a positive-dimensional fixed-diameter feasible component.

I could not prove any of these. Active-constraint counting does not force them: the contact graph can have nearly \(3n\) edges, the diameter graph can have \(n\) edges, and a planar triangulated interior can satisfy all the positive-spanning and cut conditions above. Moreover, the necessary conditions for avoiding rattlers are qualitatively aligned with dense packing: triangular local coordination traps interior points, while a disk-like hull may arrange every boundary point to have a diametral partner.

Consequently, the missing statement is not a routine rigidity lemma. It is an exact global theorem about the boundary and contact structure of at least one optimizer at every sufficiently large order, and appears comparable in difficulty to the original problem.

## Self-Audit

1. **The local criterion excludes diameter endpoints.**  
   This restriction is essential: an upper constraint active at \(p\) may block the ray even when the contact cone has a nonzero direction. The proof applies only when all upper constraints involving \(p\) are strict. I believe the statement as written is complete because this strictness is used explicitly.

2. **The passage from a rattler arc to infinitely many unordered congruence classes could conceal relabeling issues.**  
   The finite-distance-set argument avoids choosing labels under the congruence: any pairwise distance in a congruent configuration must belong to a fixed finite set, regardless of how vertices are permuted. Intersections of two fixed-center circles are finite, so relabeling cannot collapse a continuum.

3. **There is no theorem connecting the structural criteria to all large exact optimizers.**  
   This is not a gap being hidden as “routine”; it is the decisive missing step and the reason for the BLOCKED status. Density estimates, planarity, and active-constraint counts do not establish it, and the necessary no-rattler structure is compatible with highly coordinated disk-like packings.

## Computations To Verify

The following exploratory code detects the certified local and collective mechanisms on numerical candidate minimizers. Floating-point output is not a proof of exact contacts or exact diameter ties; promising cases must be rechecked with interval arithmetic or exact algebraic coordinates.

```python
import itertools
import numpy as np
from scipy.optimize import linprog
from scipy.spatial.distance import cdist

def cone_escape(vectors, tol=1e-10):
    """
    Find nonzero v with a·v >= 0 for all rows a.
    Homogeneity lets us impose one coordinate equal to +1 or -1.
    Returns v, or None if the vectors positively span R^2.
    """
    A = np.asarray(vectors, dtype=float)
    if len(A) == 0:
        return np.array([1.0, 0.0])

    for k in range(2):
        for s in (-1.0, 1.0):
            Aeq = np.zeros((1, 2))
            Aeq[0, k] = 1.0
            res = linprog(
                c=np.zeros(2),
                A_ub=-A,
                b_ub=np.zeros(len(A)),
                A_eq=Aeq,
                b_eq=np.array([s]),
                bounds=[(None, None), (None, None)],
                method="highs"
            )
            if res.success and np.min(A @ res.x) >= -tol:
                return res.x
    return None

def analyze_candidate(X, tol=1e-7, enumerate_subsets=True):
    """
    Detect non-diameter point rattlers and translational subframework rattlers.
    """
    X = np.asarray(X, dtype=float)
    n = len(X)
    d = cdist(X, X)
    np.fill_diagonal(d, np.nan)
    D = np.nanmax(d)

    contacts = set()
    diameter_edges = set()
    endpoints = set()

    for i in range(n):
        for j in range(i + 1, n):
            if abs(d[i, j] - 1.0) <= tol:
                contacts.add((i, j))
            if abs(d[i, j] - D) <= tol:
                diameter_edges.add((i, j))
                endpoints.add(i)
                endpoints.add(j)

    point_escapes = []
    for i in range(n):
        if i in endpoints:
            continue
        A = []
        for j in range(n):
            if i != j and abs(d[i, j] - 1.0) <= tol:
                A.append(X[i] - X[j])
        v = cone_escape(A)
        if v is not None:
            point_escapes.append((i, v))

    subset_escapes = []
    movable = [i for i in range(n) if i not in endpoints]

    if enumerate_subsets and len(movable) <= 22:
        # Complement always contains every diameter endpoint.
        for r in range(1, len(movable) + 1):
            for tup in itertools.combinations(movable, r):
                S = set(tup)
                A = []
                for i, j in contacts:
                    if i in S and j not in S:
                        A.append(X[i] - X[j])
                    elif j in S and i not in S:
                        A.append(X[j] - X[i])
                v = cone_escape(A)
                if v is not None:
                    subset_escapes.append((tuple(sorted(S)), v))
                    # Remove this break to enumerate all escaping subsets.
                    break
            if subset_escapes:
                break

    return {
        "diameter": D,
        "contacts": contacts,
        "diameter_edges": diameter_edges,
        "diameter_endpoints": endpoints,
        "point_escapes": point_escapes,
        "subset_escapes": subset_escapes,
    }

def translate_subset(X, S, v, t):
    Y = np.array(X, dtype=float, copy=True)
    for i in S:
        Y[i] += t * np.asarray(v)
    return Y

def feasible_at_diameter(X, D, tol=1e-9):
    d = cdist(X, X)
    n = len(X)
    for i in range(n):
        for j in range(i + 1, n):
            if d[i, j] < 1.0 - tol:
                return False
            if d[i, j] > D + tol:
                return False
    return True

def verify_escape_numerically(X, S, v, D):
    """
    Halve t until a feasible translated realization is found.
    This is only exploratory.
    """
    t = 1.0
    for _ in range(80):
        Y = translate_subset(X, S, v, t)
        if feasible_at_diameter(Y, D):
            return t, Y
        t *= 0.5
    return None, None
```

Exact triangular-patch test:

```python
def triangular_patch(m):
    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.5, np.sqrt(3.0)/2.0])
    pts = []
    labels = []
    for i in range(m + 1):
        for j in range(m + 1 - i):
            pts.append(i*e1 + j*e2)
            labels.append((i, j))
    return np.array(pts), labels

for m in range(2, 15):
    X, labels = triangular_patch(m)
    report = analyze_candidate(X, enumerate_subsets=False)
    k = m // 2 if m // 2 >= 1 else 1
    p = labels.index((k, 0))
    print(m, len(X), report["diameter"], p,
          [r for r in report["point_escapes"] if r[0] == p])
```

Regular even-polygon isolation test:

```python
def regular_polygon(m):
    assert m % 2 == 0 and m >= 4
    R = 1.0 / (2.0 * np.sin(np.pi / m))
    ang = 2.0 * np.pi * np.arange(m) / m
    return R * np.column_stack([np.cos(ang), np.sin(ang)])

for m in range(4, 30, 2):
    X = regular_polygon(m)
    d = cdist(X, X)
    D = np.max(d)

    p = 0
    plus, minus, opposite = 1, m - 1, m // 2

    # Put all active inequalities in the form c·v >= 0.
    signed_normals = [
        X[p] - X[plus],       # lower contact
        X[p] - X[minus],      # lower contact
        -(X[p] - X[opposite]) # upper diameter constraint
    ]
    print(m, D, cone_escape(signed_normals))
    # Expected: None, up to numerical tolerance.
```

For numerical optimizers at \(4\le n\le 30\), the most informative experiment is:

1. run many nonlinear-programming starts minimizing \(D\) subject to
   \[
   1\le\|x_i-x_j\|\le D;
   \]
2. cluster candidate solutions by complete distance matrices;
3. apply `analyze_candidate`;
4. for every reported escape, continue it numerically and then certify all inequalities by interval arithmetic;
5. separately test whether every numerical hull point is an apparent diameter endpoint.

The critical empirical question is whether high-quality candidates consistently satisfy the no-rattler conditions. If they do, Route 2 should likely be abandoned unless a new exact stress or boundary theorem is found.

## Route Diagnosis

**Proved ledger**

- A non-isolated fixed-core feasible region preserving an independent diameter pair gives continuum many incongruent optimal configurations.
- For a non-diameter point, local movability is exactly equivalent to failure of its contact vectors to positively span \(\mathbb R^2\).
- Every diameter endpoint is an exposed hull vertex.
- Any non-diametral boundary point in an optimizer forces \(h(n)=\infty\).
- Any translationally separable subset of non-diameter points forces \(h(n)=\infty\).
- Hence finite \(h(n)\) forces diametrally covered boundaries, contact-surrounded interiors, and a positive-spanning contact-cut condition.
- Exact large same-diameter flexible families exist, but the exhibited families are not globally optimal.
- Arbitrarily large feasible configurations can have every point individually locally isolated, so cardinality alone cannot force a rattler.

**Plausible but unproved claims**

- Some sufficiently large exact optimizer has a non-diametral hull point.
- Some sufficiently large exact optimizer has an undercoordinated interior defect.
- Boundary-size or stress considerations might force a translationally flexible interior subset.
- None currently has a proof, and fully jammed triangular-type optimizers remain a serious counter-scenario.

**Dead ends**

- Pure active-constraint counting: there can be more than enough contact and diameter constraints to isolate the framework.
- Average contact-degree arguments: triangular interiors have degree six and easily satisfy local positive-spanning conditions.
- Convex-hull arguments alone: regular or near-constant-width polygons can make every hull vertex diametral.
- Asymptotic density: it cannot distinguish an exactly optimal jammed configuration from a same-diameter flexible competitor with an \(O(1)\) diameter disadvantage.
- Genericity: exact optimization can select nongeneric, highly stressed configurations, so generic flexibility heuristics are inapplicable.

A fresh Route 2 attempt should target a genuinely global theorem: either prove that a diametrally covered hull plus positive-spanning contact cuts is incompatible with exact diameter optimality for large \(n\), or derive from equilibrium stresses that such a completely jammed optimizer must crystallize into a structure whose boundary necessarily contains a defect. That would, however, approach the finite-crystallization difficulty underlying Routes 1 and 4.