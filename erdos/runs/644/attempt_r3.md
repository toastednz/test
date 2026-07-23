STATUS: BLOCKED

## Result

Route 3’s fractional half is substantially stronger than anticipated: every \(7\)-locally \(2\)-coverable \(k\)-uniform hypergraph satisfies
\[
\tau^*(\mathcal H)\le (35k)^{1/3}=o(k).
\]
However, the proposed asymptotically lossless rounding step is false by a linear margin. For every \(k\), a complete \(k\)-uniform hypergraph on \(\lceil 7k/4\rceil-1\) vertices is \(7\)-locally \(2\)-coverable and has
\[
\tau=\left\lceil\frac{3k}{4}\right\rceil,
\qquad
\tau^*<\frac74.
\]
Thus \(\tau-\tau^*=(3/4-o(1))k\). This construction rigorously proves the required lower bound in Q1 for every \(k\), not merely a subsequence, but the universal upper bound remains unproved. Route 3, specifically its necessary rounding assertion, is therefore decisively blocked.

## Complete Argument

### 1. A strong universal fractional-transversal bound

We first work with a finite nonempty hypergraph. By finite LP duality,
\[
\tau^*(\mathcal H)=\nu^*(\mathcal H),
\]
where
\[
\nu^*(\mathcal H)
=
\max\left\{
\sum_{A\in E}y_A:
y_A\ge 0,\ 
\sum_{A\ni v}y_A\le1\quad(v\in V)
\right\}.
\]

#### Proposition 1

If \(\mathcal H\) is \(k\)-uniform and \(7\)-locally \(2\)-coverable, then
\[
\tau^*(\mathcal H)\le (35k)^{1/3}.
\]

#### Proof

Let \(y=(y_A)_{A\in E}\) be an optimal fractional matching, and put
\[
S=\sum_{A\in E}y_A=\tau^*(\mathcal H).
\]
The assertion is trivial if \(S=0\), so assume \(S>0\). Define a probability distribution on \(E\) by
\[
p_A=\frac{y_A}{S}.
\]
For each vertex \(v\), let
\[
q_v=\Pr_{A\sim p}(v\in A)
=\sum_{A\ni v}p_A.
\]
The fractional-matching constraints give
\[
q_v
=\frac1S\sum_{A\ni v}y_A
\le\frac1S.
\tag{10}
\]
Since every sampled edge has exactly \(k\) vertices,
\[
\sum_{v\in V}q_v
=\sum_{v\in V}\sum_{A\ni v}p_A
=\sum_{A\in E}p_A|A|
=k.
\tag{11}
\]

Now sample seven edges \(A_1,\dots,A_7\) independently according to \(p\), allowing repetitions. Their distinct members form a subfamily of size at most seven, so some pair \(\{x,y\}\) meets every \(A_i\).

Assign each index \(i\) to one of \(x,y\) lying in \(A_i\). By the pigeonhole principle, one of \(x,y\) is assigned at least four indices. Consequently, for every outcome there is a four-element set \(I\subseteq[7]\) such that
\[
\bigcap_{i\in I}A_i\ne\varnothing.
\]
A union bound over the \(\binom74=35\) choices of \(I\) gives
\[
1
\le
\sum_{\substack{I\subseteq[7]\\|I|=4}}
\Pr\left(\bigcap_{i\in I}A_i\ne\varnothing\right).
\tag{12}
\]

For a fixed \(I\), another union bound gives
\[
\Pr\left(\bigcap_{i\in I}A_i\ne\varnothing\right)
\le
\sum_{v\in V}\Pr(v\in A_i\text{ for all }i\in I)
=
\sum_{v\in V}q_v^4.
\]
Using (10) and (11),
\[
\sum_v q_v^4
\le
\left(\max_v q_v\right)^3\sum_vq_v
\le
\frac{k}{S^3}.
\tag{13}
\]
Combining (12) and (13),
\[
1\le \frac{35k}{S^3}.
\]
Hence
\[
S\le(35k)^{1/3}.
\]
By LP duality, \(S=\tau^*(\mathcal H)\), proving the proposition. \(\square\)

The same proof gives the following general statement.

#### Proposition 2

Let \(r\ge3\), put \(q=\lceil r/2\rceil\), and suppose \(\mathcal H\) is \(k\)-uniform and \(r\)-locally \(2\)-coverable. Then
\[
\tau^*(\mathcal H)
\le
\left(\binom rq\,k\right)^{1/(q-1)}.
\tag{14}
\]

Indeed, among \(r\) edges covered by two vertices, one of the two vertices belongs to at least \(q\) of them. The preceding sampling argument then uses \(q\)-fold intersections instead of four-fold intersections.

In particular, for every fixed \(r\ge5\),
\[
\tau^*(\mathcal H)=o(k).
\]

For an infinite hypergraph, Proposition 1 remains valid. For every finite edge subfamily there is a fractional cover of total weight at most \((35k)^{1/3}\). In the compact space \([0,1]^V\), the edge constraints are closed, and the condition
\[
\sum_{v\in V}w_v\le C
\]
means
\[
\sum_{v\in F}w_v\le C
\quad\text{for every finite }F\subseteq V,
\]
so it is also closed. The finite intersection property therefore supplies a global fractional cover of the same total weight.

---

### 2. A clique-cover lemma

The lower construction rests on the following elementary but sharp fact.

#### Lemma 3

Let \(n\ge2\), let \(s\le7\), and let \(B_1,\dots,B_s\subseteq[n]\). Suppose every two-element subset of \([n]\) is contained in at least one \(B_i\). Then
\[
\max_{1\le i\le s}|B_i|\ge\frac{3n}{7}.
\tag{15}
\]

#### Proof

For each \(x\in[n]\), define its incidence mask
\[
M_x=\{i\in[s]:x\in B_i\}.
\]
The hypothesis says that
\[
M_x\cap M_y\ne\varnothing
\qquad(x\ne y).
\tag{16}
\]
In particular, all \(M_x\) are nonempty.

Suppose first that some \(M_x\) has size at most two. Every \(M_y\), including \(M_x\) itself, intersects \(M_x\). Therefore
\[
\sum_{i\in M_x}|B_i|
=
\sum_{y\in[n]}|M_y\cap M_x|
\ge n.
\]
Since \(|M_x|\le2\), one of these \(B_i\) has size at least \(n/2\), and hence at least \(3n/7\).

Otherwise every mask has size at least three. Double-counting incidences gives
\[
\sum_{i=1}^s|B_i|
=
\sum_{x\in[n]}|M_x|
\ge3n.
\]
As \(s\le7\),
\[
\max_i|B_i|
\ge\frac{3n}{s}
\ge\frac{3n}{7}.
\]
This proves the lemma. \(\square\)

---

### 3. The complete-hypergraph lower construction

#### Proposition 4

For every integer \(k\ge1\),
\[
f(k,7)\ge \left\lceil\frac{3k}{4}\right\rceil.
\tag{17}
\]

#### Proof

For \(k\ge2\), set
\[
n=\left\lceil\frac{7k}{4}\right\rceil-1
\]
and let
\[
\mathcal H_k=\binom{[n]}k
\]
be the complete \(k\)-uniform hypergraph on \([n]\).

Because
\[
n<\frac{7k}{4},
\]
we have
\[
n-k<\frac{3n}{7}.
\tag{18}
\]

We claim that \(\mathcal H_k\) satisfies \(P_7\). Let
\[
A_1,\dots,A_s\in\mathcal H_k,\qquad s\le7,
\]
and put
\[
B_i=[n]\setminus A_i.
\]
Each \(B_i\) has size \(n-k\).

Suppose the selected edges have no two-point transversal. Then for every distinct \(x,y\in[n]\), some \(A_i\) is disjoint from \(\{x,y\}\). Equivalently,
\[
\{x,y\}\subseteq B_i
\]
for some \(i\). Thus the \(B_i\) cover every pair of vertices. Lemma 3 gives
\[
\max_i|B_i|\ge\frac{3n}{7},
\]
contradicting (18). Hence every subfamily of at most seven edges has a two-point transversal.

It remains to compute the global transversal number. For the complete \(k\)-uniform hypergraph on \(n\) vertices,
\[
\tau\left(\binom{[n]}k\right)=n-k+1.
\tag{19}
\]
Indeed, a set of at most \(n-k\) vertices leaves at least \(k\) vertices outside it and therefore misses a \(k\)-edge. Conversely, any \(n-k+1\) vertices meet every \(k\)-edge.

Consequently,
\[
\tau(\mathcal H_k)
=n-k+1
=\left\lceil\frac{7k}{4}\right\rceil-k
=\left\lceil\frac{3k}{4}\right\rceil.
\]
For \(k=1\), the one-edge complete hypergraph gives the weaker but sufficient value \(1=\lceil3/4\rceil\). This proves (17). \(\square\)

Thus the lower half of Q1 is established uniformly for every \(k\):
\[
f(k,7)\ge\frac{3k}{4}+O(1).
\]

---

### 4. Exact fractional value of the construction

#### Proposition 5

For the hypergraph \(\mathcal H_k=\binom{[n]}k\),
\[
\tau^*(\mathcal H_k)=\frac nk.
\tag{20}
\]

#### Proof

Assign weight \(1/k\) to each vertex. Every edge then receives total weight one, so
\[
\tau^*(\mathcal H_k)\le\frac nk.
\]

Conversely, let \(w\) be any fractional transversal. Summing the constraints
\[
\sum_{v\in A}w_v\ge1
\]
over all \(A\in\binom{[n]}k\) gives
\[
\binom nk
\le
\binom{n-1}{k-1}\sum_{v=1}^n w_v.
\]
Since
\[
\frac{\binom nk}{\binom{n-1}{k-1}}=\frac nk,
\]
we obtain
\[
\sum_vw_v\ge\frac nk.
\]
Therefore equality holds. \(\square\)

For the construction in Proposition 4,
\[
\tau^*(\mathcal H_k)=\frac nk<\frac74,
\]
while
\[
\tau(\mathcal H_k)=\left\lceil\frac{3k}{4}\right\rceil.
\]
Hence
\[
\tau(\mathcal H_k)-\tau^*(\mathcal H_k)
\ge
\frac{3k}{4}-\frac74,
\tag{21}
\]
and in particular
\[
\frac{\tau(\mathcal H_k)-\tau^*(\mathcal H_k)}k
\longrightarrow\frac34.
\]

Therefore the Route 3 rounding assertion
\[
\tau(\mathcal H)\le\tau^*(\mathcal H)+o(k)
\]
is false, even on the natural family giving the conjectured sharp lower bound.

Indeed, no bound of the form
\[
\tau(\mathcal H)\le o(k)\,\tau^*(\mathcal H)
\]
can hold universally here, because
\[
\frac{\tau(\mathcal H_k)}{\tau^*(\mathcal H_k)}
\sim \frac{3}{7}k.
\]

---

### 5. Sharpness of the \(3/7\) clique-cover threshold

Lemma 3 is sharp. Let \(n=7m\), partition the vertex set into seven classes indexed by the seven lines of the Fano plane, each of size \(m\). Index seven sets \(B_1,\dots,B_7\) by the Fano points, and put a vertex from line-class \(L\) into \(B_i\) exactly when \(i\in L\).

Every Fano point belongs to three lines, so
\[
|B_i|=3m=\frac{3n}{7}.
\]
Any two Fano lines intersect, so every pair of vertices is jointly contained in some \(B_i\).

Consequently, when \(k=4m\) and \(n=7m\), the seven complements
\[
A_i=[n]\setminus B_i
\]
are \(k\)-sets with no two-point transversal. Thus the complete hypergraph at the equality value \(n=7k/4\) fails \(P_7\). This explains both the strict inequality in Proposition 4 and the appearance of \(3/4\).

---

### 6. A general positive linear lower bound

For completeness, the same complete-hypergraph idea gives a positive lower ratio for every fixed \(r\).

Let \(q=n-k\). If
\[
r\binom q2<\binom n2,
\tag{22}
\]
then any at most \(r\) complements of size \(q\) collectively contain fewer than all pairs of \([n]\). A missing pair is a transversal of the corresponding \(k\)-edges. Hence \(\binom{[n]}k\) satisfies \(P_r\), and its transversal number is \(q+1\).

Taking
\[
\alpha=\frac1{2\sqrt r},
\qquad
n_k=\left\lfloor\frac{k}{1-\alpha}\right\rfloor,
\qquad
q_k=n_k-k,
\]
condition (22) holds for all sufficiently large \(k\), since
\[
r\left(\frac{q_k}{n_k}\right)^2\longrightarrow r\alpha^2=\frac14.
\]
Therefore
\[
\liminf_{k\to\infty}\frac{f(k,r)}k
\ge
\frac{\alpha}{1-\alpha}
=
\frac1{2\sqrt r-1}>0.
\tag{23}
\]
This does not prove existence of the limit in Q2.

## Self-Audit

1. **The decisive missing component is the universal integral upper bound.**  
   Nothing above proves
   \[
   f(k,7)\le(3/4+o(1))k.
   \]
   I do not regard this as routine or implicit in the fractional estimate. The explicit construction shows that converting fractional covers into integral covers is exactly where essentially the entire linear term can be lost.

2. **The fractional proof samples with repetitions, while \(P_7\) is stated for subfamilies.**  
   This is harmless because the distinct sampled edges form a subfamily of size at most seven. A pair covering those distinct edges also covers all repeated sampled indices. Thus the pigeonhole step producing four edges with a common vertex is valid.

3. **The lower construction depends on the strict integer choice \(n=\lceil7k/4\rceil-1\).**  
   The strict inequality \(n-k<3n/7\) follows exactly from \(n<7k/4\), and the Fano construction shows equality cannot simply be allowed. The computation
   \[
   n-k+1=\lceil3k/4\rceil
   \]
   is also exact because subtracting the integer \(k\) commutes with the ceiling operation.

## Computations To Verify

```python
from itertools import combinations
from math import comb, isclose

def ceil_div(a, b):
    return -(-a // b)

def has_two_cover(subfamily):
    """subfamily: iterable of frozensets"""
    subfamily = list(subfamily)
    if not subfamily:
        return True

    U = set().union(*subfamily)

    # One-point transversals
    for x in U:
        if all(x in A for A in subfamily):
            return True

    # Two distinct points
    for x, y in combinations(U, 2):
        if all((x in A or y in A) for A in subfamily):
            return True

    return False

def is_r_locally_two_coverable(edges, r=7):
    edges = list(edges)
    for s in range(1, min(r, len(edges)) + 1):
        for F in combinations(edges, s):
            if not has_two_cover(F):
                return False
    return True

def transversal_number(V, edges):
    V = list(V)
    edges = list(edges)
    for t in range(len(V) + 1):
        for T in combinations(V, t):
            T = set(T)
            if all(T.intersection(A) for A in edges):
                return t
    raise RuntimeError("No transversal found")

def complete_construction(k):
    n = ceil_div(7 * k, 4) - 1
    V = tuple(range(n))
    edges = [frozenset(A) for A in combinations(V, k)]
    return V, edges

# Direct exhaustive local checks are practical for k <= 4.
for k in range(2, 5):
    V, edges = complete_construction(k)
    expected_tau = ceil_div(3 * k, 4)
    assert is_r_locally_two_coverable(edges, 7)
    assert transversal_number(V, edges) == expected_tau
    print(k, len(V), len(edges), expected_tau)
```

Fractional-transversal verification using SciPy:

```python
import numpy as np
from scipy.optimize import linprog

def fractional_transversal_number(V, edges):
    V = list(V)
    index = {v: i for i, v in enumerate(V)}
    M = np.zeros((len(edges), len(V)))

    for row, A in enumerate(edges):
        for v in A:
            M[row, index[v]] = 1.0

    # Minimize sum w_v subject to M w >= 1 and w >= 0.
    result = linprog(
        c=np.ones(len(V)),
        A_ub=-M,
        b_ub=-np.ones(len(edges)),
        bounds=[(0, None)] * len(V),
        method="highs",
    )
    assert result.success
    return result.fun

for k in range(2, 7):
    V, edges = complete_construction(k)
    n = len(V)
    tau_star = fractional_transversal_number(V, edges)
    assert isclose(tau_star, n / k, rel_tol=1e-8, abs_tol=1e-8)
    print({
        "k": k,
        "n": n,
        "tau": ceil_div(3 * k, 4),
        "tau_star": tau_star,
        "fractional_bound": (35 * k) ** (1 / 3),
    })
```

Fano-plane certificate showing sharpness at \(n=7k/4\):

```python
def fano_bad_seven(m):
    # Seven Fano lines on points 0,...,6.
    lines = [
        frozenset([0, 1, 3]),
        frozenset([0, 2, 5]),
        frozenset([0, 4, 6]),
        frozenset([1, 2, 4]),
        frozenset([1, 5, 6]),
        frozenset([2, 3, 6]),
        frozenset([3, 4, 5]),
    ]

    # Vertex (ell, j) has incidence mask equal to Fano line ell.
    V = frozenset((ell, j) for ell in range(7) for j in range(m))

    B = []
    for point in range(7):
        B_point = frozenset(
            (ell, j)
            for ell, L in enumerate(lines)
            if point in L
            for j in range(m)
        )
        B.append(B_point)

    A = [V - B_point for B_point in B]

    assert all(len(Bi) == 3 * m for Bi in B)
    assert all(len(Ai) == 4 * m for Ai in A)
    assert not has_two_cover(A)
    return V, A

for m in range(1, 5):
    V, bad_seven = fano_bad_seven(m)
    print(m, len(V), len(bad_seven[0]))
```

A direct counterexample to trace preservation in Route 2:

```python
def trace_failure_example(k=4):
    assert k >= 3
    B = frozenset(("b", i) for i in range(k))
    z = ("z", 0)

    A = []
    for i in range(3):
        private = frozenset(("p", i, j) for j in range(k - 2))
        A.append(frozenset([z, ("b", i)]) | private)

    H = [B] + A
    assert is_r_locally_two_coverable(H, 7)

    traces = [edge & B for edge in H]
    assert not has_two_cover(traces[1:4])
    return H, traces
```

## Route Diagnosis

### Proved ledger

- Every \(7\)-locally \(2\)-coverable \(k\)-uniform hypergraph has
  \[
  \tau^*\le(35k)^{1/3}.
  \]
- More generally, with \(q=\lceil r/2\rceil\),
  \[
  \tau^*\le\left(\binom rq k\right)^{1/(q-1)}.
  \]
- For every \(k\),
  \[
  f(k,7)\ge\left\lceil\frac{3k}{4}\right\rceil.
  \]
- The lower examples have \(\tau^*<7/4\), so their integral/fractional gap is \((3/4-o(1))k\).
- The \(3/7\) complement-density threshold is sharp by the Fano plane.
- For every fixed \(r\), \(f(k,r)=\Omega_r(k)\), although existence of a normalized limit remains open.

### Plausible but unproved

- The complete \(k\)-uniform construction may be asymptotically extremal for \(r=7\).
- Equivalently, the still-needed statement is
  \[
  \tau(\mathcal H)\le(3/4+o(1))k
  \]
  for all admissible \(\mathcal H\). None of the fractional arguments approaches this integral conclusion.

### Dead ends

1. **Asymptotically lossless LP rounding is false.**  
   The conjectured lower construction itself has bounded \(\tau^*\) and linear \(\tau\). Route 3 cannot work in its stated form.

2. **Passing to traces on a matching core does not preserve local coverability.**  
   The explicit computation above gives a \(k\)-uniform family consisting of one edge \(B\) and three edges sharing an external point \(z\). The original family is globally two-coverable, while three traces on \(B\) have transversal number three.

3. **Private-edge incidence alone is insufficient.**  
   In the complete construction, if \(T\) is a minimum transversal and \(x\in T\), then
   \[
   E_x=([n]\setminus T)\cup\{x\}
   \]
   is private to \(x\), and all these private edges share the same \(k-1\) external vertices. Thus high-degree external vertices are not an exceptional pathology; they occur in the sharp lower example. Any private-edge argument must use the rest of the hypergraph and the full minimum-transversal condition, not merely the selected private edges.

A fresh attempt should therefore target the integral cover directly, most likely through a classification or compression theorem for \(\tau\)-critical dual incidence systems. Fractional matching data are too weak: on the expected extremizers they contain only \(O(1)\) information while the desired transversal has order \(k\).