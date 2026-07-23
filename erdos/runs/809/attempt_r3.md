STATUS: BLOCKED

## Result

I did not obtain the required universal lower bound. I established four rigorous partial results relevant to Route 3: (i) an exact algebraic formulation of the palette-savings charge that must be proved; (ii) a complete classification of color classes for the balanced complete-bipartite graph plus one internal edge, including an exact computation of its \(C_7\)-conflict chromatic number; (iii) a robust version of that classification for almost-complete bipartite cores activated by one internal edge; and (iv) two sufficient linkage criteria—high minimum degree and an ordinary-block cleanup criterion. I also give an explicit infinite family showing that individual color classes can have quadratic size and that a natural universal cleanup lemma is false. The unresolved step is a global structural theorem that simultaneously handles activated near-bipartite blocks, dense nonbipartite blocks, and cycle-separated \(C_7\)-free regions while preventing different color classes from repeatedly charging the same exceptional structure.

## Complete Argument

### 1. The exact palette-savings ledger

Let the color classes have sizes \(s_1,\dots,s_r\), and let
\[
a_j=\bigl|\{i:s_i=j\}\bigr|.
\]
Then
\[
e=\sum_{j\ge1}j a_j,\qquad r=\sum_{j\ge1}a_j.
\]
Consequently,
\[
2r-e
=
\sum_{j\ge1}(2-j)a_j
=
a_1-\sum_{j\ge3}(j-2)a_j.
\]
Therefore
\[
\boxed{
r\ge \frac e2-o(n^2)
\iff
\sum_{j\ge3}(j-2)a_j\le a_1+o(n^2).
}
\]

Thus classes of size two are exactly neutral at the target constant. Every edge after the second edge in a larger color class must, globally, be charged either to a singleton color or to an \(o(n^2)\) exceptional budget.

This is the precise form that a successful Route 3 charging theorem must take. Merely bounding the number of large classes is not enough.

---

### 2. Exact classification for \(K_{a,b}\) plus one internal edge

Let \(A,B\) be disjoint sets with
\[
|A|=a\ge4,\qquad |B|=b\ge3.
\]
Let \(x,y\in A\), and let
\[
H=K_{A,B}+xy.
\]
Write \(d=xy\).

#### Proposition 2.1

For two distinct cross edges
\[
e=\alpha\beta,\qquad f=\alpha'\beta',
\quad \alpha,\alpha'\in A,\quad \beta,\beta'\in B,
\]
there is no \(C_7\) in \(H\) containing both \(e\) and \(f\) if and only if one of the following holds:

1. \(\alpha=\alpha'=x\);
2. \(\alpha=\alpha'=y\);
3. \(\{\alpha,\alpha'\}=\{x,y\}\) and \(\beta=\beta'\).

Moreover, \(d\) lies on a \(C_7\) with every cross edge.

#### Proof

Because \(K_{A,B}\) is bipartite and \(d\) is the only edge internal to either part, every odd cycle in \(H\) contains \(d\). Thus every \(C_7\) consists of \(d\) together with a simple cross-edge path of length six from \(x\) to \(y\), of the form
\[
x-B-A-B-A-B-y.
\]

If two selected cross edges are both incident with \(x\), they cannot both occur in such a path because \(x\) is an endpoint of the path and has path-degree one. The same applies to two edges incident with \(y\).

If the two edges are \(x\beta\) and \(y\beta\), then the selected edges already form the simple \(x\)-\(y\) path \(x\beta y\). They cannot both belong to a longer simple \(x\)-\(y\) path.

It remains to show that all other pairs extend to a length-six path. The following constructions cover every case; unspecified vertices are chosen distinct from all already used vertices.

- If \(e=z\beta_1\) and \(f=z\beta_2\), where \(z\in A\setminus\{x,y\}\), use
  \[
  x-\beta_1-z-\beta_2-z'-\beta_3-y.
  \]

- If \(e=z_1\beta\) and \(f=z_2\beta\), with \(z_1,z_2\in A\setminus\{x,y\}\), use
  \[
  x-\beta_1-z_1-\beta-z_2-\beta_2-y.
  \]

- If \(e=x\beta\) and \(f=z\beta\), use
  \[
  x-\beta-z-\beta_2-z'-\beta_3-y.
  \]
  The case involving \(y\) is symmetric.

- If \(e=x\beta_1\) and \(f=y\beta_2\) with \(\beta_1\ne\beta_2\), use
  \[
  x-\beta_1-z_1-\beta_3-z_2-\beta_2-y.
  \]

- If \(e=x\beta_1\) and \(f=z\beta_2\) are disjoint, use
  \[
  x-\beta_1-z'-\beta_2-z-\beta_3-y.
  \]
  Again, the case involving \(y\) is symmetric.

- If \(e=z_1\beta_1\) and \(f=z_2\beta_2\) are disjoint and neither \(z_i\) is \(x\) or \(y\), use
  \[
  x-\beta_1-z_1-\beta_3-z_2-\beta_2-y.
  \]

The hypotheses \(a\ge4\) and \(b\ge3\) guarantee all required distinct vertices.

Finally, a cross edge incident with \(x\) can be included in a path
\[
x-\beta-z_1-\beta_2-z_2-\beta_3-y.
\]
The analogous statement holds for an edge incident with \(y\). An edge \(z\beta\), where \(z\notin\{x,y\}\), lies in
\[
x-\beta_1-z-\beta-z_2-\beta_2-y.
\]
Thus \(d\) lies on a \(C_7\) with every cross edge. ∎

#### Corollary 2.2: Classification of color classes

Let \(F\subseteq E(H)\) have the property that no \(C_7\) contains two edges of \(F\). Then exactly one of the following applies:

1. \(F=\{d\}\);
2. \(F\) is contained in the cross-edge star at \(x\);
3. \(F\) is contained in the cross-edge star at \(y\);
4. \(F=\{x\beta,y\beta\}\) for some \(\beta\in B\);
5. \(F\) is a singleton.

In particular, if \(F\) contains a cross edge \(z\beta\) with \(z\in A\setminus\{x,y\}\), then \(F\) is a singleton.

#### Proof

The edge \(d\) conflicts with every cross edge, so a class containing \(d\) is \(\{d\}\).

By Proposition 2.1, an edge whose \(A\)-endpoint is outside \(\{x,y\}\) conflicts with every other distinct cross edge.

It remains to consider edges in the two stars
\[
X=\{x\beta:\beta\in B\},\qquad
Y=\{y\beta:\beta\in B\}.
\]
If \(F\) contains two distinct members \(x\beta_1,x\beta_2\), then an edge \(y\gamma\) is incompatible with both only if simultaneously \(\gamma=\beta_1\) and \(\gamma=\beta_2\), which is impossible. Hence \(F\subseteq X\). The case of two edges from \(Y\) is symmetric. If \(F\) contains at most one edge from each star, it has size at most two, and a two-edge class must be \(\{x\beta,y\beta\}\). ∎

#### Theorem 2.3: Exact conflict chromatic number

For \(a\ge4\) and \(b\ge3\),
\[
\boxed{\chi(Q_7(K_{a,b}+xy))=(a-2)b+3.}
\]

#### Proof

Let
\[
Z=\{z\beta:z\in A\setminus\{x,y\},\ \beta\in B\}.
\]
By Proposition 2.1, every two distinct edges of \(Z\) lie together on a \(C_7\). Every edge of \(Z\) also conflicts with every edge in \(X\cup Y\) and with \(d\). Hence the \((a-2)b\) edges in \(Z\), together with \(d\), require
\[
(a-2)b+1
\]
distinct colors, none reusable on \(X\cup Y\).

At least two further colors are needed for \(X\cup Y\), because \(x\beta_1\) and \(y\beta_2\) conflict whenever \(\beta_1\ne\beta_2\). Conversely, one may color all of \(X\) with one color and all of \(Y\) with another. Hence the total is
\[
(a-2)b+1+2=(a-2)b+3.
\]
∎

For balanced \(a,b\), this is \(\frac14n^2-O(n)\), much larger than the conjectured minimum \(\frac18n^2\). Thus the most obvious Turán graph plus one internal edge is very far from minimizing the number of colors.

This theorem also disproves the naive claim that every color class has size at most two: the stars at \(x\) and \(y\) have size \(b=\Theta(n)\).

---

### 3. Robust classification in an almost-complete bipartite core

The preceding classification survives \(o(n)\) missing neighbors per vertex.

Let \(K\) be a bipartite graph with parts \(A,B\), where
\[
|A|=a,\qquad |B|=b.
\]
Suppose
\[
d_K(v)\ge
\begin{cases}
b-t,&v\in A,\\
a-t,&v\in B.
\end{cases}
\]
Let \(x,y\in A\), and suppose \(xy\in E(H)\) and \(K\subseteq H\). Set
\[
B_0=N_K(x)\cap N_K(y).
\]
Then
\[
|B_0|\ge b-2t.
\]

We first record an elementary extension lemma.

#### Lemma 3.1: Extending a partially embedded alternating path

Assume
\[
\min\{a,b\}\ge2t+8.
\]
Consider the seven-vertex alternating path template
\[
A-B-A-B-A-B-A.
\]
Suppose some template positions have been injectively assigned vertices of the appropriate part, and every edge whose two endpoints are already assigned maps to an edge of \(K\). Then the assignment extends to a full injective copy of the path in \(K\).

#### Proof

Assign the remaining positions one at a time. When assigning a position, it has at most two already assigned neighbors in the template.

If it lies in \(A\), the common neighborhood in \(A\) of those zero, one, or two assigned \(B\)-vertices has size at least respectively
\[
a,\qquad a-t,\qquad a-2t.
\]
The analogous bounds hold for a position in \(B\). At most six vertices are already used. Since
\[
\min\{a,b\}-2t-6\ge2,
\]
an unused candidate always exists. Every template edge is checked when its second endpoint is assigned. ∎

#### Proposition 3.2: Robust activated-bipartite linkage

Assume \(\min\{a,b\}\ge2t+8\). Let
\[
e=\alpha\beta,\qquad f=\alpha'\beta'
\]
be distinct edges of \(K\) with \(\beta,\beta'\in B_0\). Unless one of
\[
\alpha=\alpha'=x,\qquad
\alpha=\alpha'=y,\qquad
\{\alpha,\alpha'\}=\{x,y\}\text{ and }\beta=\beta'
\]
holds, the graph \(K+xy\) contains a \(C_7\) containing both \(e\) and \(f\).

Moreover, \(xy\) lies on a \(C_7\) with every edge \(\alpha\beta\in E(K)\) having \(\beta\in B_0\).

#### Proof

Use the same path templates as in Proposition 2.1, now treating unspecified positions as unassigned. Whenever a prescribed \(B\)-vertex is placed next to \(x\) or \(y\) without that boundary edge being one of \(e,f\), it belongs to \(B_0\), so the required boundary edge is present.

For example, for two disjoint internal edges \(z_1\beta_1,z_2\beta_2\), use the partial assignment
\[
x-\beta_1-z_1-*-z_2-\beta_2-y.
\]
The edges \(x\beta_1\) and \(y\beta_2\) exist because \(\beta_1,\beta_2\in B_0\). Lemma 3.1 fills the remaining position.

The other cases use the partial templates
\[
\begin{array}{ll}
x-\beta_1-z-\beta_2-*-*-y,
&\text{for two edges sharing internal }z,\\[2mm]
x-*-z_1-\beta-z_2-*-y,
&\text{for two internal edges sharing }\beta,\\[2mm]
x-\beta-z-*-*-*-y,
&\text{for }x\beta,z\beta,\\[2mm]
x-\beta_1-*-*-*-\beta_2-y,
&\text{for }x\beta_1,y\beta_2,\ \beta_1\ne\beta_2,\\[2mm]
x-\beta_1-*-\beta_2-z-*-y,
&\text{for disjoint }x\beta_1,z\beta_2.
\end{array}
\]
The cases involving \(y\) are obtained by reversing the path.

The three listed exceptional patterns are impossible for the same endpoint-degree reasons as in Proposition 2.1.

For the final assertion, one prescribed edge can be placed in the same templates, and Lemma 3.1 fills all other positions. ∎

#### Corollary 3.3

Let
\[
Z=\{\alpha\beta\in E(K):
\alpha\in A\setminus\{x,y\},\ \beta\in B_0\}.
\]
Then \(Z\) is a clique in \(Q_7(H)\). Therefore every valid coloring of \(H\) uses at least
\[
|Z|
\ge (a-2)(|B_0|-t)
\ge (a-2)(b-3t)
\]
colors.

In particular, if \(a,b=\Theta(n)\) and \(t=o(n)\), then
\[
r\ge ab-o(n^2).
\]

#### Proof

Any two distinct edges of \(Z\) avoid all three exceptional patterns in Proposition 3.2, so they lie together on a \(C_7\).

For each \(\alpha\in A\setminus\{x,y\}\), at most \(t\) vertices of \(B_0\) fail to be adjacent to \(\alpha\). Hence
\[
d_K(\alpha,B_0)\ge |B_0|-t,
\]
and summing over the \(a-2\) choices of \(\alpha\) gives the claimed bound. ∎

Thus an almost-complete bipartite block containing even one internal edge is highly expensive in colors. This rigorously handles the most obvious stability regime, but arbitrary hosts need not contain such a near-complete bipartite core.

---

### 4. A high-minimum-degree linkage criterion

#### Proposition 4.1

Let \(G\) have \(N\) vertices and
\[
\delta(G)\ge \frac N2+5.
\]
Then every two distinct edges of \(G\) lie together on a \(C_7\). Consequently,
\[
Q_7(G)=K_{|E(G)|}.
\]

#### Proof

First suppose the two edges are adjacent, say \(uv\) and \(vw\), with \(u\ne w\). Choose an edge \(xy\) in
\[
G-\{u,v,w\}.
\]
Such an edge exists because every vertex outside this three-element set has more than three neighbors.

For any vertices \(p,q\),
\[
|N(p)\cap N(q)|
\ge d(p)+d(q)-N
\ge 2\delta(G)-N
\ge10.
\]
Choose
\[
a\in N(u)\cap N(x)
\]
outside \(\{v,w,y\}\), and then choose
\[
b\in N(y)\cap N(w)
\]
outside \(\{u,v,x,a\}\). The vertices
\[
u,v,w,b,y,x,a
\]
are distinct and form the cycle
\[
u-v-w-b-y-x-a-u.
\]

Now suppose the selected edges \(uv\) and \(xy\) are disjoint. Choose
\[
a\in N(v)\cap N(x)
\]
outside \(\{u,v,x,y\}\). Let
\[
S=\{u,v,x,y,a\}.
\]
There is an edge between \(N(y)\setminus S\) and \(N(u)\setminus S\). Otherwise, for any \(b\in N(y)\setminus S\),
\[
d(b)\le N-|N(u)\setminus S|
\le N-\delta(G)+5,
\]
which would imply
\[
2\delta(G)\le N+5,
\]
contrary to \(2\delta(G)\ge N+10\).

Choose such an edge \(bc\), where
\[
b\in N(y)\setminus S,\qquad c\in N(u)\setminus S.
\]
Then
\[
u-v-a-x-y-b-c-u
\]
is a simple \(C_7\) containing both prescribed edges. ∎

The threshold is qualitatively sharp: at minimum degree \(N/2\), a balanced complete bipartite graph has no odd cycle at all.

A useful conditional consequence is that if an arbitrary host contains a subgraph \(G\) satisfying this degree condition and
\[
|E(G)|\ge \frac{n^2}{8}-o(n^2),
\]
then the desired lower bound follows immediately. I do not know how to force such a subgraph in every admissible host.

---

### 5. The ordinary-cycle surrogate and a sharp block inequality

It is instructive to replace “common \(C_7\)” by “common cycle of arbitrary length.” In that stronger problem, the desired constant follows from ordinary block decomposition.

A block is either a maximal 2-connected subgraph or a bridge considered as a \(K_2\).

#### Lemma 5.1

Any two edges in the same 2-connected block lie on a common simple cycle.

#### Proof

Subdivide both edges once. Subdivision preserves 2-connectivity. In a 2-connected graph, any two vertices lie on a common cycle: by Menger’s theorem, there are two internally vertex-disjoint paths between them, whose union is a cycle. A cycle containing both subdivision vertices corresponds, after suppressing them, to a cycle containing both original edges. ∎

Edges in different blocks cannot lie on a common cycle. Hence if every cycle of a graph must be rainbow, the exact number of colors required is
\[
\max_B |E(B)|,
\]
where the maximum is over blocks.

The following inequality controls the largest block.

#### Proposition 5.2

Let \(G\) be an \(n\)-vertex graph with \(e>0\) edges, and let
\[
M=\max_B |E(B)|.
\]
Then
\[
\boxed{
M\ge
2\left(\frac e{n-1}\right)^2-\frac e{n-1}.
}
\]

#### Proof

For a block \(B\), put
\[
x_B=|V(B)|-1.
\]
The block-cut forest identity gives
\[
\sum_B x_B\le n-1.
\]
Also,
\[
|E(B)|\le \binom{x_B+1}{2}
=\frac{x_B(x_B+1)}2
\]
and \(|E(B)|\le M\).

Let \(x_0\ge0\) be defined by
\[
M=\frac{x_0(x_0+1)}2,
\]
and put
\[
\rho=\frac{x_0+1}{2}
=\frac{1+\sqrt{1+8M}}4.
\]
For every \(x>0\),
\[
\min\left\{M,\frac{x(x+1)}2\right\}\le \rho x.
\]
Indeed, if \(x\le x_0\), then
\[
\frac{x(x+1)}{2x}=\frac{x+1}{2}\le\rho;
\]
if \(x\ge x_0\), then
\[
\frac Mx\le\frac M{x_0}=\rho.
\]

Therefore
\[
e
=\sum_B |E(B)|
\le \rho\sum_B x_B
\le \rho(n-1).
\]
Writing \(q=e/(n-1)\), we have \(\rho\ge q\). Since
\[
M=2\rho^2-\rho
\]
and the right side is increasing for the relevant \(\rho\ge1/2\),
\[
M\ge2q^2-q.
\]
∎

For
\[
e=t_2(n)+1=\frac{n^2}{4}+O(1),
\]
this gives
\[
M\ge\frac{n^2}{8}-O(1).
\]

Thus the problem would be solved if “common cycle” could be replaced by “common \(C_7\)” after deleting \(o(n^2)\) edges in a suitable dominant block.

More precisely:

#### Corollary 5.3: A sufficient cleanup criterion

Suppose \(D\subseteq E(H)\), \(G=H-D\), and every two distinct edges in each block of \(G\) lie together on a \(C_7\) of \(H\). Then every valid coloring of \(H\) uses at least
\[
2\left(\frac{|E(G)|}{n-1}\right)^2
-\frac{|E(G)|}{n-1}
\]
colors.

In particular, if
\[
|D|=o(n^2)
\]
and \(|E(H)|=t_2(n)+1\), then
\[
r\ge\frac{n^2}{8}-o(n^2).
\]

#### Proof

All edges in any one block of \(G\) must receive distinct colors. Apply Proposition 5.2 to \(G\). ∎

Unfortunately, the stated cleanup criterion is false universally, as the next construction shows.

---

### 6. Obstructions to naive Route 3 classifications

#### Proposition 6.1: Quadratically large color classes are possible

For every \(u\ge2\), there is a graph \(H_u\) on \(n=6u\) vertices with
\[
|E(H_u)|=t_2(n)+1
\]
and a valid color class of size \(u^2-u=\Theta(n^2)\).

#### Construction and proof

Take two disjoint components:

1. a clique on \(4u+1\) vertices, with a matching of \(u-1\) edges deleted;
2. a complete bipartite graph \(K_{u-1,u}\).

The clique initially has
\[
\binom{4u+1}{2}=8u^2+2u
\]
edges, so after deleting the matching it has
\[
8u^2+u+1
\]
edges. The bipartite component has
\[
u(u-1)=u^2-u
\]
edges. Thus
\[
|E(H_u)|
=
8u^2+u+1+u^2-u
=
9u^2+1
=
t_2(6u)+1.
\]

Color every remaining edge in the clique component distinctly, and color all edges of \(K_{u-1,u}\) with one additional color. The bipartite component has no odd cycle, and cycles cannot traverse two components. Hence every \(C_7\) lies in the clique component, where all edge colors are distinct. The coloring is valid.

The large color class has \(u^2-u\) edges. The total number of colors is
\[
8u^2+u+2,
\]
which is much larger than \(n^2/8\); thus this is not a disproof. It does show that no universal \(O(n)\), \(O(1)\), or even \(o(n^2)\) upper bound on an individual color-class size is possible. ∎

The same construction disproves the universal cleanup criterion suggested after Corollary 5.3. If \(o(n^2)\) edges are deleted, the bipartite component still has quadratically many edges. Since no two of those edges can lie on any \(C_7\) of the original graph, every block retained in that component would have to consist of a single bridge. The retained graph would therefore be a forest and have at most \(2u-2\) edges. Consequently at least
\[
u(u-1)-(2u-2)=u^2-3u+2=\Theta(n^2)
\]
bipartite edges must be deleted.

This establishes that cycle-separated \(C_7\)-free regions must be retained and charged through their vertex and edge budgets, rather than simply discarded.

---

### 7. Precise point where Route 3 is blocked

The preceding results handle three important local configurations:

1. **Activated almost-complete bipartite regions:** one internal edge forces almost all cross edges to be pairwise \(C_7\)-conflicting.
2. **Very dense minimum-degree regions:** all edges are pairwise \(C_7\)-conflicting.
3. **Ordinary cycle-separated blocks:** palette reuse is controlled exactly by block sizes.

What remains unproved is a structural theorem covering every arbitrary \(H\) with \(t_2(n)+1\) edges. A sufficient theorem would have to decompose \(H\), up to \(o(n^2)\) exceptional edges, into pieces of the following kinds:

- \(C_7\)-free pieces, whose edge count is charged against a bipartite-type vertex budget;
- activated near-bipartite pieces, to which Proposition 3.2 applies;
- rigid nonbipartite pieces containing \(\frac{n^2}{8}-o(n^2)\) pairwise \(C_7\)-linked edges;
- sparse interfaces whose total palette savings are \(o(n^2)\).

The crucial difficulty is global: even if each large color class is separately star-like or separator-supported, different color classes may reuse the same separator. No bounded-overlap charging theorem has been proved. Establishing one appears comparable in strength to the original problem.

## Self-Audit

1. **The robust bipartite classification is only a local theorem.**  
   It requires an almost-complete bipartite core with maximum missing degree \(t=o(n)\) and an internal edge. Arbitrary threshold hosts need not have such a core. The theorem itself is rigorous: the only embedding step is Lemma 3.1, where each unassigned path position has at most two adjacency constraints and at least \(\min\{a,b\}-2t-6>0\) available vertices.

2. **The block inequality concerns arbitrary cycles, not fixed length seven.**  
   Proposition 5.2 is exact, but its direct application to the original problem needs the additional \(C_7\)-linkage hypothesis in Corollary 5.3. I believe the inequality itself is correct because it follows from the exact block-cut vertex budget and a verified one-variable optimization; I make no claim that its hypothesis can always be forced.

3. **No global charging argument has been established.**  
   This is the fatal weakness, not a technical omission. The mixed clique–bipartite construction proves that large classes and large \(C_7\)-free blocks genuinely occur. Any successful proof must account for them rather than assume them negligible. None of the proved lemmas currently prevents many medium-size classes from overlapping exceptional separators in a way that defeats the required ledger inequality.

## Computations To Verify

The following Python code verifies Proposition 2.1 for small \(a,b\), constructs conflict graphs, checks colorings, and tests the block inequality.

```python
import itertools
import math
import random
import networkx as nx

def edge(u, v):
    return tuple(sorted((u, v)))

def cycles7(G):
    """Enumerate undirected simple 7-cycles, once up to rotation/reversal."""
    nodes = sorted(G.nodes())
    out = []
    for S in itertools.combinations(nodes, 7):
        start = min(S)
        rest = [v for v in S if v != start]
        for tail in itertools.permutations(rest):
            cyc = (start,) + tail
            # Break reversal symmetry.
            if cyc[1] > cyc[-1]:
                continue
            if all(G.has_edge(cyc[i], cyc[(i + 1) % 7])
                   for i in range(7)):
                out.append(tuple(edge(cyc[i], cyc[(i + 1) % 7])
                                 for i in range(7)))
    return out

def conflict_graph(G):
    Q = nx.Graph()
    E = [edge(*e) for e in G.edges()]
    Q.add_nodes_from(E)
    for C in cycles7(G):
        for e, f in itertools.combinations(C, 2):
            Q.add_edge(e, f)
    return Q

def standard_host(a, b):
    A = list(range(a))
    B = list(range(a, a + b))
    x, y = A[0], A[1]
    G = nx.Graph()
    G.add_nodes_from(A + B)
    G.add_edges_from((u, v) for u in A for v in B)
    G.add_edge(x, y)
    return G, set(A), set(B), x, y

def cross_coordinates(e, A, B):
    u, v = e
    if u in A and v in B:
        return u, v
    if v in A and u in B:
        return v, u
    return None

def predicted_nonconflict(e, f, A, B, x, y):
    ce = cross_coordinates(e, A, B)
    cf = cross_coordinates(f, A, B)
    if ce is None or cf is None:
        return False
    ae, be = ce
    af, bf = cf
    return (
        (ae == af == x) or
        (ae == af == y) or
        ({ae, af} == {x, y} and be == bf)
    )

def check_standard_classification(a, b):
    G, A, B, x, y = standard_host(a, b)
    Q = conflict_graph(G)
    E = [edge(*e) for e in G.edges()]
    d = edge(x, y)

    for e, f in itertools.combinations(E, 2):
        actual_nonconflict = not Q.has_edge(e, f)
        if d in (e, f):
            predicted = False
        else:
            predicted = predicted_nonconflict(e, f, A, B, x, y)
        assert actual_nonconflict == predicted, (e, f, actual_nonconflict)

    expected = (a - 2) * b + 3

    # Explicit coloring with expected colors.
    colors = {}
    next_color = 0

    # Internal-A cross edges all unique.
    for e in E:
        ce = cross_coordinates(e, A, B)
        if ce is not None and ce[0] not in {x, y}:
            colors[e] = next_color
            next_color += 1

    colors[d] = next_color
    next_color += 1

    color_x = next_color
    color_y = next_color + 1
    next_color += 2

    for e in E:
        ce = cross_coordinates(e, A, B)
        if ce is not None:
            if ce[0] == x:
                colors[e] = color_x
            elif ce[0] == y:
                colors[e] = color_y

    assert len(set(colors.values())) == expected
    for e, f in itertools.combinations(E, 2):
        if colors[e] == colors[f]:
            assert not Q.has_edge(e, f)

    return expected

for a in range(4, 7):
    for b in range(3, 7):
        print(a, b, check_standard_classification(a, b))
```

A check of Proposition 4.1 on randomly generated dense graphs:

```python
def check_all_pairs_conflict(G):
    Q = conflict_graph(G)
    E = [edge(*e) for e in G.edges()]
    return all(Q.has_edge(e, f) for e, f in itertools.combinations(E, 2))

def random_dense_test(n=12, trials=20):
    # Exact cycle enumeration becomes expensive quickly.
    required = math.ceil(n / 2 + 5)
    for _ in range(trials):
        while True:
            G = nx.gnp_random_graph(n, 0.97)
            if min(dict(G.degree()).values()) >= required:
                break
        assert check_all_pairs_conflict(G)

random_dense_test()
```

The exact mixed obstruction family:

```python
def mixed_obstruction(u):
    n = 6 * u
    C = list(range(4 * u + 1))
    L = list(range(4 * u + 1, 5 * u))
    R = list(range(5 * u, 6 * u))

    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(itertools.combinations(C, 2))

    # Delete a matching of size u-1.
    for i in range(u - 1):
        G.remove_edge(C[2 * i], C[2 * i + 1])

    G.add_edges_from((x, y) for x in L for y in R)

    assert G.number_of_edges() == n * n // 4 + 1

    colors = {}
    col = 0
    for e in G.edges():
        e = edge(*e)
        if e[0] in C and e[1] in C:
            colors[e] = col
            col += 1

    bip_color = col
    for x in L:
        for y in R:
            colors[edge(x, y)] = bip_color

    # For small u, explicit verification:
    if n <= 14:
        Q = conflict_graph(G)
        E = [edge(*e) for e in G.edges()]
        for e, f in itertools.combinations(E, 2):
            if colors[e] == colors[f]:
                assert not Q.has_edge(e, f)

    assert len(set(colors.values())) == 8 * u * u + u + 2
    return G, colors
```

The block inequality can be checked on all graphs in the NetworkX graph atlas:

```python
def largest_block_edges(G):
    blocks = list(nx.biconnected_component_edges(G))
    if not blocks:
        return 0
    return max(len(list(B)) for B in blocks)

def check_block_bound(G):
    n = G.number_of_nodes()
    e = G.number_of_edges()
    if e == 0 or n <= 1:
        return True
    M = largest_block_edges(G)
    q = e / (n - 1)
    return M + 1e-9 >= 2 * q * q - q

for G in nx.graph_atlas_g():
    assert check_block_bound(G)
```

A useful computational search for Route 3 would enumerate maximal cliques in the incompatibility graph \(I_7(H)\):

```python
def maximal_color_classes(G):
    Q = conflict_graph(G)
    I = nx.complement(Q)
    return list(nx.find_cliques(I))

def summarize_classes(G):
    classes = maximal_color_classes(G)
    data = []
    for F in classes:
        endpoints = set()
        for u, v in F:
            endpoints.add(u)
            endpoints.add(v)
        data.append({
            "size": len(F),
            "support_size": len(endpoints),
            "is_star": bool(F) and
                any(all(v in e for e in F) for v in endpoints),
            "edges": F,
        })
    return sorted(data, key=lambda x: -x["size"])
```

The most informative finite search would generate 2-connected hosts with \(t_2(n)+1\) edges, exclude hosts covered by Proposition 3.2, and inspect whether maximal incompatibility cliques are still star-like or separator-supported.

## Route Diagnosis

### Proved lemmas

1. The exact savings identity
   \[
   2r-e=a_1-\sum_{j\ge3}(j-2)a_j.
   \]
2. Complete classification of pairwise \(C_7\)-incompatible edge families in \(K_{a,b}+xy\).
3. The exact formula
   \[
   \chi(Q_7(K_{a,b}+xy))=(a-2)b+3.
   \]
4. A robust extension of that classification to almost-complete bipartite cores with one internal edge.
5. If \(\delta(G)\ge |V(G)|/2+5\), every two edges of \(G\) lie on a common \(C_7\).
6. The exact ordinary-block inequality
   \[
   M\ge2\left(\frac e{n-1}\right)^2-\frac e{n-1}.
   \]
7. An explicit family showing that valid color classes can have quadratic size.

### Plausible but unproved claims

The most promising missing statement is a **dominant rigid-or-inert decomposition**: after a controlled exceptional loss, every dense block should either be \(C_7\)-free and charged by a bipartite vertex budget, or contain a set of almost all its edges in which every pair is \(C_7\)-linked. Near-bipartite blocks must include an “activation” mechanism: a single internal edge, invisible at graphon scale, can force quadratic pairwise linkage.

A weaker Route 3 formulation would be enough: every edge beyond the second edge of a color class should be chargeable, with bounded multiplicity, either to a singleton color or to a deficit from the extremal edge capacity of a cycle-separated piece. No such bounded-multiplicity charging map is known.

### Dead ends and counterexamples

1. **“Every color class is \(O(n)\)” is false.**  
   Proposition 6.1 gives classes of size \(\Theta(n^2)\).

2. **“Every color class has size at most two” is false.**  
   The complete-bipartite-plus-edge host has star classes of size \(\Theta(n)\).

3. **“Delete \(o(n^2)\) edges so every remaining block is \(C_7\)-rigid” is false.**  
   A separate dense bipartite component requires deletion of \(\Theta(n^2)\) edges.

4. **Bounding the independence number of \(Q_7(H)\) cannot work universally.**  
   The mixed construction has \(\alpha(Q_7(H))=\Theta(n^2)\) while still requiring many colors elsewhere.

5. **First-order stability or graphon arguments are insufficient.**  
   A single internal edge in an otherwise bipartite block can activate quadratic \(C_7\)-conflict, but disappears in the graphon limit.

### Recommended next attempt

The best continuation appears to combine Routes 2 and 3:

1. decompose into ordinary blocks and large 2-connected regions;
2. prove an “activated bipartite block” theorem under average, rather than maximum, missing degree;
3. prove that dense blocks not admitting such a bipartite approximation contain a \(C_7\)-rigid edge set of nearly their full edge count;
4. optimize rigid palette costs and \(C_7\)-free edge capacities using the block vertex budget;
5. explicitly track overlap of star/separator exceptions across color classes.

The present route is blocked precisely at Step 3 and at the bounded-overlap charging needed in Step 5.