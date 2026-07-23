# Problem brief: Erdős Problem #68

## 1. Precise statement

Let \(\mathbb N=\{1,2,3,\dots\}\), and for \(n\in\mathbb N\) define
\[
n!:=\prod_{j=1}^n j.
\]
Consider the real number
\[
\alpha:=\sum_{n=2}^{\infty}\frac{1}{n!-1}.
\]

The series is well-defined because \(n!-1>0\) for every \(n\ge 2\), and it converges absolutely: since \(n!\ge 2\),
\[
0<\frac1{n!-1}\le \frac2{n!},
\]
and \(\sum_{n\ge2}2/n!<\infty\).

The problem asks whether
\[
\boxed{\alpha\notin\mathbb Q.}
\]
Equivalently, is it true that for every pair of integers \(p,q\) with \(q\ne0\),
\[
\alpha\ne \frac pq?
\]

There is no serious ambiguity in the displayed database statement. The lower limit \(n=2\) is essential: the \(n=1\) term would be \(1/(1!-1)\), which is undefined.

### Equivalent representations

For every \(n\ge2\),
\[
\frac1{n!-1}
=\frac{1/n!}{1-1/n!}
=\sum_{k=1}^{\infty}\frac1{(n!)^k}.
\]
All terms are nonnegative, so Tonelli’s theorem gives
\[
\alpha
=\sum_{n=2}^{\infty}\sum_{k=1}^{\infty}\frac1{(n!)^k}
=\sum_{k=1}^{\infty}\sum_{n=2}^{\infty}\frac1{(n!)^k}.
\]

If
\[
H_k:=\sum_{n=0}^{\infty}\frac1{(n!)^k},
\]
then
\[
\alpha=\sum_{k=1}^{\infty}(H_k-2).
\]
For \(k\ge1\),
\[
H_k={}_0F_{k-1}(\,;1,\dots,1;1),
\]
with \(H_1=e\). Thus
\[
\alpha=(e-2)+\sum_{k=2}^{\infty}(H_k-2).
\]

There is also a useful integral representation:
\[
\frac1{n!-1}=\int_0^1 x^{n!-2}\,dx,
\]
hence, again by Tonelli,
\[
\alpha=\int_0^1\left(\sum_{n=2}^{\infty}x^{n!-2}\right)\,dx.
\]

Finally, define
\[
\Phi(z):=\sum_{n=2}^{\infty}\frac1{n!-z}.
\]
This is analytic for \(|z|<2\), and
\[
\Phi(1)=\alpha,\qquad
\Phi(z)=\sum_{j=0}^{\infty}z^j\sum_{n=2}^{\infty}\frac1{(n!)^{j+1}}.
\]

The decimal expansion is OEIS A331373; numerically,
\[
\alpha\approx 1.2534987557.
\]
Numerics have no bearing on the required proof.

---

## 2. What counts as a solution

### A complete proof of irrationality

A complete solution in the affirmative must prove unconditionally that
\[
\alpha\notin\mathbb Q.
\]
Concretely, it must rule out every reduced fraction \(p/q\), \(p\in\mathbb Z\), \(q\in\mathbb N\).

Any of the following would suffice:

1. A direct contradiction from the assumption \(\alpha=p/q\).
2. A proof that \(\alpha\) is transcendental.
3. A rigorous demonstration that the decimal expansion is not eventually periodic.
4. A rigorous demonstration that the factorial expansion of \(\alpha\) does not terminate, accounting for the usual endpoint ambiguity.
5. A sequence of certified integer linear forms
   \[
   L_m=A_m\alpha-B_m,\qquad A_m,B_m\in\mathbb Z,
   \]
   whose size, divisibility, and nonvanishing contradict rationality.
6. A proof that \(m!\alpha\notin\mathbb Z\) for infinitely many \(m\). Indeed, if \(\alpha=p/q\), then \(m!\alpha\in\mathbb Z\) for every \(m\ge q\).

All limiting arguments must include effective error bounds and a proof of nonvanishing where required.

### A complete disproof

A disproof must establish that \(\alpha\) is rational. It must produce integers \(p,q\), with \(q>0\) and preferably \(\gcd(p,q)=1\), and prove
\[
\sum_{n=2}^{\infty}\frac1{n!-1}=\frac pq.
\]

A finite numerical match is not a proof. A verifiable rationality certificate could, for example, consist of a sequence \(T_N\in\mathbb Q\) satisfying
\[
T_N-T_{N+1}=\frac1{(N+1)!-1},\qquad
\lim_{N\to\infty}T_N=0,
\]
and
\[
\frac pq-\sum_{n=2}^N\frac1{n!-1}=T_N.
\]
Such identities would telescope and prove the claim. Any other exact identity proving equality with \(p/q\) is equally acceptable.

---

## 3. What does not count

The following do **not** resolve the problem:

- Computing any finite number of decimal digits.
- Finding no small-denominator rational approximation.
- A PSLQ or integer-relation search that finds no relation.
- Proving only that \(\alpha\) is not an integer.
- Proving irrationality of a finite partial sum; every finite partial sum is rational.
- Proving that \(e-2\) is transcendental. The remaining positive tail could, in principle, cancel it to a rational number.
- Proving irrationality or transcendence of one or more individual \(H_k\) without controlling their infinite sum.
- Proving that at least one number in a family containing \(\alpha\) is irrational.
- Proving the result for “almost every” real parameter \(t\), or for infinitely many integers \(t\), without proving the case \(t=-1\).
- Conditional proofs depending on Schanuel’s conjecture, algebraic-independence conjectures, unproved distribution hypotheses, or Erdős’s broader transcendence prediction.
- Irrationality measures or rational-approximation estimates that do not actually exclude rationality.
- Showing that a related generating function has a natural boundary.
- Heuristic claims that the terms or digits “behave randomly.”
- A modular computation applied directly to the infinite real series without a justified finite truncation and tail argument.

---

## 4. Known results and context

### 4.1 Database commentary

Weisenberg observed the exact identity
\[
\alpha=\sum_{k=1}^{\infty}\sum_{n=2}^{\infty}\frac1{(n!)^k}.
\]

Erdős noted in [Er88c] that sums of the form
\[
\sum \frac1{n!+t}
\]
should be transcendental for every integer \(t\), subject to choosing the lower limit so that no denominator vanishes. The present problem is the case \(t=-1\), with \(n\ge2\). This is a conjectural context, not a known theorem.

### 4.2 The first geometric layer is understood

The \(k=1\) contribution is
\[
\sum_{n=2}^{\infty}\frac1{n!}=e-2,
\]
which is transcendental by the Hermite–Lindemann theorem. Thus
\[
\alpha=(e-2)+\beta,\qquad
\beta:=\sum_{k=2}^{\infty}\sum_{n=2}^{\infty}\frac1{(n!)^k}.
\]
No known principle prevents the infinite correction \(\beta\) from making the total rational.

### 4.3 Factorial expansion criterion

Every rational number has a terminating factorial expansion. Equivalently,
\[
x\in\mathbb Q
\quad\Longrightarrow\quad
m!x\in\mathbb Z
\quad\text{for every sufficiently large }m.
\]
Therefore it would suffice to prove
\[
m!\alpha\notin\mathbb Z
\]
for infinitely many \(m\). This criterion is elementary but potentially important.

It does not by itself solve the problem, because the fractional parts of \(m!\alpha\) include complicated contributions from all terms \(1/(n!-1)\).

### 4.4 Lacunary integral

Set
\[
F(z):=\sum_{n=2}^{\infty}z^{n!-2}.
\]
The exponent sequence \(n!-2\) satisfies the Hadamard gap condition eventually. Hence the Hadamard gap theorem implies that the unit circle is a natural boundary for \(F\). Moreover,
\[
\alpha=\int_0^1F(x)\,dx.
\]

This gives useful analytic structure but no automatic arithmetic conclusion: a function may have a natural boundary while a particular integral or value is rational.

### 4.5 Hypergeometric viewpoint

For fixed \(k\),
\[
H_k=\sum_{n=0}^{\infty}\frac1{(n!)^k}
={}_0F_{k-1}(\,;1,\dots,1;1).
\]
The problem concerns an infinite sum over \(k\), not a finite linear combination of standard special-function values. Classical transcendence theorems for \(e\) do not directly extend to this aggregate.

### 4.6 Elementary bounds

Let
\[
S_N:=\sum_{n=2}^N\frac1{n!-1},\qquad R_N:=\alpha-S_N,
\]
and put \(m=N+1\). Then
\[
R_N>\frac1{m!-1}.
\]
Also,
\[
\frac1{n!-1}
=\frac{1/n!}{1-1/n!}
\le \frac{1}{1-1/m!}\frac1{n!}
\qquad(n\ge m),
\]
and
\[
\sum_{n=m}^{\infty}\frac1{n!}
\le \frac{m+1}{m\,m!}.
\]
Therefore
\[
\boxed{
\frac1{m!-1}<R_N
\le
\frac1{1-1/m!}\frac{m+1}{m\,m!}.
}
\]
These bounds permit rigorous interval computations to arbitrary precision.

### 4.7 Status

The irrationality question itself remains open. Neither rationality nor irrationality is currently known. The broader transcendence assertion attributed to Erdős would settle it much more strongly, but that assertion is also unproved.

---

## 5. Traps and edge cases

1. **The \(n=1\) term is undefined.**  
   Never extend the original sum to \(n=1\).

2. **The geometric expansion begins at \(k=1\).**
   \[
   \frac1{n!-1}=\sum_{k=1}^{\infty}(n!)^{-k},
   \]
   not at \(k=0\).

3. **“Contains \(e\)” is not an irrationality proof.**  
   A transcendental number plus another transcendental number may be rational.

4. **Partial sums have bad denominators.**  
   If
   \[
   S_N=\sum_{n=2}^N\frac1{n!-1},
   \]
   its denominator divides
   \[
   \operatorname{lcm}_{2\le n\le N}(n!-1),
   \]
   not \(N!\). There is no simple nesting relation \(n!-1\mid (n+1)!-1\).

5. **Multiplication by \(N!\) does not clear the head.**  
   Generally,
   \[
   \frac{N!}{n!-1}\notin\mathbb Z.
   \]

6. **Common-denominator arguments can destroy tail smallness.**  
   Multiplying by \(\prod_{n\le N}(n!-1)\) clears a truncation but makes the scaled tail enormous.

7. **Every prime divisor of \(n!-1\) exceeds \(n\).**  
   If \(p\le n\), then \(p\mid n!\), so \(p\nmid n!-1\). This is useful, but it does not imply that \(n!-1\) has a prime factor not occurring in earlier terms.

8. **A real infinite series cannot simply be reduced modulo a prime.**  
   One must first produce a finite rational identity and control the real tail.

9. **Factorial-digit carries are serious.**  
   The positive decomposition into powers \(1/(n!)^k\) does not imply sparse nonzero factorial digits after normalization.

10. **Factorial expansions have an endpoint ambiguity.**  
    As in \(0.999\ldots=1\), terminating expansions can have an alternative tail of maximal digits. Any digit proof must rule out both forms or use the criterion \(m!\alpha\in\mathbb Z\).

11. **Natural boundary does not imply irrationality.**  
    The lacunarity of \(F(z)\) is analytic information, not a value theorem for \(\int_0^1F(x)\,dx\).

12. **Good rational approximations alone are insufficient.**  
    Every real number has arbitrarily good approximations in weak senses. One needs approximations exceeding the relevant irrationality threshold, with controlled denominators and nonzero errors.

13. **Positivity prevents termwise cancellation but not arithmetic cancellation.**  
    The original summands are positive, yet their sum may still be rational.

14. **The general parameter statement has singular cases.**  
    In \(\sum1/(n!+t)\), negative \(t\) can make a denominator zero. The present lower limit avoids the singularity for \(t=-1\).

---

## 6. Verification hooks

The following computations can be implemented exactly.

### 6.1 Exact partial sums and certified intervals

Compute
\[
S_N=\sum_{n=2}^N\frac1{n!-1}
\]
using arbitrary-precision rational arithmetic. Set \(m=N+1\), and certify
\[
S_N+\frac1{m!-1}
<
\alpha
\le
S_N+
\frac1{1-1/m!}\frac{m+1}{m\,m!}.
\]

This provides rigorous decimal digits and can test proposed identities or inequalities.

### 6.2 Certified factorial-orbit computation

For given \(r\) and \(N\), compute the exact rational number
\[
r!S_N.
\]
Use
\[
0<r!(\alpha-S_N)\le
r!\frac1{1-1/(N+1)!}
\frac{N+2}{(N+1)(N+1)!}
\]
to enclose \(r!\alpha\) in a rational interval.

Check whether this interval:

- contains an integer;
- is disjoint from every integer;
- lies close to \(0\) modulo \(1\);
- exhibits any repeatable pattern as \(r\) varies.

For a proof via this route, such intervals must be shown to avoid integers for infinitely many \(r\), not merely for a finite search.

### 6.3 Factorial digits

For the fractional part \(x=\{\alpha\}\), the canonical factorial digits can be generated by
\[
r_1=x,\qquad
a_n=\lfloor n r_{n-1}\rfloor,\qquad
r_n=n r_{n-1}-a_n,
\]
where \(0\le a_n\le n-1\) and
\[
x=\sum_{n=2}^{\infty}\frac{a_n}{n!}.
\]

Use certified intervals for \(x\). A digit \(a_n\) is certified only when the interval for \(nr_{n-1}\) lies strictly between two consecutive integers. Record positions where ambiguity caused by carries remains.

### 6.4 Denominator and prime-factor incidence

For
\[
d_n=n!-1,
\]
compute:

- factorizations of \(d_n\) for feasible \(n\);
- \(\gcd(d_m,d_n)\);
- the largest prime factor \(P^+(d_n)\);
- prime powers appearing for the first time at \(n\);
- \(\log\operatorname{lcm}(d_2,\dots,d_N)\);
- the incidence matrix \(p\mid d_n\).

This tests whether modular isolation of individual summands is plausible.

### 6.5 Geometric-layer truncation

For \(K,N\ge1\), compute
\[
A_{K,N}:=\sum_{k=1}^K\sum_{n=2}^N\frac1{(n!)^k}.
\]
The omitted \(k\)-tail at fixed \(n\) is
\[
\sum_{k>K}\frac1{(n!)^k}
=\frac{1}{(n!)^{K+1}}\frac1{1-1/n!}.
\]
Both the \(k\)-tail and \(n\)-tail can therefore be bounded explicitly. This is useful for testing proposed hypergeometric or linear-form identities.

### 6.6 Padé and recurrence searches

Compute exact Taylor coefficients
\[
c_j=\sum_{n=2}^{\infty}\frac1{(n!)^{j+1}}
\]
to certified precision, or truncate in \(n\) with explicit error. Then:

- search for low-order polynomial-coefficient recurrences in \(j\);
- search for differential equations for \(\Phi(z)\);
- construct Padé approximants to \(\Phi\);
- monitor denominator height versus error at \(z=1\).

Failure of low-order guessing is not a theorem, but it quickly tests whether a classical holonomic approach is realistic.

### 6.7 Symbolic telescoping search

Search for a rational function \(R(n,x)\) satisfying
\[
R(n,n!)-R(n+1,(n+1)!)=\frac1{n!-1}.
\]
Since \((n+1)!=(n+1)n!\), this becomes an algebraic functional equation
\[
R(n,x)-R(n+1,(n+1)x)=\frac1{x-1}.
\]
Test bounded-degree rational ansätze in \(n\) and \(x\). Also test block telescoping identities involving several consecutive terms.

---

## 7. Attack routes

### Route 1: Factorial expansion and the orbit \(\{m!\alpha\}\)

**Core mechanism.**  
Exploit the elementary rationality criterion
\[
\alpha\in\mathbb Q\implies m!\alpha\in\mathbb Z
\quad\text{for all sufficiently large }m.
\]

**Key lemma needed.**  
Prove that there are infinitely many \(m\) for which
\[
\operatorname{dist}(m!\alpha,\mathbb Z)>0,
\]
preferably with an explicit lower bound. A usable form would be a decomposition
\[
m!\alpha=X_m+Y_m,
\]
where \(X_m\) is rational with controlled residue and \(Y_m\) is smaller than the distance from \(X_m\) to the nearest integer.

**Why it might work.**  
Factorial multiplication is exactly adapted to rationality: every fixed rational denominator eventually divides \(m!\). The series itself is also built from factorials, so there may be a hidden residue pattern.

**Most likely failure point.**  
Although the tail can be made tiny by truncating far beyond \(m\), the finite head
\[
m!\sum_{n=2}^N\frac1{n!-1}
\]
has complicated denominators. No evident monotonicity or congruence controls its fractional part.

**Quick blockage test.**  
For \(m\le M\), choose \(N\) so the scaled tail is below \(10^{-P}\), compute a certified interval for \(\{m!\alpha\}\), and inspect whether it repeatedly approaches \(0\). Also compare the exact residues of \(m!S_N\) against the relevant denominator. A lack of any stable pattern by moderately large \(m\) suggests that a simple digit argument is blocked.

---

### Route 2: Prime-divisor isolation and modular contradiction

**Core mechanism.**  
Use prime divisors of \(d_n=n!-1\) to isolate one or a small number of summands after clearing selected denominators.

**Key lemma needed.**  
One needs a strong “private divisor” statement, for example: infinitely often \(n!-1\) has a prime power \(p^a\) that does not divide the relevant common denominator formed from other terms and is sufficiently large to survive a tail estimate. A weaker structured incidence lemma may also suffice.

**Why it might work.**  
Every prime divisor of \(n!-1\) is \(>n\), and factorial-minus-one numbers often contain large prime factors. A sufficiently isolated prime could force a nonzero residue inconsistent with an assumed rational identity.

**Most likely failure point.**  
There is no direct Zsigmondy theorem for the sequence \(n!-1\). Prime factors may recur across different \(m!-1\), and reducing an infinite real identity modulo \(p\) is invalid unless the tail has first been handled exactly.

**Quick blockage test.**  
Factor \(n!-1\) for feasible \(n\), record primitive prime powers and recurrence frequencies, and compare their logarithmic size with the denominator and tail costs of the proposed multiplier. If private factors are too small or the multiplier grows faster than the reciprocal tail, the straightforward modular route is blocked.

---

### Route 3: Padé approximants and integer linear forms

**Core mechanism.**  
Construct rational or Hermite–Padé approximants to
\[
\Phi(z)=\sum_{n=2}^{\infty}\frac1{n!-z}
\]
or to a finite collection of the functions
\[
\sum_{n=0}^{\infty}\frac{z^n}{(n!)^k},
\]
then evaluate at \(z=1\) to obtain small integer linear forms in \(1\) and \(\alpha\).

**Key lemma needed.**  
Produce integers \(A_m,B_m\) such that
\[
0<|A_m\alpha-B_m|
\]
is smaller than what would be possible if \(\alpha\) were rational, while keeping \(|A_m|\) and all clearing denominators under control. Nonvanishing must be proved, perhaps through positivity or an integral representation.

**Why it might work.**  
Many classical irrationality proofs for special constants arise from exceptionally accurate Padé approximation combined with arithmetic denominator estimates. Factorial coefficients can produce very rapid analytic convergence.

**Most likely failure point.**  
The denominators needed to clear the finite approximants may grow faster than the approximation error decays. Also, \(\Phi\) does not obviously belong to a standard finite-dimensional differential system amenable to classical Padé theory.

**Quick blockage test.**  
Construct exact Padé approximants of increasing degree and record
\[
-\log|\Phi(1)-P_m(1)/Q_m(1)|
\quad\text{versus}\quad
\log\operatorname{den}(P_m(1)/Q_m(1)).
\]
If the error exponent does not beat the denominator growth, the naive version cannot prove irrationality.

---

### Route 4: Hypergeometric value theory and algebraic independence

**Core mechanism.**  
Use
\[
\alpha=\sum_{k=1}^{\infty}(H_k-2),\qquad
H_k={}_0F_{k-1}(\,;1,\dots,1;1),
\]
and seek a theorem controlling rational or algebraic relations among the \(H_k\), uniformly in \(k\).

**Key lemma needed.**  
A sufficiently strong statement would assert that the infinite correction
\[
\sum_{k=2}^{\infty}(H_k-2)
\]
cannot differ from an algebraic number by \(-e\). More realistically, one could seek finite truncation results together with tail estimates and lower bounds for linear forms involving \(1,e,H_2,\dots,H_K\), uniform as \(K\to\infty\).

**Why it might work.**  
The \(k=1\) term is \(e-2\), and the remaining constants are highly structured hypergeometric values rather than arbitrary reals.

**Most likely failure point.**  
Available transcendence machinery generally treats finite systems. The number of hypergeometric functions grows with \(K\), and useful algebraic-independence estimates uniform in \(K\) appear far beyond standard results. One must also check carefully whether a proposed class is genuinely covered by \(E\)-function or \(G\)-function theorems.

**Quick blockage test.**  
For small \(K\), identify the exact differential equations of \(H_k(z)=\sum z^n/(n!)^k\), examine whether an applicable transcendence theorem really covers their values at \(1\), and estimate how constants deteriorate with \(K\). If even the finite values fall outside the theorem’s arithmetic hypotheses, the route is presently blocked.

---

### Route 5: Lacunary-series and moment methods

**Core mechanism.**  
Use
\[
\alpha=\int_0^1F(x)\,dx,\qquad
F(x)=\sum_{n=2}^{\infty}x^{n!-2},
\]
and exploit the extreme gaps in the exponent set.

**Key lemma needed.**  
Construct polynomials \(P_m(x)\), preferably with integer coefficients and controlled height, such that
\[
\int_0^1P_m(x)F(x)\,dx
\]
is both arithmetically related to an integer linear form in \(1,\alpha\) and analytically very small and nonzero. Alternatively, prove a direct arithmetic theorem for integrals of \(0\)-\(1\) lacunary power series with exponent sequence \(n!-2\).

**Why it might work.**  
The factorial gaps allow polynomial weights to annihilate or suppress long blocks of moments. Positivity may help certify nonvanishing, in the style of Beukers-type integral proofs.

**Most likely failure point.**  
The moments are
\[
\int_0^1x^{n!-2+j}\,dx=\frac1{n!-1+j},
\]
whose denominators are not nested. Clearing them may cost more than the lacunarity gains. The natural-boundary theorem by itself gives no irrationality information.

**Quick blockage test.**  
Optimize low-degree integer polynomials \(P\) numerically or by linear programming to minimize the integral while computing the exact common denominator of the resulting moments. Compare exponential decay of the integral with growth of that denominator.

---

### Route 6: Disproof through exact telescoping or a rational functional identity

**Core mechanism.**  
Search for an exact identity showing that the series telescopes, possibly after grouping terms or introducing an auxiliary rational function of \(n\) and \(n!\).

**Key lemma needed.**  
Find \(G_n\in\mathbb Q\), given by a verifiable closed form, such that
\[
\frac1{n!-1}=G_n-G_{n+1}
\quad(n\ge2),
\qquad
G_n\to0.
\]
Then
\[
\alpha=G_2\in\mathbb Q.
\]
A block identity involving several consecutive summands would also suffice.

**Why it might work.**  
Factorial recurrences occasionally conceal telescoping identities, and rationality can only be disproved by an exact structural mechanism of this kind or something comparably rigid. Automated symbolic summation can search broad classes efficiently.

**Most likely failure point.**  
The summand is not hypergeometric in \(n\) in the usual sense:
\[
\frac{a_{n+1}}{a_n}
=\frac{n!-1}{(n+1)!-1}
\]
is not a rational function of \(n\). A simple Gosper-style antiderivative is therefore unlikely.

**Quick blockage test.**  
Solve
\[
R(n,x)-R(n+1,(n+1)x)=\frac1{x-1}
\]
over bounded-degree rational functions \(R(n,x)\). Then enlarge to algebraic-logarithmic ansätze and short block telescoping. Failure at low degrees does not prove irrationality, but it rules out the most plausible simple rationality certificates.

---

## 8. Verdict on difficulty

This is a genuinely difficult open irrationality problem. The summands are elementary and the convergence is extremely rapid, but the denominators \(n!-1\) do not form a divisibility chain, which defeats the most direct Cantor-series, factorial-base, and denominator-clearing arguments.

The broader conjecture attributed to Erdős—that \(\sum 1/(n!+t)\) should be transcendental for every admissible integer \(t\)—would settle the problem immediately and much more strongly. That conjecture is itself far beyond current elementary transcendence methods.

There is no known equivalence to a single famous conjecture such as Schanuel’s conjecture, nor is a famous conjecture currently known to be necessary. Nevertheless, routes through algebraic independence may demand machinery of comparable depth. The most realistic near-term targets are:

1. a new factorial-orbit or digit lemma;
2. an arithmetic use of large prime factors of \(n!-1\);
3. a Padé construction with unexpectedly favorable denominator growth;
4. an exact telescoping identity, which would instead prove rationality.

The innocent appearance of the series should not be mistaken for low difficulty: even proving irrationality, far short of Erdős’s predicted transcendence, remains open.