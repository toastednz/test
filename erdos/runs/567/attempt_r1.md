STATUS: BLOCKED
## Result

Route 1 yields a rigorous deterministic reservoir lemma for complements of \(K_{s,s}\)-free graphs. Consequently, both \(K_{3,3}\) and \(Q_3\) are Ramsey size linear against every fixed-degeneracy target, including disconnected targets and targets of unbounded maximum degree. More precisely, if \(H\) is \(d\)-degenerate with \(m\) edges and no isolated vertices, then \(R(K_{3,3},H)\le C_{3,d}m\) and \(R(Q_3,H)\le C_{4,d}m\). I also prove exact local restrictions in \(H_5\)-free graphs. However, the reservoir argument incurs a cost polynomial in the target’s backward degree and fails badly on cliques. Removing that loss would already prove the unresolved benchmark \(R(K_{3,3},K_t)=O(t^2)\). For \(H_5\), even the first bounded-obstruction-set lemma is false, as complete bipartite red graphs demonstrate. Thus Route 1 is genuinely blocked at a statement of comparable strength to the original problem.

## Complete Argument

### 1. A local incidence lemma for \(K_{s,s}\)-free graphs

We begin with the precise common-neighbour fact driving the successful part of Route 1.

**Lemma 1.**  
Let \(s\ge2\), let \(F\) be \(K_{s,s}\)-free, and let \(U\subseteq V(F)\), with \(u=|U|\). For \(0<\eta\le1\), suppose \(\eta u\ge2s\), and define
\[
B_\eta(U)=\{x\in V(F): |N_F(x)\cap U|>\eta u\}.
\]
Then
\[
|B_\eta(U)|\le (s-1)\left(\frac2\eta\right)^s.
\]

**Proof.**  
Count pairs \((x,S)\) such that \(x\in V(F)\), \(S\in\binom Us\), and
\[
S\subseteq N_F(x).
\]
For any fixed \(S\in\binom Us\), there are at most \(s-1\) possible vertices \(x\). Indeed, \(s\) distinct common neighbours of \(S\) together with \(S\) would span a \(K_{s,s}\). The two sides are automatically disjoint: no \(x\in S\) can be adjacent to every vertex of \(S\), since \(F\) has no loops.

It follows that
\[
\sum_{x\in V(F)}\binom{|N_F(x)\cap U|}{s}
   \le (s-1)\binom us.
\]
If \(x\in B_\eta(U)\), then \(d_U(x)=|N_F(x)\cap U|>\eta u\). Since \(\eta u\ge2s\), for every \(0\le k<s\),
\[
d_U(x)-k>\eta u-(s-1)\ge \frac{\eta u}{2}.
\]
Consequently,
\[
\binom{d_U(x)}s
 =\frac1{s!}\prod_{k=0}^{s-1}(d_U(x)-k)
 \ge \frac1{s!}\left(\frac{\eta u}{2}\right)^s.
\]
Therefore
\[
|B_\eta(U)|\frac1{s!}\left(\frac{\eta u}{2}\right)^s
 \le (s-1)\binom us
 \le (s-1)\frac{u^s}{s!}.
\]
Cancelling gives the claimed bound. \(\square\)

This estimate is independent of the ambient order and the size of \(U\), provided \(\eta|U|\ge2s\).

---

### 2. A nonuniform cluster embedding theorem

The next theorem translates Lemma 1 into a deterministic reservoir embedding. Its nonuniform form is useful because it charges the cost according to an ordering of the target.

**Theorem 2.**  
Let \(s\ge2\), and let \(H\) have an ordering
\[
h_1,h_2,\dots,h_n.
\]
For each \(j\), let
\[
b_j=\bigl|N_H(h_j)\cap\{h_1,\dots,h_{j-1}\}\bigr|,
\qquad
q_j=\max\{1,b_j\},
\]
and define
\[
B_j=(s-1)(4q_j)^s.
\]
For every \(i\), set
\[
L_i=8s q_i+2+
2\sum_{\substack{j>i\\h_ih_j\in E(H)}}B_j.
\]
If \(F\) is a \(K_{s,s}\)-free graph on at least
\[
L=\sum_{i=1}^n L_i
\]
vertices, then \(\overline F\) contains a copy of \(H\).

**Proof.**  
We may restrict to an arbitrary set of exactly \(L\) vertices. Partition it into pairwise disjoint clusters
\[
V_1,\dots,V_n,\qquad |V_i|=L_i.
\]
We embed \(h_1,\dots,h_n\) in that order. For each unembedded \(h_j\), maintain a candidate set
\[
C_j\subseteq V_j.
\]
Initially \(C_j=V_j\). Whenever \(h_i\) is embedded as \(x_i\), for every unembedded neighbour \(h_j\) of \(h_i\), replace
\[
C_j\leftarrow C_j\setminus N_F(x_i).
\]
Thus every vertex left in \(C_j\) is blue-adjacent to the images of all already embedded neighbours of \(h_j\).

Put
\[
\eta_j=\frac1{2q_j}.
\]
We maintain the additional condition that whenever \(h_i\) is embedded and \(h_j\) is an unembedded neighbour, the chosen image \(x_i\) satisfies
\[
|N_F(x_i)\cap C_j|\le \eta_j|C_j|.
\]

A candidate set \(C_j\) undergoes at most \(b_j\) updates. Every update leaves at least a proportion \(1-\eta_j\) of the current set. If \(b_j=0\), it is never updated. If \(b_j\ge1\), then \(q_j=b_j\), and Bernoulli’s inequality gives
\[
(1-\eta_j)^{b_j}
 =\left(1-\frac1{2b_j}\right)^{b_j}
 \ge 1-\frac{b_j}{2b_j}
 =\frac12.
\]
Hence, throughout the embedding,
\[
|C_j|\ge \frac{L_j}{2}\ge4sq_j.
\]
In particular,
\[
\eta_j|C_j|
 \ge \frac1{2q_j}\cdot4sq_j
 =2s.
\]

Consider the stage at which \(h_i\) is to be embedded. For each future neighbour \(h_j\), call a vertex \(x\) bad for \(j\) if
\[
|N_F(x)\cap C_j|>\eta_j|C_j|.
\]
Lemma 1, applied with \(U=C_j\) and \(\eta=\eta_j\), shows that the total number of vertices bad for \(j\) is at most
\[
(s-1)\left(\frac2{\eta_j}\right)^s
 =(s-1)(4q_j)^s
 =B_j.
\]
The union of all bad sets corresponding to future neighbours of \(h_i\) therefore has size at most
\[
\sum_{\substack{j>i\\h_ih_j\in E(H)}}B_j.
\]
On the other hand,
\[
|C_i|\ge\frac{L_i}{2}
 =4sq_i+1+
 \sum_{\substack{j>i\\h_ih_j\in E(H)}}B_j
 >
 \sum_{\substack{j>i\\h_ih_j\in E(H)}}B_j.
\]
Thus \(C_i\) contains a vertex \(x_i\) that is not bad for any future neighbour. Choose such an \(x_i\).

The clusters are disjoint, so all selected images are distinct. By construction, \(x_i\in C_i\) is blue-adjacent to every previously embedded neighbour of \(h_i\). Every edge of \(H\) is therefore blue when its later endpoint is embedded. This constructs a copy of \(H\) in \(\overline F\). \(\square\)

The exact total order used by this theorem is
\[
\begin{aligned}
L
 &=2n+8s\sum_{i=1}^n q_i
   +2\sum_{i=1}^n
     \sum_{\substack{j>i\\h_ih_j\in E(H)}}B_j\\
 &=2n+8s\sum_{i=1}^n q_i
   +2\sum_{j=1}^n b_jB_j.
\end{aligned}
\]
The second equality holds because \(B_j\) is counted once for every earlier neighbour of \(h_j\).

---

### 3. Consequence for bounded-degeneracy targets

Recall that a graph is \(d\)-degenerate if its vertices admit an ordering in which every vertex has at most \(d\) earlier neighbours. This follows, for example, by repeatedly deleting a vertex of degree at most \(d\) and reversing the deletion order.

**Corollary 3.**  
Let \(H\) be a \(d\)-degenerate graph with \(m\ge1\) edges and no isolated vertices. Put
\[
D=\max\{1,d\}.
\]
Then
\[
R(K_{s,s},H)\le C_{s,d}m,
\]
where one may take
\[
C_{s,d}=4+16sD+2(s-1)(4D)^s.
\]

**Proof.**  
Choose an ordering with \(b_j\le d\), so \(q_j\le D\). Every edge is counted exactly once among the \(b_j\), hence
\[
\sum_j b_j=m.
\]
Using the expression for \(L\) above,
\[
\begin{aligned}
L
&\le 2n+8sDn
   +2(s-1)(4D)^s\sum_j b_j\\
&=(2+8sD)n+2(s-1)(4D)^s m.
\end{aligned}
\]
Because \(H\) has no isolated vertices,
\[
n\le2m.
\]
Therefore
\[
L\le
\left(4+16sD+2(s-1)(4D)^s\right)m.
\]
Theorem 2 now proves the Ramsey bound. \(\square\)

This covers high-maximum-degree targets such as stars: degeneracy, rather than maximum degree, is the relevant parameter.

---

### 4. Applications to \(K_{3,3}\) and \(Q_3\)

Taking \(s=3\) immediately gives:

**Corollary 4.**  
For every fixed \(d\), there is a constant \(C_d\) such that every \(d\)-degenerate no-isolate graph \(H\) with \(m\) edges satisfies
\[
R(K_{3,3},H)\le C_dm.
\]

For the cube, observe that its parity classes form a bipartition with four vertices on each side. Every vertex has degree three, and the four absent cross-edges form a perfect matching. Thus
\[
Q_3\cong K_{4,4}\setminus M
\]
for a perfect matching \(M\). Since copies are not induced, every \(K_{4,4}\) contains a copy of \(Q_3\). Consequently,
\[
Q_3\text{-free}\quad\Longrightarrow\quad K_{4,4}\text{-free}.
\]
Taking \(s=4\) in Corollary 3 therefore gives:

**Corollary 5.**  
For every fixed \(d\), there is a constant \(C'_d\) such that every \(d\)-degenerate no-isolate graph \(H\) with \(m\) edges satisfies
\[
R(Q_3,H)\le C'_dm.
\]

For arbitrary \(m\)-edge targets, the degeneracy satisfies
\[
d(d+1)/2\le m,
\]
because a graph of degeneracy \(d\) contains a subgraph of minimum degree \(d\), which has at least \(d+1\) vertices and at least \(d(d+1)/2\) edges. Hence the same argument gives the non-linear general estimates
\[
R(K_{3,3},H)=O(m^{5/2}),
\qquad
R(Q_3,H)=O(m^3).
\]
These do not meet the problem’s success criterion.

---

### 5. Exact local restrictions for \(H_5\)-free graphs

The corresponding first step for \(H_5\) has a different form.

**Lemma 6.**  
Let \(F\) be \(H_5\)-free, let \(cd\in E(F)\), and put
\[
W=N_F(c)\cap N_F(d).
\]
Then for any distinct \(a,b\in W\),
\[
N_F(a)\cap N_F(b)\subseteq\{c,d\}.
\]
In particular,
\[
\Delta(F[W])\le1.
\]

**Proof.**  
Suppose distinct \(a,b\in W\) had a common neighbour
\[
x\notin\{c,d\}.
\]
The vertices \(a,b,c,d,x\) are all distinct. Indeed, \(a,b\in W\) are distinct from \(c,d\), and a common neighbour of \(a,b\) cannot equal \(a\) or \(b\) in a simple graph.

The following red edges are then present:
\[
cd,\ ca,\ da,\ cb,\ db,\ ax,\ bx.
\]
These are exactly the seven required edges in the description of \(H_5\) from the brief. Extra edges are irrelevant because the copy need not be induced. This contradicts \(H_5\)-freeness.

Now suppose some \(x\in W\) had two distinct neighbours \(a,b\in W\). Then \(x\) would be a common neighbour of \(a,b\) outside \(\{c,d\}\), contrary to the first part. Hence \(\Delta(F[W])\le1\). \(\square\)

Thus \(F[W]\) is a matching together with isolated vertices. It follows that \(\overline F[W]\) contains a clique of size at least
\[
\left\lceil\frac{|W|}{2}\right\rceil.
\]
In particular:

**Corollary 7.**  
If \(F\) is \(H_5\)-free and \(\overline F\) contains no \(K_t\), then every red edge \(cd\) satisfies
\[
|N_F(c)\cap N_F(d)|\le2t-2.
\]

Another exact consequence is useful.

**Lemma 8.**  
If \(F\) is \(H_5\)-free and \(S\) spans a red \(K_4\), then every vertex outside \(S\) has at most one red neighbour in \(S\).

**Proof.**  
Suppose \(x\notin S\) has two red neighbours \(a,b\in S\). Let \(c,d\) be the other two vertices of \(S\). The red \(K_4\) supplies
\[
ac,ad,bc,bd,cd,
\]
and \(x\) supplies \(ax,bx\). These seven edges form \(H_5\), with \(x\) subdividing the edge \(ab\). The possible additional edge \(ab\) does not matter. \(\square\)

These local facts are strong, but I could not turn them into a linear universal embedding theorem.

---

### 6. Why the naive failure-to-certificate implication is false

The central hoped-for implication in Route 1 was that if a candidate reservoir is covered by red neighbourhoods of already embedded vertices, then some large red common-neighbour pattern should emerge. This is false even in forests.

Let
\[
U=U_1\sqcup\cdots\sqcup U_k
\]
and introduce distinct centres \(z_1,\dots,z_k\). Define \(F\) by
\[
E(F)=\{z_i u: u\in U_i,\ 1\le i\le k\}.
\]
This is a disjoint union of stars, so it contains none of \(K_{3,3},Q_3,H_5\). Nevertheless,
\[
U=\bigcup_{i=1}^k N_F(z_i),
\]
while the neighbourhoods \(N_F(z_i)\cap U\) are pairwise disjoint.

If a target vertex is adjacent to already embedded vertices whose images are \(z_1,\dots,z_k\), then it has no permissible blue image in \(U\): every \(u\in U_i\) is red-adjacent to \(z_i\). Yet the obstruction creates no large red common neighbourhood at all. Therefore a fixed partial blue embedding need not be extendable, and union-cover information alone cannot force any of the three local certificates.

For \(H_5\), an even earlier analogue of Lemma 1 is impossible. Let \(F=K_{r,u}\), and let \(U\) be the side of size \(u\). The graph \(F\) is bipartite and hence \(H_5\)-free, but all \(r\) vertices in the opposite side have red degree \(u\) into \(U\). Thus the number of vertices with positive-density red neighbourhood in \(U\) cannot be bounded solely in terms of that density.

## Self-Audit

1. **The most consequential weakness is scope, not a hidden proof gap.**  
   The bounded-degeneracy theorem does not cover cliques of growing order or arbitrary targets. I have explicitly marked the route blocked rather than claiming this restricted theorem solves the problem.

2. **The cluster proof depends delicately on the candidate-set lower bound.**  
   The potential concern is that repeated red-neighbour deletions might make Lemma 1 inapplicable. The explicit invariant
   \[
   |C_j|\ge L_j/2\ge4sq_j
   \]
   ensures \(\eta_j|C_j|\ge2s\) at every stage, exactly the hypothesis required by Lemma 1.

3. **The \(H_5\) certificate requires five distinct vertices.**  
   This is easy to mishandle. In Lemma 6, \(a,b\in N(c)\cap N(d)\) are distinct from \(c,d\), and a common neighbour \(x\) of \(a,b\) cannot equal \(a\) or \(b\) in a simple graph. The assumption \(x\notin\{c,d\}\) therefore guarantees all five vertices are distinct.

## Computations To Verify

The following Python code exhaustively checks the \(H_5\) local lemmas for small orders and provides direct certificate routines.

```python
from itertools import combinations, permutations
from math import comb

def graph_from_mask(n, mask):
    edges = list(combinations(range(n), 2))
    A = [set() for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            A[u].add(v)
            A[v].add(u)
    return A

def has_kss(A, s):
    n = len(A)
    V = set(range(n))
    for S in combinations(range(n), s):
        common = V.copy()
        for v in S:
            common &= A[v]
        # Simplicity automatically makes common disjoint from S.
        if len(common) >= s:
            return True
    return False

def has_h5(A):
    n = len(A)
    for c in range(n):
        for d in A[c]:
            if c >= d:
                continue
            W = A[c] & A[d]
            for a, b in combinations(W, 2):
                common = (A[a] & A[b]) - {c, d}
                if common:
                    return True
    return False

def has_q3(A):
    n = len(A)
    if n < 8:
        return False
    V = set(range(n))
    for left in combinations(range(n), 4):
        rest = V - set(left)
        for right in combinations(rest, 4):
            # matched[i] is the one cross-edge allowed to be absent
            for matched in permutations(right):
                ok = True
                for i, x in enumerate(left):
                    for y in right:
                        if y != matched[i] and y not in A[x]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return True
    return False

def check_h5_local_consequences(A):
    if has_h5(A):
        return True

    n = len(A)

    # Lemma 6
    for c in range(n):
        for d in A[c]:
            if c >= d:
                continue
            W = A[c] & A[d]
            for a, b in combinations(W, 2):
                assert (A[a] & A[b]) <= {c, d}
            for x in W:
                assert len(A[x] & W) <= 1

    # Lemma 8
    for S_tuple in combinations(range(n), 4):
        S = set(S_tuple)
        if all(v in A[u] for u, v in combinations(S_tuple, 2)):
            for x in set(range(n)) - S:
                assert len(A[x] & S) <= 1

    return True

# Exhaustive verification. n <= 7 is about 2 million graphs at n=7.
for n in range(1, 8):
    E = comb(n, 2)
    for mask in range(1 << E):
        A = graph_from_mask(n, mask)
        check_h5_local_consequences(A)
```

A direct simulation of the embedding algorithm in Theorem 2 is:

```python
def route1_cluster_embed(red, target, order, clusters, s):
    """
    red[v] and target[v] are adjacency sets.
    order is a list of target vertices.
    clusters[pos] is the ambient cluster assigned to order[pos].
    """
    n = len(order)
    pos = {v: i for i, v in enumerate(order)}

    b = []
    for j, v in enumerate(order):
        b.append(sum(pos[u] < j for u in target[v]))
    q = [max(1, x) for x in b]
    B = [(s - 1) * (4 * x) ** s for x in q]

    for i, v in enumerate(order):
        required = 8 * s * q[i] + 2
        required += 2 * sum(
            B[j] for j in range(i + 1, n)
            if order[j] in target[v]
        )
        assert len(clusters[i]) >= required

    C = [set(X) for X in clusters]
    image = {}

    for i, v in enumerate(order):
        future = [
            j for j in range(i + 1, n)
            if order[j] in target[v]
        ]

        good = []
        for x in C[i]:
            # Equivalent to red degree <= |C[j]|/(2q[j])
            if all(
                2 * q[j] * len(red[x] & C[j]) <= len(C[j])
                for j in future
            ):
                good.append(x)

        assert good, "Would contradict the counting proof"
        x = good[0]
        image[v] = x

        for j in future:
            C[j] -= red[x]

    # Verify every target edge maps to a blue ambient edge.
    for u in target:
        for v in target[u]:
            if pos[u] < pos[v]:
                assert image[v] not in red[image[u]]

    return image
```

For clique-target searches, the following brute-force routine records
\[
\frac{N}{\binom{\alpha(F)+1}{2}}
\]
over small \(G\)-free graphs.

```python
def independence_number(A):
    n = len(A)
    best = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        if size <= best:
            continue
        S = [v for v in range(n) if (mask >> v) & 1]
        if all(v not in A[u] for u, v in combinations(S, 2)):
            best = size
    return best

def clique_target_search(n, forbidden_test):
    best = (0.0, None, None)
    for mask in range(1 << comb(n, 2)):
        A = graph_from_mask(n, mask)
        if forbidden_test(A):
            continue
        a = independence_number(A)
        ratio = n / comb(a + 1, 2)
        if ratio > best[0]:
            best = (ratio, mask, a)
    return best

# Examples feasible for small n:
# clique_target_search(7, lambda A: has_kss(A, 3))
# clique_target_search(7, has_h5)
```

For larger \(N\), the decisive computational experiment is SAT search for a \(G\)-free graph with \(\alpha(F)<t\) at \(N\) near \(ct^2\). This directly tests the unresolved clique bottleneck rather than only restricted embedding lemmas.

## Route Diagnosis

**Proved ledger.**

- A sharp-enough bounded high-incidence lemma for \(K_{s,s}\)-free red graphs.
- A deterministic nonuniform reservoir embedding theorem with total cost
  \[
  2n+8s\sum_i q_i+
  2(s-1)4^s\sum_i b_iq_i^s.
  \]
- Ramsey size linearity of \(K_{3,3}\) and \(Q_3\) against every fixed-degeneracy target, including disconnected graphs and stars.
- Exact \(H_5\)-free common-neighbour restrictions: the common red neighbourhood of a red edge induces a matching, and an external vertex has at most one red neighbour in a red \(K_4\).
- Explicit forest examples showing that failure of a fixed blue extension gives only a union of red neighbourhoods, not a useful common-neighbour certificate.
- Complete bipartite examples showing that the \(K_{s,s}\)-style bounded-bad-set lemma is false for \(H_5\).

**Plausible but unproved.**

- For \(K_{3,3}\) and \(Q_3\), a genuinely simultaneous multi-reservoir argument might exploit correlations between bad sets more efficiently than a union bound.
- For \(H_5\), Lemmas 6 and 8 may combine with near-bipartite stability to give a global dichotomy, but no compatible embedding theorem was obtained.

**Dead ends.**

- “Every partial blue embedding extends after \(O(d)\) extra vertices” is false: a red star blocks extension even for one previously embedded neighbour.
- “A red-neighbourhood cover forces a large red intersection” is false: disjoint unions of stars give covers with disjoint obstruction sets.
- “Only boundedly many vertices can be red-dense into a reservoir” is false for \(H_5\): complete bipartite red graphs provide arbitrarily many such vertices.

**Precise block.**

For \(H=K_t\), every ordering has backward degrees \(0,1,\dots,t-1\). Theorem 2 consequently pays polynomially more than \(t^2\), while a complete solution would require only
\[
N=O(e(K_t))=O(t^2).
\]
For \(G=K_{3,3}\), eliminating this loss would in particular prove
\[
R(K_{3,3},K_t)=O(t^2),
\]
the difficult benchmark identified in the brief. Thus the missing step is not routine bookkeeping but an unresolved off-diagonal Ramsey estimate of comparable strength to the original problem.

A fresh attempt should first isolate and attack the clique case. For \(K_{3,3}\) and \(Q_3\), it needs a simultaneous common-neighbour or critical-core principle rather than one-reservoir-at-a-time union bounds. For \(H_5\), Route 1’s basic incidence premise fails, so the stability-based Route 4 appears more promising.