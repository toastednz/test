STATUS: BLOCKED

## Result

Let \(b(n)=N(D_n)\), the largest number of points that fit at the optimal diameter \(D_n\). I prove that Route 3 succeeds completely for every nonterminal member of a capacity plateau: if \(b(n)>n\), equivalently \(D_{n+1}=D_n\), then
\[
h(n)\ge \frac{\sqrt n}{2\pi\sqrt2}.
\]
In fact, if \(b(n)\ge n+2\), a stronger linear bound follows from the Hopf–Pannwitz theorem, while the delicate case \(b(n)=n+1\) is handled by a centroidal moment invariant for one-point deletions. Thus \(h(n)\to\infty\) along every sequence of nonterminal plateau orders. The route is nevertheless blocked because the terminal orders
\[
\mathcal E=\{n:N(D_n)=n\}=\{n:D_{n+1}>D_n\}
\]
form an infinite sequence, may conceivably contain all sufficiently large integers, and deletion from a same-diameter larger configuration is unavailable there. Proving divergence along \(\mathcal E\) remains a problem of comparable strength to the original one.

## Complete Argument

### 1. Capacity plateaus

For \(D\ge0\), recall
\[
N(D)=\max\{|X|:\min_{x\ne y}\|x-y\|\ge1,\ \operatorname{diam}(X)\le D\}.
\]

This maximum is finite. Indeed, after fixing \(x_0\in X\), every point of \(X\) lies in the disk \(B(x_0,D)\). The open disks of radius \(1/2\) about the points of \(X\) are disjoint and lie in \(B(x_0,D+1/2)\), giving a finite area bound.

For each \(n\), put
\[
b=b(n):=N(D_n).
\]

#### Lemma 1: Plateau inheritance

There is a feasible \(b\)-point set \(X\) of diameter exactly \(D_n\), and
\[
D_n=D_{n+1}=\cdots=D_b.
\]
Moreover, every subset \(Y\subseteq X\) with \(n\le |Y|\le b\) has diameter exactly \(D_n\), and hence is optimal for its cardinality.

#### Proof

By the definition of \(N(D_n)\), there is a feasible \(b\)-point set \(X\) with
\[
\operatorname{diam}(X)\le D_n.
\]
For every \(m\) with \(n\le m\le b\), selecting any \(m\) points of \(X\) gives
\[
D_m\le D_n.
\]
Monotonicity of \(D_m\) gives \(D_m\ge D_n\), so \(D_m=D_n\).

Now let \(Y\subseteq X\) have \(m\in[n,b]\) points. If
\[
\operatorname{diam}(Y)<D_n,
\]
then \(D_m\le\operatorname{diam}(Y)<D_n\), contradicting \(D_m=D_n\). Thus every such \(Y\) has diameter \(D_n\). In particular, taking \(m=b\) shows that \(X\) itself has diameter exactly \(D_n\). ∎

Thus, on a plateau, there is no danger that deletion removes every diameter pair: for cardinalities still lying on the plateau, this is impossible.

---

### 2. Counting subsets using the diameter graph

The following gives a strong bound whenever at least two points can be deleted from a capacity configuration.

#### Lemma 2: Diameter-edge counting

Let \(X\) be a \(b\)-point planar set of diameter \(D\), and suppose every \(m\)-point subset of \(X\) has diameter \(D\), where \(2\le m\le b\). Then the \(m\)-point subsets of \(X\) represent at least
\[
\frac{\binom bm}{4b}
\]
distinct unordered congruence classes.

#### Proof

Partition the \(m\)-subsets of \(X\) into congruence classes. Fix one such class and one representative \(Y\subseteq X\). Since \(\operatorname{diam}(Y)=D\), choose an ordered pair \(u,v\in Y\) with
\[
\|u-v\|=D.
\]

If \(Y'\subseteq X\) is congruent to \(Y\), there is a Euclidean isometry \(T\) with \(T(Y)=Y'\). The ordered pair \((T(u),T(v))\) is then an ordered diameter pair of \(X\).

By the Hopf–Pannwitz theorem, the diameter graph of \(X\) has at most \(b\) unoriented edges, hence at most \(2b\) ordered diameter pairs.

For any fixed ordered source pair \((u,v)\) and fixed ordered target pair \((p,q)\) of the same nonzero length, there are at most two Euclidean isometries satisfying
\[
T(u)=p,\qquad T(v)=q:
\]
one orientation-preserving and one orientation-reversing. Therefore there are at most
\[
2\cdot 2b=4b
\]
possible isometries relevant to copies of \(Y\) contained in \(X\). Each such isometry determines its image \(T(Y)\), so the congruence class contains at most \(4b\) subsets.

There are \(\binom bm\) subsets in total. Hence the number of classes is at least
\[
\frac{\binom bm}{4b}.
\]
∎

Applying this to the capacity configuration from Lemma 1 gives:

#### Corollary 3

If \(b(n)\ge n+2\), then
\[
h(n)\ge \frac{\binom{b(n)}n}{4b(n)}
       \ge \frac{b(n)-1}{8}
       \ge \frac n8.
\]

#### Proof

Here \(2\le n\le b-2\), so
\[
\binom bn\ge \binom b2=\frac{b(b-1)}2.
\]
Lemma 2 and Lemma 1 now give the result. ∎

Thus plateaus with at least two points of headroom already give linearly many optimal configurations.

---

### 3. The one-deletion case

The preceding counting only gives a constant when \(b=n+1\). A different invariant resolves this case.

For a finite set
\[
X=\{x_1,\dots,x_b\},
\]
write
\[
X_i=X\setminus\{x_i\}.
\]

#### Lemma 4: Congruent deletion cards lie on a centroidal circle

Let
\[
c=\frac1b\sum_{j=1}^b x_j
\]
be the centroid of \(X\). If \(X_i\) and \(X_j\) are congruent, then
\[
\|x_i-c\|=\|x_j-c\|.
\]

#### Proof

Define
\[
A=\sum_{1\le p<q\le b}\|x_p-x_q\|^2
\]
and
\[
W_i=\sum_{j\ne i}\|x_i-x_j\|^2.
\]
The sum of squared pairwise distances in \(X_i\) is exactly \(A-W_i\). Since congruent sets have the same pairwise distances,
\[
X_i\cong X_j\quad\Longrightarrow\quad A-W_i=A-W_j,
\]
so \(W_i=W_j\).

On the other hand,
\[
\begin{aligned}
W_i
 &=\sum_{k=1}^b\|x_i-x_k\|^2\\
 &=\sum_{k=1}^b
   \big\|(x_i-c)-(x_k-c)\big\|^2\\
 &=b\|x_i-c\|^2+\sum_{k=1}^b\|x_k-c\|^2,
\end{aligned}
\]
because \(\sum_k(x_k-c)=0\). The second term is independent of \(i\), so equality \(W_i=W_j\) implies
\[
\|x_i-c\|^2=\|x_j-c\|^2.
\]
∎

#### Lemma 5: A deletion-card class has at most \(2\pi D\) members

Suppose \(X\) has mutual distances at least \(1\) and diameter \(D\ge1\). Then any congruence class among the one-point deletions \(X_i\) contains at most \(2\pi D\) members.

#### Proof

By Lemma 4, if indices \(i\) belong to one deletion-card class, then their corresponding points \(x_i\) lie on a circle centered at the centroid \(c\), say of radius \(\rho\).

First,
\[
x_i-c=\frac1b\sum_{k=1}^b(x_i-x_k),
\]
and therefore
\[
\rho=\|x_i-c\|
\le \frac1b\sum_{k=1}^b\|x_i-x_k\|
\le \frac{b-1}{b}D<D.
\]

If the class contains \(q\ge2\) points, put them in cyclic order around the circle. Every arc between consecutive such points has length at least the chord joining its endpoints, and that chord has length at least \(1\). The sum of these \(q\) arc lengths is \(2\pi\rho\), so
\[
q\le2\pi\rho<2\pi D.
\]
For \(q=1\), the same asserted bound holds because \(D\ge1\). ∎

#### Corollary 6: One-deletion plateau bound

If \(b(n)=n+1\), then
\[
h(n)\ge \frac{b(n)}{2\pi D_n}.
\]

#### Proof

Choose the \(b\)-point capacity configuration \(X\) from Lemma 1. All its \(b\) one-point deletions are optimal \(n\)-point configurations of diameter \(D_n\). By Lemma 5, no congruence class contains more than \(2\pi D_n\) of these deletion sets. ∎

We now use a crude but explicit upper bound for \(D_b\). Let
\[
k=\lceil\sqrt b\rceil.
\]
Choose any \(b\) points from the \(k\times k\) integer grid. This gives
\[
D_b\le\sqrt2(k-1)<\sqrt{2b}.
\]
Since \(D_b=D_n\) on the plateau, Corollary 6 yields
\[
h(n)>
\frac{b}{2\pi\sqrt{2b}}
=\frac{\sqrt b}{2\pi\sqrt2}
>\frac{\sqrt n}{2\pi\sqrt2}.
\]

Combining the two deletion cases proves the principal partial result.

#### Theorem 7: All nonterminal plateau orders have growing multiplicity

If
\[
D_{n+1}=D_n,
\]
then
\[
\boxed{\displaystyle
h(n)\ge \frac{\sqrt n}{2\pi\sqrt2}.}
\]

Consequently, along any sequence \(n_j\to\infty\) satisfying \(D_{n_j+1}=D_{n_j}\), one has
\[
h(n_j)\to\infty.
\]

#### Proof

The equality \(D_{n+1}=D_n\) is equivalent to \(b(n)\ge n+1\).

If \(b(n)=n+1\), use Corollary 6 and the grid estimate above. If \(b(n)\ge n+2\), Corollary 3 gives
\[
h(n)\ge\frac n8\ge\frac{\sqrt n}{2\pi\sqrt2}
\]
for \(n\ge1\). ∎

---

### 4. A restriction on plateau widths

There is also a purely graph-theoretic restriction on how far a plateau can extend downward.

Suppose \(D\) occurs on the maximal block
\[
D_a=D_{a+1}=\cdots=D_b=D,
\]
where \(b=N(D)\). Let \(X\) be a \(b\)-point capacity configuration and let \(G_D(X)\) be its diameter graph.

Every \(a\)-subset of \(X\) has diameter \(D\), by Lemma 1. Therefore no \(a\)-subset is independent in \(G_D(X)\), and hence
\[
\alpha(G_D(X))\le a-1.
\]

For any graph with \(b\) vertices and \(e\) edges, the random-ordering proof of the Caro–Wei bound gives
\[
\alpha(G)\ge\sum_v\frac1{d(v)+1}
\ge\frac{b^2}{b+2e}.
\]
Hopf–Pannwitz gives \(e\le b\), so
\[
\alpha(G_D(X))\ge\frac b3.
\]
Consequently,
\[
a-1\ge\frac b3,
\qquad
b-a+1\le\frac{2b}{3}.
\]

This does not rule out large plateaus, but it shows that a capacity jump at \(D\) cannot cover more than approximately the upper two-thirds of the orders up to \(b\).

---

### 5. Exact obstruction at terminal orders

Define the terminal-capacity orders
\[
\mathcal E=\{n:N(D_n)=n\}.
\]
By attainment of \(D_{n+1}\),
\[
N(D_n)=n
\quad\Longleftrightarrow\quad
D_{n+1}>D_n.
\]

The set \(\mathcal E\) is infinite. Otherwise, \(D_{n+1}=D_n\) for all sufficiently large \(n\), making \(D_n\) eventually constant, contrary to \(D_n\to\infty\).

Theorem 7 proves the desired divergence for every \(n\notin\mathcal E\). Therefore the original problem is now reduced exactly to
\[
h(n)\longrightarrow\infty
\quad\text{as }n\to\infty\text{ through }n\in\mathcal E.
\]

At an order \(n\in\mathcal E\), there is no \((n+1)\)-point configuration of diameter \(D_n\). Thus deletion from a larger same-diameter parent—the mechanism of Route 3—is unavailable. A single optimal \(n\)-point parent has only itself as an \(n\)-point subset, so deletion orbit counting gives no multiplicity at that order.

This is a genuine block, not merely a missing estimate. It is consistent with all established facts that \(D_{n+1}>D_n\) for every sufficiently large \(n\); in that case \(\mathcal E\) is cofinite and the remaining subproblem is essentially the original problem.

## Self-Audit

1. **Use of Hopf–Pannwitz.** Lemma 2 and the plateau-width estimate import the theorem that a planar diameter graph has at most \(b\) edges rather than reproving it. This is a classical theorem explicitly included among the supplied structural facts; the counting argument only uses its stated edge bound.

2. **The centroid in Lemma 4 belongs to the full parent, not to either deletion card.** At first sight, congruence of \(X_i\) and \(X_j\) need not identify their positions relative to the centroid of \(X\). The proof avoids that issue: congruence only supplies equality of the scalar sums of squared pairwise distances, and the full-centroid identity then algebraically forces equal radii.

3. **The endpoint reduction supplies no endpoint multiplicity.** It might be tempting to regard Theorem 7 as “almost” proving the limit if plateaus are expected to be common. There is no rigorous basis for that expectation, and the endpoint set is necessarily infinite. I therefore do not claim a solution; the reduction itself is exact, but the unresolved endpoint statement may have the full strength of the original problem.

## Computations To Verify

The following exact code checks the deletion-card invariant and the diameter-edge counting for rational-coordinate candidate parents. It uses complete squared-distance matrices, not merely sorted distance multisets.

```python
from itertools import combinations, permutations
from collections import defaultdict
from fractions import Fraction
from math import comb, pi, sqrt

def sqdist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx*dx + dy*dy

def distance_matrix(points):
    b = len(points)
    return [[sqdist(points[i], points[j]) for j in range(b)]
            for i in range(b)]

def canonical_subset(Q, subset):
    """
    Exact canonical complete squared-distance matrix under relabeling.
    Suitable only for small subsets because it checks every permutation.
    """
    subset = tuple(subset)
    m = len(subset)
    signatures = []
    for p in permutations(subset):
        sig = tuple(Q[p[i]][p[j]]
                    for i in range(m)
                    for j in range(i+1, m))
        signatures.append(sig)
    return min(signatures)

def subset_diameter2(Q, subset):
    subset = tuple(subset)
    return max(Q[i][j] for i, j in combinations(subset, 2))

def group_subsets_by_congruence(Q, m):
    b = len(Q)
    groups = defaultdict(list)
    for S in combinations(range(b), m):
        groups[canonical_subset(Q, S)].append(S)
    return groups

def verify_plateau_parent(points, n):
    """
    The user must supply X for which every n-subset is expected to
    retain the full diameter. This verifies the finite conclusions.
    Coordinates should be Fractions for exact comparisons.
    """
    points = [(Fraction(x), Fraction(y)) for x, y in points]
    b = len(points)
    assert 2 <= n < b

    Q = distance_matrix(points)
    D2 = max(Q[i][j] for i, j in combinations(range(b), 2))

    # Feasibility.
    assert all(Q[i][j] >= 1
               for i, j in combinations(range(b), 2))

    # Plateau inheritance condition to check on this parent.
    all_subsets = list(combinations(range(b), n))
    assert all(subset_diameter2(Q, S) == D2 for S in all_subsets)

    # Diameter graph and Hopf–Pannwitz finite check.
    diameter_edges = [(i, j) for i, j in combinations(range(b), 2)
                      if Q[i][j] == D2]
    assert len(diameter_edges) <= b

    groups = group_subsets_by_congruence(Q, n)
    assert max(len(g) for g in groups.values()) <= 4*b
    assert len(groups) * 4*b >= comb(b, n)

    # For the one-deletion case, verify the centroid-radius invariant.
    if n == b - 1:
        cx = sum(p[0] for p in points) / b
        cy = sum(p[1] for p in points) / b
        radius2 = [
            (p[0] - cx)**2 + (p[1] - cy)**2
            for p in points
        ]

        card_groups = defaultdict(list)
        for deleted in range(b):
            card = tuple(i for i in range(b) if i != deleted)
            card_groups[canonical_subset(Q, card)].append(deleted)

        for deleted_indices in card_groups.values():
            values = {radius2[i] for i in deleted_indices}
            assert len(values) == 1

        D = sqrt(float(D2))
        assert max(len(g) for g in card_groups.values()) <= 2*pi*D + 1e-12

    return {
        "b": b,
        "n": n,
        "D2": D2,
        "diameter_edges": len(diameter_edges),
        "number_of_subset_classes": len(groups),
        "largest_class": max(len(g) for g in groups.values())
    }
```

For exact triangular-lattice capacity plateaus, use axial coordinates. The squared Euclidean distance between axial points \((i,j)\) and \((k,\ell)\) is
\[
(i-k)^2+(i-k)(j-\ell)+(j-\ell)^2.
\]

```python
from itertools import combinations

def tri_q(p, q):
    di = p[0] - q[0]
    dj = p[1] - q[1]
    return di*di + di*dj + dj*dj

def triangular_lattice_capacity(D2):
    """
    Exact but exponential.
    Computes the largest unit triangular-lattice subset of squared
    diameter <= D2. Translation is removed by requiring (0,0).
    """
    R = int(D2) + 1
    V = [(i, j)
         for i in range(-R, R+1)
         for j in range(-R, R+1)
         if tri_q((i, j), (0, 0)) <= D2]
    origin = (0, 0)
    others = [v for v in V if v != origin]

    for m in range(len(V), 0, -1):
        for rest in combinations(others, m-1):
            S = (origin,) + rest
            if all(tri_q(p, q) <= D2
                   for p, q in combinations(S, 2)):
                return m, S
    return 1, (origin,)

def lattice_deletion_diameters(S):
    D2 = max(tri_q(p, q) for p, q in combinations(S, 2))
    data = []
    for deleted in range(len(S)):
        T = S[:deleted] + S[deleted+1:]
        d2 = 0 if len(T) <= 1 else max(
            tri_q(p, q) for p, q in combinations(T, 2)
        )
        data.append((deleted, d2, d2 == D2))
    return D2, data
```

Useful finite searches are:

1. Compute exact triangular-lattice capacities for small integral \(D^2\) and record jump sizes.
2. For each capacity witness, classify all deletion subsets by the complete exact distance matrix.
3. For continuous candidates at small \(n\), certify both \(\operatorname{Feas}_n(D^2)\) and \(\neg\operatorname{Feas}_{n+1}(D^2)\) by quantifier elimination to determine whether the order is terminal.
4. Search terminal candidates for genuine fixed-diameter rattlers or active-graph flips; these are the configurations Route 3 cannot address.

## Route Diagnosis

**Proved ledger**

- A capacity configuration at \(D_n\) generates optimal subsets at every order remaining on the same plateau.
- If at least two points can be deleted, diameter-graph counting gives
  \[
  h(n)\ge \binom{N(D_n)}n/(4N(D_n)).
  \]
- Congruent one-point deletions correspond to deleted points lying on a common circle centered at the parent centroid.
- A one-deletion congruence class has at most \(2\pi D_n\) members.
- Therefore every nonterminal plateau order satisfies
  \[
  h(n)\ge \sqrt n/(2\pi\sqrt2).
  \]
- A plateau ending at capacity \(b\) has length at most \(2b/3\).

**Plausible but unproved**

- Capacity plateaus may be rare; it is possible that \(D_{n+1}>D_n\) eventually, or even for every \(n\ge3\).
- Terminal optimal configurations might sometimes have rattlers or exchangeable boundary pieces, but no mechanism forces this for every large terminal order.
- Stronger reconstruction statements for deletion cards might improve constants, but they cannot create a same-diameter parent at a terminal order.

**Dead ends and counterexamples checked**

- It is false that many deletion cards must be inequivalent for an arbitrary bounded-diameter parent without using the \(D=O(\sqrt b)\) density scale: a regular \(b\)-gon has all one-point deletions congruent and diameter of order \(b\).
- Congruence of \(X\setminus\{x\}\) and \(X\setminus\{y\}\) need not be induced by a symmetry of \(X\). For example, take a complete regular \(q\)-orbit on one circle and three consecutive points of a rotated regular \(q\)-orbit on another circle. Rotation by \(2\pi/q\) maps the deletion of one endpoint of the three-point arc to the deletion of the other, while a generic relative phase destroys every symmetry of the full set exchanging those endpoints.
- Wide capacity plateaus alone cannot settle the problem: each plateau has a terminal order, and there are infinitely many terminal orders.
- Switching to rattlers or active-graph flips does not presently repair the endpoint gap. It would require proving that every sufficiently large terminal optimum admits such a motion or exchange while retaining exact global optimality—an unproved statement at least as difficult as eventual nonuniqueness.

The sharp next target is therefore not a better deletion count. It is a theorem specifically about terminal capacity configurations \(N(D_n)=n\): either force many distinct maximum-capacity realizations, or force a genuine fixed-diameter flex in at least one such realization.