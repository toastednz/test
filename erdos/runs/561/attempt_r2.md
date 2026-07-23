STATUS: BLOCKED

## Result

I did not prove the conjectured lower bound \(\widehat R(F_1,F_2)\ge L\). Pursuing Route B yields an exact Hall-type characterization once the centers are fixed, but allowing the centers to vary introduces an essential center-versus-leaf conflict that destroys the natural matching/LP formulation. I prove the fixed-center theorem, a universal lower bound \(\widehat R(F_1,F_2)\ge \sum_i n_i+\sum_jm_j-1\), and a useful family of deficiency certificates with a corresponding coloring lemma. I also give explicit counterexamples to three tempting continuations: the natural fractional star-packing relaxation, a simple deficiency-allocation proof of the full threshold, and a maximal-coloring/pivotal-edge argument.

## Complete Argument

### 1. The unconditional upper bound

For completeness, define
\[
H^\star=\bigsqcup_{k=2}^{s+t}K_{1,l_k},
\qquad
l_k=\max_{i+j=k}(n_i+m_j-1).
\]
Then
\[
|E(H^\star)|=\sum_{k=2}^{s+t}l_k=L.
\]

Consider an arbitrary red-blue coloring of \(H^\star\). Start with \(i=j=1\). When considering the unused component \(K_{1,l_{i+j}}\), let \(r\) and \(b\) be its numbers of red and blue edges.

If \(r\ge n_i\), select a red \(K_{1,n_i}\) in this component and increment \(i\). Otherwise \(r\le n_i-1\), and hence
\[
b=l_{i+j}-r
 \ge l_{i+j}-(n_i-1)
 \ge m_j.
\]
Select a blue \(K_{1,m_j}\) and increment \(j\).

Each step increments \(i+j\), so a different component of \(H^\star\) is used. After at most \(s+t-1\) steps, either \(i=s+1\), yielding all components of a red \(F_1\), or \(j=t+1\), yielding a blue \(F_2\). The selected stars are vertex-disjoint because the components of \(H^\star\) are.

Thus
\[
\widehat R(F_1,F_2)\le L.
\]

### 2. A universal edge-count lower bound

Set
\[
A=\sum_{i=1}^s n_i,\qquad B=\sum_{j=1}^t m_j.
\]

#### Proposition 2.1
For all star forests in the problem,
\[
\widehat R(F_1,F_2)\ge A+B-1.
\]

#### Proof

Let \(H\) have \(q\le A+B-2\) edges. Choose an integer \(r\) satisfying
\[
\max\{0,q-(B-1)\}\le r\le \min\{q,A-1\}.
\]
Such an integer exists because \(q\le A+B-2\).

Color exactly \(r\) arbitrary edges red and all remaining edges blue. The red graph has at most \(A-1\) edges, whereas every copy of \(F_1\) uses exactly \(A\) distinct edges. Therefore it contains no red \(F_1\). Similarly, the blue graph has at most \(B-1\) edges and contains no blue \(F_2\).

Thus every graph with at most \(A+B-2\) edges has an avoiding coloring. ∎

This bound is consistent with the proposed value because \(L\ge A+B-1\). Indeed, on antidiagonals \(k=2,\ldots,s+1\), choose \((i,j)=(k-1,1)\), and on the remaining antidiagonals choose \((i,j)=(s,k-s)\). Then
\[
\begin{aligned}
L
&\ge
\sum_{i=1}^s(n_i+m_1-1)
+
\sum_{j=2}^t(n_s+m_j-1)\\
&=
A+B-1+(s-1)(m_1-1)+(t-1)(n_s-1)\\
&\ge A+B-1.
\end{aligned}
\]

### 3. Exact min-max theorem when the centers are fixed

Let \(G\) be a graph, let \(c_1,\ldots,c_r\) be distinct proposed centers, and let \(a_1,\ldots,a_r\) be positive leaf demands. Put
\[
C=\{c_1,\ldots,c_r\},
\qquad
W_i=N_G(c_i)\setminus C.
\]

#### Theorem 3.1: Fixed-center capacitated Hall theorem

There are pairwise vertex-disjoint stars centered respectively at \(c_i\), with \(a_i\) leaves at \(c_i\), if and only if
\[
\left|\bigcup_{i\in I}W_i\right|
\ge \sum_{i\in I}a_i
\qquad\text{for every }I\subseteq[r].
\tag{3.1}
\]

#### Proof

Necessity is immediate: the stars indexed by \(I\) require \(\sum_{i\in I}a_i\) distinct leaves, all lying in \(\bigcup_{i\in I}W_i\).

For sufficiency, replace each index \(i\) by \(a_i\) clones
\[
(i,1),\ldots,(i,a_i),
\]
each adjacent in an auxiliary bipartite graph to all vertices of \(W_i\).

We verify Hall’s condition for every set \(Q\) of clones. Let \(I\) be the set of indices represented among the clones of \(Q\). Then
\[
|Q|\le \sum_{i\in I}a_i
\le \left|\bigcup_{i\in I}W_i\right|
=|N(Q)|.
\]
Hall’s theorem therefore gives a matching covering all clones. The vertices matched to the \(a_i\) clones of index \(i\) are \(a_i\) distinct leaves adjacent to \(c_i\). No selected leaf is a center because every \(W_i\) excludes \(C\). ∎

Consequently, for variable centers one has the exact characterization
\[
G\supseteq \bigsqcup_{i=1}^rK_{1,a_i}
\]
if and only if there exist distinct \(c_1,\ldots,c_r\) such that (3.1) holds for every \(I\subseteq[r]\).

Equivalently, noncontainment has the alternating-quantifier form
\[
\forall(c_1,\ldots,c_r)\text{ distinct},\quad
\exists I\subseteq[r]:
\left|\bigcup_{i\in I}
  \bigl(N(c_i)\setminus\{c_1,\ldots,c_r\}\bigr)\right|
<
\sum_{i\in I}a_i.
\tag{3.2}
\]

This is exact, including when some \(a_i=1\): in a selected \(K_{1,1}\), either endpoint may be designated as its center.

### 4. Why varying the centers breaks the natural matching formulation

One can represent \(G\) by a bipartite graph with a center-copy \(v_C\) and a leaf-copy \(v_L\) of every vertex \(v\), placing an edge \(v_Cu_L\) whenever \(vu\in E(G)\).

The fixed-center problem is then a bipartite \(b\)-matching problem after deleting the leaf-copies of selected centers. With variable centers, however, one must impose the conflict condition
\[
v_C\text{ selected as a center}
\quad\Longrightarrow\quad
v_L\text{ cannot be used as a leaf}.
\tag{4.1}
\]

Condition (4.1) is indispensable. For example, let \(G=K_3\) on vertices \(a,b,c\), and seek \(2K_{1,1}\). If (4.1) is omitted, the auxiliary bipartite graph permits the two assignments
\[
a_Cb_L,\qquad b_Cc_L.
\]
The center-copies and leaf-copies are separately distinct, but the original vertex \(b\) has been used twice. The triangle contains no matching of size two, hence no \(2K_{1,1}\).

Thus a direct bipartite-flow formulation does not solve the variable-center problem.

### 5. The natural complete-star LP has an integrality gap

For each demand \(a_i\), let \(\mathcal S_i\) be the collection of all stars
\[
S=(c,L),\qquad L\subseteq N(c),\quad |L|=a_i,
\]
and write \(V(S)=\{c\}\cup L\).

The exact integer formulation has variables \(x_{i,S}\in\{0,1\}\) and constraints
\[
\sum_{S\in\mathcal S_i}x_{i,S}=1
\qquad (i=1,\ldots,r),
\tag{5.1}
\]
and
\[
\sum_i\sum_{\substack{S\in\mathcal S_i\\v\in V(S)}}x_{i,S}\le1
\qquad(v\in V(G)).
\tag{5.2}
\]
This integer program is feasible exactly when \(G\) contains the prescribed star forest.

Relaxing \(x_{i,S}\in\{0,1\}\) to \(x_{i,S}\ge0\) is not exact.

#### Proposition 5.1

Let
\[
G=C_4\sqcup C_5.
\]
The natural fractional packing LP admits a packing of three copies of \(K_{1,2}\), while \(G\) contains at most two vertex-disjoint copies of \(K_{1,2}\).

#### Proof

In each cycle, every vertex \(v\) defines the star consisting of \(v\) and its two cycle-neighbors. There are \(4+5=9\) such stars. Every graph vertex belongs to exactly three of them: the star centered at itself and those centered at its two neighbors.

For three labeled demands, set
\[
x_{i,S}=\frac19
\]
for every label \(i\in\{1,2,3\}\) and every one of the nine stars \(S\). For each label,
\[
\sum_Sx_{i,S}=9\cdot\frac19=1.
\]
For every graph vertex \(v\), its total load is
\[
3\text{ labels}\times 3\text{ containing stars}\times\frac19=1.
\]
Thus the fractional LP is feasible.

Every \(K_{1,2}\) uses three vertices and lies wholly inside one connected component. Since \(C_4\) and \(C_5\) each have fewer than six vertices, each contains at most one member of a vertex-disjoint \(K_{1,2}\)-packing. Hence the integral packing number is at most two. It is exactly two by selecting one star in each component. ∎

In the corresponding unlabeled maximum-packing LP, the fractional optimum is exactly \(3\): the construction gives \(3\), while summing all vertex-capacity constraints gives
\[
3\sum_Sx_S\le9.
\]
The integral optimum is \(2\).

Therefore the most immediate LP-duality continuation of the fixed-center Hall theorem cannot prove the conjecture.

### 6. An edge-deficiency obstruction that remains valid with variable centers

Although it is not exact, the following certificate is universal.

For a sorted demand list \(a_1\ge\cdots\ge a_r\), define
\[
A_h=\sum_{i=h+1}^r a_i
\qquad(0\le h<r).
\]

#### Lemma 6.1

If \(G\) contains
\[
\bigsqcup_{i=1}^rK_{1,a_i},
\]
then for every \(X\subseteq V(G)\) with \(|X|=h<r\),
\[
e(G-X)\ge A_h.
\tag{6.1}
\]

#### Proof

Because the selected star components are vertex-disjoint, at most \(h\) of them can meet \(X\). Thus at least \(r-h\) selected components lie wholly in \(G-X\).

Any \(r-h\) of the demands have total at least the sum of the \(r-h\) smallest demands, namely
\[
a_{h+1}+\cdots+a_r=A_h.
\]
The edges of those components are distinct edges of \(G-X\). ∎

Hence
\[
e(G-X)\le A_h-1
\tag{6.2}
\]
is a sufficient certificate that \(G\) avoids the prescribed star forest.

This produces a genuine edge-allocation lemma.

#### Corollary 6.2

Write
\[
N_a=\sum_{i=a+1}^s n_i,\qquad
M_b=\sum_{j=b+1}^t m_j.
\]
Suppose there are disjoint sets \(X,Y\subseteq V(H)\) with
\[
|X|=a<s,\qquad |Y|=b<t,
\]
such that
\[
e\bigl(H-(X\cup Y)\bigr)\le N_a+M_b-2.
\tag{6.3}
\]
Then \(H\) has an \((F_1,F_2)\)-avoiding coloring.

#### Proof

Color every edge incident with \(X\) red. Of the remaining edges, color every edge incident with \(Y\) blue.

It remains to color only the edges of \(H-(X\cup Y)\). By (6.3), these can be divided into at most \(N_a-1\) red edges and at most \(M_b-1\) blue edges.

Every red edge of \(H-X\) belongs to the red portion of \(H-(X\cup Y)\), so
\[
e(R-X)\le N_a-1.
\]
Lemma 6.1 implies that \(R\) contains no \(F_1\). Similarly,
\[
e(B-Y)\le M_b-1,
\]
so \(B\) contains no \(F_2\). ∎

### 7. The deficiency-allocation lemma does not reach \(L\)

Take
\[
F_1=F_2=2K_{1,2}.
\]
Here
\[
L=3(2+2-1)=9.
\]
Let \(H=C_8\), which has \(8=L-1\) edges.

The possible values of \(a,b\) in Corollary 6.2 are \(0\) and \(1\).

- If \(a=b=0\), the right side of (6.3) is
  \[
  4+4-2=6,
  \]
  but \(e(C_8)=8\).

- If \((a,b)=(1,0)\) or \((0,1)\), the right side is
  \[
  2+4-2=4.
  \]
  Deleting one vertex from \(C_8\) leaves six edges.

- If \(a=b=1\), the right side is
  \[
  2+2-2=2.
  \]
  Deleting two vertices from \(C_8\) removes at most four edges, so at least four remain.

Thus Corollary 6.2 cannot color this graph. Nevertheless, alternating red and blue around \(C_8\) makes both monochromatic graphs matchings. In particular, neither contains even one \(K_{1,2}\).

Therefore edge-count deficiencies after deleting proposed exceptional vertices are too coarse for the full lower bound.

### 8. A maximal-coloring/pivotal-edge continuation also fails

A tempting alternative is to choose an inclusion-maximal red \(F_1\)-free edge set \(R\). If its blue complement contains \(F_2\), every blue edge is individually pivotal for creating a red \(F_1\). One might hope to count these witnesses and recover \(L\). This is false.

Again take
\[
F_1=F_2=2K_{1,2},\qquad L=9.
\]
Let \(H\) have red edges
\[
ab,\ ac,\ de
\]
and blue edges
\[
dx,\ dy,\ ez,\ ew.
\]
The red graph has one \(K_{1,2}\), centered at \(a\), and one isolated edge \(de\), so it has no \(2K_{1,2}\). The blue graph contains two disjoint stars:
\[
d\text{ with leaves }x,y,
\qquad
e\text{ with leaves }z,w.
\]

Every blue edge is red-pivotal:

- Adding \(dx\) or \(dy\) to red makes a second red \(K_{1,2}\), centered at \(d\), using \(de\).
- Adding \(ez\) or \(ew\) makes a second red \(K_{1,2}\), centered at \(e\), again using \(de\).

Thus \(R\) is inclusion-maximal \(F_1\)-free, its complement contains \(F_2\), every blue edge is pivotal, but
\[
|E(H)|=7<9=L.
\]

The failure is caused by witness sharing: the same deficient red edge \(de\) supports pivotal edges belonging to two vertex-disjoint blue stars.

For reference, this host is not Ramsey. One avoiding coloring is
\[
\text{red: }ab,ac,dx,ez,
\qquad
\text{blue: }de,dy,ew.
\]
Red has only one \(K_{1,2}\), while all blue \(K_{1,2}\)'s intersect.

### 9. The antidiagonal maxima need not follow a coherent lattice path

An induction that always realizes the maximizing pair defining \(l_k\) cannot simply follow one sequence of adjacent states. For example, take
\[
(n_1,n_2,n_3)=(10,5,5),
\qquad
(m_1,m_2,m_3)=(10,6,1).
\]

On antidiagonal \(k=3\),
\[
n_1+m_2-1=15,\qquad n_2+m_1-1=14,
\]
so the unique maximizing pair is \((1,2)\).

On antidiagonal \(k=4\),
\[
n_1+m_3-1=10,\quad
n_2+m_2-1=10,\quad
n_3+m_1-1=14,
\]
so the unique maximizing pair is \((3,1)\).

The states adjacent to \((1,2)\) are \((1,3)\) and \((2,2)\), neither of which maximizes the next antidiagonal. Thus any proof that accumulates \(l_k\) along a single coherent center-deficiency path needs an additional mechanism for reconciling incompatible maximizers.

## Self-Audit

1. **The LP gap only refutes the natural fractional relaxation, not every possible min-max theorem.**  
   I do not claim otherwise. The calculation for \(C_4\sqcup C_5\) is exact, but a successful theory could add generalized blossom or role-conflict inequalities.

2. **The deficiency certificate is only sufficient for noncontainment.**  
   Lemma 6.1 and Corollary 6.2 are fully proved in their stated direction. The \(C_8\) example explicitly demonstrates that no converse, and no proof of the full conjecture from this certificate alone, is being asserted.

3. **The conclusion that Route B is blocked is a diagnosis rather than an impossibility theorem.**  
   Fixed centers are completely handled by Hall’s theorem, but the remaining quantifier over centers has not been eliminated. The explicit role-conflict and integrality-gap examples justify the diagnosis that the naive flow/LP route fails, though they do not rule out a substantially more sophisticated integral min-max theorem.

## Computations To Verify

The following code checks monochromatic star-forest containment by exact vertex-set packing.

```python
import itertools
import networkx as nx

def indexed_edges(G):
    edges = [tuple(sorted(e)) for e in G.edges()]
    edges.sort()
    return edges

def star_supports(G, demand, mask):
    """Vertex supports of K_{1,demand} using only allowed mask edges."""
    edges = indexed_edges(G)
    allowed_neighbors = {v: [] for v in G.nodes()}

    for k, (u, v) in enumerate(edges):
        if (mask >> k) & 1:
            allowed_neighbors[u].append(v)
            allowed_neighbors[v].append(u)

    ans = set()
    for center in G.nodes():
        for leaves in itertools.combinations(
                allowed_neighbors[center], demand):
            ans.add(frozenset((center,) + leaves))
    return ans

def contains_star_forest(G, demands, mask):
    candidates = [
        list(star_supports(G, q, mask))
        for q in demands
    ]

    # Search the most constrained demand first.
    order = sorted(range(len(demands)),
                   key=lambda i: len(candidates[i]))

    def search(pos, used):
        if pos == len(order):
            return True
        i = order[pos]
        for S in candidates[i]:
            if used.isdisjoint(S):
                if search(pos + 1, used | set(S)):
                    return True
        return False

    return search(0, set())

def avoiding_coloring(G, red_demands, blue_demands):
    q = G.number_of_edges()
    full = (1 << q) - 1
    for red_mask in range(1 << q):
        blue_mask = full ^ red_mask
        if (not contains_star_forest(G, red_demands, red_mask)
                and not contains_star_forest(
                    G, blue_demands, blue_mask)):
            return red_mask
    return None  # H arrows the pair
```

The fixed-center Hall theorem can be checked directly on all small graphs.

```python
def fixed_center_hall(G, centers, demands):
    C = set(centers)
    r = len(centers)

    for bits in range(1 << r):
        I = [i for i in range(r) if (bits >> i) & 1]
        union = set()
        required = 0
        for i in I:
            union |= set(G.neighbors(centers[i])) - C
            required += demands[i]
        if len(union) < required:
            return False
    return True

def fixed_center_bruteforce(G, centers, demands):
    C = set(centers)

    def search(i, used):
        if i == len(centers):
            return True
        available = set(G.neighbors(centers[i])) - C - used
        for leaves in itertools.combinations(
                available, demands[i]):
            if search(i + 1, used | set(leaves)):
                return True
        return False

    return search(0, set())

for G in nx.graph_atlas_g():
    for r in range(1, min(3, G.number_of_nodes()) + 1):
        for centers in itertools.permutations(G.nodes(), r):
            for demands in itertools.product([1, 2], repeat=r):
                assert fixed_center_hall(
                    G, centers, demands
                ) == fixed_center_bruteforce(
                    G, centers, demands
                )
```

The LP-gap example can be checked without an LP solver.

```python
G = nx.disjoint_union(nx.cycle_graph(4), nx.cycle_graph(5))
full = (1 << G.number_of_edges()) - 1
copies = list(star_supports(G, 2, full))

assert len(copies) == 9
assert all(sum(v in S for S in copies) == 3
           for v in G.nodes())

def max_disjoint(copies, pos=0, used=frozenset()):
    if pos == len(copies):
        return 0
    best = max_disjoint(copies, pos + 1, used)
    if used.isdisjoint(copies[pos]):
        best = max(
            best,
            1 + max_disjoint(
                copies, pos + 1, used | copies[pos])
        )
    return best

assert max_disjoint(copies) == 2

# Fractional value: weight 1/3 on each candidate star.
fractional_value = len(copies) / 3
assert fractional_value == 3
```

For the seed \((3,2)\) versus \((3,2)\), every fixed host with at most \(11\) edges can be checked by the `avoiding_coloring` function. An exhaustive unlabeled-graph search can use Brendan McKay’s `geng`.

```python
import subprocess

def geng_graphs(v, q):
    # Requires nauty's geng executable.
    cmd = ["geng", "-q", "-d1", str(v), f"{q}:{q}"]
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, text=False)
    for line in proc.stdout:
        yield nx.from_graph6_bytes(line.strip())
    assert proc.wait() == 0

red_demands = [3, 2]
blue_demands = [3, 2]
L = 12

for q in range(5, L):  # A host must have at least 5 edges.
    for v in range(7, 2*q + 1):
        for G in geng_graphs(v, q):
            full = (1 << q) - 1

            # Necessary all-red/all-blue containment filters.
            if not contains_star_forest(
                    G, red_demands, full):
                continue
            if not contains_star_forest(
                    G, blue_demands, full):
                continue

            mask = avoiding_coloring(
                G, red_demands, blue_demands)
            if mask is None:
                print("COUNTEREXAMPLE",
                      v, q,
                      nx.to_graph6_bytes(
                          G, header=False).strip())
                raise SystemExit

print("No counterexample found through 11 edges")
```

Because \(q\le11\), each surviving graph requires at most \(2^{11}=2048\) colorings, although unlabeled graph generation remains the expensive part.

## Route Diagnosis

**Proved ledger.**

- The canonical disjoint-star host gives \(\widehat R(F_1,F_2)\le L\).
- Universally,
  \[
  \widehat R(F_1,F_2)\ge
  \sum_i n_i+\sum_jm_j-1.
  \]
- Fixed centers admit an exact capacitated Hall characterization.
- Variable-center packing has an unavoidable center/leaf role-conflict.
- The natural complete-star LP is nonintegral, already for \(3K_{1,2}\) in \(C_4\sqcup C_5\).
- Vertex-deletion edge deficiencies give valid noncontainment certificates and Corollary 6.2.
- The \(C_8\) and seven-edge pivotal examples rigorously invalidate two proposed continuations.

**Dead ends.**

1. **Naive LP duality:** blocked by Proposition 5.1.
2. **Deleting exceptional vertices and allocating residual edges:** too coarse, as shown by \(C_8\).
3. **Maximal red coloring plus pivotal-edge counting:** witness sharing defeats the required \(L\)-count.
4. **Following antidiagonal maximizers along one state path:** maximizers can jump between nonadjacent states.

**Precise remaining block.**

Hall’s theorem converts the fixed-center problem into an integral matching problem, but the full obstruction is
\[
\forall\text{ ordered center sets }C\ \exists\text{ Hall-deficient }I.
\]
No argument was found that allocates red and blue edges so as to enforce these two alternating-quantifier systems simultaneously below \(L\). Replacing the center choice by fractional mixing is invalid, while using one coarse deficiency witness loses essential degree and neighborhood information. Establishing an integral “generalized blossom theorem” for typed star packings would itself be a major result and is presently unproved.

A fresh attempt should first run the exhaustive \((3,2)\) versus \((3,2)\) search. If no counterexample appears, the most promising theoretical direction is not the basic Hall LP but a generalized role-conflict polytope containing analogues of matching odd-set inequalities. Alternatively, a recoloring/exchange argument would need to control the kind of shared deficient component exhibited by the edge \(de\) in Section 8.