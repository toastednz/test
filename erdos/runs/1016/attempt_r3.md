STATUS: BLOCKED

## Result

Route 3 yields an exact and useful decomposition. If \(A\) is a longest chord-free arc of length \(a\), deleting its interior leaves a graph \(H\) with a Hamilton path \(B\), cycle rank \(h\), and two simultaneous spectral requirements: its block cycle spectra cover an initial interval, while the Minkowski sum of its block path-deficit spectra covers \([0,a-2]\). Moreover, in the sparse regime \(h=O(\log n)\), almost all cycle rank of \(H\) must lie in one Hamilton-path block, and that block realizes all but at most \(2^q-1\) lengths of a long initial interval, where \(q\) is the rank outside the block. I also prove that the simplest binary “series of rank-one blocks” architecture has order only \(O(h^2)\) if it is pancyclic. The route remains blocked because the dominant block need not realize an initial interval without holes, and binary path-deficit sumsets can be exponentially long even when no individual block has a nontrivial interval. A new simultaneous cycle/path fiber-deficiency theorem is needed.

## Complete Argument

### 1. Long chord-free arc decomposition

Let

\[
G=C_n\cup F,\qquad |F|=h\ge 1,
\]

be pancyclic. Let \(t\) be the number of distinct chord endpoints. Then \(t\le 2h\), and these endpoints divide \(C_n\) into \(t\) chord-free arcs.

Choose a longest such arc \(A\), with endpoints \(x,y\), and write

\[
a=|E(A)|,\qquad b=n-a.
\]

Let \(B\) be the complementary \(x\)-to-\(y\) arc of \(C_n\), so \(|E(B)|=b\). Delete the internal vertices and edges of \(A\), leaving

\[
H=B\cup F.
\]

Thus \(H\) has \(b+1\) vertices and \(b+h\) edges, and \(B\) is a Hamilton \(x\)-to-\(y\) path in \(H\). In particular,

\[
\beta(H)=|E(H)|-|V(H)|+1=h.
\tag{12}
\]

Since \(A\) is longest,

\[
a\ge \frac n t\ge \frac{n}{2h}.
\tag{13}
\]

#### Lemma 1: Exact cycle/path correspondence

Every simple cycle of \(G\) is exactly one of the following:

1. a simple cycle contained in \(H\);
2. \(A\cup P\), where \(P\) is a simple \(x\)-to-\(y\) path in \(H\).

Consequently, if \(c(X)\) denotes the number of simple cycles of a graph \(X\), and \(p_{xy}(H)\) the number of simple \(x\)-to-\(y\) paths in \(H\), then

\[
c(G)=c(H)+p_{xy}(H).
\tag{14}
\]

**Proof.**

Every internal vertex of \(A\) has degree \(2\) in \(G\). Therefore, if a simple cycle uses one edge of \(A\), degree \(2\) propagation through the internal vertices forces it to use all of \(A\). Removing \(A\) from such a cycle leaves a simple \(x\)-to-\(y\) path in \(H\). Conversely, adjoining \(A\) to any simple \(x\)-to-\(y\) path in \(H\) produces a simple cycle. The two classes are disjoint. ∎

Let

\[
\lambda=\min\{|E(P)|:P\text{ is an }x\text{-to-}y\text{ path in }H\}.
\]

Because \(B\) is such a path,

\[
1\le \lambda\le b.
\]

#### Lemma 2: Initial cycle and terminal path intervals

The following hold.

1. \(a\le b+1\).
2. \(H\) contains a cycle of every length
   \[
   3,4,\dots,a+\lambda-1.
   \tag{15}
   \]
3. \(H\) contains an \(x\)-to-\(y\) path of every length
   \[
   b+2-a,\ b+3-a,\dots,b.
   \tag{16}
   \]

Equivalently, the path deficits \(b-|P|\) include every integer in

\[
[0,a-2].
\tag{17}
\]

**Proof.**

A cycle using \(A\) has length at least \(a+\lambda\). Hence every cycle length below \(a+\lambda\) must be realized by a cycle in \(H\), proving (15).

A cycle avoiding \(A\) has at most \(|V(H)|=b+1\) vertices. Therefore every required cycle of length

\[
b+2,b+3,\dots,n
\]

must use \(A\). Removing \(A\) gives the path lengths in (16).

It remains to verify that the lower endpoint in (16) is positive. If \(a\ge b+2\), then the required cycle length \(b+2\) can neither avoid \(A\), because \(H\) has only \(b+1\) vertices, nor contain \(A\), because every such cycle has length at least \(a+1\ge b+3\). This contradicts pancyclicity. Thus \(a\le b+1\). ∎

In particular, the naive statement that the complementary endpoint-path spectrum must itself be a full interval from \(1\) to \(b\) is false; only the terminal interval (16) is forced.

---

### 2. Block decomposition of the complementary Hamilton-path graph

Decompose \(H\) into its blocks, treating each bridge as a \(K_2\)-block.

#### Lemma 3: The blocks of \(H\) form a chain

The block-cut tree of \(H\) is a path. Moreover, if its blocks in order are

\[
K_1,K_2,\dots,K_s,
\]

then \(B\cap K_i\) is a Hamilton path in \(K_i\) between its two boundary vertices, with \(x\) or \(y\) serving as a boundary vertex in an end block.

**Proof.**

A leaf block of the block-cut tree has a unique articulation vertex \(z\), unless \(H\) consists of one block. If a leaf block contained neither \(x\) nor \(y\), then a Hamilton \(x\)-to-\(y\) path would have to enter the vertices of that block through \(z\) and leave again through \(z\), repeating \(z\), which is impossible.

Also, \(x\) and \(y\) are not cut vertices: deleting \(x\), respectively \(y\), leaves the remaining vertices connected by the corresponding subpath of \(B\). Thus at most two leaf blocks are possible. A finite tree with at most two leaves is a path.

The Hamilton path cannot leave a block and later return to it without repeating the separating articulation vertex. Hence its intersection with each block is one contiguous boundary-to-boundary segment containing every vertex of that block. ∎

Let the cyclic blocks be \(K_1,\dots,K_s\), omitting bridge blocks from the notation when convenient. Write

\[
r_i=\beta(K_i)\ge1.
\]

Since cycle spaces split over blocks,

\[
\sum_{i=1}^s r_i=h.
\tag{18}
\]

Let:

- \(c_i\) be the number of simple cycles in \(K_i\);
- \(p_i\) be the number of simple paths in \(K_i\) between its boundary vertices.

Fix the boundary Hamilton path \(B_i=B\cap K_i\).

Every boundary path \(P\) maps injectively to the cycle-space vector

\[
E(P)\mathbin{\triangle}E(B_i).
\]

Therefore

\[
p_i\le 2^{r_i}.
\tag{19}
\]

Every simple cycle is a distinct nonzero cycle-space vector, so

\[
c_i\le 2^{r_i}-1.
\tag{20}
\]

Since an \(x\)-to-\(y\) path independently chooses a boundary path in each block, while every simple cycle lies in one block,

\[
p_{xy}(H)=\prod_{i=1}^s p_i,
\qquad
c(H)=\sum_{i=1}^s c_i.
\tag{21}
\]

Combining (14), (19), and (20) gives the structural cycle bound

\[
n-2
\le c(G)
\le
2^h+\sum_{i=1}^s(2^{r_i}-1).
\tag{22}
\]

This is stronger than raw \(2^{h+1}-1\) counting whenever the rank of \(H\) is distributed over multiple blocks.

---

### 3. Exact boundary-signature formulation

For each block \(K_i\), let

\[
\mathcal P_i=
\{\text{lengths of simple boundary-to-boundary paths in }K_i\}.
\]

Since \(B_i\) is Hamilton in \(K_i\), write

\[
\ell_i=|E(B_i)|=|V(K_i)|-1
\]

and define the nonnegative deficit set

\[
D_i=\{\ell_i-p:p\in\mathcal P_i\}.
\]

The global path spectrum is the Minkowski sum of the block path spectra. Therefore the global deficit spectrum is

\[
D_1+\cdots+D_s.
\]

Lemma 2 now gives the exact necessary condition

\[
[0,a-2]\subseteq D_1+\cdots+D_s.
\tag{23}
\]

Let \(\mathcal C_i\) be the set of cycle lengths in \(K_i\). Since every cycle in \(H\) lies in one block, Lemma 2 also gives

\[
[3,a+\lambda-1]
\subseteq
\mathcal C_1\cup\cdots\cup\mathcal C_s.
\tag{24}
\]

Thus Route 3 reduces the problem to simultaneous conditions of two different additive types:

- a long interval in a Minkowski sum of path-deficit sets;
- a long interval in a union of cycle spectra.

Cardinality alone gives only

\[
a-1\le \prod_i p_i\le 2^h
\tag{25}
\]

and

\[
a+\lambda-3
\le
\sum_i c_i
\le
\sum_i(2^{r_i}-1).
\tag{26}
\]

Neither reaches the required iterated-logarithmic loss.

---

### 4. Concentration in one dominant block

Although (26) does not solve the problem, it forces a strong structural concentration.

Let

\[
R=\max_i r_i.
\]

For \(1\le r\le R\), the sequence \((2^r-1)/r\) is increasing, hence

\[
\sum_i(2^{r_i}-1)
\le
\frac{h}{R}(2^R-1)
\le
\frac{h}{R}2^R.
\tag{27}
\]

By (13) and (26),

\[
\frac{n}{2h}-2
\le a-2
\le \frac{h}{R}2^R.
\tag{28}
\]

If \(n\ge 8h\), this gives

\[
2^R\ge \frac{nR}{4h^2},
\]

and consequently

\[
R\ge \log_2 n-2\log_2 h+\log_2R-2.
\tag{29}
\]

In the only regime relevant to the conjecture, namely

\[
h\le 2\log_2 n,
\]

equation (29) first implies \(R\ge \tfrac12\log_2n\) for all sufficiently large \(n\). Hence \(R/h\ge1/4\), so

\[
\log_2R\ge\log_2h-2.
\]

Substitution into (29) yields:

#### Proposition 4: Dominant-block rank

For all sufficiently large \(n\), if \(h\le2\log_2n\), then \(H\) has a cyclic block of rank

\[
R\ge \log_2n-\log_2h-4.
\tag{30}
\]

Let

\[
q=h-R
\]

be the total cycle rank outside a selected dominant block \(K_*\). Then

\[
q\le h-\log_2n+\log_2h+4.
\tag{31}
\]

The cycles outside \(K_*\) number at most

\[
\sum_{i\ne *}(2^{r_i}-1)\le2^q-1.
\tag{32}
\]

Indeed, repeatedly applying

\[
(2^u-1)+(2^v-1)\le2^{u+v}-1
\]

proves (32).

Let

\[
N=a+\lambda-3,
\]

the number of required lengths in (24). At most \(2^q-1\) of those lengths can be absent from the cycle spectrum of \(K_*\). Therefore \(K_*\) realizes a consecutive run of cycle lengths of size at least

\[
\left\lceil
\frac{N-(2^q-1)}{2^q}
\right\rceil
\ge
\frac{N}{2^q}-1.
\tag{33}
\]

Thus a hypothetical near-counterexample necessarily contains a single Hamilton-path block of almost full rank realizing a long consecutive interval.

For example, put

\[
s=h-\log_2n.
\]

From (31),

\[
2^q\le16h\,2^s.
\]

Since \(N\ge a-2\ge n/(4h)\) for sufficiently large \(n\), (33) gives a run of at least

\[
\frac{n}{64h^2\,2^s}-1
\tag{34}
\]

consecutive cycle lengths inside a block of rank \(h-q\).

This is a genuine recursive concentration statement, but the interval in (34) need not begin at \(3\), and the block need not contain a distinguished closing edge that turns its Hamilton path into a Hamilton cycle.

---

### 5. Why a simple path-spectrum recursion is false

Consider a Hamilton path \(H_d\) built from \(d\) rank-one blocks in series. In block \(i\), join consecutive articulation vertices \(z_{i-1},z_i\) by:

- a path of length \(w_i+1\);
- a shortcut chord \(z_{i-1}z_i\).

Take

\[
w_i=2^{i-1}.
\]

Every \(z_0\)-to-\(z_d\) path independently chooses the shortcut or the long branch in each block. Hence its length is

\[
d+\sum_{i\in S}w_i
\]

for some \(S\subseteq[d]\). The endpoint-path spectrum is therefore the complete interval

\[
[d,d+2^d-1].
\tag{35}
\]

Nevertheless, each block has only one cycle, of length

\[
w_i+2=2^{i-1}+2.
\tag{36}
\]

Thus no individual block has a substantial path interval, and the union of cycle spectra is extremely sparse. This disproves any proposed lemma asserting that a long endpoint-path interval must descend to a long interval in one factor.

---

### 6. The pure binary series architecture cannot be asymptotically pancyclic

The preceding example can be closed by an internally disjoint \(z_0\)-to-\(z_d\) path \(A\) of length \(a_0\), producing a Hamilton cycle with \(d\) shortcut chords. The following restricted theorem shows that this architecture cannot disprove the conjecture.

#### Proposition 5: Polynomial bound for a series of rank-one blocks

Suppose \(G\) consists of:

- an \(x\)-to-\(y\) path \(A\) of length \(a_0\);
- a chain of \(d\) blocks, where block \(i\) consists of an \(x_i\)-to-\(x_{i+1}\) path of length \(w_i+1\) and the shortcut edge \(x_ix_{i+1}\).

Assume the resulting graph is simple and pancyclic. Then

\[
a_0\le3
\]

and

\[
n\le 2d^2+6d+6.
\tag{37}
\]

**Proof.**

The cycles are exactly:

1. the \(d\) local block cycles, of lengths \(w_i+2\);
2. \(A\) together with a chain path, of length
   \[
   a_0+d+\sum_{i\in S}w_i
   \]
   for some \(S\subseteq[d]\).

The second family has minimum length \(a_0+d\). Hence all lengths

\[
3,4,\dots,a_0+d-1
\]

must be supplied by the \(d\) local cycles. There are \(a_0+d-3\) such lengths, so

\[
a_0+d-3\le d,
\]

which proves \(a_0\le3\).

Moreover, the weights must contain every integer

\[
1,2,\dots,T,\qquad T=a_0+d-3.
\tag{38}
\]

Let

\[
W=\sum_{i=1}^d w_i,
\qquad
S_0=1+2+\cdots+T=\frac{T(T+1)}2.
\]

The number of weights not prescribed by (38) is

\[
f=d-T=3-a_0\le2.
\tag{39}
\]

For each \(t\in[0,W]\), the target cycle length \(a_0+d+t\) must be realized. If \(t\) is not a subset sum of the \(w_i\), that length must be one of the \(d\) local cycle lengths. Thus at most \(d\) integers in \([0,W]\) can fail to be subset sums.

Order the weights as \(v_1\le\cdots\le v_d\), and put \(S_{j-1}=v_1+\cdots+v_{j-1}\). If

\[
v_j>S_{j-1}+d+1,
\]

then every integer in

\[
[S_{j-1}+1,v_j-1]
\]

is missing from the subset-sum set: it is too large to use only earlier weights and too small to use \(v_j\) or any later weight. This would produce more than \(d\) missing integers. Therefore

\[
v_j\le S_{j-1}+d+1
\tag{40}
\]

for every \(j\).

The prescribed weights have total \(S_0\). There are at most two free weights. Applying (40) to them in their sorted order gives

\[
W\le 4S_0+3d+3.
\]

Since \(T\le d\),

\[
S_0\le\frac{d(d+1)}2,
\]

and hence

\[
W\le2d^2+5d+3.
\]

Finally,

\[
n=a_0+d+W\le2d^2+6d+6.
\]

∎

For comparison, the binary choices \(w_i=2^{i-1}\) happen to produce pancyclic graphs for \(d=3\) and \(d=4\), of orders \(11\) and \(20\), respectively. For \(d\ge5\), the gap below the large-cycle interval appears: for example, length \(5\) is already missing when \(d=5\).

This proposition rigorously eliminates the most direct attempt to remove the recursive “level tax,” but only in a restricted block architecture.

## Self-Audit

1. **The dominant-block argument does not iterate to the desired bound.**  
   Proposition 4 is rigorous, but the dominant block may miss \(2^q-1\) strategically placed lengths, and the consecutive run extracted in (33) may begin far above \(3\). I do not claim that it yields the conjecture; this is precisely the block.

2. **The block-chain factorization depends critically on the Hamilton path \(B\).**  
   The conclusion would be false for an arbitrary connected graph. Here it holds because a leaf block not containing \(x\) or \(y\) could not be visited by a simple Hamilton \(x\)-to-\(y\) path, forcing the block-cut tree to be a path. The proof above addresses endpoint and cut-vertex cases.

3. **Proposition 5 concerns only rank-one blocks in series.**  
   Higher-rank blocks can simultaneously have exponentially many boundary paths and many cycles, so the polynomial conclusion cannot be generalized without a new theorem. The restricted statement itself is sound because all cycles in that architecture are explicitly classified.

## Computations To Verify

The following Python-style code enumerates all cycle-space vectors of the complementary graph \(H\) for a selected chord-free arc. It verifies the exact cycle/path decomposition and the forced intervals.

```python
from itertools import combinations

def norm_edge(u, v):
    return (u, v) if u < v else (v, u)

def connected_on_incident(edges):
    if not edges:
        return False
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    start = next(iter(adj))
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(adj)

def is_cycle(edges):
    if not edges or not connected_on_incident(edges):
        return False
    deg = {}
    for u, v in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    return all(d == 2 for d in deg.values())

def is_xy_path(edges, x, y):
    if not edges or not connected_on_incident(edges):
        return False
    deg = {}
    for u, v in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    if deg.get(x, 0) != 1 or deg.get(y, 0) != 1:
        return False
    return all(
        v in (x, y) or d == 2
        for v, d in deg.items()
    )

def forward_vertices(n, u, v):
    """u,u+1,...,v cyclically."""
    out = [u]
    while out[-1] != v:
        out.append((out[-1] + 1) % n)
    return out

def complementary_spectra(n, chords, x, y):
    """
    A is the forward cycle arc x,...,y.
    B is the complementary forward arc y,...,x.
    """
    chords = {norm_edge(*e) for e in chords}
    Averts = forward_vertices(n, x, y)
    Bverts = forward_vertices(n, y, x)
    a = len(Averts) - 1
    b = len(Bverts) - 1

    Bedges = {
        norm_edge(Bverts[i], Bverts[i+1])
        for i in range(b)
    }
    Hedges = sorted(Bedges | chords)
    idx = {e: i for i, e in enumerate(Hedges)}

    Bmask = 0
    for e in Bedges:
        Bmask ^= 1 << idx[e]

    pos = {v: i for i, v in enumerate(Bverts)}
    basis = []
    for u, v in sorted(chords):
        i, j = sorted((pos[u], pos[v]))
        mask = 1 << idx[norm_edge(u, v)]
        for k in range(i, j):
            mask ^= 1 << idx[norm_edge(Bverts[k], Bverts[k+1])]
        basis.append(mask)

    cycle_lengths_H = []
    path_lengths_H = []

    for choice in range(1 << len(basis)):
        Q = 0
        for i, z in enumerate(basis):
            if (choice >> i) & 1:
                Q ^= z

        Qedges = [
            Hedges[i] for i in range(len(Hedges))
            if (Q >> i) & 1
        ]
        if is_cycle(Qedges):
            cycle_lengths_H.append(len(Qedges))

        Pmask = Bmask ^ Q
        Pedges = [
            Hedges[i] for i in range(len(Hedges))
            if (Pmask >> i) & 1
        ]
        if is_xy_path(Pedges, x, y):
            path_lengths_H.append(len(Pedges))

    G_cycle_lengths = (
        set(cycle_lengths_H) |
        {a + p for p in path_lengths_H}
    )

    assert set(range(3, a + min(path_lengths_H))).issubset(
        set(cycle_lengths_H)
    )
    assert set(range(b + 2 - a, b + 1)).issubset(
        set(path_lengths_H)
    )

    return {
        "a": a,
        "b": b,
        "cycles_H": cycle_lengths_H,
        "paths_H": path_lengths_H,
        "cycle_lengths_G": G_cycle_lengths,
    }
```

Exhaustive small-\(n\) test:

```python
def all_chords(n):
    cycle_edges = {
        norm_edge(i, (i + 1) % n) for i in range(n)
    }
    return [
        norm_edge(i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if norm_edge(i, j) not in cycle_edges
    ]

def is_pancyclic_fixed_cycle(n, chords):
    endpoints = sorted({v for e in chords for v in e})
    if not endpoints:
        return n == 3

    all_lengths = set()
    for i, x in enumerate(endpoints):
        y = endpoints[(i + 1) % len(endpoints)]
        data = complementary_spectra(n, chords, x, y)
        all_lengths |= data["cycle_lengths_G"]
        break  # one arc already enumerates every cycle of G

    return set(range(3, n + 1)).issubset(all_lengths)

for n in range(3, 13):
    possible = all_chords(n)
    for h in range(0, 6):
        witnesses = []
        for F in combinations(possible, h):
            if is_pancyclic_fixed_cycle(n, F):
                witnesses.append(F)
                break
        if witnesses:
            print("h(", n, ") <=", h, witnesses[0])
            break
```

The rank-one series examples can be checked without graph search:

```python
def series_cycle_lengths(a0, weights):
    d = len(weights)
    path_lengths = set()
    for mask in range(1 << d):
        extra = sum(
            weights[i] for i in range(d)
            if (mask >> i) & 1
        )
        path_lengths.add(d + extra)

    local = {w + 2 for w in weights}
    all_cycles = local | {a0 + p for p in path_lengths}
    n = a0 + d + sum(weights)
    return n, all_cycles

for d in range(2, 9):
    weights = [1 << i for i in range(d)]
    n, lengths = series_cycle_lengths(1, weights)
    missing = sorted(set(range(3, n + 1)) - lengths)
    print(d, n, missing[:20])
# Expected: d=3 and d=4 have no missing lengths;
# d=5 already misses length 5.
```

A particularly useful exhaustive experiment would record, for every optimized chord set:

1. all longest chord-free arcs;
2. the cyclic block ranks \(r_i\) after deleting each such arc;
3. the dominant rank \(R\) and outside rank \(q\);
4. the missing lengths of the dominant block in \([3,a+\lambda-1]\);
5. each block deficit set \(D_i\);
6. whether the forced interval \([0,a-2]\) arises from binary-like two-point factors.

## Route Diagnosis

### Proved ledger

- Exact cycle decomposition
  \[
  \{\text{cycles of }G\}
  =
  \{\text{cycles of }H\}
  \sqcup
  \{A\cup P:P\text{ an }x\text{-}y\text{ path in }H\}.
  \]
- Longest arc bound
  \[
  \frac{n}{2h}\le a\le\frac{n+1}{2}.
  \]
- Forced initial cycle interval and terminal path interval:
  \[
  [3,a+\lambda-1]\subseteq\operatorname{Spec}_{\rm cyc}(H),
  \qquad
  [0,a-2]\subseteq\operatorname{Def}_{xy}(H).
  \]
- The blocks of \(H\) form a chain and give the exact union/Minkowski-sum signature conditions (23)–(24).
- Dominant-block concentration:
  \[
  R\ge\log_2n-\log_2h-O(1)
  \]
  in the sparse regime.
- A dominant block of outside rank \(q\) misses at most \(2^q-1\) lengths from the forced initial interval.
- Pure rank-one series constructions have only \(O(h^2)\) vertices if pancyclic.

### Plausible but unproved claim needed next

A sufficient next theorem would be a quantitative simultaneous-deficiency statement for a Hamilton-path block \(K\): if its cycle spectrum covers almost all of a long interval and its boundary path-deficit spectrum participates in a long exact sumset interval, then the number of usable cycle-space fibers is smaller than \(2^{\beta(K)}\) by a factor that incurs at least one bit at each iterated-log scale.

No such theorem is proved here. It appears to require combining Route 3 with Route 2’s fiber pairing, rather than using path spectra alone.

### Dead ends

1. **“Deleting a longest arc leaves a pancyclic graph.”** False.  
   In \(C_6+\{02,04\}\), all three endpoint gaps have length \(2\). Deleting the interior of the arc \(2,3,4\) leaves only the two triangles \(0,1,2,0\) and \(0,5,4,0\), not a pancyclic graph on five vertices.

2. **“The complementary endpoint-path spectrum is an interval.”** False beyond the forced terminal interval.  
   In the same graph, deleting the interior of the arc \(0,1,2\) gives endpoint-path lengths \(\{1,3,4\}\).

3. **“A long interval in a block-path sumset forces a long interval in one block.”** False.  
   The binary rank-one chain has path spectrum (35), while every factor has only two path lengths.

4. **Cardinality optimization alone.** Insufficient.  
   The abstract bounds permit one block of rank about \(h-\log h\) to carry exponentially many cycles and paths while the remaining \(O(\log h)\) rank supplies scale transitions. Excluding simultaneous near-saturation inside that block is essentially the unresolved heart of the problem.

A fresh attempt should retain the exact boundary signatures but analyze the same cycle-space vector simultaneously as a block cycle and as the symmetric difference of a boundary path with the Hamilton path. The dominant-block reduction shows where such a fiber theorem must be applied; Route 3 alone does not currently provide it.