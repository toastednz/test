# Problem brief: Erdős Problem #196

## 1. Precise statement

Let  
\[
\mathbb N=\{1,2,3,\dots\}.
\]
A permutation of \(\mathbb N\) is a bijection
\[
x:\mathbb N\to\mathbb N,\qquad i\mapsto x_i.
\]
For each \(n\in\mathbb N\), define its position in the permutation by
\[
p(n)=x^{-1}(n).
\]
Thus \(p:\mathbb N\to\mathbb N\) is also a permutation.

A nontrivial four-term arithmetic progression in \(\mathbb N\) is a tuple
\[
(a,a+d,a+2d,a+3d)
\]
with \(a,d\in\mathbb N\), so \(d>0\).

The problem asks whether the following assertion is true:

> For every permutation \(x\) of \(\mathbb N\), there exist \(a,d\in\mathbb N\) such that either
> \[
> p(a)<p(a+d)<p(a+2d)<p(a+3d),
> \]
> or
> \[
> p(a)>p(a+d)>p(a+2d)>p(a+3d).
> \]

Equivalently, every ordering of the positive integers must contain some four-term arithmetic progression whose elements occur in numerical order or in reverse numerical order.

In the notation of the database statement, set
\[
i=p(a),\quad j=p(a+d),\quad k=p(a+2d),\quad l=p(a+3d).
\]
Then the two alternatives are \(i<j<k<l\) and \(i>j>k>l\).

### Equivalent sign formulation

For fixed \(d\ge 1\) and a residue-class ray
\[
r,r+d,r+2d,\dots,
\]
define
\[
s_t=\operatorname{sgn}\bigl(p(r+(t+1)d)-p(r+td)\bigr)\in\{+,-\}.
\]
A counterexample is exactly a permutation \(p\) for which, for every \(d,r\), the sign sequence has no run of three equal signs. In other words, every block of three consecutive signs contains both \(+\) and \(-\).

Equivalently, for every \(a,d\), at least one of the two middle terms
\[
p(a+d),\qquad p(a+2d)
\]
is a local extremum among its two neighbors in the four-term sequence
\[
p(a),p(a+d),p(a+2d),p(a+3d).
\]

### Ambiguities and conventions

1. “Arithmetic progression” must be nonconstant, so \(d>0\). Allowing \(d=0\) would be incompatible with a permutation and would trivialize terminology.
2. The intended meaning is not merely that the unordered set
   \[
   \{x_i,x_j,x_k,x_l\}
   \]
   happens to be a four-term arithmetic progression. Such a reading would make monotonicity irrelevant and would not match the DEGS context.
3. If one uses \(\mathbb N=\{0,1,2,\dots\}\), the problem is equivalent after translating all labels and indices by one.
4. One may instead allow negative common differences and require increasing indices only. That is equivalent to the formulation above.

---

## 2. What counts as a solution

### A complete affirmative solution

A proof of “yes” must establish
\[
\forall p:\mathbb N\to\mathbb N\text{ bijective}\quad
\exists a,d\in\mathbb N
\]
such that
\[
p(a),p(a+d),p(a+2d),p(a+3d)
\]
is strictly increasing or strictly decreasing.

The proof must use only consequences valid for an arbitrary permutation. In particular, it may not assume regular growth, positive density, computability, bounded displacement, or any other structural condition not shared by all permutations.

A finite forcing result would be sufficient: if one proves that there is an \(N\) such that every linear ordering of \([N]=\{1,\dots,N\}\) contains a monotone four-term arithmetic progression, then every permutation of \(\mathbb N\) contains one, by considering the relative order in which the elements of \([N]\) appear.

A computer-assisted affirmative proof is valid if it supplies:

1. a rigorously specified finite reduction;
2. a complete unsatisfiability or exhaustive-search certificate;
3. independently checkable verification code or a standard proof certificate such as DRAT/LRAT;
4. a proof that the finite statement really implies the infinite theorem.

### A complete negative solution

A disproof must establish the existence of a bijection
\[
p:\mathbb N\to\mathbb N
\]
such that for every \(a,d\ge 1\),
\[
p(a),p(a+d),p(a+2d),p(a+3d)
\]
is neither strictly increasing nor strictly decreasing.

Equivalently, one must construct a permutation
\[
x_1,x_2,\dots
\]
in which no four-term arithmetic progression occurs in numerical or reverse numerical order.

If the counterexample is explicit or algorithmic, verification requires separate proofs of:

1. **Injectivity:** every integer is output at most once.
2. **Surjectivity/fairness:** every positive integer is eventually output.
3. **Avoidance:** for every \(a,d\ge1\), the four positions of
   \[
   a,a+d,a+2d,a+3d
   \]
   are not monotone.

An existence proof by recursion or compactness is also acceptable, but it must ensure that the resulting order has order type \(\omega\), hence actually arises from a permutation sequence. Producing only an abstract total order on \(\mathbb N\) is insufficient.

---

## 3. What does not count

The following do not resolve the problem.

1. Reproving that every permutation contains a monotone three-term arithmetic progression.
2. Exhibiting a permutation with no monotone five-term progression.
3. Proving the result only for bounded displacement permutations, random models, computable permutations, block permutations, or another restricted class.
4. Proving that a positive-density set of values contains a four-term arithmetic progression. The issue is the order of appearance of all four terms.
5. Applying Erdős–Szekeres to obtain a monotone subsequence of length four whose values are not themselves in arithmetic progression.
6. Applying van der Waerden or Szemerédi merely to find an arithmetic progression inside one color or position class. This does not force its four entry times to be monotone.
7. Establishing the claim only for \(d=1\), only for bounded \(d\), or only for progressions inside a prescribed interval.
8. Showing that “most” permutations or permutations in a finite random model have the desired progression.
9. Producing arbitrarily long finite permutations avoiding monotone four-term progressions. That does not automatically yield an infinite permutation.
10. Producing an abstract total order on \(\mathbb N\) avoiding the configuration unless every element has finitely many predecessors. A permutation order must have order type \(\omega\).
11. Giving extensive numerical evidence without either an all-parameter proof or a rigorously verified finite forcing certificate.
12. A conditional proof depending on an unproved conjecture.

An asymptotic improvement, such as proving a monotone progression of some length between four and five in a special regime, also does not settle the exact problem.

---

## 4. Known results and context

### DEGS theorem

Davis, Entringer, Graham, and Simmons [DEGS77] proved, in the terminology of the database, that:

1. Every permutation of \(\mathbb N\) contains a monotone three-term arithmetic progression.
2. There exists a permutation of \(\mathbb N\) containing no monotone five-term arithmetic progression.

Thus the length threshold is known on both sides:

- lengths \(1\) and \(2\): trivial;
- length \(3\): unavoidable;
- length \(4\): open;
- length \(5\): avoidable;
- every length \(k\ge5\): avoidable, using the same five-term-avoiding permutation, since a monotone \(k\)-term progression contains a monotone five-term initial segment.

Therefore length four is the only unresolved threshold in this family.

The five-term construction does not answer the four-term problem: a permutation can contain many monotone four-term progressions while containing no monotone five-term progression. Conversely, the three-term theorem does not extend formally, since a monotone three-term progression need not be extendable to a monotone four-term one.

The database also points to Problems #194 and #195 as related progression-ordering problems. Their precise statements should be consulted before importing any claimed implication.

### Relevant classical theorems

Several major theorems are nearby but do not directly solve the problem.

- **Erdős–Szekeres monotone subsequence theorem:** long finite sequences contain long monotone subsequences. The selected indices or values need not be equally spaced.
- **van der Waerden’s theorem:** finite colorings contain arbitrarily long monochromatic arithmetic progressions. Monochromaticity does not encode the required ordering of four entry times.
- **Szemerédi’s theorem:** positive-density subsets of \(\mathbb N\) contain long arithmetic progressions. Natural monotone or record subsets arising from a permutation can have density zero.
- **Infinite Ramsey theorem:** the comparison coloring
  \[
  \{u,v\}\mapsto \mathbf 1[p(u)<p(v)]
  \]
  has large homogeneous structures, but a homogeneous infinite subset may be arithmetic-progression-free.

These results may be ingredients, but none by itself resolves the order-plus-additive-structure interaction.

### Hypergraph viewpoint

Let \(H\) be the four-uniform hypergraph on \(\mathbb N\) whose edges are the sets
\[
\{a,a+d,a+2d,a+3d\}.
\]
Each edge has two distinguished “bad” vertex orders: increasing numerical order and decreasing numerical order. The question is whether every fair sequential ordering of the vertices realizes one edge in one of its two bad orders.

This is not ordinary hypergraph independence: all four vertices may appear, but their relative order is constrained.

---

## 5. Traps and edge cases

1. **The indices need not be consecutive.** Only their relative order matters.
2. **All common differences matter.** Avoiding monotone runs among consecutive values, \(d=1\), is far too weak.
3. **Four distinct terms are required.** This is automatic from \(d>0\).
4. **The second index alternative is not redundant under the positive-\(d\) convention.** It records an increasing numerical progression appearing backwards.
5. **A monotone subset is not necessarily an arithmetic progression.** Erdős–Szekeres cannot be used without controlling additive spacing.
6. **A four-term arithmetic progression contains two consecutive three-term progressions, but their orientations may not combine.**
7. **No five-term progression does not mean no four-term progression.**
8. **Finite compactness is delicate.** If every \([N]\) has an avoiding order, compactness can yield an avoiding total order of \(\mathbb N\), but that order may have infinite descending chains or elements with infinitely many predecessors and hence may not be the order of a permutation sequence.
9. **Infinite reversal is not a symmetry.** A finite ordering can be reversed, but there is no sequence listing all positive integers in globally reverse order.
10. **Affine restrictions are legitimate.** If \(x\) were a counterexample, then the induced order on any infinite arithmetic progression
    \[
    r+q\mathbb N
    \]
    would, after rescaling, again avoid monotone four-term progressions. Any construction must therefore survive every residue-class restriction.
11. **Prefix avoidance is hereditary but surjectivity is not.** It is easy to construct longer and longer injective avoiding words by continually choosing large safe values; such a construction may omit infinitely many small integers.
12. **Small cases do not force the phenomenon.** For \(N\le3\) there is no four-term progression. For \(N=4\), the only one is \(1,2,3,4\), and the order
    \[
    2,1,4,3
    \]
    avoids it monotonically.
13. **Checking only progressions wholly contained in an initial position prefix is valid for that prefix, but says nothing about later insertions of missing values.**
14. **Rank ties never occur.** Any coding that permits equal ranks is modeling the wrong problem.

---

## 6. Verification hooks

### 6.1 Direct finite-word checker

Given a finite word \(w_1,\dots,w_L\) of distinct positive integers:

1. Build the position table \(\operatorname{pos}(v)\).
2. Let \(M=\max_i w_i\).
3. For every \(d\ge1\) and \(a\ge1\) with \(a+3d\le M\), check whether all four values
   \[
   a,a+d,a+2d,a+3d
   \]
   occur in the word.
4. If they do, inspect
   \[
   \operatorname{pos}(a),\operatorname{pos}(a+d),
   \operatorname{pos}(a+2d),\operatorname{pos}(a+3d).
   \]
5. Reject if these positions are strictly increasing or strictly decreasing.

This is a necessary regression test for every proposed construction.

### 6.2 Sign-run checker

For each tested \(d\) and residue \(r\), form
\[
\operatorname{sgn}(p(r+(t+1)d)-p(r+td)).
\]
A four-term violation occurs exactly when three consecutive signs are all \(+\) or all \(-\). This formulation is often faster for dense finite restrictions.

### 6.3 SAT encoding for finite orders

For \([N]\), introduce a Boolean variable \(B_{u,v}\) for each \(u<v\), interpreted as “\(u\) precedes \(v\).”

Add clauses ensuring that the resulting tournament is transitive, hence represents a total order. For every four-term progression
\[
a,a+d,a+2d,a+3d\le N,
\]
add clauses forbidding
\[
a\prec a+d\prec a+2d\prec a+3d
\]
and its reverse.

Alternatively, use integer rank variables \(r_v\in[N]\) with an all-different constraint and forbid the two strict chains.

- A satisfying assignment gives a finite avoiding order.
- An unsatisfiability certificate for some \(N\) would prove the original problem affirmatively.

The converse is not automatic: satisfiability for every \(N\) does not by itself give an infinite permutation counterexample.

### 6.4 Testing recursive block constructions

For a base-\(B\) or substitution construction:

1. Generate complete stages, preferably through several digit lengths.
2. Enumerate all four-term progressions in the stage.
3. Classify violations by carry pattern across digits and by the number of blocks met.
4. Record the smallest violating \((a,d)\) and its block profile.

A proposed inductive proof should have a finite, exhaustive classification of carry types. Code can verify that the classification covers all progressions up to several stages.

### 6.5 Testing finite-prefix extension algorithms

If a construction appends one unused value at a time, a newly created violation must use the newly appended value as the latest position. If the new value is \(y\), only two types need checking:

- \(y=a+3d\), with \(a,a+d,a+2d\) previously occurring in increasing numerical order;
- \(y=a\), with \(a+d,a+2d,a+3d\) previously occurring in reverse numerical order.

This gives an efficient forbidden-next-value list.

For any finite prefix that already avoids the pattern, only finitely many values are forbidden as possible next entries. Hence some unused safe extension always exists. The difficult part is ensuring that every postponed integer is eventually inserted.

### 6.6 Proof-certificate regression

Any general lemma intended to prove unavoidability should also be tested against the DEGS five-term-avoiding construction, if its explicit form is available. A lemma that would force monotone progressions of every length is necessarily false.

---

## 7. Attack routes

### Route 1: Double-count local extrema across arithmetic directions

**Core mechanism.**  
In a counterexample, every four-term progression must contain a turn:
\[
+++,---\quad\text{are forbidden sign patterns}.
\]
Thus every pair \((a,d)\) must be “witnessed” by a local maximum or minimum at \(a+d\) or \(a+2d\).

**Key lemma needed.**  
A useful form would bound how many four-term progressions can be certified by local extrema of a permutation rank function inside a large finite value interval, with enough boundary control to show that not all \(\Theta(N^2)\) progressions can be covered.

One possible target is a weighted bound that uses the fact that the low-rank sublevel sets
\[
\{n:p(n)\le t\}
\]
have exactly \(t\) elements.

**Why it might work.**  
The avoidance condition is highly overdetermined: for every step \(d\), every arithmetic ray must change direction at least once every three comparisons. Simultaneously enforcing this for all \(d\) may create too many required extrema.

**Likely failure point.**  
A single value can be a local extremum for many different steps \(d\), potentially \(\Theta(N)\) of them. A naive counting argument will therefore have the same order of magnitude on both sides and may not contradict anything.

**Quick blockage test.**  
For large finite SAT-generated avoiders, compute for each vertex the number of \((a,d)\) constraints it witnesses. If a few ranks consistently witness a linear number of progressions, unweighted counting is blocked and a rank-sensitive or multiscale weight is required.

---

### Route 2: Multiscale density and arrival-time quantiles

**Core mechanism.**  
View the permutation dynamically through
\[
A_t=\{x_1,\dots,x_t\}=\{n:p(n)\le t\}.
\]
For a finite value interval \([N]\), color each \(n\le N\) by the quantile containing \(p(n)\). A four-term progression whose colors are \(1,2,3,4\) in numerical order is automatically monotone in position; likewise for \(4,3,2,1\).

**Key lemma needed.**  
A multiscale “ordered rainbow four-AP” theorem: for the nested colorings generated by one global rank function, some scale must contain an arithmetic progression with strictly increasing or decreasing arrival bands.

Arbitrary balanced four-colorings are probably too flexible, so the lemma must exploit consistency as \(N\) and the time thresholds vary.

**Why it might work.**  
The sets \(A_t\) are not arbitrary color classes: they are nested, increase one point at a time, and eventually cover every integer. Density-increment or energy arguments may force an ordered transition across four levels.

**Likely failure point.**  
Van der Waerden and Szemerédi favor monochromatic progressions, whereas this route needs a particular rainbow order. Balanced colorings may avoid the two ordered rainbow patterns at all accessible scales.

**Quick blockage test.**  
Use SAT or integer programming to construct balanced four-colorings of \([N]\) avoiding color patterns \(1234\) and \(4321\) on every four-AP. Then impose nesting constraints between several scales. If even strongly nested finite models remain easy to construct, a simple density argument is unlikely to suffice.

---

### Route 3: Transitive pair-coloring plus the order-type-\(\omega\) constraint

**Core mechanism.**  
Color every pair \(u<v\) by
\[
c(u,v)=
\begin{cases}
+,&p(u)<p(v),\\
-,&p(u)>p(v).
\end{cases}
\]
Because \(c\) comes from a total order, it is a transitive tournament coloring. The target is
\[
c(a,a+d)=c(a+d,a+2d)=c(a+2d,a+3d).
\]

In addition, this total order has order type \(\omega\): every integer has only finitely many predecessors.

**Key lemma needed.**  
Every transitive two-coloring of pairs of \(\mathbb N\) whose underlying order has type \(\omega\) contains a four-term arithmetic progression whose three consecutive edges have one color.

**Why it might work.**  
General total orders can evade conclusions unavailable to permutation orders. The finite-predecessor condition is the crucial noncompact feature behind the DEGS three-term theorem and may force additive regularity.

**Likely failure point.**  
Ramsey theory can produce an infinite homogeneous subset, but that subset can be extremely sparse and contain no nontrivial arithmetic progression. Standard Ramsey arguments ignore order type and additive density.

**Quick blockage test.**  
Construct avoiding total orders of non-\(\omega\) type by finite compactness, then identify exactly where their infinite predecessor sets are used. Any proposed lemma that remains true without the finite-predecessor assumption is probably false or too strong.

---

### Route 4: Sharpen and iterate the DEGS three-term argument

**Core mechanism.**  
Recover the original DEGS proof in full detail and isolate its minimal forcing configuration. Attempt to strengthen it from “some monotone three-AP exists” to a three-AP with controlled endpoint, common difference, rank, or surrounding interval, allowing two compatible three-APs to concatenate into a four-AP.

**Key lemma needed.**  
A controlled three-term theorem, for example one forcing
\[
p(a)<p(a+d)<p(a+2d)
\]
together with a structural condition ensuring that either \(a-d\) or \(a+3d\) appears on the correct side in the order, possibly after passing to an affine subprogression.

**Why it might work.**  
Length four is immediately adjacent to the exact DEGS positive theorem. Their proof may contain unused structural information lost in the statement.

**Likely failure point.**  
The forced three-term progressions may be isolated: their possible extensions can consistently appear on the wrong side. Any argument that merely finds many three-APs without aligning their differences will probably fail.

**Quick blockage test.**  
Formalize proposed strengthened DEGS lemmas as finite constraints and search for counterorders. If arbitrarily large finite models satisfy the negation, determine whether the intended proof genuinely uses surjectivity/order type rather than only finite structure.

---

### Route 5: Constructive disproof by hierarchical blocks or priority scheduling

**Core mechanism.**  
Attempt to build a counterexample directly.

Two promising variants are:

1. **Hierarchical substitution:** order integers by base-\(B\) digit rules, recursively permuting blocks and positions within blocks.
2. **Priority construction:** append safe unused integers while scheduling every integer for eventual insertion.

**Key lemma needed.**

For block substitution, one needs a composition lemma showing that every four-AP either lies inside one block, projects to a lower-level progression already controlled, or has a carry pattern that forces a turn.

For a priority construction, one needs a repair or buffer lemma:

> Given any finite avoiding prefix and any omitted target \(m\), there is a finite avoiding extension that includes \(m\).

This would permit a fair stage construction.

**Why it might work.**  
DEGS already constructed an infinite permutation avoiding monotone five-term progressions, so structured infinite avoidance is demonstrably possible. Four terms may still admit a more delicate carry-based construction.

Also, any finite avoiding prefix has infinitely many safe possible next values; the only obstruction is fairness, not local extendability.

**Likely failure point.**  
Arithmetic progressions crossing blocks create carries that defeat naive substitution. In the priority approach, a small omitted value can become permanently unsafe after certain larger values have appeared, so greedy extension may omit it forever.

**Quick blockage test.**  
Brute-force all small block permutations and substitutions for bases \(B=2,3,\dots\), classify the first cross-block violations, and see whether any finite set of local state rules eliminates them. For priority constructions, search for finite prefixes from which a specified missing target cannot be appended after any bounded number of safe buffer moves.

This is the principal route aimed at disproof.

---

### Route 6: Finite SAT search, obstruction extraction, and proof mining

**Core mechanism.**  
Search finite total orders avoiding all monotone four-APs, but use the output to discover either:

- a finite forcing threshold \(N\), or
- a stable recursive structure suggestive of an infinite counterexample.

One should go beyond raw satisfiability by extracting backbones, symmetries, minimal unsatisfiable cores, and extension obstructions.

**Key lemma needed.**  
For an affirmative result, an explicit \(N\) for which the finite ordering instance is unsatisfiable.

For a negative result, a composition or extension theorem inferred from the recurring structure of large finite solutions.

**Why it might work.**  
The local constraints have a compact SAT encoding, and length four is small enough that substantial finite exploration is realistic. The problem’s exact-threshold nature makes finite structural data especially valuable.

**Likely failure point.**  
Finite avoiders may exist for every tested \(N\) without approaching an order of type \(\omega\). Conversely, an unsatisfiable model with additional artificial bounds may reflect those bounds rather than the original problem.

**Quick blockage test.**  
Compare three model classes:

1. arbitrary orders of \([N]\);
2. finite prefixes required to contain \([m]\);
3. bounded-displacement or block-structured permutations.

If obstructions appear only in the restricted classes, they are not evidence for the full theorem. Require certified unsatisfiability for unrestricted orders of \([N]\) before claiming a finite proof.

---

## 8. Verdict on difficulty

This is a genuinely hard, long-standing threshold problem. According to the database it remains open, while the adjacent lengths were settled by DEGS: three terms are unavoidable and five terms are avoidable. Thus four is not a routine quantitative refinement; it is the unique boundary case separating known positive and negative behavior.

No standard implication from van der Waerden’s theorem, Szemerédi’s theorem, Ramsey theory, or Erdős–Szekeres is known. The central difficulty is the interaction of:

1. additive structure in the **values**;
2. total-order structure in the **positions**;
3. the noncompact requirement that the order have type \(\omega\).

There is no established equivalence to a famous conjecture such as Szemerédi, Erdős–Turán, or a major Ramsey conjecture. Nevertheless, the problem has resisted the natural tools surrounding all of them and should be treated as high difficulty. A successful attack will likely need either a sharp exploitation of order type \(\omega\), a new ordered-additive Ramsey lemma, or a carefully engineered recursive counterexample.