# Problem Brief: Erdős Problem #930

## 1. Precise statement

### Standard intended formulation

For every positive integer \(r\), does there exist a positive integer \(K=K(r)\) such that the following holds?

Let
\[
I_i=\{a_i,a_i+1,\dots,b_i\}\subset \mathbb Z_{>0}
\qquad (1\le i\le r)
\]
be pairwise disjoint intervals of positive consecutive integers, where \(1\le a_i\le b_i\), and let
\[
|I_i|=b_i-a_i+1\ge K
\]
for every \(i\). Define
\[
P(I_1,\dots,I_r)
   =\prod_{i=1}^{r}\prod_{m=a_i}^{b_i}m.
\]
The question is whether one can choose \(K(r)\) so that \(P(I_1,\dots,I_r)\) is never a perfect power.

Here a positive integer \(P>1\) is a **perfect power** if there exist integers \(y\ge 2\) and \(e\ge 2\) such that
\[
P=y^e.
\]

Equivalently, writing \(v_p(P)\) for the exponent of the prime \(p\) in \(P\), \(P\) is a perfect power exactly when
\[
\gcd_{p\mid P}v_p(P)\ge 2.
\]
It is enough to exclude \(q\)-th powers for prime exponents \(q\): if \(P=y^e\) and \(q\mid e\) is prime, then \(P=(y^{e/q})^q\).

The intervals are disjoint as sets. They are allowed to be adjacent; for example, \([1,5]\) and \([6,10]\) are disjoint.

### Necessary convention about “integers”

The intended domain must be the positive integers. If intervals in all of \(\mathbb Z\) were allowed, an interval containing \(0\) would make the product \(0=0^2\), immediately falsifying the statement for arbitrarily long intervals. Negative integers also introduce irrelevant conventions about odd powers. The Erdős–Selfridge context confirms that positive integers are intended.

### Quantifier form

The assertion is
\[
\forall r\in\mathbb Z_{\ge1}\ \exists K\in\mathbb Z_{\ge1}\
\forall I_1,\dots,I_r:
\left[
\begin{array}{l}
I_i\subset\mathbb Z_{>0}\text{ are pairwise disjoint integer intervals},\\
|I_i|\ge K\text{ for every }i
\end{array}
\right]
\Longrightarrow
P(I_1,\dots,I_r)\text{ is not a perfect power}.
\]

If it exists, denote the least possible threshold by \(K_r\).

---

## 2. What counts as a solution

### Complete proof

A complete affirmative solution must prove, unconditionally, that for every fixed positive integer \(r\), some finite \(K(r)\) works simultaneously for:

- all choices of pairwise disjoint positive-integer intervals;
- all starting points and gaps, with no upper bound on their size;
- all interval lengths at least \(K(r)\), not merely exactly \(K(r)\);
- all perfect-power exponents \(e\ge2\).

The bound \(K(r)\) need not be explicit unless the proof requires effectivity, but its existence must be established. It is enough to prove that
\[
\gcd_{p\mid P} v_p(P)=1
\]
for every admissible configuration.

A proof only for a particular value of \(r\) settles that case, not the full problem. The case \(r=1\) is already known.

### Complete disproof

The logical negation is
\[
\exists r_0\ge1\ \forall K\ge1\ \exists I_1,\dots,I_{r_0}
\]
such that:

1. the \(I_i\) are pairwise disjoint intervals in \(\mathbb Z_{>0}\);
2. \(|I_i|\ge K\) for every \(i\);
3. their product is a perfect power:
   \[
   \prod_{i=1}^{r_0}\prod_{m\in I_i}m=y^e
   \]
   for some \(y\ge2\), \(e\ge2\).

Equivalently, a disproof may give a sequence of configurations for one fixed \(r_0\) such that
\[
\min_i |I_i|\longrightarrow\infty
\]
and every corresponding product is a perfect power. The exponent may vary with the configuration.

An explicit counterexample family must include:

- formulas or an algorithm for all endpoints;
- a proof of pairwise disjointness;
- a proof that the minimum interval length is unbounded;
- an exact identity proving that the product is a perfect power.

A single finite example, however large, only gives a lower bound on \(K_{r_0}\); it does not disprove the problem.

---

## 3. What does not count

The following would not resolve the problem:

1. **Only the square case.**  
   Proving that the product is never a square does not rule out cubes or other odd prime powers. It is nevertheless a major subproblem.

2. **Only one fixed exponent \(q\).**  
   An affirmative proof must handle every prime exponent \(q\). By contrast, an infinite square family would be a complete disproof.

3. **Fixed interval lengths.**  
   Showing that for each fixed length tuple \((\ell_1,\dots,\ell_r)\) only finitely many endpoint tuples work does not provide a threshold uniform over arbitrarily large lengths.

4. **Intervals of exactly length \(K(r)\).**  
   The statement concerns every length at least \(K(r)\).

5. **Bounded endpoints or bounded gaps.**  
   A result valid only when all intervals lie in \([1,N]\), or when their gaps satisfy a prescribed bound, is insufficient.

6. **Density-zero or “almost all” results.**  
   Counterexamples could be extremely sparse. Showing that almost all configurations are nonpowers does not prove there are no exceptional configurations.

7. **Conditional arguments.**  
   Results assuming \(abc\), GRH, Vojta-type conjectures, or unproved prime-gap hypotheses do not constitute an unconditional solution.

8. **Showing each block product is individually a nonpower.**  
   Products of nonpowers can be perfect powers because their prime-valuation vectors can cancel modulo an exponent.

9. **A finite computational search.**  
   Search can find counterexamples to proposed thresholds or lemmas, but cannot establish a global threshold without a rigorous reduction to a finite range.

10. **A family with bounded minimum length.**  
    Infinitely many examples with, say, two intervals of length \(2\) do not disprove the existence of a larger threshold.

---

## 4. Known results and context

### 4.1 The case \(r=1\)

Erdős and Selfridge proved in [ErSe75] that the product of two or more consecutive positive integers is never a perfect power. Thus
\[
K_1=2.
\]

The value \(K_1=1\) is impossible because a singleton interval such as \(\{4\}\) has square product.

The Erdős–Selfridge theorem also settles every configuration whose intervals, after ordering, are all adjacent and therefore have a single contiguous union.

### 4.2 The lower-length condition is genuinely necessary

Even for \(r=2\), products of two short blocks can be squares. Two concrete examples are
\[
(1\cdot2)(8\cdot9)=144=12^2
\]
and
\[
(1\cdot2\cdot3)(48\cdot49\cdot50)=705600=840^2.
\]
Thus, if \(K_2\) exists, then
\[
K_2\ge4.
\]

The first type occurs infinitely often with both intervals of length \(2\). Indeed,
\[
\binom n2=y^2
\]
is the Pell equation
\[
(2n-1)^2-8y^2=1,
\]
which has infinitely many solutions. Each such solution gives
\[
(1\cdot2)((n-1)n)=(2!)^2\binom n2,
\]
a square.

This does not disprove the problem because the interval lengths remain \(2\).

### 4.3 The square-binomial-coefficient obstruction

A central special family is obtained from
\[
I_1=[1,\ell],\qquad I_2=[n-\ell+1,n],
\]
where \(n\ge2\ell\), so the intervals are disjoint. Then
\[
\prod_{m\in I_1}m\prod_{m\in I_2}m
  =\ell!\,\frac{n!}{(n-\ell)!}
  =(\ell!)^2\binom n\ell.
\]
Therefore this product is a square exactly when
\[
\binom n\ell
\]
is a square.

For example,
\[
\binom92=36,\qquad \binom{50}{3}=19600=140^2,
\]
which yield the two examples above.

Consequently:

> If there are square binomial coefficients \(\binom{n_j}{\ell_j}\) with
> \[
> n_j\ge2\ell_j,\qquad \ell_j\to\infty,
> \]
> then Erdős Problem #930 is false already for \(r=2\).

Conversely, an affirmative solution for \(r=2\) would prove that the lower index of every square binomial coefficient in the lower half of Pascal’s triangle is bounded:
\[
\exists K\quad
\ell\ge K,\ n\ge2\ell
\Longrightarrow
\binom n\ell\text{ is not a square}.
\]

This is the important link to Problem #363 indicated in the database commentary. The exact constructions and claims in #363 should be consulted before relying on anything stronger than this identity.

### 4.4 Fixed-index Diophantine results do not give uniformity

For fixed \(\ell\), the equation
\[
\binom n\ell=y^2
\]
defines a hyperelliptic curve. After clearing denominators, its smooth projective model has genus
\[
\left\lfloor\frac{\ell-1}{2}\right\rfloor.
\]
For fixed \(\ell\ge5\), Faltings’ theorem therefore implies only finitely many rational, hence integer, solutions \(n\). This does not provide any bound uniform in \(\ell\), and it does not show that there are no solutions.

Low fixed indices can behave differently: \(\ell=2\) gives a Pell equation and infinitely many solutions.

### 4.5 Relevant valuation formulas

For an interval \(I=[a,b]\),
\[
v_p\left(\prod_{m=a}^{b}m\right)
 =\sum_{j\ge1}
 \left(
 \left\lfloor\frac b{p^j}\right\rfloor
 -
 \left\lfloor\frac{a-1}{p^j}\right\rfloor
 \right).
\]
Hence for the full product,
\[
v_p(P)
 =\sum_{i=1}^r\sum_{j\ge1}
 \left(
 \left\lfloor\frac {b_i}{p^j}\right\rfloor
 -
 \left\lfloor\frac{a_i-1}{p^j}\right\rfloor
 \right).
\]

Writing \(\ell_i=b_i-a_i+1\),
\[
\prod_{m=a_i}^{b_i}m
  =\ell_i!\binom{b_i}{\ell_i}.
\]
Thus
\[
P=\prod_{i=1}^r
\ell_i!\binom{b_i}{\ell_i}.
\]
Legendre’s formula and Kummer’s carry theorem can therefore be applied to its valuations.

### 4.6 Large-prime theorems

Classical Sylvester-type theorems guarantee large prime divisors in sufficiently long products of consecutive integers under suitable hypotheses. Such results are relevant to the Erdős–Selfridge argument, but they do not directly solve the present problem: a large prime may divide selected integers in several separate intervals, and the total valuation may become divisible by the target exponent.

### 4.7 Status

The supplied commentary settles only \(r=1\). No case \(r\ge2\) should be treated as settled on the basis of the database entry. The square-binomial special family shows that even \(r=2\) contains a substantial unresolved uniform Diophantine problem.

---

## 5. Traps and edge cases

### 5.1 Zero and negative integers

Allowing \(0\) trivializes the problem. Every formal argument must explicitly work in \(\mathbb Z_{>0}\).

### 5.2 Length convention

The interval
\[
[a,b]=\{a,a+1,\dots,b\}
\]
has length \(b-a+1\), not \(b-a\).

In the binomial construction,
\[
[n-\ell+1,n]
\]
has exactly \(\ell\) elements.

### 5.3 Disjoint versus separated

Adjacent intervals are disjoint. If every gap is zero, the union is one interval and Erdős–Selfridge applies. Any genuine counterexample must therefore contain at least one omitted integer between consecutive blocks after sorting.

### 5.4 A prime dividing one selected integer need not have valuation one

If \(p\) divides exactly one selected integer \(m\), it can still contribute
\[
v_p(P)=v_p(m)>1.
\]
To rule out a \(q\)-th power, one needs \(v_p(P)\not\equiv0\pmod q\), not merely uniqueness of the divisible term.

### 5.5 A prime larger than every interval length can occur in several blocks

If \(p>|I_i|\), then at most one integer in each individual interval is divisible by \(p\), but up to \(r\) selected integers can still be divisible by \(p\). Their valuations may sum to a multiple of \(q\).

### 5.6 Individual nonpower blocks may cancel

For a square, each block has a squarefree kernel. The total product is square precisely when the product of these kernels is trivial in
\[
\mathbb Q^\times/(\mathbb Q^\times)^2.
\]
The examples above exhibit exact cancellation. Applying Erdős–Selfridge separately to each block is therefore insufficient.

### 5.7 Ruling out squares is not enough

Every even perfect power is a square, but cubes, fifth powers, and other odd prime powers remain. A proof must handle all prime exponents.

### 5.8 Factorial-ratio cancellation

The representation
\[
\prod_{m=a}^{b}m=\frac{b!}{(a-1)!}
\]
contains a denominator only formally; its prime valuations are nonnegative after cancellation. Arguments that assign independent prime factors to numerator and denominator without tracking cancellation are invalid.

### 5.9 Fixed finite sets of primes can often be engineered

Congruence conditions on endpoints can be arranged by the Chinese remainder theorem for any fixed finite collection of primes. Thus a proposed argument that inspects only finitely many small primes, independently of the endpoints, is especially vulnerable.

### 5.10 Off-by-one in the binomial construction

For
\[
I_1=[1,\ell],\qquad I_2=[n-\ell+1,n],
\]
disjointness is
\[
\ell<n-\ell+1,
\]
equivalently \(n\ge2\ell\). At \(n=2\ell\), the intervals are adjacent, but still disjoint.

### 5.11 Search ranges do not match the quantifiers

A proposed \(K(r)\) must work at arbitrarily large starting points. There is no reason the hardest examples should occur near the origin.

---

## 6. Verification hooks

### 6.1 Exact perfect-power test by valuations

For a finite candidate configuration:

1. Factor each selected integer, preferably using a smallest-prime-factor table if all endpoints are bounded.
2. Sum the exponent vectors to obtain \(v_p(P)\).
3. Compute
   \[
   d=\gcd_{p\mid P}v_p(P).
   \]
4. The product is a perfect power iff \(d\ge2\).

This avoids constructing the potentially enormous integer \(P\).

For a proof certificate, record the prime factorization and verify each prime with deterministic primality certificates if necessary.

### 6.2 Valuation computation from endpoints

For large intervals, use
\[
v_p(P)=
\sum_{i=1}^r\sum_{j\ge1}
\left(
\left\lfloor\frac{b_i}{p^j}\right\rfloor
-
\left\lfloor\frac{a_i-1}{p^j}\right\rfloor
\right).
\]
This is useful for testing proposed \(p\)-adic lemmas without multiplying or factoring every term.

### 6.3 Square-binomial search

Search over
\[
2\le \ell\le L,\qquad 2\ell\le n\le N
\]
and test whether \(\binom n\ell\) is a square.

Implementation:

- update \(\binom n\ell\) by exact recurrence;
- use modular quadratic-residue filters for several small primes;
- perform an exact integer-square-root test on survivors.

Any square found gives two disjoint equal-length intervals through
\[
[1,\ell],\quad[n-\ell+1,n].
\]

The known checks should reproduce
\[
\binom92=36,\qquad \binom{50}{3}=19600.
\]

### 6.4 Squarefree-kernel collision search

For a fixed length \(\ell\), compute
\[
S(a,\ell)=\operatorname{sf}\left(\prod_{j=0}^{\ell-1}(a+j)\right),
\]
where \(\operatorname{sf}\) is the squarefree kernel. Two disjoint intervals of length \(\ell\) have square product exactly when their squarefree kernels agree.

Store hashes of parity valuation vectors rather than multiplying kernels. Collisions should be checked exactly.

For \(r>2\), seek zero-sums among \(r\) such vectors over \(\mathbb F_2\), subject to disjointness.

### 6.5 Testing “valuation-one” lemmas

For all configurations in a bounded box, record:

- whether \(\gcd_p v_p(P)=1\);
- whether some prime has \(v_p(P)=1\);
- whether for each prime \(q\) there is a prime \(p\) with
  \[
  v_p(P)\not\equiv0\pmod q.
  \]

This distinguishes the actual nonpower criterion from stronger claims that may already be false.

### 6.6 Testing carry-based claims

Using
\[
P=\prod_i \ell_i!\binom{b_i}{\ell_i},
\]
compute \(v_p(\binom{b_i}{\ell_i})\) both by Legendre’s formula and by counting carries when adding \(\ell_i\) and \(b_i-\ell_i\) in base \(p\). Test any proposed “some base has an unmatched carry” lemma against the examples
\[
(\ell,n)=(2,9),\qquad (3,50).
\]

### 6.7 Counterexample-family certification

For a proposed symbolic family, a robust verification script should check for many parameter values:

- integer endpoints;
- positive endpoints;
- pairwise disjointness;
- interval lengths;
- exact power identity;
- growth of the minimum length.

Numerical checking is supporting evidence only; the final family requires a symbolic proof.

---

## 7. Attack routes

## Route 1: Extend the Erdős–Selfridge prime-allocation mechanism

### Core idea

Revisit the Erdős–Selfridge proof for one interval and identify which part uses connectedness rather than merely a bounded number of connected components. Attempt to replace it with a lemma for unions of at most \(r\) intervals.

### Key lemma needed

A suitable form would be:

> For every fixed \(r\), there exists \(K(r)\) such that for every union \(U\) of \(r\) disjoint intervals, each of length at least \(K(r)\), the valuation vector
> \[
> (v_p(\prod_{m\in U}m))_p
> \]
> has gcd \(1\).

A more exponent-specific version would show that for every prime \(q\) there is a prime \(p\) with
\[
v_p(P)\not\equiv0\pmod q.
\]

### Why it might work

The number of interval boundaries is only \(2r\). Many arguments for one interval ultimately compare prime-power divisibility patterns against the small number of “exceptional” boundary positions. A bounded number of components may permit a bounded loss depending only on \(r\).

### Likely failure point

Disconnected intervals allow the same prime-power contribution to appear in several blocks and cancel modulo \(q\). The original ordering and uniqueness arguments may rely critically on having no gaps. A lemma asserting the existence of a prime of valuation exactly \(1\) may be substantially stronger than the problem and could be false.

### Quick obstruction test

Enumerate two- and three-interval configurations and search for nonperfect products with:

- no prime of valuation \(1\);
- all large-prime valuations occurring in matched pairs;
- gcd of all valuations still equal to \(1\).

Such examples would refute overly strong versions of the proposed extension without refuting the main problem.

---

## Route 2: Large-prime and sieve analysis for boundedly many blocks

### Core idea

Use Sylvester-type large-prime divisors, smooth-number bounds, and sieving over primes or prime powers to force an unmatched valuation among the selected integers.

### Key lemma needed

One possible target is a bounded-component Sylvester principle:

> Given fixed \(r\) and a prime exponent \(q\), every sufficiently long union of \(r\) disjoint intervals contains a prime power \(p^a\) whose number or weighted multiplicity among the selected integers is not divisible by \(q\).

The bound must depend only on \(r\), not on the endpoints or \(q\), or \(q\) must first be bounded in terms of \(r\).

### Why it might work

Each prime \(p\) larger than all interval lengths occurs at most once per block. Thus its contribution is controlled by at most \(r\) selected multiples. Large prime powers may provide even sharper localization. Fixed \(r\) may make complete modular cancellation impossible once enough independent primes are present.

### Likely failure point

There is no prime guaranteed inside an arbitrary interval of fixed absolute length situated at an arbitrarily large endpoint. Also, a prime larger than every block length can divide one integer in each block, and those contributions can sum to \(0\bmod q\). CRT constructions can neutralize any argument based on a predetermined finite set of primes.

### Quick obstruction test

For proposed prime ranges, computationally choose endpoints that maximize cancellation of
\[
v_p(P)\pmod q
\]
for all primes in those ranges. Also test long runs beginning near factorial-based composite stretches, such as \(N!+2,\dots,N!+N\), to expose hidden assumptions about primes among the selected integers.

---

## Route 3: Factorial ratios, Kummer carries, and induction on components

### Core idea

Write
\[
P=\prod_{i=1}^r \ell_i!\binom{b_i}{\ell_i}
\]
and analyze valuations through Legendre’s digit-sum formula and Kummer’s theorem. Try to use the ordering and disjointness of the intervals to find a base \(p\) in which the carry patterns cannot all cancel modulo \(q\).

### Key lemma needed

For every fixed \(r\) and every prime \(q\), sufficiently large disjoint blocks should admit a prime \(p\) such that
\[
\sum_{i=1}^r
\left(
v_p(\ell_i!)+v_p\binom{b_i}{\ell_i}
\right)
\not\equiv0\pmod q.
\]

An inductive version could remove an extreme interval while controlling the finitely many primes whose valuations are altered modulo \(q\).

### Why it might work

Factorial valuations are rigid digit-sum functions:
\[
v_p(n!)=\frac{n-s_p(n)}{p-1}.
\]
Kummer’s theorem turns binomial valuations into carry counts. Disjointness imposes inequalities among the \(b_i\) and \(\ell_i\), potentially preventing all carry patterns from synchronizing over every prime base.

### Likely failure point

The square-binomial examples are exact carry cancellations, not accidental numerical coincidences. Carry patterns can be highly structured across many bases, and the factorial terms \(\ell_i!\) contribute additional cancellation. A statement uniform in arbitrary endpoints may be too strong.

### Quick obstruction test

Any proposed carry lemma must first survive
\[
\binom92=6^2,\qquad \binom{50}{3}=140^2.
\]
Search systematically for further square binomial coefficients and for arbitrary pairs of blocks with equal squarefree kernels. Record the base-\(p\) carry patterns of all examples to identify the precise failure mode.

---

## Route 4: Valuation-vector and zero-sum methods

### Core idea

For a prime \(q\), work in
\[
\mathbb Q^\times/(\mathbb Q^\times)^q
   \cong \bigoplus_p\mathbb F_q.
\]
Associate to an interval \(I\) its valuation vector
\[
V_q(I)=\bigl(v_p(\prod_{m\in I}m)\bmod q\bigr)_p.
\]
The full product is a \(q\)-th power exactly when
\[
V_q(I_1)+\cdots+V_q(I_r)=0.
\]

Seek a coding-theoretic or additive-combinatorial statement saying that long, pairwise disjoint intervals cannot form such a zero-sum of bounded size.

### Key lemma needed

> For every \(r\), there exists \(K(r)\) such that, for every prime \(q\), no \(r\) pairwise disjoint intervals of lengths at least \(K(r)\) have valuation vectors summing to zero in \(\bigoplus_p\mathbb F_q\).

For \(q=2\), this says that no bounded collection of sufficiently long disjoint blocks has squarefree kernels whose product is \(1\).

### Why it might work

The fixed number \(r\) is natural from a bounded zero-sum perspective. Large primes can act as sparse coordinates, and the incidence pattern “which interval contains a multiple of \(p\)” may yield a triangular or uniquely supported coordinate after suitable ordering.

### Likely failure point

The vectors are highly nonrandom and admit exact collisions:
\[
V_2([1,\ell])=V_2([n-\ell+1,n])
\]
whenever \(\binom n\ell\) is square. There may be structured zero-sums invisible to generic coding heuristics.

### Quick obstruction test

Hash squarefree-kernel vectors for all intervals in a bounded range, build a graph joining disjoint intervals with equal vectors, and search for:

- collisions for \(r=2\);
- zero-sum triples and higher tuples;
- recurring algebraic patterns in the endpoints.

For odd \(q\), perform the same search with exponent vectors modulo \(q\).

---

## Route 5: Uniform Diophantine geometry of factorial-ratio equations

### Core idea

Assume a counterexample
\[
y^q=\prod_{i=1}^r\frac{b_i!}{(a_i-1)!}
\]
and interpret it as an integral point on a superelliptic variety. Try to obtain a uniform theorem excluding integral points as all interval lengths grow.

### Key lemma needed

One would need something much stronger than fixed-curve finiteness, for example:

- a bound on the prime exponent \(q\) depending only on \(r\);
- a uniform bound on interval lengths for integral points on the resulting family;
- or a proof that all positive-dimensional exceptional subvarieties correspond to overlapping, adjacent, or bounded-length configurations.

### Why it might work

For fixed lengths and fixed \(q\), the equations often have high genus or high logarithmic general type. The large number of distinct linear factors should create many branch points, which is favorable for superelliptic finiteness arguments.

### Likely failure point

The lengths vary, so the curve or variety varies. For \(r\ge2\), several endpoints are free variables, producing higher-dimensional varieties that may contain rational or Pell-type subfamilies. Existing results such as Faltings’ theorem are not uniform enough. An \(abc\)- or Vojta-based argument would be conditional unless the required special case can be proved independently.

### Quick obstruction test

For fixed small length tuples, compute the genus or dimension of the resulting varieties and search for:

- Pell-type parametrizations;
- rational curves;
- elliptic curves of positive rank;
- identities coming from binomial coefficients.

If such exceptional families persist as the lengths grow, this route is likely blocked.

---

## Route 6: Disproof through unbounded square-binomial or related families

### Core idea

Seek square products for \(r=2\). The cleanest target is an unbounded family
\[
\binom{n_j}{\ell_j}=y_j^2,\qquad
n_j\ge2\ell_j,\qquad
\ell_j\to\infty.
\]
Then
\[
\left(\prod_{m=1}^{\ell_j}m\right)
\left(\prod_{m=n_j-\ell_j+1}^{n_j}m\right)
=(\ell_j!y_j)^2
\]
is a square product of two disjoint intervals whose lengths tend to infinity.

A broader target is
\[
\prod_{m=a_j}^{a_j+\ell_j-1}m
\prod_{m=b_j}^{b_j+\ell'_j-1}m
=y_j^2
\]
with both \(\ell_j,\ell'_j\to\infty\).

### Key lemma needed

Either:

- construct square binomial coefficients with unbounded lower index; or
- produce a different parametric mechanism pairing the squarefree kernels of two increasingly long blocks.

### Why it might work

There are genuine Pell and elliptic phenomena at small lengths, and the database explicitly points to constructions in Problem #363. A single unbounded square family would settle #930 negatively without addressing odd exponents.

### Likely failure point

Passing from infinitely many solutions at one fixed lower index to solutions with unbounded lower index is precisely the difficult uniform issue. Fixed-\(\ell\) Pell families do not help. For larger fixed \(\ell\), the relevant curves have increasing genus and generally do not admit obvious parametrizations.

### Quick obstruction test

Run a modularly sieved search for square \(\binom n\ell\) with \(\ell\) increasing. In parallel, search for equal squarefree kernels of arbitrary disjoint blocks rather than restricting one block to \([1,\ell]\). Any apparent pattern must be converted into an exact recurrence or algebraic identity before it has theoretical value.

---

## 8. Verdict on difficulty

This is a very difficult uniform problem. The case \(r=1\) is exactly the deep Erdős–Selfridge theorem, while the first unsettled case already allows cancellation between two independently positioned blocks.

Most importantly, the \(r=2\) case would imply a uniform boundedness theorem for square binomial coefficients:
\[
\binom n\ell\text{ square},\quad n\ge2\ell
\quad\Longrightarrow\quad
\ell<K_2.
\]
Conversely, square binomial coefficients with unbounded lower index would disprove the problem immediately. This connection should be treated as a major warning: the problem contains a long-standing and notoriously resistant perfect-power problem in Pascal’s triangle.

Fixed-length Diophantine finiteness, prime-divisor results for one block, and density heuristics all fall far short of the required endpoint- and length-uniform statement. A successful proof will probably require either:

- a genuinely new bounded-component extension of the Erdős–Selfridge mechanism;
- a uniform valuation theorem across arbitrary gaps;
- or unexpectedly strong uniform Diophantine input.

A disproof is also plausible in principle, especially through structured square families, but it would require an unbounded-length construction rather than the known Pell-type examples at fixed small lengths.