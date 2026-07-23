STATUS: BLOCKED

## Result

For the natural repaired question assuming \(\operatorname{ex}(n;\mathcal F)\) is unbounded, Route 4 can be made rigorous in several substantial cases but does not presently solve the all-bipartite cyclic case. I proved a precise copy-hypergraph deletion lemma, a sequential retention criterion, retention for families with no bipartite member, a reduction eliminating nonbipartite members when bipartite members exist, and the repaired conjecture whenever \(\mathcal F\) contains a forest. I also found an explicit unbounded family, \(\{P_4,2K_2\}\), showing that retention can fail catastrophically for the wrong choice of \(G\): an extremal \(P_4\)-free graph can have only \(O(1)\) edges in its largest \(\mathcal F\)-free subgraph despite having \(\Theta(n)\) edges. Thus unboundedness alone gives no copy-hypergraph control for a prescribed member. The remaining core is a finite family of bipartite graphs each containing a cycle, where the needed constant-fraction independent-set theorem remains unproved and is essentially as strong as the repaired problem itself.

## Complete Argument

### 1. Target of Route 4

The literal assertion in the brief is already disproved by
\[
\mathcal F=\{P_3,2K_2\}.
\]
Thus Route 4 is meaningful only for the natural repair:

> **Unbounded repaired question.** If \(\mathcal F\) is finite and
> \[
> \sup_n\operatorname{ex}(n;\mathcal F)=\infty,
> \]
> must some \(G\in\mathcal F\) satisfy
> \[
> \operatorname{ex}(n;G)=O_{\mathcal F}(\operatorname{ex}(n;\mathcal F))?
> \]

All statements below concern this repaired question.

---

### 2. Exact copy-hypergraph formulation

Fix \(G\in\mathcal F\) and let \(X\) be a \(G\)-free graph. Define a hypergraph
\[
\mathscr C_X(\mathcal F\setminus\{G\})
\]
as follows:

- its vertex set is \(E(X)\);
- for every \(H\in\mathcal F\setminus\{G\}\) and every copy \(H'\subseteq X\), the edge set \(E(H')\subseteq E(X)\) is a hyperedge.

Repeated copies with the same edge set may be identified; this does not affect independence.

#### Lemma 2.1: Exact equivalence

For \(S\subseteq E(X)\), the spanning subgraph
\[
Y=(V(X),S)
\]
is \(\mathcal F\)-free if and only if \(S\) is an independent set in
\(\mathscr C_X(\mathcal F\setminus\{G\})\).

#### Proof

Because \(Y\subseteq X\) and \(X\) is \(G\)-free, \(Y\) is automatically \(G\)-free.

If \(Y\) contains a copy \(H'\) of some \(H\in\mathcal F\setminus\{G\}\), then
\[
E(H')\subseteq S,
\]
so \(S\) contains a hyperedge of the copy hypergraph.

Conversely, if a hyperedge \(E(H')\) is contained in \(S\), all edges of the corresponding copy \(H'\) lie in \(Y\), so \(Y\) contains \(H\). Isolated vertices in \(H\) cause no difficulty: the copy \(H'\subseteq X\) already specifies their distinct images, and deleting other edges does not invalidate a non-induced copy. ∎

Thus Route 4 asks for a member \(G\) such that, in appropriate near-extremal \(G\)-free graphs \(X\),
\[
\alpha\!\left(\mathscr C_X(\mathcal F\setminus\{G\})\right)
\ge c_{\mathcal F}e(X).
\]

---

### 3. A rigorous random deletion lemma

A simple but useful sufficient condition is that the copy hypergraph have bounded average degree.

#### Lemma 3.1: Linear-copy deletion lemma

Let \(X\) have \(m\) edges, and let \(\mathcal A\) be a finite family of graphs, each having at least two edges. Suppose the total number \(Q\) of distinct edge sets of copies in \(X\) of members of \(\mathcal A\) satisfies
\[
Q\le Am
\]
for some constant \(A\ge0\). Then \(X\) has an \(\mathcal A\)-free subgraph \(Y\) with
\[
e(Y)\ge \frac{m}{4(A+1)}.
\]

#### Proof

Retain every edge of \(X\) independently with probability
\[
p=\frac1{2(A+1)}.
\]
Let \(S\) be the retained edge set, and let \(N(S)\) be the number of copy-hyperedges completely contained in \(S\).

Every copy-hyperedge has size at least two, so
\[
\mathbb E N(S)\le p^2Q\le Ap^2m.
\]
Also,
\[
\mathbb E|S|=pm.
\]
Consequently,
\[
\mathbb E\bigl(|S|-N(S)\bigr)
\ge (p-Ap^2)m.
\]
Since
\[
Ap=\frac{A}{2(A+1)}<\frac12,
\]
we obtain
\[
p-Ap^2=p(1-Ap)\ge\frac p2=\frac1{4(A+1)}.
\]
Hence some outcome satisfies
\[
|S|-N(S)\ge \frac{m}{4(A+1)}.
\]

For each copy-hyperedge contained in \(S\), choose one of its edges and delete the union of the chosen edges. At most \(N(S)\) edges are deleted. The remaining set is independent in the copy hypergraph and therefore gives an \(\mathcal A\)-free subgraph with at least
\[
|S|-N(S)\ge \frac{m}{4(A+1)}
\]
edges. ∎

This proves the desired retention whenever, for a suitable \(G\), every relevant \(G\)-free graph contains only \(O_{\mathcal F}(e(X))\) copies of all the other forbidden graphs. The later counterexample shows that unbounded joint extremal number does not imply this copy bound.

---

### 4. Sequential pairwise retention

It is enough to solve pairwise retention problems one at a time.

#### Lemma 4.1: Sequential retention

Fix \(G\in\mathcal F\). Suppose that for every \(H\in\mathcal F\setminus\{G\}\) there is \(c_H>0\) such that every \(G\)-free graph \(Z\) has an \(H\)-free subgraph \(Z'\subseteq Z\) satisfying
\[
e(Z')\ge c_H e(Z).
\]
Then every \(G\)-free graph \(X\) has an \(\mathcal F\)-free subgraph \(Y\) with
\[
e(Y)\ge
\left(\prod_{H\in\mathcal F\setminus\{G\}}c_H\right)e(X).
\]

#### Proof

Order the other members as \(H_1,\dots,H_k\). Starting with \(X_0=X\), recursively choose an \(H_i\)-free subgraph
\[
X_i\subseteq X_{i-1},\qquad e(X_i)\ge c_{H_i}e(X_{i-1}).
\]
Every \(X_i\) remains \(G\)-free. Moreover, passing to a subgraph cannot create a previously forbidden graph, so \(X_i\) remains \(H_j\)-free for \(j<i\). Therefore \(X_k\) is \(\mathcal F\)-free and
\[
e(X_k)\ge\left(\prod_{i=1}^k c_{H_i}\right)e(X).
\]
∎

The obstacle is that even the pairwise assertion can fail for a badly chosen \(G\), as shown in Section 8.

---

### 5. Route 4 succeeds for families with no bipartite member

Suppose every \(H\in\mathcal F\) is nonbipartite, and put
\[
r=\min_{H\in\mathcal F}\chi(H)\ge3.
\]
Choose \(G\in\mathcal F\) with \(\chi(G)=r\).

#### Proposition 5.1

Every graph \(X\), in particular every \(G\)-free graph \(X\), has an \(\mathcal F\)-free subgraph \(Y\) with
\[
e(Y)\ge \frac{r-2}{r-1}e(X).
\]

#### Proof

Partition \(V(X)\) independently and uniformly into \(r-1\) classes, and retain only edges whose endpoints lie in different classes. Every edge is retained with probability
\[
1-\frac1{r-1}=\frac{r-2}{r-1}.
\]
Thus some partition retains at least that proportion of the edges.

The retained graph is \((r-1)\)-partite, hence has chromatic number at most \(r-1\). It cannot contain any \(H\in\mathcal F\), since every such \(H\) has chromatic number at least \(r\). ∎

Applying this to an extremal \(G\)-free graph gives
\[
\operatorname{ex}(n;\mathcal F)
\ge \frac{r-2}{r-1}\operatorname{ex}(n;G).
\]

This is a full Route 4 retention theorem, stronger than the usual Erdős–Stone asymptotic argument.

---

### 6. Bounded-versus-linear dichotomy

The bounded obstruction admits a useful strengthening: once it is absent, the joint extremal number is automatically at least linear.

For a graph \(H\), call it:

- **star-supported** if all edges of \(H\) have a common endpoint after isolated vertices are ignored;
- **matching-supported** if its nonisolated part is a matching.

#### Lemma 6.1: Dichotomy

Let \(\mathcal F\) be a finite family of graphs, each having at least one edge. Exactly one of the following holds asymptotically:

1. \(\mathcal F\) contains both a star-supported member and a matching-supported member, in which case
   \[
   \operatorname{ex}(n;\mathcal F)=O_{\mathcal F}(1);
   \]
2. at least one of the following graphs is \(\mathcal F\)-free for every \(n\):
   \[
   K_{1,n-1},\qquad M_{\lfloor n/2\rfloor},
   \]
   and consequently
   \[
   \operatorname{ex}(n;\mathcal F)\ge \left\lfloor\frac n2\right\rfloor.
   \]

#### Proof

Suppose first that \(\mathcal F\) contains a star-supported graph \(H_s\) with \(s=e(H_s)\), and a matching-supported graph \(H_m\) with \(t=e(H_m)\).

For \(n\ge\max\{v(H_s),v(H_m)\}\), any vertex of degree at least \(s\) supplies the nonisolated part of \(H_s\), while the remaining vertices can supply its isolated vertices. Thus every \(\mathcal F\)-free graph \(X\) has
\[
\Delta(X)\le s-1.
\]
Likewise, a matching of size \(t\) supplies \(H_m\), so
\[
\nu(X)\le t-1.
\]
Let \(M\) be a maximal matching. Its endpoint set \(S\) is a vertex cover and
\[
|S|\le2(t-1).
\]
Therefore
\[
e(X)\le\sum_{v\in S}\deg(v)
\le2(t-1)(s-1).
\]

Conversely, suppose no member of \(\mathcal F\) is star-supported. Then no member can embed into a star, so \(K_{1,n-1}\) is \(\mathcal F\)-free.

If instead no member is matching-supported, no member can embed into a matching, so \(M_{\lfloor n/2\rfloor}\) is \(\mathcal F\)-free.

If the family does not contain both kinds of supported member, at least one of these alternatives applies. ∎

Hence for finite forbidden families there is no genuinely sublinear-but-unbounded regime:
\[
\operatorname{ex}(n;\mathcal F)=O(1)
\quad\text{or}\quad
\operatorname{ex}(n;\mathcal F)=\Omega(n).
\]

---

### 7. The repaired conjecture holds whenever a forest is present

#### Lemma 7.1: Elementary forest bound

If \(T\) is a forest on \(h\ge2\) vertices, then
\[
\operatorname{ex}(n;T)\le(h-2)n.
\]

#### Proof

Extend \(T\) to a tree \(T^*\) on the same \(h\) vertices by adding edges between its components.

Suppose a graph \(X\) has more than \((h-2)n\) edges. Repeatedly delete a vertex of degree at most \(h-2\), for as long as one exists. If every vertex were deleted, the total number of edges removed would be at most \((h-2)n\), a contradiction. Thus a nonempty subgraph \(X'\subseteq X\) remains with
\[
\delta(X')\ge h-1.
\]

Every tree on \(h\) vertices embeds greedily in a graph of minimum degree at least \(h-1\): order the tree from a root so that parents precede children, and embed each new vertex at an unused neighbor of its already embedded parent. At any stage fewer than \(h\) vertices have been used, while the parent has at least \(h-1\) neighbors.

Thus \(X'\) contains \(T^*\), and therefore contains \(T\), contradicting \(T\)-freeness. ∎

#### Theorem 7.2: Forest-containing unbounded families

Let \(\mathcal F\) be finite, assume its joint extremal number is unbounded, and suppose \(\mathcal F\) contains a forest \(G\) on \(h\) vertices. Then
\[
\operatorname{ex}(n;G)
\le 3(h-2)\operatorname{ex}(n;\mathcal F)
\]
for all sufficiently large \(n\).

#### Proof

By Lemma 6.1, because the joint extremal number is unbounded, either every star is \(\mathcal F\)-free or every matching is \(\mathcal F\)-free.

In the star case,
\[
\operatorname{ex}(n;\mathcal F)\ge n-1\ge \frac n2.
\]
In the matching case,
\[
\operatorname{ex}(n;\mathcal F)\ge\left\lfloor\frac n2\right\rfloor\ge\frac n3
\]
for \(n\ge2\). Thus in all cases
\[
\operatorname{ex}(n;\mathcal F)\ge\frac n3.
\]
Lemma 7.1 gives
\[
\operatorname{ex}(n;G)\le(h-2)n
\le3(h-2)\operatorname{ex}(n;\mathcal F).
\]
∎

This also has a weak Route 4 realization. The \(\mathcal F\)-free star or matching furnished by Lemma 6.1 has \(\Theta(n)\) edges and is therefore a constant-factor near-extremal \(G\)-free graph by Lemma 7.1. Its copy hypergraph is empty, so it retains all of its edges. This does not assert retention inside every extremal \(G\)-free graph.

---

### 8. Retention can fail for the wrong member even when the joint extremal number is unbounded

Let
\[
\mathcal F=\{P_4,2K_2\},
\]
where \(P_4\) is the path with three edges.

#### Proposition 8.1

For \(n\ge4\),
\[
\operatorname{ex}(n;\mathcal F)=n-1.
\]

#### Proof

Every \(P_4\) contains two disjoint edges, namely its first and third edges. Consequently every \(2K_2\)-free graph is automatically \(P_4\)-free. Thus
\[
\operatorname{ex}(n;\mathcal F)=\operatorname{ex}(n;2K_2).
\]

A \(2K_2\)-free graph has pairwise-intersecting edges. Such an edge family is either contained in a star or is the three-edge set of a triangle: if \(ab\) and \(ac\) are present and an edge not containing \(a\) is present, it must be \(bc\); any further distinct edge would miss at least one of \(ab,ac,bc\). Therefore
\[
e(X)\le\max\{n-1,3\}=n-1
\]
for \(n\ge4\), and the star attains this bound. ∎

Thus the joint extremal number is unbounded and is controlled by \(2K_2\).

Now choose the wrong member \(G=P_4\).

#### Proposition 8.2

For \(n=3q\), the graph
\[
X=qK_3
\]
is extremal \(P_4\)-free and has \(e(X)=n\), but every \(\mathcal F\)-free subgraph of \(X\) has at most three edges.

#### Proof

First classify connected \(P_4\)-free graphs.

- If a connected component is acyclic, it is a tree with no path of length three, hence has diameter at most two and is a star.
- If it contains a cycle, a shortest cycle cannot have length at least four, since three consecutive cycle edges would form a \(P_4\). Hence it contains a triangle \(abc\). If there were any vertex outside this triangle in the same component, a shortest path to the triangle would supply an outside vertex \(y\) adjacent to, say, \(a\); then
  \[
  y-a-b-c
  \]
  is a non-induced \(P_4\), a contradiction.

Thus every connected \(P_4\)-free graph is a star or a triangle. Each such component has at most as many edges as vertices. Hence every \(n\)-vertex \(P_4\)-free graph has at most \(n\) edges. For \(n=3q\), \(qK_3\) has exactly \(n\) edges, so it is extremal.

Now let \(Y\subseteq qK_3\) be \(2K_2\)-free. If \(Y\) had an edge in each of two different triangle components, those two edges would be disjoint. Therefore every edge of \(Y\) lies in a single triangle, and
\[
e(Y)\le3.
\]
Since \(X\) is already \(P_4\)-free, this is also the largest possible size of an \(\mathcal F\)-free subgraph of \(X\). ∎

Therefore
\[
\frac{\max\{e(Y):Y\subseteq X,\ Y\text{ is }\mathcal F\text{-free}\}}
{e(X)}
\le \frac3n\longrightarrow0.
\]

The copy hypergraph here is especially transparent. Its \(3q\) vertices are partitioned into \(q\) groups of three, corresponding to the edges of the triangles. Its hyperedges are all pairs of vertices from different groups. Hence
\[
\alpha=3
\]
and the number of hyperedges is
\[
9\binom q2=\Theta(e(X)^2).
\]

This proves that:

- unbounded joint extremal number does not imply retention for an arbitrary \(G\in\mathcal F\);
- linear bounds on the number of other forbidden copies cannot be inferred from unboundedness;
- choosing the correct member is an essential and nonlocal part of Route 4.

---

### 9. Reduction to the all-bipartite cyclic core

Let
\[
\mathcal B=\{H\in\mathcal F:H\text{ is bipartite}\}.
\]

#### Proposition 9.1

If \(\mathcal B\ne\varnothing\), then
\[
\frac12\operatorname{ex}(n;\mathcal B)
\le \operatorname{ex}(n;\mathcal F)
\le \operatorname{ex}(n;\mathcal B).
\]

#### Proof

The upper bound is immediate because every \(\mathcal F\)-free graph is \(\mathcal B\)-free.

For the lower bound, take an extremal \(\mathcal B\)-free graph \(X\). A random bipartition of its vertices retains each edge as a crossing edge with probability \(1/2\), so some bipartite spanning subgraph \(Y\subseteq X\) has
\[
e(Y)\ge\frac12e(X).
\]
As a subgraph of \(X\), it remains \(\mathcal B\)-free. Since it is bipartite, it contains no nonbipartite member of \(\mathcal F\). Hence it is \(\mathcal F\)-free. ∎

Consequences:

1. If \(\mathcal B=\varnothing\), Proposition 5.1 solves the problem.
2. If \(\mathcal B\) contains a forest and the joint extremal number is unbounded, Theorem 7.2 solves it.
3. If some \(G\in\mathcal B\) controls \(\mathcal B\), then it controls \(\mathcal F\) with at most an additional factor of two.

The unresolved core is therefore:

> \(\mathcal F\) is a finite family of bipartite graphs, and every member contains a cycle.

In this core, all stars and matchings are automatically \(\mathcal F\)-free, but these provide only linear lower bounds, while singleton extremal numbers may be superlinear.

---

### 10. Why the natural template version of Route 4 stops at bipartite graphs

For nonbipartite families, Proposition 5.1 used a fixed multipartite template. This cannot directly extend to a family containing a bipartite graph \(H\) with an edge.

Indeed, every such \(H\) admits a homomorphism
\[
H\longrightarrow K_2.
\]
If a template \(T\) has any edge, then
\[
K_2\longrightarrow T,
\]
so \(H\to T\). A sufficiently large blow-up of \(T\) therefore contains \(H\): assign distinct clones to vertices of \(H\) having the same template image.

Thus no positive-edge template can have all its blow-ups \(H\)-free. The successful random-partition argument for nonbipartite families has no direct bipartite analogue.

---

### 11. Precise block

To finish Route 4 in the remaining all-bipartite cyclic case, one would need to prove that some \(G\in\mathcal F\) has the following property:

\[
\alpha\!\left(
\mathscr C_X(\mathcal F\setminus\{G\})
\right)
\ge c_{\mathcal F}e(X)
\tag{*}
\]
for every sufficiently large extremal, or at least for some sufficiently dense near-extremal, \(G\)-free graph \(X\).

The available hypotheses do not imply:

- \(O(e(X))\) total copy-hyperedges;
- bounded copy-hypergraph degrees or codegrees;
- a bounded decomposition of \(E(X)\) into \(\mathcal F\)-free classes;
- a fixed homomorphic template avoiding the family.

Moreover, Proposition 8.2 shows that unboundedness alone does not imply \((*)\) for a prescribed member. There is currently no rigorous rule selecting a member for which \((*)\) must hold. Proving that such a member always exists is essentially a stronger form of the repaired conjecture, rather than a reduction to a simpler established statement.

## Self-Audit

1. **Handling of isolated vertices in the bounded-versus-linear dichotomy.** The degree and matching bounds require \(n\ge\max_{H\in\mathcal F}v(H)\), so that unused host vertices can represent isolated forbidden vertices. I believe the statement is sound because this threshold is explicitly imposed and non-induced containment permits those images to have extra incident edges.

2. **The forest upper bound is deliberately coarse.** The claim \(\operatorname{ex}(n;G)\le(h-2)n\) is weaker than standard forest bounds. It nevertheless holds by the fully given deletion-to-minimum-degree and greedy tree-embedding argument, including disconnected forests by first extending them to a tree on the same vertex set.

3. **The bad-retention example depends on exact extremality of \(qK_3\).** This is not being inferred from Erdős–Gallai without proof: the connected-component classification shows directly that every \(P_4\)-free component is a star or triangle and hence every \(P_4\)-free graph has at most \(n\) edges. Thus \(qK_3\) is genuinely extremal when \(3\mid n\).

## Computations To Verify

The following exhaustive program verifies the extremal values for \(\{P_4,2K_2\}\) for small \(n\).

```python
from itertools import combinations, permutations

def edge_data(n):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    return edges, index

def edge_bit(index, u, v):
    if u > v:
        u, v = v, u
    return 1 << index[(u, v)]

def forbidden_patterns(n):
    edges, index = edge_data(n)

    p4 = set()
    for a, b, c, d in permutations(range(n), 4):
        mask = (
            edge_bit(index, a, b)
            | edge_bit(index, b, c)
            | edge_bit(index, c, d)
        )
        p4.add(mask)

    m2 = set()
    for e1, e2 in combinations(edges, 2):
        if len(set(e1 + e2)) == 4:
            mask = (1 << index[e1]) | (1 << index[e2])
            m2.add(mask)

    return edges, list(p4), list(m2)

def contains_pattern(mask, patterns):
    return any((mask & p) == p for p in patterns)

def extrema(n):
    edges, p4_patterns, m2_patterns = forbidden_patterns(n)
    best_p4 = 0
    best_m2 = 0
    best_joint = 0

    for mask in range(1 << len(edges)):
        count = mask.bit_count()
        has_p4 = contains_pattern(mask, p4_patterns)
        has_m2 = contains_pattern(mask, m2_patterns)

        if not has_p4:
            best_p4 = max(best_p4, count)
        if not has_m2:
            best_m2 = max(best_m2, count)
        if not has_p4 and not has_m2:
            best_joint = max(best_joint, count)

    return best_p4, best_m2, best_joint

for n in range(1, 8):
    print(n, extrema(n))
```

Expected output:

```text
1 (0, 0, 0)
2 (1, 1, 1)
3 (3, 3, 3)
4 (3, 3, 3)
5 (4, 4, 4)
6 (6, 5, 5)
7 (6, 6, 6)
```

The expected general formulas are
\[
\operatorname{ex}(n;P_4)
=
3\left\lfloor\frac n3\right\rfloor
+\binom{n\bmod 3}{2},
\]
and
\[
\operatorname{ex}(n;2K_2)
=
\operatorname{ex}(n;\{P_4,2K_2\})
=
n-1\qquad(n\ge4).
\]

The secondary optimization inside \(qK_3\) can be checked as follows.

```python
from itertools import combinations

def q_triangles(q):
    edges = []
    for i in range(q):
        a, b, c = 3*i, 3*i + 1, 3*i + 2
        edges.extend([(a, b), (a, c), (b, c)])
    return edges

def two_edges_disjoint(e, f):
    return len(set(e + f)) == 4

def largest_2K2_free_subgraph_of_qK3(q):
    edges = q_triangles(q)
    best = 0

    for mask in range(1 << len(edges)):
        chosen = [edges[i] for i in range(len(edges))
                  if (mask >> i) & 1]
        if all(not two_edges_disjoint(e, f)
               for e, f in combinations(chosen, 2)):
            best = max(best, len(chosen))

    return len(edges), best

for q in range(1, 6):
    m, alpha = largest_2K2_free_subgraph_of_qK3(q)
    copy_hyperedges = 9 * q * (q - 1) // 2
    print(q, m, alpha, copy_hyperedges)
```

Expected output:

```text
1 3 3 0
2 6 3 9
3 9 3 27
4 12 3 54
5 15 3 90
```

For arbitrary candidate families and host graphs, the secondary Route 4 optimization is the following binary program:

```text
Variables:
    y_e in {0,1} for every e in E(X).

Objective:
    maximize sum_{e in E(X)} y_e.

Constraints:
    For every H in F \ {G} and every injective embedding phi of H into X,
        sum_{uv in E(H)} y_{phi(u)phi(v)} <= e(H)-1.
```

Its optimum is exactly the independence number of the copy hypergraph and hence the largest number of edges in an \(\mathcal F\)-free subgraph of the \(G\)-free host \(X\).

## Route Diagnosis

**Proved ledger.**

- Exact equivalence between \(\mathcal F\)-free subgraphs and independent sets in the copy hypergraph.
- Constant retention when the total number of relevant copies is \(O(e(X))\).
- Sequential reduction from family retention to pairwise retention.
- Constant retention for families with no bipartite member.
- The bounded-versus-linear dichotomy for finite forbidden families.
- The unbounded repaired conjecture whenever the family contains a forest.
- A factor-two reduction from a mixed family to its bipartite subfamily.
- An unbounded example where an extremal graph for the wrong member has retained fraction tending to zero.

**Plausible but unproved.**

- In every finite all-bipartite cyclic family, some member may admit constant-fraction retention in a suitable near-extremal construction.
- Selecting a member with the smallest singleton Turán scale may be the right principle, but no fixed-member or constant-factor selection theorem is known here.
- Structural bounds on copy concentration, rather than raw copy counts, may suffice via a tailored independent-set theorem.

**Dead ends.**

- Retention for an arbitrary chosen \(G\): disproved by \(\{P_4,2K_2\}\) with \(G=P_4\).
- Inferring \(O(e(X))\) copies from unbounded joint extremal number: the same example has \(\Theta(e(X)^2)\) copy-hyperedges.
- Fixed positive-density homomorphic templates: impossible for bipartite forbidden graphs because every bipartite graph maps to \(K_2\).
- Invoking containers without additional hypotheses: containers generally organize independent sets but do not by themselves force a linear-sized independent set in a dense copy hypergraph.

**Sharp block.** After all rigorous reductions, Route 4 requires a constant-fraction independent-set theorem for copy hypergraphs arising from extremal graphs for some member of a finite all-bipartite cyclic family. No consequence of unboundedness supplies the needed copy, degree, codegree, or transversal bounds. Establishing this retention statement is at least as strong as the repaired conjecture and may be strictly stronger if required for every extremal host.

A fresh attempt should therefore focus on relative Turán problems for pairs of bipartite cyclic graphs: compute or bound the largest \(H\)-free subgraph of extremal \(G\)-free constructions, identify which member minimizes the relative loss, and seek family-specific decompositions or sparsifications. Raw copy counting should not be the primary invariant; concentration and the minimum edge-transversal number of the copy hypergraph are more relevant.