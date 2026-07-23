# Problem brief: Erdős Problem #291

## 1. Precise statement

For each integer \(n\ge 1\), define

\[
L_n:=\operatorname{lcm}(1,2,\dots,n)
\]

and the \(n\)-th harmonic number

\[
H_n:=\sum_{k=1}^n \frac1k.
\]

Since every \(k\le n\) divides \(L_n\),

\[
a_n:=L_nH_n=\sum_{k=1}^n \frac{L_n}{k}
\]

is an integer. Thus \(a_n\) is uniquely determined by

\[
H_n=\frac{a_n}{L_n}.
\]

Importantly, \(a_n/L_n\) is not assumed to be reduced.

Define

\[
g_n:=\gcd(a_n,L_n).
\]

The problem asks whether both sets

\[
\mathcal C:=\{n\ge 1:g_n=1\}
\]

and

\[
\mathcal D:=\{n\ge 1:g_n>1\}
\]

are infinite. Formally, the desired affirmative statement is

\[
(\forall N\ge1)(\exists n>N)\;g_n=1
\]

and

\[
(\forall N\ge1)(\exists n>N)\;g_n>1.
\]

The second assertion is already known unconditionally. Therefore the unresolved content is:

> Are there infinitely many \(n\) for which \(a_n\) and \(L_n\) are coprime?

### Equivalent denominator formulation

Write \(H_n=A_n/B_n\) in lowest terms, with \(B_n>0\) and \(\gcd(A_n,B_n)=1\). Since \(B_n\mid L_n\),

\[
a_n=\frac{L_n}{B_n}A_n,
\]

and hence

\[
\gcd(a_n,L_n)=\frac{L_n}{B_n}.
\]

Consequently,

\[
g_n=1\quad\Longleftrightarrow\quad B_n=L_n.
\]

Thus the open problem is equivalently whether the reduced denominator of \(H_n\) equals \(\operatorname{lcm}(1,\dots,n)\) for infinitely many \(n\).

There is little genuine ambiguity in the database statement, but one must not reinterpret \(a_n\) as the reduced numerator of \(H_n\).

---

## 2. Exact local criterion

For a prime \(p\le n\), let

\[
e_p(n):=\max\{e\ge 0:p^e\le n\}=\lfloor \log_p n\rfloor.
\]

Thus

\[
p^{e_p(n)}\le n<p^{e_p(n)+1}.
\]

Define the leading base-\(p\) digit of \(n\) by

\[
d_p(n):=\left\lfloor \frac{n}{p^{e_p(n)}}\right\rfloor\in\{1,\dots,p-1\}.
\]

For \(1\le d\le p-1\), write

\[
H_d=\sum_{j=1}^d\frac1j=\frac{U_d}{V_d}
\]

in lowest terms. Since \(d<p\), one has \(p\nmid V_d\), so the assertion \(p\mid U_d\) is equivalent to

\[
\sum_{j=1}^d j^{-1}\equiv 0\pmod p.
\]

Define

\[
S_p:=\left\{d\in\{1,\dots,p-1\}:
\sum_{j=1}^d j^{-1}\equiv0\pmod p\right\}.
\]

Here \(j^{-1}\) denotes the inverse of \(j\) modulo \(p\).

### Proposition: exact prime-divisor criterion

For every prime \(p\le n\),

\[
p\mid g_n
\quad\Longleftrightarrow\quad
d_p(n)\in S_p.
\]

Equivalently,

\[
p\mid \gcd(a_n,L_n)
\quad\Longleftrightarrow\quad
p\mid U_{d_p(n)}.
\]

#### Proof

Let \(e=e_p(n)\), \(d=d_p(n)\), and write

\[
L_n=p^eM,\qquad p\nmid M.
\]

In

\[
a_n=\sum_{j=1}^n\frac{L_n}{j},
\]

every term with \(v_p(j)<e\) is divisible by \(p\). The terms not automatically divisible by \(p\) are exactly those with

\[
j=rp^e,\qquad 1\le r\le d.
\]

Modulo \(p\),

\[
\frac{L_n}{rp^e}\equiv Mr^{-1}\pmod p.
\]

Therefore

\[
a_n\equiv M\sum_{r=1}^d r^{-1}\pmod p.
\]

Since \(M\not\equiv0\pmod p\), this vanishes exactly when \(d\in S_p\). Since \(p\le n\), one also has \(p\mid L_n\), proving the criterion.

### Interval form

The condition \(d_p(n)=d\) is equivalent to the existence of an integer \(e\ge1\) such that

\[
dp^e\le n<(d+1)p^e.
\]

Thus the set of \(n\) detected by \(p\) is

\[
\mathcal B_p
=
\bigcup_{e\ge1}\;\bigcup_{d\in S_p}
\left([dp^e,(d+1)p^e)\cap\mathbb Z\right).
\]

The open problem is therefore equivalent to asking whether infinitely many positive integers avoid every \(\mathcal B_p\):

\[
\#\left(\mathbb N\setminus\bigcup_p\mathcal B_p\right)=\infty.
\]

### Immediate observations

- \(S_2=\varnothing\), because the only possible digit is \(1\), and \(H_1=1\not\equiv0\pmod2\).
- \(1\notin S_p\) for every prime \(p\). Hence any prime witnessing \(p\mid g_n\) satisfies \(p\le n/2\).
- For odd \(p\),

  \[
  p-1\in S_p,
  \]

  since

  \[
  \sum_{j=1}^{p-1}j^{-1}\equiv\sum_{j=1}^{p-1}j\equiv0\pmod p.
  \]

  For \(p\ge5\), Wolstenholme’s theorem gives the stronger congruence
  \(H_{p-1}\equiv0\pmod{p^2}\). The case \(p=3\) is immediate from
  \(H_2=3/2\). The statement fails for \(p=2\).
- There is a symmetry

  \[
  d\in S_p\quad\Longleftrightarrow\quad p-1-d\in S_p
  \]

  for \(1\le d\le p-2\). Indeed, modulo \(p\),

  \[
  H_{p-1-d}
  =H_{p-1}-\sum_{r=1}^d\frac1{p-r}
  \equiv H_d.
  \]

- A useful equivalent binomial congruence is

  \[
  d\in S_p
  \quad\Longleftrightarrow\quad
  \binom{p-1}{d}\equiv(-1)^d\pmod{p^2}.
  \]

  This follows from

  \[
  \binom{p-1}{d}
  =(-1)^d\prod_{j=1}^d\left(1-\frac pj\right)
  \equiv(-1)^d(1-pH_d)\pmod{p^2}.
  \]

---

## 3. What counts as a solution

### Complete affirmative solution

A complete affirmative solution must prove unconditionally that:

1. For every \(N\), there exists \(n>N\) such that

   \[
   \gcd(a_n,L_n)=1.
   \]

   Equivalently, it must produce infinitely many \(n\) satisfying

   \[
   d_p(n)\notin S_p
   \qquad\text{for every prime }p\le n.
   \]

2. It must also establish infinitely many \(n\) with \(g_n>1\), although this part may simply cite or reproduce the existing elementary construction.

For example, for every \(e\ge1\) and every integer

\[
2\cdot3^e\le n<3^{e+1},
\]

the leading base-\(3\) digit is \(2\), and

\[
H_2=\frac32\equiv0\pmod3.
\]

Hence

\[
3\mid g_n.
\]

In particular, \(n=2\cdot3^e\) gives an explicit infinite sequence in \(\mathcal D\).

Any unconditional lower bound

\[
\#\{n\le x:g_n=1\}\to\infty
\]

would suffice. An asymptotic formula is not required.

### Complete negative solution

Logically, a negative answer to “do both occur infinitely often?” could come from finiteness of either set. But \(\mathcal D\) is already proved infinite. Therefore a disproof under the standard reading must prove

\[
\exists N_0\;\forall n\ge N_0,\qquad g_n>1.
\]

Equivalently, it must prove the eventual covering statement

\[
[N_0,\infty)\cap\mathbb Z
\subseteq
\bigcup_p\mathcal B_p.
\]

In explicit local terms: for every \(n\ge N_0\), one must exhibit or prove the existence of a prime \(p\le n\) such that

\[
d_p(n)\in S_p.
\]

A single integer with \(g_n>1\) is not a counterexample: the claim is an infinitude claim, not a universal assertion that every \(n\) is coprime. Likewise, no finite computation by itself can establish eventual non-coprimality unless it is accompanied by a rigorous argument covering all larger \(n\).

---

## 4. What does not count

The following do not resolve the open part:

1. **Proving infinitely many \(n\) have \(g_n>1\).** This is already known.
2. **Checking \(g_n=1\) for very large finite ranges.** This supports the conjecture but does not prove infinitude.
3. **Showing that \(g_n=1\) occurs for arbitrarily large \(n\) only under an unproved hypothesis**, including Schanuel’s conjecture or any logarithmic-independence assumption.
4. **A heuristic estimate**, such as

   \[
   \#\{n\le x:g_n=1\}\asymp \frac{x}{\log x}.
   \]
5. **Showing that each fixed prime \(p\) fails to divide \(g_n\) infinitely often.** The problem requires simultaneous avoidance of every prime \(p\le n\).
6. **Showing that the reduced denominator of \(H_n\) is large**, or contains the full powers of many primes, without proving it equals \(L_n\).
7. **Proving the result only in a bounded range of \(n\)** or only for a finite set of possible prime witnesses.
8. **A density statement for the non-coprime set**, such as upper density \(1\). A set can have upper density \(1\) while its complement remains infinite.
9. **Showing that a random model predicts infinitely many survivors.** Dependencies among the base-\(p\) leading-digit conditions are the central issue.
10. **Finding long intervals containing coprime examples**, unless this is proved for infinitely many intervals.

An infinite explicitly defined subsequence of coprime examples would, of course, fully solve the problem; what does not count is a subsequence verified only experimentally or conditionally.

---

## 5. Known results and context

### 5.1 The non-coprime alternative is settled

As above, if the leading base-\(p\) digit of \(n\) is \(p-1\), with \(p\) odd, then

\[
p\mid g_n.
\]

Taking \(p=3\) gives infinitely many examples. Thus the second half of the original question has a complete elementary affirmative answer.

The phrase in the database commentary “if the leading digit is \(p-1\)” needs the minor qualification \(p\) odd and \(p\le n\). For \(p=2\), the only leading digit is \(1\), but \(2\nmid g_n\).

### 5.2 Necessary and sufficient local condition

The exact criterion

\[
p\mid g_n
\iff
p\mid \operatorname{num}(H_{d_p(n)})
\]

completely reduces the problem to the modular zero sets \(S_p\) and simultaneous avoidance of the corresponding leading-digit intervals.

The congruence in the commentary should technically be written after factoring out the unit \(L_n/p^{e_p(n)}\):

\[
a_n
\equiv
\frac{L_n}{p^{e_p(n)}}
\sum_{j=1}^{d_p(n)}j^{-1}
\pmod p.
\]

The omitted factor is nonzero modulo \(p\), so it does not affect divisibility.

### 5.3 Heuristic prediction

The cited heuristic, associated in the commentary with Shiu [Sh16], predicts

\[
C(x):=\#\{n\le x:g_n=1\}\asymp\frac{x}{\log x}.
\]

This predicts:

- infinitely many coprime examples;
- zero natural density for the coprime set;
- density \(1\) for the non-coprime set.

The scale \(x/\log x\) is consistent with a sieve-dimension-one model. It remains heuristic because the events \(d_p(n)\in S_p\) have substantial deterministic structure and nontrivial correlations across different bases.

### 5.4 Conditional density result

Wu and Yan [WuYa22] proved, conditional on the assertion that

\[
\left\{\frac1{\log p}:p\in P\right\}
\]

is linearly independent over \(\mathbb Q\) for every finite set \(P\) of distinct primes, that

\[
\limsup_{x\to\infty}
\frac{\#\{n\le x:g_n>1\}}{x}
=1.
\]

The required logarithmic-independence statement is itself a consequence of Schanuel’s conjecture.

This result does **not** prove that coprime examples are infinite, even conditionally. Upper density \(1\) for the bad set is compatible both with infinitely many and with finitely many coprime examples.

### 5.5 The prime \(2\) and Kürschák’s argument

The fact \(S_2=\varnothing\) implies that the reduced denominator \(B_n\) always contains the full power

\[
2^{\lfloor\log_2 n\rfloor}
\]

appearing in \(L_n\). This is closely related to the standard \(2\)-adic proof, often attributed to Kürschák, that \(H_n\) is not an integer for \(n>1\): among \(1,\dots,n\), exactly one denominator has the maximal power of \(2\).

This strong control of the \(2\)-part does not extend automatically to odd primes, because several denominators can have maximal \(p\)-adic valuation and their contributions can cancel modulo \(p\).

---

## 6. Traps and edge cases

### 6.1 Confusing \(a_n\) with the reduced numerator

The fraction \(a_n/L_n\) is generally not reduced. For example,

\[
H_6=\frac{49}{20}=\frac{147}{60},
\]

so \(L_6=60\), \(a_6=147\), and

\[
g_6=3.
\]

Using \(49\) as \(a_6\) changes the problem.

### 6.2 The leading digit is defined using the largest power \(p^e\le n\)

At a boundary \(n=p^{e+1}\), the exponent changes from \(e\) to \(e+1\), and the leading digit becomes \(1\), not \(p\). The correct intervals are half-open:

\[
dp^e\le n<(d+1)p^e.
\]

For integer marking, this is

\[
dp^e\le n\le (d+1)p^e-1.
\]

### 6.3 The criterion applies only to \(p\le n\)

For example, \(n=2\) has leading base-\(3\) digit \(2\), but \(3\nmid L_2\). Thus \(n=2\) is not a non-coprime example arising from \(p=3\). In the interval formulation one should take \(e\ge1\).

### 6.4 The \(p=2\) exception

Statements based on the digit \(p-1\) must exclude \(p=2\). Wolstenholme’s theorem also has its standard hypothesis \(p\ge5\); \(p=3\) must be checked separately.

### 6.5 “Numerator of \(H_d\)” must be interpreted correctly

For \(d<p\), the denominator of \(H_d\) is prime to \(p\), so

\[
p\mid\operatorname{num}(H_d)
\]

is unambiguous and equivalent to \(H_d\equiv0\pmod p\). This equivalence would need care if \(d\ge p\), but the leading digit always satisfies \(d\le p-1\).

### 6.6 Pairwise irrationality is not enough

For distinct primes \(p,q\), \(\log p/\log q\) is irrational, since otherwise \(p^a=q^b\) for some positive integers \(a,b\). However, this does not establish the finite-dimensional linear independence of

\[
1/\log p
\]

needed in the cited dynamical argument. Pairwise irrationality does not imply linear independence of larger finite collections.

### 6.7 Independence heuristics can be misleading

The events \(\mathcal B_p\) are deterministic unions of intervals on logarithmic scales. They are not ordinary independent congruence classes. Applying a standard sieve product without rigorous joint-count estimates is invalid.

### 6.8 Upper density \(1\) is not eventual coverage

Even

\[
\limsup_{x\to\infty}\frac{\#(\mathcal D\cap[1,x])}{x}=1
\]

does not imply that \(\mathcal C\) is finite. The heuristic predicts that \(\mathcal C\) is infinite despite having density zero.

### 6.9 Prime divisibility versus prime-power divisibility

The local criterion detects whether \(p\mid g_n\). It does not by itself determine \(v_p(g_n)\). For deciding whether \(g_n=1\), first-power divisibility is sufficient; claims about the exact value of the gcd require higher \(p\)-adic analysis.

### 6.10 Small sanity checks

\[
\begin{array}{c|c|c|c}
n & L_n & a_n & g_n\\ \hline
1&1&1&1\\
2&2&3&1\\
3&6&11&1\\
4&12&25&1\\
5&60&137&1\\
6&60&147&3
\end{array}
\]

Also, \(n=6,7,8\) are detected by \(p=3\), while \(n=9\) is coprime:

\[
H_9=\frac{7129}{2520},\qquad L_9=2520.
\]

---

## 7. Verification hooks

### 7.1 Precompute the modular zero sets \(S_p\)

For each prime \(p\), compute

\[
h_0=0,\qquad h_d=h_{d-1}+d^{-1}\pmod p
\]

for \(1\le d\le p-1\). Then

\[
S_p=\{d:h_d=0\}.
\]

Checks:

- \(S_2=\varnothing\).
- \(S_3=\{2\}\).
- \(S_5=\{4\}\).
- \(S_7=\{6\}\).
- \(S_{11}=\{3,7,10\}\).
- \(p-1\in S_p\) for every odd \(p\).
- If \(d\in S_p\) and \(d\le p-2\), then \(p-1-d\in S_p\).

The binomial test

\[
\binom{p-1}{d}\equiv(-1)^d\pmod{p^2}
\]

provides an independent verification.

### 7.2 Interval sieve for all \(n\le X\)

Initialize a Boolean array `bad[1..X]` as false. For each prime \(p\le X\):

1. Compute \(S_p\) only up to

   \[
   d\le \min(p-1,\lfloor X/p\rfloor),
   \]

   since larger digits cannot produce an interval starting below \(X\).
2. For every \(d\in S_p\), iterate over powers \(q=p^e\), \(e\ge1\), with \(dq\le X\).
3. Mark

   \[
   dq\le n\le \min((d+1)q-1,X)
   \]

   as bad, recording \(p\) as a witness if desired.

After all primes are processed, the unmarked integers are exactly the \(n\le X\) with \(g_n=1\).

This avoids constructing the enormous integer \(L_n\).

### 7.3 Direct exact-rational cross-check

For moderate \(X\), independently compute

\[
L_n=\operatorname{lcm}(L_{n-1},n),\qquad
a_n=\sum_{k=1}^n \frac{L_n}{k},
\]

or update \(H_n\) using exact rational arithmetic. Compare

\[
\gcd(a_n,L_n)=1
\]

against the interval sieve. Every disagreement indicates an implementation error, usually at a power boundary or interval endpoint.

### 7.4 Empirical counting tests

Compute

\[
C(X)=\#\{n\le X:g_n=1\}
\]

and inspect

\[
\frac{C(X)\log X}{X}.
\]

This tests the \(X/\log X\) heuristic but does not prove it. Also record:

- largest coprime \(n\le X\);
- maximal gap between coprime examples;
- distribution of the least prime \(p\mid g_n\);
- number of prime witnesses for each bad \(n\).

### 7.5 Local hazard statistics

For each \(p\), compute

\[
W_p:=\sum_{d\in S_p}\log\left(1+\frac1d\right).
\]

On logarithmic scale, the leading-digit interval for \(d\) has relative length

\[
\frac{\log(1+1/d)}{\log p}.
\]

Thus \(W_p/\log p\) is a natural local measure of the bad digit set. Compare it with random-model predictions and separate the forced digit \(d=p-1\) from exceptional zeros.

### 7.6 Correlation tests

For primes \(p\ne q\), estimate

\[
\#\{n\le X:n\in\mathcal B_p\cap\mathcal B_q\}
\]

and compare it to the product of the individual frequencies. Repeat for triples of small primes. Large systematic deviations identify where a naive sieve or independence argument is likely to fail.

### 7.7 Testing proposed covering arguments

If a disproof route proposes that a collection of primes covers all sufficiently large \(n\), explicitly compute the complement of

\[
\bigcup_{p\in P}\mathcal B_p
\]

for increasing finite \(P\) and large \(X\). Record whether survivors persist, their logarithmic phases, and whether a finite set of primes appears capable of covering all phases.

---

## 8. Attack routes

### Route 1: Arithmetic structure of the harmonic zero sets \(S_p\)

**Core mechanism.** Study the congruences

\[
H_d\equiv0\pmod p
\]

or equivalently

\[
\binom{p-1}{d}\equiv(-1)^d\pmod{p^2}.
\]

The aim is to obtain uniform information on the size and location of \(S_p\), especially its weighted size

\[
\sum_{d\in S_p}\log(1+1/d).
\]

**Key lemma needed.** A theorem giving sufficiently strong average control over \(S_p\), for example a bound or asymptotic for

\[
\sum_{p\le y}\sum_{d\in S_p} w(d,p)
\]

with the leading-digit weight \(w(d,p)\approx 1/(d\log p)\), together with control of exceptional primes.

**Why it might work.** The obstruction is entirely encoded by the modular partial sums \(H_d\). If these zeros behave approximately randomly apart from the forced zero \(d=p-1\) and symmetry, one expects a dimension-one sieve and \(C(x)\asymp x/\log x\).

**Likely failure point.** Modular harmonic zeros are sparse but arithmetically rigid. Even proving useful uniform bounds for the number of \(d<p\) with \(H_d\equiv0\pmod p\) may be difficult, and local information alone does not control correlations between different bases.

**Quick blockage test.** Compute \(|S_p|\), the least exceptional zero, and \(W_p\) for all primes up to a large bound. Check whether rare primes with unusually large or small-digit zero sets dominate the weighted sums.

---

### Route 2: A genuine sieve for logarithmic leading-digit events

**Core mechanism.** Treat each condition

\[
n\in\mathcal B_p
\]

as a local sieving event and seek a lower-bound sieve for integers avoiding all such events.

**Key lemma needed.** Uniform joint-count estimates of the form

\[
\#\{n\le x:n\in\mathcal B_p\text{ for all }p\in P\}
=
x\,\delta(P)+\text{controlled error}
\]

for sufficiently many finite prime sets \(P\), plus a tail estimate showing that primes larger than the sieve level do not eliminate all survivors.

**Why it might work.** The heuristic \(x/\log x\) strongly suggests a dimension-one sieve. The exact interval description makes the local events explicit rather than probabilistic abstractions.

**Likely failure point.** These are not residue classes modulo \(p\). Their endpoints occur at powers of \(p\), and simultaneous conditions involve incompatible logarithmic scales. Standard Selberg or combinatorial sieve axioms do not apply automatically. The large-prime tail may also be as difficult as the original problem.

**Quick blockage test.** For finite prime sets \(P\), compare the exact survivor proportion to the product of individual survivor proportions over many dyadic ranges. If errors remain comparable to the main term as \(|P|\) grows, a conventional sieve is blocked.

---

### Route 3: Dynamical and Fourier analysis on logarithmic tori

**Core mechanism.** Put \(t=\log n\). The leading base-\(p\) digit is determined by

\[
\left\{\frac{t}{\log p}\right\}.
\]

More precisely,

\[
d_p(n)=d
\quad\Longleftrightarrow\quad
\left\{\frac{\log n}{\log p}\right\}
\in
[\log_p d,\log_p(d+1)).
\]

For a finite set of primes, simultaneous digit conditions become a hitting problem for a linear flow on a torus.

**Key lemma needed.** Quantitative equidistribution, with usable discrepancy bounds, for

\[
t\longmapsto
\left(\frac{t}{\log p_1},\dots,\frac{t}{\log p_r}\right)\pmod1
\]

as the dimension \(r\) grows, together with a transfer from continuous \(t\) to integer \(n=e^t\).

**Why it might work.** It directly addresses the correlations among different bases and matches the framework behind the conditional Wu–Yan result.

**Likely failure point.** The required finite-dimensional rational independence of \(1/\log p\) is unproved and follows from Schanuel’s conjecture. Even qualitative independence for each fixed dimension may be insufficient; the problem requires control as the relevant set of primes grows with \(n\).

**Quick blockage test.** Perform Fourier expansions for two or three small primes and identify the needed lower bounds on linear forms

\[
\sum_j \frac{m_j}{\log p_j}.
\]

If the error term requires an unproved nonvanishing or quantitative lower bound for such expressions, the route has reached the known transcendence barrier.

---

### Route 4: Deterministic construction by nested intervals or a local lemma

**Core mechanism.** Construct \(n\) iteratively. At each stage, choose a subinterval avoiding the bad leading digits for another block of primes, while preserving enough interval length to continue.

Possible tools include a deterministic Lovász local lemma, entropy compression, multiscale interval selection, or a Cantor-set construction on the logarithmic axis.

**Key lemma needed.** A robust survivor lemma: after excluding \(\mathcal B_p\) for all \(p\le z\), every sufficiently large scale still contains a long interval or a quantitatively large, well-distributed survivor set that cannot be completely removed by primes \(p>z\).

**Why it might work.** The events have a clear multiscale geometry. A constructive argument might avoid the need for full statistical independence and produce one survivor at each large scale.

**Likely failure point.** The exclusions are global and highly nonlocal. A choice that is safe for small primes can force bad leading digits for later primes. The survivor set may be large in cardinality but fragmented into intervals too short for continued construction.

**Quick blockage test.** Run the interval sieve while retaining the connected components of the survivor set after each prime block. Measure component lengths and branching numbers. Rapid collapse to isolated points indicates that a nested-interval argument needs a substantially stronger invariant.

---

### Route 5: \(p\)-adic denominator dynamics under \(H_{n+1}=H_n+1/(n+1)\)

**Core mechanism.** Track the reduced denominator \(B_n\) or the deficit

\[
g_n=\frac{L_n}{B_n}
\]

under the recurrence

\[
H_{n+1}=H_n+\frac1{n+1}.
\]

Special attention should be paid to times when \(n+1\) is a prime power, since those are exactly the times when \(L_n\) gains a new prime factor or a higher prime power.

**Key lemma needed.** A renewal or restoration principle ensuring that the full \(p\)-adic denominator is recovered simultaneously for all relevant odd primes infinitely often, perhaps near a controlled family of prime-power boundaries.

**Why it might work.** The \(2\)-adic component is always maximal, and changes in \(L_n\) are sparse and structured. A successful induction might exploit moments when new denominator powers enter without immediate cancellation.

**Likely failure point.** Between prime-power boundaries, repeated additions can create or remove \(p\)-adic cancellations in ways depending on many earlier terms. Simultaneous control over all old primes appears difficult, and the local leading-digit criterion may simply reappear in another form.

**Quick blockage test.** Compute the vector

\[
\bigl(v_p(B_n):p\le n\bigr)
\]

around prime powers and least-common-multiple jump points. Test whether clean values cluster near any reproducible class of boundaries. If no stable renewal pattern appears, a simple induction is unlikely.

---

### Route 6: Disproof via eventual covering

**Core mechanism.** Attempt to prove that every sufficiently large \(n\) lies in at least one bad interval

\[
[dp^e,(d+1)p^e),\qquad d\in S_p.
\]

One could seek either:

- a finite set of primes whose logarithmic bad sets cover all sufficiently large scales; or
- a theorem producing, for every large \(n\), a prime \(p\) with \(d_p(n)\in S_p\).

**Key lemma needed.** An eventual covering theorem:

\[
\exists N_0\;\forall n\ge N_0\;\exists p\le n:
d_p(n)\in S_p.
\]

A more specific version might find \(p\) in a controlled interval and then force the relevant harmonic congruence.

**Why it might work.** The bad set is conjectured to have density \(1\), and every odd prime contributes at least the forced digit \(p-1\). Additional zeros in \(S_p\) enlarge the covering substantially.

**Likely failure point.** Density \(1\) is far weaker than eventual coverage. The prevailing heuristic predicts approximately \(x/\log x\) uncovered integers, so this route is aimed against the expected answer. Forced digits alone appear too sparse, and exceptional harmonic zeros behave more like a divergent probabilistic sieve than a deterministic cover.

**Quick blockage test.** Compute uncovered integers to the largest feasible \(X\), their gap statistics, and their count relative to \(X/\log X\). Persistent survivors with sieve-like counts strongly disfavor eventual coverage, though they cannot rule it out.

---

## 9. Verdict on difficulty

The second half of the problem is elementary and completely settled. The first half—infinitely many \(n\) with

\[
\gcd(a_n,L_n)=1
\]

—is genuinely open.

The exact local criterion is simple, but the global problem requires simultaneous avoidance of infinitely many structured leading-digit conditions in different prime bases. This is not a routine harmonic-number congruence problem and not a routine sieve problem.

A major natural density approach encounters linear independence questions for the numbers \(1/\log p\). The hypothesis used by Wu and Yan is a consequence of **Schanuel’s conjecture**, so there is a real transcendence-theoretic barrier in that approach. This should be stated loudly:

> A prominent route to controlling the cross-prime logarithmic dynamics currently relies on an independence statement implied by Schanuel’s conjecture.

However, the Erdős problem is not known to be equivalent to Schanuel’s conjecture, and the cited Schanuel-conditional result does not itself prove infinitely many coprime cases. A successful solution may require a different mechanism—most plausibly a new sieve for logarithmic interval events, a strong theorem on modular zeros of partial harmonic sums, or a deterministic multiscale construction.

The heuristic prediction \(C(x)\asymp x/\log x\) strongly favors an affirmative answer, but turning that heuristic into even the bare statement \(C(x)\to\infty\) appears difficult.