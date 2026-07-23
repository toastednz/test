STATUS: BLOCKED

## Result

I proved a substantial lattice-restricted multiplicity theorem. For the unit triangular lattice, the diameter-capacity function has unbounded jumps, because squared lattice distances form a zero-density set of integers while capacity grows linearly in the squared diameter. At every sufficiently large jump of size \(J\), all but the top three orders in that \(J\)-order plateau have at least \(\asymp n\) incongruent lattice-optimal configurations, obtained by deleting sites while retaining a diameter pair. Consequently, the lattice analogue has \(\limsup h_\Lambda(n)=\infty\), with multiplicity tending to infinity uniformly on arbitrarily long blocks. However, this does not transfer to the unrestricted problem without an exact finite crystallization theorem \(D_n=D_n^\Lambda\), and it does not settle even the eventual lattice analogue because the top three orders of every plateau remain uncontrolled. Exact crystallization is already false for \(n=4\): \(D_4=\sqrt2\), whereas the triangular-lattice optimum is \(\sqrt3\). Thus Route 1 is blocked at two precise points: global lattice optimality and multiplicity at lattice capacity maxima.

## Complete Argument

### 1. The triangular-lattice capacity function

Let
\[
\Lambda=\{a e_1+b e_2:a,b\in\mathbb Z\},
\qquad
e_1=(1,0),\quad e_2=\left(\frac12,\frac{\sqrt3}{2}\right).
\]
Then
\[
\|a e_1+b e_2\|^2=Q(a,b):=a^2+ab+b^2.
\]
The shortest nonzero lattice vectors have length \(1\).

Define
\[
A(t)=\max\{|S|:S\subseteq\Lambda,\ \operatorname{diam}(S)^2\le t\}.
\]
The maximum exists: after translating one point of \(S\) to the origin, all of \(S\) lies among the finitely many lattice points satisfying \(Q(a,b)\le t\).

Let
\[
D_n^\Lambda=\min\{\operatorname{diam}(S):S\subseteq\Lambda,\ |S|=n\},
\]
and let \(h_\Lambda(n)\) be the number of congruence classes of lattice subsets attaining \(D_n^\Lambda\), where congruence is by arbitrary Euclidean isometries, not merely lattice symmetries.

The possible nonzero squared distances in \(\Lambda\) form
\[
\mathcal Q=\{Q(a,b):(a,b)\in\mathbb Z^2\setminus\{(0,0)\}\}.
\]
Thus \(A(t)\) changes only when \(t\) crosses an element of \(\mathcal Q\), and
\[
(D_n^\Lambda)^2=\min\{m\in\mathcal Q:A(m)\ge n\}.
\]

### 2. Sharp first-order growth of \(A(t)\)

Set
\[
c=\frac{\pi}{2\sqrt3}.
\]

#### Lemma 1
As \(t\to\infty\),
\[
A(t)=ct+O(\sqrt t).
\]

#### Proof

The upper bound is Oler’s inequality, applied to a lattice subset \(S\) of diameter at most \(\sqrt t\):
\[
|S|
\le \frac{2}{\sqrt3}\operatorname{area}(\operatorname{conv}S)
+\frac12\operatorname{perimeter}(\operatorname{conv}S)+1.
\]
The isodiametric and perimeter-diameter inequalities give
\[
\operatorname{area}(\operatorname{conv}S)\le\frac{\pi t}{4},
\qquad
\operatorname{perimeter}(\operatorname{conv}S)\le\pi\sqrt t.
\]
Hence
\[
A(t)\le \frac{\pi}{2\sqrt3}t+\frac{\pi}{2}\sqrt t+1.
\]

For the lower bound, the fundamental-cell area of \(\Lambda\) is
\[
a_0=\frac{\sqrt3}{2},
\]
and the covering radius of \(\Lambda\) is
\[
\rho=\frac1{\sqrt3}.
\]
Let \(N(R)=|\Lambda\cap B(0,R)|\). The union of the Voronoi cells centered at points of \(\Lambda\cap B(0,R)\) covers \(B(0,R-\rho)\): every \(x\) in the latter disk has a nearest lattice point \(\lambda\) with
\[
\|\lambda\|\le\|x\|+\|x-\lambda\|\le R.
\]
Since Voronoi-cell interiors are disjoint and every cell has area \(a_0\),
\[
N(R)a_0\ge \pi(R-\rho)^2.
\]
Taking \(R=\sqrt t/2\), the set \(\Lambda\cap B(0,R)\) has diameter at most \(\sqrt t\). Therefore
\[
\begin{aligned}
A(t)
&\ge \frac{\pi}{a_0}\left(\frac{\sqrt t}{2}-\rho\right)^2\\
&=\frac{\pi}{2\sqrt3}t-\frac{2\pi}{3}\sqrt t+\frac{2\pi}{3\sqrt3}
\end{aligned}
\]
for \(t\ge4\rho^2\). This proves the lemma. ∎

This also gives the familiar lattice upper bound
\[
D_n^\Lambda
\le \sqrt{\frac{2\sqrt3}{\pi}}\sqrt n+\frac2{\sqrt3}.
\]
It is only an additive-\(O(1)\) approximation and supplies no exact crystallization.

### 3. Squared triangular-lattice distances have density zero

#### Lemma 2
The set \(\mathcal Q\) has natural density zero:
\[
|\mathcal Q\cap[1,T]|=o(T).
\]

#### Proof

Let \(p\equiv2\pmod3\) be prime. Suppose
\[
p\mid Q(a,b)=a^2+ab+b^2.
\]
If \(b\not\equiv0\pmod p\), then \(u=ab^{-1}\) satisfies
\[
u^2+u+1\equiv0\pmod p.
\]
Hence \(u^3\equiv1\pmod p\). Moreover \(u\not\equiv1\pmod p\), since otherwise \(3\equiv0\pmod p\), impossible for \(p\equiv2\pmod3\). Thus \(\mathbb F_p^\times\) would contain an element of order \(3\), requiring \(3\mid p-1\), again impossible.

Therefore \(b\equiv0\pmod p\), and then \(a\equiv0\pmod p\). It follows that
\[
p^2\mid Q(a,b).
\]
In particular, every represented integer \(q\in\mathcal Q\) satisfies, for every prime \(p\equiv2\pmod3\),
\[
p\mid q\quad\Longrightarrow\quad p^2\mid q.
\]

For a finite set \(P\) of primes congruent to \(2\pmod3\), let \(E_P\) be the positive integers satisfying this implication for every \(p\in P\). Modulo \(p^2\), the allowed residue classes are the \(p^2-p\) classes not divisible by \(p\), together with the zero class. Therefore, by the Chinese remainder theorem, \(E_P\) has density
\[
\prod_{p\in P}\left(1-\frac1p+\frac1{p^2}\right).
\]
Since \(\mathcal Q\subseteq E_P\),
\[
\overline d(\mathcal Q)
\le
\prod_{p\in P}\left(1-\frac1p+\frac1{p^2}\right).
\]

It remains to recall that
\[
\sum_{\substack{p\ {\rm prime}\\p\equiv2\pmod3}}\frac1p=\infty.
\]
For completeness, let \(\chi\) be the nonprincipal character modulo \(3\). For \(s>1\),
\[
\log L(s,\chi)
=
\sum_{p\equiv1(3)}p^{-s}
-\sum_{p\equiv2(3)}p^{-s}+O(1),
\]
where the \(O(1)\) is uniform as \(s\downarrow1\), since all prime-power terms of exponent at least \(2\) converge absolutely. Also
\[
L(s,\chi)\longrightarrow
L(1,\chi)
=
\sum_{k\ge0}\left(\frac1{3k+1}-\frac1{3k+2}\right)>0.
\]
If the reciprocal sum over primes \(p\equiv2\pmod3\) converged, then the divergence of the reciprocal sum over all primes would force
\[
\sum_{p\equiv1(3)}p^{-s}\longrightarrow\infty
\]
as \(s\downarrow1\). The displayed formula would then imply \(\log L(s,\chi)\to\infty\), contradicting the finite positive limit of \(L(s,\chi)\). Thus the reciprocal sum diverges.

Consequently,
\[
\prod_{\substack{p\le y\\p\equiv2(3)}}
\left(1-\frac1p+\frac1{p^2}\right)\longrightarrow0,
\]
because its logarithm is at most
\[
-\sum_{\substack{p\le y\\p\equiv2(3)}}
\left(\frac1p-\frac1{p^2}\right).
\]
Letting \(P\) increase through these primes gives \(\overline d(\mathcal Q)=0\). ∎

### 4. Lattice-capacity jumps are unbounded

For \(m\in\mathcal Q\), define
\[
A_-(m)=\max_{t<m}A(t),
\qquad
J(m)=A(m)-A_-(m).
\]
Thus \(J(m)\) is the capacity jump at squared diameter \(m\).

#### Lemma 3
The jumps \(J(m)\) are unbounded as \(m\to\infty\).

#### Proof

Let
\[
R(T)=|\mathcal Q\cap[1,T]|.
\]
Because \(A\) changes only at values in \(\mathcal Q\),
\[
A(T)-1
=
\sum_{\substack{m\in\mathcal Q\\m\le T}}J(m).
\]
By Lemma 1,
\[
A(T)-1=cT+O(\sqrt T),
\]
while Lemma 2 gives \(R(T)=o(T)\). Therefore
\[
\max_{\substack{m\in\mathcal Q\\m\le T}}J(m)
\ge
\frac{A(T)-1}{R(T)}
\longrightarrow\infty.
\]
Hence there is a sequence \(m_j\to\infty\) with \(J(m_j)\to\infty\). ∎

There is also a useful upper bound on individual jumps.

#### Lemma 4
For active levels \(m\to\infty\),
\[
J(m)=O(\sqrt m)=o(A(m)).
\]

#### Proof

Let \(k\) be the largest nonnegative integer satisfying \(k^2<m\). Then
\[
k\ge\sqrt m-1,
\]
and \(k^2=Q(k,0)\in\mathcal Q\). Consequently,
\[
A_-(m)\ge A(k^2).
\]
Lemma 1 gives
\[
A(m)\le cm+O(\sqrt m),
\qquad
A(k^2)\ge ck^2-O(k).
\]
Since \(m-k^2=O(\sqrt m)\),
\[
J(m)\le c(m-k^2)+O(\sqrt m)=O(\sqrt m).
\]
Also \(A(m)=cm+O(\sqrt m)\), so \(J(m)/A(m)\to0\). ∎

### 5. A rigorous deletion-multiplicity theorem

The next lemma handles unordered congruence classes and arbitrary reflections; it is not merely a labeled count.

#### Lemma 5
Let \(m\in\mathcal Q\) have positive jump
\[
J=A(m)-A_-(m)>0,
\]
and write \(M=A(m)\). For every integer \(r\) satisfying
\[
0\le r<J,
\]
one has
\[
h_\Lambda(M-r)
\ge
\frac{\binom{M-2}{r}}{2M(M-1)}.
\]

#### Proof

Choose a capacity-maximizing set \(S\subseteq\Lambda\) with
\[
|S|=M,\qquad \operatorname{diam}(S)^2\le m.
\]
Its diameter must be exactly \(\sqrt m\). Otherwise its squared diameter would be a represented value strictly smaller than \(m\), yielding
\[
M\le A_-(m),
\]
contrary to \(J>0\).

Fix a diameter pair \(p,q\in S\), so
\[
\|p-q\|^2=m.
\]
For each \(r\)-element subset
\[
R\subseteq S\setminus\{p,q\},
\]
put
\[
X_R=S\setminus R.
\]
Every \(X_R\) has \(M-r\) points, minimum pairwise distance at least \(1\), and diameter exactly \(\sqrt m\), since it retains \(p,q\).

Moreover,
\[
M-r>M-J=A_-(m).
\]
No lattice set of \(M-r\) points can therefore have squared diameter strictly smaller than \(m\). Hence every \(X_R\) is lattice-optimal.

There are
\[
\binom{M-2}{r}
\]
such sets. It remains to bound how many can belong to one congruence class.

Fix one \(X_R\), and choose two distinct points \(x_1,x_2\in X_R\). If \(X_{R'}\) is congruent to \(X_R\), some Euclidean isometry \(T\) maps \(X_R\) onto \(X_{R'}\). The ordered pair
\[
(Tx_1,Tx_2)
\]
is an ordered pair of distinct points of \(S\), giving at most \(M(M-1)\) possibilities. For any prescribed ordered target pair with the correct distance, there are at most two plane isometries sending \(x_1,x_2\) to it, one of each orientation. Thus there are at most
\[
2M(M-1)
\]
possible isometries, and hence at most that many members of the deletion family in any one congruence class.

Dividing the family size by this bound proves the claim. ∎

#### Corollary 6
There are arbitrarily long consecutive blocks of orders on which the lattice-optimal multiplicity tends uniformly to infinity.

More precisely, there are \(m_j\to\infty\), with
\[
M_j=A(m_j),\qquad J_j=J(m_j)\to\infty,
\]
such that
\[
\min_{A_-(m_j)<n\le M_j-3}h_\Lambda(n)\longrightarrow\infty.
\]

#### Proof

Write \(n=M_j-r\). The indicated range is exactly
\[
3\le r\le J_j-1.
\]
By Lemma 4, \(J_j=o(M_j)\), so for sufficiently large \(j\),
\[
r\le \frac{M_j-2}{2}.
\]
The binomial coefficients are increasing in this range. Lemma 5 therefore gives
\[
h_\Lambda(n)
\ge
\frac{\binom{M_j-2}{3}}{2M_j(M_j-1)}
=
\frac{(M_j-2)(M_j-3)(M_j-4)}
{12M_j(M_j-1)}.
\]
The right-hand side is asymptotic to \(M_j/12\) and hence tends to infinity. The number of covered consecutive orders is \(J_j-3\), which also tends to infinity. ∎

In particular, taking \(n_j=M_j-3\) proves
\[
\limsup_{n\to\infty}h_\Lambda(n)=\infty.
\]

This is not enough to prove \(h_\Lambda(n)\to\infty\): the orders
\[
A(m),\quad A(m)-1,\quad A(m)-2
\]
at the top of every plateau remain uncontrolled, as do plateaus whose jumps are small.

### 6. Exact crystallization does not follow from density: the case \(n=4\)

The global and lattice problems already differ at \(n=4\).

#### Lemma 7
\[
D_4=\sqrt2.
\]

#### Proof

We first prove that any four planar points of diameter \(D\) contain a pair at distance at most \(D/\sqrt2\).

By Radon’s theorem, the four points admit a partition into two nonempty parts whose convex hulls intersect.

If the partition has type \(1+3\), write
\[
x_1=\lambda_2x_2+\lambda_3x_3+\lambda_4x_4,
\qquad
\lambda_j\ge0,\quad \sum\lambda_j=1.
\]
The variance identity gives
\[
\sum_{j=2}^4\lambda_j\|x_1-x_j\|^2
=
\sum_{2\le j<k\le4}\lambda_j\lambda_k\|x_j-x_k\|^2.
\]
The right side is at most
\[
D^2\sum_{j<k}\lambda_j\lambda_k
=
\frac{D^2}{2}\left(1-\sum_j\lambda_j^2\right)
\le\frac{D^2}{3}.
\]
If every pair had distance greater than \(D/\sqrt2\), the left side would be greater than \(D^2/2\), a contradiction.

If the partition has type \(2+2\), let the segments \([x_1,x_2]\) and \([x_3,x_4]\) meet at
\[
z=(1-t)x_1+tx_2=(1-s)x_3+sx_4.
\]
Let \(U\) equal \(x_1,x_2\) with probabilities \(1-t,t\), and let \(V\) equal \(x_3,x_4\) with probabilities \(1-s,s\). Then \(EU=EV=z\), and
\[
\begin{aligned}
E\|U-V\|^2
&=E\|U-z\|^2+E\|V-z\|^2\\
&=t(1-t)\|x_1-x_2\|^2
+s(1-s)\|x_3-x_4\|^2\\
&\le \frac{D^2}{2}.
\end{aligned}
\]
If every cross-distance were greater than \(D/\sqrt2\), the expectation would be greater than \(D^2/2\), again a contradiction.

Thus the minimum distance among four points is at most \(D/\sqrt2\). A feasible four-point configuration therefore has \(D\ge\sqrt2\). A unit square attains this bound. ∎

#### Lemma 8
For the triangular lattice,
\[
D_4^\Lambda=\sqrt3.
\]

#### Proof

The value \(2\) is not represented by \(Q(a,b)=a^2+ab+b^2\). Indeed, modulo \(2\), \(Q(a,b)\) is even only when both \(a,b\) are even; in that case \(Q(a,b)\) is divisible by \(4\).

Thus any lattice set of diameter strictly less than \(\sqrt3\) has every nonzero squared distance equal to \(1\). There cannot be four planar points all mutually at distance \(1\): after choosing two of them, the common unit-distance points are the two equilateral-triangle apexes, which are themselves at distance \(\sqrt3\). Hence such a set has at most three points.

On the other hand,
\[
\{0,e_1,e_2,e_1+e_2\}
\]
has five squared distances equal to \(1\) and one equal to \(3\). Its diameter is \(\sqrt3\). ∎

Therefore
\[
D_4=\sqrt2<\sqrt3=D_4^\Lambda.
\]
This does not rule out eventual crystallization, but it proves that exact lattice optimality is not an automatic consequence of the local kissing geometry or density bound.

### 7. The exact missing implication

Always
\[
D_n\le D_n^\Lambda.
\]
If equality happened at an order \(n\), every lattice-optimal configuration at that order would also be globally optimal, and therefore
\[
h(n)\ge h_\Lambda(n).
\]

The rigorous results above would thus transfer at those orders for which one could prove
\[
D_n=D_n^\Lambda.
\]
No such eventual equality theorem is available. The estimates proved above give only
\[
D_n^\Lambda-D_n=O(1),
\]
whereas the problem requires exact equality. Moreover, even a theorem asserting equality for every sufficiently large \(n\) would not by itself finish Route 1: one would still need to control the top orders of every lattice-capacity plateau and all small-jump plateaus.

## Self-Audit

1. **The fatal global bridge is absent.** Nothing proved here implies \(D_n=D_n^\Lambda\), and the \(n=4\) calculation shows that such equality can fail. I do not claim that the bridge “should” hold; this is exactly why the status is BLOCKED.

2. **The zero-density proof uses standard analytic number theory.** The only external ingredients are the Euler products for \(\zeta(s)\) and \(L(s,\chi)\), and the finite positive limit \(L(1,\chi)\). The argument is included far enough to show precisely how they imply divergence of the reciprocal primes \(p\equiv2\pmod3\).

3. **The congruence count is deliberately coarse.** A congruence between deletion subsets need not extend to an automorphism of the original capacity set. The proof does not assume extension: it bounds all possible isometries by fixing two source points and counting their ordered images in \(S\), including both orientations.

## Computations To Verify

The following exact combinatorial code computes \(A(m)\), capacity jumps, and deletion-family congruence classes for moderate \(m\). Every lattice set can be translated to contain the origin, so maximum cliques in this finite graph are exhaustive.

```python
import math
import itertools
import networkx as nx

def q(v):
    a, b = v
    return a*a + a*b + b*b

def qdiff(u, v):
    return q((u[0] - v[0], u[1] - v[1]))

def lattice_vertices(m):
    # q(a,b) >= (a^2+b^2)/2, so this box is exhaustive.
    B = math.ceil(math.sqrt(2*m)) + 1
    return [(a, b)
            for a in range(-B, B+1)
            for b in range(-B, B+1)
            if q((a, b)) <= m]

def maximum_cliques_at_diameter(m):
    V = lattice_vertices(m)
    G = nx.Graph()
    G.add_nodes_from(V)
    for i, u in enumerate(V):
        for v in V[i+1:]:
            if qdiff(u, v) <= m:
                G.add_edge(u, v)

    # The origin is adjacent to every vertex, hence belongs to every
    # maximal clique. find_cliques is therefore exhaustive for anchored sets.
    best_size = 0
    best = []
    for C in nx.find_cliques(G):
        if len(C) > best_size:
            best_size = len(C)
            best = [tuple(sorted(C))]
        elif len(C) == best_size:
            best.append(tuple(sorted(C)))

    assert all((0, 0) in C for C in best)
    return best_size, best

def represented_levels(T):
    B = math.ceil(math.sqrt(2*T)) + 1
    return sorted({
        q((a, b))
        for a in range(-B, B+1)
        for b in range(-B, B+1)
        if 0 < q((a, b)) <= T
    })

def scan_capacities(T):
    previous = 1
    output = []
    for m in represented_levels(T):
        A, maximizers = maximum_cliques_at_diameter(m)
        jump = A - previous
        output.append((m, A, jump, len(maximizers)))
        previous = A
    return output

def distance_graph(S):
    G = nx.Graph()
    G.add_nodes_from(range(len(S)))
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            G.add_edge(i, j, w=qdiff(S[i], S[j]))
    return G

edge_match = nx.algorithms.isomorphism.categorical_edge_match("w", None)

def congruent(S, T):
    if len(S) != len(T):
        return False
    return nx.is_isomorphic(
        distance_graph(S), distance_graph(T), edge_match=edge_match
    )

def deletion_orbits(m, r):
    M, maximizers = maximum_cliques_at_diameter(m)
    S = tuple(maximizers[0])

    diameter_pairs = [
        (u, v) for u, v in itertools.combinations(S, 2)
        if qdiff(u, v) == m
    ]
    if not diameter_pairs:
        raise ValueError("This level is not a positive capacity jump.")

    p, q0 = diameter_pairs[0]
    removable = [x for x in S if x not in (p, q0)]

    family = []
    for R in itertools.combinations(removable, r):
        R = set(R)
        family.append(tuple(sorted(x for x in S if x not in R)))

    representatives = []
    for X in family:
        if not any(congruent(X, Y) for Y in representatives):
            representatives.append(X)

    theorem_bound = math.comb(M-2, r) / (2*M*(M-1))
    return {
        "M": M,
        "family_size": len(family),
        "number_of_congruence_classes": len(representatives),
        "proved_lower_bound": theorem_bound,
        "representatives": representatives
    }

# Basic exact checks:
assert maximum_cliques_at_diameter(1)[0] == 3
assert maximum_cliques_at_diameter(2)[0] == 3
assert maximum_cliques_at_diameter(3)[0] == 4

print(scan_capacities(30))
```

A numerical continuous optimizer can search for nonlattice improvements over a lattice threshold. Any promising floating-point output should be converted to rational coordinates and checked using the exact ratio certificate below.

```python
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction

def local_continuous_search(start_points, m):
    """
    Search for n points with max squared distance z < m and
    every squared distance >= 1. Point 0 is anchored at the origin.
    """
    P = np.asarray(start_points, dtype=float)
    P = P - P[0]
    n = len(P)

    def unpack(v):
        X = np.zeros((n, 2))
        X[1:] = v[:-1].reshape((n-1, 2))
        z = v[-1]
        return X, z

    def objective(v):
        return v[-1]

    def inequalities(v):
        X, z = unpack(v)
        values = []
        for i in range(n):
            for j in range(i+1, n):
                d2 = np.dot(X[i] - X[j], X[i] - X[j])
                values.append(d2 - 1.0)
                values.append(z - d2)
        return np.array(values)

    maxd2 = max(np.dot(P[i]-P[j], P[i]-P[j])
                for i in range(n) for j in range(i+1, n))
    v0 = np.r_[P[1:].ravel(), maxd2]
    B = math.sqrt(m)
    bounds = [(-B, B)] * (2*(n-1)) + [(1.0, float(m))]

    return minimize(
        objective, v0, method="SLSQP",
        bounds=bounds,
        constraints={"type": "ineq", "fun": inequalities},
        options={"maxiter": 20000, "ftol": 1e-13}
    )

def exact_ratio_certificate(decimal_points, m):
    """
    decimal_points should be strings or exact decimal numbers.
    If True, scaling by the inverse minimum distance gives an exact
    feasible configuration of squared diameter strictly below m.
    """
    P = [(Fraction(str(x)), Fraction(str(y)))
         for x, y in decimal_points]

    d2 = []
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            dx = P[i][0] - P[j][0]
            dy = P[i][1] - P[j][1]
            d2.append(dx*dx + dy*dy)

    mn, mx = min(d2), max(d2)
    return mn > 0 and mx < Fraction(m) * mn
```

The most informative computations would be:

1. Tabulate \(A(m)\), \(J(m)\), and all capacity maximizers for every represented \(m\) accessible.
2. Compute \(h_\Lambda(A(m))\), \(h_\Lambda(A(m)-1)\), and \(h_\Lambda(A(m)-2)\), the three orders not covered by the theorem.
3. Run continuous searches at every lattice threshold. An exact rational ratio certificate with value below \(m\) rigorously refutes global lattice optimality at that order.
4. Test whether large jumps correspond to many geometrically distinct capacity-maximizing windows, which could address the top-order obstruction.

## Route Diagnosis

**Proved ledger**

- \(A(t)=\frac{\pi}{2\sqrt3}t+O(\sqrt t)\).
- Triangular-lattice squared distances have density zero.
- Lattice-capacity jumps are unbounded but each is \(O(\sqrt m)\).
- At a jump of size \(J\), deleting \(r<J\) sites while retaining a diameter pair preserves exact lattice optimality.
- After quotienting by all Euclidean isometries, these deletions give the explicit lower bound
  \[
  h_\Lambda(M-r)\ge\frac{\binom{M-2}{r}}{2M(M-1)}.
  \]
- There are arbitrarily long blocks on which \(h_\Lambda(n)\to\infty\) uniformly.
- Exact triangular-lattice crystallization fails at \(n=4\).

**Plausible but unproved**

- The lattice analogue may itself satisfy \(h_\Lambda(n)\to\infty\), but capacity-maximal orders are not controlled.
- Some large unrestricted optima may be lattice subsets, but there is no evidence for eventual equality \(D_n=D_n^\Lambda\).
- Capacity maximizers may have many inequivalent boundary realizations, potentially resolving the top-order obstruction, but this requires an exact discrete isodiametric classification.

**Dead ends**

- Oler’s inequality cannot certify exact lattice windows: its uncertainty is \(O(\sqrt m)\) points, precisely the boundary scale on which competing patterns differ.
- Large deletion families do not address the top three orders of a plateau.
- Unbounded jumps only yield selected long blocks, not the required eventual quantifier.
- Switching to a naive rattler argument does not help: planar contact and diameter constraints are numerous enough to jam every point, and no globally optimal flexible family is known.

**Precise block**

Route 1 now requires two new theorems:

1. an exact global statement strong enough to prove \(D_n=D_n^\Lambda\) for all sufficiently large relevant \(n\); and
2. a classification or multiplicity theorem for lattice capacity maxima and near-maxima, especially \(A(m),A(m)-1,A(m)-2\), valid at every sufficiently large threshold.

The first is a finite crystallization theorem far beyond density estimates; the second is unresolved even in the purely discrete lattice problem. A fresh Route 1 attempt should first settle the lattice top-order problem computationally and conjecturally. If those orders exhibit bounded or unique maximizers, Route 1 cannot prove the desired limit even under crystallization. If they exhibit growing multiplicity, the remaining—and much harder—task is an exact discrete-to-continuous optimality theorem.