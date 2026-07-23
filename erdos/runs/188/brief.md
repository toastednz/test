# Problem brief: Erdős Problem #188

## 1. Precise statement

Let \(\|\cdot\|_2\) denote Euclidean norm on \(\mathbb R^2\). A red/blue coloring is an arbitrary function
\[
c:\mathbb R^2\to\{\mathrm R,\mathrm B\}.
\]
No measurability, periodicity, definability, or other regularity is assumed.

For an integer \(k\ge 2\), a **unit-step \(k\)-term arithmetic progression** is a set, or equivalently an ordered sequence,
\[
P(x,u,k)=\{x,x+u,x+2u,\ldots,x+(k-1)u\},
\]
where \(x\in\mathbb R^2\) and \(u\in\mathbb R^2\) satisfies \(\|u\|_2=1\). Thus consecutive terms, not the two endpoints, are at distance \(1\).

Define \(A(k)\) to be the assertion that there exists a coloring \(c\) satisfying both:

1. **Red unit-distance avoidance**
   \[
   \forall x,y\in\mathbb R^2,\quad
   \|x-y\|_2=1\implies
   \neg(c(x)=\mathrm R\ \wedge\ c(y)=\mathrm R).
   \]

2. **Blue unit-step progression avoidance**
   \[
   \forall x\in\mathbb R^2\ \forall u\in\mathbb R^2,\quad
   \|u\|_2=1\implies
   \exists i\in\{0,\ldots,k-1\}\ \ c(x+iu)=\mathrm R.
   \]
   Equivalently, no \(P(x,u,k)\) is entirely blue.

The problem asks for
\[
K=\min\{k\ge 2:A(k)\},
\]
if this set is nonempty. If \(A(k)\) fails for every finite \(k\), the correct answer is that no such \(k\) exists, which one may denote by \(K=\infty\).

### Equivalent set formulation

Writing
\[
R=c^{-1}(\mathrm R),\qquad B=\mathbb R^2\setminus R,
\]
one seeks a set \(R\subseteq\mathbb R^2\) such that

- \(R\) is an independent set in the unit-distance graph:
  \[
  r,r'\in R\implies \|r-r'\|_2\ne 1;
  \]
- \(R\) intersects every unit-step \(k\)-term progression:
  \[
  R\cap P(x,u,k)\ne\varnothing
  \quad\text{for all }x\in\mathbb R^2,\ \|u\|_2=1.
  \]

Thus \(R\) must simultaneously be unit-distance-avoiding and a transversal for all straight unit-step paths of \(k\) vertices.

### Monotonicity

If \(A(k)\) holds, then \(A(\ell)\) holds for every \(\ell\ge k\), using the same coloring: every \(\ell\)-term progression contains a \(k\)-term initial subprogression. Hence the admissible values of \(k\), if any, form an upper interval.

On every fixed orbit
\[
\{x+nu:n\in\mathbb Z\},\qquad \|u\|_2=1,
\]
the red indices form a subset of \(\mathbb Z\) with:

- no two consecutive indices;
- no gap containing \(k\) consecutive blue indices.

Equivalently, consecutive red indices along such an orbit have differences between \(2\) and \(k\). The difficulty is enforcing this simultaneously for every base point and every direction.

### Ambiguity in the historical wording

The standard reading, and the one intended here, is that the common-difference vector \(u\) has norm \(1\). Two alternative readings must be distinguished:

- If “distance \(1\)” meant that the endpoints of the progression are distance \(1\), then the common difference would have norm \(1/(k-1)\). This is a different problem.
- Erdős and Graham’s printed formulation apparently forbade blue arithmetic progressions of arbitrary common difference. Under that stronger requirement, no finite \(k\) works; see Section 4.

The present problem uses unit common difference.

---

## 2. What counts as a solution

### Exact finite answer

To prove that the answer is a particular finite integer \(K\), one must establish both:

1. **Upper bound:** \(A(K)\) holds. That is, construct or otherwise prove the existence of a coloring of all of \(\mathbb R^2\) satisfying both global conditions.
2. **Matching lower bound:** \(A(K-1)\) fails. By monotonicity this implies failure for every smaller \(k\).

Since the published lower bound is \(K\ge 6\), a valid construction for \(k=6\), together with a correct invocation or reproduction of Tsaturian’s theorem, would settle the problem with \(K=6\).

A construction for \(k=10^7\), for example, would be a major result because it would prove that \(K\) is finite, but it would not determine the smallest \(k\) unless accompanied by matching lower bounds.

### Proving that no finite \(k\) exists

A complete negative resolution must prove
\[
\forall k\ge2\ \forall c:\mathbb R^2\to\{\mathrm R,\mathrm B\},
\]
either \(c\) has a red unit-distance pair or it has an all-blue unit-step \(k\)-term progression.

Equivalently, every coloring with no red unit-distance pair must contain blue unit-step progressions of every finite length.

### What a valid explicit coloring must satisfy

An explicit coloring for a given \(k\) must:

- assign a color to every point of \(\mathbb R^2\), including all boundary points of any regions used;
- prove, for every pair \(x,y\), that if both are red then \(\|x-y\|_2\ne1\);
- prove, for every \(x\in\mathbb R^2\) and every unit vector \(u\), that at least one of
  \[
  x,x+u,\ldots,x+(k-1)u
  \]
  is red.

Finite sampling, numerical evidence, or verification only for a dense set of points does not establish these universal statements.

### What a valid nonexistence proof for fixed \(k\) may look like

For fixed \(k\), Boolean compactness implies that \(A(k)\) fails if and only if there is a finite obstruction.

Concretely, a finite obstruction consists of:

- a finite point set \(V\subset\mathbb R^2\);
- selected unit-distance pairs \(E\subseteq\binom V2\);
- selected unit-step \(k\)-progressions \(\mathcal P\subseteq\binom Vk\);

such that every red/blue coloring of \(V\) either colors both endpoints of some \(e\in E\) red or colors all vertices of some \(P\in\mathcal P\) blue.

Using Boolean variables \(r_v\), meaning “\(v\) is red,” the clauses are
\[
\neg r_v\lor\neg r_w
\quad\text{for each }\{v,w\}\in E,
\]
and
\[
\bigvee_{v\in P}r_v
\quad\text{for each }P\in\mathcal P.
\]
An exact unsatisfiability proof for this formula, together with exact verification of all claimed geometric incidences, proves \(\neg A(k)\).

A SAT certificate alone is insufficient if the coordinates or distance/progression relations were only computed numerically.

### Counterexamples to intermediate claims

- To refute a claim that \(A(k)\) is impossible, one must give a global coloring satisfying \(A(k)\).
- To refute a proposed explicit coloring, it suffices to exhibit either:
  - two specified red points exactly unit distance apart, or
  - specified \(x,u\), with \(\|u\|_2=1\), for which all \(x+iu\), \(0\le i<k\), are blue.
  
Such a defect only refutes that particular construction; it does not prove \(\neg A(k)\).

---

## 3. What does not count

The following do not resolve the problem:

1. **A nonmatching bound.**  
   Proving \(K\ge7\) or constructing a coloring for some large \(k\) is progress but does not determine the smallest \(k\) unless the bounds meet.

2. **A coloring of a lattice or countable dense subset.**  
   A coloring of \(\mathbb Z^2\), the triangular lattice, \(\mathbb Q^2\), or any fixed countable subset does not color all of \(\mathbb R^2\).

3. **Checking only finitely many directions.**  
   Progressions occur in every direction \(u\in S^1\), not merely horizontal, vertical, or lattice directions.

4. **Checking only finitely many translations.**  
   The initial point \(x\) is arbitrary.

5. **A measurable-only impossibility theorem.**  
   The problem permits nonmeasurable colorings. Proving that no measurable coloring works does not prove \(\neg A(k)\). Conversely, a measurable construction is fully valid if it satisfies the pointwise conditions.

6. **Almost-everywhere assertions.**  
   It is not enough that almost every unit pair avoids red-red or almost every progression contains red. A single exceptional forbidden configuration invalidates the coloring.

7. **Random or heuristic evidence.**  
   A random construction must be converted into a rigorous existence argument covering uncountably many constraints.

8. **A numerical periodic pattern without boundary analysis.**  
   Exact unit distances often occur on tile boundaries. Every boundary point must receive a color, and all boundary cases must be proved.

9. **Replacing “distance exactly \(1\)” with “distance at least \(1\).”**  
   Red points may be closer than \(1\); only exact distance \(1\) is forbidden. Packing arguments that assume minimum separation \(1\) impose a much stronger condition.

10. **Forbidding progressions of arbitrary common difference.**  
    That is a different and already negatively settled formulation. Its van der Waerden argument does not force common difference \(1\).

11. **A bounded-box computation.**  
    Satisfiability or unsatisfiability in one finite box, without a valid compactness obstruction or extension theorem, is not a plane result.

12. **A conditional result.**  
    A proof depending on an unresolved conjecture is not a complete solution unless that conjecture is proved as part of the argument.

---

## 4. Known results and context

### Published lower bounds

According to the database commentary:

- Erdős, Graham, Montgomery, Rothschild, Spencer, and Straus [EGMRSS75] proved
  \[
  K\ge5.
  \]
- Tsaturian [Ts17] improved this to
  \[
  K\ge6.
  \]

Thus it is known that \(A(k)\) fails for every \(k\le5\). In particular, a complete solution cannot have \(K<6\).

No rigorous finite upper bound is supplied by the database. Erdős and Graham stated that \(K\le 10{,}000{,}000\), “more or less,” but gave no proof. This should not be treated as a theorem. On the current record, even the existence of some finite admissible \(k\) remains unsettled.

### The unrestricted-common-difference version

Suppose instead that one asks for a coloring with no red unit-distance pair and no blue \(k\)-term arithmetic progression of any common difference. Then no finite \(k\) works.

Fix \(x\in\mathbb R^2\) and a unit vector \(u\), and consider
\[
x+\mathbb Zu.
\]
Let
\[
B=\{n\in\mathbb Z:c(x+nu)=\mathrm B\}.
\]
If there is no red unit-distance pair, then whenever \(n\notin B\), the point at \(n+1\) must be blue. Define a two-coloring of \(\mathbb Z\) by whether \(n\in B\).

By van der Waerden’s theorem, for every \(m\) there is an \(m\)-term integer arithmetic progression
\[
a,a+d,\ldots,a+(m-1)d
\]
whose indices are all in \(B\) or all outside \(B\).

- If they are all in \(B\), the corresponding plane points are a blue progression.
- If they are all outside \(B\), they are all red, so their shifts
  \[
  a+1,a+d+1,\ldots,a+(m-1)d+1
  \]
  all belong to \(B\), again giving a blue progression.

The resulting common-difference vector is \(du\), of norm \(d\), not generally \(1\). Hence this argument settles the unrestricted version but not the present problem.

### Unit-distance graph context

Let \(G_{\mathrm{unit}}\) be the graph on \(\mathbb R^2\) joining points at distance \(1\). The red set must be an independent set in \(G_{\mathrm{unit}}\). The problem is therefore related to the Hadwiger–Nelson problem, but ordinary proper colorings of the unit-distance graph do not directly solve it: the complement of one independent color class may contain arbitrarily long unit-step straight paths.

The known bounds \(5\le\chi(\mathbb R^2)\le7\) likewise do not determine \(K\).

### Compactness

The Boolean compactness theorem is especially relevant. For fixed \(k\), all constraints are finite clauses involving point colors. Therefore:

- if no global coloring exists, some finite subfamily of constraints is already inconsistent;
- if every finite subfamily is satisfiable, a global coloring exists, possibly highly nonconstructive.

This gives both a concrete route to lower bounds through finite obstructions and a possible nonconstructive route to an upper bound through a theorem that all finite systems are satisfiable.

---

## 5. Traps and edge cases

1. **Common difference versus total length.**  
   A \(k\)-term unit-step progression has total endpoint distance \(k-1\), not \(1\).

2. **Exact distance only.**  
   Red-red distances below or above \(1\) are allowed.

3. **All orientations count.**  
   The sequences with steps \(u\) and \(-u\) represent the same unoriented progression, but both are included harmlessly by the quantifiers.

4. **Nonconsecutive terms.**  
   In a unit-step progression, terms \(i\) and \(j\) are at distance \(|i-j|\). Only consecutive terms are unit-distance pairs. Consequently red points can occur in the same progression at index separation at least \(2\).

5. **Linewise solutions do not globalize automatically.**  
   On one unit-spaced line, the alternating pattern
   \[
   \mathrm R,\mathrm B,\mathrm R,\mathrm B,\ldots
   \]
   satisfies both local conditions for every \(k\ge2\). Any obstruction must use interactions among multiple directions.

6. **Small \(k\).**
   - If \(k=2\), both red and blue would have to be independent in the unit-distance graph. An equilateral unit triangle makes this impossible.
   - If one allows \(k=1\), “no blue one-term progression” forces every point red, which immediately fails. Usually arithmetic progressions are only considered for \(k\ge2\) or \(k\ge3\); this convention does not affect the known lower bound \(K\ge6\).

7. **Monotonicity direction.**  
   A coloring avoiding blue \(k\)-term progressions also avoids all longer ones. It need not avoid shorter ones.

8. **Tile boundaries.**  
   Periodic stripe or polygon constructions often fail only at boundaries. Declaring boundaries red can create unit red pairs; declaring them blue can create all-blue progressions.

9. **Sampling cannot rule out exact equalities.**  
   A numerical search may miss a unit pair or progression occurring at a special algebraic angle.

10. **Compactness is not a finite search bound.**  
    If \(\neg A(k)\), some finite obstruction exists, but compactness gives no useful bound on its size or coordinate complexity.

11. **A finite lattice obstruction is sufficient, but lattice satisfiability is not.**  
    An unsatisfiable finite configuration embedded in the plane proves nonexistence. A satisfiable coloring of every tested lattice says little about arbitrary off-lattice constraints.

12. **Density arguments require care.**  
    The coloring can be nonmeasurable. Translation-invariant means or finite averaging certificates may sometimes replace Lebesgue measure, but ordinary integration cannot simply be assumed.

---

## 6. Verification hooks

### 6.1 Exact SAT encoding for finite configurations

For a finite exact coordinate set \(V\):

1. Create one Boolean variable \(r_v\) per point.
2. For every exactly verified unit pair \(\{v,w\}\), add
   \[
   \neg r_v\lor\neg r_w.
   \]
3. For every exactly verified unit-step \(k\)-progression
   \[
   v_i=x+iu,\qquad \|u\|_2=1,
   \]
   add
   \[
   r_{v_0}\lor\cdots\lor r_{v_{k-1}}.
   \]
4. Run a SAT solver.
5. If unsatisfiable, produce a DRAT/LRAT-style certificate and independently verify it.
6. Separately verify all coordinates, squared distances, collinearity, and equal-step relations exactly, preferably in a specified algebraic number field.

An unsatisfiable core is especially valuable because it may expose a human-readable geometric gadget.

### 6.2 Configuration generation

Useful exact families include:

- points obtained by repeated intersections of unit circles;
- equilateral-triangle and rhombus extensions;
- points \(x+iu\) explicitly added to complete progression clauses;
- finite unions of rotated or reflected gadgets;
- algebraic unit vectors such as
  \[
  (1,0),\quad (0,1),\quad
  \left(\frac{a}{c},\frac{b}{c}\right),\ a^2+b^2=c^2,
  \]
  and vectors in quadratic number fields.

Numerical coordinates should only guide discovery; final verification must be symbolic.

### 6.3 One-dimensional consistency checks

Enumerate binary words with:

- no substring \(\mathrm{RR}\);
- no substring \(\mathrm B^k\).

For periodic candidate colorings, enumerate cyclic words as well. These checks are only necessary conditions, but they quickly catch errors in claimed behavior along chosen directions.

### 6.4 Verification of periodic constructions

Suppose \(R\) is periodic under a lattice \(\Lambda\), with red set \(R_0\) specified in a fundamental domain. The two required torus conditions are:

\[
\forall r,s\in R_0\ \forall\lambda\in\Lambda,\qquad
\|r-s+\lambda\|_2\ne1,
\]
and
\[
\forall x\in\mathbb R^2/\Lambda\ \forall u\in S^1,\qquad
\exists i\in\{0,\ldots,k-1\}:x+iu\pmod\Lambda\in R_0.
\]

If \(R_0\) is semialgebraic with algebraic data, these become real-quantifier problems. Only finitely many lattice translates can be relevant to the first condition. Cylindrical algebraic decomposition, exact SMT, or certified interval subdivision may be applicable.

A robust numerical precursor should seek positive margins:

- all red-red difference sets remain a definite distance from the unit circle;
- every unit-step \(k\)-chain hits the interior of the red region by a definite margin.

Without margins, discretization is unreliable.

### 6.5 Adversarial search against proposed constructions

For a proposed periodic \(R\), numerically optimize over
\[
(x_1,x_2,\theta)\in(\mathbb R^2/\Lambda)\times[0,2\pi)
\]
to find a chain
\[
x+i(\cos\theta,\sin\theta),\qquad 0\le i<k,
\]
that avoids \(R\). Candidate failures should then be converted to exact or certified interval witnesses.

Separately search the red-red difference set
\[
(R-R)+\Lambda
\]
for intersections with the unit circle.

### 6.6 LP and counting certificates

For finite \(V\), introduce real variables \(0\le r_v\le1\). Add:

- progression inequalities
  \[
  \sum_{v\in P}r_v\ge1;
  \]
- independent-set inequalities for finite unit-distance subgraphs \(Q\):
  \[
  \sum_{v\in Q}r_v\le\alpha(G_{\mathrm{unit}}[Q]).
  \]

If a nonnegative linear combination yields a contradiction, it gives a short exact lower-bound certificate. If the LP is feasible but the SAT instance is not, the integrality gap indicates that purely density-based methods are too weak for that configuration.

---

## 7. Attack routes

### Route 1: Finite geometric obstruction and exact SAT

**Core mechanism.** Search for a finite family of unit pairs and unit-step \(k\)-progressions with no admissible red transversal.

**Key lemma needed.** For the target \(k\), construct a finite \(V\subset\mathbb R^2\) such that every independent set in the unit-distance graph on \(V\) misses at least one selected \(k\)-progression.

**Why it might work.** Boolean compactness guarantees that every genuine nonexistence result has some finite witness. The known lower bounds are naturally compatible with finite-gadget methods.

**Most likely failure point.** The smallest obstruction may be enormous or require geometries not generated by standard unit-circle closures. SAT instances can remain satisfiable for all tractable configurations even when a distant finite obstruction exists.

**Quick blockage test.** Generate progressively larger exact configurations from unit-circle intersections and progression completions. If SAT remains easily satisfiable and the solutions stabilize into a repeatable local pattern, the current gadget family is probably structurally inadequate rather than merely too small.

---

### Route 2: Periodic semialgebraic construction

**Core mechanism.** Find a lattice-periodic red set \(R\) on a torus that is unit-distance-avoiding and intersects every length-\(k\) unit orbit segment.

**Key lemma needed.** Construct a torus subset \(R_0\) satisfying
\[
((R_0-R_0)+\Lambda)\cap S^1=\varnothing
\]
and
\[
\forall x\in\mathbb R^2/\Lambda,\ \forall u\in S^1,\quad
\{x,x+u,\ldots,x+(k-1)u\}\cap R_0\ne\varnothing.
\]

**Why it might work.** The alleged \(10^7\) upper bound suggests that Erdős and Graham may have had a coarse geometric or periodic construction in mind. Large \(k\) allows sparse but uniformly unavoidable red regions.

**Most likely failure point.** A periodic red set may have an exceptional direction and phase whose entire finite orbit segment avoids it. Exact unit-distance avoidance between different translates, especially on boundaries, is another severe constraint.

**Quick blockage test.** Optimize adversarially over \((x,\theta)\) for increasingly long blue chains. If chain lengths grow rapidly with the torus resolution or align with rational/near-rational torus directions, the candidate lacks a uniform hitting property.

---

### Route 3: Compactness plus a finite independent-transversal theorem

**Core mechanism.** Prove directly that for some universal \(k\), every finite subsystem of the plane constraints is satisfiable. Compactness would then give a global coloring without an explicit formula.

**Key lemma needed.** There exists a finite \(k\) such that for every finite \(V\subset\mathbb R^2\), the unit-distance graph on \(V\) has an independent set meeting every unit-step \(k\)-progression contained in \(V\).

**Why it might work.** This exactly matches the finite form of the problem and could exploit geometric restrictions on finite unit-distance graphs and collinear paths. It avoids having to build a regular coloring of the continuum.

**Most likely failure point.** General independent-transversal theorems usually require bounded degree, large hyperedges relative to neighborhoods, or pseudorandomness. Finite unit-distance graphs can have very large degree, and progression hyperedges can overlap heavily.

**Quick blockage test.** On adversarial finite configurations, compare greedy, local-search, and integer-programming solutions as \(k\) grows. If the minimum \(k\) required by finite examples appears unbounded, this route may instead be producing evidence for \(K=\infty\).

---

### Route 4: Averaging, fractional bounds, and LP duality

**Core mechanism.** Combine lower bounds forced by progression hitting with upper bounds on the size of independent sets in finite unit-distance configurations.

**Key lemma needed.** Find weighted finite configurations for which:
- every \(k\)-progression requires a total red weight of at least \(1\);
- unit-distance independence gives a strictly smaller global upper bound on red weight.

Equivalently, find a Farkas-dual combination of valid inequalities yielding \(0\ge\varepsilon>0\).

**Why it might work.** It can compress a very large combinatorial obstruction into a symmetric counting proof and can use fractional chromatic or independence-ratio information from unit-distance graphs.

**Most likely failure point.** The relevant contradiction may be intrinsically integral. Fractional red assignments can satisfy all linear inequalities even when no Boolean coloring exists. Known unit-distance independence bounds may also be too weak.

**Quick blockage test.** Run LP and SAT on the same exact configuration. A persistent large LP/SAT gap means that density or fractional-chromatic arguments alone are unlikely to reach the desired lower bound.

---

### Route 5: Hierarchical or probabilistic geometric construction

**Core mechanism.** Build the red set at multiple scales, using random shifts or hierarchical tilings so that every unit-step chain is hit while potential red unit pairs are eliminated or repaired.

**Key lemma needed.** A finite-scale construction with uniform positive margins, plus an extension or limiting theorem ensuring that:
- every chain is eventually forced to meet a stable red region;
- no later modification creates a red pair at exact distance \(1\).

A local-lemma-type finite theorem followed by compactness is another possible implementation.

**Why it might work.** Exact-distance avoidance is less restrictive than minimum-separation packing, and multiscale randomness may destroy long coherent blue chains in all directions.

**Most likely failure point.** There are uncountably many chains, so probability-one statements for each fixed chain do not automatically hold uniformly. Repairing red unit pairs can open new arbitrarily long blue chains, and exact equality is not a robust event under limits.

**Quick blockage test.** Simulate finite torus approximations at several scales and search continuously for worst-case chains. If the longest blue chain grows with scale rather than stabilizing, there is no evidence of a uniform \(k\).

---

### Route 6: Disproof via geometric Ramsey amplification

**Core mechanism.** Prove that every unit-distance-independent red set leaves arbitrarily long unit-step blue progressions. Construct, for each \(k\), a finite family of \(k\)-chains such that any choice of one red point from each chain forces a red unit pair.

**Key lemma needed.** A recursive geometric gadget that transforms forcing data for shorter chains into a forcing family for longer chains, or otherwise gives finite unsatisfiable configurations for every \(k\).

**Why it might work.** There is presently no proved finite upper bound. The unrestricted version is impossible by van der Waerden, and a sufficiently strong multidirectional synchronization phenomenon could restore an analogous conclusion for unit steps.

**Most likely failure point.** Along every individual line, alternating red-blue patterns avoid arbitrarily long blue runs. The proof must therefore synchronize many directions, and there may in fact be a global construction defeating every proposed forcing gadget.

**Quick blockage test.** Search for unsatisfiable finite instances for increasing \(k\), while attempting to identify a repeatable substitution rule in the unsatisfiable cores. If obstruction size grows without reusable structure and SAT solutions become more periodic, the amplification hypothesis is weak.

---

## 8. Verdict on difficulty

This is a very difficult open problem. The present rigorous information is only
\[
K\ge6,
\]
with no proved finite upper bound in the supplied record. Therefore the problem is not merely asking which of several nearby integers is correct: it is not even established that \(K<\infty\).

A proof of any finite upper bound would already be substantial. An exact solution would additionally require matching that construction with a lower bound. A proof that \(K=\infty\) would overturn the unproved Erdős–Graham expectation and require a new geometric Ramsey mechanism unavailable from ordinary one-dimensional van der Waerden theory.

The problem is related to the Hadwiger–Nelson problem, finite unit-distance graphs, independent transversals, and van der Waerden-type Ramsey theory, but it is not known to be equivalent to a standard famous conjecture. Results about the chromatic number of the plane do not by themselves settle it. The central difficulty is the simultaneous control of every translation and every unit direction under completely arbitrary, possibly nonmeasurable colorings.