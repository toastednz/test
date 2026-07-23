# Problem Brief: Erdős Problem #1212

## 1. Precise statement

Let \(\mathbb N=\{1,2,3,\dots\}\). The convention \(\mathbb N=\{0,1,2,\dots\}\) would make no difference to the question because the desired path is required to have both coordinates \(>1\).

Define the **visible lattice-point graph**
\[
G=(V,E)
\]
by
\[
V=\{(x,y)\in \mathbb N^2:\gcd(x,y)=1\},
\]
and
\[
\{(x,y),(x',y')\}\in E
\quad\Longleftrightarrow\quad
|x-x'|+|y-y'|=1.
\]
Thus adjacent vertices differ by \(+1\) or \(-1\) in exactly one coordinate.

An integer \(n>1\) is **composite** if it is not prime. Define the set of admissible vertices
\[
A=\left\{(x,y)\in V:
x>1,\ y>1,\ \text{and }(x\text{ is composite or }y\text{ is composite})
\right\}.
\]
Since \(x,y>1\), the last condition is equivalent to saying that \(x\) and \(y\) are not both prime.

Let \(H=G[A]\) be the subgraph of \(G\) induced by \(A\).

### Formal question

Does \(H\) contain a one-way infinite simple path, i.e. a sequence
\[
v_0,v_1,v_2,\dots,\qquad v_n=(x_n,y_n)\in A,
\]
such that:

1. \(v_n\neq v_m\) whenever \(n\neq m\);
2. \(|x_{n+1}-x_n|+|y_{n+1}-y_n|=1\) for every \(n\);
3. \(\gcd(x_n,y_n)=1\) for every \(n\);
4. \(x_n,y_n\ge 2\) for every \(n\);
5. at least one of \(x_n,y_n\) is composite for every \(n\)?

Such a path is usually called a **ray**.

Because \(H\) is locally finite, every ray eventually leaves every finite box. Conversely, an unbounded walk in \(H\), even if it repeats vertices, visits an infinite connected locally finite subgraph and hence yields a ray by König’s infinity lemma. Thus the usual readings of “a path going to infinity” are equivalent here.

### Ambiguities and stronger variants

- The database commentary later asks whether the path can be **monotone**. This is a stronger follow-up, not part of the main problem. In the positive quadrant, monotonicity in distance from the origin means that every step is east or north.
- The still stronger question about changing direction after a bounded number of steps asks for a uniform bound on the lengths of horizontal and vertical runs. It is also not part of the main problem.
- No starting vertex is prescribed.

---

## 2. What counts as a solution

### Complete proof

A complete affirmative solution must establish the existence of a ray in \(H\). This can be done in any of the following equivalent ways.

1. **Direct construction:** Give an explicit or recursively defined sequence \(v_0,v_1,\dots\) and prove all five conditions above for every index.
2. **Infinite-component proof:** Prove that \(H\) has an infinite connected component. Since \(H\) is locally finite, that component contains a ray.
3. **Rooted compactness proof:** Find one fixed admissible vertex \(v\) from which there are self-avoiding admissible paths of every finite length. The finitely branching tree of such path prefixes then has an infinite branch by König’s lemma.

Every arithmetic claim used to certify the path must be proved uniformly. In particular:

- every visited pair must be coprime;
- the path may never visit a prime-prime pair;
- no use of \(1\) is allowed;
- adjacency must be by unit horizontal or vertical steps;
- an infinite list of disconnected finite paths is insufficient.

A monotone admissible ray, or one with bounded straight-run length, would solve the stated problem because it is stronger than required.

### Complete disproof

A complete negative solution must prove
\[
H\text{ has no ray}.
\]
Because \(H\) is locally finite, this is equivalent to
\[
\text{every connected component of }H\text{ is finite}.
\]

There is no single finite “counterexample vertex” to this existential question. A valid disproof must control **every possible starting vertex**. Examples of adequate forms would be:

- a theorem assigning to every \(v\in A\) a finite set \(S_v\subseteq A\) such that \(v\in S_v\) and every admissible neighbor of every point of \(S_v\) also lies in \(S_v\);
- a family of finite arithmetic barriers proving that every admissible point is enclosed in a finite region from which no admissible path can escape;
- a global invariant or decomposition proving all components finite.

For a machine-verifiable trapping certificate, each boundary point must be checked against all four possible grid neighbors. A boundary neighbor is blocked only if it is outside the positive region, has nontrivial gcd, or is a prime-prime pair. A finite trapped component proves only that particular component is finite; it does not disprove the problem unless the construction applies to all possible starts.

---

## 3. What does not count

The following do not resolve the problem.

1. **A path in the full graph \(G\)** that passes through prime-prime pairs.
2. **The older result with only \(x,y>1\)** and no compositeness restriction.
3. A path that has only finitely many, or density zero many, forbidden vertices. There must be no forbidden vertex at all.
4. Arbitrarily long admissible finite paths whose starting points vary. A locally finite graph can have finite components of unbounded size but no ray.
5. Admissible paths crossing arbitrarily large boxes unless they are rooted or linked compatibly so that compactness applies.
6. Positive density of admissible vertices.
7. Proof that the full visible-point graph has an infinite component.
8. A finite computation finding a long path, a large apparent component, or annular crossings up to some bound.
9. Conditional constructions based on unproved conjectures such as Hardy–Littlewood prime-tuples, Cramér-type gap estimates, or unproved uniform sieve assertions.
10. Heuristic arguments based on independent site percolation.
11. A proof restricted to a finite coordinate range or to a special collection of boxes without showing how the crossings concatenate indefinitely.
12. A proof that no monotone ray exists. That would not exclude a nonmonotone ray.
13. A finite trapped component. A negative answer requires all components to be finite.

---

## 4. Known results and context

### 4.1 The classical weaker construction

Let \(p_k\) be the \(k\)-th prime. Erdős reports that Stewart observed the path
\[
(p_k,p_{k+1})
\to (p_k,p_{k+1}+1)
\to\cdots\to
(p_k,p_{k+2})
\]
followed by
\[
(p_k,p_{k+2})
\to(p_k+1,p_{k+2})
\to\cdots\to
(p_{k+1},p_{k+2}).
\]
This joins \((p_k,p_{k+1})\) to \((p_{k+1},p_{k+2})\).

For the vertical segment, \(p_k\) is prime, so visibility fails only at multiples of \(p_k\). If
\[
p_{k+2}<2p_k,
\]
then the interval \([p_{k+1},p_{k+2}]\subset (p_k,2p_k)\) contains no multiple of \(p_k\). On the horizontal segment, every varying coordinate is positive and smaller than the fixed prime \(p_{k+2}\), so it is automatically coprime to \(p_{k+2}\). The inequality holds for \(k\ge 4\), as noted in the database commentary.

Concatenating these paths gives a monotone ray in the visible-point graph restricted only by \(x,y>1\).

This does **not** solve the present problem. Its waypoints \((p_k,p_{k+1})\) are prime-prime pairs and hence forbidden. The straight segments can also contain further prime-prime vertices.

### 4.2 Infinite components of the full visible-point graph

According to Erdős’s account, Herzog and Stewart proved that the full graph \(G\) has exactly one infinite component and conjectured that
\[
(a,p)
\]
lies in that infinite component whenever \(p\) is prime and \(p\nmid a\). The database commentary notes that the cited Herzog–Stewart paper [HeSt71] concerns finite patterns of visible points and apparently does not contain this graph-theoretic result, so the attribution and precise theorem should be treated cautiously.

Even if correct, this result does not settle the problem: deleting the prime-prime vertices may destroy the relevant connections. A zero-density deletion can radically change component structure.

### 4.3 Density information

The number of coprime pairs in \([1,N]^2\) is
\[
\frac{6}{\pi^2}N^2+O(N\log N).
\]
The number of prime-prime pairs in the box is at most
\[
\pi(N)^2=O\!\left(\frac{N^2}{\log^2 N}\right)=o(N^2).
\]
Therefore the admissible set \(A\) still has asymptotic density
\[
\frac{6}{\pi^2}
\]
in the integer lattice.

This is suggestive but proves nothing about an infinite component. Positive-density subsets of \(\mathbb Z^2\) can have only finite components.

### 4.4 Relevant elementary arithmetic structure

For fixed \(y=m\), the visible points in that row are exactly
\[
\{(x,m):\gcd(x,m)=1\}.
\]
Thus a horizontal interval at height \(m\) can be traversed only if every integer in the corresponding \(x\)-interval is coprime to \(m\). The analogous statement holds for columns.

Important consequences include:

- If \(m\) is even, there is no horizontal edge at height \(m\): among two consecutive \(x\)-coordinates, one is even and hence not coprime to \(m\).
- If \(m\) is even, a visible point \((x,m)\) has \(x\) odd.
- Long runs of composite numbers do not automatically produce paths because visibility imposes independent divisibility obstructions.
- The Chinese remainder theorem can construct long prescribed patterns of divisibility or compositeness, but avoiding divisibility throughout a corridor is a different and often harder requirement.

The standard Jacobsthal-function viewpoint—measuring gaps between integers coprime to a modulus—is relevant to locating visible points in rows and columns, though traversing a whole interval requires consecutive reduced residues rather than merely one reduced residue.

### 4.5 Stronger follow-up questions

The database commentary asks whether one can require:

1. a monotone admissible ray; and
2. a monotone admissible ray whose direction changes after at most \(C\) steps, for some absolute constant \(C\).

Neither strengthening is part of Problem #1212. Failure of either stronger statement would not settle the unrestricted problem.

---

## 5. Traps and edge cases

### 5.1 Parity is a serious local obstruction

All primes other than \(2\) are odd. Near a forbidden odd prime-prime point \((p,q)\), the four axis-neighbors have one even coordinate:
\[
(p\pm1,q),\qquad (p,q\pm1).
\]
A naive one-cell square detour generally fails. For example,
\[
(p-1,q+1)
\]
has both coordinates even and is not visible. Thus “go around each prime-prime point by a unit square” is invalid.

More generally:

- at an even-height row, no horizontal move is possible;
- at an even-\(x\) column, no vertical move is possible.

Parity can force a path to continue straight through a local region before it is able to turn.

### 5.2 The prime \(2\)

Points such as \((2,p)\) with \(p\) an odd prime are forbidden because both coordinates are prime. Points \((2,m)\) with \(m\) odd composite are potentially admissible, but vertical movement at \(x=2\) is impossible because one of two consecutive \(y\)-coordinates is even and shares gcd \(2\).

Arguments stated only for odd primes must handle or avoid coordinate \(2\).

### 5.3 Composite does not imply visible

A point such as \((15,21)\) has both coordinates composite but is not a vertex of \(G\). Every visited point must satisfy both the compositeness disjunction and coprimality.

### 5.4 Composite waypoints do not suffice

Making every turning point composite-composite does not guarantee that the straight segments are admissible. Every intermediate point on the segment must be visible. If the fixed coordinate of a segment is prime, every prime value of the varying coordinate creates a forbidden prime-prime point.

A safe sufficient condition is that the fixed coordinate of each segment is composite, but coprimality along the entire segment remains nontrivial.

### 5.5 Sparse deletion is not harmless

Prime-prime points have zero density, but they may occupy strategically important “turning” locations. One cannot infer that the known infinite component survives their deletion.

### 5.6 Long composite intervals are not corridors

The existence of arbitrarily long runs of consecutive composite integers is elementary, but such intervals do not directly provide a path. If a fixed coordinate has small prime factors, most or all candidate unit moves may be blocked by gcd conditions.

### 5.7 Arbitrarily long paths versus a ray

Paths of every finite length somewhere in \(H\) do not imply a ray. To invoke König’s lemma, the paths must originate at one fixed vertex or lie in one fixed connected component.

Similarly, finite-box “giant components” need not be nested or compatible.

### 5.8 Planar barrier arguments require correct duality

A visually closed loop of forbidden lattice vertices is not automatically a vertex cut because of corner contacts and the distinction between site and edge duality. Any computational or theoretical barrier claim should be checked directly as a vertex-separation statement, preferably by max-flow/min-cut or exhaustive neighbor verification.

### 5.9 Small-index prime inequalities

Any use of asymptotic prime estimates must separately handle initial primes. The Stewart construction specifically begins in the safe stated range \(k\ge4\).

### 5.10 Optional monotonicity must not be silently assumed

The target path may move west or south and may revisit coordinate levels, though it must be simple under the standard ray formulation. Restricting to north-east paths can be useful, but failure in that restricted class is not a disproof.

---

## 6. Verification hooks

All computations should use the predicate
\[
\operatorname{allowed}(x,y)
\iff
x,y\ge2,\quad \gcd(x,y)=1,\quad
(\neg\operatorname{prime}(x)\lor \neg\operatorname{prime}(y)).
\]

For admissible vertices, compositeness can be certified by a nontrivial factor of at least one coordinate. For rigorous large computations, prime claims should use deterministic primality tests or primality certificates.

### 6.1 Finite-box graph exploration

For \(N\ge2\), construct
\[
H_N=H[\{2,\dots,N\}^2].
\]
Compute:

- connected components;
- largest component size;
- components touching each side of the box;
- shortest paths between selected boundary sets;
- degree distribution;
- articulation points and narrow cutsets.

A component touching the box boundary is not known to be infinite. A component not touching the boundary is a rigorously certified finite component, provided all four external neighbors of its listed vertices have been checked.

### 6.2 Annulus-crossing tests

For \(2\le r<R\), test whether \(H\) restricted to \([2,R]^2\) connects
\[
\{(x,y):\max(x,y)\le r\}
\]
to
\[
\{(x,y):\max(x,y)=R\}.
\]
Repeat with multiple inner seeds and with rectangular annuli. Record whether crossings use narrow arithmetic bottlenecks.

For monotone paths, dynamic programming suffices: mark a vertex reachable from a seed if its west or south neighbor is reachable. For unrestricted paths, use BFS.

### 6.3 Rooted depth tests

Fix several admissible roots \(v\). Search for self-avoiding paths of length \(L\), or more cheaply for vertices at graph distance \(L\). Increasing distances in expanding boxes provide evidence for a large component. To support a König-lemma strategy, the root must remain fixed.

### 6.4 Local detours around prime-prime points

For each pair of distinct primes \(p,q\le B\):

1. construct the induced admissible graph in
   \[
   [p-R,p+R]\times[q-R,q+R];
   \]
2. choose pairs of admissible “entry” and “exit” points that would be adjacent through \((p,q)\) in an unmodified corridor;
3. determine the minimum detour radius and length;
4. optionally require the detour to be monotone.

Classify failures by:

- parity;
- divisibility of \(p\pm a\) by factors of \(q\pm b\);
- local prime constellations.

The growth of the maximum required detour radius is a direct test of the prime-ladder repair route.

### 6.5 Search for composite-anchor staircases

Search for increasing sequences \(a_n,b_n\) satisfying
\[
\gcd(t,b_n)=1\quad
(a_n\le t\le a_{n+1}),
\]
and
\[
\gcd(a_{n+1},t)=1\quad
(b_n\le t\le b_{n+1}),
\]
with \(b_n\) and \(a_{n+1}\) composite. These conditions make the horizontal-then-vertical L-shaped connector admissible.

Record:

- lengths of available horizontal and vertical runs;
- smallest prime factors of the fixed composite coordinates;
- whether odd composite anchors dominate;
- whether a directed graph of such anchor states has long paths or cycles with positive drift.

### 6.6 Leaf stripping and robust-core experiments

In \(H_N\), iteratively remove vertices of degree \(0\) or \(1\). Repeat with different treatments of the outer boundary:

- optimistic: boundary vertices may connect outside;
- pessimistic: all outside connections are deleted.

A persistent large core would suggest robust connectivity. Its disappearance does not prove the absence of a ray, since a ray itself need not survive iterative finite leaf stripping.

### 6.7 Barrier search

Use SAT, integer programming, or backtracking to search for rectangular or irregular vertex cuts consisting entirely of disallowed points. A candidate blocked point must satisfy either:

- \(\gcd(x,y)>1\), with an explicit common divisor; or
- \(x,y\) are both prime.

For a proposed barrier, verify separation by direct graph search or a vertex-cut computation rather than visual inspection. Search separately for:

- barriers around a fixed target;
- families with scalable CRT descriptions;
- nested barriers.

---

## 7. Attack routes

### Route 1: Repair the Stewart prime ladder by arithmetic detours

**Core mechanism.**  
Begin with the monotone Stewart path connecting consecutive prime pairs and replace every forbidden prime-prime vertex by a visible admissible detour.

**Needed key lemma.**  
A sufficiently uniform local-detour theorem: whenever a monotone visible corridor meets a prime-prime point \((p,q)\), there is a compatible admissible path around it inside a controlled rectangle, with entry and exit points suitable for concatenation. The control may be absolute, depend mildly on \(p,q\), or be bounded relative to the neighboring prime gaps.

**Why it might work.**  
Prime-prime points are sparse, and their immediate axis-neighbors usually have an even composite coordinate. The underlying Stewart corridor is already monotone and visible, so only the additional deletion must be repaired.

**Most likely failure point.**  
Parity destroys the obvious one-cell detour: corners such as \((p-1,q+1)\) are even-even. Larger detours may require nearby odd composite values in prescribed residue classes. A uniform detour lemma could conceal difficult statements about prime constellations or simultaneous divisibility avoidance. Separate detours may also overlap or force backward motion.

**Quick blockage test.**  
For all prime pairs up to a large bound, compute the minimum admissible monotone detour radius for standard corridor entry/exit configurations. If the required radius grows with prime gaps or repeatedly fails in structured parity classes, a bounded-template approach is blocked.

---

### Route 2: Build a staircase whose fixed coordinates are composite

**Core mechanism.**  
Construct increasing composite sequences
\[
a_0<a_1<a_2<\cdots,\qquad
b_0<b_1<b_2<\cdots
\]
and concatenate L-shaped paths
\[
(a_n,b_n)\to(a_{n+1},b_n)\to(a_{n+1},b_{n+1}).
\]
If \(b_n\) is composite, every point on the horizontal segment satisfies the compositeness condition. If \(a_{n+1}\) is composite, every point on the vertical segment does as well.

**Needed key lemma.**  
An infinite extension lemma producing \(a_{n+1},b_{n+1}\) such that
\[
\gcd(t,b_n)=1
\quad\text{for every }t\in[a_n,a_{n+1}],
\]
and
\[
\gcd(a_{n+1},t)=1
\quad\text{for every }t\in[b_n,b_{n+1}],
\]
while the relevant anchors remain composite and both coordinates tend to infinity.

**Why it might work.**  
This route removes primes from the avoidance condition entirely: the fixed coordinate on each segment is composite. CRT constructions, numbers with large least prime factor, and carefully chosen odd composite anchors may permit short safe intervals.

**Most likely failure point.**  
Consecutive coprimality is stringent. If a fixed coordinate is even, no nontrivial segment in the corresponding direction is possible. Even for odd composites, every prime factor creates a forbidden residue class, and CRT naturally forces divisibility rather than avoidance over whole intervals. Recursive choices may eventually leave no legal extension.

**Quick blockage test.**  
Construct the finite directed state graph of admissible L-shaped transitions below \(B\). Measure whether long directed paths persist and whether required increments increase rapidly. Test prime powers, semiprimes with large least prime factor, and odd squarefree anchors separately.

---

### Route 3: Arithmetic block crossings and deterministic renormalization

**Core mechanism.**  
Tile a large region into boxes. Define a box to be “good” if \(H\) contains prescribed horizontal and vertical crossings joining robust port sets. Prove that good boxes form an infinite connected chain.

**Needed key lemma.**  
A uniform block-crossing theorem, possibly after choosing favorable translates:
for all sufficiently large scales, a positive proportion of boxes have compatible admissible crossings, with enough quantitative control to force an infinite chain rather than isolated good boxes.

Potential tools include Möbius inversion for coprimality, sieve estimates, averaging over translations, and second-moment bounds.

**Why it might work.**  
Admissible vertices have density \(6/\pi^2\), and the prime-prime deletion has zero density. Large boxes empirically may contain many alternate routes, so connectivity could be robust at a coarse scale.

**Most likely failure point.**  
Density does not imply crossing. Visibility events have strong arithmetic correlations along rows and columns. Averaged existence of many good boxes does not ensure they connect, and importing an independent percolation threshold is unjustified.

**Quick blockage test.**  
For many translated \(L\times L\) boxes, compute robust left-right and bottom-top crossings, including the number and width of disjoint crossings. Build the adjacency graph of good boxes. If crossing rates do not stabilize or good boxes occur in arithmetic clusters separated by systematic bad strips, naive renormalization is unlikely to work.

---

### Route 4: A rooted extension tree and sieve-controlled branching

**Core mechanism.**  
Fix one admissible root. Consider the finitely branching tree whose nodes are self-avoiding admissible path prefixes. Prove that this tree has nodes at every depth, then apply König’s lemma.

Rather than constructing a rigid geometric corridor, maintain several possible frontier states so that arithmetic obstructions in one branch can be avoided by another.

**Needed key lemma.**  
A branching extension theorem: every sufficiently advanced “good” path prefix, or at least one among a controlled family of prefixes, has an extension that makes definite outward progress while preserving enough future options. Quantitatively, bad extensions caused by gcd or prime-prime obstructions must not cover all available branches.

**Why it might work.**  
The problem asks for only one path. Allowing many competing candidate prefixes may avoid the need for a uniform local template. Sieve estimates might show that among many possible turns, at least one is arithmetically clean.

**Most likely failure point.**  
The path history creates self-avoidance and geometric dependencies, while arithmetic obstructions are highly correlated. A positive average branching factor is not enough: rare bottlenecks could kill every branch. Paths of arbitrary length with varying roots would also be useless.

**Quick blockage test.**  
From a fixed root, perform bounded-depth exhaustive or beam search while recording the number of viable frontier states after quotienting by a local-state description. If all branches repeatedly collapse at specific modular configurations, identify whether those configurations can be excluded by an invariant.

---

### Route 5: Planar connectivity and exclusion of large arithmetic cutsets

**Core mechanism.**  
Use planarity to show that an infinite admissible component must exist unless the disallowed set forms sufficiently many separating dual barriers. Then prove that such barriers cannot occur at all large scales because every long candidate separator must contain an admissible opening.

**Needed key lemma.**  
A quantitative “no closed barrier” statement: every sufficiently large dual circuit, or every member of a suitably chosen family of annular separators, contains a point through which \(H\) crosses. This would likely require simultaneous control of gcd obstructions and prime-prime sites along long curves.

**Why it might work.**  
The lattice is planar, and the admissible set has positive density. Connectivity can sometimes be attacked more effectively through the geometry of separators than by constructing a path directly.

**Most likely failure point.**  
The invisible set itself has density \(1-6/\pi^2\), is highly structured, and may support long divisibility barriers. A count of admissible points on a curve does not ensure that one is connected to both sides. Site/dual topology also has corner subtleties.

**Quick blockage test.**  
Compute minimum admissible vertex cuts between inner and outer boundaries of increasing annuli. Track whether cut sizes grow, remain bounded, or admit simple CRT descriptions. Small recurring cutsets would undermine a robust-connectivity strategy.

---

### Route 6: Disproof by CRT-generated trapping barriers

**Core mechanism.**  
Attempt to construct closed circuits or rectangular boundaries consisting entirely of disallowed points, using shared prime factors to make most boundary points invisible and prime-prime points to fill residual holes. If such barriers can be nested around every admissible point, every component is finite.

**Needed key lemma.**  
A scalable barrier theorem: for every sufficiently large target region, or for every admissible starting point, one can place a finite closed vertex cut around it such that each point of the cut either has nontrivial gcd or is a prime-prime pair. The family must cover all starts, not merely specially chosen locations.

**Why it might work.**  
The Chinese remainder theorem can create arbitrary finite runs in which prescribed integers have prescribed small divisors. Long segments of nonvisible lattice points are therefore plausible. Factorial-type constructions and covering congruences may generate pieces of walls.

**Most likely failure point.**  
Constructing one blocked line segment is much easier than constructing four compatible sides of a closed barrier. Coordinates are shared along a side, CRT conditions can conflict at corners, and visible openings may be unavoidable. Barriers placed at rare special locations do not trap arbitrary starting points.

**Quick blockage test.**  
Use a constraint solver to search for fully blocked rectangular annuli around many targets, first using only gcd obstructions and then allowing prime-prime sites. Determine whether minimal barrier thickness and distance grow uncontrollably, and inspect whether all successful examples rely on special target congruences.

---

## 8. Verdict on difficulty

This is a genuinely open, elementary-looking arithmetic connectivity problem. The known monotone path in the full visible-point graph is simple, but the deletion of prime-prime vertices interacts badly with parity and with the row-by-row divisibility structure. The main difficulty is not scarcity of admissible vertices—their density remains \(6/\pi^2\)—but proving that local admissibility can be maintained coherently forever.

No standard equivalence to a famous conjecture such as the twin-prime conjecture, Goldbach’s conjecture, or Hardy–Littlewood is known. The problem should therefore not be advertised as equivalent to one of those conjectures. However, several tempting uniform-detour approaches could accidentally demand unproved control of prime constellations or prime gaps. Any such hidden implication must be isolated explicitly.

The unrestricted problem is likely substantially more approachable than the bounded-direction-change variant, but it still requires a global mechanism: a recursive arithmetic construction, a robust infinite-component theorem, or a universal trapping theorem. Finite computations are valuable for identifying parity bottlenecks, detour templates, and candidate invariants, but cannot by themselves settle the question.