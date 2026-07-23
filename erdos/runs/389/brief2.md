# ROUND 2 PROBLEM BRIEF: ERDŐS PROBLEM #389

## 1. PRECISE STATEMENT

### 1.1 Original formulation

For positive integers \(n\) and \(k\), define the two consecutive blocks

\[
A(n,k)=\prod_{i=0}^{k-1}(n+i)
\]

and

\[
B(n,k)=\prod_{i=0}^{k-1}(n+k+i).
\]

The problem asks whether

\[
\boxed{\forall n\in \mathbb Z_{\ge 1}\ \exists k\in\mathbb Z_{\ge 1}
\quad A(n,k)\mid B(n,k).}
\]

Equivalently, for every \(n\ge 1\), is there a positive integer \(k\) such that

\[
\frac{B(n,k)}{A(n,k)}\in\mathbb Z?
\]

Here \(k\ge 1\) is essential. If one allowed \(k=0\), both products would be empty products equal to \(1\), making the problem trivial. Thus the standard and intended reading is \(k\in\mathbb Z_{\ge1}\).

---

### 1.2 Fixed-width notation

It is useful to put

\[
m=n-1,\qquad X=m+k=n+k-1,\qquad Y=2X-m=n+2k-1.
\]

Then \(m\ge0\), \(X>m\), and the two blocks are

\[
[m+1,X]\qquad\text{and}\qquad [X+1,Y].
\]

Define

\[
R_m(X)=\frac{Y!\,m!}{(X!)^2}
      =\frac{(2X-m)!\,m!}{(X!)^2}.
\]

The problem is equivalently

\[
\boxed{\forall m\in\mathbb Z_{\ge0}\ \exists X\in\mathbb Z,\ X>m,
\quad R_m(X)\in\mathbb Z.}
\]

The original parameter is recovered as

\[
n=m+1,\qquad k=X-m.
\]

The boundary between the two blocks is

\[
b=X+1=n+k.
\]

---

### 1.3 Equivalent binomial-coefficient formulations

Several exact identities are useful:

\[
R_m(X)
=
\frac{\binom{2X-m}{X}}{\binom{X}{m}}
=
\frac{\binom{2X}{X}}{\binom{2X}{m}}.
\]

Thus the problem can also be written as

\[
\boxed{\forall m\ge0\ \exists X>m:
\quad \binom{2X}{m}\mid \binom{2X}{X}.}
\]

In the notation \(x=n-1=m\) and \(k=X-m\),

\[
R_m(X)
=
\frac{\binom{x+2k}{k}}{\binom{x+k}{k}}.
\]

---

### 1.4 Exact valuation formulation

For a prime \(p\), let \(v_p(r)\) denote the exponent of \(p\) in a nonzero rational number \(r\). Then

\[
R_m(X)\in\mathbb Z
\quad\Longleftrightarrow\quad
D_p(m,X):=v_p(R_m(X))\ge0
\quad\text{for every prime }p.
\]

By Legendre’s formula,

\[
D_p(m,X)=\sum_{a\ge1}E_{p^a}(m,X),
\]

where, for every integer \(q\ge2\),

\[
E_q(m,X)
=
\left\lfloor\frac{2X-m}{q}\right\rfloor
+\left\lfloor\frac m q\right\rfloor
-2\left\lfloor\frac Xq\right\rfloor.
\]

Writing

\[
r_q=X\bmod q,\qquad s_q=m\bmod q,
\]

one has the exact residue formula

\[
\boxed{
E_q(m,X)
=
\left\lfloor\frac{2r_q-s_q}{q}\right\rfloor
\in\{-1,0,1\}.
}
\]

Only powers \(p^a\le Y\) can contribute.

Therefore a completely formal version of the problem is

\[
\boxed{
\forall m\ge0\ \exists X>m\ \forall p\text{ prime}:
\sum_{\substack{a\ge1\\p^a\le 2X-m}}
\left\lfloor
\frac{2(X\bmod p^a)-(m\bmod p^a)}{p^a}
\right\rfloor
\ge0.
}
\]

---

### 1.5 Carry formulation

Let \(c_p(u,v)\) be the number of carries, including propagated carries, when \(u\) and \(v\) are added in base \(p\). Kummer’s theorem gives

\[
D_p(m,X)
=
c_p(X-m,X)-c_p(X-m,m).
\]

Hence the problem is also:

> For every \(m\ge0\), does there exist \(X>m\) such that, for every prime \(p\), adding \(X-m\) to \(X\) in base \(p\) produces at least as many carries as adding \(X-m\) to \(m\)?

In the original clean notation \(x=n-1\), this is the supplied formulation with \(k=X-m\).

---

## 2. WHAT COUNTS AS A SOLUTION

### 2.1 Complete proof

A complete affirmative solution must prove, unconditionally, that for every integer \(m\ge0\) there exists an integer \(X>m\) such that one—and hence all—of the following equivalent conditions hold:

1. \(R_m(X)\in\mathbb Z\);
2. \(D_p(m,X)\ge0\) for every prime \(p\);
3. \(\binom{2X}{m}\mid \binom{2X}{X}\);
4. the original product divisibility holds with \(n=m+1\) and \(k=X-m\).

An explicit formula for \(X\) or \(k\) is not required, but an existence argument must control every prime, including primes that depend on the constructed \(X\).

A proof for all sufficiently large \(m\), together with rigorous verification of every omitted finite \(m\), would count. A terminating algorithm also counts only if its termination for every input \(m\) is proved.

---

### 2.2 Complete disproof

A complete negative solution must exhibit one integer

\[
m_0\ge1
\quad\text{equivalently}\quad
n_0=m_0+1\ge2
\]

and prove

\[
\forall X>m_0\ \exists p=p(X)\text{ prime}:
\quad D_p(m_0,X)<0.
\]

Equivalently, it must prove that no positive \(k=X-m_0\) works.

An “explicit counterexample” therefore consists of:

1. a specific integer \(n_0\);
2. a proof covering every \(k\ge1\), not merely a large finite range;
3. for each possible \(k\), a logically verifiable mechanism producing a prime \(p\) whose valuation is deficient.

A finite or automatic covering certificate could be acceptable if it comes with a rigorous induction or periodicity argument proving that it covers all \(X>m_0\). Exhaustive search up to a finite bound alone cannot disprove the statement.

---

### 2.3 Verification of a claimed candidate

For a proposed pair \((n,k)\), it suffices to compute \(D_p(m,X)\) for every prime \(p\le Y\). This is finite and exact.

For a claimed *minimal* \(k\), one must additionally verify failure for every \(1\le k'<k\).

---

## 3. WHAT DOES NOT COUNT

The following do not resolve the problem:

1. Proving the assertion only for infinitely many \(n\), for a positive-density set of \(n\), or for almost all \(n\).
2. Proving it for a finite range of \(n\), unless all remaining \(n\) are covered theoretically.
3. Finding very large solutions for many individual \(n\).
4. Improving upper bounds on the least \(k\) without proving it is finite for every \(n\).
5. Satisfying the valuation inequalities only for primes \(p\le P(n)\), with uncontrolled larger primes.
6. Producing a prime-free interval of the necessary length near \(X\). This is necessary but far from sufficient.
7. Making all endpoint integers composite.
8. Making all endpoint integers \(\sqrt{Y}\)-smooth. Smoothness is necessary in a large range but is not sufficient.
9. Proving the Gaussian or \(q\)-analogue is a polynomial; in fact that strengthening is impossible.
10. A conditional proof relying on Schinzel’s hypothesis, a prime-tuples conjecture, unproved smooth-value correlations, or another unproved conjecture.
11. Heuristics suggesting a positive density of good \(X\).
12. Failure of a search up to any finite bound.
13. A CRT construction that controls only a fixed finite collection of primes.
14. A proof that the rational number \(R_m(X)\) is large, or that its numerator exceeds its denominator. Integrality is prime-by-prime.

---

## 4. KNOWN RESULTS AND CONTEXT

### 4.1 Small cases and computed data

For \(n=1\), equivalently \(m=0\),

\[
R_0(X)=\frac{(2X)!}{(X!)^2}=\binom{2X}{X},
\]

so every \(k=X\ge1\) works. Thus \(k(1)=1\).

The supplied minimal values are:

\[
\begin{array}{c|c|c|c|c}
n&m=n-1&k_{\min}&X=m+k&b=X+1\\ \hline
1&0&1&1&2\\
2&1&5&6&7\\
3&2&4&6&7\\
4&3&207&210&211\\
5&4&206&210&211\\
6&5&2475&2480&2481\\
7&6&984&990&991\\
8&7&8171&8178&8179\\
9&8&8170&8178&8179\\
10&9&45144&45153&45154\\
11&10&45143&45153&45154
\end{array}
\]

For example,

\[
R_1(6)=77,\qquad R_2(6)=14.
\]

Bhavik Mehta has computed the minimal values through \(1\le n\le18\), recorded as OEIS A375071. Thus no \(n\le18\) is a counterexample.

Several adjacent values of \(n\) share the same boundary \(b=X+1\). In the supplied data:

\[
b=7,\ 211,\ 8179,\ 45154
\]

are shared by consecutive pairs. Here \(211\) and \(8179\) are prime, while

\[
45154=2\cdot107\cdot211.
\]

This is a genuine structural clue, but not yet a theorem.

The finite data are too short and too nonmonotone to justify a formal claim that the least \(k\) grows superpolynomially. The large values merely show that small-\(k\) searches are misleading.

---

### 4.2 Exact adjacent-parameter recurrences

For fixed \(X\),

\[
\boxed{
R_{m+1}(X)=R_m(X)\frac{m+1}{2X-m}.
}
\]

For fixed \(m\),

\[
\boxed{
R_m(X+1)=R_m(X)
\frac{(2X-m+1)(2X-m+2)}{(X+1)^2}.
}
\]

The first recurrence is directly relevant to shared boundaries. If the same \(X\) works for \(m\) and \(m+1\), then

\[
2X-m\mid (m+1)R_m(X).
\]

Also,

\[
R_m(X)=\frac{\binom{2X}{X}}{\binom{2X}{m}},
\]

so a single \(X\) works for all \(m\le M\) precisely when

\[
\operatorname{lcm}_{0\le r\le M}\binom{2X}{r}
\mid \binom{2X}{X}.
\]

---

### 4.3 Exact classification of negative levels

Let

\[
H=\left\lceil\frac m2\right\rceil.
\]

For \(q>m\), one has \(m\bmod q=m\), so

\[
E_q(m,X)=-1
\quad\Longleftrightarrow\quad
X\bmod q\in\{0,1,\ldots,H-1\}.
\]

Equivalently,

\[
\boxed{
q>m,\ E_q(m,X)=-1
\Longrightarrow
q\mid X-j
\text{ for some }0\le j<H.
}
\]

Thus every negative high-level contribution is attached to one of the endpoint integers

\[
X,\ X-1,\ldots,X-H+1.
\]

For \(q>m\),

\[
E_q(m,X)=1
\quad\Longleftrightarrow\quad
2(X\bmod q)-m\ge q.
\]

Every successful candidate with \(m>0\) must use cancellation between negative and positive powers of the same prime.

---

### 4.4 Prime-gap obstruction

Suppose \(q\) is prime and

\[
\max\left(m,\frac Y2\right)<q\le X.
\]

Then \(q\) occurs exactly once in the lower block and not at all in the upper block, so

\[
D_q(m,X)=-1.
\]

Therefore a necessary condition is

\[
\boxed{
\text{There is no prime }
q\in\left(\max\left(m,X-\frac m2\right),X\right].
}
\]

In original variables this is exactly

\[
q\in
\left(
\max\left(n-1,\frac{n+2k-1}{2}\right),
n+k-1
\right].
\]

For \(X>3m/2\), this requires a prime-free interval of length approximately \(m/2\) immediately below \(X\).

Arbitrarily long prime-free intervals exist, even by the elementary factorial construction, and much stronger large-gap theorems are known. Conversely, Baker–Harman–Pintz-type short-interval prime results limit how long a gap ending near \(X\) can be. None of these results controls the additional prime-power valuation conditions.

---

### 4.5 Stronger endpoint smoothness obstruction

Assume

\[
Y=2X-m>m^2.
\]

If a prime \(p>\sqrt{Y}\) divides one of

\[
X,\ X-1,\ldots,X-H+1,
\]

then \(p>m\), \(E_p=-1\), and \(p^2>Y\), so there is no higher \(p\)-power level available to compensate. Therefore

\[
\boxed{
P^+(X-j)\le\sqrt{Y}
\quad\text{for every }0\le j<H,
}
\]

where \(P^+(N)\) denotes the largest prime factor of \(N\).

More generally, if \(p>m\), \(0\le j<H\), and

\[
t=v_p(X-j),\qquad L=\lfloor\log_p Y\rfloor,
\]

then the first \(t\) \(p\)-power levels contribute \(-1\), while at most \(L-t\) higher levels can contribute \(+1\). Hence

\[
D_p(m,X)\le L-2t.
\]

In particular,

\[
\boxed{
p>m,\quad p^{2v_p(X-j)}>Y
\quad\Longrightarrow\quad D_p(m,X)<0.
}
\]

The restriction \(p>m\) is important in this simple form; small-prime levels can have additional behavior.

---

### 4.6 Smoothness is not sufficient

Two explicit failures are:

- \(m=1,\ X=30\): the only endpoint is \(30\), whose prime factors are all below \(\sqrt{59}\), but

  \[
  D_3(1,30)=-1.
  \]

- \(m=3,\ X=16\): the endpoints are \(16\) and \(15\), both \(\sqrt{29}\)-smooth, but

  \[
  D_2(3,16)=-4.
  \]

Thus any approach based only on largest prime factors is incomplete.

---

### 4.7 Sealing a fixed prime

A useful exact local lemma is:

> If \(p^A\mid k=X-m\) and \(p^A>m\), then
> \[
> D_p(m,X)\ge0.
> \]

Indeed, for \(a\le A\), \(X\equiv m\pmod{p^a}\), so \(E_{p^a}=0\). For \(a>A\), the residue \(X\bmod p^a\) is at least \(m\), so no negative level can occur.

Consequently, any prescribed finite collection of primes can be sealed simultaneously by CRT.

This does not solve the problem because making the CRT modulus larger also makes \(X\) larger and introduces new prime factors in the endpoint integers.

---

### 4.8 Every fixed CRT progression contains fresh failures

There is a rigorous form of the archimedean obstruction.

Fix \(m>0\) and an arithmetic progression

\[
X\equiv a\pmod M.
\]

Let \(d=\gcd(a,M)\). By Dirichlet’s theorem, there are infinitely many primes

\[
p\equiv a/d\pmod{M/d},
\]

with the modulus-\(1\) case interpreted trivially. For such \(p\), set

\[
X=dp.
\]

Then \(X\equiv a\pmod M\), and for sufficiently large \(p\),

\[
p>\sqrt{2X-m}.
\]

Since \(p\mid X\), this gives \(D_p(m,X)<0\).

Therefore:

\[
\boxed{
\text{Every fixed arithmetic progression of }X
\text{ contains infinitely many failures.}
}
\]

This does not say that a progression contains no successes. It proves that finite CRT control cannot make all sufficiently large representatives successful.

---

### 4.9 Composite endpoint runs can be forced, but do not suffice

For fixed \(m\), CRT can simultaneously:

1. seal all primes \(p\le m\);
2. force each endpoint \(X-j\), \(0\le j<H\), to have a prescribed nontrivial divisor;
3. locally balance the finitely many auxiliary primes used in the construction.

Thus one can construct entire composite endpoint blocks while controlling every prescribed finite set of primes.

The uncontrolled cofactor of an endpoint can nevertheless contain a new prime \(p>\sqrt{Y}\), immediately causing failure. Ordinary composite-run constructions therefore do not address the main obstruction.

---

### 4.10 Prime-power boundaries are impossible

If \(m>0\) and

\[
X=p^a
\]

is a prime power, then every level \(p^i\le X\) divides \(X\), so its contribution is \(0\) or \(-1\), and the level \(p^a=X\) contributes \(-1\). Since

\[
Y<2X\le pX=p^{a+1},
\]

there is no higher \(p\)-power level available. Hence

\[
D_p(m,X)<0.
\]

Thus no nontrivial solution can have \(X\) equal to a prime power.

---

### 4.11 The Gaussian-binomial strengthening is impossible

Define the \(q\)-factorial quotient

\[
G_{m,X}(z)
=
\frac{(z;z)_{2X-m}(z;z)_m}{(z;z)_X^2},
\qquad
(z;z)_r=\prod_{i=1}^r(1-z^i).
\]

Its cyclotomic exponent at \(\Phi_d(z)\) is exactly

\[
E_d(m,X).
\]

For \(m>0\),

\[
E_X(m,X)
=
\left\lfloor\frac{2X-m}{X}\right\rfloor
+\left\lfloor\frac mX\right\rfloor-2
=1+0-2=-1.
\]

Therefore \(G_{m,X}(z)\) is never a polynomial for any \(m>0\) and \(X>m\).

More strongly, if \(g=\gcd(m,X)\), then for every \(d\mid X\) with \(d\nmid m\),

\[
E_d(m,X)=-1.
\]

Hence the reduced cyclotomic denominator contains

\[
\frac{z^X-1}{z^g-1},
\]

of degree \(X-g\).

This kills every route requiring coefficientwise inequalities \(E_d\ge0\). Ordinary integrality survives only because, for a fixed prime \(p\), negative \(E_{p^a}\) may be offset by positive \(E_{p^b}\) at other powers of the same prime.

---

### 4.12 Analytic information from Round 1

The previous analysis established two useful qualitative facts for fixed \(m\):

1. For some \(\eta>0\), all but \(o(T)\) integers \(X\in[T,2T]\) satisfy

   \[
   D_p(m,X)\ge0
   \quad\text{for every }
   p\le \exp\!\bigl(\eta\sqrt{\log T}\bigr).
   \]

   Thus the main obstruction lies in moving medium and large primes.

2. At one endpoint, the obstruction from a prime factor exceeding \(\sqrt{Y}\) has asymptotic density

   \[
   \log 2+o(1).
   \]

   Equivalently, the one-endpoint probability of avoiding this top obstruction is approximately

   \[
   1-\log2\approx0.30685.
   \]

No valid independence theorem is known for the \(H\) shifted endpoints. Moreover, even simultaneous smoothness would not settle the higher-power digit conditions.

---

### 4.13 Relevant named results

The main standard tools are:

- Legendre’s formula for \(v_p(N!)\);
- Kummer’s theorem on carries and binomial valuations;
- Dirichlet’s theorem on primes in arithmetic progressions;
- Bertrand-type and Baker–Harman–Pintz short-interval prime results;
- elementary and Rankin-type constructions of large prime gaps;
- Dickman–de Bruijn theory for one-dimensional smooth-number statistics;
- Farhi’s binomial-row lcm identity
  \[
  \operatorname{lcm}_{0\le r\le N}\binom Nr
  =
  \frac{\operatorname{lcm}(1,2,\ldots,N+1)}{N+1}.
  \]

None currently resolves the required simultaneous shifted and prime-power conditions.

---

## 5. DEAD ROUTES FROM ROUND 1

The following should not be retried without a genuinely new ingredient.

### 5.1 Coefficientwise cyclotomic positivity

Requiring

\[
E_d(m,X)\ge0\qquad\text{for every }d
\]

is impossible because \(E_X=-1\) for every \(m>0\). The entire Gaussian-polynomial route is categorically dead.

---

### 5.2 Pure finite-prime CRT control

Any fixed finite set of primes can be sealed, but the resulting larger \(X\) has new endpoint factors. Every fixed CRT progression contains infinitely many failures caused by fresh large primes.

A successful construction must control the factorization of the final endpoint values, not merely their residues modulo a predetermined modulus.

---

### 5.3 Ordinary composite runs

Forcing

\[
X,\ X-1,\ldots,X-H+1
\]

to be composite leaves uncontrolled cofactors. A composite endpoint can still contain a prime \(p>\sqrt{Y}\), which causes immediate failure.

---

### 5.4 Prime-gap-only arguments

The required prime-free window is necessary but eliminates only endpoint values that are themselves large primes. It does not eliminate large prime factors of composite endpoints.

Known prime-gap theorems therefore do not close the problem.

---

### 5.5 Smoothness-only arguments

Simultaneous \(\sqrt{Y}\)-smoothness is necessary for large \(X\), but the examples \((m,X)=(1,30)\) and \((3,16)\) show it is not sufficient.

Higher \(p\)-power residue balance must be retained.

---

### 5.6 Prime-power choices of \(X\)

These always fail for \(m>0\), as explained above.

---

### 5.7 Naive union bounds and independence heuristics

A single endpoint top obstruction already has density about \(\log2\). A union bound is useless once several endpoints are present, and no independence theorem for the shifted smoothness and digit conditions is available.

---

## 6. TRAPS AND EDGE CASES

1. **The case \(n=1\).** Here \(m=0\), and every \(k\ge1\) works. Statements such as \(E_X=-1\) require \(m>0\).

2. **Off-by-one errors.**
   \[
   X=n+k-1,\qquad b=X+1=n+k,\qquad Y=n+2k-1.
   \]
   The last lower-block term is \(X\), while the first upper-block term is \(X+1\).

3. **Prime versus prime power.** A negative level \(E_d=-1\) matters for ordinary integrality only when \(d=p^a\). Negative composite non-prime-power levels matter for the \(q\)-analogue but not directly for any \(v_p\).

4. **Cancellation is only within one prime chain.** A negative \(E_{p^a}\) can be offset by positive \(E_{p^b}\), but never by a power of another prime.

5. **Floor division with negative numerators.** In code,
   \[
   E_q=\left\lfloor\frac{2r-s}{q}\right\rfloor.
   \]
   Languages that truncate negative integer division toward \(0\) will give wrong answers.

6. **A prime-free endpoint interval is not enough.** Large prime factors of composite endpoint values remain dangerous.

7. **Smoothness threshold has hypotheses.** The simple conclusion \(P^+(X-j)\le\sqrt Y\) uses \(Y>m^2\), ensuring that a prime above \(\sqrt Y\) is also above \(m\).

8. **The bound \(D_p\le L-2t\)** is clean for \(p>m\). Do not apply it blindly to \(p\le m\).

9. **Large total size is irrelevant.** The fact that \(R_m(X)\gg1\) does not imply integrality.

10. **A negative \(E_X\) does not by itself disprove ordinary integrality** unless \(X\) is a prime power. Its main role is to kill coefficientwise cyclotomic positivity.

11. **Finite-prime success is not close to completion.** The uncontrolled primes are exactly those tied to the final endpoint factorizations.

12. **Shared boundaries must be interpreted at fixed \(X\), not fixed \(k\).** For adjacent \(n\), the same boundary gives different \(k\).

13. **Finite growth data do not establish asymptotic growth.** The observed least \(k\) values are irregular and nonmonotone in \(n\).

---

## 7. VERIFICATION HOOKS

### 7.1 Exact candidate checker

For given \(n,k\):

1. Set
   \[
   m=n-1,\quad X=m+k,\quad Y=2X-m.
   \]
2. Sieve all primes \(p\le Y\).
3. For each prime \(p\), compute
   \[
   D_p=\sum_{p^a\le Y}
   \left\lfloor
   \frac{2(X\bmod p^a)-(m\bmod p^a)}{p^a}
   \right\rfloor.
   \]
4. Accept if and only if every \(D_p\ge0\).

This avoids huge factorials.

---

### 7.2 Independent Legendre check

Verify against

\[
D_p=
\sum_{a\ge1}
\left(
\left\lfloor\frac Y{p^a}\right\rfloor
+\left\lfloor\frac m{p^a}\right\rfloor
-2\left\lfloor\frac X{p^a}\right\rfloor
\right).
\]

The residue implementation and the Legendre implementation should agree exactly.

---

### 7.3 Carry checker

For each prime \(p\le Y\), count base-\(p\) carries in

\[
(X-m)+X
\]

and in

\[
(X-m)+m.
\]

Check that their difference equals \(D_p\).

This is useful for catching residue and floor-division bugs.

---

### 7.4 Minimality verification

For fixed \(n\), test \(k=1,2,\ldots\) in increasing order. Record the first success. This reproduces the supplied data through \(n=11\), and the OEIS values through \(18\).

For each failed \(k\), store the least prime \(p\) with \(D_p<0\). The distribution of witness primes is useful research data.

---

### 7.5 Endpoint-obstruction diagnostics

For each candidate:

1. factor
   \[
   X,\ X-1,\ldots,X-H+1;
   \]
2. reject immediately if any has a prime factor \(>\sqrt Y\);
3. for each endpoint prime \(p>m\), record
   \[
   t=v_p(X-j),\quad L=\lfloor\log_pY\rfloor,
   \]
   and test whether \(2t>L\).

This identifies whether failure is caused by a top prime, a repeated prime factor, or a subtler digit imbalance.

---

### 7.6 Verify the smooth-but-bad examples

The implementation should confirm:

\[
D_3(1,30)=-1,
\]

and

\[
D_2(3,16)=-4.
\]

These are mandatory regression tests against any proposed “smoothness implies success” lemma.

---

### 7.7 Shared-boundary search

For each \(X\le B\), compute the set

\[
S_X=\{m<X:R_m(X)\in\mathbb Z\}.
\]

Record:

- intervals of consecutive \(m\) contained in \(S_X\);
- whether supplied boundaries \(X=6,210,8178,45153\) solve more \(m\) than the two known minimal cases;
- the longest initial segment \(\{0,1,\ldots,M\}\subseteq S_X\).

This directly tests Route 1 below.

---

### 7.8 Prime-chain ledger

For every successful or near-successful pair \((m,X)\), output the sequence

\[
E_p,E_{p^2},E_{p^3},\ldots
\]

for each prime dividing an endpoint. Identify explicit matchings

\[
E_{p^a}=-1
\longleftrightarrow
E_{p^b}=+1,\qquad b>a.
\]

The goal is to discover recurring compensation patterns rather than merely record \(D_p\).

---

### 7.9 Finite disproof-certificate checker

Any proposed counterexample mechanism should be encoded as a partition of all \(X>m_0\) into symbolic classes. Each class must provide a prime \(p\) and enough residue or factorization information to prove \(D_p<0\).

The checker should verify:

1. every class’s valuation claim;
2. disjointness or harmless overlap;
3. exhaustive coverage, including the induction from one size range to the next.

---

## 8. FOUR NEW ROUND-2 ATTACK ROUTES

## Route 1: Universal boundaries via truncated binomial-row lcm

### Core mechanism

Use

\[
R_m(X)=\frac{\binom{2X}{X}}{\binom{2X}{m}}.
\]

For \(M<X\), define

\[
L_M(X)=\operatorname{lcm}_{0\le r\le M}\binom{2X}{r}.
\]

If

\[
L_M(X)\mid\binom{2X}{X},
\]

then the single boundary \(X\) solves every \(m\le M\). This would explain repeated boundaries and would prove the original problem if such an \(X\) exists for every \(M\).

### Key lemma needed

Prove the stronger assertion

\[
\boxed{
\forall M\ge1\ \exists X>M:
\quad
\operatorname{lcm}_{0\le r\le M}\binom{2X}{r}
\mid \binom{2X}{X}.
}
\]

Prime-by-prime, this is

\[
v_p\binom{2X}{X}
\ge
\max_{0\le r\le M}v_p\binom{2X}{r}
\qquad\text{for every prime }p.
\]

By Kummer, it asks that the carry count in \(X+X\) dominate the carry counts in all additions

\[
r+(2X-r),\qquad 0\le r\le M.
\]

### Why it might work

- It directly uses the shared-boundary phenomenon.
- The denominator family is finite for fixed \(M\).
- There is substantial existing structure in lcm’s of binomial rows, including Farhi’s identity for the full row.
- A successful \(X\) for all \(m\le M\) avoids the circularity of constructing separate CRT moduli for each \(m\).
- The fixed-\(X\) recurrence
  \[
  R_{m+1}(X)=R_m(X)\frac{m+1}{2X-m}
  \]
  may permit an induction through adjacent \(m\).

### Most likely failure point

This is strictly stronger than the original problem and may be false. Moving prime factors of the finitely many binomial coefficients \(\binom{2X}{r}\) may require incompatible central carry patterns.

The full-row analogue cannot hold in general and is also too large numerically, so any proof must exploit that \(M\) is fixed while \(X\) is free.

### Quick blocking test

For \(M=1,2,\ldots,30\), search for the least \(X\) satisfying

\[
L_M(X)\mid\binom{2X}{X}.
\]

Use valuations rather than forming the lcm. Also test whether

\[
X=6,\ 210,\ 8178,\ 45153
\]

satisfy the universal condition up to the corresponding observed \(m\).

If the least \(X\) ceases to exist for a small \(M\), this strengthening should be abandoned, though the adjacent-\(m\) recurrence may remain useful.

---

## Route 2: Self-compensating endpoint factorizations

### Core mechanism

Construct the endpoint integers so that every large prime divisor automatically creates its own compensating positive level at the next prime power.

Let \(0\le j<H\), set

\[
N=X-j,
\]

and suppose \(p>m\) divides \(N\) exactly once. Write \(N=pu\). If

\[
u\equiv-1\pmod p,
\]

then

\[
X=N+j\equiv p^2-p+j\pmod{p^2}.
\]

Consequently,

\[
E_p=-1,
\]

while

\[
E_{p^2}=1
\]

provided

\[
p^2-2p+2j-m\ge0.
\]

This certainly holds for all sufficiently large \(p\), for example once \(p>m+2\).

Moreover, a later negative level \(E_{p^a}=-1\), \(a\ge2\), would force \(X\bmod p^a<H<p\), contradicting the already large residue modulo \(p^2\). Thus this one congruence can seal \(p\) completely.

### Key lemma needed

For every fixed \(m\), construct \(X>m\) and a threshold \(P\) such that:

1. every prime \(p\le P\) is sealed, for instance by \(p^{A_p}\mid X-m\);
2. for every endpoint \(N=X-j\), \(0\le j<H\), and every prime \(p>P\) dividing \(N\),
   \[
   v_p(N)=1
   \quad\text{and}\quad
   \frac Np\equiv-1\pmod p.
   \]

A more flexible version may allow a bounded chain of congruences pairing several negative levels with several higher positive levels.

### Why it might work

- It addresses the exact failure of CRT: no endpoint cofactor is left uncontrolled.
- It turns factorization into an explicit prime-power compensation certificate.
- For a squarefree integer \(N\), the congruences
  \[
  N/p\equiv-1\pmod p\qquad(p\mid N)
  \]
  are closely related to weak primary pseudoperfect or “minus-Giuga” congruences.
- Known Euclid-type recursions for such numbers may inspire a multiplicatively closed construction.
- It gives a clear target stronger than smoothness but much closer to the exact ledger.

### Most likely failure point

These self-referential factorization congruences are extremely rigid. Requiring them simultaneously for several consecutive integers may be impossible or may amount to a very difficult system of Egyptian-fraction or \(S\)-unit constraints.

Sealing small primes through \(X-m\) may also conflict with the required endpoint factorizations.

### Quick blocking test

For every known successful \((m,X)\):

1. factor all endpoint values \(X-j\);
2. for each prime \(p>m+2\), test
   \[
   v_p(X-j)=1,\qquad (X-j)/p\equiv-1\pmod p;
   \]
3. where this fails, determine whether the negative \(p\)-levels nevertheless admit a short higher-power matching.

Then search directly for \(X\) whose endpoint block satisfies the one-step condition, without initially testing the full ratio. If such \(X\) disappear already for small \(m\), broaden to bounded-depth compensation trees.

---

## Route 3: Lopsided local lemma and entropy-compression on exact bad events

### Core mechanism

For fixed \(m\) and a large dyadic interval \(X\in[T,2T]\), define

\[
\mathcal B_p=\{X:D_p(m,X)<0\}.
\]

Each \(\mathcal B_p\) is determined by residues modulo powers of \(p\), together with the archimedean restriction \(X\in[T,2T]\).

Round 1 showed that almost every \(X\) already avoids all \(\mathcal B_p\) for

\[
p\le \exp(\eta\sqrt{\log T}).
\]

The remaining bad events are attached to prime divisors of the short endpoint block. Instead of applying a union bound or a multidimensional Buchstab decomposition, attempt a lopsided Lovász local lemma, cluster expansion, or Moser–Tardos-type resampling argument on the exact valuation-deficit events.

The relevant negative dependence is that a prime \(p>m\) can divide at most one of the endpoints \(X-j\), because their pairwise differences are \(<m<p\).

### Key lemma needed

Prove an interval version of the local lemma of the following kind:

> After removing the negligible small-prime exceptional set, the hypergraph of exact bad events \(\mathcal B_p\) on \(X\in[T,2T]\) has a nonempty independent complement.

The lemma must preserve an actual integer representative in the interval; a merely profinite solution is not enough. It must also group the high-probability top-factor events more efficiently than an ordinary union bound.

A possible technical target is a convergent witness-tree or cluster expansion in which a bad event is weighted by its endpoint index, cofactor, and first uncompensated prime-power level.

### Why it might work

- Distinct primes are genuinely independent in the profinite residue model.
- Large primes interact with only one endpoint.
- Small primes are already controlled for almost every \(X\).
- The exact bad events are substantially more structured than arbitrary shifted-smoothness events.
- Entropy compression could avoid the “modulus grows faster than the representative” defect of sequential CRT by selecting from a large pool in parallel.

### Most likely failure point

Standard local-lemma criteria will almost certainly fail without grouping: the one-endpoint top obstruction has probability about \(\log2\), not a tiny probability, and the archimedean interval creates long-range dependence between moduli whose product exceeds \(T\).

If the only workable grouping reproduces a full multidimensional Buchstab decomposition, this route collapses back into the already blocked analytic route.

### Quick blocking test

For fixed small \(m\) and large finite \(T\):

1. enumerate \(X\in[T,2T]\) after pre-sieving small primes;
2. construct the bad-event incidence hypergraph;
3. test asymmetric LLL, cluster-expansion, and resampling criteria numerically;
4. measure witness-tree growth when events are grouped by endpoint and cofactor size.

If every reasonable criterion fails by a factor growing rapidly with \(H\), this route is unlikely to close without a major new dependence theorem.

---

## Route 4: Disproof through a scale-invariant covering of carry deficits

### Core mechanism

Search for an \(m_0\) such that the bad sets

\[
\mathcal B_p(m_0)=\{X>m_0:D_p(m_0,X)<0\}
\]

cover every integer \(X>m_0\).

A finite set of fixed primes cannot suffice, because those primes can be simultaneously sealed. Therefore any disproof must use moving primes, most naturally prime divisors of

\[
X,\ X-1,\ldots,X-H+1.
\]

The intended certificate should combine:

1. finite-state base-\(p\) carry rules for small primes;
2. a largest-prime-factor or largest-prime-power rule for the endpoint block;
3. an induction reducing an uncovered \(X\) to a smaller endpoint cofactor.

### Key lemma needed

Find a specific \(m_0\) and prove a scale-invariant covering theorem such as:

> For every \(X>m_0\), either a fixed small-prime carry automaton gives \(D_p<0\), or one endpoint \(X-j\) has a prime-power divisor \(p^t\) whose size and exponent force \(D_p<0\); if neither occurs, the endpoint cofactors map to a strictly smaller integer satisfying the same alternatives.

The descent must terminate and must use the exact \(D_p\), not merely smoothness.

### Why it might work

- As \(m\) grows, many endpoint integers must simultaneously satisfy restrictive smoothness and digit-balance conditions.
- A counterexample could arise from incompatibility among several prime chains even though each chain is locally repairable.
- Carry deficits are finite-state at each fixed prime and may admit automatic covering certificates.
- The exact endpoint localization sharply restricts where moving witness primes can come from.

### Most likely failure point

The heuristic evidence points toward successful \(X\) having positive, though possibly extremely small, density for each fixed \(m\). The verified data through \(n=18\) also give no candidate counterexample.

Any covering based only on top prime factors will fail because some endpoint blocks are simultaneously smooth. Any covering using only fixed primes will fail by the sealing lemma.

### Quick blocking test

For moderate \(m\):

1. search \(X\) to a very large bound using the exact valuation checker;
2. for failed \(X\), classify the least witness prime as:
   - fixed small prime,
   - top endpoint factor,
   - repeated endpoint prime,
   - higher-digit imbalance;
3. use SAT or automata minimization to seek a recursive covering rule;
4. test whether uncovered residue/factorization states persist and generate successful \(X\).

A found successful \(X\) eliminates that \(m\) as a counterexample. Long finite failure ranges are only exploratory evidence and have no disproof value by themselves.

---

## 9. VERDICT ON DIFFICULTY

This is a genuinely difficult open problem. The zero prize should not be interpreted as evidence of accessibility.

There is no known equivalence to the Riemann hypothesis, \(abc\), Schinzel’s hypothesis, or another single famous conjecture. However, the most direct analytic formulation reaches a hard simultaneous shifted-friable correlation problem with extra \(p\)-adic digit constraints. Natural balanced-semiprime or prime-value constructions run into parity and prime-tuples barriers.

Round 1 rules out the most tempting approaches:

- coefficientwise Gaussian positivity is impossible;
- fixed-prime CRT is inherently circular;
- every fixed CRT progression contains fresh failures;
- composite runs and prime gaps do not control endpoint cofactors;
- simultaneous square-root smoothness is still insufficient.

A successful proof will likely require one of two genuinely new ingredients:

1. a multiplicative construction that closes every endpoint factorization under explicit prime-power compensation; or
2. a new global theorem showing that exact valuation-deficit events cannot cover all integers in a large interval.

A disproof would be equally substantial: it would require a scale-invariant mechanism forcing some prime deficit for every possible boundary \(X\) at one fixed \(m\).