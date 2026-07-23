# Problem Brief: Erdős Problem #893

## 1. PRECISE STATEMENT

For each positive integer \(m\), let

\[
\tau(m)=\#\{d\in \mathbb Z_{>0}:d\mid m\}
\]

be the number of positive divisors of \(m\). In particular, \(\tau(1)=1\).

For \(k\ge 1\), write

\[
M_k=2^k-1
\]

and define

\[
b_k=\tau(M_k),\qquad
f(n)=\sum_{k=1}^{n}b_k
=\sum_{k=1}^{n}\tau(2^k-1)
\]

for \(n\in\mathbb Z_{>0}\). The object of study is

\[
R(n)=\frac{f(2n)}{f(n)}.
\]

The original question asks whether \(R(n)\) tends to a limit as \(n\to\infty\) through positive integers.

### Ambiguity about “a limit”

There are two standard readings.

1. **Finite-limit reading:** Does there exist \(L\in\mathbb R\) such that
   \[
   \forall \varepsilon>0\ \exists N\ \forall n\ge N:
   \left|R(n)-L\right|<\varepsilon?
   \]

2. **Extended-limit reading:** Does \(R(n)\) converge in \(\mathbb R\cup\{+\infty\}\)? Since all terms are positive, the only additional plausible limit is \(+\infty\), meaning
   \[
   \forall A>0\ \exists N\ \forall n\ge N:
   R(n)>A.
   \]

Kovač and Luca have proved

\[
\limsup_{n\to\infty}R(n)=+\infty.
\]

Consequently, the finite-limit reading is already settled negatively. The database’s continued `OPEN` status, together with its commentary, shows that the intended surviving problem is:

> **Surviving open problem.** Prove or disprove
> \[
> \boxed{\lim_{n\to\infty}\frac{f(2n)}{f(n)}=+\infty.}
> \]

Equivalently, determine whether

\[
\liminf_{n\to\infty}R(n)=+\infty.
\]

---

## 2. WHAT COUNTS AS A SOLUTION

### A complete affirmative solution

A complete proof must establish the uniform statement

\[
\forall A>0\ \exists N(A)\ \forall n\ge N(A):
\quad f(2n)>A f(n).
\]

It is not enough to produce arbitrarily large values of \(R(n)\), since that is already known. The estimate must hold for **every sufficiently large integer \(n\)**.

An equivalent target is

\[
f(2n)-2f(n)\gg_{A} f(n)
\]

with a factor tending to infinity, or any other rigorously proved estimate implying \(R(n)\to\infty\).

### A complete negative solution

Because \(\limsup R(n)=\infty\) is known, disproving convergence to \(+\infty\) amounts to proving that \(R(n)\) is bounded along an infinite subsequence. Precisely, it is enough to establish

\[
\exists C<\infty\ \forall N\ \exists n\ge N:
\quad f(2n)\le C f(n).
\]

Equivalently,

\[
\liminf_{n\to\infty}R(n)<\infty.
\]

A constructive disproof could provide an explicit increasing sequence \(n_j\to\infty\) and a fixed constant \(C\) such that

\[
f(2n_j)\le C f(n_j)
\qquad\text{for every }j.
\]

The inequalities must be proved uniformly in \(j\). A finite list of numerical examples is not a counterexample to an asymptotic assertion.

### Verification requirements for an explicit construction

If a proposed disproof relies on exact values of \(f(2n_j)\), then exact divisor counts for all \(2^k-1\), \(k\le 2n_j\), must be certified. A partial factorization generally supplies only a lower bound for \(\tau(2^k-1)\), not the upper bound needed to prove \(f(2n_j)\le C f(n_j)\). Any unfactored cofactors must therefore be certified prime or otherwise controlled rigorously.

---

## 3. WHAT DOES NOT COUNT

None of the following resolves the surviving problem:

- Reproving
  \[
  \limsup_{n\to\infty}R(n)=\infty.
  \]
- Showing \(R(n)\to\infty\) only along a subsequence, including \(n=2^j\), primorials, highly composite numbers, or a density-one set.
- Showing \(R(n)>A\) for infinitely many \(n\), for each fixed \(A\).
- Establishing a lower bound such as \(R(n)\ge 2\), \(R(n)\gg 1\), or even \(R(n)\gg \log\log n\) on a restricted set of \(n\).
- Proving large lower bounds for individual terms \(\tau(2^k-1)\) without controlling the denominator \(f(n)\) and the entire interval \(n<k\le 2n\).
- Improving upper or lower bounds for \(f(n)\) that do not compare \(f(2n)\) uniformly with \(f(n)\).
- Conditional arguments based on Artin-type conjectures, generalized Riemann hypotheses, conjectural factorization statistics, random-integer heuristics, or unproved independence assumptions.
- Numerical evidence over any fixed range.
- Heuristics that typical cyclotomic or Mersenne values have many prime factors.
- Proving a “smoothed” or averaged statement such as
  \[
  \frac1X\sum_{n\le X}R(n)\to\infty
  \]
  without a mechanism upgrading it to all sufficiently large \(n\).

Under the strictly finite-real interpretation of “limit,” the problem is already answered: no finite limit exists. That observation alone does not solve the intended open form.

---

## 4. KNOWN RESULTS AND CONTEXT

### 4.1 The result of Kovač and Luca

Kovač and Luca, building on a heuristic independently found by Cambie, proved

\[
\boxed{\limsup_{n\to\infty}\frac{f(2n)}{f(n)}=\infty.}
\]

Thus:

- \(R(n)\) is unbounded;
- no finite real limit can exist;
- the only possible extended limit is \(+\infty\).

They also gave theoretical and numerical evidence suggesting

\[
R(n)\to\infty.
\]

That final uniform assertion remains open.

Erdős reportedly remarked that there was probably no simple asymptotic formula for \(f(n)\), because \(f(n)\) “increases too fast.” This is contextual motivation, not a theorem resolving the ratio question.

---

### 4.2 Divisibility-sequence structure

The Mersenne numbers satisfy

\[
\gcd(M_m,M_n)=M_{\gcd(m,n)}.
\]

In particular,

\[
d\mid k\quad\Longrightarrow\quad M_d\mid M_k,
\]

and hence

\[
\tau(M_d)\le \tau(M_k).
\]

Also,

\[
M_{2k}=(2^k-1)(2^k+1),
\]

and

\[
\gcd(2^k-1,2^k+1)=1.
\]

Therefore

\[
\boxed{\tau(M_{2k})
=\tau(M_k)\tau(2^k+1).}
\]

Since \(\tau(2^k+1)\ge 2\),

\[
\tau(M_{2k})\ge 2\tau(M_k).
\]

Summing over \(k\le n\) and retaining only the even-indexed terms in \(f(2n)\) gives the useful universal bound

\[
\boxed{f(2n)\ge 2f(n),\qquad R(n)\ge 2.}
\]

This lower bound is far from the conjectured \(R(n)\to\infty\).

---

### 4.3 Exact multiplicative-order decomposition

For an odd positive integer \(d\), let \(\operatorname{ord}_d(2)\) denote the multiplicative order of \(2\bmod d\), with the convention

\[
\operatorname{ord}_1(2)=1.
\]

Define

\[
a(r)=\#\{d\in\mathbb Z_{>0}:d\text{ odd and }\operatorname{ord}_d(2)=r\}.
\]

This is finite because \(\operatorname{ord}_d(2)=r\) implies \(d\mid 2^r-1\).

A divisor \(d\) of \(2^k-1\) is characterized by

\[
\operatorname{ord}_d(2)\mid k.
\]

Consequently,

\[
\boxed{\tau(2^k-1)=\sum_{r\mid k}a(r).}
\]

By Möbius inversion,

\[
\boxed{a(r)=\sum_{d\mid r}\mu(r/d)\tau(2^d-1).}
\]

Summing over \(k\le N\) yields the exact formula

\[
\boxed{
f(N)=\sum_{r\le N}a(r)\left\lfloor\frac Nr\right\rfloor.
}
\]

This recasts the problem as one about the distribution of the nonnegative “exact-order mass” \(a(r)\).

In particular,

\[
\begin{aligned}
f(2n)-2f(n)
&=\sum_{r\le 2n}a(r)
\left(
\left\lfloor\frac{2n}{r}\right\rfloor
-2\left\lfloor\frac nr\right\rfloor
\right).
\end{aligned}
\]

Every coefficient in this sum is either \(0\) or \(1\). For \(n<r\le 2n\), it is exactly \(1\). Hence

\[
\boxed{
f(2n)-2f(n)\ge \sum_{n<r\le 2n}a(r).
}
\]

Thus the sufficient condition

\[
\sum_{n<r\le 2n}a(r)\gg \omega(n) f(n),
\qquad \omega(n)\to\infty,
\]

would prove the conjecture. It is not currently known.

---

### 4.4 Bang–Zsigmondy and an elementary lower bound

The Bang–Zsigmondy theorem implies that for every integer \(r>1\), except \(r=6\), the number \(2^r-1\) has a prime divisor that divides no earlier \(2^j-1\), \(1\le j<r\).

Applying this to each divisor \(r\mid k\), with \(r>1\) and \(r\ne6\), gives distinct prime divisors of \(M_k\). Therefore

\[
\omega(M_k)\ge \tau(k)-1-\mathbf 1_{6\mid k},
\]

where \(\omega(m)\) is the number of distinct prime factors of \(m\). Hence

\[
\boxed{
\tau(M_k)\ge
2^{\,\tau(k)-1-\mathbf 1_{6\mid k}}.
}
\]

This gives very large individual terms at divisor-rich exponents \(k\). It does not by itself compare a new spike with the accumulated sum \(f(n)\).

A related bound applies to \(2^k+1\). Write \(k=2^\alpha u\) with \(u\) odd. Primitive divisors associated with the indices \(2^{\alpha+1}e\), \(e\mid u\), give, up to the \(r=6\) exception,

\[
\tau(2^k+1)\ge
2^{\,\tau(u)-\mathbf 1_{\alpha=0,\ 3\mid u}}.
\]

This may be useful in conjunction with the exact identity for \(\tau(M_{2k})\).

---

### 4.5 General divisor-function upper bounds

Wigert’s maximal-order theorem for the divisor function gives

\[
\log \tau(m)
\le (\log 2+o(1))\frac{\log m}{\log\log m}.
\]

Applied to \(m=2^k-1\),

\[
\log \tau(2^k-1)
\le
\left((\log 2)^2+o(1)\right)\frac{k}{\log k}.
\]

Thus

\[
f(n)\le
n\exp\left(
\left((\log 2)^2+o(1)\right)\frac{n}{\log n}
\right).
\]

This generic upper bound is much too large to be defeated by the elementary Zsigmondy lower bound at a single divisor-rich exponent. Any successful spike argument needs substantially more structure than these two estimates alone.

---

## 5. TRAPS AND EDGE CASES

1. **The first Mersenne number is \(1\).**  
   \(2^1-1=1\) and \(\tau(1)=1\). There is no primitive prime divisor at exponent \(1\).

2. **Zsigmondy has an exception at exponent \(6\).**  
   \(2^6-1=63=3^2\cdot7\), and both primes already occur at earlier exponents. Any count of one new prime per divisor of \(k\) must remove \(r=6\).

3. **Cyclotomic factors need not be coprime.**  
   Although
   \[
   2^k-1=\prod_{d\mid k}\Phi_d(2),
   \]
   the integers \(\Phi_d(2)\) are not pairwise coprime. For example,
   \[
   \Phi_2(2)=3,\qquad \Phi_6(2)=3.
   \]
   Therefore one cannot multiply their divisor counts.

4. **The inequality for \(\tau(ab)\) goes in the dangerous direction.**  
   In general,
   \[
   \tau(ab)\le \tau(a)\tau(b),
   \]
   with equality when \(\gcd(a,b)=1\). A factorization into non-coprime pieces does not automatically yield a product lower bound.

5. **Large individual terms do not automatically dominate \(f(n)\).**  
   The denominator contains all earlier spikes. One must compare the whole new block
   \[
   \sum_{n<k\le2n}\tau(M_k)
   \]
   with the cumulative past.

6. **The assertion must hold for every large integer \(n\).**  
   Results only at dyadic \(n\), primorial \(n\), or highly composite \(n\) are insufficient.

7. **Unbounded limsup is not convergence to infinity.**  
   A sequence can have arbitrarily large spikes while repeatedly returning to bounded values.

8. **Generic nonnegative-coefficient arguments are insufficient.**  
   A function of the form
   \[
   F(N)=\sum_{r\le N}c_r\left\lfloor\frac Nr\right\rfloor,
   \qquad c_r\ge0,
   \]
   may have unbounded dyadic limsup but bounded dyadic liminf if the \(c_r\) are sufficiently lacunary. The arithmetic structure of \(a(r)\), not merely its nonnegativity, must be used.

9. **Incomplete factorizations can be misleading.**  
   An unresolved cofactor may be prime or may contain many small factors. Exact divisor counts require a complete certified factorization or rigorous bounds on every cofactor.

10. **Primitive prime divisors provide only one prime per order.**  
    Size of \(\Phi_r(2)\) does not force it to have many distinct prime factors; it could conceivably be prime or almost prime.

11. **Numerical ratios can oscillate sharply.**  
    Exceptional values such as \(\tau(2^{12}-1)=48\) create immediate jumps. Local monotonicity of \(R(n)\) should not be assumed.

---

## 6. VERIFICATION HOOKS

### 6.1 Direct exact computation

For a chosen cutoff \(N\):

1. Completely factor \(2^k-1\) for every \(1\le k\le 2N\).
2. If
   \[
   2^k-1=\prod_i p_i^{e_i},
   \]
   compute
   \[
   b_k=\prod_i(e_i+1).
   \]
3. Form cumulative sums
   \[
   f(n)=\sum_{k\le n}b_k
   \]
   and ratios \(R(n)=f(2n)/f(n)\).

Cyclotomic factorization

\[
2^k-1=\prod_{d\mid k}\Phi_d(2)
\]

can reduce repeated work, but shared primes among cyclotomic values must be merged before computing exponents.

### 6.2 Small values for cross-checking

The first values are:

\[
\begin{array}{c|c|c|c}
k & 2^k-1 & \tau(2^k-1) & f(k)\\ \hline
1&1&1&1\\
2&3&2&3\\
3&7&2&5\\
4&15&4&9\\
5&31&2&11\\
6&63&6&17\\
7&127&2&19\\
8&255&8&27\\
9&511&4&31\\
10&1023&8&39\\
11&2047&4&43\\
12&4095&48&91
\end{array}
\]

For example,

\[
R(1)=3,\quad R(2)=3,\quad R(3)=\frac{17}{5},
\quad R(4)=3,\quad R(6)=\frac{91}{17}.
\]

### 6.3 Exact-order consistency check

From computed \(b_k\), define recursively

\[
a(k)=b_k-\sum_{\substack{d\mid k\\d<k}}a(d).
\]

The result must always be a nonnegative integer. For \(1\le k\le12\),

\[
(a(1),\ldots,a(12))
=
(1,1,1,2,1,3,1,4,2,5,3,40).
\]

Then verify independently that

\[
b_k=\sum_{d\mid k}a(d)
\]

and

\[
f(N)=\sum_{r\le N}a(r)\left\lfloor\frac Nr\right\rfloor.
\]

### 6.4 Dyadic defect

Compute

\[
E(n)=f(2n)-2f(n).
\]

Cross-check it using

\[
E(n)=
\sum_{r\le2n}a(r)
\left(
\left\lfloor\frac{2n}{r}\right\rfloor
-2\left\lfloor\frac nr\right\rfloor
\right).
\]

Record separately:

\[
S(n)=\sum_{n<r\le2n}a(r)
\]

and the old-order contribution from \(r\le n\). Determine whether \(S(n)\) or the old-order contribution is responsible for large \(R(n)\).

### 6.5 Test the doubling-factor lower bound

Let

\[
c_k=\tau(2^k+1)
\]

and compute

\[
L(n)=
\frac{\sum_{k\le n}b_kc_k}{\sum_{k\le n}b_k}.
\]

Since

\[
f(2n)\ge \sum_{k\le n}b_{2k}
=\sum_{k\le n}b_kc_k,
\]

one has \(R(n)\ge L(n)\). Numerically test:

- whether \(L(n)\) appears to grow;
- whether the \(b_k\)-weight concentrates on indices with small \(c_k\);
- the proportions
  \[
  \frac{\sum_{k\le n,\ c_k\le T}b_k}{f(n)}
  \]
  for fixed thresholds \(T\).

### 6.6 Search for a disproof pattern

For each \(n\), record:

\[
R(n),\qquad
D(n)=\frac{\max_{k\le n}b_k}{f(n)},\qquad
B(n)=\frac{\sum_{n<k\le2n}b_k}{f(n)}.
\]

Inspect local minima of \(R(n)\). A plausible disproof mechanism would require large denominator concentration \(D(n)\) followed by a relatively tame next dyadic block.

---

## 7. ATTACK ROUTES

### Route 1: Weighted doubling-factor amplification

Use

\[
b_{2k}=b_k\tau(2^k+1)
\]

to obtain

\[
R(n)\ge
\frac{\sum_{k\le n}b_k\tau(2^k+1)}{\sum_{k\le n}b_k}.
\]

#### Key lemma needed

Prove that the \(b_k\)-weighted average of \(\tau(2^k+1)\) diverges:

\[
\frac{\sum_{k\le n}\tau(2^k-1)\tau(2^k+1)}
{\sum_{k\le n}\tau(2^k-1)}
\longrightarrow\infty.
\]

A sufficient formulation is that for every fixed \(T\),

\[
\sum_{\substack{k\le n\\ \tau(2^k+1)\le T}}b_k=o(f(n)).
\]

#### Why it might work

The factor \(2^k+1\) acquires distinct primitive prime divisors from many divisors of the odd part of \(k\). Indices with divisor-rich odd part force \(\tau(2^k+1)\) to be large. Large \(b_k\) may also preferentially occur at divisor-rich exponents, creating useful positive correlation.

#### Most likely failure point

The weight \(b_k\) could concentrate on exponents whose odd parts have few divisors, such as numbers close to powers of \(2\). Current methods provide poor upper bounds for that exceptional weighted set.

#### Quick obstruction test

Compute \(L(n)\) and the weighted exceptional proportions for fixed \(T\). If most of the \(b_k\)-mass repeatedly lies on small-\(\tau(2^k+1)\) indices, this route is blocked without a new correlation theorem.

---

### Route 2: Exact-order mass in every dyadic shell

Use

\[
f(N)=\sum_{r\le N}a(r)\left\lfloor\frac Nr\right\rfloor
\]

and

\[
f(2n)-2f(n)\ge \sum_{n<r\le2n}a(r).
\]

#### Key lemma needed

Prove a uniform shell-dominance result such as

\[
\sum_{n<r\le2n}a(r)\ge \omega(n)f(n),
\qquad \omega(n)\to\infty.
\]

A weaker lemma controlling the full exact defect

\[
\sum_{r\le2n}a(r)
\left(
\left\lfloor\frac{2n}{r}\right\rfloor
-2\left\lfloor\frac nr\right\rfloor
\right)
\]

would also suffice.

#### Why it might work

The coefficient \(a(r)\) counts all divisors whose exact order is \(r\), not merely primitive primes. Products of prime powers with orders having least common multiple \(r\) can cause a combinatorial explosion in \(a(r)\). The interval \((n,2n]\) introduces entirely new exact orders.

#### Most likely failure point

The exact-order mass may be highly irregular and concentrated at sparse exponents. Primitive-divisor theorems guarantee at least one new prime for most \(r\), but not enough new divisors to dominate the whole past.

#### Quick obstruction test

Calculate \(S(n)=\sum_{n<r\le2n}a(r)\) and compare \(S(n)/f(n)\) at local minima of \(R(n)\). If \(S(n)\) remains small while the old-order floor contribution creates the known spikes, shell dominance is unlikely to be the correct statement.

---

### Route 3: Uniform divisor-rich exponents in \((n,2n]\)

Exploit Bang–Zsigmondy:

\[
b_k\ge 2^{\tau(k)-1-\mathbf 1_{6\mid k}}.
\]

Try to find, for every \(n\), one or many exponents \(k\in(n,2n]\) with exceptionally large \(\tau(k)\).

#### Key lemma needed

A result of the form

\[
\sum_{n<k\le2n}2^{\tau(k)}
\ge \omega(n) f(n),
\qquad \omega(n)\to\infty,
\]

or a stronger structural upper bound on \(f(n)\) that makes one carefully chosen new exponent dominate.

#### Why it might work

Every dyadic interval contains integers with many divisors, and each divisor of \(k\) typically contributes a new primitive prime to \(M_k\). This converts divisor richness of the exponent into exponentially many divisors of the Mersenne number.

#### Most likely failure point

The generic upper bound on \(f(n)\) is vastly larger than the Zsigmondy lower bound attainable from known estimates for \(\tau(k)\). Moreover, there may be an earlier Mersenne spike in \(f(n)\) larger than all available lower bounds in the next block.

#### Quick obstruction test

For computationally feasible \(n\), compare

\[
\max_{n<k\le2n}
2^{\tau(k)-1-\mathbf1_{6\mid k}}
\]

and its block sum with exact \(f(n)\). Also compare the logarithmic scales of the best rigorous lower bound and Wigert’s upper bound; the present generic estimates show a major gap.

---

### Route 4: Analytic counting of multiplicative orders

Start from

\[
f(N)=
\sum_{\substack{d\text{ odd}\\ \operatorname{ord}_d(2)\le N}}
\left\lfloor\frac{N}{\operatorname{ord}_d(2)}\right\rfloor.
\]

Study the distribution of \(\operatorname{ord}_d(2)\) over composite moduli \(d\), especially moduli built as products of primes dividing cyclotomic values.

#### Key lemma needed

Show that in every dyadic order range \((n,2n]\), there are sufficiently many moduli \(d\) with exact order in that range to dominate all moduli of smaller order counted with multiplicity.

A possible target is an aggregate lower bound for

\[
\#\{d:\ n<\operatorname{ord}_d(2)\le2n\}.
\]

#### Why it might work

If primes \(p_i\) have orders \(r_i\), then for suitable squarefree products,

\[
\operatorname{ord}_{\prod p_i}(2)=\operatorname{lcm}(r_i).
\]

A moderate collection of primes can therefore generate exponentially many divisors with the same or nearby exact order.

#### Most likely failure point

Unconditional control of multiplicative orders of \(2\) is difficult and often Artin-like. Primitive-divisor results provide existence but not enough primes, and the least common multiples may overshoot the desired dyadic interval.

#### Quick obstruction test

Factor \(\Phi_r(2)\) for moderate \(r\), record the orders of all prime powers, and determine how much of \(a(r)\) comes from combinatorial products versus a few isolated factors. If most \(a(r)\) remain near the minimum allowed by Zsigmondy, this route lacks sufficient multiplicity.

---

### Route 5: Upgrade the known limsup theorem by anti-lacunarity

Analyze the mechanism in the Kovač–Luca proof that creates large values of \(R(n)\), and attempt to show that these forcing events cannot be separated by long multiplicative gaps.

#### Key lemma needed

An arithmetic persistence or anti-lacunarity statement, for example:

- large exact-order mass at one scale forces large dyadic ratios over a whole subsequent interval; or
- the scales at which the Kovač–Luca construction works have multiplicative gap \(1+o(1)\); or
- the coefficient sequence \(a(r)\) cannot have the sparse-spike behavior possible for arbitrary nonnegative sequences.

#### Why it might work

The limsup theorem already identifies a mechanism producing arbitrarily large amplification. The remaining issue is uniformity. Divisibility relations among Mersenne numbers may spread a large event to many multiples and neighboring scales.

#### Most likely failure point

For a general nonnegative exact-order transform, isolated spikes can be extremely narrow. Mersenne divisor spikes may likewise be too localized, and ratios \(R(n)\) have no evident monotonicity.

#### Quick obstruction test

Reproduce the large-ratio examples from the known proof and compute \(R(m)\) throughout broad windows around each forcing scale. If high values collapse immediately outside a sparse set, a persistence lemma is unlikely without an additional arithmetic mechanism.

---

### Route 6: Disproof via record spikes followed by quiet blocks

Seek an infinite sequence \(n_j\) for which \(f(n_j)\) is dominated by one or a few exceptional earlier terms, while the next block contributes only a bounded multiple of that accumulated mass:

\[
\sum_{n_j<k\le2n_j}b_k=O(f(n_j)).
\]

Then \(R(n_j)=O(1)\).

#### Key lemma needed

Construct \(n_j\to\infty\) and \(C<\infty\) such that

\[
\sum_{n_j<k\le2n_j}\tau(2^k-1)
\le (C-1)f(n_j).
\]

A plausible stronger scenario would be:

\[
f(n_j)\asymp \tau(2^{m_j}-1)
\]

for some record exponent \(m_j\le n_j\), followed by a dyadic interval containing no comparable Mersenne divisor spike.

#### Why it might work

The factorization of \(2^k-1\) is highly irregular, and exceptional values can dominate short cumulative sums. Unbounded limsup does not rule out repeated returns to a bounded ratio.

#### Most likely failure point

The available tools are far better at producing lower bounds than upper bounds for \(\tau(2^k-1)\). Proving an entire dyadic block is quiet would require strong uniform upper control over many cyclotomic values. Moreover, the current heuristic evidence points in the opposite direction, namely \(R(n)\to\infty\).

#### Quick obstruction test

Search for local minima of \(R(n)\) immediately after record values of \(b_k\). Measure whether

\[
\max_{k\le n}b_k/f(n)
\]

is large and whether the subsequent dyadic block remains small. Persistent downward minima would support this route; steadily rising minima would count against it.

---

## 8. VERDICT ON DIFFICULTY

The finite-limit version is no longer open: Kovač and Luca’s theorem rules out every finite limit.

The surviving assertion

\[
\frac{f(2n)}{f(n)}\to\infty
\]

appears genuinely difficult. It asks for uniform control over every dyadic interval in a sequence governed by the unpredictable factorizations of Mersenne and cyclotomic values. Existing elementary tools readily create large individual terms and large subsequential ratios, but do not prevent long quiet intervals or domination by old spikes.

No equivalence with a famous named conjecture is currently known. However, some natural analytic approaches run directly into difficult questions about multiplicative orders of \(2\), primitive prime divisors, and prime factors of cyclotomic values—territory adjacent to Artin-type problems. A proof should not be expected from generic divisor estimates alone.

The central conceptual obstacle is:

> Convert known mechanisms producing arbitrarily large new divisor mass into a statement that such mass dominates the accumulated past in **every** sufficiently large dyadic interval.

Conversely, a disproof would require the equally difficult task of proving infinitely many entire dyadic blocks are uniformly quiet. Both directions demand arithmetic structure substantially beyond the known limsup result.