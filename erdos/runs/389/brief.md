# Problem brief: Erdős Problem #389

## 1. Precise statement

For integers \(n,k\ge 1\), define the two products of \(k\) consecutive positive integers
\[
A(n,k):=\prod_{i=0}^{k-1}(n+i)
\]
and
\[
B(n,k):=\prod_{i=0}^{k-1}(n+k+i).
\]

The problem asks whether
\[
\boxed{\forall n\in \mathbb Z_{\ge 1}\ \exists k\in\mathbb Z_{\ge 1}
\quad A(n,k)\mid B(n,k).}
\]

Here \(A\mid B\) means that there is an integer \(Q\ge 1\) such that \(B=QA\). The integer \(k\) may depend on \(n\), and no upper bound on \(k\) is prescribed.

The standard interpretation requires \(k\ge 1\). If \(k=0\) were allowed, both products would be empty products equal to \(1\), making the problem trivial.

### Factorial formulation

Put
\[
m:=n-1\ge 0.
\]
Then
\[
A(n,k)=\frac{(m+k)!}{m!},
\qquad
B(n,k)=\frac{(m+2k)!}{(m+k)!}.
\]
Thus the desired quotient is
\[
R_m(k):=\frac{B(n,k)}{A(n,k)}
       =\frac{(m+2k)!\,m!}{(m+k)!^2}.
\]

Therefore the problem is equivalently
\[
\boxed{\forall m\in\mathbb Z_{\ge 0}\ \exists k\in\mathbb Z_{\ge 1}
\quad R_m(k)\in\mathbb Z.}
\]

### Binomial-coefficient formulation

Since
\[
\frac{\binom{m+2k}{k}}{\binom{m+k}{k}}
=
\frac{(m+2k)!\,m!}{(m+k)!^2},
\]
the problem is also equivalent to
\[
\boxed{\forall m\ge 0\ \exists k\ge 1
\quad
\binom{m+k}{k}\mid \binom{m+2k}{k}.}
\]

### Exact \(p\)-adic formulation

For a prime \(p\), Legendre’s formula gives
\[
v_p(R_m(k))
=
\sum_{a\ge 1}
\left(
\left\lfloor\frac{m+2k}{p^a}\right\rfloor
+
\left\lfloor\frac{m}{p^a}\right\rfloor
-
2\left\lfloor\frac{m+k}{p^a}\right\rfloor
\right).
\]
The sum is finite because all terms with \(p^a>m+2k\) vanish. Hence
\[
R_m(k)\in\mathbb Z
\quad\Longleftrightarrow\quad
v_p(R_m(k))\ge 0
\quad\text{for every prime }p.
\]

By Kummer’s theorem, if \(c_p(x,y)\) denotes the number of carries, counted with multiplicity by digit position, when \(x\) and \(y\) are added in base \(p\), then
\[
v_p(R_m(k))
=
c_p(k,m+k)-c_p(k,m).
\]
Thus one needs at least as many total base-\(p\) carries in \(k+(m+k)\) as in \(k+m\), for every prime \(p\).

---

## 2. What counts as a solution

### A complete affirmative solution

A complete proof must establish, unconditionally, that for every \(m\ge 0\) there is at least one positive integer \(k\) satisfying
\[
\frac{(m+2k)!\,m!}{(m+k)!^2}\in\mathbb Z.
\]

Any of the following would suffice:

1. **An explicit construction:** give a function \(k=k(m)\) and prove that it works for every \(m\).
2. **An effective existence theorem:** prove that a solution exists below some finite bound \(K(m)\), even if \(K(m)\) is extremely large.
3. **A nonconstructive existence proof:** prove existence for every \(m\) without explicitly locating \(k\).
4. **A stronger result:** for example, prove that every \(m\) has infinitely many suitable \(k\), or a positive density of suitable \(k\).

A computer-assisted proof would count if it reduces the universal assertion to finitely many rigorously certified computations and all algorithms, bounds, and arithmetic certificates are reproducible.

### A complete disproof

A disproof must exhibit some explicit
\[
m_0\ge 0
\quad\text{equivalently}\quad
n_0=m_0+1\ge 1
\]
and prove
\[
\forall k\ge 1,\qquad R_{m_0}(k)\notin\mathbb Z.
\]

Equivalently, it must prove that for every \(k\ge 1\) there exists a prime \(p=p(k)\) such that
\[
v_p(R_{m_0}(k))<0.
\]

An explicit counterexample is therefore not verified merely by searching many values of \(k\). It needs an infinite obstruction, such as:

- a rule producing an obstructing prime \(p(k)\) for every \(k\);
- a finite covering of all \(k\) by cases, with a certified valuation deficit in each case;
- or a proof reducing all sufficiently large \(k\) to a general obstruction, together with finite verification of the remaining \(k\).

---

## 3. What does not count

The following do not resolve the problem:

1. Verifying the assertion for \(n\le N\), for any fixed finite \(N\).
2. Finding successful \(k\) for infinitely many \(n\), unless all \(n\) are covered.
3. Proving the assertion for a density-one set of \(n\), or for all \(n\) in selected congruence classes.
4. Proving existence only under an unproved conjecture about primes, prime gaps, smooth numbers, or random models.
5. Showing that \(R_m(k)>1\), or that \(R_m(k)\to\infty\). Size has no bearing on integrality.
6. Showing that each individual denominator factor is smaller than some numerator factor.
7. Finding a necessary condition on \(k\), such as the absence of primes in a short interval, without proving that some \(k\) satisfies all valuation conditions.
8. Proving that each relevant floor summand is “usually” nonnegative, or that the expected valuation is positive.
9. A computational search that fails to find a solution up to a very large cutoff.
10. Proving a stronger sufficient condition, such as Gaussian-binomial divisibility, fails for some \(m\). Failure of a sufficient condition is not a counterexample to the original problem.
11. An asymptotic theorem that leaves an uncontrolled exceptional set of \(n\). A theorem for all sufficiently large \(n\) would resolve the problem only after the finite remaining set is rigorously checked.

---

## 4. Known results and context

The problem was asked by Erdős and Straus and remains open according to the supplied database record.

### Settled small cases

For \(n=1\), so \(m=0\),
\[
R_0(k)=\frac{(2k)!}{k!^2}=\binom{2k}{k},
\]
which is an integer for every \(k\ge 1\). Thus \(n=1\) is completely settled.

For \(n=2\), \(m=1\), the displayed solution is \(k=5\):
\[
R_1(5)=\frac{11!}{6!^2}=77.
\]
In fact \(k=5\) is minimal, since
\[
R_1(1)=\frac32,\quad
R_1(2)=\frac{10}{3},\quad
R_1(3)=\frac{35}{4},\quad
R_1(4)=\frac{126}{5}.
\]

For \(n=3\), \(m=2\), the displayed solution is \(k=4\):
\[
R_2(4)=\frac{10!\,2!}{6!^2}=14.
\]
It is minimal because
\[
R_2(1)=\frac43,\quad
R_2(2)=\frac52,\quad
R_2(3)=\frac{28}{5}.
\]

The database commentary reports that Bhavik Mehta computed the minimal suitable \(k\) for every \(1\le n\le 18\); these values are recorded as OEIS A375071. Thus existence for those finitely many \(n\) is settled by explicit witnesses, and minimality can be certified by exact finite valuation checks.

### Relevant standard theorems

#### Legendre’s formula

For a prime \(p\),
\[
v_p(N!)=\sum_{a\ge 1}\left\lfloor\frac{N}{p^a}\right\rfloor.
\]
This yields the exact local criterion above.

#### Kummer’s theorem

For integers \(0\le b\le a\),
\[
v_p\binom{a}{b}
\]
equals the number of carries in the base-\(p\) addition of \(b\) and \(a-b\). It converts the problem into simultaneous carry inequalities over all primes.

#### Cyclotomic factorization of Gaussian binomial coefficients

Let \(\binom{a}{b}_q\) denote the Gaussian binomial coefficient. The exponent of the cyclotomic polynomial \(\Phi_d(q)\) in \(\binom{a}{b}_q\) is
\[
\left\lfloor\frac ad\right\rfloor
-
\left\lfloor\frac bd\right\rfloor
-
\left\lfloor\frac{a-b}{d}\right\rfloor.
\]
Consequently
\[
\frac{\binom{m+2k}{k}_q}{\binom{m+k}{k}_q}\in\mathbb Z[q]
\]
if and only if
\[
e_d(m,k):=
\left\lfloor\frac{m+2k}{d}\right\rfloor
+
\left\lfloor\frac m d\right\rfloor
-
2\left\lfloor\frac{m+k}{d}\right\rfloor
\ge 0
\]
for every \(d\ge 2\).

This is a sufficient condition for the original problem, because specializing at \(q=1\) gives the ordinary binomial quotient. It is generally stronger: ordinary integrality only requires
\[
\sum_{a\ge1} e_{p^a}(m,k)\ge0
\]
for each prime \(p\), allowing cancellation between different powers of the same prime.

#### Landau-type factorial-ratio criteria

Landau’s theorem characterizes factorial ratios that are integral for every value of a scaling parameter through nonnegativity of an associated floor function. It is conceptually relevant, but it does not directly resolve this problem: here \(m\) is fixed, the arguments are affine in \(k\), and only the existence of one \(k\) is required.

### Exact recurrence

The quotients satisfy
\[
R_m(0)=1
\]
and
\[
\frac{R_m(k+1)}{R_m(k)}
=
\frac{(m+2k+1)(m+2k+2)}{(m+k+1)^2}.
\]
Thus
\[
v_p(R_m(k+1))
=
v_p(R_m(k))
+v_p(m+2k+1)+v_p(m+2k+2)-2v_p(m+k+1).
\]
This is useful computationally and may expose inductive structure, but it does not itself preserve integrality.

---

## 5. Traps and edge cases

### 5.1 Allowing \(k=0\) trivializes the problem

The intended domain is \(k\ge 1\). With \(k=0\), both products are empty and equal to \(1\).

### 5.2 Off-by-one errors

With \(m=n-1\), the left block is
\[
m+1,m+2,\ldots,m+k,
\]
and the right block is
\[
m+k+1,m+k+2,\ldots,m+2k.
\]
Hence the quotient is
\[
\frac{(m+2k)!\,m!}{(m+k)!^2},
\]
not a version shifted by one factorial.

### 5.3 Individual floor terms need not be nonnegative

For ordinary integrality one needs
\[
\sum_{a\ge1} e_{p^a}(m,k)\ge0
\]
for each prime \(p\). A negative contribution at \(p^a\) can be canceled by a positive contribution at another power of the same prime.

Therefore requiring every \(e_{p^a}(m,k)\ge0\), or every \(e_d(m,k)\ge0\), is stronger than necessary.

### 5.4 Carry domination need only hold in total

Kummer gives a comparison of the total number of carries. Requiring carry domination at each digit position separately is a stronger condition and may incorrectly exclude genuine solutions.

### 5.5 Pairwise term matching is too strong

It is not necessary to pair each number in the left block with a divisible number in the right block. Prime factors may be distributed across many numerator terms. Any termwise or permutation-based matching argument proves only a sufficient condition.

### 5.6 A useful large-prime obstruction

Let
\[
x=m+k.
\]
If there is a prime \(p\) satisfying
\[
p>m,\qquad \frac{m+2k}{2}<p\le m+k,
\]
then
\[
v_p(R_m(k))=-1.
\]
Indeed,
\[
v_p((m+2k)!)=1,\quad v_p(m!)=0,\quad v_p((m+k)!)=1,
\]
because \(p\le m+k\) but \(2p>m+2k\).

Thus a necessary condition for success is that
\[
\left(k+\frac m2,\;k+m\right]
\]
contain no prime greater than \(m\).

The endpoints matter: the lower endpoint is strict. If \(2p=m+2k\), then the numerator factorial contains both \(p\) and \(2p\), eliminating this particular deficit.

More generally, if
\[
p>m,\qquad p^2>m+2k,
\]
and \(r\) is the residue of \(m+k\) modulo \(p\), then
\[
v_p(R_m(k))
=
\left\lfloor\frac{2r-m}{p}\right\rfloor.
\]
In particular,
\[
2r<m\quad\Longrightarrow\quad v_p(R_m(k))=-1.
\]

This is a strong source of failure certificates, but proving that such a prime exists for every \(k\) is difficult. Bertrand’s postulate does not apply to these fixed-length intervals, and large prime gaps prevent naïve short-interval arguments.

### 5.7 Huge quotient does not imply integrality

For fixed \(m\), \(R_m(k)\) grows exponentially in \(k\), roughly on the scale of a central binomial coefficient times a power of \(k^{-1}\). Nevertheless, a single uncanceled prime in the denominator destroys integrality.

### 5.8 Computation can certify success but not universal failure

For a fixed \(m,k\), integrality is finite and exactly checkable. For a fixed \(m\), failure for all \(k\) is an infinite statement and cannot be established by a search cutoff alone.

---

## 6. Verification hooks

### 6.1 Direct exact verification

For a proposed pair \((n,k)\), compute
\[
A=\prod_{i=0}^{k-1}(n+i),\qquad
B=\prod_{i=0}^{k-1}(n+k+i)
\]
using arbitrary-precision integers and test \(B\bmod A=0\).

For large parameters, prime valuations are preferable.

### 6.2 Valuation verifier

Given \(m,k\), enumerate all primes \(p\le m+2k\), and compute
\[
D_p=
\sum_{\substack{a\ge1\\p^a\le m+2k}}
\left(
\left\lfloor\frac{m+2k}{p^a}\right\rfloor
+
\left\lfloor\frac{m}{p^a}\right\rfloor
-
2\left\lfloor\frac{m+k}{p^a}\right\rfloor
\right).
\]

Then:

- \(R_m(k)\) is integral iff every \(D_p\ge0\).
- If \(D_p<0\), the prime \(p\) is a concise failure certificate.

### 6.3 Incremental search

For fixed \(m\), initialize all valuations at \(k=0\) to zero. Use
\[
D_p(k+1)=D_p(k)
+v_p(m+2k+1)+v_p(m+2k+2)-2v_p(m+k+1).
\]

With a smallest-prime-factor sieve up to \(m+2K\), this allows exact enumeration of all \(k\le K\) without repeatedly evaluating factorials.

To certify that a reported \(k_0\) is minimal:

1. store one obstructing prime \(p_k\) with \(D_{p_k}(k)<0\) for every \(1\le k<k_0\);
2. store all nonnegative valuations, or the exact integral quotient, for \(k=k_0\).

### 6.4 Carry-based verification

For each prime \(p\le m+2k\):

1. write \(m\), \(k\), and \(m+k\) in base \(p\);
2. count carries in \(k+m\);
3. count carries in \(k+(m+k)\);
4. verify that the second count is at least the first.

This provides an independent check of the Legendre implementation.

### 6.5 Gaussian-binomial sufficient-condition test

For each \(2\le d\le m+2k\), compute
\[
e_d(m,k)=
\left\lfloor\frac{m+2k}{d}\right\rfloor
+\left\lfloor\frac m d\right\rfloor
-2\left\lfloor\frac{m+k}{d}\right\rfloor.
\]
If all \(e_d(m,k)\ge0\), then the Gaussian-binomial quotient is a polynomial, hence \(R_m(k)\) is an integer.

This test can determine whether known solutions satisfy a stronger cyclotomic positivity property.

### 6.6 Obstruction-prime classification

For failed pairs \((m,k)\), record:

- the smallest prime \(p\) with \(D_p<0\);
- whether \(p^2>m+2k\);
- whether \(p\in((m+2k)/2,m+k]\);
- the residue \(r=(m+k)\bmod p\);
- the individual contributions \(e_{p^a}(m,k)\).

This can reveal whether failures are usually caused by large one-level primes, small-prime carry deficits, or cancellation phenomena.

---

## 7. Attack routes

### Route 1: Direct \(p\)-adic carry construction

**Core mechanism.** Construct \(k\) so that
\[
c_p(k,m+k)\ge c_p(k,m)
\]
for every prime \(p\).

**Key lemma needed.** A simultaneous digit-control theorem: for every fixed \(m\), one can choose \(k\) whose base-\(p\) digits satisfy the carry inequalities for all relevant primes, together with a proof that primes not explicitly controlled cannot create a deficit.

**Why it might work.** For any finite collection of primes, digit patterns can often be imposed through congruences modulo powers of those primes. Since \(m\) is fixed, the “bad” digit patterns might be avoidable by CRT.

**Likely failure point.** The set of relevant primes depends on the size of \(k\). Choosing \(k\) by CRT makes \(k\) large and introduces new primes and new prime powers. This circular growth is the central obstacle.

**Quick test.** For each known minimal solution, compute the full carry profiles. Check whether successful \(k\) exhibit a recognizable uniform pattern, such as no carries in \(k+m\), or forced carries in \(k+(m+k)\), for all small primes.

---

### Route 2: Gaussian-binomial or cyclotomic strengthening

**Core mechanism.** Seek \(k\) satisfying the stronger inequalities
\[
e_d(m,k)\ge0\qquad\text{for every }d\ge2.
\]
Then
\[
\binom{m+k}{k}_q\mid \binom{m+2k}{k}_q
\]
in \(\mathbb Z[q]\), and specialization at \(q=1\) solves the original instance.

**Key lemma needed.**
\[
\forall m\ge0\ \exists k\ge1\ \forall d\ge2,\qquad e_d(m,k)\ge0.
\]

**Why it might work.** The floor functions depend only on residues of \(m+k\) modulo \(d\). Cyclotomic positivity removes the delicate cancellation between prime powers and may admit a clean residue-based or geometric interpretation.

**Likely failure point.** The strengthening may be false even if the original problem is true. Some genuine integer quotients may rely essentially on cancellation between \(e_p,e_{p^2},\ldots\).

**Quick test.** Apply the \(e_d\)-test to every known solution for \(n\le18\), then search for each \(m\) for the least \(k\) satisfying the stronger condition. If some small \(m\) has ordinary solutions but no cyclotomic solution over a very large range, this route is probably too rigid.

---

### Route 3: Structured CRT construction around a composite interval

**Core mechanism.** Write \(x=m+k\), so
\[
R_m(k)=\frac{(2x-m)!\,m!}{x!^2}.
\]
First force the interval
\[
(x-m/2,x]
\]
to contain no primes, eliminating the simplest large-prime obstructions. Then impose additional congruences to balance small-prime valuations.

**Key lemma needed.** For every fixed \(m\), there exists an integer \(x>m\) satisfying both:

1. a prescribed composite covering of the last roughly \(m/2\) integers before \(x\);
2. all remaining valuation inequalities
   \[
   v_p((2x-m)!m!)\ge 2v_p(x!)
   \]
   for small and medium primes.

**Why it might work.** Arbitrarily long runs of composite numbers can be constructed by CRT. Since \(m\) is fixed, the dangerous endpoint interval has fixed length. The remaining small primes might be handled by choosing \(x\) modulo sufficiently high prime powers.

**Likely failure point.** Eliminating endpoint primes does not control medium-sized primes whose multiples occur asymmetrically around \(x\). CRT conditions for different valuation levels may conflict, and enlarging \(x\) again introduces uncontrolled primes.

**Quick test.** For each \(m\), construct \(x\) via a standard CRT composite-run covering, set \(k=x-m\), and compute the exact valuation deficits. Classify whether the remaining failures are confined to a bounded set of small primes or continually arise from new medium primes.

---

### Route 4: Analytic or probabilistic sieve for successful \(k\)

**Core mechanism.** Regard the conditions
\[
D_p(m,k)\ge0
\]
as local restrictions on \(k\), and estimate the number of \(k\le X\) satisfying all of them.

**Key lemma needed.** For every fixed \(m\), a lower bound such as
\[
\#\{k\le X:R_m(k)\in\mathbb Z\}>0
\]
for some sufficiently large \(X\), or preferably an asymptotic lower bound tending to infinity.

**Why it might work.** For fixed \(m\), the most obvious large-prime obstruction comes from a fixed-length interval near \(k\), and fixed-length intervals become increasingly likely to contain no primes as \(k\to\infty\). This suggests that large primes alone may not force perpetual failure.

**Likely failure point.** The local conditions are highly correlated across primes and prime powers. Treating them as independent random events is unjustified, and the product of local success probabilities may decay too quickly.

**Quick test.** For fixed \(m\), count successful \(k\le X\) and near-successful \(k\) with exactly one negative valuation. Compare frequencies with a naïve independent-local model. If observed frequencies collapse much faster than the model predicts, this route is likely blocked.

---

### Route 5: Induction or lifting in \(m\)

**Core mechanism.** Relate neighboring parameters using
\[
R_{m+1}(k)
=
R_m(k)\,
\frac{(m+1)(m+2k+1)}{(m+k+1)^2}.
\]
Try to transform a solution for \(m\) into a possibly different solution for \(m+1\).

**Key lemma needed.** A lifting theorem of the form:
if \(R_m(k)\) is integral, then some explicitly controlled \(k'=F(m,k,t)\) makes \(R_{m+1}(k')\) integral; or, more plausibly, if \(m\) has infinitely many solutions then \(m+1\) has at least one.

**Why it might work.** The problem has only one fixed parameter \(m\), and the cases begin with the completely integral family \(m=0\). A lifting mechanism would turn this into an induction from the central binomial coefficients.

**Likely failure point.** The factor
\[
\frac{(m+1)(m+2k+1)}{(m+k+1)^2}
\]
introduces a square denominator and does not preserve integrality at the same \(k\). There may be no monotonic relationship between solution sets for consecutive \(m\).

**Quick test.** Use the known data for \(m\le17\) to search for algebraic relations between successful \(k\)-values for \(m\) and \(m+1\), including linear, multiplicative, and congruence-based transformations. Also test whether each small \(m\) appears to have infinitely many solutions.

---

### Route 6: Disproof by a universal obstructing prime or prime power

**Core mechanism.** Search for an \(m_0\) such that every \(k\) has a prime \(p\) with
\[
D_p(m_0,k)<0.
\]

Potential obstructions include:

- a prime in
  \[
  \left(k+\frac{m_0}{2},k+m_0\right];
  \]
- a prime \(p>\!m_0\) with \(p^2>m_0+2k\) and
  \[
  2((m_0+k)\bmod p)<m_0;
  \]
- a systematic small-prime carry deficit;
- a finite covering of residue classes of \(k\) by different prime-power obstructions.

**Key lemma needed.** For one explicit \(m_0\), prove that the union of these obstruction mechanisms covers every positive integer \(k\).

**Why it might work.** Integrality requires simultaneous nonnegativity for all primes, so only one bad prime is needed for each \(k\). Different ranges of \(k\) can be obstructed by different primes, making a covering argument conceivable.

**Likely failure point.** Long composite or smooth stretches may evade all simple large-prime obstructions, while small-prime deficits can be canceled at higher powers. A finite modular covering may fail because valuations involve arbitrarily high powers and nonperiodic size cutoffs.

**Quick test.** Search beyond \(n=18\) for an \(m\) with an exceptionally long initial run of failures. For every failed \(k\), record a minimal obstruction prime and attempt to infer a residue-class covering. Then deliberately search for \(k\) avoiding all inferred classes. This is useful for falsifying proposed universal obstruction patterns before attempting a proof.

---

## 8. Verdict on difficulty

This is a genuine open problem with an elementary statement but a difficult quantifier structure:
\[
\forall m\ \exists k\ \forall p.
\]
The witness \(k\) is unbounded and may have complicated arithmetic structure. An affirmative proof must coordinate infinitely many potential prime obstructions, while a disproof must control every \(k\) for one fixed \(m\).

No equivalence to a famous named conjecture is presently indicated by the supplied record, and one should not claim that it is equivalent to the Riemann hypothesis, a standard prime-gap conjecture, or any other major conjecture. Nevertheless, several natural approaches run directly into hard questions about simultaneous \(p\)-adic behavior, primes in short intervals, and factorial-ratio integrality.

The zero-dollar prize is not evidence of low difficulty. The existing computation through \(n=18\) supplies useful data but leaves the universal problem essentially untouched. The most promising initial research program is:

1. reproduce and extend the exact valuation search;
2. determine whether known solutions satisfy the stronger Gaussian-binomial criterion;
3. classify all obstruction primes for failed \(k\);
4. test structured CRT and carry constructions;
5. separately search for candidate counterexamples exhibiting stable, provable obstruction patterns.