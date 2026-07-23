STATUS: BLOCKED

## Result

The general lower bound remains unresolved. Pursuing Ramsey-minimal-host induction produced a rigorous peeling mechanism: deleted vertices can be assigned to one color as “exceptional vertices,” after which only a bounded-degree coloring problem remains. This proves several exact and general partial results. In particular,
\[
\widehat R(F_1,F_2)\ge
\max\!\left\{
|E(F_1)|+|E(F_2)|-1,\,
|E(F_2)|+(s-1)m_1,\,
|E(F_1)|+(t-1)n_1
\right\},
\]
the conjectured formula holds whenever one target is a matching, and—using the supplied settled one-sided case—it holds for \(s=t=2\) whenever \(n_1\) and \(m_1\) are odd, even if \(n_2,m_2\) are even and the lists are nonconstant. More generally, the formula follows when the antidiagonal maxima admit a compatible monotone maximizing path and the relevant interior demands are odd. The general route is blocked because antidiagonal maximizers need not form such a path, while the natural bounded-degree replacement fails on odd-cycle-type cores.

## Complete Argument

Write
\[
A=\sum_{i=1}^s n_i,\qquad B=\sum_{j=1}^t m_j.
\]

### 1. Universal upper bound

For completeness, let
\[
H^\star=\bigsqcup_{k=2}^{s+t}K_{1,l_k}.
\]
It has \(L=\sum l_k\) edges.

Starting at \((i,j)=(1,1)\), inspect the star \(K_{1,l_{i+j}}\). If it has at least \(n_i\) red edges, take a red \(K_{1,n_i}\) and increment \(i\). Otherwise it has at most \(n_i-1\) red edges and hence at least
\[
l_{i+j}-(n_i-1)\ge m_j
\]
blue edges, so take a blue \(K_{1,m_j}\) and increment \(j\). Different selected stars lie in different components of \(H^\star\). Eventually \(i=s+1\) or \(j=t+1\), proving
\[
\widehat R(F_1,F_2)\le L.
\]

The rest concerns lower bounds.

---

### 2. A Ramsey-minimal pivotal-edge lemma

#### Lemma 2.1
Let \(G_1,G_2\) be nonempty graphs. Then
\[
\widehat R(G_1,G_2)\ge |E(G_1)|+|E(G_2)|-1.
\]

#### Proof
Let \(H\to(G_1,G_2)\), and choose an edge-minimal arrowing subgraph \(H_0\subseteq H\). Fix \(e\in E(H_0)\). By minimality, \(H_0-e\) has a coloring \(c\) containing neither a red \(G_1\) nor a blue \(G_2\).

Coloring \(e\) red must create a red copy \(A\) of \(G_1\), because the blue graph is unchanged and contains no \(G_2\). The copy \(A\) must use \(e\). Similarly, coloring \(e\) blue creates a blue copy \(B\) of \(G_2\) using \(e\).

Every edge of \(A-e\) is red under \(c\), while every edge of \(B-e\) is blue. Therefore
\[
E(A)\cap E(B)=\{e\}.
\]
Consequently
\[
|E(H)|\ge |E(H_0)|
 \ge |E(A)\cup E(B)|
 =|E(G_1)|+|E(G_2)|-1.
\]
∎

Applied to the present targets,
\[
\widehat R(F_1,F_2)\ge A+B-1.
\]

This lemma is useful but generally falls short of \(L\).

---

### 3. A vertex-transversal lower bound

For a graph \(F\), define
\[
\tau_F(H)=\min\{|X|: H-X\text{ contains no copy of }F\}.
\]

#### Lemma 3.1
For every graph \(H\),
\[
\tau_{F_2}(H)\ge r
\quad\Longrightarrow\quad
|E(H)|\ge (r-1)m_1+B.
\]

#### Proof
Suppose \(\tau_{F_2}(H)\ge r\). We construct vertices
\[
v_1,\ldots,v_{r-1}
\]
successively. After deleting \(v_1,\ldots,v_q\), where \(q<r\), the remaining graph still contains \(F_2\). In particular it contains its largest component \(K_{1,m_1}\). Choose its center as \(v_{q+1}\). Thus
\[
d_{H-\{v_1,\ldots,v_q\}}(v_{q+1})\ge m_1.
\]

The edge sets removed at these successive deletions are disjoint, so the first \(r-1\) deletions account for at least \((r-1)m_1\) edges. The final graph
\[
H-\{v_1,\ldots,v_{r-1}\}
\]
still contains \(F_2\), hence has at least \(B\) edges. Therefore
\[
|E(H)|\ge (r-1)m_1+B.
\]
∎

#### Proposition 3.2
For arbitrary star forests \(F_1,F_2\),
\[
\widehat R(F_1,F_2)\ge (s-1)m_1+B.
\]

#### Proof
Let
\[
|E(H)|<(s-1)m_1+B.
\]
By Lemma 3.1, \(\tau_{F_2}(H)\le s-1\). Choose \(X\subseteq V(H)\), \(|X|\le s-1\), such that \(H-X\) is \(F_2\)-free.

Color every edge having an endpoint in \(X\) red, and every remaining edge blue. The blue graph is exactly \(H-X\), so it contains no \(F_2\).

Every red edge meets \(X\). Hence every nonempty vertex-disjoint red star component uses at least one distinct vertex of \(X\). Thus the red graph contains at most \(|X|\le s-1\) pairwise vertex-disjoint nonempty stars, and in particular no copy of \(F_1\), which has \(s\) components. ∎

Swapping the colors gives
\[
\widehat R(F_1,F_2)\ge (t-1)n_1+A.
\]

Combining this with Lemma 2.1,
\[
\boxed{
\widehat R(F_1,F_2)\ge
\max\{A+B-1,\ B+(s-1)m_1,\ A+(t-1)n_1\}.
}
\]

---

### 4. Exact formula when one target is a matching

#### Theorem 4.1
If
\[
F_1=sK_{1,1},
\]
then
\[
\widehat R(F_1,F_2)
=(s-1)m_1+\sum_{j=1}^t m_j.
\]

#### Proof
Here \(n_i=1\) for every \(i\). On antidiagonal \(k\),
\[
l_k=\max\{m_j:i+j=k\}.
\]
The smallest admissible \(j\) gives the maximum. Thus
\[
l_k=
\begin{cases}
m_1,&2\le k\le s+1,\\
m_{k-s},&s+2\le k\le s+t.
\end{cases}
\]
Therefore
\[
L=s m_1+\sum_{j=2}^t m_j
=(s-1)m_1+B.
\]

Proposition 3.2 gives the lower bound \(L\), and the universal construction gives the upper bound \(L\). ∎

By symmetry, the formula also holds whenever \(F_2\) is a matching.

---

### 5. The exceptional-vertex extension lemma

For \(1\le i\le s\), write
\[
F_1^{(i)}=\bigsqcup_{r=i}^s K_{1,n_r},
\]
and define \(F_2^{(j)}\) analogously.

#### Lemma 5.1
Let \(X,Y\subseteq V(H)\) be disjoint, with
\[
|X|=i-1,\qquad |Y|=j-1,
\]
and put \(Z=V(H)\setminus(X\cup Y)\).

Suppose \(H[Z]\) has a coloring containing neither a red \(F_1^{(i)}\) nor a blue \(F_2^{(j)}\). Extend it by coloring:

- all edges between \(X\) and \(Z\), and all edges inside \(X\), red;
- all edges between \(Y\) and \(Z\), and all edges inside \(Y\), blue;
- all edges between \(X\) and \(Y\), arbitrarily, say red.

Then the resulting coloring contains neither a red \(F_1\) nor a blue \(F_2\).

The same conclusion holds under the weaker local hypotheses
\[
\Delta(R[Z])\le n_i-1,\qquad
\Delta(B[Z])\le m_j-1.
\]

#### Proof
Suppose there is a red copy of \(F_1\). At most \(|X|=i-1\) of its vertex-disjoint components can meet \(X\), so at least
\[
s-i+1
\]
components avoid \(X\).

No red edge joins \(Y\) to \(Z\), and all red edges between \(X\) and \(Y\) meet \(X\). Hence every red component avoiding \(X\) lies entirely in \(Z\).

Among any \(s-i+1\) of the demands \(n_1,\ldots,n_s\), the decreasing rearrangement termwise dominates
\[
n_i,n_{i+1},\ldots,n_s.
\]
Thus, by discarding excess leaves if necessary, these components contain a copy of \(F_1^{(i)}\) in \(R[Z]\), a contradiction.

Under the degree hypothesis, it is enough to note that among the \(s-i+1\) components in \(Z\), at least one has demand at least \(n_i\), contradicting \(\Delta(R[Z])\le n_i-1\).

The blue argument is symmetric, with \(Y\) in place of \(X\). ∎

This is the central successful induction device: coloring all edges incident with a deleted red-exceptional vertex red is safe provided the residual red target is shortened by one component.

---

### 6. A bounded-degree edge decomposition

#### Lemma 6.1
If \(a,b\) are nonnegative even integers and
\[
\Delta(G)\le a+b,
\]
then \(E(G)\) can be partitioned into red and blue edges so that
\[
\Delta(R)\le a,\qquad \Delta(B)\le b.
\]

#### Proof
Write \(a+b=2h\). We first show that every graph of maximum degree at most \(2h\) can have its edges partitioned into \(h\) subgraphs of maximum degree at most \(2\).

In each connected component, pair its odd-degree vertices and add one auxiliary edge for each pair. The resulting multigraph is Eulerian. Orient every Euler circuit cyclically and then delete the auxiliary edges. Every original vertex has indegree and outdegree at most \(h\).

Construct a bipartite multigraph with a left and right copy of every vertex. Replace an oriented edge \(u\to v\) by an edge from \(u_L\) to \(v_R\). This bipartite graph has maximum degree at most \(h\). By König’s line-coloring theorem, its edges can be partitioned into \(h\) matchings.

Transferring these colors back to \(G\), every color class has at most one incoming and one outgoing edge at each vertex, and therefore maximum undirected degree at most \(2\).

Take \(a/2\) of these classes to be red and the remaining \(b/2\) classes blue. Then
\[
\Delta(R)\le 2(a/2)=a,\qquad
\Delta(B)\le 2(b/2)=b.
\]
∎

In particular, if \(n_i,m_j\) are odd and
\[
\Delta(G)\le n_i+m_j-2,
\]
then \(G\) can be colored with
\[
\Delta(R)\le n_i-1,\qquad
\Delta(B)\le m_j-1.
\]

---

### 7. A maximizing-path structural theorem

A monotone antidiagonal path is a sequence
\[
(i_k,j_k),\qquad 2\le k\le s+t,
\]
such that

- \(i_k+j_k=k\);
- \((i_2,j_2)=(1,1)\) and \((i_{s+t},j_{s+t})=(s,t)\);
- at every step exactly one coordinate increases by one.

Call it maximizing if
\[
n_{i_k}+m_{j_k}-1=l_k
\]
for every \(k\).

Let \(k_0\) be the first \(k\) for which \(i_k=s\) or \(j_k=t\).

#### Theorem 7.1
Assume:

1. there exists a maximizing monotone path;
2. for every \(2\le k<k_0\), both \(n_{i_k}\) and \(m_{j_k}\) are odd.

Then, using the settled one-sided case from the problem brief,
\[
\widehat R(F_1,F_2)=L.
\]

#### Proof
Let \(H\) have at most \(L-1\) edges. We construct disjoint exceptional sets \(X,Y\), initially empty, while following the fixed path.

At state \((i_k,j_k)\), before reaching \(k_0\), let
\[
G=H-(X\cup Y).
\]
By construction,
\[
|X|=i_k-1,\qquad |Y|=j_k-1.
\]

If
\[
\Delta(G)\le l_k-1
=n_{i_k}+m_{j_k}-2,
\]
then Lemma 6.1 colors \(G\) with
\[
\Delta(R[G])\le n_{i_k}-1,\qquad
\Delta(B[G])\le m_{j_k}-1.
\]
Lemma 5.1 then extends this to an avoiding coloring of \(H\).

Otherwise choose \(v\in V(G)\) with \(d_G(v)\ge l_k\). If the next path step increments \(i\), put \(v\) into \(X\); if it increments \(j\), put \(v\) into \(Y\). Delete \(v\) and continue.

Suppose no low-degree state occurs before \(k_0\). The deleted vertices have removed disjoint sets of at least
\[
\sum_{k=2}^{k_0-1}l_k
\]
edges. Therefore the residual graph \(G_0=H-(X\cup Y)\) at state
\[
(i_{k_0},j_{k_0})
\]
has at most
\[
\sum_{k=k_0}^{s+t}l_k-1
\]
edges.

Consider the suffix targets \(F_1^{(i_{k_0})}\) and \(F_2^{(j_{k_0})}\). On every later antidiagonal, the tail of the maximizing path belongs to the suffix rectangle and still attains the global maximum \(l_k\). Hence the conjectured value for this suffix pair is exactly
\[
\sum_{k=k_0}^{s+t}l_k.
\]

At least one suffix consists of only one star component because \(i_{k_0}=s\) or \(j_{k_0}=t\). The one-sided case supplied in the brief therefore gives an avoiding coloring of \(G_0\). Lemma 5.1 extends it over \(X\cup Y\), producing an avoiding coloring of \(H\).

Thus every \(H\) with fewer than \(L\) edges is colorable, proving the lower bound. Together with the universal upper bound, equality follows. ∎

---

### 8. A concrete additional exact class

#### Corollary 8.1
Let
\[
s=t=2,\qquad n_1\ge n_2,\qquad m_1\ge m_2.
\]
If \(n_1\) and \(m_1\) are odd, then
\[
\widehat R\!\left(
K_{1,n_1}\sqcup K_{1,n_2},
K_{1,m_1}\sqcup K_{1,m_2}
\right)=L.
\]

#### Proof
There is only one nontrivial intermediate antidiagonal:
\[
l_3=\max\{n_1+m_2-1,\ n_2+m_1-1\}.
\]
Choose a maximizing pair on that antidiagonal. It gives a monotone path
\[
(1,1)\longrightarrow (1,2)\text{ or }(2,1)\longrightarrow(2,2).
\]
The path reaches the boundary immediately after \((1,1)\), so the only parity requirements in Theorem 7.1 are that \(n_1,m_1\) be odd. ∎

For example, this covers
\[
(n_1,n_2)=(5,2),\qquad (m_1,m_2)=(3,2),
\]
which is neither a constant-list case nor an all-odd case.

It also covers the search seed
\[
(3,2)\quad\text{versus}\quad(3,2),
\]
proving its value is \(12\): if a host below \(12\) has maximum degree at least \(5\), peel that vertex toward an appropriate one-sided suffix; otherwise \(\Delta\le4\), and Lemma 6.1 splits the edges into two graphs of maximum degree at most \(2\), so neither color even contains a \(K_{1,3}\).

---

### 9. Why the induction does not presently extend

The pointwise antidiagonal maximizers need not form a monotone path. For example, take
\[
n=(101,91,91),\qquad m=(101,99,1).
\]
The antidiagonal maxima are
\[
201,\ 199,\ 191,\ 189,\ 91,
\]
so \(L=871\). The unique maximizer on the third antidiagonal is \((1,2)\), while the unique maximizer on the fourth is \((3,1)\). These cannot be consecutive states of a monotone path. The maximum total weight of a monotone path is only \(869\).

Thus fixed-path vertex peeling can account for at most \(869\) edges, while the desired exact lower bound is \(871\). Because the problem is exact, this two-edge defect cannot be discarded.

There is also a genuine low-degree obstruction to replacing the packing problem by degree bounds. For \(F_1=F_2=2K_{1,2}\), the graph \(C_7\) has maximum degree \(2\), but its edges cannot be split into two matchings; nevertheless it has an avoiding coloring because an alternating coloring has only one monochromatic adjacent edge pair. A general proof must exploit the number and disjointness of monochromatic stars, not merely forbid the largest star in each color.

## Self-Audit

1. **The maximizing-path theorem imports the one-sided case.**  
   I have not reproved the known theorem for \(s=1\) or \(t=1\). It is explicitly listed as settled in the supplied brief, and it is used only at the first boundary state. All new reduction steps before that point are proved above.

2. **The exceptional-set argument relies on sorted-demand domination.**  
   The potentially delicate point is that components meeting \(X\) need not be the largest target components. Nevertheless, deleting at most \(i-1\) components from a sorted list leaves \(s-i+1\) demands whose decreasing rearrangement termwise dominates \(n_i,\ldots,n_s\). Since copies are not induced, larger stars may be trimmed to the required sizes.

3. **The bounded-degree decomposition is only valid here because both capacities are even.**  
   The assertion is false in general: \(C_3\) cannot be decomposed into two subgraphs of maximum degree \(1\). In Lemma 6.1 the evenness permits grouping degree-\(2\) color classes obtained from a balanced orientation and bipartite edge coloring, so the stated version avoids this parity obstruction.

## Computations To Verify

```python
from itertools import combinations

def antidiagonal_values(n, m):
    s, t = len(n), len(m)
    vals = []
    maximizers = []
    for k in range(2, s + t + 1):
        cand = []
        for i in range(s):
            for j in range(t):
                if (i + 1) + (j + 1) == k:
                    cand.append((n[i] + m[j] - 1, i, j))
        z = max(x[0] for x in cand)
        vals.append(z)
        maximizers.append({(i, j) for w, i, j in cand if w == z})
    return vals, maximizers

def best_monotone_path(n, m):
    s, t = len(n), len(m)
    dp = {(0, 0): (n[0] + m[0] - 1, [(0, 0)])}
    for k in range(3, s + t + 1):
        ndp = {}
        for i in range(s):
            for j in range(t):
                if (i + 1) + (j + 1) != k:
                    continue
                preds = []
                if (i - 1, j) in dp:
                    preds.append(dp[(i - 1, j)])
                if (i, j - 1) in dp:
                    preds.append(dp[(i, j - 1)])
                if preds:
                    best = max(preds, key=lambda z: z[0])
                    ndp[(i, j)] = (
                        best[0] + n[i] + m[j] - 1,
                        best[1] + [(i, j)]
                    )
        dp = ndp
    return dp[(s - 1, t - 1)]

def has_pointwise_maximizing_path(n, m):
    vals, maxsets = antidiagonal_values(n, m)
    reachable = {(0, 0)}
    for maxset in maxsets[1:]:
        reachable = {
            (i, j) for i, j in maxset
            if (i - 1, j) in reachable or (i, j - 1) in reachable
        }
    return (len(n) - 1, len(m) - 1) in reachable

n = [101, 91, 91]
m = [101, 99, 1]
vals, _ = antidiagonal_values(n, m)
print(vals, sum(vals))
print(best_monotone_path(n, m))
print(has_pointwise_maximizing_path(n, m))
# Expected:
# [201, 199, 191, 189, 91], 871
# best path total 869
# False
```

A direct monochromatic-star-forest detector and exhaustive coloring check:

```python
def has_star_forest(num_vertices, edges, active_edge_ids, demands):
    adj = [set() for _ in range(num_vertices)]
    for eid in active_edge_ids:
        u, v = edges[eid]
        adj[u].add(v)
        adj[v].add(u)

    candidates = {}
    for q in set(demands):
        cq = []
        for center in range(num_vertices):
            for leaves in combinations(sorted(adj[center]), q):
                vertices = frozenset((center,) + leaves)
                cq.append(vertices)
        candidates[q] = cq

    demands = sorted(demands, reverse=True)

    def search(pos, used):
        if pos == len(demands):
            return True
        q = demands[pos]
        for star_vertices in candidates[q]:
            if used.isdisjoint(star_vertices):
                if search(pos + 1, used | star_vertices):
                    return True
        return False

    return search(0, frozenset())

def arrows(num_vertices, edges, red_demands, blue_demands):
    M = len(edges)
    all_ids = set(range(M))
    for mask in range(1 << M):
        red = {e for e in range(M) if (mask >> e) & 1}
        blue = all_ids - red
        if not has_star_forest(num_vertices, edges, red, red_demands):
            if not has_star_forest(num_vertices, edges, blue, blue_demands):
                return False, mask
    return True, None

# C7 obstruction to overly local/minimum-degree lemmas.
C7 = [(i, (i + 1) % 7) for i in range(7)]

# Alternating avoiding coloring.
red = {0, 2, 4, 6}
blue = set(range(7)) - red
assert not has_star_forest(7, C7, red, [2, 2])
assert not has_star_forest(7, C7, blue, [2, 2])

# Pivotal coloring at e_0:
red0 = {2, 3, 6}
blue0 = {1, 4, 5}
assert not has_star_forest(7, C7, red0, [2, 2])
assert not has_star_forest(7, C7, blue0, [2, 2])
assert has_star_forest(7, C7, red0 | {0}, [2, 2])
assert has_star_forest(7, C7, blue0 | {0}, [2, 2])
```

For a finite search of the seed \((3,2)\) versus \((3,2)\):

```text
for q = 1,...,11:
    generate every unlabeled simple graph H with q edges and no isolated vertices
    discard H unless it contains K1,3 disjoint from K1,2 uncolored
    for each of the 2^q edge colorings:
        test red [3,2] by exact star packing
        test blue [3,2] by exact star packing
        if both are absent, record the coloring and stop testing H
    if no avoiding coloring exists:
        output H as a counterexample
```

Corollary 8.1 predicts that this search finds no arrowing graph.

## Route Diagnosis

**Proved ledger**

- The universal disjoint-star upper bound \(L\).
- The pivotal-edge lower bound
  \[
  \widehat R(G_1,G_2)\ge e(G_1)+e(G_2)-1.
  \]
- The star-forest transversal bound
  \[
  \widehat R(F_1,F_2)\ge
  \max\{B+(s-1)m_1,\ A+(t-1)n_1\}.
  \]
- The full conjectured formula when either target is a matching.
- The exceptional-vertex extension lemma, which safely implements component peeling.
- The even-capacity bounded-degree decomposition.
- The maximizing-path theorem.
- The \(s=t=2\), \(n_1,m_1\) odd exact case.

**Dead ends**

- Merely knowing that every edge of a minimal Ramsey graph belongs to transverse copies of both targets is insufficient. On \(C_7\), every edge has an avoiding coloring of its deletion for which either color of that edge creates \(2K_{1,2}\), yet \(C_7\) itself has an avoiding alternating coloring.
- Minimum degree or a single low-degree vertex does not control leaf-completion effects.
- Requiring both colors to avoid their largest individual stars is too strong; odd cycles already obstruct the corresponding degree decomposition.
- A fixed lattice-path induction cannot generally sum to \(L\), because pointwise antidiagonal maximizers can jump incompatibly.

**Precise block**

The peeling argument naturally pays the cell value
\[
n_i+m_j-1
\]
at the current state \((i,j)\). The conjectured value instead sums the independent maximum on every antidiagonal. When these maxima do not form a monotone path, the induction loses an exact positive amount. Recovering that amount requires either:

1. a multi-vertex reduction that can jump between nonadjacent maximizing states without losing control of disjoint components; or
2. a packing-aware coloring theorem for the residual low-degree core that uses the slack \(l_{i+j}-(n_i+m_j-1)\).

Neither statement has been proved here, and either appears to contain the central unresolved difficulty. A fresh attempt should focus specifically on such “maximizer-jump” antidiagonals, preferably beginning with \(3\times3\) parameter lists where the best monotone-path sum is \(L-1\) or \(L-2\).