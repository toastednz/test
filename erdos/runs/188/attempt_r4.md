STATUS: BLOCKED

## Result

Route 4 is blocked by a rigorous fractional-feasibility theorem. For every finite plane unit-distance graph and every family of unit-step \(k\)-progressions with \(k\ge5\), even the strongest LP relaxation obtained by imposing **all** linear inequalities valid for independent sets remains feasible: the constant vector \(x_v=1/k\) is feasible. Consequently, no Farkas-dual argument combining progression inequalities with weighted independence bounds can prove \(\neg A(k)\) for any \(k\ge5\); in particular, it cannot recover Tsaturian’s integral obstruction for \(k=5\), much less settle \(k=6\). This does not determine \(K\).

## Complete Argument

### 1. The strongest independence-based LP

Let \(V\subset\mathbb R^2\) be finite, let \(G=(V,E)\) be any graph whose edges join unit-distance pairs, and let \(\mathcal P\) be any family of unit-step \(k\)-term progressions contained in \(V\).

Write
\[
\operatorname{STAB}(G)
 =\operatorname{conv}\{\mathbf 1_I:I\subseteq V\text{ is independent in }G\}
 \subseteq\mathbb R^V.
\]
This is the stable-set polytope. It incorporates every linear inequality valid for independent sets, not merely edge inequalities or inequalities of the form
\[
\sum_{v\in Q}x_v\le \alpha(G[Q]).
\]

The strongest LP of the type proposed in Route 4 is
\[
x\in\operatorname{STAB}(G),\qquad
\sum_{v\in P}x_v\ge1\quad(P\in\mathcal P).
\tag{LP}
\]

Every genuine red independent transversal gives a \(0\)-\(1\) solution of this system. I will prove that when \(k\ge5\), the fractional vector
\[
x_v=\frac1k\qquad(v\in V)
\tag{1}
\]
always solves (LP).

---

### 2. A periodic unit-distance-independent set of density greater than \(1/5\)

Let
\[
\Lambda=\langle (2,0),(1,\sqrt3)\rangle_{\mathbb Z}.
\]
For
\[
\lambda=m(2,0)+n(1,\sqrt3),
\]
we have
\[
\|\lambda\|_2^2
 =(2m+n)^2+3n^2
 =4(m^2+mn+n^2).
\]
The positive-definite integer-valued quadratic form \(m^2+mn+n^2\) is at least \(1\) whenever \((m,n)\ne(0,0)\). Thus every nonzero lattice vector has length at least \(2\).

Set
\[
\rho=\frac{49}{100}
\]
and define
\[
S=\bigcup_{\lambda\in\Lambda}\overline{B}(\lambda,\rho).
\]

#### Lemma 1
The set \(S\) contains no pair of points at distance exactly \(1\).

#### Proof

If \(p,q\) belong to the same disk, then
\[
\|p-q\|_2\le2\rho=\frac{49}{50}<1.
\]

If they belong to disks centered at distinct \(\lambda,\mu\in\Lambda\), then
\[
\|p-q\|_2
 \ge \|\lambda-\mu\|_2-2\rho
 \ge2-\frac{49}{50}
 =\frac{51}{50}>1.
\]
Thus their distance is never exactly \(1\). ∎

A fundamental parallelogram of \(\Lambda\) has area
\[
\left|\det\begin{pmatrix}2&1\\0&\sqrt3\end{pmatrix}\right|
=2\sqrt3.
\]
Since \(\rho<1\), the disk around each lattice point injects into the quotient torus \(\mathbb R^2/\Lambda\). Hence the density of \(S\) is
\[
\delta=\frac{\pi\rho^2}{2\sqrt3}
=\frac{2401\pi}{20000\sqrt3}.
\]

Using the elementary strict bounds
\[
\pi>3,\qquad \sqrt3<\frac74,
\]
we obtain
\[
\delta
>
\frac{2401\cdot3}{20000}\cdot\frac47
=\frac{28812}{140000}
>\frac{28000}{140000}
=\frac15.
\tag{2}
\]

Thus \(S\) is a measurable, periodic, unit-distance-independent set of density strictly greater than \(1/5\).

---

### 3. Averaging translations gives a fractional independent set

Let \(V\subset\mathbb R^2\) be finite. Choose \(t\) uniformly from the torus \(\mathbb R^2/\Lambda\), and put
\[
I_t=V\cap(S+t).
\]
By Lemma 1, every \(I_t\) is independent in the full unit-distance graph on \(V\), and therefore also independent in any selected subgraph \(G\).

For each fixed \(v\in V\), translation invariance of Haar measure gives
\[
\Pr(v\in I_t)=\delta.
\]
Consequently,
\[
\mathbb E[\mathbf 1_{I_t}]
=\delta\mathbf 1_V.
\tag{3}
\]

There are only finitely many possible subsets \(I_t\subseteq V\). If
\[
p_I=\Pr(I_t=I),
\]
then
\[
\delta\mathbf 1_V
 =\sum_{\substack{I\subseteq V\\I\text{ independent}}}
 p_I\mathbf 1_I.
\]
Therefore
\[
\delta\mathbf 1_V\in\operatorname{STAB}(G).
\tag{4}
\]

Since \(0\in\operatorname{STAB}(G)\) and this polytope is convex, every scalar multiple
\[
a\delta\mathbf 1_V,\qquad 0\le a\le1,
\]
also lies in \(\operatorname{STAB}(G)\).

For \(k\ge5\), equation (2) gives \(k\delta>1\). Taking
\[
a=\frac1{k\delta}<1
\]
in (4) yields
\[
\frac1k\mathbf 1_V\in\operatorname{STAB}(G).
\tag{5}
\]

This proves the essential fractional-feasibility assertion.

---

### 4. Every progression inequality is satisfied

Let \(P\in\mathcal P\) be a unit-step \(k\)-term progression. Its \(k\) vertices are distinct because the step vector has norm \(1\). At the vector (1),
\[
\sum_{v\in P}x_v
=k\cdot\frac1k
=1.
\]
Thus every progression constraint is satisfied with equality.

Combining this with (5), the constant vector \(x_v=1/k\) is feasible for (LP).

We have proved:

#### Theorem 2: Fractional barrier
For every \(k\ge5\), every finite \(V\subset\mathbb R^2\), every selection of unit-distance edges \(E\), and every family \(\mathcal P\) of unit-step \(k\)-progressions in \(V\), the system
\[
x\in\operatorname{STAB}(G),\qquad
\sum_{v\in P}x_v\ge1\quad(P\in\mathcal P)
\]
is feasible.

In particular, no nonnegative Farkas combination of:

- progression inequalities \(\sum_{v\in P}x_v\ge1\), and
- arbitrary linear inequalities valid for independent sets of the finite unit-distance graph,

can yield a contradiction for \(k\ge5\).

Indeed, such a contradiction would certify that the displayed LP is infeasible, whereas the constant vector \(1/k\) is a feasible point.

---

### 5. Weighted form of the obstruction

The same construction directly defeats asymmetric weighted attempts.

Let \(w_v\ge0\) be arbitrary and let
\[
\alpha_w(G)=
\max_{I\text{ independent}}\sum_{v\in I}w_v.
\]
Averaging the translated independent sets gives
\[
\mathbb E\left[\sum_{v\in I_t}w_v\right]
=\delta\sum_{v\in V}w_v.
\]
Therefore some translation \(t\) satisfies
\[
\sum_{v\in I_t}w_v
\ge\delta\sum_{v\in V}w_v,
\]
and hence
\[
\alpha_w(G)\ge\delta\sum_{v\in V}w_v
>\frac15\sum_{v\in V}w_v.
\tag{6}
\]

Thus no clever choice of nonnegative vertex weights can force the weighted independence ratio of a finite plane unit-distance graph below \(1/5\).

One may optimize the construction by taking any \(\rho<1/2\) and then letting \(\rho\uparrow1/2\). Since finite stable-set polytopes are closed, this gives
\[
\frac{\pi}{8\sqrt3}\mathbf 1_V\in\operatorname{STAB}(G)
\]
and therefore
\[
\chi_f(G)\le\frac{8\sqrt3}{\pi}<5
\tag{7}
\]
for every finite plane unit-distance graph. The strict inequality follows from
\[
8\sqrt3<14<15<5\pi.
\]

This stronger formulation explains the obstruction conceptually: an LP certificate of the proposed type for \(\neg A(k)\) would require, as a necessary condition, a finite plane unit-distance graph with fractional chromatic number exceeding \(k\). That is impossible already for \(k=5\).

---

### 6. Why this does not give a coloring

The periodic set \(S\) is only a fractional-averaging device. It does not hit all long unit-step progressions.

For example, lattice rows have \(y\)-coordinates \(n\sqrt3\). The horizontal line
\[
y=\frac{\sqrt3}{2}
\]
has distance at least \(\sqrt3/2>1/2>\rho\) from every lattice row. It is therefore disjoint from \(S\). Every horizontal unit-step progression on this line is entirely outside \(S\).

Thus the fractional solution cannot be promoted directly to an upper-bound construction.

---

### 7. Ledger

**Proved lemmas**

1. The triangular-lattice disk union \(S\) is unit-distance-independent.
2. Its density is strictly greater than \(1/5\).
3. Every finite plane unit-distance graph satisfies
   \[
   \frac1k\mathbf 1\in\operatorname{STAB}(G)\qquad(k\ge5).
   \]
4. Consequently, every strongest-form Route 4 LP is feasible for \(k\ge5\).
5. The optimized construction gives the universal bound
   \[
   \chi_f(G)\le\frac{8\sqrt3}{\pi}<5.
   \]

**Plausible but unproved claims**

None are used in the argument. Whether any finite \(k\) admits an actual coloring remains unresolved here.

**Dead ends**

- Edge inequalities alone are even weaker: \(x_v=1/k\) satisfies
  \[
  x_v+x_w=\frac2k\le1
  \]
  for every \(k\ge2\).
- Adding all weighted independence inequalities does not help for \(k\ge5\), by Theorem 2.
- The periodic disk construction itself has infinite blue corridors.
- Maximal-independent-set domination does not visibly bound blue chains: unit neighbors of the vertices of an arbitrarily long line chain can be chosen generically to be pairwise non-unit-distance, so merely assigning a red blocker to each blue point creates no finite contradiction.

## Self-Audit

1. **Scope of the no-go theorem.** It excludes LPs whose progression information is represented by the individual cover inequalities and whose independence information consists of arbitrary valid linear inequalities for independent sets. It does not exclude integral cuts jointly encoding several progression clauses, Sherali–Adams-type correlation variables, or SAT arguments. I believe the stated scope is exact because the constructed vector lies in the full stable-set polytope, not merely a weaker relaxation.

2. **Use of measure.** Haar/Lebesgue measure appears in averaging translations of the auxiliary periodic set. No measurability of a prospective red/blue coloring is assumed. This is legitimate because \(S\) is explicitly measurable and is used only to construct a finite convex combination of independent-set incidence vectors.

3. **The argument does not resolve \(K\).** It proves that the assigned route cannot settle the relevant cases, rather than proving existence or nonexistence of a coloring. This is why the status is BLOCKED rather than SOLVED or PARTIAL toward a numerical value of \(K\).

## Computations To Verify

The basic geometric margins and density estimate can be checked exactly:

```python
from fractions import Fraction

rho = Fraction(49, 100)

# Same-disk distances are below 1.
assert 2 * rho == Fraction(49, 50)
assert 2 * rho < 1

# Different disks have center distance at least 2.
assert 2 - 2 * rho == Fraction(51, 50)
assert 2 - 2 * rho > 1

# delta = 2401*pi/(20000*sqrt(3)).
# Use pi > 3 and 1/sqrt(3) > 4/7.
delta_lower = Fraction(2401 * 3 * 4, 20000 * 7)
assert delta_lower > Fraction(1, 5)

print(float(delta_lower))  # 0.2058...
```

The lattice norm formula can be tested over a large finite range:

```python
def lattice_norm_squared(m, n):
    # Vector is (2m+n, sqrt(3)n)
    return (2*m + n)**2 + 3*n*n

for m in range(-100, 101):
    for n in range(-100, 101):
        if (m, n) != (0, 0):
            assert lattice_norm_squared(m, n) >= 4
            assert lattice_norm_squared(m, n) == 4*(m*m + m*n + n*n)
```

For a concrete finite graph, the claim \( \mathbf 1/k\in\operatorname{STAB}(G)\) can be checked by enumerating independent sets and solving for a convex combination:

```python
import numpy as np
from scipy.optimize import linprog

def independent_masks(n, edges):
    edges = list(edges)
    out = []
    for mask in range(1 << n):
        if all(not ((mask >> u) & 1 and (mask >> v) & 1)
               for u, v in edges):
            out.append(mask)
    return out

def verify_uniform_in_stab(n, edges, k):
    masks = independent_masks(n, edges)
    M = len(masks)

    # Variables lambda_I, one per independent set.
    # Sum lambda_I = 1 and each vertex marginal = 1/k.
    Aeq = np.zeros((n + 1, M))
    beq = np.zeros(n + 1)

    Aeq[0, :] = 1.0
    beq[0] = 1.0

    for v in range(n):
        for j, mask in enumerate(masks):
            Aeq[v + 1, j] = (mask >> v) & 1
        beq[v + 1] = 1.0 / k

    result = linprog(
        c=np.zeros(M),
        A_eq=Aeq,
        b_eq=beq,
        bounds=[(0, None)] * M,
        method="highs"
    )
    return result.success, result

# For exact certification, replace scipy by a rational LP solver.
```

Given progression lists, their constraints need no solver check:

```python
def verify_progressions_at_uniform(progressions, k):
    for P in progressions:
        assert len(P) == k
        assert len(set(P)) == k
        assert sum(1/k for _ in P) == 1
```

## Route Diagnosis

What worked was the averaging component itself, but it worked in the opposite direction: a dense periodic independent set produces a universal fractional solution. The obstruction is precise and unconditional. Route 4, interpreted as weighted progression counting versus arbitrary linear independent-set bounds, cannot address any \(k\ge5\). The known failure of \(A(5)\) is therefore intrinsically integral relative to this relaxation.

A fresh lower-bound attempt should use exact SAT, integer cutting planes, or joint inequalities coupling several progression clauses; ordinary density and fractional-chromatic bounds cannot suffice. A fresh upper-bound attempt must instead pursue Routes 2, 3, or 5: construct a genuine independent set with uniformly bounded gaps in every unit direction, or prove an integral independent-transversal theorem for every finite subsystem. The periodic disk averaging construction cannot serve directly because it has explicit infinite blue corridors.