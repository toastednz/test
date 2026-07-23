STATUS: BLOCKED

## Result

The weighted-core reduction can be sharpened substantially: after fixing a Hamilton cycle, every large core weight lies on a distinguished Hamiltonian spine, while all \(h\) off-spine edges have weight \(1\). I prove rigorous rank and support constraints at every weight threshold, and an additional rank loss when many spine arcs are heavy. However, these conditions do not yield the required \(\log_* n\) correction. Indeed, I construct admissible weighted cores of excess \(h\) whose cycle spectrum contains a consecutive interval of \(2^h\) lengths, showing that any theorem depending only on the largest consecutive interval, unrestricted subset sums, or the total number of simple cycles is false. I also prove that this construction’s simple serial-diamond topology can be pancyclic only when \(n=O(h^2)\); thus the unresolved issue is precisely how arbitrary overlapping or recursively nested chord structures cover the short initial interval \(3,\dots,O(h)\).

## Complete Argument

### 1. Exact Hamiltonian weighted-core reduction

Let \(G\) be a graph on \(n\) vertices with \(n+h\) edges, and fix a Hamilton cycle \(C\). Let \(F=E(G)\setminus E(C)\), so \(|F|=h\).

Assume \(h>0\), and let \(B\) be the set of endpoints of edges in \(F\). Write \(b=|B|\). Since every chord has two endpoints,

\[
b\le 2h.
\tag{8}
\]

Compress each of the \(b\) arcs of \(C\) between consecutive vertices of \(B\) to a single edge. Give that edge weight equal to the number of original \(C\)-edges in the arc. Retain each chord as an edge of weight \(1\). Denote the resulting weighted multigraph by \(K\), and denote its distinguished cyclic collection of compressed \(C\)-arcs by \(H\).

For \(b=2\), \(H\) consists of two parallel edges; this is regarded as a multigraph \(2\)-cycle.

The construction has the following properties.

1. \(K\) has \(b\) vertices and \(b+h\) edges.
2. The \(b\) edges of \(H\) have positive integer weights \(a_1,\dots,a_b\) satisfying
   \[
   \sum_{i=1}^b a_i=n.
   \tag{9}
   \]
3. Every edge outside \(H\) has weight \(1\), and there are exactly \(h\) such edges.
4. Every vertex of \(K\) is incident with at least one off-spine edge.
5. The weighted sum of all core edges is \(n+h\).
6. The excess of the core is
   \[
   |E(K)|-|V(K)|=h.
   \]
7. Simple cycles of \(G\) correspond bijectively to connected \(2\)-regular submultigraphs of \(K\), with the original cycle length equal to the sum of the corresponding edge weights.

For the last assertion, every internal vertex of a compressed \(C\)-arc has degree \(2\) in \(G\). If a simple cycle uses one edge of that arc, degree \(2\) forces it to traverse the whole arc. Compressing all traversed arcs therefore produces a connected \(2\)-regular submultigraph of \(K\). Conversely, expanding such a core circuit gives a simple cycle of \(G\). Two parallel core edges are allowed to form a core circuit, and their expansion has length at least \(3\) because \(G\) itself is simple.

Thus Route 1 can be formulated more narrowly than in the brief:

> The only potentially large weights are the weights of a distinguished Hamiltonian spine. Every off-spine edge has weight exactly \(1\).

This additional fact is essential; arbitrary weighted multigraph cores are a much larger class than the cores arising here.

---

### 2. A rigorous multiscale rank profile

For an integer \(t\) with \(3\le t\le n+1\), let \(K_{<t}\) be the spanning subgraph of \(K\) containing:

- all \(h\) off-spine edges, each of weight \(1\);
- precisely those spine edges whose weights are less than \(t\).

Let

\[
r_t:=\#\{e\in E(H):w(e)\ge t\},
\]

let \(c_t\) be the number of connected components of \(K_{<t}\), including isolated vertices, and let

\[
\beta_t:=\dim Z_1(K_{<t};\mathbb F_2).
\]

Since \(K_{<t}\) has \(b+h-r_t\) edges and \(b\) vertices,

\[
\beta_t=h-r_t+c_t.
\tag{10}
\]

#### Lemma 1: Threshold-rank inequality

If \(G\) is pancyclic, then for every \(3\le t\le n+1\),

\[
\beta_t\ge \left\lceil \log_2(t-2)\right\rceil.
\tag{11}
\]

**Proof.**

Every cycle of weight less than \(t\) avoids every spine edge of weight at least \(t\), and hence is a circuit of \(K_{<t}\).

Pancyclicity supplies cycles of each of the \(t-3\) distinct lengths

\[
3,4,\dots,t-1.
\]

These give \(t-3\) distinct nonzero cycle-space vectors in \(K_{<t}\). Since a binary vector space of dimension \(\beta_t\) has \(2^{\beta_t}-1\) nonzero vectors,

\[
t-3\le 2^{\beta_t}-1.
\]

Thus \(t-2\le 2^{\beta_t}\), proving (11). ∎

If \(r_t\ge1\), deleting \(r_t\) edges from the spine \(H\) leaves \(r_t\) path-components. Adding chords can only merge these components, so \(c_t\le r_t\). Consequently,

\[
r_t\ge1\quad\Longrightarrow\quad \beta_t\le h.
\tag{12}
\]

In particular, if \(a_{\max}\) is the largest spine weight, then

\[
a_{\max}\le 2^h+2.
\tag{13}
\]

Indeed, apply (11) with \(t=a_{\max}\), when \(r_t\ge1\), and use (12).

#### Lemma 2: Vertex-support inequality

For \(4\le t\le n+1\),

\[
\sum_{\substack{e\in H\\w(e)\ge t}}\bigl(w(e)-1\bigr)\le n-t+1.
\tag{14}
\]

**Proof.**

A core cycle of weight \(t-1\) cannot use a spine edge of weight at least \(t\). In the original graph it therefore avoids every internal vertex of every such compressed arc.

Those internal vertex sets are pairwise disjoint. Their total cardinality is

\[
\sum_{\substack{e\in H\\w(e)\ge t}}\bigl(w(e)-1\bigr).
\]

The cycle of length \(t-1\) must fit among the remaining

\[
n-\sum_{w(e)\ge t}(w(e)-1)
\]

vertices. Hence

\[
t-1\le n-\sum_{w(e)\ge t}(w(e)-1),
\]

which is (14). ∎

For example, if \(a_{\max}\ge4\), then choosing \(t=a_{\max}\) gives

\[
a_{\max}\le \frac{n+2}{2}.
\tag{15}
\]

#### Lemma 3: Additional rank loss from many heavy arcs

If \(r_t\ge1\), then

\[
\beta_t
\le
h-
\left\lceil
\frac{\max(0,2r_t-b)}2
\right\rceil.
\tag{16}
\]

Consequently,

\[
\left\lceil\log_2(t-2)\right\rceil
\le
h-
\left\lceil
\frac{\max(0,2r_t-b)}2
\right\rceil.
\tag{17}
\]

**Proof.**

Deleting the \(r_t\) heavy spine edges divides \(H\) into \(r_t\) path-components. Contract each such component to a vertex. Every chord becomes either a loop or an edge between two contracted vertices. Let \(Q_t\) be the resulting multigraph.

Then \(Q_t\) has \(r_t\) vertices and \(c_t\) components. Set

\[
x_t:=r_t-c_t.
\]

By (10),

\[
\beta_t=h-x_t.
\tag{18}
\]

There are \(b-r_t\) light spine edges. Every nonsingleton component of the light spine contains at least one such edge, so at most \(b-r_t\) of the \(r_t\) components are nonsingletons. Therefore at least

\[
u_t:=\max(0,r_t-(b-r_t))
=\max(0,2r_t-b)
\]

contracted vertices correspond to singleton spine components.

Every core vertex is incident with a chord. A chord incident with a singleton spine component cannot become a loop in \(Q_t\), because its other endpoint is a distinct core vertex. Thus each of these \(u_t\) vertices is incident with a nonloop edge of \(Q_t\).

In a component of \(Q_t\) having \(q\ge2\) vertices, at most \(q\) vertices can be among these distinguished vertices, and

\[
q\le 2(q-1).
\]

A one-vertex component contains none of the distinguished vertices, since such a vertex would have a nonloop incident edge. Summing over components,

\[
u_t\le 2(r_t-c_t)=2x_t.
\]

Therefore

\[
x_t\ge \left\lceil\frac{u_t}{2}\right\rceil.
\]

Combining this with (18) proves (16), and (17) follows from Lemma 1. ∎

These are genuine multiscale constraints: at every threshold \(t\), sufficiently many low-weight cycles must survive in a cycle subspace of controlled rank.

They nevertheless do not recover an additional \(\log_* n\).

---

### 3. An obstruction to any “largest interval” or unrestricted subset-sum theorem

For every integer \(r\ge2\), construct a weighted core \(K_r\) with vertices

\[
v_0,v_1,\dots,v_r.
\]

Its distinguished spine \(H\) consists of:

- an edge \(e_0=v_rv_0\) of weight \(1\);
- for \(1\le i\le r\), an edge
  \[
  e_i=v_{i-1}v_i
  \]
  of weight
  \[
  w(e_i)=2^{i-1}+1.
  \]

For every \(i\), add an off-spine edge \(f_i=v_{i-1}v_i\) of weight \(1\).

Since \(w(e_i)\ge2\), expansion replaces \(e_i\) by a path of length at least \(2\), so \(f_i\) is not parallel to an original graph edge. Thus the expanded graph is simple.

There are \(r\) off-spine edges, so \(h=r\), and the order of the expansion is

\[
n=1+\sum_{i=1}^r(2^{i-1}+1)=2^r+r.
\tag{19}
\]

The core’s simple cycles are exactly of two types.

1. The \(r\) digons
   \[
   e_i\cup f_i,
   \]
   having weights
   \[
   2^{i-1}+2.
   \tag{20}
   \]

2. Cycles containing \(e_0\), which choose exactly one of \(e_i,f_i\) for every \(i\). If \(S\subseteq\{1,\dots,r\}\) is the set of indices where \(e_i\) is chosen, the weight is
   \[
   1+r+\sum_{i\in S}2^{i-1}.
   \tag{21}
   \]

The binary subset sums in (21) run through every integer from \(0\) to \(2^r-1\). Therefore the cycle spectrum contains every length in

\[
r+1,r+2,\dots,r+2^r=n.
\tag{22}
\]

This is a consecutive interval of exactly \(2^r=2^h\) lengths.

For \(r\ge5\), however, the graph has no \(5\)-cycle: the cycles in (21) have minimum length \(r+1\ge6\), while the lengths in (20) are

\[
3,4,6,10,18,\dots.
\]

Thus this family is not pancyclic once \(r\ge5\).

This establishes three important negative facts.

- A weighted Hamiltonian core of excess \(h\) can have a consecutive cycle-length interval of \(2^h\) lengths.
- The total number of simple core cycles can be
  \[
  2^h+h,
  \]
  a constant fraction of all \(2^{h+1}\) cycle-space vectors.
- Consequently, no universal estimate of the form
  \[
  \#\{\text{simple-cycle lengths}\}
  \le C\frac{2^h}{2^{\log_*L}}
  \]
  can hold when \(L\) is merely the largest represented interval.

The fact that the required interval begins at \(3\), rather than at \(h+O(1)\), is indispensable.

This family also passes the numerical rank and support conditions from the preceding section. Indeed, if \(j\) of the edges \(e_i\) have weight less than \(t\), then the unit edges \(f_1,\dots,f_r,e_0\) already form a connected cycle, and

\[
\beta_t=j+1.
\]

If \(j<r\), then \(t\le2^j+1\), so

\[
\left\lceil\log_2(t-2)\right\rceil\le j<\beta_t.
\]

If \(j=r\), then \(\beta_t=r+1\), which suffices through \(t=n+1\). Thus rank profiles alone do not detect the missing length \(5\).

---

### 4. The serial-diamond topology cannot itself be asymptotically pancyclic

The preceding binary construction suggests using independent path choices to imitate unrestricted binary subset sums. The following theorem shows that, in this simple topology, exact coverage from length \(3\) destroys the exponential growth.

#### Proposition

Let \(r\ge2\). Consider the same serial-diamond core, but give:

- the closing spine edge \(e_0\) an arbitrary weight \(a_0\ge1\);
- the spine edge \(e_i\) a weight \(a_i\ge2\);
- every parallel off-spine edge \(f_i\) weight \(1\).

If its expansion is pancyclic of order \(n\), then \(a_0\le3\), and

\[
n\le
\begin{cases}
\dfrac{r(r+1)}2+r+3,&a_0=3,\\[2mm]
r^2+4,&a_0=2,\\[2mm]
2r^2-5r+14,&a_0=1.
\end{cases}
\tag{23}
\]

In particular,

\[
n\le 2r^2+14.
\tag{24}
\]

Since this core has excess \(h=r\), it cannot provide pancyclic graphs with \(h\sim\log_2 n\).

**Proof.**

Put

\[
b_i:=a_i-1\ge1,\qquad
A:=a_0+r,\qquad
B:=\sum_{i=1}^r b_i.
\]

Then

\[
n=a_0+\sum_{i=1}^r a_i=A+B.
\tag{25}
\]

As before, all cycles are either digons or transversal cycles. Their lengths are

\[
b_i+2\qquad(1\le i\le r)
\tag{26}
\]

and

\[
A+\sum_{i\in S}b_i\qquad(S\subseteq\{1,\dots,r\}).
\tag{27}
\]

Every transversal cycle has length at least \(A\). Hence every length in

\[
3,4,\dots,A-1
\]

must be supplied by a digon. There are \(A-3=a_0+r-3\) such lengths but only \(r\) digons. Therefore

\[
a_0+r-3\le r,
\]

so

\[
a_0\le3.
\tag{28}
\]

Set

\[
e:=3-a_0\in\{0,1,2\},
\qquad
\ell:=A-3=r-e.
\]

To obtain every length from \(3\) through \(A-1\), the multiset \(\{b_i\}\) must contain every integer

\[
1,2,\dots,\ell.
\tag{29}
\]

After selecting one occurrence of each of these values, exactly \(e\) entries remain. Call them

\[
x_1\le x_2\le\cdots\le x_e.
\]

Let

\[
S_0=1+2+\cdots+\ell=\frac{\ell(\ell+1)}2.
\]

Now consider the interval \(A,\dots,n=A+B\). If an integer \(A+y\) is not represented by (27), it must be represented by a digon.

The digons associated with the forced values \(1,\dots,\ell\) have lengths at most

\[
\ell+2=A-1,
\]

so only the \(e\) remaining digons can repair missing values in \([A,n]\). Consequently, the subset sums of the \(b_i\) miss at most \(e\) integers in \([0,B]\).

Let \(S_j=S_0+x_1+\cdots+x_j\). If for some \(j\),

\[
x_j>S_{j-1}+e+1,
\]

then every integer in

\[
S_{j-1}+1,\dots,x_j-1
\]

is absent from the full subset-sum set: a sum not using \(x_j,\dots,x_e\) is at most \(S_{j-1}\), while a sum using one of them is at least \(x_j\). This interval would contain more than \(e\) missing values, a contradiction. Hence

\[
x_j\le S_{j-1}+e+1,
\]

and therefore

\[
S_j\le2S_{j-1}+e+1.
\]

Iteration gives

\[
B=S_e\le 2^eS_0+(e+1)(2^e-1).
\tag{30}
\]

There are three cases.

- If \(a_0=3\), then \(e=0\), \(\ell=r\), and
  \[
  B=\frac{r(r+1)}2.
  \]
  Hence
  \[
  n\le \frac{r(r+1)}2+r+3.
  \]

- If \(a_0=2\), then \(e=1\), \(\ell=r-1\), and (30) gives
  \[
  B\le r(r-1)+2.
  \]
  Hence
  \[
  n\le r^2+4.
  \]

- If \(a_0=1\), then \(e=2\), \(\ell=r-2\), and (30) gives
  \[
  B\le
  4\frac{(r-2)(r-1)}2+9
  =
  2(r-2)(r-1)+9.
  \]
  Hence
  \[
  n\le2r^2-5r+14.
  \]

This proves (23) and (24). ∎

The proposition rigorously identifies the lower-end obstruction in the simplest binary-choice core: almost all of the \(r\) weights must be spent producing the short lengths \(3,\dots,r+O(1)\), leaving too few generators for exponential growth.

The missing theorem would have to show that arbitrary chord arrangements cannot evade this cost through overlapping or recursively nested choices without paying approximately one additional chord at each iterated-logarithmic scale. I do not have such a theorem.

## Self-Audit

1. **The main conjecture remains unproved.**  
   The threshold inequalities do not imply any improvement over the cycle-space lower bound. The binary serial family explicitly demonstrates why: it has the correct rank profile and an exponential upper interval while missing one small length. I therefore do not infer the desired result from these lemmas.

2. **The core argument must handle multigraph \(2\)-cycles.**  
   Suppression can create parallel edges, especially when there are only two chord endpoints. The correspondence remains valid because a pair of parallel core edges expands to two internally disjoint paths forming a simple original cycle. The proofs above consistently use connected \(2\)-regular multigraph circuits, not only ordinary simple-graph cycles.

3. **The \(O(h^2)\) theorem is highly topology-specific.**  
   Its proof relies on the exact classification of cycles in a chain of parallel pairs. General chorded Hamilton cycles can contain chords spanning many blocks, so their spectra do not decompose into digons plus one subset-sum family. The proposition is rigorous in its stated class but provides no justified extrapolation to arbitrary cores.

## Computations To Verify

The following Python performs exact cycle-space enumeration for a chorded Hamilton cycle.

```python
def norm_edge(u, v):
    return (u, v) if u < v else (v, u)

def cycle_lengths(n, chords):
    """
    Exact simple-cycle lengths in C_n plus the listed chords.
    chords is a list of distinct unordered pairs.
    """
    base = [norm_edge(i, (i + 1) % n) for i in range(n)]
    base_set = set(base)

    chords = [norm_edge(*e) for e in chords]
    assert len(set(chords)) == len(chords)
    assert all(u != v and (u, v) not in base_set for u, v in chords)

    edges = base + chords
    edge_index = {e: i for i, e in enumerate(edges)}
    assert len(edge_index) == len(edges)

    Cmask = (1 << n) - 1
    basis = [Cmask]

    # Fundamental cycle of each chord using the forward cyclic arc u -> v.
    for j, (u, v) in enumerate(chords):
        mask = 1 << (n + j)
        cur = u
        while cur != v:
            nxt = (cur + 1) % n
            mask ^= 1 << edge_index[norm_edge(cur, nxt)]
            cur = nxt
        basis.append(mask)

    def is_single_simple_cycle(mask):
        if mask == 0:
            return False

        deg = [0] * n
        adj = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                deg[u] += 1
                deg[v] += 1
                adj[u].append(v)
                adj[v].append(u)

        active = [v for v in range(n) if deg[v] != 0]
        if not active or any(deg[v] != 2 for v in active):
            return False

        seen = {active[0]}
        stack = [active[0]]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)

        return len(seen) == len(active)

    lengths = set()
    for choice in range(1, 1 << len(basis)):
        mask = 0
        for i, vec in enumerate(basis):
            if (choice >> i) & 1:
                mask ^= vec
        if is_single_simple_cycle(mask):
            lengths.add(mask.bit_count())

    return lengths

def is_pancyclic(n, chords):
    return set(range(3, n + 1)) <= cycle_lengths(n, chords)
```

The weighted threshold profile can be checked directly:

```python
def weighted_profile(spine_weights, chords):
    """
    spine_weights[i] is the weight of edge i--(i+1 mod b).
    chords may contain pairs parallel to spine edges at the core level.
    """
    b = len(spine_weights)
    h = len(chords)
    n = sum(spine_weights)

    class DSU:
        def __init__(self, n):
            self.p = list(range(n))

        def find(self, x):
            while self.p[x] != x:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x

        def union(self, x, y):
            x, y = self.find(x), self.find(y)
            if x != y:
                self.p[y] = x

    result = []
    for t in range(3, n + 2):
        dsu = DSU(b)
        r = 0

        for i, a in enumerate(spine_weights):
            if a < t:
                dsu.union(i, (i + 1) % b)
            else:
                r += 1

        for u, v in chords:
            dsu.union(u, v)

        c = len({dsu.find(i) for i in range(b)})
        beta = h - r + c
        q = (t - 3).bit_length()  # ceil(log2(t-2))

        available_vertices = (
            b + sum(a - 1 for a in spine_weights if a < t)
        )

        row = {
            "t": t,
            "r": r,
            "components": c,
            "beta": beta,
            "required_rank": q,
            "available_vertices": available_vertices,
        }

        if r:
            u = max(0, 2 * r - b)
            row["singleton_rank_bound"] = h - (u + 1) // 2

        result.append(row)

    return result
```

The serial-diamond spectra and the binary obstruction are verified by:

```python
def serial_spectrum(a0, a):
    """
    a0: closing spine weight
    a[i]: weight of the heavy member of the i-th parallel pair
    """
    r = len(a)
    b = [x - 1 for x in a]
    A = a0 + r
    n = a0 + sum(a)

    sums = {0}
    for x in b:
        sums = sums | {s + x for s in sums}

    transversal = {A + s for s in sums}
    digons = {x + 1 for x in a}
    return n, transversal | digons

for r in range(2, 15):
    a = [2 ** i + 1 for i in range(r)]
    n, spectrum = serial_spectrum(1, a)

    assert n == 2 ** r + r
    assert set(range(r + 1, n + 1)) <= spectrum

    if r >= 5:
        assert 5 not in spectrum
```

A bounded exhaustive check of the serial theorem is:

```python
from itertools import product

def serial_bound(r, a0):
    if a0 == 3:
        return r * (r + 1) // 2 + r + 3
    if a0 == 2:
        return r * r + 4
    if a0 == 1:
        return 2 * r * r - 5 * r + 14
    return None

def check_serial_theorem(max_r=6, max_weight=10):
    for r in range(2, max_r + 1):
        for a0 in range(1, max_weight + 1):
            for a in product(range(2, max_weight + 1), repeat=r):
                n, spectrum = serial_spectrum(a0, a)
                if set(range(3, n + 1)) <= spectrum:
                    assert a0 <= 3
                    assert n <= serial_bound(r, a0)

check_serial_theorem()
```

To verify the weighted spectra against actual simple expanded graphs:

```python
def expand_serial(a0, a):
    """
    Returns n and the chord list of the expanded serial core.
    The Hamilton cycle traverses a[0],...,a[r-1],a0 in order.
    """
    positions = [0]
    current = 0
    for length in a:
        current += length
        positions.append(current)

    n = current + a0
    chords = [
        norm_edge(positions[i], positions[i + 1])
        for i in range(len(a))
    ]
    return n, chords

for r in range(2, 11):
    a = [2 ** i + 1 for i in range(r)]
    n, chords = expand_serial(1, a)
    exact = cycle_lengths(n, chords)
    _, predicted = serial_spectrum(1, a)
    assert exact == predicted
```

## Route Diagnosis

### Proved ledger

- Exact Hamiltonian-spine reduction: all large weights lie on the compressed Hamilton cycle, and all \(h\) chords have weight \(1\).
- Threshold-rank inequality
  \[
  \beta_t\ge\lceil\log_2(t-2)\rceil.
  \]
- Vertex-support inequality for heavy spine arcs.
- Additional rank loss when more than half the spine arcs are heavy.
- An admissible excess-\(h\) family with a consecutive interval of \(2^h\) represented lengths and \(2^h+h\) simple cycles.
- A complete \(n=O(h^2)\) upper bound for pancyclic expansions of serial-diamond cores.

### Dead ends

1. **Bounding only the largest consecutive interval.**  
   The binary serial family has an interval of \(2^h\) consecutive lengths, so no growing \(2^{\log_*L}\) deficiency is possible without using that the interval starts at \(3\).

2. **Treating cycle weights as unrestricted subset sums.**  
   The same family realizes a full binary subset-sum interval. Generic additive-combinatorial interval bounds can recover only the \(\log_2n\) term.

3. **Bounding only the total number of simple cycles.**  
   The family has \(2^h+h\) simple cycles. Thus there is no universal growing multiplicative deficiency among simple cycles in a graphic cycle space.

4. **Using only the threshold cycle-space ranks.**  
   The binary family satisfies the resulting numerical rank and vertex-support inequalities while missing length \(5\).

### Precise block

What remains is a structural theorem about the **short initial end** of the spectrum. One needs to prove that if an admissible weighted Hamiltonian core uses approximately \(q\) independent choices to generate an interval of exponential size, then covering all lengths below the minimum of that interval forces a smaller recursively rich cycle-spectrum gadget, consuming at least one additional unit of excess. Iterating this statement would plausibly produce the \(\log_*n\) term.

For a serial chain of parallel pairs, the proposition above proves exactly this “low-end tax,” and in fact gives a much stronger polynomial restriction. For arbitrary chord arrangements, however, cycles can share and overlap their choices, and no justified decomposition forces the short lengths into disjoint smaller blocks. Establishing such a decomposition appears comparable in difficulty to the original problem.

A fresh attempt should study the block/SPQR decomposition of \(K-e\), where \(e\) is a suitable spine edge, while retaining two boundary spectra:

- simple terminal-to-terminal path weights;
- internal simple-cycle weights.

The required theorem must be stable under series, parallel, and genuinely \(3\)-connected compositions. Computationally, the next useful step is to enumerate small weighted cores together with these boundary signatures and determine whether extremizers are recursively series-parallel or whether \(3\)-connected pieces permit significant sharing of the low-end repair cost.