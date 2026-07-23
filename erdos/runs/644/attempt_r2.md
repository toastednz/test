STATUS: BLOCKED

## Result

Route 2 yields a clean but lossy reduction: if \(\mathcal H\) contains disjoint edges \(B,C\), then every five other edges have traces on \(B\cup C\) covered by a cross-pair \((b,c)\in B\times C\). However, the trace family need not itself be \(7\)-locally 2-coverable; I give an explicit \(k\)-uniform counterexample for every \(k\ge6\). I also prove the matching lower bound
\[
f(k,7)\ge \left\lceil\frac{3k}{4}\right\rceil
\]
for every \(k\), using all \(k\)-subsets of a suitably chosen ground set. Thus the entire lower-bound half of Q1 is established, but the universal upper bound remains open. The maximal-matching route is blocked because external witnesses cannot be compressed merely by incidence type, and because the surviving core condition is not presently strong enough to force a \((3/4+o(1))k\)-transversal.

## Complete Argument

### 1. A weighted intersecting-mask lemma

#### Lemma 1

Let \(\mathcal M\) be a finite multiset of nonempty subsets of \([7]\), with total multiplicity \(N\), such that any two members of \(\mathcal M\) intersect. For \(i\in[7]\), let
\[
d_i=\bigl|\{M\in\mathcal M:i\in M\}\bigr|,
\]
counting multiplicity. Then
\[
\max_{i\in[7]}d_i\ge \frac{3N}{7}.
\]

#### Proof

If \(\mathcal M\) contains a member \(S\) with \(|S|\le2\), every member of \(\mathcal M\) intersects \(S\). Consequently,
\[
\sum_{i\in S}d_i\ge N,
\]
and hence
\[
\max_i d_i\ge \frac{N}{|S|}\ge \frac N2\ge \frac{3N}{7}.
\]

Otherwise every member has size at least three, so
\[
\sum_{i=1}^7 d_i
 =\sum_{M\in\mathcal M}|M|
 \ge 3N.
\]
Averaging over the seven coordinates gives
\[
\max_i d_i\ge \frac{3N}{7}.
\]
This proves the lemma. \(\square\)

The constant \(3/7\) is sharp: the seven lines of the Fano plane form seven pairwise-intersecting triples on seven points, with every point lying on three lines.

---

### 2. A complete lower construction for every \(k\)

#### Theorem 2

Under the at-most-seven convention,
\[
f(k,7)\ge \left\lceil\frac{3k}{4}\right\rceil
\qquad(k\ge1).
\]

#### Proof

Set
\[
n=\left\lceil\frac{7k}{4}\right\rceil-1
\]
and let
\[
\mathcal H=\binom{[n]}{k}
\]
be the complete \(k\)-uniform hypergraph on \([n]\). Put
\[
q=n-k=\left\lceil\frac{3k}{4}\right\rceil-1.
\]

We first prove that \(\mathcal H\) satisfies \(P_7\). Since
\[
n<\frac{7k}{4},
\]
we have
\[
k>\frac{4n}{7},
\qquad\text{and therefore}\qquad
q=n-k<\frac{3n}{7}.
\tag{10}
\]

Suppose, toward a contradiction, that some \(s\le7\) edges
\[
A_1,\dots,A_s\in\mathcal H
\]
have no two-point transversal. Let
\[
C_i=[n]\setminus A_i.
\]
Each \(C_i\) has size \(q\). Add empty sets \(C_{s+1},\dots,C_7\) if \(s<7\).

For each vertex \(v\in[n]\), define its complement-incidence mask
\[
M_v=\{i\in[7]:v\in C_i\}.
\]
Because the selected edges have no one-point transversal, each \(M_v\) is nonempty. Because they have no two-point transversal, for any vertices \(u,v\in[n]\), there is some selected edge avoiding both. Equivalently,
\[
M_u\cap M_v\ne\varnothing.
\]
Thus the multiset
\[
\{M_v:v\in[n]\}
\]
is pairwise intersecting.

Lemma 1 now gives a coordinate \(i\in[7]\) belonging to at least \(3n/7\) masks. But the number of masks containing coordinate \(i\) is exactly \(|C_i|\). For \(i\le s\), this is \(q\), while for an added coordinate it is zero. Hence
\[
q\ge\frac{3n}{7},
\]
contradicting (10). Therefore every at most seven edges of \(\mathcal H\) have a two-point transversal.

It remains to compute \(\tau(\mathcal H)\). A set \(T\subseteq[n]\) meets every \(k\)-subset if and only if its complement has size at most \(k-1\). Hence
\[
\tau(\mathcal H)=n-k+1=q+1
 =\left\lceil\frac{3k}{4}\right\rceil.
\]
Therefore
\[
f(k,7)\ge\left\lceil\frac{3k}{4}\right\rceil.
\]
\(\square\)

In particular,
\[
\liminf_{k\to\infty}\frac{f(k,7)}k\ge\frac34.
\]

This covers every \(k\), rather than merely a subsequence.

---

### 3. What a disjoint maximal matching really gives

#### Lemma 3: Cross-pair trace reduction

Let \(\mathcal H\) satisfy \(P_7\), and let \(B,C\in E(\mathcal H)\) be disjoint. Put
\[
U=B\cup C.
\]
Then:

1. every edge of \(\mathcal H\) meets \(U\);
2. for every collection of at most five edges
   \[
   A_1,\dots,A_s\in E(\mathcal H)\setminus\{B,C\},
   \qquad s\le5,
   \]
   there are \(b\in B\) and \(c\in C\) such that
   \[
   A_j\cap\{b,c\}\ne\varnothing
   \qquad(1\le j\le s).
   \tag{11}
   \]

Thus every at most five traces \(A_j\cap U\) are covered by a cross-pair from \(B\times C\).

#### Proof

If an edge \(D\) were disjoint from \(U\), the three edges \(B,C,D\) would be pairwise disjoint and therefore could not be covered by two points, contrary to \(P_7\). This proves the first assertion.

Apply \(P_7\) to
\[
B,C,A_1,\dots,A_s.
\]
Any pair meeting both disjoint sets \(B\) and \(C\) must contain one point \(b\in B\) and one point \(c\in C\). That same pair meets all the \(A_j\), proving (11). \(\square\)

The corresponding trace system consists of nonempty sets
\[
X_A\cup Y_A,\qquad
X_A=A\cap B,\quad Y_A=A\cap C,
\]
with
\[
|X_A|+|Y_A|\le k.
\]
The local condition can equivalently be written in rectangle language. Define
\[
R_A=(B\setminus X_A)\times(C\setminus Y_A).
\]
A cross-pair \((b,c)\) misses \(A\) exactly when \((b,c)\in R_A\). Hence Lemma 3 says that no five of the rectangles \(R_A\) cover \(B\times C\).

Any transversal of the trace family is also a transversal of \(\mathcal H\), so
\[
\tau(\mathcal H)\le
\tau\bigl(\{A\cap U:A\in E(\mathcal H)\}\bigr).
\tag{12}
\]
The missing step is a sharp upper bound for the right side.

---

### 4. External witnesses cannot simply be deleted

The warning that traces need not retain the original local condition is genuine even in a very small explicit example.

#### Proposition 4

For every \(k\ge6\), there is a \(k\)-uniform hypergraph
\[
\mathcal H_k=\{B,C,D_0,\dots,D_5\}
\]
such that:

1. \(B\cap C=\varnothing\);
2. \(\mathcal H_k\) satisfies \(P_7\);
3. the six traces \(D_i\cap(B\cup C)\) have no two-point transversal;
4. the full eight-edge family has transversal number exactly three.

#### Construction

Let
\[
B=\{b_0,\dots,b_{k-1}\},\qquad
C=\{c_0,\dots,c_{k-1}\}.
\]
Assign to each point a mask contained in \(\{0,1,2,3,4,5\}\).

For \(b_j\in B\), define
\[
I_{b_j}=
\begin{cases}
\{0,1,j\},&j\in\{3,4,5\},\\
\{0,1,2\},&\text{otherwise}.
\end{cases}
\]
For \(c_j\in C\), define
\[
J_{c_j}=
\begin{cases}
\{0,3,4,5\},&j=0,\\
\{1,3,4,5\},&j=1,\\
\{2,3,4,5\},&j\ge2.
\end{cases}
\]

For \(i\in\{0,\dots,5\}\), define the trace
\[
T_i=
\{b\in B:i\notin I_b\}
\cup
\{c\in C:i\notin J_c\}.
\tag{13}
\]

A direct count gives
\[
|T_i|=k-1\quad(i\ne2),
\qquad
|T_2|=5.
\tag{14}
\]

Let \(z\) be a new vertex. Define
\[
D_i=T_i\cup\{z\}
\quad(i\ne2),
\]
and
\[
D_2=T_2\cup\{z\}\cup P,
\]
where \(P\) is a set of \(k-6\) new private vertices, disjoint from all previously used vertices. By (14), all eight edges have size \(k\).

#### Verification of \(P_7\)

For each \(i\in\{0,\dots,5\}\), choose the points \(b_i,c_i\). Their masks satisfy
\[
I_{b_i}\cap J_{c_i}=\{i\}.
\tag{15}
\]

Consider any at most five of the six edges \(D_0,\dots,D_5\). Choose an omitted index \(i\). If \(j\ne i\), equation (15) implies that at least one of \(b_i,c_i\) has \(j\) absent from its mask, and therefore belongs to \(T_j\subseteq D_j\). Hence \(\{b_i,c_i\}\) covers all the chosen \(D_j\).

Now consider any subfamily of \(\mathcal H_k\) with at most seven edges.

- If it contains neither \(B\) nor \(C\), then \(z\) covers all its edges.
- If it contains exactly one of \(B,C\), then \(z\), together with any point of that core edge, covers the subfamily.
- If it contains both \(B\) and \(C\), it contains at most five of the \(D_i\), and the cross-pair just constructed covers them as well as \(B,C\).

Thus \(\mathcal H_k\) satisfies \(P_7\).

#### The traces have no two-point transversal

A point \(u\in B\cup C\) lies outside \(T_i\) exactly when \(i\) belongs to its mask.

- Any two \(B\)-masks intersect, because every \(I_b\) contains \(0\) and \(1\).
- Any two \(C\)-masks intersect, because every \(J_c\) contains \(3,4,5\).
- Every \(B\)-mask has size three and every \(C\)-mask has size four in a six-element universe, so every \(B\)-mask intersects every \(C\)-mask.

Consequently, for every pair \(u,v\in B\cup C\), there is an index \(i\) belonging to both masks. Then \(u,v\notin T_i\), so \(\{u,v\}\) misses \(T_i\). Therefore
\[
\tau(\{T_0,\dots,T_5\})>2.
\]

Finally, the full eight-edge family is not covered by two points. A pair hitting both disjoint edges \(B,C\) must be a cross-pair \(b,c\), and the masks of \(b,c\) intersect, so that pair misses some \(D_i\). On the other hand,
\[
\{z,b,c\}
\]
hits all eight edges for any \(b\in B,c\in C\). Thus
\[
\tau(\mathcal H_k)=3.
\]
\(\square\)

This example proves that deleting external vertices can destroy local 2-coverability, even though the original family satisfies the condition exactly up to seven edges.

---

### 5. The intersecting case reduces to a near-disjoint core

If no disjoint pair exists, a maximal matching has size one and the family is intersecting. A basic intersection bound isolates the hard regime.

#### Lemma 5

Let \(B\) be an edge of a hypergraph and suppose
\[
d=\min_{A\in E(\mathcal H)}|A\cap B|\ge1.
\]
Then
\[
\tau(\mathcal H)\le k-d+1.
\]

#### Proof

Choose any \(S\subseteq B\) with
\[
|S|=k-d+1.
\]
Then
\[
|B\setminus S|=d-1.
\]
Every edge \(A\) has at least \(d\) points in \(B\), so \(A\cap B\) cannot be contained in \(B\setminus S\). Hence \(A\cap S\ne\varnothing\). Thus \(S\) is a transversal. \(\square\)

In particular, if some \(B\) satisfies
\[
|A\cap B|\ge \frac{k}{4}-o(k)
\qquad\text{for all }A,
\]
then
\[
\tau(\mathcal H)\le\left(\frac34+o(1)\right)k.
\]

Conversely, high transversal number forces near-disjoint edges.

#### Lemma 6

If \(\tau(\mathcal H)>t\), where \(t\le k\), then for every edge \(B\) and every \(t\)-subset \(S\subseteq B\), there is an edge \(C\) such that
\[
C\cap S=\varnothing
\quad\text{and hence}\quad
|B\cap C|\le k-t.
\]

#### Proof

The set \(S\) is not a transversal because \(|S|=t<\tau(\mathcal H)\). Thus some edge \(C\) is disjoint from \(S\). Since \(B\setminus S\) has \(k-t\) points,
\[
B\cap C\subseteq B\setminus S
\]
and the claimed bound follows. \(\square\)

Suppose now that \(\mathcal H\) is intersecting, \(\tau(\mathcal H)>t\), and \(B,C\) are supplied by Lemma 6. Put
\[
I=B\cap C,\qquad s=|I|\le k-t,
\]
and let
\[
\mathcal H_0=\{A\in E(\mathcal H):A\cap I=\varnothing\}.
\]

#### Lemma 7: Common-or-cross residual condition

Every at most five edges \(A_1,\dots,A_m\in\mathcal H_0\) satisfy at least one of the following:

1. they have a common vertex;
2. they are covered by a cross-pair
   \[
   b\in B\setminus I,\qquad c\in C\setminus I.
   \]

#### Proof

Apply \(P_7\) to
\[
B,C,A_1,\dots,A_m.
\]
Let \(\{x,y\}\) be a witness.

If one of \(x,y\), say \(x\), lies in \(I\), then \(x\) lies in none of the \(A_j\). Therefore \(y\) must lie in every \(A_j\), giving the first alternative.

If neither witness point lies in \(I\), then to hit both \(B\) and \(C\), one must lie in \(B\setminus I\) and the other in \(C\setminus I\). This gives the second alternative. \(\square\)

The set \(I\) covers all edges outside \(\mathcal H_0\). Hence a proof of
\[
\tau(\mathcal H_0)\le t-s
\tag{16}
\]
would imply \(\tau(\mathcal H)\le t\).

At the conjectured threshold \(t\sim3k/4\), one may have \(s\sim k/4\), so (16) requires a roughly \(k/2\)-sized transversal of \(\mathcal H_0\). The complete-hypergraph lower construction realizes this scale, so there is essentially no slack. I do not have a proof of (16); it is a residual problem of comparable difficulty to the original upper bound.

---

### 6. A naive \(O(k)\)-type kernel is impossible

One hoped-for Route 2 statement was that external vertices might be replaced by \(O(k)\) incidence types. This is false if “type” means an inclusion-maximal dual incidence set.

Fix \(k\ge2\) and put \(d=k-1\). For arbitrarily large \(N>d\), let \(G\) be a simple \(d\)-regular bipartite graph with parts
\[
L=\{1,\dots,N\},\qquad R=\{1,\dots,N\}.
\]
For every graph edge \(ij\), introduce a vertex \(e_{ij}\), and introduce two additional vertices \(z,w\). Define
\[
Z_i=\{z\}\cup\{e_{ij}:ij\in E(G)\},
\]
\[
W_j=\{w\}\cup\{e_{ij}:ij\in E(G)\}.
\]
All these edges have size \(d+1=k\). The pair \(\{z,w\}\) covers the whole hypergraph, so it satisfies \(P_r\) for every \(r\).

Choose a nonedge \(i_0j_0\) and put
\[
B=Z_{i_0},\qquad C=W_{j_0}.
\]
Then \(B\cap C=\varnothing\). For every graph edge \(ij\) with \(i\ne i_0\) and \(j\ne j_0\), the vertex \(e_{ij}\) lies outside \(B\cup C\) and has dual incidence set
\[
D_{e_{ij}}=\{Z_i,W_j\}.
\]
These sets are all distinct and inclusion-maximal among vertex incidence sets:

- they are not contained in \(D_z=\{Z_1,\dots,Z_N\}\), because they contain \(W_j\);
- they are not contained in \(D_w=\{W_1,\dots,W_N\}\), because they contain \(Z_i\);
- no other link vertex has a strictly larger incidence set.

There are at least \(d(N-2)\) such external types, which is unbounded for fixed \(k\). Thus local 2-coverability alone does not bound the number of undominated external incidence types by \(O(k)\).

This does not rule out a more sophisticated optimization-preserving kernel, but it blocks the most direct incidence-type compression.

---

### 7. A quantitative barrier to a simple rectangle-cover argument

Suppose \(B,C\) are disjoint \(k\)-edges and \(\tau(\mathcal H)>t\). For any \(t\)-set \(S\subseteq B\cup C\), there is an edge \(A\) disjoint from \(S\). Its complement rectangle
\[
R_A=(B\setminus A)\times(C\setminus A)
\]
contains
\[
(S\cap B)\times(S\cap C).
\]

A tempting strategy is to preselect five \(t\)-sets \(S_1,\dots,S_5\) whose induced rectangles cover \(B\times C\), and then choose five edges avoiding them. This cannot work near \(t=3k/4\).

Write
\[
a_j=|S_j\cap B|,\qquad b_j=|S_j\cap C|,
\]
so \(a_j+b_j=t\). If the five induced rectangles cover \(B\times C\), then
\[
k^2
 \le \sum_{j=1}^5a_jb_j
 \le 5\frac{t^2}{4}.
\]
Consequently,
\[
t\ge \frac{2k}{\sqrt5}\approx0.8944k.
\]
Thus a proof based only on five preassigned missed \(t\)-sets cannot approach the conjectured \(3k/4\). Any successful argument must exploit the extra portions of the actual complement rectangles or additional structure beyond \(\tau>t\).

## Self-Audit

1. **The lower construction hinges on translating failure of a two-point transversal into pairwise-intersecting masks.**  
   This is the most delicate logical conversion. It holds because if \(\{u,v\}\) misses no selected edge, it is a transversal; therefore failure of every pair means some complement contains both \(u\) and \(v\), exactly saying \(M_u\cap M_v\ne\varnothing\). The strict inequality \(q<3n/7\) is verified from \(n<7k/4\).

2. **The trace counterexample has several indexed mask calculations where a transcription error would be easy.**  
   The essential checks are explicit: all \(B\)-masks contain \(0,1\), all \(C\)-masks contain \(3,4,5\), every cross pair of masks intersects by \(3+4>6\), and \(I_{b_i}\cap J_{c_i}=\{i\}\). The supplied code below exhaustively verifies the construction.

3. **The kernel obstruction has deliberately limited scope.**  
   It proves only that one cannot retain one representative of every inclusion-maximal incidence type and hope for \(O(k)\) types. It does not prove that every possible optimization-preserving compression is impossible. I have not used it to claim more than that.

## Computations To Verify

```python
from itertools import combinations
from math import ceil

def has_two_cover(F):
    """F is a list/tuple of finite sets."""
    if not F:
        return True
    U = set().union(*F)

    # One-point transversals
    for x in U:
        if all(x in A for A in F):
            return True

    # Two distinct points
    for x, y in combinations(U, 2):
        if all((x in A) or (y in A) for A in F):
            return True
    return False

def local_ok(edges, r=7):
    m = len(edges)
    for s in range(1, min(r, m) + 1):
        for F in combinations(edges, s):
            if not has_two_cover(F):
                return False, F
    return True, None

def transversal_number(edges):
    U = sorted(set().union(*edges), key=repr)
    for t in range(len(U) + 1):
        for T in combinations(U, t):
            T = set(T)
            if all(T & A for A in edges):
                return t, T
    raise RuntimeError("impossible")

# ------------------------------------------------------------
# Complete-hypergraph lower construction
# Practical for small k only: k <= 4 is quick.
# ------------------------------------------------------------

def complete_lower_example(k):
    n = (7*k + 3)//4 - 1  # ceil(7k/4)-1
    V = range(n)
    edges = [frozenset(A) for A in combinations(V, k)]
    return n, edges

for k in range(1, 5):
    n, E = complete_lower_example(k)
    ok, bad = local_ok(E, 7)
    tau, witness = transversal_number(E)
    print("complete", k, n, len(E), ok, tau, ceil(3*k/4))
    assert ok
    assert tau == ceil(3*k/4)

# ------------------------------------------------------------
# Explicit trace-preservation counterexample, valid for k >= 6.
# ------------------------------------------------------------

def trace_counterexample(k):
    assert k >= 6

    B = frozenset(("b", j) for j in range(k))
    C = frozenset(("c", j) for j in range(k))

    I = {}
    for j in range(k):
        if j in (3, 4, 5):
            I[("b", j)] = frozenset((0, 1, j))
        else:
            I[("b", j)] = frozenset((0, 1, 2))

    J = {}
    for j in range(k):
        if j == 0:
            J[("c", j)] = frozenset((0, 3, 4, 5))
        elif j == 1:
            J[("c", j)] = frozenset((1, 3, 4, 5))
        else:
            J[("c", j)] = frozenset((2, 3, 4, 5))

    traces = []
    for i in range(6):
        T = {b for b in B if i not in I[b]}
        T |= {c for c in C if i not in J[c]}
        traces.append(frozenset(T))

    assert [len(T) for T in traces] == [
        k-1, k-1, 5, k-1, k-1, k-1
    ]

    z = ("z", 0)
    D = []
    for i, T in enumerate(traces):
        filler_count = k - len(T) - 1
        filler = {("private", i, h) for h in range(filler_count)}
        D.append(frozenset(set(T) | {z} | filler))
        assert len(D[-1]) == k

    edges = [B, C] + D
    return edges, traces

for k in range(6, 13):
    E, traces = trace_counterexample(k)

    ok, bad = local_ok(E, 7)
    assert ok, bad

    # The six traces have no two-point transversal.
    assert not has_two_cover(traces)

    # The full eight-edge hypergraph has tau exactly 3.
    tau, witness = transversal_number(E)
    assert tau == 3

    print("trace counterexample", k, "verified")

# ------------------------------------------------------------
# Restricted trace-system ILP/SAT search blueprint.
#
# Search for a family of rank-at-most-k traces on B union C:
#   - B and C are selected;
#   - every at most five selected traces have a cross-pair;
#   - no t-set of B union C is a transversal.
#
# This tests whether the trace-only consequence of Lemma 3 might
# imply a sharp upper bound. It does not enforce the full original
# P_7 condition involving external vertices.
# ------------------------------------------------------------

def cross_coverable(F, B, C):
    return any(
        all((b in A) or (c in A) for A in F)
        for b in B for c in C
    )

"""
B = {0,...,k-1}
C = {k,...,2k-1}

candidates = all nonempty subsets A of B union C with |A| <= k
binary variable x[A] says trace A is selected
force x[B] = x[C] = 1

For every F of 1,...,5 candidate traces with no cross-pair:
    sum(x[A] for A in F) <= len(F)-1

To force transversal number > t, for every t-subset S of B union C:
    sum(x[A] for A in candidates if A.isdisjoint(S)) >= 1

Solve as a 0-1 feasibility problem.
Record any solution with t > ceil(3*k/4).
"""
```

## Route Diagnosis

### Proved ledger

- The mask inequality \(\max_i d_i\ge3N/7\) for pairwise-intersecting masks on seven coordinates.
- The all-\(k\)-subsets construction proving
  \[
  f(k,7)\ge\left\lceil\frac{3k}{4}\right\rceil
  \]
  for every \(k\).
- The exact disjoint-core reduction: after fixing disjoint \(B,C\), every five other traces are covered by a cross-pair from \(B\times C\).
- An explicit family showing that traces need not retain \(P_7\), or even \(P_6\).
- The dense-intersection upper bound
  \[
  \tau(\mathcal H)\le k-d+1.
  \]
- The near-disjoint-core consequence of large transversal number.
- The common-or-cross residual condition after deleting \(B\cap C\).
- The impossibility of bounding all undominated external incidence types by \(O(k)\).
- The \(2/\sqrt5\) barrier for a simple five-preassigned-rectangle argument.

### Plausible but unproved

A successful Route 2 theorem would need to exploit more than the cross-\(P_5\) trace condition. In the intersecting case, it would suffice to prove a sharp transversal bound for the residual system \(\mathcal H_0\) from Lemma 7. I have no proof, and that residual statement appears comparable in strength to the original upper-bound problem.

A more sophisticated kernel might retain only vertices relevant to near-minimum transversals or to minimal seven-edge witnesses, rather than all maximal incidence types. The regular bipartite example rules out only the naive type compression.

### Dead ends

- **Delete all external vertices:** false, by Proposition 4.
- **Keep one representative of every maximal incidence type:** cannot give an \(O(k)\) kernel.
- **Choose five \(t\)-sets in advance and then choose edges avoiding them:** cannot beat \(2k/\sqrt5\), well above \(3k/4\).
- **Use only the existence of a \(2k\)-point matching core:** this loses precisely the external common-point alternatives that can certify \(P_7\).

### Final diagnosis

The lower-bound half of Q1 is complete. Route 2 does expose the hard upper-bound structure, especially the near-disjoint pair with overlap at most \(k/4+o(k)\), but it does not presently yield the required transversal. A fresh attempt should combine the near-disjoint core with private edges of a minimum transversal, rather than treating traces alone. In particular, the residual “every five are common-point-covered or cross-covered” condition should be tested computationally for a sharp \(t-s\) transversal theorem. Q2 remains unresolved as well; none of these reductions supplies the approximate subadditivity or interpolation needed for existence of \(c_r\).