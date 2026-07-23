# Problem Brief: Erdős Problem #217

## 1. Precise statement

Let \(n\) be a positive integer, and let \(P\subset \mathbb R^2\) be a set of \(n\) distinct points.

For \(r>0\), define the multiplicity of the distance \(r\) in \(P\) by
\[
\mu_P(r)
=
\#\bigl\{\{p,q\}\subset P:p\neq q,\ \|p-q\|=r\bigr\},
\]
where pairs are unordered. Let
\[
\Delta(P)=\{\|p-q\|:p,q\in P,\ p\neq q\}
\]
be the set of distinct positive distances determined by \(P\).

The required general-position conditions are:

1. **No three collinear:** every three distinct points of \(P\) are affinely independent.
2. **No four concyclic:** no four distinct points of \(P\) lie on a common Euclidean circle.

The problem asks for a complete characterization of the integers \(n\) for which there exists such a set \(P\) satisfying
\[
|\Delta(P)|=n-1
\]
and such that there is a bijection
\[
\delta:\{1,\dots,n-1\}\longrightarrow \Delta(P)
\]
with
\[
\mu_P(\delta(i))=i
\qquad (1\le i\le n-1).
\]

Equivalently, the multiset of distance multiplicities is exactly
\[
\{\mu_P(r):r\in\Delta(P)\}=\{1,2,\dots,n-1\}.
\]
This is arithmetically consistent because
\[
1+2+\cdots +(n-1)=\binom n2,
\]
the total number of unordered pairs of points.

### Interpretation of “in some ordering”

The phrase “in some ordering of the distances” means an arbitrary relabeling of the distinct distances. It does **not** mean that the \(i\)-th smallest distance must occur \(i\) times. Thus the condition concerns only the multiplicity multiset, not the numerical ordering of the distance values.

### Domain convention

The nontrivial problem begins at \(n\ge 2\).

- If \(n=1\) is admitted, the condition is vacuously true: there are no distances and the required ordering is empty.
- For \(n=2\), the unique distance occurs once.
- The database discussion starts at \(n=4\), evidently because \(n=2,3\) are immediate.

Hence, under the literal positive-integer convention, \(n=1\) is a vacuous affirmative case; under the usual nontrivial convention, study \(n\ge2\).

---

## 2. What counts as a solution

Because this is a classification question rather than a single yes/no assertion, a complete solution must determine the entire set
\[
\mathcal N=\{n\ge2:\text{a configuration satisfying all conditions exists}\}.
\]

A complete result therefore requires both:

1. **Existence for every claimed affirmative \(n\):**  
   Supply a construction, or invoke a fully proved construction theorem, and verify:
   - there are exactly \(n\) distinct points;
   - no three are collinear;
   - no four are concyclic;
   - there are exactly \(n-1\) distinct distances;
   - their multiplicities are exactly \(1,2,\dots,n-1\).

2. **Nonexistence for every remaining \(n\):**  
   Prove that every \(n\)-point planar set satisfying the two general-position conditions fails the prescribed distance-multiplicity condition.

For example, proving that configurations exist for \(2\le n\le8\) and that none exist for \(n\ge9\) would completely solve the problem.

### Requirements for an explicit construction

If coordinates \(p_j=(x_j,y_j)\) are proposed, verification must be exact. One must prove:

- For all triples \(a,b,c\),
  \[
  \det
  \begin{pmatrix}
  x_a&y_a&1\\
  x_b&y_b&1\\
  x_c&y_c&1
  \end{pmatrix}\neq0.
  \]
- For all quadruples \(a,b,c,d\),
  \[
  \det
  \begin{pmatrix}
  x_a^2+y_a^2&x_a&y_a&1\\
  x_b^2+y_b^2&x_b&y_b&1\\
  x_c^2+y_c^2&x_c&y_c&1\\
  x_d^2+y_d^2&x_d&y_d&1
  \end{pmatrix}\neq0.
  \]
- The \(\binom n2\) squared distances
  \[
  (x_a-x_b)^2+(y_a-y_b)^2
  \]
  split into exactly \(n-1\) equality classes of sizes \(1,\dots,n-1\), with distinct values between different classes.

Floating-point agreement is not sufficient. Algebraic coordinates, certified intervals, exact symbolic identities, or another rigorous certification are needed.

### What would disprove Erdős’s eventual-nonexistence belief?

The database records Erdős’s belief that configurations are impossible for all sufficiently large \(n\). To disprove that belief, one must construct configurations for arbitrarily large \(n\), equivalently for an unbounded sequence of \(n\). A single example at \(n=9\), or at any one larger value, would enlarge the known affirmative set but would not disprove eventual nonexistence.

---

## 3. What does not count

The following do not resolve the classification problem:

- Constructing one additional example, such as \(n=9\), without addressing larger \(n\).
- Proving nonexistence only for a finite range, such as \(9\le n\le100\).
- Proving eventual nonexistence without settling the finitely many values below the threshold.
- Showing merely that at least \(n-1\), at most \(n-1\), or approximately \(n\) distances occur.
- Producing the correct number \(n-1\) of distances but not the exact multiplicity spectrum \(1,\dots,n-1\).
- Producing the multiplicity spectrum while allowing three collinear or four concyclic points.
- Conditional results depending on an unproved distinct-distance conjecture.
- Dimension counts, probabilistic heuristics, or numerical optimization without rigorous certification.
- Approximate equalities of distances.
- Constructions in \(\mathbb R^3\), on a sphere, or in a non-Euclidean metric.
- Assuming the distances are ordered increasingly; that is a different, stronger problem.
- Proving \(h(n)\ge n\) on a subsequence only, unless all remaining \(n\) are separately resolved.

Deletion is not a valid monotonicity argument: deleting a point changes several distance multiplicities, so an example for \(n\) does not automatically produce one for \(n-1\). Likewise, nonexistence for one \(n\) says nothing immediate about larger \(n\).

---

## 4. Known results and context

### 4.1 Affirmative values from the supplied record

The supplied commentary gives constructions for
\[
n=4,5,6,7,8.
\]

The trivial small cases give \(n=2,3\), and \(n=1\) under the empty-distance convention. Thus the known affirmative range is
\[
2\le n\le8.
\]

The supplied record gives no affirmative or negative result for any \(n\ge9\); these should be treated as unresolved unless the cited literature reveals more.

### 4.2 Small explicit examples

#### \(n=2\)

Any two distinct points work: the unique distance occurs once.

#### \(n=3\)

A non-equilateral isosceles triangle works. For example,
\[
(-1,0),\quad (1,0),\quad (0,2).
\]
The base has length \(2\), while the two equal sides have length \(\sqrt5\). Thus the multiplicities are \(1,2\).

#### \(n=4\)

The database’s “isosceles triangle with the point in the centre” is most naturally read as a non-equilateral isosceles triangle together with its circumcenter.

An exact example is
\[
A=(-1,0),\quad B=(1,0),\quad C=(0,2),\quad O=\left(0,\frac34\right).
\]
Here \(O\) is the circumcenter of \(\triangle ABC\). The distances are

- \(AB=2\), occurring once;
- \(AC=BC=\sqrt5\), occurring twice;
- \(OA=OB=OC=\frac54\), occurring three times.

The three values are distinct. No three selected points are collinear, and the four are not concyclic because \(A,B,C\) lie on their circumcircle while its center \(O\) does not.

### 4.3 Historical constructions

According to the supplied commentary:

- Erdős initially believed no example existed for \(n\ge5\).
- Pomerance constructed an example for \(n=5\), described in \([{\rm Er83c}]\).
- Palásti constructed an example for \(n=7\) in \([{\rm Pa87}]\).
- Palásti constructed an example for \(n=6\) with the additional property of containing no equilateral triangle, in \([{\rm Pa89}]\).
- Palásti constructed an example for \(n=8\) in \([{\rm Pa89b}]\).

The no-equilateral condition is not part of Problem #217. The commentary’s wording concerning Erdős’s question about five points and Palásti’s six-point construction should be checked against the original source: a six-point example does not literally answer a five-point existence question by deletion.

### 4.4 The auxiliary function \(h(n)\)

The commentary refers to the standard general-position distinct-distance function
\[
h(n)=\min\{|\Delta(P)|: |P|=n,\ P\subset\mathbb R^2,\ 
P\text{ has no three collinear and no four concyclic}\}.
\]

Any configuration in this problem has \(n-1\) distinct distances, so it implies
\[
h(n)\le n-1.
\]
Consequently,
\[
h(n)\ge n
\]
implies nonexistence for that \(n\). In particular, the conjectural statement
\[
h(n)\ge n\quad\text{for all sufficiently large }n
\]
would prove Erdős’s eventual-nonexistence belief.

The converse is false: \(h(n)\le n-1\) does not guarantee the very special multiplicity spectrum \(1,\dots,n-1\).

### 4.5 Elementary structural facts

For each distance \(r\), define the distance graph \(G_r\) on vertex set \(P\), joining \(p\) and \(q\) when \(\|p-q\|=r\). Then:

1. \(|E(G_r)|=\mu_P(r)\).
2. Every vertex of \(G_r\) has degree at most \(3\). Indeed, four neighbors at distance \(r\) from one point would be four points on the circle of radius \(r\) centered at that point.
3. Therefore
   \[
   \mu_P(r)\le \left\lfloor\frac{3n}{2}\right\rfloor.
   \]
   This does not contradict the required maximum multiplicity \(n-1\).
4. \(G_r\) contains no \(K_{2,3}\): two distinct circles of the same radius have at most two common intersection points.
5. An equilateral triangle, i.e. a monochromatic \(K_3\), is allowed by the original problem.
6. A distance graph should not be assumed planar; its straight-line edges may cross.

The degree bound yields the elementary general-position estimate
\[
h(n)\ge
\left\lceil
\frac{\binom n2}{\lfloor 3n/2\rfloor}
\right\rceil,
\]
which is only about \(n/3\), far short of \(h(n)\ge n\).

### 4.6 Moment identities forced by the spectrum

The required multiplicities give, for every \(k\ge1\),
\[
\sum_{r\in\Delta(P)}\binom{\mu_P(r)}k
=
\sum_{i=1}^{n-1}\binom ik
=
\binom n{k+1}.
\]

In particular,
\[
\sum_r \binom{\mu_P(r)}2=\binom n3.
\]
Thus there must be exactly \(\binom n3\) unordered pairs of distinct point-pairs having the same length. Also,
\[
\sum_r\mu_P(r)^2
=
\sum_{i=1}^{n-1}i^2
=
\frac{n(n-1)(2n-1)}6.
\]
These exact identities may be more exploitable than merely knowing that there are \(n-1\) distances.

---

## 5. Traps and edge cases

1. **Arbitrary ordering, not increasing ordering.**  
   The distance occurring once need not be the shortest, and the distance occurring \(n-1\) times need not be the longest.

2. **The spectrum is global.**  
   A distance class of size \(i\) may be distributed across many components of \(G_r\); it need not form a star, path, cycle, or connected graph.

3. **No four concyclic does not mean no three concyclic.**  
   Every noncollinear triple is concyclic.

4. **Equilateral triangles are permitted.**  
   Only Palásti’s strengthened \(n=6\) example excludes them.

5. **A central-point construction stops being automatic after \(n=4\).**  
   If a selected center is equidistant from four other selected points, those four outer points are concyclic, violating the hypothesis.

6. **No monotonicity in \(n\).**  
   Neither existence nor nonexistence obviously passes between adjacent values.

7. **Dimension counting is not a proof.**  
   A prescribed partition into \(n-1\) distance classes imposes
   \[
   \binom n2-(n-1)=\frac{(n-1)(n-2)}2
   \]
   equality constraints. This exceeds the generic configuration-space dimension for \(n\ge6\), yet examples exist for \(n=6,7,8\). The equalities can have substantial algebraic dependence.

8. **Symmetric constructions often violate general position.**  
   Regular polygons, lattices, and points on one circle typically produce many concyclic quadruples or collinear triples.

9. **Perturbation destroys exact distance equalities.**  
   General position can usually be obtained by perturbation, but the required multiplicities cannot generally survive arbitrary perturbation.

10. **Numerical clusters are not exact equality classes.**  
    Near-equal distances do not count.

11. **Squared distances are preferable algebraically.**  
    Since all distances are positive, equality of distances is equivalent to equality of squared distances; using squared distances avoids radicals.

12. **The no-four-concyclic determinant also vanishes on some degenerate configurations.**  
    Collinearity must be controlled separately.

---

## 6. Verification hooks

### 6.1 Exact candidate checker

Given exact or certified algebraic coordinates:

1. Compute every squared distance \(d_{ab}^2\).
2. Partition the \(\binom n2\) pairs by exact equality.
3. Check that class sizes, sorted numerically as integers, are
   \[
   1,2,\dots,n-1.
   \]
4. Check all \(\binom n3\) collinearity determinants.
5. Check all \(\binom n4\) concyclicity determinants.
6. Verify the moment identities
   \[
   \sum m_i=\binom n2,\qquad
   \sum\binom{m_i}{2}=\binom n3,\qquad
   \sum m_i^2=\frac{n(n-1)(2n-1)}6.
   \]

For algebraic coordinates, use exact number-field arithmetic, minimal polynomials plus isolating intervals, or Sturm-sequence sign determination.

### 6.2 Abstract edge-coloring enumeration

Encode the complete graph \(K_n\) with colors \(1,\dots,n-1\), where color \(i\) must occur exactly \(i\) times. Add necessary constraints:

- every color has maximum degree at most \(3\);
- no color contains a \(K_{2,3}\);
- color labels may be fixed by multiplicity, eliminating most color-permutation symmetry;
- quotient by vertex relabeling.

A SAT, CP-SAT, or integer-programming search can enumerate combinatorially admissible patterns for \(n=9\) and perhaps \(n=10\). These constraints are necessary but not sufficient for Euclidean realizability.

### 6.3 Polynomial realizability system

For a fixed edge-coloring, introduce point coordinates \((x_j,y_j)\) and one squared-distance variable \(s_i\) for each color. Impose
\[
(x_a-x_b)^2+(y_a-y_b)^2=s_i
\]
whenever edge \(ab\) has color \(i\).

Normalize Euclidean similarity, for example,
\[
p_1=(0,0),\qquad p_2=(1,0),\qquad y_3>0.
\]
Then add:

- \(s_i>0\);
- \(s_i\neq s_j\) for \(i\neq j\);
- all collinearity determinants nonzero;
- all concyclicity determinants nonzero.

Possible tools include Gröbner bases, resultants, homotopy continuation followed by interval certification, cylindrical algebraic decomposition for reduced systems, and sum-of-squares or Positivstellensatz certificates for real infeasibility.

### 6.4 Saturation for nonvanishing constraints

For algebraic infeasibility, combine all required nonzero expressions into a product \(D\) and introduce a variable \(z\) with
\[
zD-1=0.
\]
This algebraically excludes solutions where distinct distance values collapse or where general position fails. A Gröbner-basis certificate that the resulting ideal contains \(1\) proves complex, hence real, infeasibility for that coloring.

### 6.5 Jacobian-rank tests

For a candidate coloring, form the Jacobian of all equal-distance equations with respect to the coordinates. Numerical rank tests can reveal:

- whether a putative solution is isolated;
- whether a positive-dimensional family may exist;
- which equality constraints are dependent;
- whether known \(n\le8\) examples exhibit a reusable rigidity pattern.

Numerical rank is exploratory only; any final rank statement must be exact or certified.

### 6.6 Small-case benchmark suite

Any implementation should first reproduce:

- \(n=2\): one class of size \(1\);
- \(n=3\): classes \(1,2\);
- the explicit \(n=4\) coordinates above, with classes \(1,2,3\).

If exact coordinates for the Pomerance and Palásti constructions can be extracted from the cited papers, they should become benchmark instances for \(n=5,6,7,8\).

---

## 7. Attack routes

### Route A: Prove a strong lower bound for \(h(n)\)

**Core mechanism:** incidence geometry and general-position distinct-distance bounds.

**Needed key lemma:** Prove
\[
h(n)\ge n
\]
for all sufficiently large \(n\), or ideally for every \(n\ge9\).

**Why it might work:** Every desired configuration has only \(n-1\) distinct distances, so such a theorem immediately excludes it. The no-four-concyclic condition gives strong local bounds on equal-distance circles that are absent from the unrestricted distinct-distances problem.

**Likely failure point:** Existing elementary multiplicity arguments give only about \(n/3\) distances. Standard distance-energy methods generally lose too much and do not approach the sharp constant \(1\).

**Quick blockage test:** Translate the best available incidence estimate into an explicit lower bound for \(h(n)\). If its leading constant is below \(1\), the route cannot settle the problem without a genuinely new structural input.

---

### Route B: Exploit the exact multiplicity moments

**Core mechanism:** equal-distance energy, isosceles-triangle counts, and decomposition into adjacent versus disjoint equal edge pairs.

The target spectrum forces
\[
\sum_r\binom{\mu(r)}2=\binom n3.
\]
Split this count into:

- equal-length edge pairs sharing a vertex, corresponding to isosceles triangles;
- equal-length disjoint edge pairs.

**Needed key lemma:** An upper bound, under no-three-collinear and no-four-concyclic assumptions, strictly below \(\binom n3\) for all sufficiently large \(n\), or a structural classification of the equality-scale case.

**Why it might work:** The full spectrum imposes much more than \(n-1\) distinct distances. The identities
\[
\sum_r\binom{\mu(r)}k=\binom n{k+1}
\]
for all \(k\) may force an impossible concentration pattern.

**Likely failure point:** General equal-distance energy bounds are too large, often by logarithmic factors or constants. Disjoint equal segments are not directly prohibited by the circle condition.

**Quick blockage test:** Compute the strongest known or derivable upper bound for
\[
Q(P)=\sum_r\binom{\mu_P(r)}2.
\]
If it remains \(\gg n^3\) with a constant at least \(1/6\), it does not contradict the required
\[
Q(P)\sim n^3/6.
\]

---

### Route C: Distance-colored graph structure plus geometric forbidden patterns

**Core mechanism:** regard the configuration as an edge-coloring of \(K_n\), with color-class sizes \(1,\dots,n-1\), then combine graph constraints with Euclidean geometry.

**Needed key lemma:** Show that every such geometrically realizable coloring, once \(n\) is large enough, forces either:

- a monochromatic degree-\(4\) vertex;
- a monochromatic \(K_{2,3}\);
- a collinear triple;
- a concyclic quadruple; or
- another explicitly forbidden Euclidean subconfiguration.

**Why it might work:** The unusually dense collection of differently sized bounded-degree distance graphs may force overlap patterns impossible in the plane.

**Likely failure point:** Abstract colorings with the correct class sizes and maximum degree \(3\) probably exist for arbitrarily large \(n\). Pure graph theory may therefore be insufficient; the essential lemma must use metric consistency.

**Quick blockage test:** Use SAT to find abstract colorings for \(n=9,10,\dots\) satisfying all obvious graph constraints. If these are plentiful, focus immediately on additional Euclidean forbidden submatrices rather than further degree bookkeeping.

---

### Route D: Algebraic rigidity and rank deficiency

**Core mechanism:** study the algebraic variety cut out by prescribed equal-length equations.

For a fixed coloring, there are
\[
\frac{(n-1)(n-2)}2
\]
nominal equal-distance constraints in a configuration space of dimension \(2n-3\) modulo Euclidean motions.

**Needed key lemma:** Any sufficiently large family of equal-length equations with class sizes \(1,\dots,n-1\) either has Jacobian rank exceeding the available geometric dimension or has rank deficiency only because of a forbidden collinearity or concyclicity relation.

**Why it might work:** Known examples for \(n=6,7,8\) must rely on exceptional algebraic dependencies. These dependencies may admit a finite classification and cease to be possible beyond a threshold.

**Likely failure point:** Framework rigidity can have subtle stress dependencies unrelated to obvious degeneracies. Dimension counts alone have already failed at \(n=6,7,8\).

**Quick blockage test:** Extract the exact colorings of all known examples and compute their rigidity matrices and stress spaces. If their rank deficiencies display no common constrained pattern, a universal rank theorem may be difficult.

---

### Route E: Construct an unbounded family — disproof route

**Core mechanism:** recursive geometric gadgets, linkage constructions, or controlled deformation of symmetric configurations.

A recursive extension from \(n\) to \(n+1\) must transform the old multiplicity spectrum
\[
1,2,\dots,n-1
\]
into
\[
1,2,\dots,n
\]
using the \(n\) new edges incident to the added point, possibly while continuously deforming old points.

**Needed key lemma:** An extension or composition gadget that:

- preserves exact distance equalities in a controlled way;
- creates the new required multiplicity distribution;
- retains no three collinear and no four concyclic;
- works for infinitely many iterations.

**Why it might work:** The existing isolated examples up to \(8\) may be initial cases of an undiscovered recursive mechanism. If the equality equations define a positive-dimensional family, general-position inequalities might be enforceable generically inside that family.

**Likely failure point:** A new point has only two coordinates but may need to satisfy many exact equal-distance constraints. High-symmetry methods tend to create forbidden concyclic quadruples.

**Quick blockage test:** Formulate every combinatorially plausible \(8\to9\) extension and run numerical homotopy or nonlinear solving. If all systems are overdetermined even before imposing general position, simple one-point recursion is unlikely; more global deformation would be required.

An unbounded family would refute Erdős’s eventual-nonexistence belief. A single \(n=9\) construction would not.

---

### Route F: Certified finite classification beginning with \(n=9\)

**Core mechanism:** exhaustive combinatorial enumeration followed by exact semialgebraic realizability testing.

**Needed key lemma:** Reduce all candidate colorings at a given \(n\) to finitely many manageable isomorphism classes and certify each one realizable or impossible.

**Why it might work:** The multiplicity labels distinguish the colors, and degree-\(3\), \(K_{2,3}\), and symmetry constraints may reduce the search dramatically. Settling \(n=9\) is a natural first target and may reveal the general obstruction.

**Likely failure point:** The number of edge-colorings may still be enormous, while real-algebraic feasibility with strict nondegeneracy constraints is expensive. Finite checks alone cannot settle all \(n\).

**Quick blockage test:** Implement the SAT model for \(n=9\), quotient by graph isomorphism, and measure the number of surviving patterns. If the count is moderate, proceed to Gröbner/interval certification; if enormous, derive stronger geometric forbidden patterns first.

---

## 8. Verdict on difficulty

This is a very difficult open classification problem. The supplied record establishes all values through \(8\) but gives no resolution for \(n\ge9\).

Erdős’s eventual-nonexistence belief would follow from the strong general-position distinct-distance assertion
\[
h(n)\ge n
\quad\text{for all sufficiently large }n.
\]
That is a substantial distinct-distances problem in its own right. It is important not to overstate the relationship: Problem #217 may be easier because it imposes the much stronger multiplicity spectrum \(1,\dots,n-1\), but the commentary gives only an implication, not an equivalence.

A realistic research program should proceed on two levels:

1. **Finite frontier:** obtain and certify the known \(n=5,6,7,8\) configurations, then attack \(n=9\) by coloring enumeration and exact algebraic realizability.
2. **Asymptotic structure:** exploit the exact moment identities and rigidity dependencies to seek an obstruction stronger than a generic lower bound for \(h(n)\).

A proof of nonexistence for all \(n\ge9\) would completely solve the problem and vindicate a sharp form of Erdős’s belief. An infinite family of constructions would be equally significant and would refute his eventual-nonexistence prediction.