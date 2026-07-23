STATUS: BLOCKED

## Result

I did not solve Erdős Problem #567. Pursuing Route 3 yields a rigorous core–reservoir reduction and linear Ramsey bounds for substantial low-degeneracy target classes. Specifically, \(R(K_{3,3},H)\le16e(H)\) when the degeneracy of \(H\) is \(O(e(H)^{1/3})\), and \(R(Q_3,H)\le16e(H)\) when it is \(O(e(H)^{1/4})\), with explicit constants below. More generally, after peeling low-degree target vertices, it suffices to embed a core of order \(O(m^{2/3})\) for \(K_{3,3}\), or \(O(m^{3/4})\) for \(Q_3\), into a suitable blue reservoir. The route then becomes blocked: even a hypothetical quadratic clique Ramsey bound only automatically embeds cores of order \(O(\sqrt m)\), while the reservoir extension permits peeling only up to degree \(O(m^{1/3})\) or \(O(m^{1/4})\). For \(H_5\), extremal sparsity is unavailable, and the missing weighted multipartite compatibility statement is essentially the unresolved heart of the problem.

## Complete Argument

### 1. A general core-extension lemma

Let \(F\) be the red graph, so blue edges are the edges of \(\overline F\).

For an integer \(d\ge0\), define the \((d+1)\)-core \(C=C_d(H)\) by repeatedly deleting a vertex whose current degree is at most \(d\), until no such vertex remains.

#### Lemma 1: Reservoir extension from a blue core

Let \(H\) have \(h\) vertices. Suppose \(U\subseteq V(F)\) satisfies
\[
\max_{u\in U}|N_F(u)\cap U|\le q.
\]
Let \(C=C_d(H)\). If

1. \(H[C]\) has a blue embedding into \(U\), and
2. \[
   |U|\ge h+dq,
   \]

then that embedding extends to a blue embedding of all of \(H\) into \(U\).

Moreover, if \(H\) has \(m\) edges, then
\[
|C|\le \frac{2m}{d+1}.
\]

#### Proof

Let \(x_1,\dots,x_r\) be the order in which the vertices outside \(C\) were deleted. At the moment \(x_i\) was deleted, it had at most \(d\) neighbours among
\[
C\cup\{x_{i+1},\dots,x_r\}.
\]

Start with the given blue embedding of \(H[C]\), then embed
\[
x_r,x_{r-1},\dots,x_1
\]
in that order.

When \(x_i\) is to be embedded, at most \(d\) of its neighbours have already been embedded. If their images are \(u_1,\dots,u_t\), with \(t\le d\), a candidate \(w\in U\) is forbidden either because it is already used, or because \(wu_j\) is red for some \(j\). Thus the number of forbidden vertices is at most
\[
(h-1)+\sum_{j=1}^t |N_F(u_j)\cap U|
   \le (h-1)+dq.
\]
Since \(|U|\ge h+dq\), at least one candidate remains. Choosing such a candidate preserves every edge of \(H\) whose other endpoint is already embedded. Induction completes the embedding.

If \(C\neq\varnothing\), then \(H[C]\) has minimum degree at least \(d+1\). Hence
\[
(d+1)|C|\le 2e(H[C])\le 2m.
\]
The assertion is trivial if \(C=\varnothing\). ∎

This is a genuine Route 3 reduction: the target is separated into a relatively dense core and a peelable remainder, and any suitable core embedding with a controlled reservoir automatically extends.

---

### 2. A low-red-degree reservoir in \(K_{s,s}\)-free graphs

The following elementary moment estimate gives the reservoirs needed for Lemma 1.

#### Lemma 2: Degree moment bound

Let \(F\) be a \(K_{s,s}\)-free graph on \(N\) vertices, where \(s\ge2\). Define
\[
B_s=\left(\frac{s^s(s-1)}{s!}+(s-1)^s\right)^{1/s}.
\]
Then
\[
\sum_{v\in V(F)}d_F(v)\le B_sN^{2-1/s}.
\]
Consequently, there is a set \(U\subseteq V(F)\) satisfying
\[
|U|\ge \frac N2
\]
and
\[
d_F(u)\le 2B_sN^{1-1/s}
\qquad\text{for every }u\in U.
\]

#### Proof

For every \(s\)-set \(S\subseteq V(F)\), its common neighbourhood has size at most \(s-1\); otherwise \(S\) and any \(s\) common neighbours form a \(K_{s,s}\). Double-counting pairs \((v,S)\) with \(S\subseteq N_F(v)\) gives
\[
\sum_v\binom{d_F(v)}s
 =\sum_{\substack{S\subseteq V(F)\\|S|=s}}
   \left|\bigcap_{x\in S}N_F(x)\right|
 \le (s-1)\binom Ns.
\]

For an integer \(a\ge s\),
\[
\frac{\binom as}{a^s}
 =\frac1{s!}\prod_{j=0}^{s-1}\left(1-\frac ja\right)
 \ge \frac{\binom ss}{s^s}
 =\frac1{s^s}.
\]
Thus
\[
a^s\le s^s\binom as.
\]
For \(a<s\), we simply have \(a^s\le(s-1)^s\). Therefore
\[
\begin{aligned}
\sum_v d_F(v)^s
&\le s^s\sum_v\binom{d_F(v)}s+(s-1)^sN\\
&\le s^s(s-1)\binom Ns+(s-1)^sN\\
&\le
\left(\frac{s^s(s-1)}{s!}+(s-1)^s\right)N^s\\
&=B_s^sN^s.
\end{aligned}
\]
By Hölder's inequality,
\[
\sum_vd_F(v)
 \le N^{1-1/s}
      \left(\sum_vd_F(v)^s\right)^{1/s}
 \le B_sN^{2-1/s}.
\]

The average red degree is therefore at most \(B_sN^{1-1/s}\). At least \(N/2\) vertices have degree at most twice this average. Taking those vertices as \(U\) proves the final assertion. ∎

The two constants needed here are
\[
B_3=17^{1/3}<3,
\qquad
B_4=113^{1/4}<4.
\]

---

### 3. Linear bounds for low-degeneracy targets

#### Theorem 3

Let \(H\) have no isolated vertices and \(m\ge1\) edges.

1. If
   \[
   \operatorname{degen}(H)
   \le \frac{(16m)^{1/3}}{16B_3},
   \]
   then
   \[
   R(K_{3,3},H)\le16m.
   \]

2. If
   \[
   \operatorname{degen}(H)
   \le \frac{(16m)^{1/4}}{16B_4},
   \]
   then
   \[
   R(Q_3,H)\le16m.
   \]

#### Proof

Set
\[
N=16m.
\]
Because \(H\) has no isolated vertices,
\[
h:=v(H)\le2m=\frac N8.
\]

First consider \(G=K_{3,3}\). Let \(F\) be a red \(K_{3,3}\)-free graph on \(N\) vertices. Apply Lemma 2 with \(s=3\). We obtain \(U\subseteq V(F)\) with
\[
|U|\ge\frac N2
\]
and
\[
d_F(u)\le q:=2B_3N^{2/3}
\qquad(u\in U).
\]
Let \(d=\operatorname{degen}(H)\). By hypothesis,
\[
dq\le
\frac{N^{1/3}}{16B_3}\cdot2B_3N^{2/3}
=\frac N8.
\]
Since \(H\) is \(d\)-degenerate, its \((d+1)\)-core is empty. Lemma 1 therefore applies without any initial core embedding, because
\[
h+dq\le\frac N8+\frac N8=\frac N4\le |U|.
\]
Thus \(\overline F[U]\), and hence \(\overline F\), contains \(H\).

For \(G=Q_3\), observe that \(K_{4,4}\) contains \(Q_3\): under the parity bipartition of \(Q_3\), it is \(K_{4,4}\) with four edges of a perfect matching omitted. Since copies are not induced, every red \(K_{4,4}\) contains a red \(Q_3\). Consequently, a \(Q_3\)-free graph is \(K_{4,4}\)-free.

Apply Lemma 2 with \(s=4\). There is \(U\) of size at least \(N/2\) whose vertices have red degree at most
\[
q:=2B_4N^{3/4}.
\]
The assumed degeneracy bound gives
\[
dq\le
\frac{N^{1/4}}{16B_4}\cdot2B_4N^{3/4}
=\frac N8.
\]
The same application of Lemma 1 embeds \(H\) in blue. ∎

This does not solve the problem because cliques \(K_t\), for example, have degeneracy \(t-1=\Theta(\sqrt m)\), outside both ranges.

---

### 4. The resulting core reductions

Set \(N=16m\), and define
\[
d_s=\left\lfloor\frac{N^{1/s}}{16B_s}\right\rfloor.
\]

#### Corollary 4

For \(s=3\), let \(F\) be a \(K_{3,3}\)-free graph on \(N\) vertices; for \(s=4\), let \(F\) be a \(Q_3\)-free graph on \(N\) vertices. In each case there is a set \(U\subseteq V(F)\), \(|U|\ge N/2\), with the following property:

If the \((d_s+1)\)-core \(C\) of \(H\) has a blue embedding into \(U\), then all of \(H\) has a blue embedding into \(U\).

Furthermore,
\[
|C|<\frac{32B_s m}{N^{1/s}}.
\]
Thus the core has order

- \(O(m^{2/3})\) for \(K_{3,3}\);
- \(O(m^{3/4})\) for \(Q_3\).

#### Proof

The reservoir \(U\) comes from Lemma 2. Since
\[
d_s\le\frac{N^{1/s}}{16B_s},
\]
we have
\[
d_s\cdot 2B_sN^{1-1/s}\le\frac N8.
\]
Also \(v(H)\le N/8\), so Lemma 1 extends any blue embedding of the core.

Finally,
\[
d_s+1>\frac{N^{1/s}}{16B_s},
\]
and Lemma 1 gives
\[
|C|\le\frac{2m}{d_s+1}
 <\frac{32B_sm}{N^{1/s}}.
\]
∎

This identifies the precise quantitative obstruction to completing Route 3 by merely embedding the core in a blue clique.

Suppose, optimistically, that one already had the necessary quadratic off-diagonal estimate
\[
R(G,K_t)\le A_Gt^2.
\]
An ambient set of order \(\Theta(m)\) then automatically supplies a blue clique only of order \(O(\sqrt m)\). But the cores produced above may have orders \(m^{2/3}\) and \(m^{3/4}\).

Trying to force the core down to \(O(\sqrt m)\) requires peeling at threshold
\[
d=\Omega(\sqrt m),
\]
because \(|C|\le2m/(d+1)\). On the other hand, the reservoir extension permits only
\[
d=O(m^{1/3})
\quad\text{or}\quad
d=O(m^{1/4}),
\]
respectively. There is no overlap between these ranges. Thus even proving the quadratic clique benchmark would not complete this particular degree-based core decomposition.

---

### 5. What a genuinely weighted colour-class embedding would require

The following exact Hall formulation clarifies the missing weighted theorem.

#### Lemma 5: Independent-class extension

Let \(I\) be an independent set in \(H\). Suppose \(\phi\) is a blue embedding of \(H-I\) into a host, and let \(W\) be a reservoir disjoint from \(\phi(V(H-I))\). For \(x\in I\), put
\[
A_x
 =
 W\setminus
 \bigcup_{y\in N_H(x)}
 \bigl(N_F(\phi(y))\cap W\bigr).
\]
Then \(\phi\) extends over \(I\) if and only if the family
\[
\{A_x:x\in I\}
\]
has a system of distinct representatives.

In particular, if
\[
\sum_{y\in N_H(x)}
 |N_F(\phi(y))\cap W|
 \le |W|-|I|
 \qquad\text{for every }x\in I,
\]
then the extension exists.

More quantitatively, write
\[
\rho(y)=|N_F(\phi(y))\cap W|
\]
and
\[
T=\sum_{x\in I}\sum_{y\in N_H(x)}\rho(y)
  =\sum_{y\in V(H-I)}d_H(y,I)\rho(y).
\]
If \(|W|>|I|\), all but fewer than
\[
\frac{T}{|W|-|I|}
\]
vertices \(x\in I\) satisfy the sufficient inequality above.

#### Proof

A vertex \(w\in W\) may be used for \(x\) precisely when every required edge from \(x\) to \(H-I\) becomes blue, which is exactly the condition \(w\in A_x\). Since \(I\) is independent, there are no further edge constraints among its images. Thus an extension is precisely a system of distinct representatives. Hall's theorem gives the first assertion.

By the union bound,
\[
|W\setminus A_x|
\le
\sum_{y\in N_H(x)}
 |N_F(\phi(y))\cap W|.
\]
Under the stated inequality, \(|A_x|\ge|I|\). For every nonempty \(X\subseteq I\),
\[
\left|\bigcup_{x\in X}A_x\right|
\ge |A_x|
\ge |I|
\ge |X|
\]
for any fixed \(x\in X\). Hence Hall's condition holds.

Finally, if
\[
b_x:=\sum_{y\in N_H(x)}\rho(y)>|W|-|I|,
\]
then summing \(b_x\) over all exceptional \(x\) proves that their number is less than \(T/(|W|-|I|)\). ∎

The quantity
\[
T=\sum_y d_H(y,I)\rho(y)
\]
is exactly the weighted incidence cost that a successful Route 3 theorem must control. A proper colouring decomposes \(H\) into independent classes, but one must choose the earlier embedding so that target vertices with many future incidences are mapped to host vertices with appropriately small or highly overlapping red neighbourhoods.

The moment estimate in Lemma 2 controls only the unweighted average of \(\rho(y)\). It does not supply a blue embedding of the core that optimizes this weighted sum. Moreover, the union bound loses potentially decisive overlap information among red neighbourhoods.

---

### 6. Why an arbitrary partial embedding cannot be extended

There is a uniform obstruction for all three fixed red graphs.

Let \(F=K_{2,n-2}\), with red bipartition
\[
A=\{a,b\},\qquad B,
\]
and all edges between \(A\) and \(B\) red.

Then \(F\) is:

- \(K_{3,3}\)-free, since its matching number is at most \(2\);
- \(Q_3\)-free, since \(Q_3\) has a matching of size \(4\);
- \(H_5\)-free, since \(F\) is bipartite while \(H_5\) contains triangles.

Let the target be the path \(P_3\), with centre \(x\) and leaves \(y,z\). The partial blue embedding of \(P_3-x\), which consists of two isolated vertices, may map \(y,z\) to \(a,b\). It has no extension: every unused vertex in \(B\) is red-adjacent to both \(a\) and \(b\), while no unused vertex remains in \(A\).

Nevertheless, the blue graph contains a large clique on \(B\), and hence globally contains \(P_3\). Thus any extension lemma that is required to work from every partial embedding is false, even for a target vertex of degree two. The core and its reservoirs must be selected globally.

---

### 7. Why chromatic criticality alone does not close the gap

Every \(k\)-chromatic graph contains a vertex-critical \(k\)-chromatic subgraph \(J\). Such a graph satisfies
\[
\delta(J)\ge k-1,
\]
because otherwise a \((k-1)\)-colouring of \(J-v\) could be extended to \(v\). Therefore
\[
|V(J)|\le\frac{2m}{k-1}.
\]

This is useful only when \(k\) is large. If \(k=\Theta(\sqrt m)\), then \(J\) has \(O(\sqrt m)\) vertices and could conceivably be embedded using a quadratic off-diagonal theorem. For fixed or moderately growing \(k\), however, the bound is much larger.

Moreover, removing one critical subgraph need not decrease the chromatic number of the remainder. For example, take two vertex-disjoint copies of \(K_k\) and join them by one bridge. The resulting connected graph is \(k\)-chromatic; either \(K_k\) is a critical core, but deleting it leaves another \(K_k\). Hence a single critical core does not produce a lower-chromatic remainder.

A complete blue multipartite host based only on colour-class sizes also overpays badly. A matching of \(m\) edges has a proper two-colouring with classes of size \(m\), but requiring all \(m^2\) cross-pairs between the classes to be blue ignores that the target has only \(m\) required edges. Therefore the missing theorem really must be weighted by the actual edge incidences, as in Lemma 5.

---

### 8. Disconnected targets are not the principal obstruction

For completeness, there is a simple composition inequality.

#### Lemma 6

If \(H=H_1\sqcup\cdots\sqcup H_r\) is a disjoint union, then
\[
R(G,H)\le\sum_{i=1}^rR(G,H_i).
\]

#### Proof

Set \(n_i=R(G,H_i)\), and consider a red \(G\)-free graph on \(\sum_i n_i\) vertices. Inside any chosen \(n_1\) vertices there is a blue \(H_1\). Delete the vertices of this copy. Since \(n_1\ge v(H_1)\), at least \(\sum_{i=2}^r n_i\) vertices remain. Repeat. The resulting blue copies are vertex-disjoint, and no cross-edges are required between distinct components. ∎

Thus a uniform linear theorem for connected targets would imply the full theorem. The main Route 3 obstruction is compatibility inside connected targets, not disconnectedness.

## Self-Audit

1. **The decisive core-embedding theorem is missing.**  
   Corollary 4 is conditional on embedding a core of size \(O(m^{2/3})\) or \(O(m^{3/4})\) in a particular reservoir. I have no theorem accomplishing this, and do not claim that the desired weighted statement follows from known off-diagonal Ramsey estimates. This is the principal reason for the BLOCKED status.

2. **The reservoir argument uses a crude union bound.**  
   Lemmas 1 and 5 may discard substantial overlap among red neighbourhoods. The conclusions nevertheless hold because they are only sufficient conditions: the number of excluded vertices is certainly at most the sum of the relevant red degrees. The weakness affects the range of applicability, not the correctness of the stated lemmas.

3. **The \(Q_3\) estimate passes through the larger forbidden graph \(K_{4,4}\).**  
   This loses information specific to \(Q_3\) and likely gives a far from optimal exponent. The implication used is nonetheless valid in the required direction: every \(K_{4,4}\) contains \(Q_3\) as a non-induced subgraph, so every \(Q_3\)-free graph is \(K_{4,4}\)-free.

## Computations To Verify

The following Python implements the graph-specific certificate checks and the degree-moment assertions used above.

```python
from itertools import combinations, permutations
from math import comb
import random

def graph_from_mask(n, mask):
    edges = list(combinations(range(n), 2))
    adj = [set() for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            adj[u].add(v)
            adj[v].add(u)
    return adj

def contains_kss(adj, s):
    n = len(adj)
    V = set(range(n))
    for A in combinations(range(n), s):
        common = V.copy()
        for a in A:
            common &= adj[a]
        if len(common) >= s:
            return True
    return False

def contains_h5(adj):
    # Certificate: edge cd, common neighbours a,b,
    # and a fifth common neighbour x of a,b.
    n = len(adj)
    for c in range(n):
        for d in adj[c]:
            if c >= d:
                continue
            common_cd = adj[c] & adj[d]
            for a, b in combinations(common_cd, 2):
                for x in (adj[a] & adj[b]):
                    if x not in {a, b, c, d}:
                        return True
    return False

def contains_q3(adj):
    # Q3 = K_{4,4} minus a perfect matching.
    # Matching edges may also be present, since copies are non-induced.
    n = len(adj)
    V = set(range(n))
    for A in combinations(range(n), 4):
        rem = V - set(A)
        for B in combinations(rem, 4):
            Bset = set(B)
            for omitted_partner in permutations(B):
                ok = True
                for i, a in enumerate(A):
                    for b in B:
                        if b != omitted_partner[i] and b not in adj[a]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return True
    return False

def moment_lhs(adj, s):
    return sum(comb(len(adj[v]), s) for v in range(len(adj)))

def verify_moment_bound(adj, s):
    n = len(adj)
    if not contains_kss(adj, s):
        assert moment_lhs(adj, s) <= (s - 1) * comb(n, s)

def exhaustive_k33_moment_check(n=6):
    M = comb(n, 2)
    for mask in range(1 << M):
        adj = graph_from_mask(n, mask)
        verify_moment_bound(adj, 3)
    print("All K_3,3 moment checks passed on", n, "vertices")

def verify_q3_implies_k44_free(adj):
    if not contains_q3(adj):
        assert not contains_kss(adj, 4)

def explicit_unextendable_example(n=10):
    # Red K_{2,n-2}
    adj = [set() for _ in range(n)]
    A = {0, 1}
    B = set(range(2, n))
    for a in A:
        for b in B:
            adj[a].add(b)
            adj[b].add(a)

    assert not contains_kss(adj, 3)
    assert not contains_q3(adj)
    assert not contains_h5(adj)

    # Leaves of P3 are mapped to 0 and 1.
    unused = set(range(n)) - {0, 1}
    candidates = [
        w for w in unused
        if w not in adj[0] and w not in adj[1]
    ]
    assert candidates == []
    print("Unextendable partial P3 embedding verified")
```

The peeling and extension lemma can be tested as follows.

```python
def peel_core(Hadj, d):
    n = len(Hadj)
    alive = set(range(n))
    deletion_order = []

    while True:
        found = None
        for v in alive:
            current_degree = len(Hadj[v] & alive)
            if current_degree <= d:
                found = v
                break
        if found is None:
            break
        alive.remove(found)
        deletion_order.append(found)

    return alive, deletion_order

def extend_from_core(red_adj, Hadj, U, d, core_mapping):
    """
    core_mapping maps every vertex in the (d+1)-core to U.
    Raises AssertionError if the hypotheses of Lemma 1 hold but
    the prescribed greedy extension fails.
    """
    core, deletion_order = peel_core(Hadj, d)
    assert set(core_mapping) == set(core)

    used = set(core_mapping.values())
    mapping = dict(core_mapping)

    q = max(
        (len(red_adj[u] & set(U)) for u in U),
        default=0
    )
    h = len(Hadj)
    assert len(U) >= h + d * q

    for x in reversed(deletion_order):
        already_embedded_neighbors = [
            y for y in Hadj[x] if y in mapping
        ]
        assert len(already_embedded_neighbors) <= d

        candidates = []
        for w in U:
            if w in used:
                continue
            if all(
                mapping[y] not in red_adj[w]
                for y in already_embedded_neighbors
            ):
                candidates.append(w)

        assert candidates, "Would contradict Lemma 1"
        w = candidates[0]
        mapping[x] = w
        used.add(w)

    # Final verification of all required blue edges.
    for x in range(h):
        for y in Hadj[x]:
            if x < y:
                assert mapping[y] not in red_adj[mapping[x]]

    return mapping
```

A direct search relevant to the possible disproof route is:

```python
def independence_number(adj):
    n = len(adj)
    for r in range(n, -1, -1):
        for S in combinations(range(n), r):
            if all(v not in adj[u] for u, v in combinations(S, 2)):
                return r

def random_maximal_G_free(n, contains_G, trials=100):
    edges = list(combinations(range(n), 2))
    best = None

    for _ in range(trials):
        random.shuffle(edges)
        adj = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            if contains_G(adj):
                adj[u].remove(v)
                adj[v].remove(u)

        alpha = independence_number(adj)
        ratio = n / comb(alpha + 1, 2)
        if best is None or ratio > best[0]:
            best = (ratio, alpha, adj)

    return best

# Examples:
# best_k33 = random_maximal_G_free(12, lambda A: contains_kss(A, 3))
# best_h5  = random_maximal_G_free(12, contains_h5)
# Q3 checking becomes expensive sooner.
```

For a clique-based disproof, the quantity
\[
N/\binom{\alpha(F)+1}{2}
\]
would have to grow without bound along a provably \(G\)-free family.

## Route Diagnosis

The part of Route 3 that works is the peeling principle: once a dense core is embedded in a blue reservoir whose red degrees are controlled, the remainder can be embedded at a cost proportional to its backward degree. For \(K_{3,3}\) and \(Q_3\), forbidden complete bipartite subgraphs provide such reservoirs and yield genuine linear bounds for targets of degeneracy \(O(m^{1/3})\) and \(O(m^{1/4})\).

The route is blocked at the core. Degree peeling leaves cores much larger than \(\sqrt m\), while chromatic criticality only guarantees a \(\sqrt m\)-sized core when the target chromatic number is already \(\Theta(\sqrt m)\). A weighted multipartite theorem capable of embedding the remaining cores would have to coordinate target incidence weights with red-neighbourhood geometry. Its clique specialization includes the unresolved estimate \(R(K_{3,3},K_t)=O(t^2)\), and even that estimate alone would not bridge the \(m^{2/3}\)-versus-\(\sqrt m\) exponent gap.

For \(H_5\), the sparse-reservoir method does not apply: \(H_5\)-free red graphs may have \(\Theta(N^2)\) edges. The balanced complete bipartite extremal example is benign because its blue complement consists of two large cliques, but exploiting this requires a stability-based, concentration-resistant compatibility theorem. The known result for bipartite targets cannot simply be applied pairwise between colour classes because shared vertices must receive consistent images.

A fresh attempt should therefore do one of the following:

1. Develop an overlap-sensitive reservoir theorem using the triple-codegree restriction for \(K_{3,3}\) or the almost-\(4\times4\) restriction for \(Q_3\), rather than bounding unions by sums of red degrees.
2. Use a randomized nibble plus absorption to choose the core embedding and the reservoirs simultaneously, optimizing the weighted quantity in Lemma 5.
3. For \(H_5\), pursue Route 4: prove a stability dichotomy robust against exceptional red edges concentrated around high-degree target vertices.
4. In parallel, test Route 5 using algebraic or \(G\)-free-process constructions and rigorous independence-number bounds; a family with \(\alpha(F)=o(\sqrt N)\) would disprove the corresponding case immediately.