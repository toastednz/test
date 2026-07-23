# Problem Brief: Erdős Problem #1016 — Sparse Pancyclic Graphs

## 1. Precise statement

Throughout, a **graph** means a finite, undirected, simple graph.

For an integer \(n\ge 3\), a graph \(G=(V,E)\) of order \(n\) is **pancyclic** if

\[
|V|=n
\]

and, for every integer \(k\) with \(3\le k\le n\), there are distinct vertices

\[
v_0,v_1,\dots,v_{k-1}\in V
\]

such that

\[
v_iv_{i+1}\in E\quad(0\le i<k-1),
\qquad
v_{k-1}v_0\in E.
\]

Thus “cycle” always means a simple cycle, and its length is its number of vertices, equivalently its number of edges.

Define

\[
h(n):=\min\left\{|E(G)|-n:\; G \text{ is a pancyclic graph on }n\text{ vertices}\right\}.
\]

This minimum exists because \(K_n\) is pancyclic. Since every pancyclic graph contains a Hamilton cycle, it has at least \(n\) edges, so \(h(n)\ge 0\).

The principal question is whether

\[
h(n)\ge \log_2 n+\log_* n-O(1).
\tag{1}
\]

We use the convention

\[
\log_2^{(0)}x=x,\qquad
\log_2^{(j+1)}x=\log_2\bigl(\log_2^{(j)}x\bigr),
\]

and

\[
\log_*x:=\min\{j\ge 0:\log_2^{(j)}x\le 1\}.
\]

Changing the base or stopping threshold changes \(\log_*x\) by at most an additive constant, so it does not affect (1).

Formally, (1) means:

> There exist absolute constants \(C\in\mathbb R\) and \(N\in\mathbb N\) such that, for every integer \(n\ge N\),
> \[
> h(n)\ge \log_2 n+\log_*n-C.
> \]

### Equivalent chorded-cycle formulation

Every pancyclic graph contains a Hamilton cycle \(C\). After labeling its vertices cyclically as \(0,1,\dots,n-1\), all other edges are chords of \(C_n\). Hence \(h(n)\) is equivalently the least \(h\) for which there is a set \(F\) of \(h\) chords of \(C_n\) such that

\[
C_n\cup F
\]

contains a cycle of every length \(3,\dots,n\).

This is the most useful formulation: the graph has exactly \(h\) edges in addition to a fixed Hamilton cycle.

### Ambiguity in “estimate \(h(n)\)”

The broad request “estimate \(h(n)\)” has already been resolved at leading order:

\[
h(n)=(1+o(1))\log_2 n.
\]

The intended unresolved issue is the second-order term. In view of the known upper bound, an affirmative proof of (1) would yield

\[
h(n)=\log_2 n+\log_*n+O(1).
\tag{2}
\]

No exact value of the bounded \(O(1)\) term is being requested.

---

## 2. What counts as a solution

### Complete affirmative solution

A complete affirmative solution must prove that there are constants \(C,N\) such that every pancyclic simple graph \(G\) on \(n\ge N\) vertices satisfies

\[
|E(G)|-n\ge \log_2n+\log_*n-C.
\]

Equivalently, it must prove that for every sufficiently large \(n\), no cycle \(C_n\) with fewer than

\[
\log_2n+\log_*n-C
\]

added chords can contain cycles of all lengths \(3,\dots,n\).

Together with the known upper bound, this establishes (2).

Finite exceptional values of \(n\) are harmless because they can be absorbed into the constant \(C\).

### Complete disproof

The negation of (1) is

\[
\forall C\in\mathbb R\ \forall N\in\mathbb N\
\exists n\ge N:
h(n)<\log_2n+\log_*n-C.
\]

Equivalently, there must be an increasing sequence \(n_j\to\infty\) such that

\[
\log_2n_j+\log_*n_j-h(n_j)\longrightarrow\infty.
\tag{3}
\]

It is enough to construct pancyclic graphs \(G_j\) with

\[
|V(G_j)|=n_j,\qquad |E(G_j)|=n_j+q_j,
\]

such that

\[
\log_2n_j+\log_*n_j-q_j\longrightarrow\infty,
\]

because \(h(n_j)\le q_j\).

A particularly strong disproof would construct infinitely many \(n\) with

\[
h(n)\le \log_2 n+O(1).
\]

### Verification required for a counterexample family

For every graph in a proposed family one must verify:

1. it is finite, simple, and has exactly \(n_j\) vertices;
2. it has exactly \(n_j+q_j\) edges;
3. for every \(k=3,\dots,n_j\), it contains a simple \(k\)-cycle;
4. the asymptotic gap in (3) tends to infinity.

One need not prove \(h(n_j)=q_j\); an upper-bound construction suffices to disprove the conjectured lower bound.

Because the claim contains an unspecified \(O(1)\), **no single finite graph can disprove it**. A family with an unbounded deficit is essential.

---

## 3. What does not count

The following would not resolve the problem.

- Reproving only
  \[
  h(n)\ge \log_2(n-1)-1.
  \]
- Proving
  \[
  h(n)\ge \log_2n+\omega(1)
  \]
  without reaching a \(\log_*n-O(1)\) correction. This would be a major advance, but not a complete solution.
- Proving
  \[
  h(n)\ge \log_2n+o(\log_*n).
  \]
- Establishing the desired bound only for a special infinite subsequence of \(n\). The conjecture is an eventual statement for every \(n\).
- Establishing the bound only for restricted graph classes, such as chords with distinct endpoints, noncrossing chords, bounded maximum degree, or cubic graphs.
- Producing pancyclic graphs with a better upper bound unless the improvement violates (1) by an unbounded amount. A fixed improvement in the hidden constant does not disprove an \(O(1)\) statement.
- Finding cycles of almost every length, or every length only up to \((1-o(1))n\).
- Finding closed walks, Eulerian subgraphs, or elements of the binary cycle space of every relevant cardinality. The required objects are single simple cycles.
- Computer verification for finitely many \(n\), regardless of size.
- A conditional proof depending on an unresolved conjecture.
- Probabilistic or numerical evidence without a rigorous existence or nonexistence argument.
- An asymptotic argument valid only for “most” \(n\) or “most” chord sets.

---

## 4. Known results and context

### 4.1 Bondy’s claimed bounds

Bondy [Bo71] claimed, without supplying full details, that

\[
\log_2(n-1)-1
\le h(n)
\le \log_2n+\log_*n+O(1).
\tag{4}
\]

A published proof of the lower bound was later given by Griffin [Gr13]. A published proof of the upper bound appears in Chapter 4.5 of George, Khodkar, and Wallis [GKW16].

Thus the current rigorous bounds are

\[
\log_2(n-1)-1
\le h(n)
\le \log_2n+\log_*n+O(1).
\tag{5}
\]

Consequences include

\[
h(n)=\log_2n+O(\log_*n)
\]

and

\[
h(n)\sim\log_2n.
\]

The leading asymptotic order is therefore settled. The problem concerns an extremely fine additive correction.

### 4.2 The standard cycle-space lower bound

Let \(G\) be pancyclic with

\[
|V(G)|=n,\qquad |E(G)|=n+h.
\]

Because \(G\) is Hamiltonian, it is connected. Its binary cycle space

\[
Z_1(G;\mathbb F_2)
\]

has dimension

\[
|E|-|V|+1=h+1.
\]

It therefore has exactly

\[
2^{h+1}-1
\]

nonzero elements.

Every simple cycle has a distinct nonzero edge-incidence vector in this cycle space. Since a pancyclic graph has at least one cycle of each of the \(n-2\) lengths \(3,\dots,n\),

\[
n-2\le 2^{h+1}-1.
\]

Hence

\[
n-1\le 2^{h+1}
\]

and therefore

\[
h\ge \log_2(n-1)-1.
\tag{6}
\]

For integral \(h\), this can be written as

\[
h(n)\ge \left\lceil\log_2(n-1)\right\rceil-1.
\]

The desired extra \(\log_*n\) cannot follow from the dimension of the cycle space alone. It must exploit the fact that only a highly constrained subset of cycle-space elements are connected 2-regular subgraphs, and that their edge cardinalities must cover an entire interval.

### 4.3 Fiber structure relative to a Hamilton cycle

Fix a Hamilton cycle \(C\) and let \(F\) be its \(h\) chords. Projection of a cycle-space vector onto its chord coordinates maps the \((h+1)\)-dimensional cycle space to \(\mathbb F_2^h\). Its kernel is

\[
\{0,C\}.
\]

Consequently, for each specified subset \(S\subseteq F\), there are at most two cycle-space vectors whose chord set is exactly \(S\), and they differ by symmetric difference with \(C\).

If both vectors are simple cycles \(D,D'\), then their base-cycle edges are complementary and they have the same chord set. Thus

\[
|D|+|D'|=n+2|S|.
\tag{7}
\]

This pairing is a substantial source of additional structure beyond raw cycle-space counting.

### 4.4 Suppression to a small weighted core

A Hamiltonian graph has minimum degree at least \(2\). If \(G\) has \(n+h\) edges, then

\[
\sum_{v\in V(G)}(\deg(v)-2)=2h.
\tag{8}
\]

Therefore at most \(2h\) vertices have degree at least \(3\).

For \(h>0\), suppress all maximal paths whose internal vertices have degree \(2\). The result is a weighted multigraph \(K\), where each core edge is assigned the number of original edges in its corresponding path. If \(b=|V(K)|\), then

\[
b\le 2h,
\qquad
|E(K)|=b+h\le 3h.
\tag{9}
\]

The edge weights are positive integers summing to

\[
n+h.
\]

Simple cycles in the original graph correspond to suitable simple cycles of the multigraph, with original cycle length equal to the sum of the corresponding edge weights.

Thus the problem may be viewed as an additive problem about cycle weights in a multigraph of size \(O(h)\), with total weight exponential in \(h\).

### 4.5 Erdős’s stronger belief

Erdős believed the upper bound in (4) was closer to the truth. According to the commentary, he could not even prove

\[
h(n)-\log_2n\longrightarrow\infty.
\tag{10}
\]

The proposed lower bound would imply (10), since \(\log_*n\to\infty\).

### 4.6 Relation to other pancyclicity results

Bondy’s dense pancyclicity theorem states, roughly, that a sufficiently dense Hamiltonian graph is pancyclic, with the balanced complete bipartite graph as the extremal exception. That theorem concerns forcing pancyclicity from density. The present problem is in the opposite regime: it asks how sparse a deliberately constructed pancyclic graph can be. Dense pancyclicity theorems do not directly approach the additive \(\log_*n\) issue.

---

## 5. Traps and edge cases

### 5.1 The cycle-space dimension is \(h+1\), not \(h\)

There are \(h\) chords relative to a Hamilton cycle, but the Hamilton cycle itself contributes one independent cycle-space direction. Thus

\[
\dim Z_1(G;\mathbb F_2)=h+1.
\]

Dropping this extra \(1\) changes the lower bound.

### 5.2 A chord subset does not determine a unique cycle

Even one chord produces two cycles, obtained using the two arcs between its endpoints on the Hamilton cycle. More generally, a fixed chord subset can correspond to as many as two cycle-space vectors. A claimed \(2^h\) upper bound on the total number of cycles is therefore false; the immediate bound is \(2^{h+1}-1\).

### 5.3 Most cycle-space vectors are not simple cycles

A nonzero even subgraph can be a disjoint union of cycles or a connected Eulerian graph with vertices of degree \(4\) or more. It cannot automatically be used as a cycle of its edge cardinality.

### 5.4 Different lengths require different cycles, but not disjoint cycles

The \(n-2\) required cycles need not be edge-disjoint, vertex-disjoint, nested, or related in any consistent way.

### 5.5 Chord crossings have no topological significance

The graph is not assumed planar. Crossing chords in a circular drawing do not create vertices and cannot be treated as intersections.

### 5.6 Small \(n\)

The natural domain is \(n\ge3\). If \(n<3\), the defining range of cycle lengths is empty and vacuous conventions would distort the problem.

Some exact small values are:

\[
h(3)=0,\qquad h(4)=1,\qquad h(5)=1,\qquad h(6)=2,\qquad h(7)=2.
\]

Constructions:

- \(n=4\): \(C_4\) plus one diagonal;
- \(n=5\): \(C_5\) plus a chord joining vertices at cyclic distance \(2\);
- \(n=6\): \(C_6\) plus chords \(02\) and \(03\);
- \(n=7\): \(C_7\) plus chords \(02\) and \(03\).

The corresponding lower bounds follow from (6).

### 5.7 Non-monotonicity

There is no immediate useful monotonicity relation between \(h(n)\) and \(h(n+1)\). Deleting or subdividing a vertex can destroy many required cycle lengths. An upper bound or lower bound on a subsequence does not automatically extend to intervening orders.

### 5.8 Suppression produces a multigraph

Even though the original graph is simple, suppressing degree-2 paths can produce parallel edges. Core cycles of two parallel edges may expand to simple cycles of length at least \(3\). Arguments on the core must use the correct multigraph notion and retain edge weights.

### 5.9 The Hamilton cycle is not unique

For exhaustive search one may fix and label one Hamilton cycle, because every pancyclic graph has at least one. But an arbitrary graph may have many Hamilton cycles and therefore many chord representations. Counting representations is not the same as counting graphs.

### 5.10 A finite improvement cannot refute an \(O(1)\) statement

For example, finding one graph with

\[
h<\log_2n+\log_*n-100
\]

does not disprove the conjecture. The hidden constant could exceed \(100\).

---

## 6. Verification hooks

### 6.1 Exhaustive cycle-space enumeration for a fixed chord set

For a graph \(G=C_n\cup F\) with \(|F|=h\), construct a cycle-space basis as follows:

- one basis vector is the Hamilton cycle \(C_n\);
- for each chord \(f=uv\), choose one \(u\)-to-\(v\) arc \(P_f\) on \(C_n\), and use
  \[
  B_f=P_f\cup\{f\}.
  \]

The vectors

\[
C_n,\quad \{B_f:f\in F\}
\]

form a basis, since each \(B_f\) has a unique chord coordinate.

Enumerate all \(2^{h+1}\) symmetric differences of basis vectors. A nonempty edge set \(X\) is the edge set of a single simple cycle exactly when:

1. every vertex incident with \(X\) has degree \(2\) in \((V,X)\);
2. the non-isolated part of \((V,X)\) is connected.

Record \(|X|\) for every such vector. The graph is pancyclic exactly when all lengths \(3,\dots,n\) occur.

For the relevant sparse regime \(h\approx\log_2n\), this requires only about \(O(n)\) cycle-space vectors per graph, rather than \(2^n\) vertex subsets.

### 6.2 Exhaustive search for \(h(n)\) at small \(n\)

Fix the labeled Hamilton cycle

\[
0\,1\,2\,\cdots\,(n-1)\,0.
\]

There are

\[
\binom n2-n=\frac{n(n-3)}2
\]

possible chords. For a proposed value \(q\), enumerate all \(q\)-subsets of these chords, quotienting by the dihedral action if desired. Test each graph by cycle-space enumeration.

This search is exhaustive because every pancyclic graph contains a Hamilton cycle that can be relabeled as the fixed \(C_n\).

To prove \(h(n)=q\), one needs:

- a pancyclic chord set of size \(q\);
- exhaustive nonexistence for every size \(<q\).

### 6.3 Independently checkable certificates

A positive certificate can consist of:

- the chord list;
- for every \(k=3,\dots,n\), an ordered list of \(k\) distinct vertices forming a \(k\)-cycle.

Verification is polynomial in the total certificate size.

A negative finite certificate is harder. It may be supplied as:

- an exhaustive canonical list of chord sets;
- an independently checkable SAT/SMT unsatisfiability certificate;
- or a complete branch-and-bound log with verifiable pruning rules.

### 6.4 SAT or integer programming formulation

For fixed \(n,h\), use Boolean variables \(x_{uv}\) for potential chords. Impose

\[
\sum x_{uv}=h.
\]

For each \(k\), introduce variables encoding a selected \(k\)-cycle. Degree-two constraints alone are insufficient because they permit disjoint unions of cycles; connectivity or subtour-elimination constraints are required.

Alternatively, use a lazy solver:

1. propose a chord set;
2. enumerate all simple-cycle lengths by cycle-space enumeration;
3. if a length \(k\) is missing, derive a blocking constraint against the current chord configuration.

### 6.5 Weighted-core checks

For small \(h\):

1. enumerate connected multigraph cores with
   \[
   |V|\le2h,\qquad |E|-|V|=h;
   \]
2. assign bounded positive integer weights to core edges;
3. enumerate simple core cycles and their weighted lengths;
4. optimize the largest \(n\) for which all lengths \(3,\dots,n\) occur and the weighted subdivision is a simple Hamiltonian graph.

SMT is suitable because the condition that a chosen cycle has a prescribed length is linear in the edge weights once the core cycles are enumerated.

### 6.6 Statistics worth recording

For optimized chord sets, record:

- number of simple cycles;
- number of distinct cycle lengths;
- for each chord subset \(S\), whether zero, one, or two simple cycles occur;
- collisions among cycle lengths;
- the distribution of the paired sums \(n+2|S|\);
- gaps between consecutive chord endpoints on the Hamilton cycle;
- sizes and weights of the suppressed core.

These can directly test the structural claims needed by the attack routes below.

---

## 7. Attack routes

### Route 1: Weighted-core reduction and additive cycle spectra

**Core mechanism.**  
Suppress degree-2 paths and reduce the graph to an \(O(h)\)-vertex weighted multigraph. The original order \(n\) is carried by large positive edge weights, and pancyclicity becomes the requirement that weighted simple-cycle sums cover the entire interval \([3,n]\).

**Key lemma needed.**  
A sufficient theorem would be:

> If an admissible weighted core has excess \(h\), total subdivision order \(n\), and has a simple cycle of every weight \(3,\dots,n\), then
> \[
> h\ge \log_2n+\log_*n-O(1).
> \]

A more useful proof would establish this through an explicit multiscale bound on the length of a consecutive interval in the core’s cycle-weight spectrum.

**Why it might work.**  
The core has at most \(2h\) vertices and \(3h\) edges, while its total weight is about \(n\), exponentially larger than \(h\). Long intervals of exact subset sums normally require strong “complete sequence” structure. Simple core cycles are much more constrained than arbitrary subsets of edges, so one may be able to prove that each transition to a new weight scale consumes an additional unit of excess. Iterating over scales is a natural possible source of \(\log_*n\).

**Likely failure point.**  
Weighted cores may simulate almost unrestricted binary subset sums. A theorem based only on the number of core edges or ordinary subset-sum gaps will probably recover only the \(\log_2n\) term.

**Quick obstruction test.**  
For \(h\le 8\) or \(10\), enumerate or optimize weighted cores. Test whether extremizers resemble binary complete sequences and whether they lose approximately one additional edge at each iterated-log scale. If arbitrary cores produce substantially longer intervals than chorded-Hamiltonian cores, the admissibility conditions must be incorporated explicitly.

---

### Route 2: Binary cycle-space fibers and a multiscale deficiency theorem

**Core mechanism.**  
Use the projection from the cycle space onto the \(h\) chord coordinates. Each chord subset has at most two possible cycle vectors, paired by symmetric difference with the Hamilton cycle, and paired simple cycles satisfy

\[
|D|+|D'|=n+2|S|.
\]

**Key lemma needed.**  
One target is a bound of the form

\[
\#\{\text{distinct simple-cycle lengths}\}
\le
C\frac{2^h}{2^{\log_* L}},
\tag{11}
\]

where \(L\) is the largest interval of consecutive lengths represented, or a comparable self-consistent parameter. If \(L\ge n-2\), (11) gives

\[
n\le C\frac{2^h}{2^{\log_*n}}
\]

and hence the conjectured lower bound.

The real content must be a multiscale statement that many chord-coordinate fibers are unusable, disconnected, nonsimple, or length-colliding.

**Why it might work.**  
Raw cycle-space counting allows two vectors per chord set, but simultaneous simplicity of both paired vectors is restrictive. Their lengths are reflected around \((n+2|S|)/2\). Covering every integer length may force near-saturation at one scale, which in turn forces additional losses at a smaller scale. Such repeated saturation-versus-deficiency arguments are plausible sources of an iterated logarithm.

**Likely failure point.**  
The known upper constructions are presumably close to saturating the available fibers. A crude constant-factor loss at each fixed scale is insufficient; the proof must extract precisely a factor comparable to \(2^{\log_*n}\), while not accidentally proving a stronger false bound such as \(\log n+\log\log n\).

**Quick obstruction test.**  
For computationally optimized examples, tabulate the number of chord subsets producing zero, one, or two simple cycles. Plot

\[
\frac{2^h}{\#\{\text{distinct cycle lengths}\}}
\]

against \(2^{\log_*n}\). If extremizers exhibit no growing multiscale deficiency, this route in its naive form is blocked.

---

### Route 3: Long chord-free arcs and recursive path-spectrum decomposition

**Core mechanism.**  
The at most \(2h\) chord endpoints divide the Hamilton cycle into at most \(2h\) chord-free arcs. A cycle that enters the interior of such an arc must traverse the whole arc between its endpoints. Cycle lengths can therefore be expressed using lengths of paths in the complementary chorded region.

**Key lemma needed.**  
Find a chord-free arc \(A\) for which pancyclicity forces the complementary graph to realize a long consecutive interval of path lengths between the endpoints of \(A\). Then prove a recurrence showing that each reduction to a smaller path-spectrum problem costs at least one chord, and that the number of reductions is \(\log_*n-O(1)\).

A schematic desired recurrence would separate a near-binary doubling term from a one-unit “scale transition” penalty.

**Why it might work.**  
The upper bound’s \(\log_*n\) term strongly suggests a recursive construction across iterated size scales. A matching lower bound may come from reversing that recursion: exact coverage of lengths around a long empty arc forces a smaller exact interval problem in the remainder.

**Likely failure point.**  
The longest guaranteed chord-free arc has length only about \(n/(2h)\), and cycles may cover missing lengths using many unrelated chord configurations. The first decomposition step may yield only the known \(\log n\) count and fail to recurse cleanly.

**Quick obstruction test.**  
For extremal small examples, identify the longest chord-free arc and compute the full set of endpoint-to-endpoint path lengths in the complementary graph. If this set is highly disconnected even though the whole graph is pancyclic, then a simple interval-recursion lemma is false and more elaborate boundary states are needed.

---

### Route 4: Generating functions and constrained subset sums

**Core mechanism.**  
For the weighted core or chorded cycle, consider the cycle-length generating polynomial

\[
P_G(z)=\sum_{D\text{ simple cycle}}z^{|D|}.
\]

Pancyclicity says every coefficient of \(z^k\), \(3\le k\le n\), is positive. Encode cycle incidence vectors as constrained subsets of a small collection of weighted arcs and chords.

**Key lemma needed.**  
Prove that the support of the constrained cycle-sum family cannot contain a consecutive interval of length \(n-O(1)\) unless there are at least

\[
\log_2n+\log_*n-O(1)
\]

independent chord choices. Possible tools include:

- inverse Littlewood–Offord theory;
- additive-energy bounds;
- dissociated-set decompositions;
- interval-covering theorems for subset sums;
- log-concavity or unimodality properties of specialized cycle polynomials.

The lemma must use graphic/simple-cycle constraints, not merely arbitrary subset sums.

**Why it might work.**  
The requirement is unusually rigid: every integer in a long interval must be represented exactly as a cycle weight. The support, not just the number of representations, matters. Additive inverse theorems may show that near-perfect interval coverage forces a hierarchical sequence of weights, with one extra structural choice at each iterated-log level.

**Likely failure point.**  
Unrestricted binary subset sums cover intervals of exponential length with only \(\log_2n+O(1)\) generators. Therefore any argument that forgets the connectivity and degree-two constraints of cycles cannot recover \(\log_*n\).

**Quick obstruction test.**  
For optimized graphs, compare the actual cycle-length support with the unrestricted subset-sum support of the same arc weights. If the two supports are nearly identical, generic additive combinatorics may be too weak. If most unrestricted sums are forbidden by simplicity, this route is more promising.

---

### Route 5: Disproof by eliminating the recursive “level tax”

**Core mechanism.**  
Treat the known upper construction as a recursive length-covering gadget. Attempt to redesign the composition step so that the additive one-chord cost per iterated-log level is avoided.

**Key lemma needed.**  
Construct a composition operation that takes smaller chorded cycles or path-length gadgets and produces a much larger pancyclic graph while paying only the binary information cost. Ideally it would yield infinitely many \(n\) with

\[
h(n)\le \log_2n+O(1),
\]

or at least

\[
h(n)\le \log_2n+\log_*n-f(n)
\]

for some \(f(n)\to\infty\).

The composition must guarantee every intermediate cycle length, not merely many lengths or a union of large intervals.

**Why it might work.**  
The \(\log_*n\) term in the published upper bound could conceivably be an artifact of repairing gaps independently at each recursion level. Shared chords, overlapping gadgets, or a more efficient mixed-radix construction might repair several levels simultaneously.

**Likely failure point.**  
Exact interval coverage at the interface between two gadgets may intrinsically require one new chord per scale. If so, the upper construction’s \(\log_*n\) tax reflects a genuine obstruction rather than inefficiency.

**Quick obstruction test.**  
Define finite boundary signatures recording which path lengths a gadget realizes between one or two attachment vertices. Use SAT or exhaustive search to find the cheapest gadget composition for small depth. If every composition that doubles the usable interval necessarily increases the “repair count,” this is evidence against disproof by simple recursive gluing. Conversely, a reusable gadget that repairs multiple scales at once would be a serious candidate for an infinite counterexample family.

---

## 8. Verdict on difficulty

This is a longstanding and technically difficult second-order extremal problem. The leading term

\[
h(n)\sim\log_2n
\]

is easy from the cycle-space count and the known construction, but the conjecture asks for an additive term of only \(\log_*n\), which grows extraordinarily slowly. Standard asymptotic losses will completely swamp the quantity one is trying to detect.

Even the weaker statement

\[
h(n)-\log_2n\to\infty
\]

was explicitly beyond Erdős’s methods and remains an important intermediate target according to the supplied commentary.

There is no known equivalence to a famous conjecture such as the Riemann hypothesis, Hadwiger’s conjecture, or a major additive-combinatorial conjecture. The difficulty instead comes from requiring an almost sharp structural analysis of which vectors in a low-dimensional graphic cycle space can simultaneously be simple cycles with all possible cardinalities.

A successful proof will probably need a genuinely multiscale structural lemma. A counting argument that sees only the dimension \(h+1\), or an additive argument that treats cycles as arbitrary subsets, cannot distinguish the conjectured bound from the already known \(\log_2n-O(1)\) lower bound.