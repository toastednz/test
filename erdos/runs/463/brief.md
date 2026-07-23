# Problem Brief: Erdős Problem #463

## 1. PRECISE STATEMENT

Let \(\mathbb N=\{1,2,3,\dots\}\). For every integer \(m\ge 2\), let
\[
P^-(m)=\min\{p:\ p\text{ is prime and }p\mid m\}
\]
denote the least prime factor of \(m\).

The standard interpretation of the problem is:

> Does there exist a function \(f:\mathbb N\to\mathbb R\) such that
> \[
> \lim_{n\to\infty}f(n)=+\infty
> \]
> and an integer \(N_0\) such that for every integer \(n\ge N_0\), there is a composite integer \(m\) satisfying
> \[
> n+f(n)<m<n+P^-(m)?
> \]

There is no stated monotonicity requirement on \(f\), and allowing \(f\) to be integer-valued instead of real-valued does not materially change the problem.

### Equivalent additive formulation

Write
\[
d=m-n.
\]
Then the two strict inequalities become
\[
d>f(n),\qquad d<P^-(n+d),
\]
and \(n+d\) must be composite. Thus the problem asks whether there is \(f(n)\to\infty\) such that, for every sufficiently large \(n\), one can find an integer \(d>f(n)\) for which
\[
n+d\text{ is composite}
\quad\text{and}\quad
P^-(n+d)>d.
\]

In words: every sufficiently large \(n\) should be followed, at a distance tending uniformly to infinity, by a composite number having no prime factor at most its distance from \(n\).

Define
\[
D(n)=
\max\Bigl(
\{d\in\mathbb N:\ n+d\text{ is composite and }P^-(n+d)>d\}
\cup\{0\}
\Bigr).
\]
Then the problem is exactly equivalent to
\[
\boxed{D(n)\longrightarrow\infty.}
\]

Indeed:

- If the original \(f\) exists, then \(D(n)>f(n)\) for all sufficiently large \(n\), so \(D(n)\to\infty\).
- Conversely, if \(D(n)\to\infty\), one may take, for example,
  \[
  f(n)=D(n)-1
  \]
  for all sufficiently large \(n\). A monotone witness can also be obtained from tail minima of \(D\).

Equivalently, the desired assertion is the following fully quantified statement:
\[
\forall B\in\mathbb N\ \exists N_B\ \forall n\ge N_B\ \exists d\in\mathbb N
\]
such that
\[
d>B,\qquad n+d\text{ is composite},\qquad P^-(n+d)>d.
\]

### Multiplicative formulation

Suppose \(m=n+d\) is a valid witness and put \(p=P^-(m)\). Write
\[
m=pb.
\]
Since \(p\) is the least prime factor of \(m\), every prime factor of \(b\) is at least \(p\), and \(b\ge p\). The inequalities are
\[
p(b-1)<n<pb.
\]

Conversely, a prime \(p\) and integer \(b\ge p\) give a witness precisely when

- every prime factor of \(b\) is at least \(p\);
- \(p(b-1)<n<pb\).

If \(p\nmid n\), this forces
\[
b=\left\lceil\frac np\right\rceil,\qquad
d=pb-n=p-(n\bmod p).
\]
Thus one may search over primes \(p\) for which
\[
P^-\!\left(\left\lceil\frac np\right\rceil\right)\ge p
\]
and the complementary residue \(p-(n\bmod p)\) is large.

A particularly useful sufficient special case is
\[
m=pq
\]
with primes \(p\le q\), where
\[
n<pq<n+p.
\]

### Necessary size bound

For a composite \(m=n+d\),
\[
P^-(m)\le \sqrt m.
\]
Therefore every valid \(d\) satisfies
\[
d<P^-(n+d)\le \sqrt{n+d},
\]
hence
\[
d^2<n+d
\]
and so
\[
d<\frac{1+\sqrt{1+4n}}2=\sqrt n+O(1).
\]
Thus \(D(n)=O(\sqrt n)\). Any successful \(f\) must necessarily grow more slowly than this pointwise upper scale.

### Ambiguity in the commentary’s \(F(n)\)

The database commentary writes
\[
F(n)=\min_{m>n}(m-p(m)).
\]
For this to be nontrivial, the minimum must be over **composite** \(m\). If primes were admitted and \(p(m)=m\) for prime \(m\), then every prime \(m>n\) would contribute \(m-p(m)=0\), making \(F(n)=0\).

Accordingly, the standard reading is
\[
F_C(n)=\min_{\substack{m>n\\m\ \mathrm{composite}}}
\bigl(m-P^-(m)\bigr).
\]

---

## 2. WHAT COUNTS AS A SOLUTION

### Complete proof

A complete affirmative solution must prove the uniform statement
\[
D(n)\to\infty.
\]
Equivalently, it must prove that for every fixed \(B\), all sufficiently large \(n\) admit a distance \(d>B\) such that

1. \(n+d\) is composite;
2. no prime \(q\le d\) divides \(n+d\).

The threshold \(N_B\) may depend on \(B\), but the conclusion must hold for **every** \(n\ge N_B\), not merely almost all \(n\).

A proof may instead construct an explicit \(f\), but it must establish both:

- \(f(n)\to\infty\) in the usual uniform tail sense;
- for every sufficiently large \(n\), an appropriate composite \(m\) exists.

No effective formula for \(f\) is required if existence is proved rigorously.

### Complete disproof

The negation is
\[
D(n)\not\to\infty.
\]
Since \(D(n)\) is nonnegative and integer-valued, this is equivalent to:

> There exists a fixed integer \(B\ge0\) and infinitely many integers \(n\) such that \(D(n)\le B\).

Thus a complete disproof must produce or prove the existence of a fixed \(B\) and an unbounded sequence \(n_j\) such that, for every \(j\) and every integer \(d>B\),

- either \(n_j+d\) is prime, or
- \(n_j+d\) has a prime factor \(q\le d\).

It is enough to check \(d\) only up to the largest integer satisfying
\[
d^2<n_j+d,
\]
because larger \(d\) cannot be valid even in principle.

A stronger disproof would exhibit infinitely many \(n\) with \(D(n)=0\), meaning that no admissible composite \(m\) exists at all.

### Verification of an explicit counterexample

For a particular \(n\), a certificate that \(D(n)\le B\) consists of, for every integer
\[
B<d<\frac{1+\sqrt{1+4n}}2,
\]
one of:

- a primality certificate for \(n+d\); or
- an explicit divisor \(q\mid n+d\) with \(2\le q\le d\).

The divisor \(q\) need not itself be proved to be the least prime factor: any divisor \(q\le d\) implies that some prime factor is at most \(q\le d\).

A finite list of such \(n\) is not a disproof. One needs an infinite family or a theorem producing arbitrarily large certified examples with a single fixed bound \(B\).

---

## 3. WHAT DOES NOT COUNT

None of the following resolves the problem:

1. **Infinitely many successful \(n\).**  
   The assertion is required for every sufficiently large \(n\).

2. **A density-one or “almost all \(n\)” result.**  
   An infinite sparse exceptional set would still defeat the conjecture.

3. **Showing only that \(\sup_n D(n)=\infty\).**  
   The required conclusion is \(D(n)\to\infty\), not merely that \(D(n)\) is unbounded.

4. **A bounded-distance result.**  
   Proving that every sufficiently large \(n\) has some admissible \(d\le C\) establishes only eventual coverage, not a witness distance tending to infinity.

5. **Allowing \(m\) to be prime.**  
   Prime values \(m=n+d\) are explicitly excluded, even though they automatically have no small prime factors.

6. **Replacing a strict inequality by a weak one.**  
   The condition is \(d<P^-(n+d)\), not \(d\le P^-(n+d)\). The boundary case \(d=P^-(n+d)\) is invalid.

7. **A subsequentially divergent function.**  
   It is not enough that \(f(n)\) be unbounded or tend to infinity along some subsequence.

8. **Conditional results.**  
   A proof under Hardy–Littlewood, Elliott–Halberstam, a random model, or another unproved hypothesis is informative but does not solve the open problem.

9. **Prime-gap results alone.**  
   Locating primes close to \(n\) does not help directly because the required \(m\) is composite.

10. **An asymptotic estimate for the commentary’s \(F_C(n)\) without control of the other endpoint.**  
    This is related but not automatically sufficient, as explained below.

---

## 4. KNOWN RESULTS AND CONTEXT

### The interval interpretation

Each composite \(m\) defines the open interval
\[
I_m=(m-P^-(m),m).
\]
An integer \(n\) has \(m\) as a witness exactly when
\[
n\in I_m.
\]

For such an interval, define

- right depth:
  \[
  d=m-n;
  \]
- left depth:
  \[
  \ell=n-(m-P^-(m)).
  \]

Then
\[
d+\ell=P^-(m).
\]
The problem asks whether every sufficiently large integer lies in one of these intervals at right depth tending to infinity.

### Relation with the commentary’s \(F_C(n)\)

Define
\[
F_C(n)=
\min_{\substack{m>n\\m\ \mathrm{composite}}}
\bigl(m-P^-(m)\bigr).
\]
Then
\[
F_C(n)<n
\]
if and only if at least one witness exists, equivalently \(D(n)\ge1\).

Also,
\[
n-F_C(n)
=
\max_{\substack{m>n\\m\ \mathrm{composite}}}
\left(P^-(m)-(m-n)\right).
\]
Thus \(n-F_C(n)\) is the maximum **left depth** \(\ell\), whereas \(D(n)\) is the maximum **right depth** \(d\).

Erdős asked whether
\[
n-F_C(n)\sim c\sqrt n
\]
for some constant \(c>0\). This concerns the left-hand margin of the covering intervals. Problem #463 concerns the right-hand margin. Even an asymptotic of the displayed form does not by itself prove that the corresponding right depth tends to infinity: it is logically possible that intervals achieving the best left depth end only \(O(1)\) to the right of \(n\).

The database also refers to Problem #385, but the supplied commentary gives no further usable statement from that entry.

### Rough numbers and sieve theory

The condition
\[
P^-(n+d)>d
\]
says that \(n+d\) is \(d\)-rough. Standard tools relevant to rough numbers include:

- Buchstab’s identity;
- the fundamental lemma of sieve theory;
- Selberg and combinatorial sieves;
- Jacobsthal-type questions about gaps between integers avoiding prescribed small prime divisors.

However, there are two extra difficulties here:

1. the roughness threshold varies with the offset \(d\);
2. rough values that happen to be prime do not count.

The second issue is closely related to the sieve parity problem: lower-bound sieves have difficulty separating primes from integers with an even number of large prime factors, particularly in very short intervals.

### Semiprime subproblem

Restricting to \(m=pq\) with primes \(p\le q\) yields the sufficient condition
\[
n<pq<n+p.
\]
Equivalently,
\[
q=\left\lceil\frac np\right\rceil
\]
must be prime, and the residue gap
\[
pq-n=p-(n\bmod p)
\]
must be both positive and large.

Heuristically there are many primes \(p\) up to \(\sqrt n\), and one expects some of the corresponding ceilings \(\lceil n/p\rceil\) to be prime. Proving this for every individual \(n\), in a strip of multiplicative width only \(p\), is much stronger than ordinary prime-distribution estimates.

### Elementary observations

- If \(n\ge3\) is odd, then \(m=n+1\) is even composite and
  \[
  P^-(m)=2>1,
  \]
  so \(d=1\) is admissible. This gives only bounded depth and therefore does not approach the full problem.

- More generally, whenever \(n+1\) is composite, \(d=1\) works.

- For every valid \(d\ge2\), \(n+d\) must be odd, because its least prime factor exceeds \(d\ge2\). Hence \(d\) has parity opposite to \(n\).

- The elementary upper bound \(d=O(\sqrt n)\) shows that the natural scale is at most square-root size, consistent with the commentary’s appearance of \(\sqrt n\).

No part of the full uniform divergence assertion is stated as settled in the supplied database commentary.

---

## 5. TRAPS AND EDGE CASES

### 5.1 Primes do not count

If \(n+d\) is prime, then it is not a valid witness, regardless of the convention \(P^-(p)=p\). This is a major source of false arguments: a sieve may prove the existence of an integer with no small prime factor but fail to show it is composite.

### 5.2 Strict boundary

One needs
\[
P^-(n+d)>d.
\]
If \(P^-(n+d)=d\), then
\[
m=n+P^-(m),
\]
which violates the strict upper inequality.

In the multiplicative form, if \(p\mid n\), the next multiple of \(p\) is \(n+p\), again giving the forbidden equality \(d=p\).

### 5.3 The least factor condition cannot be replaced by divisibility

Finding a large prime \(p>d\) dividing \(n+d\) is insufficient. One must also rule out every smaller prime factor. For example,
\[
105=3\cdot5\cdot7
\]
has a factor \(7>d\) for some small \(d\), but its least prime factor remains \(3\).

### 5.4 The cofactor must be \(p\)-rough

Writing \(m=pb\) with \(p\) prime does not ensure \(P^-(m)=p\). One must verify
\[
P^-(b)\ge p.
\]

### 5.5 Small cases can have no witness

For example, \(n=10\) has no admissible \(d\). The necessary bound gives \(d\le3\), and
\[
11\text{ is prime},\qquad
12\text{ has }P^-(12)=2\not>2,\qquad
13\text{ is prime}.
\]

Likewise \(n=100\) has no witness. The only possible distances are \(1\le d\le10\), and
\[
101,103,107,109
\]
are prime, while each of
\[
102,104,105,106,108,110
\]
has a prime divisor at most its corresponding offset.

Therefore any proof must genuinely use the phrase “for all sufficiently large \(n\).”

### 5.6 Pointwise divergence versus average growth

Large average values of \(D(n)\), positive density of successful large distances, or even very rare enormous values of \(D(n)\) do not imply \(D(n)\to\infty\).

### 5.7 Confusing the two margins of \(I_m\)

The commentary’s \(n-F_C(n)\) measures distance from the left endpoint \(m-P^-(m)\), while the problem requires distance from the right endpoint \(m\). Since the two depths sum to \(P^-(m)\), they are related but not interchangeable.

### 5.8 Misusing prime-gap theorems

A theorem placing a prime in \((n,n+y)\) can actually produce an excluded value rather than a witness. A valid argument must produce a composite rough number.

### 5.9 Assuming independence of the ceilings

For primes \(p\), the values
\[
\left\lceil\frac np\right\rceil
\]
are highly correlated and repeat over ranges of \(p\). Treating their primality or roughness as independent random events is only heuristic.

---

## 6. VERIFICATION HOOKS

### 6.1 Direct computation of \(D(n)\)

For \(n\le N\), precompute smallest prime factors up to
\[
N+\lceil\sqrt N\rceil+2.
\]
For each \(n\), enumerate integers \(d\ge1\) satisfying
\[
d^2<n+d.
\]
Set \(m=n+d\). Then \(d\) is admissible exactly when

- \(\operatorname{spf}(m)<m\), so \(m\) is composite;
- \(\operatorname{spf}(m)>d\).

Record the largest such \(d\), or \(0\) if none exists.

Pseudocode:

```text
for n = 1..N:
    D[n] = 0
    for d = 1 while d*d < n+d:
        m = n+d
        if spf[m] < m and spf[m] > d:
            D[n] = d
```

Useful outputs include:

- record-low values of \(D(n)\);
- the minimum of \(D(n)\) on dyadic blocks \([X,2X]\);
- counts of \(n\) with \(D(n)\le B\);
- parity and residue patterns among low-\(D(n)\) values.

The decisive empirical statistic is not the maximum or average of \(D(n)\), but block minima or the tail behavior of
\[
\min_{X\le n\le 2X}D(n).
\]

### 6.2 Prime-parameter enumeration

For each prime \(p\), set
\[
r=n\bmod p.
\]
If \(r=0\), the resulting next multiple is at distance \(p\), which is invalid. If \(r\ne0\), put
\[
d=p-r,\qquad b=\left\lceil\frac np\right\rceil.
\]
Then \(d\) is admissible exactly when

- \(b\ge p\);
- \(P^-(b)\ge p\).

This parameterization is useful for studying how many prime choices \(p\) work for each \(n\), and whether the successful values of \(d\) resemble a uniform residue distribution.

### 6.3 Semiprime-only data

Restrict the previous search to cases where \(b\) is prime. Record
\[
D_2(n)=
\max\{pq-n:\ p,q\text{ prime},\ p\le q,\ n<pq<n+p\}.
\]
Comparing \(D_2(n)\) and \(D(n)\) tests whether composites with more than two prime factors are essential.

### 6.4 Exact certificates for small \(D(n)\)

To certify \(D(n)\le B\), enumerate
\[
B<d<\frac{1+\sqrt{1+4n}}2.
\]
For each \(d\), store either:

- a primality certificate for \(n+d\); or
- a divisor \(q\le d\) of \(n+d\).

These certificates can be independently checked without trusting the factorization program.

### 6.5 Compute the commentary’s \(F_C(n)\)

For moderate ranges, compute
\[
A(n)=n-F_C(n)
\]
and record a minimizing composite \(m_F(n)\). For that minimizer calculate
\[
d_F(n)=m_F(n)-n,\qquad
\ell_F(n)=A(n),\qquad
P^-(m_F(n))=d_F(n)+\ell_F(n).
\]

Compare \(A(n)\), \(d_F(n)\), and \(D(n)\). This directly tests whether intervals optimizing the left margin tend to have useful right margin.

### 6.6 Dyadic rough-number counts

For selected \(n,y\), compute
\[
R(n,y)=
\#\{d\in[y,2y]:P^-(n+d)>2y\}.
\]
Separate this count into prime and composite values of \(n+d\). A composite counted by \(R(n,y)\) is automatically an admissible witness, since \(d\le2y<P^-(n+d)\).

This tests the most direct sieve route and quantifies how badly primes dominate the rough survivors.

---

## 7. ATTACK ROUTES

### Route 1: Uniform short-interval lower-bound sieve

**Core mechanism.**  
Find a dyadic range of offsets in which there are more rough integers than primes.

A sufficient lemma would be:

> There exists \(y=y(n)\to\infty\), with \(y=o(\sqrt n)\), such that for every sufficiently large \(n\),
> \[
> \#\{d\in[y,2y]:P^-(n+d)>2y\}
> >
> \#\{d\in[y,2y]:n+d\text{ is prime}\}.
> \]

The excess must contain a composite \(n+d\), and then
\[
P^-(n+d)>2y\ge d.
\]

**Why it might work.**  
Heuristically, a proportion about \(e^{-\gamma}/\log y\) of integers are \(2y\)-rough, while the prime density near \(n\) is about \(1/\log n\). If \(\log y=o(\log n)\), rough survivors should substantially outnumber primes.

**Likely failure point.**  
The interval length is only comparable to the sieve threshold. Standard lower-bound sieve estimates are weakest precisely in this regime, and the parity problem obstructs proving that a rough survivor is composite.

**Quick blockage test.**  
Compute \(R(n,y)\) and its prime/composite decomposition over large dyadic blocks. Determine whether worst-case \(n\) have no composite survivors even when the total rough count is near its heuristic size.

---

### Route 2: Prime lattice points near the hyperbola \(pq=n\)

**Core mechanism.**  
Restrict to balanced semiprimes \(m=pq\). Seek primes \(p\le q\) satisfying
\[
n<pq<n+p
\]
and
\[
pq-n\to\infty
\]
uniformly in \(n\).

Equivalently, find a prime \(p\) such that
\[
q=\left\lceil\frac np\right\rceil
\]
is prime and
\[
p-(n\bmod p)
\]
is large.

**Needed lemma.**  
For every fixed \(B\) and all sufficiently large \(n\), there is a prime \(p\) with
\[
p\le \left\lceil\frac np\right\rceil,
\qquad
\left\lceil\frac np\right\rceil\text{ prime},
\qquad
B<p-(n\bmod p)<p.
\]

**Why it might work.**  
There are about \(\sqrt n/\log n\) possible prime \(p\) near the square-root scale. A naive independence model predicts roughly
\[
\frac{\sqrt n}{(\log n)^2}
\]
prime pairs \(\bigl(p,\lceil n/p\rceil\bigr)\), and most complementary residues should be much larger than any fixed \(B\).

**Likely failure point.**  
This demands prime information for a highly discontinuous reciprocal sequence at essentially unit resolution. Ordinary prime-gap results allow movement in \(q\), whereas here \(q\) is forced to be one exact integer.

**Quick blockage test.**  
For each \(n\) in large intervals, count prime \(p\) for which \(\lceil n/p\rceil\) is prime. Record whether the minimum count over a block tends upward, and whether low-count cases correlate with arithmetic structure of \(n\).

---

### Route 3: Bilinear rough cofactors, not necessarily prime

**Core mechanism.**  
Use
\[
m=p\,\left\lceil\frac np\right\rceil
\]
but require only that the cofactor be \(p\)-rough:
\[
P^-\!\left(\left\lceil\frac np\right\rceil\right)\ge p.
\]
This enlarges the semiprime route by permitting cofactors with two or more prime factors, all at least \(p\).

**Needed lemma.**  
For every \(B\) and all sufficiently large \(n\), some prime \(p\) satisfies
\[
n\bmod p\ne0,\qquad
p-(n\bmod p)>B,
\]
and
\[
P^-\!\left(\left\lceil\frac np\right\rceil\right)\ge p.
\]

A promising analytic form would be a uniform lower bound for
\[
\sum_{\substack{p\in\mathcal P\\p\le \sqrt n+O(1)}}
1_{\{P^-(\lceil n/p\rceil)\ge p\}}
1_{\{p-(n\bmod p)>B\}}.
\]

**Why it might work.**  
The condition is naturally bilinear: \(p\) is a prime variable and the cofactor is a reciprocal transform of \(p\). Dispersion methods, large-sieve inequalities, or Buchstab decompositions may exploit averaging over \(p\) while retaining a pointwise parameter \(n\).

**Likely failure point.**  
For \(p\) near \(\sqrt n\), a \(p\)-rough cofactor is usually forced to be prime, so the problem collapses back to Route 2. For smaller \(p\), more composite cofactors are possible, but the sieve depth becomes severe.

**Quick blockage test.**  
Compute, for each \(n\), successful \(p\) grouped by \(p\)-scale. Determine whether witnesses genuinely arise from \(p\ll\sqrt n\) with composite cofactors, or almost exclusively from prime cofactors near \(\sqrt n\).

---

### Route 4: Lower-envelope analysis via \(F_C(n)\)

**Core mechanism.**  
Study the family of intervals
\[
I_m=(m-P^-(m),m)
\]
through the lower envelope
\[
F_C(n)=\min_{m>n}(m-P^-(m)).
\]
For a minimizing \(m\), write
\[
n-F_C(n)=\ell,\qquad m-n=d,\qquad P^-(m)=\ell+d.
\]

**Needed lemma.**  
One needs a “non-hugging” or endpoint-separation theorem, for example:
\[
P^-(m_F(n))-\bigl(n-F_C(n)\bigr)\to\infty
\]
for some choice of minimizer \(m_F(n)\), or the same conclusion for a uniformly near-minimizing interval.

Combined with strong lower bounds on \(n-F_C(n)\), this would provide the required right depth.

**Why it might work.**  
Minimizers of \(m-P^-(m)\) may have rigid multiplicative structure, probably involving large least prime factors and relatively balanced factorizations. Abrupt changes of minimizer could force overlap between adjacent intervals, potentially preventing every optimal interval from ending only boundedly to the right of \(n\).

**Likely failure point.**  
Control of the left endpoint alone gives no formal control of the right endpoint. The minimizing interval may systematically “hug” \(n\) from the right, with large left depth but bounded \(d\).

**Quick blockage test.**  
Compute minimizing \(m_F(n)\), all near-minimizers, and their right depths. Check whether small \(d_F(n)\) persists when \(n-F_C(n)\) is large, and whether alternative near-minimizers provide larger right depth.

---

### Route 5: Diagonal Jacobsthal theory

**Core mechanism.**  
View each offset \(d\) as blocked if some prime \(q\le d\) divides \(n+d\). The desired witness is an unblocked offset whose value is composite.

This resembles Jacobsthal’s function, which studies gaps between integers coprime to a fixed product of primes, but here the set of forbidden primes grows with \(d\).

**Needed lemma.**  
A suitable “diagonal Jacobsthal” statement would assert that, for every fixed \(B\) and sufficiently large \(n\), some
\[
B<d<\sqrt n+O(1)
\]
satisfies
\[
\gcd\!\left(n+d,\prod_{q\le d}q\right)=1,
\]
and that at least one such survivor is composite.

**Why it might work.**  
The obstruction is combinatorial: each small prime blocks one residue class of offsets. Density and covering arguments may show that these moving residue classes cannot cover all relevant offsets.

**Likely failure point.**  
Standard Jacobsthal results use a fixed set of primes and only guarantee a coprime survivor. Here the threshold changes with \(d\), and the survivors may all be prime.

**Quick blockage test.**  
For each \(n\), classify every offset by its first blocking prime. Use set-cover or SAT formulations to determine how efficiently small primes can cover all offsets up to \(c\sqrt n\), and isolate the surviving prime offsets.

---

### Route 6: Disproof through CRT or covering constructions

**Core mechanism.**  
Try to construct infinitely many \(n\) for which every sufficiently large allowable \(d\) is blocked by a prime \(q\le d\), except possibly offsets where \(n+d\) is prime.

One would prescribe congruences
\[
n\equiv-d\pmod q
\]
so that \(q\mid n+d\) for selected groups of offsets.

**Needed lemma.**  
For some fixed \(B\), construct arbitrarily large \(n\) such that every
\[
B<d<\frac{1+\sqrt{1+4n}}2
\]
satisfies either

- \(q\mid n+d\) for some \(q\le d\), or
- \(n+d\) is provably prime.

A stronger and cleaner construction would block every such \(d\) by a small divisor.

**Why it might work.**  
CRT constructions are effective for producing long runs of composite integers and could conceivably be adapted so that the assigned divisor is no larger than the offset.

**Likely failure point.**  
There is a severe self-consistency problem. Covering a range of length \(L\) generally requires a modulus whose size grows rapidly with \(L\), while the range that must be covered is about \(\sqrt n\). Choosing \(n\) in a CRT class usually makes \(\sqrt n\) far larger than the initially covered range. Moreover, CRT does not naturally force the uncovered values to be prime.

**Quick blockage test.**  
For increasing \(L\), solve the finite covering problem:
assign primes \(q_d\le d\) so that the congruences for \(n\) are compatible and all \(B<d\le L\) are covered. Compare the least CRT solution \(n\) with \(L^2\). A scalable disproof requires \(L\) at least of order \(\sqrt n\), not merely \(O(\log n)\).

---

## 8. VERDICT ON DIFFICULTY

This is a genuinely difficult pointwise sieve problem. Its difficulty comes from the simultaneous requirements that:

- the result hold for every sufficiently large \(n\);
- the offset tend uniformly to infinity;
- \(n+d\) avoid every prime factor up to the moving threshold \(d\);
- \(n+d\) nevertheless be composite;
- the allowable offset range is only \(O(\sqrt n)\).

The “composite but very rough” requirement places the problem directly near the sieve parity barrier. Standard methods can often count rough integers or primes, but proving that every translated short interval contains a rough **composite** is substantially harder.

The commentary’s proposed asymptotic
\[
n-F_C(n)\sim c\sqrt n
\]
is a closely related and apparently very strong question, but it does not formally settle Problem #463 without an additional theorem controlling the right endpoint of the relevant interval.

There is no clear known equivalence to a single famous conjecture such as the Riemann Hypothesis, Legendre’s conjecture, or Cramér’s conjecture. Ordinary prime-gap conjectures are not enough because primes are excluded. Nevertheless, a solution likely requires ideas comparable in strength to difficult uniform results on primes or almost primes in highly structured short sets.

The heuristic outlook is favorable: the prime-pair model suggests many possible balanced semiprime witnesses for a typical \(n\), and large valid distances should be common. The obstacle is eliminating all exceptional \(n\). Conversely, a disproof would require an unexpectedly efficient arithmetic covering construction at the square-root scale. Thus the problem appears plausible but technically formidable, with the main barrier being uniformity rather than average density.