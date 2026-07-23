# Problem Brief: Erdős Problem #14

## 1. Precise statement

### 1.1 Conventions

Take
\[
\mathbb N=\{1,2,3,\dots\}.
\]
Let \(A\subseteq\mathbb N\). For \(n\in\mathbb N\), define the **unordered representation function**
\[
r_A(n)
=
\#\{(a,a')\in A^2:a\le a',\ a+a'=n\}.
\]
Thus:

- \(a+a'\) and \(a'+a\) are the same representation;
- the diagonal representation \(n=a+a\) is allowed;
- since \(A\) is a set, there are no multiplicities attached to its elements.

Define
\[
B_A=\{n\in\mathbb N:r_A(n)=1\},
\]
and the exceptional-count function
\[
E_A(N)
=
\bigl|\{1,\dots,N\}\setminus B_A\bigr|
=
\#\{1\le n\le N:r_A(n)\ne 1\}.
\]
The exceptional set therefore includes both:

- integers with no representation, \(r_A(n)=0\);
- integers with at least two representations, \(r_A(n)\ge 2\).

The unordered convention is the only reading consistent with the Sidon-set context and the quoted finite theorem. Under ordered counting, an off-diagonal representation automatically occurs twice, making “exactly one” essentially a diagonal condition and changing the problem completely.

### 1.2 First question: universal lower bound

The standard fixed-\(A\) reading is:

> **Question (Q1).** Is it true that for every \(A\subseteq\mathbb N\) and every \(\epsilon>0\), there exist constants
> \[
> c=c(A,\epsilon)>0,\qquad N_0=N_0(A,\epsilon)
> \]
> such that
> \[
> E_A(N)\ge cN^{1/2-\epsilon}
> \]
> for every integer \(N\ge N_0\)?

Equivalently,
\[
E_A(N)=\Omega_{A,\epsilon}(N^{1/2-\epsilon})
\quad\text{for every }\epsilon>0.
\]

The notation \(\gg_\epsilon\) may instead be intended to make the multiplicative constant independent of \(A\). That stronger reading is
\[
\forall\epsilon>0\ \exists c_\epsilon>0\ \forall A\subseteq\mathbb N\
\exists N_0(A,\epsilon)\ \forall N\ge N_0:
E_A(N)\ge c_\epsilon N^{1/2-\epsilon}.
\]
Any proof should state explicitly whether its constant is uniform in \(A\). A proof of the uniform version proves the fixed-\(A\) version; a failure of uniformity alone need not disprove the fixed-\(A\) version.

Only \(0<\epsilon<1/2\) is substantively relevant. Since \(1\) is never a sum of two positive integers, \(E_A(N)\ge1\), making the assertion trivial for \(\epsilon\ge1/2\).

### 1.3 Second question: sub-square-root construction

> **Question (Q2).** Does there exist a single set \(A\subseteq\mathbb N\) such that
> \[
> E_A(N)=o(N^{1/2})?
> \]

Formally, this means
\[
\exists A\subseteq\mathbb N\ \forall\eta>0\ \exists N_0(\eta)\
\forall N\ge N_0(\eta):
E_A(N)\le \eta N^{1/2}.
\]

The estimate must hold for every sufficiently large \(N\), not merely along a subsequence.

### 1.4 Logical independence of the two questions

The two questions are not negations of one another.

For example, a hypothetical set satisfying
\[
E_A(N)\asymp \frac{\sqrt N}{\log N}
\]
would simultaneously:

- satisfy \(E_A(N)\gg_\epsilon N^{1/2-\epsilon}\) for every fixed \(\epsilon>0\);
- satisfy \(E_A(N)=o(\sqrt N)\).

Thus Q1 and Q2 could both have affirmative answers. A full resolution of the database problem should address both questions separately.

---

## 2. What counts as a solution

### 2.1 Complete affirmative solution of Q1

A complete proof must show that for every \(A\subseteq\mathbb N\) and every fixed \(0<\epsilon<1/2\), there are positive constants \(c\) and \(N_0\) such that
\[
\#\{1\le n\le N:r_A(n)\ne1\}\ge cN^{1/2-\epsilon}
\]
for every integer \(N\ge N_0\).

It is not enough to prove this only:

- for infinitely many \(N\);
- on average over \(N\);
- for a restricted class of sets \(A\);
- for one fixed \(\epsilon\);
- under an additional regularity hypothesis on \(A\).

If uniformity in \(A\) is claimed, the proof must track the multiplicative constant accordingly.

### 2.2 Complete disproof of Q1

Under the fixed-\(A\) reading, a disproof requires one set \(A\subseteq\mathbb N\) and one \(\epsilon_0\in(0,1/2)\) such that
\[
E_A(N)\ne\Omega(N^{1/2-\epsilon_0}).
\]
Equivalently,
\[
\liminf_{N\to\infty}
\frac{E_A(N)}{N^{1/2-\epsilon_0}}=0.
\]
Thus one must prove that for every \(c>0\), there are arbitrarily large \(N\) with
\[
E_A(N)<cN^{1/2-\epsilon_0}.
\]

The set \(A\) may be given by a formula, algorithm, recursion, or block construction, but the proof must establish rigorously:

1. which integers belong to \(A\);
2. how every representation \(a+a'=n\) is classified;
3. that the claimed exceptional bound holds at the required scales;
4. that no elements of later construction stages create unaccounted representations of earlier integers.

The last point is automatic only when all newly added elements exceed the earlier range, using positivity of the summands.

For the stronger uniform-in-\(A\) reading, the formal negation is weaker: \(A\) may depend on the proposed universal constant. A single-set counterexample as above would nevertheless be the mathematically more decisive disproof.

### 2.3 Complete affirmative solution of Q2

One must construct a single \(A\subseteq\mathbb N\) and prove
\[
\lim_{N\to\infty}\frac{E_A(N)}{\sqrt N}=0.
\]
Control only at selected endpoints \(N_j\) is insufficient unless accompanied by a valid interpolation argument covering every \(N_j<N<N_{j+1}\).

### 2.4 Complete negative solution of Q2

The exact negation of Q2 is:
\[
\forall A\subseteq\mathbb N,\qquad
\limsup_{N\to\infty}\frac{E_A(N)}{\sqrt N}>0.
\]
Equivalently, for every \(A\) there is a constant \(\delta_A>0\) and infinitely many \(N\) such that
\[
E_A(N)\ge\delta_A\sqrt N.
\]

A stronger theorem such as
\[
E_A(N)\ge c\sqrt N
\quad\text{for all sufficiently large }N
\]
would certainly settle Q2 negatively, but is not logically necessary.

### 2.5 What a full solution of the database entry should do

Because Q1 and Q2 are independent, a full solution should record one of the four possible answer pairs:
\[
(\text{Q1 yes/no},\ \text{Q2 yes/no}),
\]
with a proof of each component.

---

## 3. What does not count

The following do not resolve Q1:

1. A bound
   \[
   E_A(N)\gg N^\alpha
   \]
   for one fixed \(\alpha<1/2\). This leaves all exponents between \(\alpha\) and \(1/2\) untreated.

2. A lower bound holding only for infinitely many \(N\).

3. A lower bound for “most” \(N\), or an averaged estimate such as
   \[
   \sum_{n\le X}E_A(n)\gg X^{3/2-\epsilon}.
   \]

4. A result assuming that \(A\) has a density, regular counting function, bounded gaps, pseudorandomness, or controlled representation multiplicities.

5. A conditional result depending on an unproved conjecture.

6. A lower bound on the total representation count
   \[
   \sum_{n\le N}r_A(n)
   \]
   without converting it into a bound on the support of \(r_A(n)-1\).

The following do not resolve Q2:

1. A construction satisfying
   \[
   E_A(N)\ll_\epsilon N^{1/2+\epsilon}.
   \]
   This is much weaker than \(o(\sqrt N)\).

2. Finite sets \(A_N\subseteq[1,N]\) with \(E_{A_N}(N)=o(\sqrt N)\), unless the \(A_N\) can be made compatible as truncations of one infinite set.

3. A single infinite \(A\) with
   \[
   E_A(N_j)=o(\sqrt{N_j})
   \]
   only along a sparse subsequence.

4. Numerical evidence that \(E_A(N)/\sqrt N\) decreases over accessible ranges.

5. A heuristic random model. Naive independent random models generally produce Poisson-like representation counts and cannot make the probability of exactly one representation tend to \(1\).

---

## 4. Known results and context

### 4.1 Claimed infinite construction

According to the database commentary, Erdős attributed to Erdős, Sárközy, and Szemerédi a construction of an infinite \(A\subseteq\mathbb N\) such that, for every \(\epsilon>0\),
\[
E_A(N)\ll_\epsilon N^{1/2+\epsilon}
\]
for all sufficiently large \(N\).

For the same construction, it is claimed that for every \(\epsilon>0\), there are infinitely many \(N\) with
\[
E_A(N)\gg_\epsilon N^{1/3-\epsilon}.
\]

These estimates leave both questions open:

- the upper bound \(N^{1/2+\epsilon}\) does not imply \(o(\sqrt N)\);
- the lower bound \(N^{1/3-\epsilon}\), even on infinitely many scales, is far short of the proposed \(N^{1/2-\epsilon}\) bound for all large \(N\).

The database notes that the construction is attributed without a clear reference, so any use of its detailed structure should be checked against an original source.

### 4.2 Erdős–Freud finite analogue

As reported in the commentary, Erdős and Freud proved that for every \(N\) there exists
\[
X\subseteq\{1,\dots,N\}
\]
such that fewer than
\[
2^{3/2}\sqrt N
\]
integers in \(\{1,\dots,N\}\) fail to have exactly one unordered representation as a sum of two elements of \(X\).

Define the finite extremal function
\[
D(N)=
\min_{X\subseteq[1,N]}
\#\{1\le n\le N:r_X(n)\ne1\}.
\]
On the standard reading of the finite theorem,
\[
D(N)<2^{3/2}\sqrt N.
\]

Erdős and Freud reportedly suggested that \(2^{3/2}\) might be the optimal leading constant. This is only a conjectural indication, not a known lower bound.

The finite and infinite problems are linked by
\[
E_A(N)=E_{A\cap[1,N]}(N),
\]
indeed \(A\cap[1,N-1]\) suffices under the positive-integer convention. Consequently:

- any universal finite lower bound for \(D(N)\) applies immediately to every infinite \(A\);
- finite upper constructions do not automatically produce one infinite \(A\), because minimizers at different \(N\) need not be nested or even approximately compatible.

In particular, a theorem
\[
D(N)\ge c\sqrt N
\]
for all large \(N\) would answer Q2 negatively and prove a much stronger form of Q1.

### 4.3 Sidon sets

A Sidon set, or \(B_2\)-set, is a set whose unordered pair sums are all distinct. Classical Erdős–Turán theory gives
\[
\max\{|S|:S\subseteq[1,N]\text{ is Sidon}\}
=(1+o(1))\sqrt N,
\]
with algebraic lower constructions due to Singer and Bose–Chowla.

The present problem is not simply a Sidon-set problem:

- \(A\) is allowed to have many repeated sums;
- only sums in \([1,N]\) matter at scale \(N\);
- repeated representations may be concentrated on a small exceptional set;
- pair sums exceeding \(N\) are irrelevant to \(E_A(N)\).

Nevertheless, Sidon bounds and their stability versions are natural tools because every equality
\[
a+b=c+d
\]
produces a nonunique sum.

### 4.4 Generating function identity

For \(|z|<1\), let
\[
F_A(z)=\sum_{a\in A}z^a.
\]
Then
\[
\sum_{n\ge1}r_A(n)z^n
=
\frac{F_A(z)^2+F_A(z^2)}2.
\]
The \(F_A(z^2)\) term accounts for diagonal representations.

Writing
\[
h_A(n)=r_A(n)-1,
\]
one has
\[
\operatorname{supp}(h_A)\cap[1,N]
=
\{1\le n\le N:r_A(n)\ne1\},
\]
so
\[
E_A(N)=\#\{n\le N:h_A(n)\ne0\}.
\]
This gives a direct analytic formulation, but the values \(h_A(n)\) on the exceptional set may be arbitrarily large.

### 4.5 Erdős–Fuchs and Erdős–Turán

The Erdős–Fuchs theorem rules out certain excessively accurate linear asymptotics for cumulative additive representation functions; in one standard formulation, an estimate of the shape
\[
\sum_{n\le x}r_A(n)
=
cx+o\!\left(x^{1/4}(\log x)^{-1/2}\right)
\]
cannot hold. It is relevant in spirit but does not directly settle this problem, because a small support for \(r_A(n)-1\) does not control the sizes of the positive values on that support.

The Erdős–Turán conjecture asserts that the representation function of every asymptotic basis of order two is unbounded. A set with \(r_A(n)=1\) for all sufficiently large \(n\) would be an especially strong counterexample to Erdős–Turán. However,
\[
E_A(N)=o(\sqrt N)
\]
still permits infinitely many unrepresented integers, so Q2 is not known to be equivalent to the Erdős–Turán conjecture and would not directly settle it.

---

## 5. Traps and edge cases

### 5.1 Ordered versus unordered representations

The correct formula is
\[
r_A(n)=\#\{a\le a':a,a'\in A,\ a+a'=n\}.
\]
Counting ordered pairs changes the problem drastically. Computational work should use
\[
r_A(n)=
\frac{c_A(n)+d_A(n)}2,
\]
where
\[
c_A(n)=\sum_{a=1}^{n-1}1_A(a)1_A(n-a)
\]
is the ordered convolution and
\[
d_A(n)=
\begin{cases}
1_A(n/2),&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}
\]

### 5.2 Diagonal representations matter at the target scale

Disallowing \(a=a'\) replaces the generating function by
\[
\frac{F_A(z)^2-F_A(z^2)}2.
\]
There may be on the order of \(\sqrt N\) relevant diagonals, exactly the scale under investigation. The distinction cannot be treated as negligible.

### 5.3 Positive versus nonnegative integers

This brief uses \(\mathbb N=\{1,2,\dots\}\). If \(0\in A\) is allowed, every \(a\in A\) yields a representation \(a=0+a\), which materially changes the problem. Any source using \(\mathbb N=\{0,1,\dots\}\) must be normalized carefully.

### 5.4 The exceptional set has two different causes

One must distinguish
\[
Z_A(N)=\#\{n\le N:r_A(n)=0\},
\qquad
M_A(N)=\#\{n\le N:r_A(n)\ge2\},
\]
with
\[
E_A(N)=Z_A(N)+M_A(N).
\]

The total excess multiplicity
\[
\Delta_A(N)=\sum_{\substack{n\le N\\r_A(n)\ge2}}(r_A(n)-1)
\]
can be much larger than \(M_A(N)\). An argument bounding \(\Delta_A(N)\) does not automatically bound the number of exceptional sums in the desired direction.

Indeed,
\[
\sum_{n\le N}r_A(n)=N-Z_A(N)+\Delta_A(N),
\]
which does not determine \(E_A(N)\).

### 5.5 Collisions can be concentrated

Many additive quadruples may correspond to a small number of highly represented exceptional sums. Energy arguments that count quadruples must prevent this concentration before deducing a lower bound on \(E_A(N)\).

### 5.6 Sums beyond \(N\) are irrelevant at scale \(N\)

A global Sidon bound counts all pair-sum collisions. Here a collision at a sum \(>N\) does not affect \(E_A(N)\). Likewise, elements near \(N\) may have almost no effect on representations in \([1,N]\).

### 5.7 Finite minimizers need not be nested

Choosing an optimal \(X_N\subseteq[1,N]\) separately for each \(N\) does not define an infinite set. A diagonal or compactness argument must preserve exact representation information, and later choices can conflict with earlier optimal configurations.

### 5.8 Subsequence control does not imply all-\(N\) control

Although \(E_A(N)\) is nondecreasing, the normalization \(\sqrt N\) changes. If \(N_{j+1}/N_j\) is very large, a good bound at \(N_j\) says almost nothing about intermediate \(N\). Interpolation is safe only when the scale ratios are quantitatively controlled.

### 5.9 The first and second questions are compatible

Do not claim that proving Q1 rules out Q2. A lower bound \(N^{1/2-\epsilon}\) for every fixed \(\epsilon\) is compatible with \(o(\sqrt N)\).

---

## 6. Verification hooks

### 6.1 Exact computation of \(E_A(N)\)

For a finite bit vector \(x_a=1_A(a)\), compute the integer convolution
\[
c_n=\sum_{a=1}^{n-1}x_ax_{n-a}.
\]
Then compute
\[
r_A(n)=\frac{c_n+1_{\{2\mid n\}}x_{n/2}}2.
\]
Finally,
\[
E_A(N)=\sum_{n=1}^N1_{\{r_A(n)\ne1\}}.
\]

This can be implemented by:

- direct \(O(N^2)\) convolution for exact small cases;
- FFT/NTT convolution with exact reconstruction for larger cases;
- bitset methods if only zero/one/two-or-more information is needed.

All final certificates should use exact integer arithmetic.

### 6.2 Exhaustive finite optimization

Compute
\[
D(N)=\min_{X\subseteq[1,N]}E_X(N)
\]
for small \(N\). Since \(x_N\) cannot contribute to a sum at most \(N\), only \(x_1,\dots,x_{N-1}\) need be searched.

For each unordered pair \(1\le i\le j\) with \(i+j\le N\), introduce
\[
p_{ij}=x_ix_j.
\]
Then
\[
r(n)=\sum_{\substack{i\le j\\i+j=n}}p_{ij}.
\]
A CP-SAT or MILP model can maximize the number of \(n\) for which \(r(n)=1\), using exact cardinality indicator constraints.

Useful outputs include:

- \(D(N)\);
- \(D(N)/\sqrt N\);
- the separate counts of missing and multiply represented integers;
- the multiplicity histogram \(\#\{n:r(n)=k\}\);
- the location of exceptional sums.

### 6.3 Nested extension search

To test infinite-construction ideas, fix a successful initial pattern
\[
A\cap[1,N_j]
\]
and optimize the new variables in \((N_j,N_{j+1}]\). Record whether near-optimal finite configurations can be extended without destroying earlier performance.

Because later positive elements cannot represent earlier integers, earlier representation counts remain fixed. The obstruction is therefore not backward interference but the inability of a fixed prefix to participate optimally at all later scales.

### 6.4 Collision concentration diagnostics

For each candidate \(A\), compute
\[
\Delta_A(N)=\sum_{n\le N}(r_A(n)-1)_+
\]
and
\[
\mathcal E_A(N)=\sum_{n\le N}r_A(n)^2.
\]
Compare these with
\[
M_A(N)=\#\{n\le N:r_A(n)\ge2\}.
\]
A large ratio \(\Delta_A(N)/M_A(N)\) or \(\mathcal E_A(N)/M_A(N)\) indicates that an energy-to-support argument is losing information through concentration.

### 6.5 Block-profile checks

For dyadic intervals
\[
I_j=(2^{j-1},2^j],
\]
record
\[
a_j=|A\cap I_j|.
\]
Compute how many unique sums in a target dyadic interval arise from each block pair \(I_i+I_j\). This tests claims that a near-perfect configuration must have a particular multiscale density profile.

### 6.6 Modular experiments

For small moduli \(q\), optimize over \(S\subseteq\mathbb Z/q\mathbb Z\) the number of residues having exactly one unordered representation as \(s+s'\). Record:

- the maximum number of uniquely represented residues;
- whether repeated sums concentrate on a few residues;
- the Fourier spectrum of \(1_S\);
- how the answer changes for prime, prime-power, and composite \(q\).

Any transfer back to intervals must separately account for carries and sums outside \([1,N]\).

---

## 7. Attack routes

### Route 1: Finite extremal lower bound via Sidon stability

**Core idea.** Study \(D(N)\) directly. If almost every \(n\le N\) has one representation, then the relevant portion of \(A\) behaves like a highly efficient but only partially Sidon set. Combine pair counting, difference counting, and boundary information.

**Key lemma needed.** A theorem of the form
\[
D(N)\ge N^{1/2-o(1)},
\]
or preferably
\[
D(N)\ge(c-o(1))\sqrt N
\]
for an absolute \(c>0\).

A more structural version would say that if \(E_X(N)=o(\sqrt N)\), then the induced pair-sum system violates a Sidon-type inequality.

**Why it might work.** The finite theorem already places the natural scale at \(\sqrt N\). Covering almost all of \([1,N]\) once requires many useful pairs, while avoiding duplicate low sums imposes Sidon-like restrictions. The tension should be strongest near the critical cardinality \(|X|\asymp\sqrt N\).

**Likely failure point.** Standard Sidon bounds treat all pair sums symmetrically, while this problem ignores sums above \(N\). Moreover, all unavoidable collisions may be concentrated on a small number of exceptional low sums.

**Quick blockage test.** For computed finite optimizers, measure:

- how many pair collisions occur below and above \(N\);
- whether low-sum collisions are concentrated;
- whether \(|X\cap[1,N/2]|\) nearly saturates any known Sidon bound.

If near-optimal examples evade every natural Sidon stability statistic, a direct global Sidon argument is probably too coarse.

---

### Route 2: Generating functions and an Erdős–Fuchs-type support theorem

**Core idea.** Use
\[
\frac{F(z)^2+F(z^2)}2
=
\sum_{n\ge1}(1+h_n)z^n,
\qquad
\#\{n\le N:h_n\ne0\}=E_A(N).
\]
Apply Parseval, carefully chosen kernels, or integration near the unit circle to show that the coefficient error \(h_n\) cannot have support smaller than \(N^{1/2-o(1)}\).

**Key lemma needed.** A support-sensitive analytic inequality that exploits the special form of \(F\), for example:
\[
\#\{n\le N:h_n\ne0\}\ge N^{1/2-o(1)}
\]
whenever \(h_n\) arises from an unordered additive representation function.

Such a lemma must remain effective even if a few positive \(h_n\) are very large.

**Why it might work.** The target statement concerns the support of the exact coefficient defect, and the generating-function identity captures exact uniqueness without losing diagonal information. Erdős–Fuchs methods show that additive generating functions cannot imitate the geometric series too accurately.

**Likely failure point.** Parseval controls
\[
\sum |h_n|^2,
\]
not the support of \(h_n\). A small number of exceptional sums with huge multiplicity may absorb all analytic discrepancy. This is the principal obstruction to applying Erdős–Fuchs directly.

**Quick blockage test.** Search finite optimizers for examples with very small \(E_X(N)\) but very large
\[
\max_{n\le N}r_X(n)
\quad\text{or}\quad
\sum_{n\le N}(r_X(n)-1)^2.
\]
If this concentration grows rapidly with \(N\), any proposed \(L^2\)-to-support inequality needs genuinely additive input.

---

### Route 3: Modular/Fourier reduction to near-perfect cyclic sum systems

**Core idea.** Project a carefully selected interval of \(A\) modulo \(q\). Near-unique representations on a long interval should induce a set in \(\mathbb Z/q\mathbb Z\) for which most residues have exactly one representation. Fourier analysis or cyclic Sidon bounds may prohibit this.

**Key lemma needed.** A transference theorem converting
\[
E_A(N)\ll N^{1/2-\delta}
\]
into a cyclic system with \(q-o(q)\) uniquely represented residues and controlled folded multiplicities.

Alternatively, prove a strong cyclic inequality and average over moduli or translates to control carries.

**Why it might work.** In a finite group, convolution and Fourier analysis are exact:
\[
\widehat{1_S*1_S}(\chi)=\widehat{1_S}(\chi)^2.
\]
Near-constant convolution is strongly constrained by integrality, positivity, and Parseval. Difference-set and perfect-difference-set theory may supply sharp obstructions.

**Likely failure point.** Reduction modulo \(q\) folds many integer sums onto the same residue. Pairs whose integer sums lie outside the target interval can create arbitrary modular multiplicities, destroying exact uniqueness.

**Quick blockage test.** Take good finite interval examples and project them modulo several \(q\) near \(\sqrt N\) and \(N\). If almost all modular residues immediately become highly represented, naive modular projection is unusable; a random translate/window lemma would be essential.

---

### Route 4: Multiscale rigidity and extension inequalities

**Core idea.** Decompose \(A\) into dyadic or geometrically growing blocks. Unique representations in successive intervals impose constraints on which block pairs can supply those representations. Derive a recurrence forcing exceptional sums at every sufficiently large scale.

**Key lemma needed.** A rigidity or extension statement such as:

> If a prefix \(A\cap[1,N]\) produces at most \(E\) exceptions up to \(N\), then every extension to scale \(\lambda N\) creates at least
> \[
> c\sqrt N-\Phi(E)
> \]
> new exceptions in some controlled intermediate interval.

Iterating a weaker exponent-sensitive version could prove Q1.

**Why it might work.** An infinite set must use the same lower-scale elements at every future scale. This compatibility requirement is absent from the finite theorem and may be precisely what forces a lower bound for all large \(N\).

**Likely failure point.** A highly nonuniform construction may alternate between different block-pair mechanisms at different scales, placing collisions in moving “reservoir” intervals. Coarse block counts may not detect exact pair-sum structure.

**Quick blockage test.** Run nested CP-SAT searches with several growth ratios \(N_{j+1}/N_j\), fixing near-optimal prefixes. If extensions remain nearly as good as unrestricted finite optimizers over many stages, a simple one-step rigidity lemma is unlikely.

---

### Route 5: Hierarchical construction aimed at Q2 and at disproving Q1

**Core idea.** Build
\[
A=A_1\cup(M_1+A_2)\cup(M_2+A_3)\cup\cdots
\]
with rapidly separated blocks. Use mixed-radix, Singer/Bose–Chowla, or direct-sum structures so that cross-block sums cover long target intervals exactly once, while same-block sums and unwanted cross sums are confined to sparse exceptional reservoirs.

**Key lemma needed.** An extension lemma producing a larger prefix \(A'\) from \(A\) such that:

1. all previous representation counts are preserved;
2. almost every new integer is represented exactly once;
3. the cumulative deficit satisfies
   \[
   E_{A'}(N)\le\eta\sqrt N
   \]
   throughout the new range, with \(\eta\to0\).

For a disproof of Q1, one would need the substantially stronger conclusion
\[
E_A(N_j)=o(N_j^{1/2-\epsilon_0})
\]
at arbitrarily large scales.

**Why it might work.** Cross sums \(L+(M+R)\) behave like a direct sum \(L+R\) and can cover an interval uniquely even when \(L\cup(M+R)\) is not globally Sidon. Scale separation prevents later elements from changing earlier sums.

**Likely failure point.** Every block boundary tends to create \(\Theta(\sqrt N)\) uncovered or multiply represented integers. The conjectured optimality of the Erdős–Freud constant suggests that this boundary loss may be irreducible. Superexponential scale separation also leaves disastrous intermediate ranges.

**Quick blockage test.** Impose a fixed prefix and optimize one added block. Plot the best possible maximum of
\[
E_A(N)/\sqrt N
\]
over every intermediate \(N\), not just the endpoint. If a stable positive barrier appears and is localized near block transitions, the hierarchical construction is blocked unless those transitions can be overlapped.

---

### Route 6: Classification of near-extremal finite configurations

**Core idea.** Rather than prove a lower bound immediately, first classify all \(X\subseteq[1,N]\) with
\[
E_X(N)\le C\sqrt N.
\]
Show that they must resemble a small family of algebraic or geometric models, then determine whether such models can be nested indefinitely.

**Key lemma needed.** A stability theorem: every near-extremizer is close, in symmetric difference or pair-sum structure, to an Erdős–Freud/Sidon-type construction, with quantitative error \(o(\sqrt N)\).

A second incompatibility lemma would show that near-extremizers at substantially different scales cannot be consistent truncations unless they incur a positive \(\sqrt N\)-scale deficit.

**Why it might work.** The finite upper constant suggests a rigid extremal phenomenon. Infinite compatibility may be more tractable once the finite shapes are understood.

**Likely failure point.** There may be many inequivalent near-extremizers, especially because arbitrary behavior on high elements affects only sums above \(N\). Stability in symmetric difference may be false even if representation profiles are stable.

**Quick blockage test.** Enumerate or sample all optimizers for small \(N\), quotienting by identical low-sum representation profiles. If the number of structurally different optimizers grows rapidly, a simple classification theorem is unlikely; one may instead need stability of representation measures rather than of the sets themselves.

---

## 8. Verdict on difficulty

This is a genuinely difficult open problem at the intersection of additive bases, Sidon-set theory, extremal additive combinatorics, and analytic representation-function methods.

The target exponent \(1/2\) is not accidental:

- the Erdős–Freud finite construction has deficit \(O(\sqrt N)\);
- relevant set sizes and Sidon bounds naturally occur at scale \(\sqrt N\);
- diagonal representations and interval-boundary effects also occur at this scale.

The main technical obstruction is that nonuniqueness can be concentrated: a very small exceptional set may carry a huge number of pair-sum collisions. This defeats straightforward pair counting, additive-energy arguments, and direct Erdős–Fuchs estimates.

The infinite problem has a second obstruction absent from ordinary finite extremal questions: one set must work compatibly at every scale. Conversely, finite lower bounds would immediately settle major parts of the problem, while finite upper constructions do not automatically globalize.

The problem is related to the Erdős–Turán conjecture on additive bases, but it is **not known to be equivalent to it**, and \(E_A(N)=o(\sqrt N)\) would not by itself produce an asymptotic basis. Thus one should not claim that solving this problem necessarily solves Erdős–Turán. Nevertheless, the same rigidity of additive representation functions is involved, and methods capable of resolving this problem may have consequences for that broader circle of conjectures.

The most promising first objective is a sharp finite extremal or stability theorem for \(D(N)\). The most plausible counterexample program is a multiscale direct-sum construction that explicitly controls every intermediate scale. Either direction will require a mechanism substantially stronger than routine Sidon counting or generic Fourier estimates.