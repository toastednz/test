# Problem brief: Erdős Problem #103

## 1. Precise statement

For an integer \(n\ge 1\), let  
\[
\mathcal C_n=\{X\subset \mathbb R^2: |X|=n,\ \|x-y\|\ge 1\text{ for all distinct }x,y\in X\}.
\]
For a nonempty finite set \(X\subset\mathbb R^2\), define its diameter by
\[
\operatorname{diam}(X)=\max_{x,y\in X}\|x-y\|.
\]
Define the optimal diameter
\[
D_n=\min_{X\in\mathcal C_n}\operatorname{diam}(X).
\]
The minimum exists: for example, \(n\) collinear points at unit spacing give \(D_n\le n-1\), and after translating one point to the origin, all configurations with diameter at most \(n-1\) lie in a compact set.

Two finite sets \(X,Y\subset\mathbb R^2\) are **congruent** if there is a Euclidean isometry \(T\), possibly orientation-reversing, such that \(T(X)=Y\). The points are unordered.

Let
\[
\mathcal M_n=\{X\in\mathcal C_n:\operatorname{diam}(X)=D_n\},
\]
and define
\[
h(n)=|\mathcal M_n/\!\cong|,
\]
the number of congruence classes of optimal configurations. If there are infinitely many classes, write \(h(n)=\infty\).

The problem asks:

> Is it true that
> \[
> h(n)\longrightarrow\infty\qquad(n\to\infty)?
> \]

The standard meaning is:
\[
\forall k\in\mathbb N\ \exists N\in\mathbb N\ \forall n\ge N,\qquad h(n)\ge k.
\]
This is stronger than mere unboundedness or \(\limsup h(n)=\infty\).

### Equivalent normalized formulation

For \(n\ge2\), define
\[
s_n=\max_{\substack{X\subset\mathbb R^2,\ |X|=n\\ \operatorname{diam}(X)\le1}}
\min_{x\ne y}\|x-y\|.
\]
Then
\[
D_n=\frac1{s_n}.
\]
Thus the problem concerns the number of incongruent optimal max–min packings in an arbitrary planar set of diameter \(1\).

### Ambiguities and standard conventions

1. **Congruence:** The standard convention includes reflections. Restricting to orientation-preserving isometries changes counts by at most a factor of two and does not affect divergence to infinity.
2. **Unordered sets:** Labelings are not counted. Counting labeled configurations would introduce artificial factorial multiplicities and would not be the intended open problem.
3. **Infinite moduli:** An optimal family may conceivably have continuously many incongruent members. Such a value is treated as \(h(n)=\infty\).
4. **Meaning of \(h(n)\to\infty\):** The standard eventual lower-bound interpretation above is intended, not merely unboundedness along a subsequence.

For fixed \(n\), the set of squared distance vectors of optimal labeled configurations is semialgebraic. Consequently, after quotienting by the finite relabeling action, \(h(n)\) is either finite or there are continuum many congruence classes; a merely countably infinite family cannot arise from a semialgebraic moduli space.

---

## 2. What counts as a solution

### A complete affirmative solution

A proof must establish
\[
\forall k\ge1\ \exists N(k)\ \forall n\ge N(k),\qquad h(n)\ge k.
\]

It is enough to prove any explicit lower bound
\[
h(n)\ge f(n)
\]
for all sufficiently large \(n\), where \(f(n)\to\infty\). It would also suffice to prove that \(h(n)=\infty\) for every sufficiently large \(n\).

For each claimed family of minimizers, a complete proof must establish:

1. **Feasibility:** Every pair of distinct points is at distance at least \(1\).
2. **Common diameter:** The stated diameter is correct.
3. **Global optimality:** No feasible \(n\)-point configuration has smaller diameter.
4. **Incongruence:** The configurations represent distinct unordered congruence classes.
5. **Eventual quantifier:** The construction or argument works for every sufficiently large \(n\), not only for infinitely many \(n\).

A proof need not determine \(D_n\) or \(h(n)\) exactly if it supplies enough certified optimal configurations.

### A complete disproof

The negation of \(h(n)\to\infty\) is
\[
\exists k\ge1\ \forall N\ \exists n\ge N,\qquad h(n)<k.
\]
Equivalently, there must be a constant \(B<\infty\) and an infinite sequence \(n_j\to\infty\) such that
\[
h(n_j)\le B.
\]

Thus a single \(n\) with \(h(n)=1\), or even finitely many such \(n\), is not a counterexample.

A complete disproof would need, for infinitely many explicitly or rigorously characterized values \(n_j\):

1. the exact optimal diameter \(D_{n_j}\);
2. an exhaustive classification of all configurations attaining \(D_{n_j}\);
3. proof that there are at most \(B\) congruence classes, uniformly in \(j\).

An “explicit counterexample” must therefore be an infinite family of orders \(n_j\), together with a global optimality and completeness argument—not merely an explicit optimal configuration at one order.

---

## 3. What does not count

None of the following resolves the problem:

1. Proving \(h(n)\) is unbounded along a subsequence.
2. Proving \(\limsup h(n)=\infty\).
3. Constructing many feasible configurations of the same diameter without proving that diameter equals \(D_n\).
4. Constructing many local minima or jammed packings.
5. Producing exponentially many labeled versions of one unordered point set.
6. Counting rotations, translations, or reflections as different configurations.
7. Constructing many asymptotically optimal configurations whose diameters are \(D_n+o(1)\) or \((1+o(1))D_n\).
8. Improving the asymptotic estimate for \(D_n\).
9. Proving \(h(n)\ge2\) for infinitely many \(n\), or even for all sufficiently large \(n\). The latter would be major progress but is far weaker than \(h(n)\to\infty\).
10. Giving a conditional result based on an unproved finite crystallization, rigidity, or uniqueness conjecture.
11. Finding an infinitesimal flex without proving that it integrates to actual feasible configurations of exactly the same optimal diameter.
12. Showing that one \(h(n)\) is infinite; the required conclusion concerns every sufficiently large \(n\).
13. Numerical evidence, even very high precision, without exact feasibility, global lower bounds, and exhaustive classification.

---

## 4. Known results and context

### 4.1 Status from the database

The problem is open. According to the supplied commentary:

> It is not even known whether \(h(n)\ge2\) for all sufficiently large \(n\).

Thus even eventual nonuniqueness is open, while the desired conclusion asks for arbitrarily large multiplicity uniformly for all large \(n\).

The database also cross-references Problem #99, but no statement or commentary for that problem was supplied, so no precise implication should be inferred here.

### 4.2 Elementary facts

- \(D_n\) is nondecreasing in \(n\).
- \(D_n\to\infty\).
- For \(n\ge2\), every optimal configuration has minimum pairwise distance exactly \(1\). Otherwise, uniformly scaling it down would reduce its diameter while preserving the lower-distance constraint after suitable scaling.
- Small cases:
  \[
  D_1=0,\qquad h(1)=1;
  \]
  \[
  D_2=1,\qquad h(2)=1;
  \]
  \[
  D_3=1,\qquad h(3)=1,
  \]
  with the unique minimizer for \(n=3\) being the unit equilateral triangle.
- For \(n\ge4\), \(D_n>1\), since at most three points in \(\mathbb R^2\) can be pairwise at distance exactly \(1\).

There is no known monotonicity relation for \(h(n)\).

### 4.3 Asymptotic order of \(D_n\)

The optimal diameter is well understood to first order:
\[
D_n=\sqrt{\frac{2\sqrt3}{\pi}}\,\sqrt n+O(1).
\]

One way to obtain the lower bound is Oler’s finite packing inequality. If \(K=\operatorname{conv}(X)\) for a set \(X\) with mutual distances at least \(1\), then
\[
|X|\le \frac{2}{\sqrt3}\operatorname{area}(K)
+\frac12\operatorname{perimeter}(K)+1.
\]
If \(\operatorname{diam}(K)=D\), the isodiametric and perimeter–diameter inequalities give
\[
\operatorname{area}(K)\le \frac{\pi D^2}{4},
\qquad
\operatorname{perimeter}(K)\le \pi D.
\]
Hence
\[
n\le \frac{\pi}{2\sqrt3}D^2+\frac{\pi}{2}D+1.
\]
This gives
\[
D_n\ge \sqrt{\frac{2\sqrt3}{\pi}}\,\sqrt n-O(1).
\]

For the matching upper bound, take points of the unit triangular lattice inside a sufficiently large disk and retain any \(n\) of them. The lattice has density \(2/\sqrt3\), yielding
\[
D_n\le \sqrt{\frac{2\sqrt3}{\pi}}\,\sqrt n+O(1).
\]

These asymptotics say essentially nothing about the exact number of minimizers. Exact multiplicity is controlled by boundary-scale and rigidity phenomena invisible in the leading term.

### 4.4 Contact and diameter graphs

For a feasible configuration \(X\), define:

- the **contact graph**
  \[
  G_1(X)=\{\{x,y\}:\|x-y\|=1\};
  \]
- the **diameter graph**
  \[
  G_D(X)=\{\{x,y\}:\|x-y\|=\operatorname{diam}(X)\}.
  \]

Useful structural facts include:

1. The straight-line contact graph is planar. Two unit edges with disjoint endpoints cannot cross in their interiors under the mutual-distance-\(\ge1\) condition.
2. Every vertex of the contact graph has degree at most \(6\), by the planar kissing-number argument.
3. If a point has six unit-distance neighbors, those neighbors occur at angular spacing exactly \(60^\circ\), forming a regular hexagonal local pattern.
4. By the Hopf–Pannwitz theorem, the diameter graph of \(n\) planar points has at most \(n\) edges.

These bounds constrain active constraints, but they do not force flexibility: contact and diameter constraints together can easily provide enough equations to isolate an optimal framework.

### 4.5 Semialgebraic formulation

Using squared distances, define
\[
q_{ij}=\|x_i-x_j\|^2.
\]
For a proposed squared diameter \(z\), feasibility is the polynomial system
\[
1\le q_{ij}\le z \qquad(1\le i<j\le n).
\]
After fixing translation, for example \(x_1=(0,0)\), the relevant search region is compact. Therefore, for every fixed \(n\), the problem is in principle decidable by quantifier elimination over the reals. The number \(D_n^2\) is a real algebraic number.

This is a theoretical decidability statement, not a practical algorithm for large \(n\).

---

## 5. Traps and edge cases

### 5.1 Unordered versus labeled configurations

Permuting labels does not create a new solution. A large count obtained from labelings is irrelevant.

Two unlabeled point sets are congruent exactly when there exists a bijection between them preserving every pairwise distance. The multiset of pairwise distances alone is not always a complete congruence invariant; one must compare the complete edge-weighted graphs up to vertex permutation.

### 5.2 Reflections

Mirror images are congruent under the standard definition. Chiral pairs must not be counted twice.

### 5.3 A single infinite \(h(n)\) is insufficient

Even if one order \(n\) admits a continuous family of optimal configurations, this does not imply anything about \(h(m)\) for larger \(m\).

### 5.4 Minimum enclosing circle is a different objective

This problem is not the usual packing of \(n\) equal disks in a smallest circular container. It minimizes the maximum center-to-center distance, not the radius of a smallest enclosing disk.

Jung’s theorem relates the two quantities, but they are not equivalent optimization problems. A finite set of diameter \(D\) has circumradius between \(D/2\) and \(D/\sqrt3\), depending on its geometry.

Equivalently, one may place radius-\(1/2\) disks around the points; the union then has diameter \(D+1\). But the union is not required to lie in a circular container.

### 5.5 Deletion and insertion are not automatically optimality-preserving

Deleting a point from an optimal \((n+1)\)-point configuration gives a feasible \(n\)-point configuration, but its diameter may exceed \(D_n\), or deletion may remove all diameter pairs and lower the diameter. Thus no direct monotonicity of \(h(n)\) follows.

Similarly, adding a point while preserving the old diameter does not prove optimality for the larger order.

### 5.6 Density does not imply exact crystallization

Thue’s theorem and Oler’s inequality determine the leading density, but do not imply that finite minimizers are subsets of a triangular lattice. Boundary rearrangements can affect the exact optimum.

### 5.7 Rigidity-counting pitfalls

A simple comparison between the number of variables and the number of active constraints is not decisive:

- active constraints can be dependent;
- an infinitesimal flex may be obstructed at second order;
- inequalities have one-sided tangent conditions;
- a nontrivial flex may change the diameter;
- a KKT point need not be globally optimal.

Conversely, failure of infinitesimal rigidity does not by itself produce a continuum of optimal configurations.

### 5.8 “Same diameter” does not imply “optimal”

Multiple configurations having the same diameter \(D\) contribute to \(h(n)\) only after proving \(D=D_n\).

### 5.9 Numerical equality is especially dangerous

Distinct candidate arrangements can have diameters differing by extremely small amounts. Apparent ties in floating-point optimization are not evidence of exact multiplicity.

---

## 6. Verification hooks

The following computations can rigorously support intermediate work.

### 6.1 Exact feasibility predicate

For fixed \(n\) and \(z\), encode
\[
\operatorname{Feas}_n(z):
\quad
\exists x_1,\dots,x_n\in\mathbb R^2\
\forall i<j,\quad
1\le\|x_i-x_j\|^2\le z.
\]
Set \(x_1=(0,0)\) to remove translations. One may also put \(x_2=(r,0)\), \(r\ge0\), to remove rotation.

Quantifier elimination can decide this for very small \(n\) and algebraic \(z\). Interval branch-and-bound can produce certified infeasibility below a candidate \(z\), provided the entire compact search domain is covered.

### 6.2 Active-graph enumeration

For a candidate optimum, classify pairs as:

- contact edges: \(q_{ij}=1\);
- diameter edges: \(q_{ij}=z\);
- inactive pairs: \(1<q_{ij}<z\).

Enumerate planar contact graphs with maximum degree \(6\), and diameter graphs with at most \(n\) edges. For each combined active graph:

1. solve the polynomial equalities;
2. test all inactive inequalities;
3. compute the rigidity rank;
4. quotient solutions by graph isomorphism and congruence.

This is useful only if the graph enumeration is exhaustive.

### 6.3 Congruence testing

For exact or interval-certified coordinates, form the complete squared-distance matrix. Two configurations are congruent as unordered sets if and only if some permutation \(P\) satisfies
\[
Q_Y=P Q_X P^{\mathsf T}.
\]
Use exact algebraic comparison or disjoint certified intervals. Merely comparing sorted lists of distances is insufficient.

### 6.4 Tangent-cone test for flexes

At a configuration \(X=(x_i)\) of fixed diameter \(D\), let \(v_i\) be velocity vectors. For a contact edge \(ij\),
\[
(x_i-x_j)\cdot(v_i-v_j)\ge0;
\]
for a diameter edge \(ij\),
\[
(x_i-x_j)\cdot(v_i-v_j)\le0.
\]
After removing the three-dimensional space of infinitesimal Euclidean motions, solve the resulting linear feasibility problem.

A nontrivial tangent vector is a useful signal, but a nonlinear continuation or second-order analysis is still required to obtain an actual family of minimizers.

### 6.5 Rattler detection

For each point \(x_i\), keep all other points fixed and compute
\[
R_i=\{p\in\mathbb R^2:
\|p-x_j\|\ge1\text{ and }\|p-x_j\|\le D
\text{ for all }j\ne i\}.
\]
If \(R_i\) contains a nontrivial arc or open set and some diameter pair not involving \(i\) remains fixed, then moving \(x_i\) may produce continuously many configurations of the same diameter. One must check that the resulting configurations are not all congruent, for example by exhibiting a varying pairwise distance.

### 6.6 Triangular-lattice subset enumeration

For a normalized triangular lattice, enumerate \(n\)-element subsets of a sufficiently large finite lattice patch, quotienting by lattice symmetries. Compute:

- exact squared diameter;
- contact graph;
- number of diameter pairs;
- deletion and boundary-flip orbits.

This can test lattice-shell conjectures, though it cannot rule out superior nonlattice configurations without a separate global lower bound.

### 6.7 Certification of a proposed optimum

A fully certified candidate requires both:

- an exact feasible realization of diameter \(D\);
- a proof that \(\operatorname{Feas}_n(z)\) is false for every \(z<D^2\).

Possible lower-bound tools include exact quantifier elimination, interval exhaustion, geometric case analysis, or exact polynomial/SOS certificates where applicable.

---

## 7. Attack routes

### Route 1: Exact triangular-lattice crystallization and boundary multiplicity

**Core mechanism.**  
Show that optimal configurations are triangular-lattice clusters, then exploit multiple inequivalent choices of boundary sites with the same diameter.

**Key lemma needed.**  
A theorem of the following strength:
for every sufficiently large \(n\), some globally optimal \(n\)-point configuration is a subset of a unit triangular lattice, and the set of optimal lattice subsets contains \(f(n)\to\infty\) inequivalent boundary patterns.

A weaker but still sufficient version could identify an exact class of lattice-window configurations and prove they attain \(D_n\).

**Why it might work.**  
The leading asymptotic density is exactly triangular-lattice density. A disk-like cluster has \(O(\sqrt n)\) boundary sites, and incomplete outer shells may admit many combinatorially distinct occupations without changing the extreme pair distance.

**Most likely failure point.**  
Infinite-density optimality does not imply exact finite crystallization. Small boundary displacements can beat every literal lattice subset, and distinct boundary patterns usually have slightly different diameters rather than exact ties. Also, a subsequence of shell orders would not establish the required result for all large \(n\).

**Quick blocking test.**  
For moderate \(n\), enumerate optimal triangular-lattice subsets and compare their diameters with high-quality continuous nonlinear optimizers. If nonlattice configurations repeatedly improve the lattice candidates, the route requires a much subtler crystallization statement.

---

### Route 2: Rattlers and continuous optimal moduli

**Core mechanism.**  
Find an optimal configuration containing a point or subframework that can move continuously while all distances remain in \([1,D_n]\) and at least one fixed pair continues to realize \(D_n\). This would give
\[
h(n)=\infty.
\]

**Key lemma needed.**  
For every sufficiently large \(n\), there exists a globally optimal configuration with a genuine noncongruent finite flex at fixed diameter. A strong version would guarantee an interior “rattler” whose feasible region has positive dimension.

**Why it might work.**  
Diameter is controlled by extreme pairs, while many interior points do not directly affect it. An optimal packing may have slack regions or local defects even when its boundary is diameter-tight.

**Most likely failure point.**  
Globally optimal packings may be fully jammed. Near-maximal density encourages triangular local coordination, and one-sided distance constraints can obstruct every finite motion even when linearized constraint counts suggest flexibility.

**Quick blocking test.**  
On computed candidate minimizers, calculate the fixed-\(D\) tangent cone after removing rigid motions, then perform certified nonlinear continuation. If all candidates are first- and second-order jammed, the simple rattler version is blocked.

---

### Route 3: Capacity plateaus and deletion multiplicity

Define
\[
N(D)=\max\{|X|:X\subset\mathbb R^2,\ 
\min_{x\ne y}\|x-y\|\ge1,\ 
\operatorname{diam}(X)\le D\}.
\]
Then
\[
D_n=\inf\{D:N(D)\ge n\}.
\]

**Core mechanism.**  
If many consecutive orders share the same optimal diameter and arise by deleting points from one larger optimal configuration, inequivalent deletion patterns could generate many optimal configurations.

**Key lemma needed.**  
There are sufficiently wide blocks
\[
D_a=D_{a+1}=\cdots=D_b
\]
covering all large orders in a controlled way, and some optimal \(b\)-point configuration has many deletion orbits that retain diameter \(D_a\).

**Why it might work.**  
At a diameter threshold, the maximal capacity may jump by more than one. A large symmetric threshold configuration can have many inequivalent subsets while preserving a diameter pair.

**Most likely failure point.**  
The sequence \(D_n\) may be strictly increasing for most or all large \(n\). Even on a plateau, deleting points can remove all diameter-realizing pairs, and different deletion patterns may not be optimal for the smaller order.

**Quick blocking test.**  
Compute rigorous or high-precision values of \(D_n\) for the accessible range and search for exact repeated values. Enumerate deletion orbits from candidate threshold configurations and test whether their diameter remains unchanged.

---

### Route 4: Active-graph exchange and discrete multiplicity

**Core mechanism.**  
Use the combined unit-contact and diameter graph as an inequality framework. Prove that sufficiently large optimal frameworks contain many independent local circuits admitting two distinct realizations with the same active lengths and the same global diameter.

**Key lemma needed.**  
An “exchange lemma” stating that every sufficiently large optimal active framework—or at least one optimal framework for every large \(n\)—contains \(r(n)\to\infty\) disjoint flippable subframeworks, with flips preserving every inactive inequality and global optimality.

Independent flips could yield \(2^{r(n)}\) configurations before quotienting by symmetry.

**Why it might work.**  
The contact graph is planar with degree at most \(6\), while the diameter graph has at most \(n\) edges. Large disk-like packings have long boundaries where local combinatorial alternatives may occur.

**Most likely failure point.**  
Triangular contact networks can be highly rigid, and diameter inequalities can remove otherwise available flips. An alternative algebraic realization of the active equations may violate a previously inactive distance inequality. Local exchange also does not itself prove global optimality.

**Quick blocking test.**  
Enumerate active graphs of numerical minimizers, identify small circuits with multiple realizations, and verify all inactive inequalities by interval arithmetic. If all active frameworks are globally rigid and stress-stable, this route is blocked in its naive form.

---

### Route 5: Topology of the first feasible configuration space

Let
\[
F_n(D)=
\left\{
(x_1,\dots,x_n):
1\le\|x_i-x_j\|\le D\text{ for }i<j
\right\}/E(2),
\]
with a further quotient by \(S_n\) for unordered configurations.

**Core mechanism.**  
Study the topology of \(F_n(D)\) as \(D\) decreases to its first nonempty value \(D_n\). Attempt to force many inequivalent global-minimum strata using topology, stratified Morse theory, or configuration-space invariants.

**Key lemma needed.**  
A lower bound tending to infinity on the number of unordered \(E(2)\)-orbits in the first nonempty level \(F_n(D_n)\), derived from topology just above \(D_n\).

**Why it might work.**  
Hard-particle configuration spaces have complicated topology, and critical configurations are controlled by contact or stress graphs. The birth of feasibility at \(D_n\) may require many distinct balanced critical frameworks.

**Most likely failure point.**  
Complicated topology above the threshold does not force many global minima; all topology could be created at larger \(D\). Labeled configuration spaces also contain artificial multiplicity from permutations and braiding that disappears after quotienting.

**Quick blocking test.**  
For small \(n\), compute approximate persistent homology or stratified critical graphs as \(D\) varies. If \(F_n(D_n)\) appears to be a single orbit while topology arises only later, the required global-minimum theorem is unlikely.

---

### Route 6: Disproof through bounded uniqueness on a shell subsequence

**Core mechanism.**  
Identify an infinite sequence of “closed-shell” values \(n_j\) for which the optimal configuration is unique, or belongs to a uniformly bounded finite list.

**Key lemma needed.**  
There exist \(B<\infty\) and \(n_j\to\infty\) such that every optimal \(n_j\)-point configuration is congruent to one of \(B\) explicitly described rigid configurations.

This requires exact optimality and exhaustive classification, not merely a plausible canonical candidate.

**Why it might work.**  
At special orders, a highly symmetric disk-like packing may close a boundary shell and eliminate defects. Exact finite packing problems often have isolated optimizers at special sizes.

**Most likely failure point.**  
The natural “closed shells” of the triangular lattice are hexagonal rather than circular and are not expected to be globally optimal for diameter at large scale. Boundary rearrangements may produce several or continuously many competitors. Proving global uniqueness for infinitely many growing finite packings would itself be exceptionally difficult.

**Quick blocking test.**  
Select candidate magic orders suggested by lattice or numerical optimization, then search exhaustively for alternative active graphs and boundary rearrangements. Repeated discovery of distinct exact or near-exact competitors would undermine the uniqueness hypothesis.

---

## 8. Verdict on difficulty

This is a very difficult exact finite-packing problem. The database’s observation that eventual \(h(n)\ge2\) is not known shows that the requested conclusion is far beyond current basic multiplicity results.

The leading asymptotic behavior of \(D_n\) follows from classical packing theory, but this does not address \(h(n)\). The problem depends on exact boundary geometry, global rigidity, possible finite crystallization, and exact ties between competing arrangements. Those are precisely the features least controlled by density theorems.

There is no established equivalence to a famous named conjecture based on the supplied information. However, an approach that tries to prove all large minimizers are triangular-lattice clusters would require a very strong finite crystallization theorem, substantially deeper than Thue’s theorem on asymptotic packing density. Conversely, a disproof via uniqueness on infinitely many orders would require an unprecedented uniform classification of exact planar packing optima.

The most promising computationally testable possibility is the existence of flexible optimal configurations or boundary flips, because one such mechanism could produce many—or continuously many—minimizers without requiring a complete classification. The main obstacle remains global optimality: generating alternatives is much easier than proving they attain \(D_n\).