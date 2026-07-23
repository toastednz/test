STATUS: BLOCKED

## Result

Route 2 yields a sharp ordinary-block accounting lemma: every \(n\)-vertex graph with \(t_2(n)+1\) edges has a 2-connected block containing at least \(n^2/8-O(n)\) edges. This proves the desired lower bound whenever that dense block is \(C_7\)-pair-linked—for example, for clique-block hosts or blocks of minimum degree at least half their order plus \(4\). I also prove a strong linkage lemma for uniformly almost-complete bipartite graphs containing one internal edge. However, ordinary 2-connectivity is fundamentally insufficient: there are 2-connected graphs with \(e=v^2/4-\Theta(v)\), containing a \(C_7\), but whose conflict graph has chromatic number exactly \(7\). There are even exact \(t_2(n)+1\)-edge, 2-connected hosts whose two quadratic palettes are separated from one another by length-\(3\) connectors. Thus Route 2 is blocked precisely at a second-order “activation” theorem: one must show that the \(O(n)\) edges needed to raise a nearly extremal, \(C_7\)-inert structure to \(t_2(n)+1\) activate at least \(n^2/8-o(n^2)\) colors. This is comparable in strength to the original \(C_7\) problem.

## Complete Argument

### 1. Exact decomposition over ordinary blocks

A block means either a maximal 2-connected subgraph or a bridge regarded as a copy of \(K_2\).

#### Lemma 1
Let \(H\) have blocks \(B_1,\dots,B_s\), and put
\[
t_i=|V(B_i)|-1,\qquad e_i=|E(B_i)|.
\]
Then:

1. every edge of \(H\) belongs to exactly one block;
2. every cycle of \(H\), hence every \(C_7\), is contained in exactly one block;
3. consequently,
   \[
   Q_7(H)=\bigsqcup_{i=1}^s Q_7(B_i)
   \quad\text{and}\quad
   \chi(Q_7(H))=\max_i\chi(Q_7(B_i));
   \]
4. if \(H\) has \(c\) connected components, including isolated vertices, then
   \[
   \sum_{i=1}^s t_i=n-c\le n-1.
   \]

#### Proof
The first two assertions are standard consequences of the block-cut tree, but here is the needed argument. Two distinct blocks share at most one vertex. A cycle is 2-connected, so all its edges lie in one maximal 2-connected subgraph. Bridges lie on no cycle.

Thus two edges from different blocks cannot lie on a common \(C_7\). Conversely, every conflict witnessed inside a block is also a conflict in \(H\). Hence \(Q_7(H)\) is the disjoint union of the block conflict graphs, and the chromatic number of a disjoint union is the maximum of the chromatic numbers of its components.

For a connected graph, its block-cut tree gives
\[
\sum_B(|V(B)|-1)=|V(H)|-1.
\]
This can also be proved by adding the blocks one at a time along the block-cut tree: the first block contributes \(|V(B)|\) vertices, and every later block shares exactly one old cut vertex and contributes \(|V(B)|-1\) new vertices. Summing over connected components gives \(n-c\). ∎

---

### 2. A quadratic-size ordinary block is unavoidable

#### Lemma 2
Let \(H\) have \(n\ge2\) vertices and \(e>0\) edges. Some block \(B\) satisfies
\[
|E(B)|
\ge
2\left(\frac{e}{n-1}\right)^2-\frac{e}{n-1}.
\]
In particular, if \(e=t_2(n)+1\), then
\[
|E(B)|\ge \frac{n^2}{8}-O(n).
\]

#### Proof
Use the notation of Lemma 1 and set
\[
S=\sum_i t_i\le n-1.
\]
Since \(\sum_i e_i=e\), some \(i\) satisfies
\[
\alpha_i:=\frac{e_i}{t_i}\ge \frac eS\ge \frac{e}{n-1}=:d.
\]
Every block on \(t_i+1\) vertices has at most
\[
\binom{t_i+1}{2}=\frac{t_i(t_i+1)}2
\]
edges. Therefore
\[
\alpha_i=\frac{e_i}{t_i}\le\frac{t_i+1}{2},
\]
so \(t_i\ge2\alpha_i-1\). It follows that
\[
e_i=\alpha_i t_i
\ge \alpha_i(2\alpha_i-1)
\ge d(2d-1),
\]
where the final inequality holds because \(2x^2-x\) is increasing for \(x\ge1/4\), and here \(d\) is much larger for the relevant \(n\).

For \(e=t_2(n)+1=n^2/4+O(1)\),
\[
d=\frac{e}{n-1}=\frac n4+O(1),
\]
and hence \(2d^2-d=n^2/8-O(n)\). ∎

This is numerically the correct lower-bound scale. The difficulty is that a block with this many edges need not itself require nearly that many colors.

---

### 3. An abstract palette-accounting criterion

The following isolates exactly what a successful fixed-length linkage decomposition would provide.

#### Lemma 3
Suppose an edge set of size \(q\) is partitioned into sets
\[
F_1,\dots,F_s
\]
such that:

- every \(F_i\) is a clique of \(Q_7(H)\);
- there are numbers \(t_i\ge1\) with
  \[
  |F_i|\le \binom{t_i+1}{2};
  \]
- \(\sum_i t_i\le N\).

Then, writing \(M=\max_i|F_i|\),
\[
M\ge 2\left(\frac qN-\frac12\right)^2.
\]
Consequently, if \(q=n^2/4-o(n^2)\) and \(N=n+o(n)\), then
\[
\chi(Q_7(H))\ge M\ge \frac{n^2}{8}-o(n^2).
\]

#### Proof
For each \(i\), either \(t_i\le\sqrt{2M}\), in which case
\[
\frac{|F_i|}{t_i}\le\frac{t_i+1}{2}
\le\sqrt{\frac M2}+\frac12,
\]
or \(t_i>\sqrt{2M}\), in which case
\[
\frac{|F_i|}{t_i}\le\frac M{t_i}<\sqrt{\frac M2}.
\]
Thus in all cases
\[
|F_i|\le t_i\left(\sqrt{\frac M2}+\frac12\right).
\]
Summing,
\[
q\le N\left(\sqrt{\frac M2}+\frac12\right).
\]
Rearranging gives
\[
M\ge2\left(\frac qN-\frac12\right)^2.
\]
Since every \(F_i\) is a conflict clique, \(\chi(Q_7(H))\ge M\). ∎

Thus Route 2 would be complete if, after deleting \(o(n^2)\) edges, one could partition the remaining edges into \(C_7\)-pair-linked regions with total effective vertex cost \(n+o(n)\). The constructions below show why ordinary blocks do not provide that partition.

---

### 4. A strong fixed-length linkage lemma at the Dirac threshold

#### Lemma 4
Let \(G\) have \(m\) vertices and
\[
\delta(G)\ge \frac m2+4.
\]
Then every two distinct edges of \(G\) lie together on a simple \(C_7\). Hence
\[
Q_7(G)=K_{e(G)}
\quad\text{and}\quad
\chi(Q_7(G))=e(G).
\]

#### Proof
For any two vertices \(u,v\),
\[
|N(u)\cap N(v)|
\ge d(u)+d(v)-m
\ge8.
\]

First suppose the marked edges are adjacent, say \(xy\) and \(yz\). Choose an edge \(bc\) whose endpoints avoid \(x,y,z\). Such an edge exists because a vertex outside \(\{x,y,z\}\) has more than three neighbors.

Choose
\[
a\in N(x)\cap N(b)
\]
outside \(\{x,y,z,b,c\}\). This is possible because the common neighborhood has at least eight vertices and at most five are forbidden. Next choose
\[
d\in N(c)\cap N(z)
\]
outside \(\{x,y,z,a,b,c\}\), again possible because at most six vertices are forbidden. Then
\[
x\,y\,z\,d\,c\,b\,a\,x
\]
is a simple \(7\)-cycle containing both marked edges.

Now suppose the marked edges \(xy\) and \(zw\) are disjoint. Choose
\[
a\in N(y)\cap N(z)
\]
outside \(\{x,y,z,w\}\). Choose
\[
b\in N(w)\setminus\{x,y,z,w,a\}.
\]
Finally choose
\[
c\in N(b)\cap N(x)
\]
outside \(\{x,y,z,w,a,b\}\). The common-neighborhood bound again ensures this is possible. Then
\[
x\,y\,a\,z\,w\,b\,c\,x
\]
is a simple \(7\)-cycle containing both marked edges.

These are the only two positional types for two distinct edges. ∎

#### Corollary 5
If \(H\) contains a subgraph \(G\) on \(m\) vertices with
\[
\delta(G)\ge m/2+4,
\]
then every valid coloring of \(H\) uses at least
\[
e(G)\ge\frac{m^2}{4}+2m
\]
colors.

In particular, this proves the target whenever such a subgraph has
\[
m\ge(1/\sqrt2-o(1))n.
\]

The limitation is serious: \(K_{m/2,m/2}\) plus one internal edge has minimum degree only \(m/2\), and no pruning argument preserves enough edges while raising the minimum degree by a constant.

---

### 5. Clique-block hosts are settled by Route 2

#### Proposition 6
Suppose every block of \(H\) is a clique. If
\[
|V(H)|=n,\qquad |E(H)|=t_2(n)+1,
\]
then every rainbow-\(C_7\) coloring of \(H\) uses at least
\[
\frac{n^2}{8}-O(n)
\]
colors.

#### Proof
By Lemma 2, some block \(B\) has \(n^2/8-O(n)\) edges and therefore has order tending to infinity. In particular, \(|V(B)|\ge7\).

Any two distinct edges of \(K_m\), \(m\ge7\), lie on a common \(C_7\). For adjacent edges, put them consecutively and add four fresh vertices; for disjoint edges, put each as a consecutive pair and add three fresh vertices. Completeness supplies all remaining cycle edges.

Thus \(Q_7(B)\) is complete, so all edges of \(B\) need distinct colors. Lemma 1 now gives the claimed lower bound. ∎

The same proof works whenever the block selected in Lemma 2 is \(C_7\)-pair-linked after deletion of only \(o(n^2)\) exceptional edges.

---

### 6. A near-complete bipartite activation lemma

This is the most useful concrete progress toward the delicate near-bipartite case.

#### Lemma 7
Let \(A,B\) be disjoint sets of sizes \(a,b\), and let \(R\) be a bipartite graph between them such that
\[
d_R(u)\ge b-s\quad(u\in A),
\qquad
d_R(v)\ge a-s\quad(v\in B).
\]
Suppose \(xy\) is an additional edge inside \(A\). Assume
\[
a-s\ge4,\qquad b-2s\ge3.
\]
Set
\[
C=N_R(x)\cap N_R(y)
\]
and
\[
F=E_R(A\setminus\{x,y\},C).
\]
Then every two distinct edges of \(F\) lie together on a \(C_7\) using the internal edge \(xy\). Moreover,
\[
|F|\ge (a-2)(b-3s).
\]

#### Proof
By inclusion-exclusion,
\[
|C|\ge b-2s.
\]
Every \(p\in A\setminus\{x,y\}\) has at most \(s\) nonneighbors in all of \(B\), hence at least \(|C|-s\) neighbors in \(C\). Therefore
\[
|F|\ge(a-2)(|C|-s)\ge(a-2)(b-3s).
\]

It remains to prove pairwise linkage. Let the two marked edges be \(pr\) and \(qu\), with \(p,q\in A\setminus\{x,y\}\) and \(r,u\in C\).

If \(p\ne q\) and \(r\ne u\), choose
\[
t\in N_R(p)\cap N_R(q)\setminus\{r,u\}.
\]
The common neighborhood has size at least \(b-2s\ge3\). Then
\[
x\,r\,p\,t\,q\,u\,y\,x
\]
is the required \(C_7\).

If \(p=q\) and \(r\ne u\), choose
\[
z\in N_R(u)\setminus\{x,y,p\}.
\]
This is possible because \(d_R(u)\ge a-s\ge4\). Next choose
\[
t\in N_R(z)\cap N_R(y)\setminus\{r,u\}.
\]
Then
\[
x\,r\,p\,u\,z\,t\,y\,x
\]
is a simple \(C_7\) containing both marked edges.

Finally, if \(r=u\) and \(p\ne q\), choose distinct
\[
t\in N_R(x)\cap N_R(p)\setminus\{r\},
\qquad
z\in N_R(q)\cap N_R(y)\setminus\{r,t\}.
\]
Both common neighborhoods have size at least \(b-2s\ge3\). Then
\[
x\,t\,p\,r\,q\,z\,y\,x
\]
is the desired cycle.

These cases exhaust all possibilities for two distinct bipartite edges. ∎

#### Consequence
If \(a,b=\Theta(n)\) and \(s=o(n)\), the lemma produces a conflict clique of size
\[
ab-o(n^2).
\]
For a balanced almost-complete bipartite graph, this is \(n^2/4-o(n^2)\), substantially stronger than the required \(n^2/8-o(n^2)\).

The unresolved difficulty is to derive the uniform maximum-deficiency hypothesis from the exact edge count. Missing cross edges can be concentrated on a small exceptional vertex set, and the compensating internal edges can also concentrate there. Deleting those vertices loses the very \(O(n)\)-scale information that distinguishes \(t_2(n)\) from \(t_2(n)+1\).

---

### 7. Ordinary 2-connectivity does not imply fixed-length linkage

#### Proposition 8
For arbitrarily large \(m\), there is a 2-connected \(m\)-vertex graph \(G\) such that

\[
e(G)=\frac{m^2}{4}-\Theta(m),
\qquad
G\text{ contains a }C_7,
\qquad
\chi(Q_7(G))=7.
\]

#### Proof
Take disjoint graphs \(D=K_{q,q}\) and \(R=C_7\). Choose distinct vertices \(d_1,d_2\in D\) and distinct vertices \(r_1,r_2\in R\). Join \(d_i\) to \(r_i\) by an internally vertex-disjoint path of length \(3\), for \(i=1,2\).

The graph has
\[
m=2q+7+4=2q+11
\]
vertices and
\[
e(G)=q^2+7+6=q^2+13
=\frac{m^2}{4}-\Theta(m).
\]

The union of two 2-connected graphs joined by two internally vertex-disjoint paths with distinct endpoints is 2-connected. This can be checked directly after deleting any one vertex: if one connecting path is broken, the other still connects \(D\) to \(R\), while both residual segments of the broken path remain attached to one of those connected pieces.

Any cycle using a connecting path must use both connecting paths. It then has length at least
\[
3+3+1+1=8,
\]
where the final two terms are the positive lengths of paths between the attachment vertices inside \(D\) and inside \(R\). Hence no \(C_7\) uses a connecting edge or vertices from both \(D\) and \(R\).

The bipartite graph \(D\) contains no \(C_7\). Thus the only \(C_7\) is the original \(R\), and \(Q_7(G)\) consists of a \(K_7\) on its seven edges together with isolated vertices. Therefore \(\chi(Q_7(G))=7\). ∎

This refutes any prospective local lemma asserting that a 2-connected graph with
\[
e(G)=|V(G)|^2/4-o(|V(G)|^2)
\]
and at least one \(C_7\) must have quadratic conflict chromatic number. Linear deficits matter.

---

### 8. Even the exact edge count does not make ordinary blocks coincide with linkage blocks

#### Proposition 9
For every sufficiently large \(n\), there is a 2-connected \(n\)-vertex graph \(H_n\) with exactly \(t_2(n)+1\) edges such that no \(C_7\) contains both an edge from one dense piece and an edge from a second dense piece.

#### Proof
Put \(s=n-4\), and let
\[
T=t_2(n)+1.
\]
Choose an integer \(d\ge0\), of the same parity as \(s\), minimal subject to
\[
d^2\ge D_n:=4(T-6)-s^2+2s.
\]
Here
\[
D_n=
\begin{cases}
10n-44,&n\text{ even},\\
10n-45,&n\text{ odd}.
\end{cases}
\]
Thus \(d=\Theta(\sqrt n)\). Put
\[
a=\frac{s+d}{2},\qquad b=\frac{s-d}{2}.
\]

Take disjoint cliques \(K_a,K_b\). Join distinct attachment vertices of the two cliques by two internally vertex-disjoint paths of length \(3\). These paths introduce four vertices and six edges. Before any deletion, the graph has
\[
E_0=\binom a2+\binom b2+6
=\frac{s^2+d^2-2s}{4}+6.
\]
By the definition of \(D_n\),
\[
E_0-T=\frac{d^2-D_n}{4}=:R.
\]
The parity choice makes \(R\) an integer. Minimality of \(d\) gives
\[
0\le R<d-1=O(\sqrt n).
\]

Delete \(R\) edges from \(K_a\), all incident with one nonattachment vertex \(z\). For large \(n\), \(z\) still has at least two neighbors, so the resulting dense piece remains 2-connected. The full graph is therefore 2-connected and now has exactly \(T\) edges.

As in Proposition 8, any cycle using a connecting path must use both paths and has length at least \(8\). Therefore every \(C_7\) is wholly contained in one of the two dense pieces. In particular, no conflict edge of \(Q_7(H_n)\) joins an edge from the first dense piece to an edge from the second. ∎

This construction does not disprove the conjecture: the larger clique has \(\frac{n^2}{8}+\Theta(n^{3/2})\) edges. Its role is diagnostic—it shows that ordinary block decomposition can conceal two quadratic, fixed-length cycle-separated palettes inside one 2-connected block.

---

### 9. Precise point at which Route 2 stops

The established results reduce a successful Route 2 proof to a theorem retaining the linear-scale deficit from the \(C_7\)-extremal threshold. A merely first-order statement is impossible by Proposition 8.

A sufficient theorem would have to resemble the following.

> **Unproved activation/decomposition statement.**  
> Given \(H\) with \(t_2(n)+1\) edges, either:
> 1. after deleting \(o(n^2)\) edges, its dense edges decompose into \(C_7\)-pair-linked pieces with total effective vertex cost \(n+o(n)\), so Lemma 3 applies; or
> 2. \(H\) has a nearly balanced, almost-complete maximum cut, and the internal edges compensating for the missing cross edges necessarily activate a conflict clique or conflict subgraph of chromatic number at least \(n^2/8-o(n^2)\).

Lemma 7 proves the second alternative when all cross deficiencies are \(o(n)\) uniformly. No argument obtained here controls concentrated deficiencies. Removal or regularity methods only give an \(o(n^2)\) error, while the decisive edge surplus is \(1\).

Taking the second alternative for a single giant 2-connected block at exactly \(t_2(n)+1\) edges is already essentially the unresolved problem. Therefore this is a genuine block, not a completed reduction to an easier theorem.

## Self-Audit

1. **The block accounting uses bridges and disconnected components.**  
   This is a possible source of off-by-one errors. The identity is nevertheless exact: each connected component satisfies \(\sum_B(|V(B)|-1)=|V|-1\), and isolated components contribute zero to both the block sum and \(|V|-1\).

2. **The minimum-degree linkage lemma relies on avoiding previously selected vertices.**  
   I used the uniform bound \(|N(u)\cap N(v)|\ge8\). At most six vertices are forbidden at any common-neighbor choice, so every selection has at least one legal option. The displayed cycles explicitly list seven distinct vertices and cover both adjacent and disjoint marked-edge cases.

3. **The almost-complete bipartite lemma has strong hypotheses and does not regularize a general maximum cut.**  
   Within those hypotheses, the proof is complete: the three possible overlap types of two cross edges are handled explicitly. What is not established—and must not be inferred—is that an arbitrary exact-threshold host admits such a uniformly dense bipartite core containing a suitable internal edge.

## Computations To Verify

The following Python constructs \(Q_7(H)\) exactly.

```python
import itertools
import networkx as nx

def all_C7s(G):
    """Yield each undirected simple 7-cycle once as a frozenset of edges."""
    nodes = sorted(G.nodes())
    seen = set()

    for S in itertools.combinations(nodes, 7):
        root = min(S)
        rest = [v for v in S if v != root]

        for perm in itertools.permutations(rest):
            cyc = (root,) + perm

            # Quotient by reversal.
            if cyc[1] > cyc[-1]:
                continue

            edges = []
            ok = True
            for i in range(7):
                u, v = cyc[i], cyc[(i + 1) % 7]
                if not G.has_edge(u, v):
                    ok = False
                    break
                edges.append(tuple(sorted((u, v))))

            if ok:
                C = frozenset(edges)
                if C not in seen:
                    seen.add(C)
                    yield C

def conflict_graph(G):
    Q = nx.Graph()
    host_edges = [tuple(sorted(e)) for e in G.edges()]
    Q.add_nodes_from(host_edges)

    for C in all_C7s(G):
        for e, f in itertools.combinations(C, 2):
            Q.add_edge(e, f)
    return Q
```

Verification of Proposition 8:

```python
def remote_C7_graph(q):
    G = nx.Graph()

    A = [("A", i) for i in range(q)]
    B = [("B", i) for i in range(q)]
    for a in A:
        for b in B:
            G.add_edge(a, b)

    R = [("R", i) for i in range(7)]
    for i in range(7):
        G.add_edge(R[i], R[(i + 1) % 7])

    # Two paths of length 3.
    G.add_edges_from([
        (A[0], ("P", 0)), (("P", 0), ("P", 1)), (("P", 1), R[0]),
        (A[1], ("P", 2)), (("P", 2), ("P", 3)), (("P", 3), R[1]),
    ])
    return G

for q in range(4, 10):
    G = remote_C7_graph(q)
    Q = conflict_graph(G)

    R_edges = {
        tuple(sorted((("R", i), ("R", (i + 1) % 7))))
        for i in range(7)
    }

    assert nx.node_connectivity(G) >= 2
    assert all(Q.has_edge(e, f)
               for e, f in itertools.combinations(R_edges, 2))
    assert all(Q.degree(e) == 0 for e in Q if e not in R_edges)
```

Verification of the exact 2-connected construction in Proposition 9:

```python
import math

def exact_two_dense_pieces(n):
    T = (n * n) // 4 + 1
    s = n - 4
    D = 4 * (T - 6) - s * s + 2 * s

    d = s % 2
    while d * d < D:
        d += 2

    a = (s + d) // 2
    b = (s - d) // 2
    R = (d * d - D) // 4

    G = nx.Graph()
    A = [("A", i) for i in range(a)]
    B = [("B", i) for i in range(b)]
    G.add_edges_from(itertools.combinations(A, 2))
    G.add_edges_from(itertools.combinations(B, 2))

    G.add_edges_from([
        (A[0], ("P", 0)), (("P", 0), ("P", 1)), (("P", 1), B[0]),
        (A[1], ("P", 2)), (("P", 2), ("P", 3)), (("P", 3), B[1]),
    ])

    z = A[2]
    removable = [u for u in A[3:] if G.has_edge(z, u)]
    assert R <= len(removable)
    for u in removable[:R]:
        G.remove_edge(z, u)

    assert G.number_of_nodes() == n
    assert G.number_of_edges() == T
    assert nx.node_connectivity(G) >= 2
    return G

for n in range(30, 60):
    G = exact_two_dense_pieces(n)
    Q = conflict_graph(G)

    A_edges = [e for e in Q if e[0][0] == "A" and e[1][0] == "A"]
    B_edges = [e for e in Q if e[0][0] == "B" and e[1][0] == "B"]

    assert not any(Q.has_edge(e, f) for e in A_edges for f in B_edges)
```

The missing activation theorem should be attacked computationally by generating exact-threshold hosts and recording maximum-cut deficiencies:

```python
def max_cut_data(G):
    V = list(G.nodes())
    root = V[0]
    best = None

    # Feasible only for small n; fix root in A to remove complement symmetry.
    for mask in range(1 << (len(V) - 1)):
        A = {root}
        for i, v in enumerate(V[1:]):
            if (mask >> i) & 1:
                A.add(v)
        B = set(V) - A

        cross = [(u, v) for u, v in G.edges()
                 if (u in A) != (v in A)]
        if best is None or len(cross) > best[0]:
            best = (len(cross), A, B)

    cut_size, A, B = best
    internal = [(u, v) for u, v in G.edges()
                if (u in A) == (v in A)]

    deficiency = {}
    for u in A:
        deficiency[u] = len(B) - sum(G.has_edge(u, v) for v in B)
    for v in B:
        deficiency[v] = len(A) - sum(G.has_edge(v, u) for u in A)

    return cut_size, A, B, internal, deficiency
```

For each small exact-threshold host, one should compute:

1. \(\chi(Q_7(H))\);
2. its ordinary blocks and \(Q_7\)-components;
3. a maximum cut;
4. the cross deficiencies at endpoints of internal edges;
5. the largest clique supplied by Lemma 7 for each internal edge.

A particularly informative search is for hosts where:

```text
chi(Q7(H)) is small,
every internal edge has an endpoint of large cross deficiency,
and no ordinary block decomposition explains the palette reuse.
```

Such examples would either reveal the missing concentrated-deficiency configuration or suggest a counterexample template.

## Route Diagnosis

**Proved ledger**

- Exact decomposition of \(Q_7(H)\) over ordinary blocks.
- Every exact-threshold host has an ordinary block with \(n^2/8-O(n)\) edges.
- A general palette-accounting lemma for genuinely \(C_7\)-pair-linked pieces.
- Complete \(C_7\)-pair linkage under \(\delta\ge |V|/2+4\).
- The desired lower bound for clique-block hosts and analogous pair-linked block classes.
- A strong almost-complete-bipartite activation lemma.
- Explicit 2-connected counterexamples to any first-order density-plus-\(C_7\) local theorem.
- Explicit exact-threshold 2-connected hosts whose dense fixed-length linkage regions remain separated.

**Plausible but unproved**

- A maximum-cut activation theorem handling concentrated cross deficiencies.
- A decomposition into robust \(C_7\)-linkage regions with an additive second-order deficit accounting.
- A dichotomy saying that failure of the near-complete bipartite lemma forces a dense internal region whose own conflict graph already costs \(n^2/8-o(n^2)\).

**Dead ends**

- Ordinary block decomposition alone: Proposition 9 shows that one ordinary block can contain two quadratic, \(C_7\)-separated palettes.
- Any local theorem based only on \(e=v^2/4-o(v^2)\), 2-connectivity, and existence of a \(C_7\): Proposition 8 gives chromatic number \(7\).
- Regularity/removal without a second-order argument: it erases the \(O(n)\), and ultimately \(+1\), information that activates the conflict graph.
- A blanket claim that the large block from Lemma 2 has almost all edges mutually conflicting: dense bipartite cores and long fixed-length separators invalidate it.

**Recommended fresh attempt**

The most promising continuation is a hybrid of Routes 2 and 3. Choose a maximum cut \(A\cup B\). Write \(M\) for missing cross edges and \(L\) for internal edges; in the balanced near-extremal case \(L=M+1+O(1)\). Classify the endpoints of internal edges by cross deficiency. Lemma 7 settles internal edges whose endpoints lie in the uniformly good core. The remaining task is to charge internal edges incident with high-deficiency vertices against missing cross edges, while using maximality of the cut to show that concentrated bad vertices either can be switched across the cut or form a separate dense conflict-expensive region. That charging statement is exactly where the present route is blocked.