# Problem Brief: Erdős Problem #173

## 1. PRECISE STATEMENT

### Standard formalization

A **2-coloring of the plane** is an arbitrary function
\[
\chi:\mathbb R^2\to\{0,1\}.
\]
No measurability, Borel regularity, periodicity, or other regularity is assumed.

A **triangle** is an unordered set
\[
T=\{p_1,p_2,p_3\}\subset \mathbb R^2
\]
of three distinct, noncollinear points. Two triangles \(T,T'\) are **congruent** if there is a Euclidean isometry \(g\in\operatorname{Isom}(\mathbb R^2)\), possibly orientation-reversing, such that \(g(T)=T'\). Thus a triangle type is a congruence class of nondegenerate three-point subsets of the plane.

For a coloring \(\chi\), a triangle \(T\) is called **\(\chi\)-realized monochromatically** if there is an isometry \(g\) such that
\[
\chi(g(p_1))=\chi(g(p_2))=\chi(g(p_3)).
\]
Only the three vertices are required to have the same color; nothing is required of the sides or interior.

Let \(\mathcal T\) denote the set of congruence classes of nondegenerate triangles, and define the exceptional set
\[
E(\chi)=
\left\{
[T]\in\mathcal T:
\text{no congruent copy of }T\text{ is monochromatic under }\chi
\right\}.
\]

The problem asks whether
\[
\boxed{\forall \chi:\mathbb R^2\to\{0,1\},\qquad |E(\chi)|\le 1.}
\]

Equivalently, for every pair of noncongruent triangles \(T,U\) and every 2-coloring \(\chi\),
\[
\boxed{
\text{there is a monochromatic congruent copy of }T
\quad\text{or}\quad
\text{there is a monochromatic congruent copy of }U.
}
\]

This pairwise form is likely the most useful formulation.

### Parameterization by side lengths

A congruence class can be represented uniquely by an ordered side-length triple
\[
0<a\le b\le c<a+b.
\]
Triangles with the same three side lengths in a different labeling are congruent. Scale is part of the congruence class: equilateral triangles of side lengths \(1\) and \(2\) are noncongruent.

### Ambiguities in the informal wording

The standard reading above resolves several possible ambiguities:

1. **“All but at most one triangle” means one congruence class**, not one literal subset of \(\mathbb R^2\). If one literal triangle has no monochromatic congruent copy, then every congruent translate or rotation of it has the same status.

2. **The possible exception depends on the coloring.** The statement is
   \[
   \forall\chi\ \exists\text{ at most one exceptional class},
   \]
   not that there is one universal triangle class exceptional for every coloring.

3. **Congruence, not similarity.** Prescribed scale matters.

4. **Nondegenerate triangles are intended.** Allowing collinear triples would produce a substantially different problem.

5. **Vertices, not filled regions, are colored monochromatically.** This is the standard Euclidean Ramsey interpretation.

6. A “2-coloring” is best interpreted as a map into a set of two colors; surjectivity is not required. Constant colorings trivially realize every triangle.

---

## 2. WHAT COUNTS AS A SOLUTION

### Complete proof

A complete affirmative solution must establish the assertion for:

- every arbitrary coloring \(\chi:\mathbb R^2\to\{0,1\}\);
- every pair \(T,U\) of noncongruent, nondegenerate triangles;
- all translations, rotations, and reflected placements allowed by congruence;
- triangles at their exact prescribed scales.

It is enough to prove the equivalent pairwise assertion:
\[
[T]\ne[U]\implies
\bigl(M_\chi(T)\lor M_\chi(U)\bigr)
\]
for every \(\chi\), where \(M_\chi(T)\) denotes existence of a monochromatic congruent copy of \(T\).

A proof may instead characterize all possible exceptional triangles or all colorings admitting an exceptional triangle, provided that characterization rigorously implies \(|E(\chi)|\le1\).

Because Shader’s result reportedly handles every fixed right triangle, a complete proof only needs genuinely new work when both candidate triangles are non-right. However, relying on Shader requires confirming the exact statement and hypotheses of [Sh76].

### Complete disproof

A complete disproof must produce, or rigorously prove the existence of:

1. a coloring
   \[
   \chi:\mathbb R^2\to\{0,1\},
   \]
2. two nondegenerate triangles \(T,U\) with different sorted side-length triples,

such that for every isometry \(g\),
\[
\{\chi(g(p)):p\in T\}=\{0,1\}
\]
and
\[
\{\chi(g(q)):q\in U\}=\{0,1\}.
\]

Thus every congruent copy of each triangle must contain both colors.

For an explicit counterexample, the coloring rule must assign a color to every point, including strip boundaries or other exceptional loci, and the proof must verify avoidance for the continuum of all translations and orientations. A finite numerical search or dense sampling of orientations is not sufficient.

An abstract existence proof, for example through compactness or transfinite construction, would also disprove the problem if it rigorously establishes a single coloring avoiding two specified noncongruent triangles.

---

## 3. WHAT DOES NOT COUNT

The following do not resolve the problem:

- proving the assertion only for measurable, Borel, periodic, or finitely describable colorings;
- proving it only for triangles in a restricted range of angles, aspect ratios, or side lengths;
- proving that every right triangle is unavoidable—this is already the reported Shader result;
- proving the pairwise statement when one triangle belongs to some special family, unless all remaining pairs are also covered;
- proving that “almost every” triangle, in a measure-theoretic or Baire-category sense, is realized;
- proving that the exceptional set is finite, countable, measure zero, or has bounded dimension;
- finding monochromatic copies with approximately the right side lengths;
- finding monochromatic similar or homothetic copies at an unspecified scale;
- proving a result only in sufficiently high-dimensional Euclidean space;
- proving a result for finite boxes, lattices, or discretizations without a rigorous passage to arbitrary plane colorings;
- computationally checking finitely many placements or sampled orientations;
- a conditional proof depending on regularity or a separate unproved conjecture;
- showing merely that no single proposed coloring avoids two triangles;
- proving that each prescribed triangle is unavoidable under “generic” colorings.

In particular, Gallai’s theorem on monochromatic homothetic copies does not settle a fixed-congruence problem.

---

## 4. KNOWN RESULTS AND CONTEXT

### 4.1 Sharpness: one exceptional triangle can be necessary

The phrase “at most one” cannot be replaced by “none.” For every prescribed side length \(s>0\), there is an alternating-strip coloring with no monochromatic equilateral triangle of side \(s\).

Let
\[
h=\frac{\sqrt3}{2}s
\]
be the altitude of such an equilateral triangle, and color horizontal strips by
\[
\chi(x,y)=\left\lfloor \frac yh\right\rfloor \pmod 2.
\]

To verify avoidance, take any equilateral triangle of side \(s\), sort the three \(y\)-coordinates as
\[
y_0\le y_1\le y_2,
\]
and set
\[
a=y_1-y_0,\qquad b=y_2-y_1.
\]
The projection geometry of an equilateral triangle gives
\[
a^2+ab+b^2=h^2.
\]
After normalizing
\[
A=\frac ah,\qquad B=\frac bh,
\]
one has
\[
A^2+AB+B^2=1,
\]
hence
\[
A,B\le1,\qquad 1\le A+B\le\frac2{\sqrt3}<2.
\]

Suppose all three vertices had the same strip parity. Since the total normalized vertical span is at least \(1\) and less than \(2\), the bottom and top strip indices would have to differ by exactly \(2\). Write
\[
\frac{y_0}{h}=k+t,\qquad k\in\mathbb Z,\quad 0\le t<1.
\]
The middle vertex must then lie either in strip \(k\) or strip \(k+2\).

- If it lies in strip \(k\), then \(A<1-t\), while the top vertex being in strip \(k+2\) requires \(A+B\ge2-t\). Therefore \(B>1\), impossible.
- If it lies in strip \(k+2\), then \(A\ge2-t>1\), also impossible.
- If it lies in strip \(k+1\), it already has the opposite color.

Thus no congruent copy is monochromatic. The floor convention also handles all boundary cases.

This construction proves only that one prescribed equilateral class can be exceptional. It does **not** prove that its exceptional set consists of exactly that one class.

### 4.2 Shader’s right-triangle theorem

The database reports that Shader [Sh76] proved the fixed-triangle assertion for a right-angled triangle. The natural reading is:

> For every fixed nondegenerate right triangle \(R\), every 2-coloring of \(\mathbb R^2\) contains a monochromatic congruent copy of \(R\).

Assuming that is the exact theorem, no right triangle can belong to \(E(\chi)\). Consequently, the pairwise form of Problem #173 is already settled whenever at least one of \(T,U\) is right-angled.

The original paper should be checked before using this as a black box, especially for whether reflections are included and whether any regularity assumptions occur. The database wording strongly suggests the unrestricted result.

### 4.3 Hypergraph formulation

For a triangle \(T\), define the 3-uniform hypergraph
\[
\mathcal H_T=(\mathbb R^2,\mathcal E_T),
\]
where
\[
\mathcal E_T=\{g(T):g\in\operatorname{Isom}(\mathbb R^2)\}.
\]
A coloring avoids monochromatic copies of \(T\) exactly when it is a proper 2-coloring of \(\mathcal H_T\), in the sense that no hyperedge is monochromatic.

For a pair \(T,U\), the pairwise assertion says that
\[
\mathcal H_T\cup\mathcal H_U
\]
is not 2-colorable whenever \(T\) and \(U\) are noncongruent.

By Boolean compactness, an infinite hypergraph is 2-colorable if and only if every finite subhypergraph is 2-colorable. Therefore:

> For each fixed pair \(T,U\), if no coloring avoids both, then there is a finite set of points and finitely many copies of \(T\) and \(U\) on those points whose non-monochromatic constraints are already inconsistent.

Thus every positive pairwise instance has a finite obstruction in principle, although there need not be one uniform obstruction working for all triangle parameters.

### 4.4 Related elementary and classical facts

- Every prescribed two-point configuration is unavoidable in a 2-coloring. For a prescribed distance \(d\), take an equilateral triangle of side \(d\); two of its vertices have the same color.
- Gallai’s theorem states that every finite coloring of Euclidean space contains a monochromatic homothetic copy of every finite configuration. It allows an unspecified dilation and therefore does not guarantee a congruent copy at a prescribed scale.
- The problem belongs to fixed-dimensional, fixed-scale Euclidean Ramsey theory, where arbitrary colorings make topological and measure-theoretic methods difficult to apply directly.

---

## 5. TRAPS AND EDGE CASES

1. **Congruence classes include scale.** Equilateral triangles of side \(1\) and side \(2\) are two different candidates. A coloring avoiding both would already be a counterexample.

2. **Do not assume the sole possible exception must be equilateral.** Alternating strips only demonstrate sharpness using an equilateral triangle; they do not classify exceptional triangles.

3. **Arbitrary colorings need not be measurable.** Lebesgue density, Fourier analysis, ergodic theory, and limiting arguments cannot be applied without either removing the regularity assumption or reducing the problem to a finite configuration first.

4. **No continuity under perturbation.** A monochromatic copy of a triangle with nearly correct side lengths gives no information about the exact target triangle.

5. **Gallai gives the wrong scale.** A monochromatic homothetic copy is not a monochromatic congruent copy.

6. **A monochromatic pair is not enough.** If two same-colored points form one side of \(T\), avoiding \(T\) merely forces the relevant completion points to have the opposite color. This is a propagation rule, not an immediate contradiction.

7. **Every three vertices contain a same-colored pair, but usually at the wrong side length.** Simple pigeonhole arguments frequently lose control of which edge is monochromatic.

8. **Reflections must be included.** For a scalene triangle, checking only one orientation or chirality may miss congruent copies.

9. **Labels are artificial.** If side-length triples agree after permutation, the triangles are congruent. A proposed counterexample needs genuinely different sorted side triples.

10. **Isosceles and equilateral triangles have extra automorphisms.** Computational generation must avoid both omitting copies and counting coincident labeled copies incorrectly.

11. **Degenerate triangles should be excluded.** In coordinate calculations, enforce strict triangle inequalities and nonzero altitude.

12. **Strip boundaries matter.** A coloring defined using open strips but left undefined or inconsistently defined on boundary lines is not a valid counterexample.

13. **Sampling orientations is not universal verification.** The set of placements is continuous, and a missed isolated or boundary orientation can invalidate avoidance.

14. **Independent rescaling is invalid.** One may globally rescale the whole pair \(T,U\) and the coloring, but one cannot normalize the sizes of \(T\) and \(U\) independently. Their relative scale is an essential parameter.

15. **The exception depends on the coloring.** Proving that every coloring has some special unavoidable triangle is far weaker than proving that it cannot avoid two prescribed noncongruent triangles.

16. **Finite-grid evidence needs exact geometry.** Floating-point near-equalities can create or destroy purported congruent copies.

---

## 6. VERIFICATION HOOKS

### 6.1 Canonical coordinates

For a triangle with side lengths \(a,b,c\), take one side of length \(a\) as the base:
\[
P_1=(0,0),\qquad P_2=(a,0).
\]
If
\[
|P_1P_3|=b,\qquad |P_2P_3|=c,
\]
then
\[
P_3=
\left(
\frac{a^2+b^2-c^2}{2a},
\sqrt{
b^2-
\left(\frac{a^2+b^2-c^2}{2a}\right)^2
}
\right).
\]
The reflected placement uses the negative square root.

This gives exact algebraic coordinates when squared side lengths are rational or algebraic.

### 6.2 Triangle-completion routine

Given points \(P,Q\), \(d=|P-Q|\), and desired distances
\[
|P-R|=r,\qquad |Q-R|=s,
\]
define
\[
u=\frac{r^2-s^2+d^2}{2d},
\qquad
v=\sqrt{r^2-u^2}.
\]
Writing \(e=(Q-P)/d\) and \(Je\) for a quarter-turn of \(e\), the two completions are
\[
R=P+u e\pm vJe.
\]

A closure-generation program can repeatedly add all completions corresponding to every assignment of the sides of \(T\) and \(U\) to already present point pairs.

### 6.3 SAT encoding of finite obstructions

Assign a Boolean variable \(x_p\) to each point \(p\) in a finite configuration. For each copy \(\{p,q,r\}\) of either triangle, impose the not-all-equal condition
\[
\operatorname{NAE}(x_p,x_q,x_r).
\]
In CNF this is
\[
(x_p\lor x_q\lor x_r)
\land
(\neg x_p\lor\neg x_q\lor\neg x_r).
\]
Fix one variable, say \(x_{p_0}=0\), to remove global color-swap symmetry.

An UNSAT result, accompanied by a machine-checkable DRAT/LRAT certificate and exact verification of all geometric incidences, gives a rigorous finite obstruction for that pair.

### 6.4 Small-gadget enumeration

For selected parameter pairs:

1. Start from one copy of \(T\) and one of \(U\), possibly sharing an edge or vertex.
2. Close under selected triangle completions for two to six rounds.
3. Canonicalize algebraic coordinates exactly.
4. Enumerate all copies of \(T,U\) among the resulting points.
5. Test 2-colorability and record minimally unsatisfiable subhypergraphs.

Useful initial families include:

- two equilateral triangles of different side lengths;
- equilateral versus isosceles;
- two isosceles triangles with a common base;
- acute versus obtuse triangles sharing one or more side lengths;
- pairs with rational squared side lengths;
- pairs whose angles are rational multiples of \(\pi\).

These computations do not settle the universal problem but may expose reusable forcing gadgets.

### 6.5 Exact checking of strip candidates

For a coloring
\[
\chi(x,y)=f(y\bmod L)
\]
with a finite periodic strip pattern \(f\), a triangle with vertices \(p_i\) has projected heights
\[
t+\langle p_i,n\rangle,
\qquad n=(\cos\theta,\sin\theta).
\]
Avoidance requires the three values not to lie in strips of the same color for every \(t\) and \(\theta\), and for reflected copies as well.

For finite strip patterns with rational breakpoints, the universal conditions can be divided into cells according to which breakpoints are crossed. Introduce variables
\[
u=\cos\theta,\qquad v=\sin\theta,\qquad u^2+v^2=1.
\]
Within each cell, all projected coordinates are linear in \(u,v,t\). Exact interval methods or quantifier elimination over the reals can then verify or refute the candidate. Sampling \(\theta\) alone is not sufficient.

### 6.6 Entropy and rigidity experiments

For a finite geometric gadget, count the number of valid colorings avoiding a fixed triangle, modulo global color swap. Compare growth as the completion depth increases.

- Rapid collapse toward a few strip-like patterns would support a rigidity approach.
- Exponential growth with many incompatible local patterns would warn against classification arguments.

---

## 7. ATTACK ROUTES

### Route 1: Uniform finite forcing gadgets

**Core mechanism.** Use the hypergraph formulation and seek a finite non-2-colorable configuration built from copies of \(T\) and \(U\).

**Key lemma needed.** A parameter-uniform gadget theorem of the form:

> For every pair of noncongruent triangles \(T,U\), one of finitely many incidence constructions can be realized by congruent copies of \(T,U\), and the resulting NAE hypergraph is not 2-colorable.

The proof may require separate cases according to shared side lengths, angle relations, or acute/obtuse type.

**Why it might work.** Compactness guarantees that some finite obstruction exists for every positive pairwise instance. The main task is therefore not to justify finiteness but to find a controlled family of obstructions.

**Likely failure point.** The size or incidence pattern of the required obstruction may depend discontinuously on the six side parameters. Generic pairs may not admit useful coincidences among completion points.

**Quick blockage test.** Generate closure gadgets for many algebraic parameter pairs and run SAT. If minimal UNSAT cores repeatedly exhibit the same abstract patterns, a uniform theorem is plausible. If depth and size grow rapidly with no recurring core, this route may be too nonuniform.

---

### Route 2: Reflection and rotation propagation

**Core mechanism.** Avoiding a triangle gives deterministic color constraints when two vertices of a copy have the same color. Compare the two possible apexes over a fixed base and iterate the corresponding reflections and rotations.

Represent a triangle in complex coordinates as
\[
\{0,a,b\}.
\]
Its congruent copies are
\[
z+\omega\{0,a,b\}
\quad\text{and}\quad
z+\omega\{0,\overline a,\overline b\},
\qquad |\omega|=1.
\]

**Key lemma needed.** Show that simultaneous avoidance of \(T\) and \(U\) forces a color relation
\[
\chi(gx)=\chi(x)\quad\text{or}\quad \chi(gx)=1-\chi(x)
\]
for sufficiently many points and for one or more Euclidean motions \(g\), and that compositions produce an inconsistent odd color-flip cycle.

**Why it might work.** Triangle completions are governed by reflections across perpendicular bisectors and rotations by triangle angles. Combining two noncongruent triangle geometries may generate a rich transformation group, leaving no consistent binary coloring.

**Likely failure point.** The propagation begins only from a same-colored base pair. For a particular edge, its endpoints may be oppositely colored, so the desired deterministic rule may not activate.

**Quick blockage test.** For a fixed pair \(T,U\), generate the orbit of a small seed under all relevant completion maps and encode the conditional propagation rules in SAT. Check whether contradictions arise only after imposing an unjustified monochromatic base.

---

### Route 3: Use Shader’s right-triangle theorem as a monochromatic seed

**Core mechanism.** Choose a right triangle \(R=R(T,U)\) whose side lengths or angles are designed from the parameters of \(T,U\). By Shader’s theorem, every coloring contains a monochromatic congruent copy of \(R\). Attach copies of \(T\) and \(U\) to this monochromatic seed.

**Key lemma needed.** Construct, for every noncongruent \(T,U\), a finite attachment pattern around an appropriately chosen right triangle \(R\) such that:

- if the three vertices of \(R\) are monochromatic, and
- every copy of \(T\) and \(U\) in the attachment is required to be nonmonochromatic,

then the resulting color constraints are inconsistent.

**Why it might work.** A major obstacle in propagation arguments is obtaining a controlled monochromatic initial configuration. Shader supplies one at an exact prescribed scale.

**Likely failure point.** Avoiding \(T\) and \(U\) may consistently color all attachment vertices opposite to portions of the seed. A monochromatic right triangle may not impose enough independent constraints.

**Quick blockage test.** For representative parameter pairs, prescribe a monochromatic right-triangle seed in the SAT model and search automatically for small completion gadgets that become UNSAT. Compare with the same search without the seed.

---

### Route 4: Structural classification of triangle-avoiding colorings

**Core mechanism.** Try to prove that if a coloring avoids one triangle \(T\), then both \(T\) and the coloring have strong structure. The alternating-strip construction suggests a possible extremal model.

**Key lemma needed.** A rigidity theorem such as:

> If an arbitrary 2-coloring avoids a congruent copy of \(T\), then \(T\) belongs to a highly restricted family and the coloring satisfies a global one-dimensional or periodic constraint.

A weaker sufficient version would show directly that any coloring avoiding \(T\) realizes every noncongruent \(U\).

**Why it might work.** Avoidance imposes one NAE constraint for every translate and rotation of \(T\), an enormous overdetermined system. Exact avoidance might be possible only through highly organized colorings.

**Likely failure point.** Hypergraph 2-colorings can be extremely nonconstructive and need not resemble periodic examples. Local constraints may allow high-entropy pathological colorings with no geometric regularity.

**Quick blockage test.** Compute the number and diversity of valid colorings on increasingly deep finite completion closures. If solutions rapidly become strip-like, rigidity is plausible. If many unrelated patterns survive, classification is unlikely without a new invariant.

---

### Route 5: Finite averaging and geometric Ramsey extraction

**Core mechanism.** Avoid measure theory by selecting finite families of translations and orientations and averaging combinatorially. Seek a finite geometric configuration in which every 2-coloring produces either \(T\) or \(U\).

**Key lemma needed.** A finite selection theorem:

> For each noncongruent pair \(T,U\), there is a finite union of carefully chosen congruent copies such that every coloring of its vertices contains a monochromatic edge corresponding to \(T\) or \(U\).

Possible tools include Ramsey theory on circles, intersections of distance graphs, or repeated majority arguments with exact control of edge lengths.

**Why it might work.** The desired infinite-plane statement is equivalent, pair by pair, to the existence of a finite obstruction. Finite averaging is valid for arbitrary colorings and avoids all regularity issues.

**Likely failure point.** Standard Ramsey arguments naturally produce monochromatic subsets at an uncontrolled scale or with the wrong edge-length assignment. Preserving exact congruence through all pigeonhole steps is difficult.

**Quick blockage test.** Attempt the method first for two equilateral triangles of distinct side lengths. If finite circle or polygon constructions cannot control even this symmetric case, the general route is likely blocked.

---

### Route 6: Disproof through periodic or quasiperiodic one-dimensional colorings

**Core mechanism.** Generalize the alternating-strip construction. Choose a linear functional \(\ell:\mathbb R^2\to\mathbb R\) and a binary periodic function \(f\), and set
\[
\chi(x)=f(\ell(x)).
\]
Search for one pattern whose projection constraints prevent monochromatic copies of two noncongruent triangles.

**Key lemma needed.** Exhibit distinct triangles \(T,U\) and a fully specified \(f\) such that for every orientation, reflection, and translation phase, the three projected coordinates of each triangle cannot all land in color classes of the same color.

**Why it might work.** Alternating strips already avoid a fixed equilateral triangle. More complicated strip widths or periodic binary words might enforce two independent projection obstructions.

**Likely failure point.** Rotating a triangle sweeps a continuum of projection-gap triples. Simultaneously blocking two distinct triangles may overdetermine every one-dimensional pattern. This is exactly the behavior predicted by the conjecture.

**Quick blockage test.** Enumerate short periodic binary strip words and rational strip widths. Use exact cell decomposition in \((t,\cos\theta,\sin\theta)\), not sampling, to test pairs such as two equilateral scales or equilateral/isoceles pairs. Any successful candidate would be a direct disproof after universal verification.

---

## 8. VERDICT ON DIFFICULTY

This is a serious open problem in exact Euclidean Ramsey theory. The absence of regularity assumptions is a central difficulty: measure, topology, compactness of rotations, and limiting arguments do not directly control arbitrary colorings. At the same time, the prescribed scale prevents direct use of Gallai-type homothety theorems.

The alternating-strip example shows that the statement is best possible, while Shader’s theorem handles the important but special family of right triangles. Under the reported scope of Shader’s result, all unresolved pairwise instances involve two non-right triangles.

No equivalence to a famous conjecture such as Hadwiger–Nelson is apparent from the supplied material, and one should not claim such an equivalence. Nevertheless, the problem is likely difficult: it asks for a uniform theorem over a continuum of pairs of triangle parameters and over all, potentially pathological, 2-colorings.

The most promising concrete research program is:

1. formulate fixed pairs as finite NAE-hypergraph obstruction problems;
2. search exact algebraic examples for recurring UNSAT cores;
3. exploit Shader’s right-triangle theorem to supply monochromatic seeds;
4. simultaneously test generalized strip colorings for a counterexample, beginning with two equilateral triangles of different scales.

The first major benchmark should be the apparently still nontrivial subproblem:

\[
\textit{Can one 2-coloring avoid equilateral triangles of two distinct prescribed side lengths?}
\]

A proof that this is impossible would not solve Problem #173, but it would settle the most symmetric potential counterexample and likely reveal mechanisms relevant to the general case.