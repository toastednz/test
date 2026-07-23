STATUS: BLOCKED

## Result

I did not resolve the conjecture. Pursuing the generating-function route yields an exact Walsh–Fourier representation of every cycle-space fiber together with a complete simplicity criterion. This gives a rigorous structural lower bound: if \(\tau\) chords must be deleted before the chord graph has maximum degree at most \(2\), then
\[
h\ge \log_2(n-2)-1+\frac{\log_2(8/7)}3\,\tau.
\]
Thus the conjecture is reduced, at the correct iterated-logarithmic scale, to chord sets that become unions of paths and cycles after deleting \(O(\log_*n)\) chords. I also analyze exactly the fundamental “serial binary-switch” family: its cycle polynomial factors as a subset-sum product, it can realize a consecutive interval of \(2^h\) long cycle lengths with only \(h\) chords, but if it is genuinely pancyclic then its order is only \(O(h^2)\). The unresolved obstacle is to prove that every near-extremal graph has a recursively nested version of this product structure and that repairing the short missing lengths costs one chord at each iterated-log scale.

## Complete Argument

### 1. Exact constrained subset-sum representation

Fix
\[
G=C_n\cup F,\qquad |F|=h,
\]
where \(C_n\) is the labeled Hamilton cycle. For every chord \(f=uv\), choose one of the two \(u\)-to-\(v\) arcs \(P_f\subseteq C_n\).

For \(S\subseteq F\), define the base-cycle edge set
\[
x(S):=\bigtriangleup_{f\in S} P_f.
\]
There are exactly two even subgraphs having chord set exactly \(S\):
\[
X_0(S)=S\cup x(S),\qquad
X_1(S)=S\cup\bigl(C_n\triangle x(S)\bigr).
\tag{12}
\]
Indeed, \(P_f\cup\{f\}\), \(f\in F\), together with \(C_n\), is a cycle-space basis. Projection to the chord coordinates has kernel \(\{0,C_n\}\), so (12) lists the entire fiber.

Let
\[
a(S)=|x(S)|.
\]
Then
\[
|X_0(S)|=|S|+a(S),\qquad
|X_1(S)|=|S|+n-a(S).
\tag{13}
\]

For a base edge \(e\in E(C_n)\), put
\[
A_e:=\{f\in F:e\in P_f\}
\]
and define the Walsh character
\[
\chi_A(S):=(-1)^{|A\cap S|}.
\]
The indicator of \(e\in x(S)\) is the parity of \(|A_e\cap S|\), and therefore
\[
(-1)^{1_{e\in x(S)}}=\chi_{A_e}(S).
\]
Consequently,
\[
\Phi(S):=\sum_{e\in E(C_n)}\chi_{A_e}(S)=n-2a(S).
\]
Substituting in (13) gives
\[
|X_\varepsilon(S)|
=
|S|+\frac{n-(-1)^\varepsilon\Phi(S)}2,
\qquad \varepsilon\in\{0,1\}.
\tag{14}
\]

Thus the bivariate weight enumerator of the whole cycle space is exactly
\[
\mathcal E_G(z,y)
=
\sum_{S\subseteq F}y^{|S|}
\left(
z^{\,|S|+(n-\Phi(S))/2}
+
z^{\,|S|+(n+\Phi(S))/2}
\right).
\tag{15}
\]

This is a genuine constrained subset-sum/Walsh representation. Moreover, as one moves around \(C_n\), the set \(A_e\) changes only at a chord endpoint. Hence, after equal characters are combined,
\[
\Phi(S)=\sum_{j=1}^{m}w_j\chi_{A_j}(S),
\qquad
m\le 2h,\quad w_j\in\mathbb N,\quad \sum_jw_j=n.
\tag{16}
\]
The sets \(A_j\) occur along a closed walk in the \(h\)-dimensional hypercube in which each coordinate is toggled exactly twice, allowing simultaneous toggles where chords share an endpoint.

The difficulty is that (15) counts all even subgraphs, not only simple cycles. The next lemma gives the exact missing constraint.

---

### 2. Exact simplicity criterion inside a fiber

For \(S\subseteq F\), write \(d_S(v)\) for the degree of \(v\) in the chord subgraph \((V,S)\). For \(X_\varepsilon(S)\), let \(b_\varepsilon(v)\in\{0,1,2\}\) be the number of its two incident base-cycle edges that are selected.

Because \(X_\varepsilon(S)\) is even,
\[
d_S(v)+b_\varepsilon(v)\equiv0\pmod 2.
\tag{17}
\]

#### Lemma 1
The vector \(X_\varepsilon(S)\) is the edge set of a single simple cycle if and only if:

1. \(d_S(v)\le2\) for every \(v\);
2. whenever \(d_S(v)=2\), one has \(b_\varepsilon(v)=0\);
3. the non-isolated part of \((V,X_\varepsilon(S))\) is connected.

In particular, if \(S\) has a vertex of chord-degree at least \(3\), neither vector in its fiber is a simple cycle. If \(S\) has a vertex of chord-degree exactly \(2\), at most one of the two vectors in its fiber can be a simple cycle.

#### Proof

If \(X_\varepsilon(S)\) is a simple cycle, every incident vertex has total degree \(2\). Thus \(d_S(v)\le2\), and if \(d_S(v)=2\), no base-cycle edge at \(v\) can be selected.

Conversely, suppose conditions 1 and 2 hold. By (17):

- if \(d_S(v)=0\), then \(b_\varepsilon(v)\in\{0,2\}\);
- if \(d_S(v)=1\), then \(b_\varepsilon(v)=1\);
- if \(d_S(v)=2\), condition 2 gives \(b_\varepsilon(v)=0\).

Hence every vertex has total degree either \(0\) or \(2\). A nonempty finite graph in which all non-isolated vertices have degree \(2\) is a disjoint union of simple cycles. It is one simple cycle exactly when its non-isolated part is connected.

Finally, complementing the base-cycle edges replaces \(b_\varepsilon(v)\) by \(2-b_\varepsilon(v)\). At a vertex where \(d_S(v)=2\), at most one of these two values can be \(0\). ∎

If \(I_\varepsilon(S)\) denotes the indicator that these three conditions hold, with \(I_0(\varnothing)=0\), then the actual cycle polynomial is exactly
\[
P_G(z,y)
=
\sum_{S\subseteq F}\sum_{\varepsilon=0}^1
I_\varepsilon(S)y^{|S|}
z^{\,|S|+(n-(-1)^\varepsilon\Phi(S))/2}.
\tag{18}
\]
Formula (18) is the precise generating-function formulation of the problem. The unresolved issue is to control the support after imposing \(I_\varepsilon(S)\).

---

### 3. A universal branching-deficiency theorem

Let \(Q=(V,F)\) be the graph formed by the chords alone. Define
\[
\tau_2(Q):=
\min\{|R|:R\subseteq F,\ \Delta(Q-R)\le2\}.
\tag{19}
\]

Thus \(\tau_2(Q)\) is the least number of chords that must be removed to make the chord graph a union of paths and cycles.

#### Theorem 2
If \(G=C_n\cup F\) is pancyclic, \(|F|=h\), and \(\tau=\tau_2(Q)\), then
\[
n-2
\le
2^{h+1}\left(\frac78\right)^{\tau/3}.
\tag{20}
\]
Consequently,
\[
h
\ge
\log_2(n-2)-1
+
\frac{\log_2(8/7)}3\,\tau.
\tag{21}
\]

#### Proof

Construct a \(3\)-uniform hypergraph \(\mathcal H\) whose vertex set is \(F\). Its hyperedges are all triples of chords incident with a common vertex of \(Q\):
\[
E(\mathcal H)
=
\left\{T\subseteq F:|T|=3,\ T\subseteq\delta_Q(v)
\text{ for some }v\right\}.
\]

A set \(R\subseteq F\) meets every hyperedge of \(\mathcal H\) if and only if \(Q-R\) has maximum degree at most \(2\). Hence the transversal number of \(\mathcal H\) is exactly \(\tau\).

Let \(\nu\) be the maximum number of pairwise disjoint hyperedges of \(\mathcal H\). A maximal such matching has a union of \(3\nu\) chord edges which meets every hyperedge; otherwise another disjoint hyperedge could be added. Therefore
\[
\tau\le3\nu,\qquad \nu\ge\tau/3.
\tag{22}
\]

By Lemma 1, the chord set of a simple cycle cannot contain all three edges of any hyperedge of \(\mathcal H\). Fix \(\nu\) pairwise disjoint triples. On each triple there are seven permitted subsets rather than eight. Since these triples are disjoint, the number \(A\) of chord subsets which could possibly support a simple cycle satisfies
\[
A\le 7^\nu2^{h-3\nu}
=2^h\left(\frac78\right)^\nu
\le
2^h\left(\frac78\right)^{\tau/3}.
\tag{23}
\]

Every chord subset has at most two cycle-space vectors in its fiber. Therefore the total number of simple cycles is at most
\[
2A\le
2^{h+1}\left(\frac78\right)^{\tau/3}.
\]
A pancyclic graph contains at least \(n-2\) distinct simple cycles, one for each length \(3,\dots,n\), proving (20). Taking base-two logarithms proves (21). ∎

The constant in (21) is
\[
\frac{\log_2(8/7)}3\approx0.064215.
\]

Thus the desired conjecture already follows for chord sets satisfying
\[
\tau_2(Q)\ge
\left(\frac{3}{\log_2(8/7)}+o(1)\right)\log_*n
\approx15.57\log_*n.
\]
Accordingly, the difficult case becomes
\[
\tau_2(Q)=O(\log_*n).
\tag{24}
\]

There is also a sharper bound when the branching is concentrated at one vertex.

#### Corollary 3
If some vertex is incident with \(d\) chords, then
\[
n-2
\le
2^{h-d+1}
\left(1+d+\binom d2\right),
\tag{25}
\]
and hence
\[
h\ge
\log_2(n-2)-1
+d-\log_2\left(1+d+\binom d2\right).
\tag{26}
\]

#### Proof

A simple cycle can use at most two of those \(d\) chords. There are
\[
1+d+\binom d2
\]
allowed choices on them and \(2^{h-d}\) arbitrary choices on the remaining chords. Each chord set supports at most two cycles. ∎

For large \(d\), the extra term in (26) is
\[
d-2\log_2d+O(1).
\]
This nearly charges one unit for each chord concentrated at a common endpoint, but the loss \(2\log d\) is unbounded and cannot be absorbed into the conjecture’s \(O(1)\).

---

### 4. A multiscale weight-filtration lemma

The following is a rigorous generating-support observation for weighted cores, although it does not by itself improve the standard lower bound.

#### Lemma 4
Let \(K\) be a positive-integer-weighted multigraph having a simple cycle of every weight \(3,\dots,n\). For \(L\le n\), let \(K_{\le L}\) be the spanning subgraph consisting of edges of weight at most \(L\), and let \(r(L)\) be its binary cycle-space dimension. Then
\[
r(L)\ge \left\lceil\log_2(L-1)\right\rceil.
\tag{27}
\]

#### Proof

Every cycle of total weight at most \(L\) uses only edges of weight at most \(L\). Thus the \(L-2\) cycles of weights \(3,\dots,L\) are distinct nonzero vectors in the cycle space of \(K_{\le L}\). Consequently
\[
L-2\le2^{r(L)}-1,
\]
which is equivalent to (27). ∎

The obstruction is that the same cycle-space dimensions can satisfy (27) at many scales. There is no justified way to sum these inequalities over scales.

---

### 5. Exact analysis of the serial binary-switch family

The basic unrestricted-subset-sum obstruction can be realized by an extremely sparse Hamiltonian graph.

Fix \(r\ge2\). Let
\[
v_0,v_1,\dots,v_r
\]
be junction vertices. For each \(i=1,\dots,r\), join \(v_{i-1}\) to \(v_i\) by an internally disjoint path \(P_i\) of length
\[
a_i=d_i+1,\qquad d_i\ge1,
\]
and also add the direct chord
\[
f_i=v_{i-1}v_i.
\]
Finally add the edge \(v_rv_0\).

The Hamilton cycle consists of
\[
P_1P_2\cdots P_r+v_rv_0.
\]
Its order is
\[
n=1+\sum_{i=1}^r a_i
=r+1+\sum_{i=1}^r d_i,
\tag{28}
\]
and the graph has exactly \(n+r\) edges.

#### Proposition 5
The simple-cycle polynomial of this graph is
\[
P_G(z)
=
\sum_{i=1}^r z^{d_i+2}
+
z^{r+1}\prod_{i=1}^r(1+z^{d_i}).
\tag{29}
\]

#### Proof

Contract each path \(P_i\) conceptually to one of two parallel links between \(v_{i-1}\) and \(v_i\), retaining its length.

A simple cycle containing \(v_rv_0\) becomes, after deleting that edge, a simple \(v_0\)-to-\(v_r\) path through the chain. At every stage it chooses either \(P_i\), of length \(d_i+1\), or \(f_i\), of length \(1\). Its length is therefore
\[
1+\sum_{i=1}^r1+\sum_{i\in S}d_i
=
r+1+\sum_{i\in S}d_i.
\]
These cycles contribute the product term in (29).

A cycle not using \(v_rv_0\) lies in a chain whose underlying simple graph is a tree. Such a cycle must use both parallel links at exactly one stage, and consequently has length
\[
(d_i+1)+1=d_i+2.
\]
These are all the remaining cycles. ∎

This family demonstrates why unrestricted additive combinatorics cannot prove the conjecture. If
\[
d_i=2^{i-1},
\]
then \(n=2^r+r\), and the product term in (29) supplies every length
\[
r+1,r+2,\dots,n.
\tag{30}
\]
Thus \(r\) chord choices yield a consecutive interval of \(2^r\) simple-cycle lengths. The only obstruction to pancyclicity is the short initial interval.

For this family, however, exact pancyclicity forces a drastic collapse.

#### Theorem 6
If a serial switch graph with \(r\ge2\) chords is pancyclic, then
\[
n\le 2r^2-5r+10.
\tag{31}
\]

#### Proof

Every cycle represented by the product term of (29) has length at least \(r+1\). Therefore each required length
\[
3,4,\dots,r
\]
must be supplied by one of the local cycles \(d_i+2\). Hence the list \(d_1,\dots,d_r\) contains all the distinct values
\[
1,2,\dots,r-2.
\tag{32}
\]

Choose one occurrence of each value in (32), and put
\[
B=1+2+\cdots+(r-2)
=\frac{(r-2)(r-1)}2.
\]
Only two entries \(x,y\) remain.

The subset sums of the mandatory \(r-2\) entries lie in \([0,B]\), so they have at most \(B+1\) distinct values. Including or excluding \(x\) and \(y\) produces at most four translates of that support. Thus the product term in (29) has at most
\[
4(B+1)
\]
distinct exponents. The local term has at most \(r\) distinct exponents. Since pancyclicity requires \(n-2\) distinct cycle lengths,
\[
n-2\le4(B+1)+r.
\]
Substituting the value of \(B\) gives
\[
n\le2r^2-5r+10.
\]
∎

This bound is within two of an explicit construction.

#### Proposition 7
For every \(r\ge2\), there is a pancyclic serial switch graph with
\[
n=2r^2-5r+8.
\tag{33}
\]

#### Proof

Let
\[
B=\frac{(r-2)(r-1)}2
\]
and choose
\[
d_1,\dots,d_r
=
1,2,\dots,r-2,\ B+1,\ 2B+2.
\tag{34}
\]
For \(r=2\), the initial list is empty and the two values are \(1,2\).

The subset sums of \(1,\dots,r-2\) fill \([0,B]\). Adding \(B+1\) extends this to
\[
[0,2B+1],
\]
and adding \(2B+2\) extends it to
\[
[0,4B+3].
\]
Therefore the product term in (29) supplies every length from
\[
r+1
\]
through
\[
r+1+4B+3=n.
\]
The local cycles corresponding to \(d=1,\dots,r-2\) supply all lengths \(3,\dots,r\). Hence the graph is pancyclic.

Finally,
\[
n=r+1+(4B+3)
=2r^2-5r+8.
\]
∎

This completely disposes of the naive idea that one serial binary product can itself provide asymptotically extremal pancyclic graphs. Recursive “repair” structure is indispensable.

## Self-Audit

1. **The main conjecture remains unproved in the regime \(\tau_2(Q)=O(\log_*n)\).** The branching theorem is rigorous, but known-style nested constructions naturally lie in precisely this regime. I do not claim that the missing inverse theorem follows from the present arguments; this is the reason for the BLOCKED status.

2. **The Walsh polynomial (15) alone is much too permissive.** It counts disconnected and higher-degree even subgraphs. I believe the representation and simplicity criterion are exact because they follow directly from the fundamental cycle-space basis and a vertex-by-vertex degree check, but no valid support estimate strong enough for the conjecture was extracted from them.

3. **The serial-switch theorem concerns a narrow graph class.** Its classification of cycles is reliable because contracting the long paths leaves a path of parallel pairs plus one closing edge, where every cycle is explicitly classifiable. There is no established argument that an arbitrary near-extremal chord set decomposes into such serial pieces.

## Computations To Verify

The following Python enumerates all cycle-space vectors for a fixed chord set and checks simplicity.

```python
from itertools import combinations

def is_simple_cycle(n, edges, mask):
    deg = [0] * n
    adj = [[] for _ in range(n)]

    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            deg[u] += 1
            deg[v] += 1
            adj[u].append(v)
            adj[v].append(u)

    active = [v for v in range(n) if deg[v] > 0]
    if not active:
        return False
    if any(deg[v] != 2 for v in active):
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

def forward_arc_mask(n, u, v):
    """Base edge i is (i, i+1 mod n)."""
    mask = 0
    x = u
    while x != v:
        mask ^= 1 << x
        x = (x + 1) % n
    return mask

def cycle_space_data(n, chords):
    h = len(chords)
    edges = [(i, (i + 1) % n) for i in range(n)] + list(chords)

    Cmask = (1 << n) - 1
    basis = [Cmask]
    for j, (u, v) in enumerate(chords):
        B = forward_arc_mask(n, u, v)
        B |= 1 << (n + j)
        basis.append(B)

    simple = []
    all_vectors = []

    for coeff in range(1 << (h + 1)):
        mask = 0
        for j, B in enumerate(basis):
            if (coeff >> j) & 1:
                mask ^= B

        all_vectors.append(mask)
        if mask and is_simple_cycle(n, edges, mask):
            chord_subset = (coeff >> 1)
            simple.append((mask, mask.bit_count(), chord_subset))

    return edges, all_vectors, simple

def is_pancyclic(n, chords):
    _, _, simple = cycle_space_data(n, chords)
    lengths = {length for _, length, _ in simple}
    return all(k in lengths for k in range(3, n + 1))
```

The exact fiber lengths from the Walsh formula can be checked independently:

```python
def fiber_weight_pairs(n, chords):
    arc_masks = [forward_arc_mask(n, u, v) for u, v in chords]
    h = len(chords)
    ans = {}

    for S in range(1 << h):
        xmask = 0
        s = S.bit_count()
        for j in range(h):
            if (S >> j) & 1:
                xmask ^= arc_masks[j]

        a = xmask.bit_count()
        phi = n - 2 * a
        pair = (
            s + (n - phi) // 2,
            s + (n + phi) // 2
        )
        ans[S] = pair

    return ans
```

To compute \(\tau_2(Q)\) and the exact number of chord subsets of maximum degree at most \(2\):

```python
def chord_degrees(chords, kept_mask):
    vertices = set()
    for u, v in chords:
        vertices.add(u)
        vertices.add(v)
    deg = {v: 0 for v in vertices}

    for i, (u, v) in enumerate(chords):
        if (kept_mask >> i) & 1:
            deg[u] += 1
            deg[v] += 1
    return deg

def tau2(chords):
    h = len(chords)
    full = (1 << h) - 1

    for t in range(h + 1):
        for removed in combinations(range(h), t):
            rmask = sum(1 << i for i in removed)
            kept = full ^ rmask
            deg = chord_degrees(chords, kept)
            if max(deg.values(), default=0) <= 2:
                return t
    raise RuntimeError("unreachable")

def count_maxdeg2_subsets(chords):
    h = len(chords)
    count = 0
    for S in range(1 << h):
        deg = chord_degrees(chords, S)
        if max(deg.values(), default=0) <= 2:
            count += 1
    return count
```

The serial constructions can be generated and checked as follows:

```python
def serial_graph_from_d(d):
    # Hamilton path is 0,1,...,n-1; junctions occur at positions pos[i].
    a = [x + 1 for x in d]
    n = 1 + sum(a)

    pos = [0]
    cur = 0
    for length in a:
        cur += length
        pos.append(cur)

    chords = [(pos[i], pos[i + 1]) for i in range(len(d))]
    return n, chords

def complete_serial_example(r):
    assert r >= 2
    B = (r - 2) * (r - 1) // 2
    d = list(range(1, r - 1)) + [B + 1, 2 * B + 2]
    return d, *serial_graph_from_d(d)

def binary_serial_example(r):
    d = [1 << i for i in range(r)]
    return d, *serial_graph_from_d(d)

for r in range(2, 9):
    d, n, chords = complete_serial_example(r)
    assert n == 2 * r * r - 5 * r + 8
    assert is_pancyclic(n, chords)

for r in range(2, 9):
    d, n, chords = binary_serial_example(r)
    _, _, simple = cycle_space_data(n, chords)
    lengths = {length for _, length, _ in simple}
    assert all(k in lengths for k in range(r + 1, n + 1))
```

A useful exhaustive experiment for the unresolved regime is:

```python
def all_possible_chords(n):
    cycle_edges = {
        frozenset((i, (i + 1) % n))
        for i in range(n)
    }
    out = []
    for u in range(n):
        for v in range(u + 1, n):
            if frozenset((u, v)) not in cycle_edges:
                out.append((u, v))
    return out

def enumerate_pancyclic_sets(n, h):
    possible = all_possible_chords(n)
    records = []

    for F in combinations(possible, h):
        if not is_pancyclic(n, F):
            continue

        _, _, simple = cycle_space_data(n, F)
        records.append({
            "chords": F,
            "tau2": tau2(F),
            "number_of_simple_cycles": len(simple),
            "number_of_lengths": len({x[1] for x in simple}),
            "max_chord_degree": max(
                chord_degrees(F, (1 << h) - 1).values(),
                default=0
            )
        })
    return records
```

The most informative statistics would be the minimum \(\tau_2\) among optimized examples, the number of fibers producing zero, one, or two cycles, and whether deleting a minimum \(\tau_2\)-set leaves one long chord-path with a small number of nested “closing” chords.

## Route Diagnosis

**Proved lemmas**

- Exact Walsh–Fourier formula (15) for the two cycle-space vectors in every chord-coordinate fiber.
- Exact degree-and-connectivity criterion for either vector to be a simple cycle.
- The branching-deficiency inequality (21), reducing the difficult case to \(\tau_2(Q)=O(\log_*n)\).
- The one-vertex refinement (26).
- The weighted light-edge rank inequality (27).
- Exact cycle polynomial and near-sharp quadratic pancyclic bound for serial binary-switch graphs.

**Plausible but unproved**

- Near-complete interval coverage should force the chord graph, after deleting \(O(\log_*n)\) exceptional chords, into a nested serial-switch hierarchy.
- Each exceptional “closing” chord should repair only one iterated scale, yielding one full unit in the lower bound rather than the constant \(0.064\) supplied by degree counting.
- The positive Walsh polynomial in (16), together with the simplicity indicators in (18), should admit an inverse theorem distinguishing nested repair structures from unrestricted binary subset sums.

These claims are essentially the missing heart of the original problem and are not presently justified.

**Dead ends**

- An interval-support theorem for unrestricted subset sums is false: the binary serial family has \(h\) chords and a consecutive interval of \(2^h\) simple-cycle lengths.
- Working only with the even-subgraph enumerator loses the connectivity and degree-two conditions and cannot produce the extra \(\log_*n\).
- Root-of-unity, Parseval, and additive-energy estimates on \(\Phi(S)\) do not distinguish the binary serial example from a genuinely pancyclic spectrum.
- The light-edge rank filtration reuses the same dimensions at every scale and recovers only cycle-space-type bounds.
- Degree branching handles graphs far from maximum chord-degree \(2\), but nested upper-bound constructions are expected to have only \(O(\log_*n)\) exceptional branching chords.

A fresh attempt should concentrate on an inverse theorem for (18) in the regime \(\tau_2(Q)=O(\log_*n)\): classify how a union of chord paths plus a few exceptional chords can make the constrained Walsh support cover the short initial interval. The serial polynomial (29) shows exactly why merely covering almost all long lengths is insufficient; the missing theorem must quantify the recursive cost of repairing the first \(h\), then the first \(\log h\), and so on.