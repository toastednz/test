STATUS: BLOCKED

## Result

The literal Erdős problem is already disproved by \(\{P_3,2K_2\}\); the status above refers to Route 3 applied to the natural repaired conjecture assuming \(\operatorname{ex}(n;\mathcal F)\) is unbounded. I proved a component-selector theorem: up to an additive \(O_{\mathcal F}(n)\), the extremal number of any finite family equals the largest extremal number obtained by selecting one connected component from each forbidden graph. Since every unbounded finite-family extremal number is \(\Omega(n)\), this implies that an unbounded counterexample exists among arbitrary graphs if and only if one exists among connected forbidden graphs. Further pruning pendant trees and removing nonbipartite constraints reduces the remaining question to finite families of connected bipartite graphs of minimum degree at least two. Route 3 therefore completely eliminates disconnectedness as a source of any new unbounded obstruction, but it does not resolve the resulting sparse bipartite problem.

## Complete Argument

### 1. Removing isolated vertices

For a graph \(H\), let \(H^+\) be obtained by deleting all isolated vertices. If \(n\ge v(H)\), then an \(n\)-vertex graph \(X\) contains \(H\) if and only if it contains \(H^+\).

Indeed, one direction is immediate. Conversely, an embedding of \(H^+\) uses \(v(H^+)\) vertices, and at least
\[
n-v(H^+)\ge v(H)-v(H^+)
\]
vertices remain to represent the isolated vertices of \(H\). Since containment is non-induced, those remaining vertices may have arbitrary incident edges.

Thus isolated vertices do not affect any of the asymptotic statements below. I henceforth assume every forbidden graph has no isolated vertices and at least one edge.

---

### 2. A packing-transversal lemma for one disconnected graph

Let
\[
H=C_1\sqcup\cdots\sqcup C_k
\]
be the decomposition of \(H\) into connected components. Define
\[
b(H)=v(H)-\max_{1\le i\le k}v(C_i).
\]

#### Lemma 2.1

If \(X\) is \(H\)-free, then there are an index \(i\) and a set
\[
S\subseteq V(X),\qquad |S|\le b(H),
\]
such that \(X-S\) is \(C_i\)-free.

#### Proof

Order the components so that a largest component is last. Greedily search for vertex-disjoint copies in that order.

Suppose copies of the first \(j-1\) components have already been chosen, and let \(S\) be the union of their vertices. If \(X-S\) contains the \(j\)-th component, choose such a copy and continue. If this succeeds for every component, the chosen copies are pairwise vertex-disjoint and together form a copy of \(H\), contrary to the assumption that \(X\) is \(H\)-free.

Therefore the process fails at some component \(C_i\), and \(X-S\) is \(C_i\)-free. Since the largest component was placed last, every proper prefix of the ordering has total order at most
\[
v(H)-\max_i v(C_i)=b(H).
\]
Thus \(|S|\le b(H)\). ∎

A direct consequence is

\[
\max_i\operatorname{ex}(n;C_i)
\le \operatorname{ex}(n;H)
\le \max_i\operatorname{ex}(n;C_i)+b(H)n.
\tag{2.1}
\]

For the lower bound, every \(C_i\)-free graph is \(H\)-free. For the upper bound, apply Lemma 2.1 to an \(H\)-free graph \(X\). The number of edges incident with \(S\) is at most \(|S|n\), while
\[
e(X-S)\le \operatorname{ex}(n;C_i).
\]

The additive linear term cannot generally be improved to \(o(n)\): for \(H=2K_2\), its only component type is \(K_2\), but
\[
\operatorname{ex}(n;2K_2)=n-1\quad(n\ge4),
\qquad
\operatorname{ex}(n;K_2)=0.
\]

---

### 3. The component-selector theorem for finite families

Let
\[
\mathcal F=\{H_1,\dots,H_r\}.
\]
Write the connected components of \(H_j\) as
\[
C_{j,1},\dots,C_{j,k_j}.
\]

A **component selector** is a tuple
\[
\sigma=(i_1,\dots,i_r),\qquad 1\le i_j\le k_j.
\]
Associated with \(\sigma\) is the connected family
\[
\mathcal C_\sigma
=
\{C_{1,i_1},\dots,C_{r,i_r}\}.
\]
Set
\[
G_{\mathcal F}(n)
=
\max_\sigma \operatorname{ex}(n;\mathcal C_\sigma)
\]
and
\[
B_{\mathcal F}=\sum_{j=1}^r b(H_j).
\]

#### Theorem 3.1: Component-selector theorem

For all \(n\),
\[
G_{\mathcal F}(n)
\le \operatorname{ex}(n;\mathcal F)
\le G_{\mathcal F}(n)+B_{\mathcal F}n.
\tag{3.1}
\]

#### Proof

For the lower bound, fix a selector \(\sigma\). If a graph avoids \(C_{j,i_j}\), it necessarily avoids \(H_j\), because \(C_{j,i_j}\subseteq H_j\). Thus every \(\mathcal C_\sigma\)-free graph is \(\mathcal F\)-free, and hence
\[
\operatorname{ex}(n;\mathcal C_\sigma)
\le \operatorname{ex}(n;\mathcal F).
\]
Taking the maximum over \(\sigma\) gives the first inequality.

For the upper bound, let \(X\) be an \(n\)-vertex \(\mathcal F\)-free graph. For each \(j\), Lemma 2.1 supplies a component \(C_{j,i_j}\) and a set
\[
S_j\subseteq V(X),\qquad |S_j|\le b(H_j),
\]
such that \(X-S_j\) is \(C_{j,i_j}\)-free.

Let
\[
S=\bigcup_{j=1}^r S_j.
\]
Then
\[
|S|\le B_{\mathcal F},
\]
and \(X-S\) is \(\mathcal C_\sigma\)-free for the selector
\(\sigma=(i_1,\dots,i_r)\). Therefore
\[
e(X-S)\le \operatorname{ex}(n-|S|;\mathcal C_\sigma)
\le \operatorname{ex}(n;\mathcal C_\sigma).
\]
The final monotonicity holds because every member of \(\mathcal C_\sigma\) is connected and has an edge, so adding isolated vertices cannot create a forbidden copy. Hence
\[
e(X)
\le e(X-S)+|S|n
\le G_{\mathcal F}(n)+B_{\mathcal F}n.
\]
Maximizing over \(X\) proves the result. ∎

---

### 4. Why the \(O(n)\) error is sufficient in the unbounded case

The following dichotomy makes the linear error harmless.

#### Lemma 4.1: Bounded-or-linear dichotomy

For every finite family \(\mathcal F\) of edge-containing graphs, either
\[
\operatorname{ex}(n;\mathcal F)=O_{\mathcal F}(1),
\]
or, for all sufficiently large \(n\),
\[
\operatorname{ex}(n;\mathcal F)\ge \left\lfloor\frac n2\right\rfloor.
\tag{4.1}
\]

#### Proof

Call a graph star-supported if all its edges share a common endpoint, and matching-supported if its maximum degree is at most one.

If \(\mathcal F\) contains both a star-supported member \(K_{1,a}\) and a matching-supported member \(tK_2\), up to previously removed isolated vertices, then every \(\mathcal F\)-free graph satisfies
\[
\Delta(X)\le a-1,\qquad \nu(X)\le t-1.
\]
The endpoints of a maximal matching form a vertex cover of order at most \(2(t-1)\). Consequently,
\[
e(X)\le 2(t-1)(a-1),
\]
so the joint extremal number is bounded.

Otherwise, at least one of the following holds:

1. No member of \(\mathcal F\) is star-supported. Then the \(n\)-vertex star is \(\mathcal F\)-free, giving \(n-1\) edges.
2. No member of \(\mathcal F\) is matching-supported. Then an \(n\)-vertex matching is \(\mathcal F\)-free, giving \(\lfloor n/2\rfloor\) edges.

This proves the dichotomy. ∎

Combining (2.1) with Lemma 4.1 gives a useful exact criterion.

#### Corollary 4.2

Assume
\[
f(n)=\operatorname{ex}(n;\mathcal F)
\]
is unbounded. For \(H\in\mathcal F\), the following are equivalent:

1. \(\operatorname{ex}(n;H)=O_{\mathcal F}(f(n))\);
2. every connected component \(C\) of \(H\) satisfies
   \[
   \operatorname{ex}(n;C)=O_{\mathcal F}(f(n)).
   \]

#### Proof

If \(H\) controls \(\mathcal F\), then for every component \(C\subseteq H\),
\[
\operatorname{ex}(n;C)\le\operatorname{ex}(n;H)=O(f(n)).
\]

Conversely, if every component has extremal number \(O(f(n))\), then (2.1) and \(n=O(f(n))\), supplied by Lemma 4.1, give
\[
\operatorname{ex}(n;H)
\le \max_{C\in\operatorname{Comp}(H)}\operatorname{ex}(n;C)+b(H)n
=O(f(n)).
\]
∎

---

### 5. Equivalence with the connected-family problem

Consider the repaired assertion:

> For every finite family \(\mathcal F\) with unbounded joint extremal number, some \(H\in\mathcal F\) satisfies
> \[
> \operatorname{ex}(n;H)=O_{\mathcal F}(\operatorname{ex}(n;\mathcal F)).
> \tag{R}
> \]

#### Theorem 5.1

Assertion (R) holds for all finite graph families if and only if it holds for finite families of connected graphs.

#### Proof

One direction is immediate because connected families are special cases.

For the other direction, suppose that \(\mathcal F=\{H_1,\dots,H_r\}\) is an unbounded counterexample to (R). Put
\[
f(n)=\operatorname{ex}(n;\mathcal F).
\]
For each \(j\), \(H_j\) fails to control \(\mathcal F\). By Corollary 4.2, \(H_j\) has a connected component \(C_j\) such that
\[
\operatorname{ex}(n;C_j)\ne O(f(n)).
\tag{5.1}
\]

Let
\[
\mathcal C=\{C_1,\dots,C_r\}.
\]
Since avoiding \(C_j\) implies avoiding \(H_j\), every \(\mathcal C\)-free graph is \(\mathcal F\)-free. Therefore
\[
q(n):=\operatorname{ex}(n;\mathcal C)\le f(n).
\tag{5.2}
\]
If some \(C_j\) controlled \(\mathcal C\), then
\[
\operatorname{ex}(n;C_j)=O(q(n))=O(f(n)),
\]
contradicting (5.1). Thus \(\mathcal C\) is a connected counterexample.

It remains to check that \(q(n)\) is unbounded. None of the selected \(C_j\) can be \(K_2\), because
\[
\operatorname{ex}(n;K_2)=0=O(f(n)).
\]
Every \(C_j\) therefore is connected and has at least two edges. An \(n\)-vertex matching contains no such graph, so
\[
q(n)\ge\left\lfloor\frac n2\right\rfloor.
\]
Thus \(\mathcal C\) is an unbounded connected counterexample. ∎

This is the main Route 3 conclusion: disconnected members cannot create a genuinely new unbounded obstruction. Any such obstruction has a connected component-selector witness.

The bounded example \(\{P_3,2K_2\}\) escapes this reduction precisely because the linear error in Theorem 3.1 is then not absorbable. Its only selector family is essentially \(\{P_3,K_2\}\), whose extremal number is zero.

---

### 6. Reduction from connected graphs to their \(2\)-cores

The connected problem can be narrowed further.

Let \(H\) be connected and contain a cycle. Its \(2\)-core \(K(H)\) is the maximal induced subgraph of minimum degree at least two.

The \(2\)-core is nonempty and connected. Indeed, if two components of the \(2\)-core were joined by a path in \(H\), adding a shortest such path would produce a larger subgraph of minimum degree at least two, contradicting maximality.

Every component of \(H-K(H)\) is a tree attached to exactly one vertex of \(K(H)\). A cycle outside the core, or a tree component with two attachments to the connected core, would again enlarge the \(2\)-core.

#### Lemma 6.1: Extension from the \(2\)-core

If \(Y\) satisfies
\[
\delta(Y)\ge v(H)-1
\]
and contains \(K(H)\), then \(Y\) contains \(H\).

#### Proof

Fix an embedding of \(K(H)\). Root each tree attached to the core at its attachment vertex and order all remaining vertices so that every parent precedes its children.

Embed them in this order. When a new vertex is to be embedded, its parent has already been embedded. At most \(v(H)-2\) already used vertices can be neighbors of the parent's image, while that image has at least \(v(H)-1\) neighbors. Hence an unused neighbor is available. Extra edges do not matter under non-induced containment. ∎

Delete successively from an \(H\)-free graph all vertices whose current degree is less than \(v(H)-1\). At most \(O_H(n)\) edges are deleted. The remaining graph has minimum degree at least \(v(H)-1\), so by Lemma 6.1 it must be \(K(H)\)-free. Therefore
\[
\operatorname{ex}(n;K(H))
\le \operatorname{ex}(n;H)
\le \operatorname{ex}(n;K(H))+O_H(n).
\tag{6.1}
\]

The same pruning can be performed simultaneously for a finite connected cyclic family \(\mathcal H\). If
\[
\mathcal K=\{K(H):H\in\mathcal H\},
\]
then
\[
\operatorname{ex}(n;\mathcal K)
\le \operatorname{ex}(n;\mathcal H)
\le \operatorname{ex}(n;\mathcal K)+O_{\mathcal H}(n).
\tag{6.2}
\]

The linear term is negligible here because a finite family of cyclic graphs has superlinear joint extremal number. To see this, let
\[
L=\max_{H\in\mathcal H}v(H).
\]
In \(G(n,p)\) with
\[
p=n^{-1+1/L},
\]
the expected number of edges is \(\Theta(n^{1+1/L})\), while the expected total number of cycles of lengths at most \(L\) is \(O_L(n)\). Some realization therefore has
\[
e(X)-\#\{\text{cycles of length at most }L\}
=\Omega_L(n^{1+1/L}).
\]
Deleting one edge from each short cycle leaves a graph of girth greater than \(L\) and \(\Omega_L(n^{1+1/L})\) edges. It avoids every member of \(\mathcal H\).

Consequently, the two sides of (6.2) are within a constant factor, indeed within \(1+o(1)\).

If a connected family contains a tree \(T\), that tree already controls the family. If \(T=K_2\), this is immediate. Otherwise an \(n\)-vertex matching is family-free, giving a linear lower bound, while
\[
\operatorname{ex}(n;T)\le (v(T)-2)n.
\]
For the latter inequality, repeatedly delete vertices of degree at most \(v(T)-2\). If a nonempty graph remained, its minimum degree would be at least \(v(T)-1\), allowing a greedy embedding of \(T\).

It follows that the connected repaired conjecture is equivalent to its restriction to connected graphs of minimum degree at least two.

---

### 7. Removing nonbipartite constraints

Let \(\mathcal H\) be a finite family of connected graphs of minimum degree at least two, and let \(\mathcal B\subseteq\mathcal H\) be its bipartite members.

If \(\mathcal B=\varnothing\), the Erdős–Stone–Simonovits theorem proves the desired comparison by choosing a member of minimum chromatic number.

Suppose \(\mathcal B\ne\varnothing\). Then
\[
\operatorname{ex}(n;\mathcal H)
\le \operatorname{ex}(n;\mathcal B).
\]
Conversely, take an extremal \(\mathcal B\)-free graph \(X\). A random bipartition of \(V(X)\) retains in expectation half its edges across the cut. Hence \(X\) has a bipartite subgraph \(Y\) with
\[
e(Y)\ge \frac12e(X).
\]
The graph \(Y\) remains \(\mathcal B\)-free because it is a subgraph of \(X\), and it avoids every nonbipartite member of \(\mathcal H\) because \(Y\) is bipartite. Thus
\[
\frac12\operatorname{ex}(n;\mathcal B)
\le \operatorname{ex}(n;\mathcal H)
\le \operatorname{ex}(n;\mathcal B).
\tag{7.1}
\]

Therefore the repaired conjecture is equivalent to the following remaining statement:

> For every finite family \(\mathcal B\) of connected bipartite graphs with minimum degree at least two, some \(B\in\mathcal B\) satisfies
> \[
> \operatorname{ex}(n;B)=O_{\mathcal B}(\operatorname{ex}(n;\mathcal B)).
> \tag{CB}
> \]

I do not have a proof or counterexample for (CB). This is a sparse bipartite Turán problem of essentially the same unresolved strength as the intended repaired question.

## Self-Audit

1. **The decisive statement (CB) remains unproved.** No component-packing argument obtained control inside connected bipartite graphs, so this is a genuine block rather than a hidden conclusion. I make no claim that (CB) is true.

2. **The selector theorem uses monotonicity under adding isolated vertices.** That monotonicity would fail for arbitrary forbidden graphs with isolated components. It is valid here because isolated vertices were first removed asymptotically and every selected component is connected and edge-containing; a new isolated vertex cannot participate in its copy.

3. **The \(2\)-core extension is the least immediate structural step.** It depends on every component outside the \(2\)-core being a singly attached tree and on the minimum-degree greedy embedding. Both facts were justified above; the large minimum-degree bound \(v(H)-1\) is deliberately wasteful but sufficient.

## Computations To Verify

The following brute-force code checks non-induced containment and extremal numbers for small graphs.

```python
from itertools import combinations, permutations, product

def all_pairs(n):
    return list(combinations(range(n), 2))

def graph_from_mask(n, mask):
    pairs = all_pairs(n)
    return (n, {
        pairs[i] for i in range(len(pairs))
        if (mask >> i) & 1
    })

def contains(X, H):
    """Non-induced subgraph containment."""
    n, EX = X
    h, EH = H
    if h > n:
        return False

    EX = {tuple(sorted(e)) for e in EX}
    for phi in permutations(range(n), h):
        if all(tuple(sorted((phi[u], phi[v]))) in EX for u, v in EH):
            return True
    return False

def extremal(n, family):
    best = 0
    for mask in range(1 << (n * (n - 1) // 2)):
        X = graph_from_mask(n, mask)
        if all(not contains(X, H) for H in family):
            best = max(best, len(X[1]))
    return best
```

Component extraction:

```python
def components(H):
    h, E = H
    adj = [set() for _ in range(h)]
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)

    # Assumes isolated vertices have already been removed.
    seen = set()
    answer = []

    for start in range(h):
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        V = []

        while stack:
            u = stack.pop()
            V.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)

        relabel = {v: i for i, v in enumerate(V)}
        CE = {
            tuple(sorted((relabel[u], relabel[v])))
            for u, v in E if u in relabel and v in relabel
        }
        answer.append((len(V), CE))

    return answer

def selector_families(F):
    choices = [components(H) for H in F]
    return [list(sel) for sel in product(*choices)]

def selector_bound(F):
    total = 0
    for H in F:
        comps = components(H)
        total += H[0] - max(C[0] for C in comps)
    return total
```

Verification of Theorem 3.1:

```python
def verify_selector_theorem(F, max_n=6):
    B = selector_bound(F)
    selectors = selector_families(F)

    for n in range(max(H[0] for H in F), max_n + 1):
        f = extremal(n, F)
        g = max(extremal(n, Cfam) for Cfam in selectors)

        print(n, g, f, g + B*n)
        assert g <= f
        assert f <= g + B*n
```

Two important tests are:

```python
K2 = (2, {(0, 1)})
P3 = (3, {(0, 1), (1, 2)})
twoK2 = (4, {(0, 1), (2, 3)})

verify_selector_theorem([twoK2], max_n=6)
verify_selector_theorem([P3, twoK2], max_n=6)
```

Expected output includes

\[
\operatorname{ex}(n;2K_2)=n-1\quad(n\ge4),
\]
while its selector extremal number is \(\operatorname{ex}(n;K_2)=0\), confirming that the additive \(O(n)\) term is necessary.

The \(2\)-core extension lemma can be tested as follows:

```python
def degrees(H):
    h, E = H
    d = [0] * h
    for u, v in E:
        d[u] += 1
        d[v] += 1
    return d

def two_core(H):
    h, E = H
    alive = set(range(h))

    while True:
        d = {v: 0 for v in alive}
        for u, v in E:
            if u in alive and v in alive:
                d[u] += 1
                d[v] += 1

        remove = {v for v in alive if d[v] < 2}
        if not remove:
            break
        alive -= remove

    relabel = {v: i for i, v in enumerate(sorted(alive))}
    CE = {
        tuple(sorted((relabel[u], relabel[v])))
        for u, v in E if u in alive and v in alive
    }
    return (len(alive), CE)

def min_degree(X):
    n, E = X
    d = [0] * n
    for u, v in E:
        d[u] += 1
        d[v] += 1
    return min(d) if n else 0

def verify_core_extension(H, max_n=7):
    C = two_core(H)
    h = H[0]
    assert C[0] > 0

    for n in range(h, max_n + 1):
        for mask in range(1 << (n * (n - 1) // 2)):
            X = graph_from_mask(n, mask)
            if min_degree(X) >= h - 1 and contains(X, C):
                assert contains(X, H)
```

For searching the remaining block, enumerate connected bipartite graphs with minimum degree at least two, form two- and three-member families, and rank them by

```python
ratio = min(extremal(n, [H]) for H in F) / extremal(n, F)
```

for feasible \(n\). Brute force becomes prohibitive beyond \(n=7\), so the same containment constraints should be transferred to an ILP or SAT solver for \(n=8,9,\dots\).

## Route Diagnosis

**Proved lemmas and reductions**

- A disconnected forbidden graph can be reduced, after deleting \(O_H(1)\) vertices, to forbidding one of its connected components.
- The component-selector formula
  \[
  \max_\sigma\operatorname{ex}(n;\mathcal C_\sigma)
  \le \operatorname{ex}(n;\mathcal F)
  \le \max_\sigma\operatorname{ex}(n;\mathcal C_\sigma)+O_{\mathcal F}(n).
  \]
- Every unbounded finite-family extremal number is \(\Omega(n)\).
- Consequently, any unbounded counterexample produces a connected component-selector counterexample.
- The repaired conjecture is equivalent to its restriction to connected bipartite graphs of minimum degree at least two.

**Plausible but unproved**

- Statement (CB), namely that every finite family of connected bipartite minimum-degree-two graphs is controlled by one member. Route 3 offers no proof of this.
- A stronger block-decomposition theorem reducing such graphs to their \(2\)-connected blocks. Straight component packing does not apply because blocks meet at articulation vertices.

**Dead ends**

- Improving the selector error from \(O(n)\) to \(o(n)\) is impossible: \(2K_2\) already gives a linear gap from its sole component type \(K_2\).
- A bounded vertex transversal alone is insufficient in the linear regime; it may support \(\Theta(n)\) edges. The bounded-or-linear dichotomy repairs this only for the unbounded reduction.
- Attempting to assemble forbidden blocks from independently abundant block copies fails because copies may have incompatible roots or articulation vertices.
- Copy-hypergraph deletion gives no general constant retention theorem; the star–matching example demonstrates the obstruction, and no replacement was found for connected sparse bipartite families.

A fresh attempt should work directly on (CB), either by finding a connected bipartite counterexample with provably incompatible extremal constructions, or by proving a constant-retention/simultaneous-construction theorem for connected bipartite forbidden families. Component packing itself has reached its natural endpoint.