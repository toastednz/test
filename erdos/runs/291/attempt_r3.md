STATUS: BLOCKED

## Result

Route 3 gives a strong unconditional finite-dimensional result: for every fixed finite set of primes \(P\), there are multiplicatively syndetic intervals on which every \(p\in P\) has leading digit \(1\), hence cannot divide \(g_n\). In fact, the integers with \(d_p(n)=1\) for all \(p\in P\) have positive lower natural density and a positive logarithmic density determined by Haar measure on the actual orbit closure; no reciprocal-logarithm independence is needed. I also prove that, for every \(\varepsilon>0\), every prime divisor of \(g_n\) is at most \((1+\varepsilon)n/\log n\) for all sufficiently large \(n\). Nevertheless, at \(n=e^T\) this still leaves about \(e^T/T^2\) primes to control. Neither compact recurrence nor Fourier analysis supplies estimates uniform in that rapidly growing dimension, and the required Fourier discrepancies lead back to uncontrolled linear forms in \(1/\log p\). Thus Route 3 does not currently bridge finite-prime avoidance to simultaneous avoidance of all possible witnesses.

## Complete Argument

### 1. Torus formulation

Fix a finite set of primes

\[
P=\{p_1,\dots,p_r\},
\qquad
\alpha=\left(\frac1{\log p_1},\dots,\frac1{\log p_r}\right),
\]

and define the one-parameter flow

\[
\phi(t)=t\alpha\pmod 1\in\mathbb T^r.
\]

Let

\[
H_P:=\overline{\{\phi(t):t\in\mathbb R\}}\subseteq\mathbb T^r.
\]

This is a compact connected subgroup of \(\mathbb T^r\).

For \(x=e^t\), the leading base-\(p\) digit is \(1\) exactly when

\[
\left\{\frac{t}{\log p}\right\}
\in
\left[0,\frac{\log 2}{\log p}\right).
\]

Thus, writing

\[
B_P
:=
\prod_{p\in P}
\left(0,\frac{\log 2}{\log p}\right)
\subseteq\mathbb T^r,
\]

we have, away from the harmless boundary points,

\[
\phi(\log n)\in B_P
\quad\Longrightarrow\quad
d_p(n)=1\quad\text{for every }p\in P.
\]

Since \(1\notin S_p\), every such integer avoids every prime in \(P\) as a divisor of \(g_n\).

---

### 2. Arbitrarily large common digit-\(1\) intervals

#### Theorem 1

For every finite set of primes \(P\), there exist constants \(K=K(P)>0\) and \(w=w(P)>0\) such that every sufficiently long logarithmic interval of length \(K\) contains an interval of length \(2w\) on which

\[
d_p(\lfloor e^t\rfloor)=1
\qquad\text{for all }p\in P.
\]

Consequently, there is a constant \(c(P)>0\) such that

\[
\liminf_{X\to\infty}
\frac1X
\#\{n\le X:d_p(n)=1\text{ for every }p\in P\}
\ge c(P)>0.
\]

#### Proof

Put

\[
\delta=\frac{\log 2}{2}.
\]

Then

\[
\phi(\delta)
=
\left(\frac{\delta}{\log p}\right)_{p\in P}
\]

lies in the interior of \(B_P\), since

\[
0<\frac{\delta}{\log p}
<
\frac{\log 2}{\log p}.
\]

By continuity, there exist an open neighborhood \(U\) of \(0\) in \(H_P\) and \(w>0\) such that

\[
U+\phi([\delta-w,\delta+w])\subseteq B_P.
\tag{1}
\]

The positive orbit \(\{\phi(t):t\ge0\}\) is dense in \(H_P\). One way to see this is that simultaneous Dirichlet approximation gives arbitrarily large \(R\) with \(\phi(R)\) arbitrarily close to \(0\). Hence any negative orbit point \(\phi(-s)\) is a limit of positive orbit points \(\phi(R-s)\).

It follows that the flow on \(H_P\) is minimal. Therefore the family

\[
\{U-\phi(t):t\ge0\}
\]

covers \(H_P\). By compactness, finitely many of these sets suffice:

\[
H_P\subseteq
\bigcup_{i=1}^m\bigl(U-\phi(t_i)\bigr),
\qquad t_i\ge0.
\]

Let \(K=\max_i t_i\). For every \(T\ge0\), applying this covering to \(\phi(T)\) gives some \(t_i\le K\) such that

\[
\phi(T+t_i)\in U.
\]

Thus every interval \([T,T+K]\) contains a return time \(R\) with \(\phi(R)\in U\).

By (1), for every such \(R\),

\[
\phi(t)\in B_P
\qquad
(R+\delta-w\le t\le R+\delta+w).
\]

For every integer \(n\) whose logarithm lies in this interval, and for every \(p\in P\), the significand of \(n\) in base \(p\) lies strictly between \(1\) and \(2\). Hence \(d_p(n)=1\).

Now let \(T=\log X\) be large. Apply the preceding return statement starting at

\[
T-(K+\delta+w).
\]

There is a good logarithmic interval \([u,u+2w]\) entirely below \(T\), with

\[
u\ge T-K-2w.
\]

It contains at least

\[
e^u(e^{2w}-1)-2
\]

integers. Therefore

\[
\frac1X
\#\{n\le X:d_p(n)=1\ \forall p\in P\}
\ge
e^{-K-2w}(e^{2w}-1)-\frac2X.
\]

Taking the lower limit proves the theorem. ∎

In particular, no finite set of primes can cover all sufficiently large integers through the bad sets \(\mathcal B_p\).

---

### 3. Quantitative finite-dimensional recurrence

The preceding compactness proof gives no usable estimate for \(K(P)\). A direct Dirichlet estimate illustrates how rapidly the available bound deteriorates with \(|P|\).

#### Lemma 2

Let \(P\) contain \(r\) primes, let \(0<\rho<\log 2/4\), and let \(M\ge1\) be an integer. There is a real number \(T\) satisfying

\[
M\le T
\le
M\left(
\left\lceil\frac{M\log p_{\max}}{\rho}\right\rceil+1
\right)^r
\tag{2}
\]

and, for each \(p\in P\), an integer \(k_p\) such that

\[
|T-k_p\log p|<\rho.
\tag{3}
\]

Consequently, throughout

\[
T+2\rho
\le t\le
T+\log 2-2\rho,
\tag{4}
\]

the leading base-\(p\) digit of \(e^t\) is \(1\) for every \(p\in P\).

#### Proof

Let

\[
Q=
\left\lceil\frac{M\log p_{\max}}{\rho}\right\rceil+1.
\]

Dirichlet’s simultaneous approximation theorem gives an integer \(q\) with

\[
1\le q\le Q^r,
\qquad
\left\|\frac q{\log p}\right\|\le\frac1Q
\quad(p\in P).
\]

Put \(T=Mq\). Then

\[
\left\|\frac T{\log p}\right\|
\le
M\left\|\frac q{\log p}\right\|
\le\frac MQ.
\]

Therefore the distance from \(T\) to the nearest multiple of \(\log p\) is at most

\[
\log p\,\frac MQ
\le
\log p_{\max}\frac MQ
<\rho.
\]

This proves (2) and (3).

Write \(T-k_p\log p=\eta_p\), where \(|\eta_p|<\rho\). If \(t=T+s\) and

\[
2\rho\le s\le\log 2-2\rho,
\]

then

\[
0<\rho\le \eta_p+s\le\log 2-\rho<\log p.
\]

Thus \(t\bmod\log p\in(0,\log 2)\), which is exactly the leading-digit-\(1\) condition. ∎

The upper bound in (2) is exponential in \(r\). This is already far too weak once \(P\) grows with \(n\).

---

### 4. Haar measure and unconditional finite-dimensional equidistribution

Define the relation lattice

\[
\Lambda_P
=
\left\{
m=(m_p)_{p\in P}\in\mathbb Z^r:
\sum_{p\in P}\frac{m_p}{\log p}=0
\right\}.
\]

This lattice is the annihilator of \(H_P\). No assertion that \(\Lambda_P=\{0\}\) is needed for qualitative equidistribution on \(H_P\).

#### Proposition 3

Let \(\mu_P\) denote normalized Haar measure on \(H_P\). Then

\[
\lim_{T\to\infty}
\frac1T
\int_0^T
1_{B_P}(\phi(t))\,dt
=
\mu_P(B_P\cap H_P)>0.
\tag{5}
\]

#### Proof

For each coordinate projection \(\pi_p:H_P\to\mathbb T\), the image is all of \(\mathbb T\), because

\[
t\longmapsto \frac t{\log p}\pmod1
\]

is surjective. The pushforward of \(\mu_P\) under \(\pi_p\) is therefore Haar measure on \(\mathbb T\). Hence every coordinate hyperplane of the form \(x_p=c\) has \(\mu_P\)-measure zero. The boundary of \(B_P\) is contained in finitely many such hyperplanes, so

\[
\mu_P(\partial B_P)=0.
\]

The linear flow is uniquely ergodic on its orbit closure. This can be checked directly on characters: for \(m\in\mathbb Z^r\),

\[
\frac1T
\int_0^T
e^{2\pi i m\cdot\phi(t)}\,dt
\longrightarrow
\begin{cases}
1,&m\in\Lambda_P,\\
0,&m\notin\Lambda_P.
\end{cases}
\]

The same is true for the Haar integral over \(H_P\). Trigonometric approximation, together with the zero-measure boundary, gives (5).

Finally, \(\phi(\delta)\in B_P\cap H_P\), where \(\delta=\log 2/2\). Thus \(B_P\cap H_P\) contains a nonempty relatively open subset of \(H_P\). Every nonempty open subset of a compact group has positive Haar measure, proving positivity. ∎

There is also a discrete logarithmic-density consequence. Let

\[
E_P=\{n\ge\max P:d_p(n)=1\text{ for all }p\in P\}.
\]

Then

\[
\sum_{\substack{n\le X\\n\in E_P}}\frac1n
=
\mu_P(B_P\cap H_P)\log X+o(\log X).
\tag{6}
\]

Indeed,

\[
\int_1^X
1_{B_P}(\phi(\log x))\,\frac{dx}{x}
=
\int_0^{\log X}1_{B_P}(\phi(t))\,dt.
\]

The indicator changes only at points \(x=p^k\) or \(x=2p^k\), \(p\in P\). On each interval of constancy,

\[
\sum_{A\le n<B}\frac1n
=
\log(B/A)+O(1/A).
\]

The sum of the errors over all boundary intervals is \(O_P(1)\), because

\[
\sum_{p\in P}\sum_{k\ge0}p^{-k}<\infty.
\]

Combining this with (5) proves (6).

---

### 5. The exact Fourier obstruction

For a smooth function \(\Phi:\mathbb T^r\to\mathbb C\), write

\[
\Phi(x)=\sum_{m\in\mathbb Z^r}\widehat\Phi(m)e^{2\pi i m\cdot x}.
\]

If the Fourier series is absolutely convergent, then

\[
\frac1T\int_0^T\Phi(\phi(t))\,dt
-
\sum_{m\in\Lambda_P}\widehat\Phi(m)
\]

has absolute value at most

\[
\sum_{m\notin\Lambda_P}
|\widehat\Phi(m)|
\min\left(
1,
\frac1{\pi T\left|\sum_{p\in P}m_p/\log p\right|}
\right).
\tag{7}
\]

This follows by integrating each character:

\[
\frac1T\int_0^T e^{2\pi i(m\cdot\alpha)t}\,dt
=
\frac{e^{2\pi i(m\cdot\alpha)T}-1}
{2\pi iT(m\cdot\alpha)}.
\]

Thus quantitative discrepancy requires lower bounds for the nonzero linear forms

\[
\sum_{p\in P}\frac{m_p}{\log p}.
\tag{8}
\]

For two primes, a relation would force a rational ratio of their logarithms and is impossible by unique factorization. For three or more primes, general rational independence of the reciprocals \(1/\log p\) is not known.

There is a further issue: uniform integers \(n\le e^T\) do not correspond to a uniform average over \(0\le t\le T\). They correspond to an exponentially weighted average near \(T\). For smooth \(\Phi\), Euler summation gives

\[
\frac1{e^T}
\sum_{n\le e^T}\Phi(\phi(\log n))
=
\int_0^\infty
e^{-u}\Phi(\phi(T)-\phi(u))\,du+o(1).
\tag{9}
\]

Indeed, replacing the sum by an integral costs \(O_\Phi(T)\), and after \(x=e^{T-u}\),

\[
e^{-T}\int_1^{e^T}\Phi(\phi(\log x))\,dx
=
\int_0^T e^{-u}\Phi(\phi(T-u))\,du.
\]

The omitted tail is \(O(e^{-T})\).

The Fourier expansion of the right side of (9) is

\[
\sum_{m\in\mathbb Z^r}
\frac{\widehat\Phi(m)e^{2\pi i(m\cdot\alpha)T}}
{1+2\pi i(m\cdot\alpha)}.
\tag{10}
\]

Hence ordinary long-time equidistribution does not directly produce a natural-density statement. Natural counting depends on the current torus phase \(\phi(T)\), not only on the Haar mean.

---

### 6. A rigorous large-prime cutoff

The torus dimension can be reduced slightly because very large primes cannot divide \(g_n\).

Write \(H_d=U_d/V_d\) in lowest terms.

#### Lemma 4

As \(d\to\infty\),

\[
\log U_d\le d\log 4+O(\log d).
\tag{11}
\]

#### Proof

Let \(L_d=\operatorname{lcm}(1,\dots,d)\), and put

\[
r=\left\lceil\frac d2\right\rceil,
\qquad
s=\left\lfloor\frac d2\right\rfloor.
\]

For each prime \(\ell\), the exponent of \(\ell\) in \(L_d/L_r\) is either \(0\) or \(1\). If it is \(1\), then the largest power \(q=\ell^a\le d\) satisfies \(q>r\). In Legendre’s formula for

\[
v_\ell\binom ds,
\]

the summand corresponding to \(q\) is

\[
\left\lfloor\frac dq\right\rfloor
-
\left\lfloor\frac rq\right\rfloor
-
\left\lfloor\frac sq\right\rfloor
=
1.
\]

Therefore

\[
\frac{L_d}{L_r}\mid\binom ds,
\]

and hence

\[
\log L_d\le d\log2+\log L_{\lceil d/2\rceil}.
\]

Iterating this inequality gives

\[
\log L_d
\le
\log2\left(
d+\left\lceil\frac d2\right\rceil
+\left\lceil\frac d4\right\rceil+\cdots
\right)
\le d\log4+O(\log d).
\tag{12}
\]

Since \(V_d\mid L_d\),

\[
L_dH_d=\frac{L_d}{V_d}U_d
\]

is a positive integer multiple of \(U_d\). Consequently,

\[
U_d\le L_dH_d.
\]

Using \(H_d\le1+\log d\) and (12) gives (11). ∎

#### Proposition 5

For every constant \(C>\log4\), all sufficiently large \(n\) satisfy

\[
p\mid g_n
\quad\Longrightarrow\quad
p\le C\frac n{\log n}.
\tag{13}
\]

Using the prime number theorem, \(\log L_d=d+o(d)\), this improves to: for every \(\varepsilon>0\), all sufficiently large \(n\) satisfy

\[
p\mid g_n
\quad\Longrightarrow\quad
p\le(1+\varepsilon)\frac n{\log n}.
\tag{14}
\]

#### Proof

Suppose, to the contrary, that for arbitrarily large \(n\) there is a witnessing prime

\[
p>C\frac n{\log n}.
\]

For large \(n\), this implies \(p>\sqrt n\), so \(e_p(n)=1\). Put

\[
d=d_p(n)=\left\lfloor\frac np\right\rfloor.
\]

By the exact local criterion,

\[
p\mid U_d.
\]

If \(d\) remained bounded along a subsequence, then \(p\) would divide one of finitely many fixed integers \(U_d\), contradicting \(p\to\infty\). Thus \(d\to\infty\).

By Lemma 4,

\[
\log p
\le
\log U_d
\le
d\log4+O(\log d)
\le
\frac{\log4}{C}\log n+O(\log\log n).
\]

On the other hand,

\[
\log p
>
\log n-\log\log n+\log C
=
(1-o(1))\log n.
\]

Since \(\log4/C<1\), this is a contradiction. This proves (13).

For (14), use the prime number theorem in the equivalent form

\[
\log L_d=\psi(d)=d+o(d).
\]

It gives

\[
\log U_d\le d+o(d).
\]

If \(p>(1+\varepsilon)n/\log n\), then

\[
d<\frac{\log n}{1+\varepsilon},
\]

so, for some fixed \(\eta>0\),

\[
\log p\le\log U_d\le(1-\eta)\log n
\]

for all sufficiently large \(n\), while again \(\log p=(1-o(1))\log n\). This contradiction proves (14). ∎

Thus at \(n=e^T\), only primes

\[
p\le(1+o(1))\frac{e^T}{T}
\]

can witness non-coprimality. Unfortunately, this is still approximately

\[
\pi(e^T/T)\asymp \frac{e^T}{T^2}
\]

coordinates.

For completeness, the non-coprime set is already infinite: if \(n=2\cdot3^e\), then \(d_3(n)=2\), and \(H_2=3/2\equiv0\pmod3\), so \(3\mid g_n\).

## Self-Audit

1. **The compact-group recurrence argument is qualitative and hides an enormous constant \(K(P)\).** The argument itself is rigorous: minimality, compactness, and a finite subcover give syndetic returns. Lemma 2 independently verifies recurrence by an explicit Dirichlet construction. What is unavailable is any useful uniform control as \(|P|\) grows.

2. **The transfer from continuous logarithmic time to integers could fail if boundary errors accumulated.** For fixed \(P\), the boundaries are only the geometric sequences \(p^k\) and \(2p^k\), and their reciprocal sum converges. This gives the stated \(O_P(1)\) harmonic-sum error and \(O_P(\log X)\) ordinary counting error. The argument is not uniform when \(P\) grows with \(X\), and I do not use it as though it were.

3. **The sharp cutoff \(p\le(1+\varepsilon)n/\log n\) invokes the prime number theorem and must handle small \(d\).** The PNT is unconditional, and bounded \(d\) is treated separately because then \(p\) divides one of finitely many fixed numerators \(U_d\). The fully elementary version \(p\le Cn/\log n\) for every \(C>\log4\) is proved without the PNT.

## Computations To Verify

```python
from math import gcd, log, exp, ceil, floor
from fractions import Fraction
from itertools import product

def primes_upto(N):
    sieve = bytearray(b"\x01") * (N + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, int(N**0.5) + 1):
        if sieve[q]:
            sieve[q*q:N+1:q] = b"\x00" * (((N-q*q)//q)+1)
    return [q for q in range(2, N+1) if sieve[q]]

def zero_digits(p, D=None):
    if D is None:
        D = p - 1
    D = min(D, p - 1)
    h = 0
    ans = []
    for d in range(1, D + 1):
        h = (h + pow(d, -1, p)) % p
        if h == 0:
            ans.append(d)
    return ans

# Basic checks on S_p.
for p in [2, 3, 5, 7, 11]:
    print(p, zero_digits(p))
# Expected:
# 2 []
# 3 [2]
# 5 [4]
# 7 [6]
# 11 [3, 7, 10]
```

```python
def leading_digit(n, p):
    assert p <= n
    q = p
    while q <= n // p:
        q *= p
    return n // q

def interval_sieve(X):
    ps = primes_upto(X)
    bad = bytearray(X + 1)
    largest_witness = [0] * (X + 1)

    for p in ps:
        D = min(p - 1, X // p)
        S = zero_digits(p, D)

        q = p
        while q <= X:
            for d in S:
                lo = d * q
                if lo > X:
                    break
                hi = min((d + 1) * q - 1, X)
                for n in range(lo, hi + 1):
                    bad[n] = 1
                    largest_witness[n] = max(largest_witness[n], p)
            if q > X // p:
                break
            q *= p

    survivors = [n for n in range(1, X + 1) if not bad[n]]
    return survivors, largest_witness

X = 10000
survivors, largest_witness = interval_sieve(X)
print("number of survivors:", len(survivors))
print("largest survivor:", survivors[-1])

# Test the asymptotic witness cutoff numerically.
ratios = [
    largest_witness[n] * log(n) / n
    for n in range(3, X + 1)
    if largest_witness[n] > 0
]
print("largest p*log(n)/n observed:", max(ratios))
```

```python
# Direct exact-rational cross-check.
def lcm(a, b):
    return a // gcd(a, b) * b

def direct_g_values(X):
    H = Fraction(0, 1)
    L = 1
    out = []
    for n in range(1, X + 1):
        H += Fraction(1, n)
        L = lcm(L, n)
        a = L * H.numerator // H.denominator
        out.append(gcd(a, L))
    return out

X = 500
survivors, _ = interval_sieve(X)
survivor_set = set(survivors)
gvals = direct_g_values(X)

for n, g in enumerate(gvals, start=1):
    assert ((g == 1) == (n in survivor_set))
print("direct and interval methods agree through", X)
```

```python
# Search for simultaneous near-returns used in Lemma 2.
def common_returns(P, Tmax, rho):
    ans = []
    for T in range(1, Tmax + 1):
        errors = [
            abs(T - round(T / log(p)) * log(p))
            for p in P
        ]
        if max(errors) < rho:
            ans.append((T, max(errors)))
    return ans

P = [2, 3, 5]
rho = log(2) / 20
returns = common_returns(P, 2_000_000, rho)
print(returns[:10])

# For any return T, all t in
# [T + 2*rho, T + log(2) - 2*rho]
# should have leading digit 1 in every base in P.
if returns:
    T = returns[0][0]
    lo = ceil(exp(T + 2*rho))
    hi = floor(exp(T + log(2) - 2*rho))
    # This interval may be astronomically large; sample endpoints instead.
    for n in [lo, min(lo + 100, hi), hi]:
        if n >= max(P):
            assert all(leading_digit(n, p) == 1 for p in P)
```

```python
# Search numerically for small reciprocal-log near-resonances.
# A very small nonzero value warns that Fourier discrepancy bounds
# may be poor; numerical output cannot prove nonvanishing.
def near_resonances(P, M):
    alpha = [1.0 / log(p) for p in P]
    best = None
    for m in product(range(-M, M + 1), repeat=len(P)):
        if all(x == 0 for x in m):
            continue
        value = abs(sum(x*a for x, a in zip(m, alpha)))
        if best is None or value < best[0]:
            best = (value, m)
    return best

print(near_resonances([2, 3, 5], 50))
print(near_resonances([2, 3, 5, 7], 15))
```

## Route Diagnosis

**Proved ledger.**

- For every fixed finite \(P\), simultaneous digit-\(1\) avoidance is multiplicatively syndetic.
- The corresponding integers have positive lower natural density.
- Their logarithmic density is the positive Haar measure \(\mu_P(B_P\cap H_P)\).
- Finite-dimensional qualitative equidistribution holds unconditionally on the actual orbit closure \(H_P\); reciprocal-log independence is needed only to assert \(H_P=\mathbb T^{|P|}\).
- The exact Fourier discrepancy involves linear forms \(\sum m_p/\log p\).
- Every witness prime satisfies \(p\le(1+\varepsilon)n/\log n\) for all sufficiently large \(n\).

**Plausible but unproved claims needed to continue.**

- A growing-dimensional survivor theorem for the full safe digit sets, with dimension roughly \(e^T/T^2\) at logarithmic height \(T\).
- Uniform discrepancy estimates strong enough to handle discontinuous boxes and a number of frequencies growing with \(T\).
- Alternatively, sufficiently strong arithmetic estimates on the exceptional harmonic zeros \(S_p\) to reduce the effective number of relevant coordinates drastically.

**Dead ends.**

- Requiring digit \(1\) for every relevant prime is much too restrictive. Dirichlet recurrence costs exponentially in the number of primes, while the required number of coordinates is exponential in \(T\).
- Replacing the orbit closure by the full torus requires rational independence of the numbers \(1/\log p\), which is unproved for general finite sets and is tied to the stated Schanuel barrier.
- Ordinary logarithmic-time equidistribution does not directly control uniform integer counts, because those counts correspond to the exponentially weighted phase expression (9).
- The large-prime cutoff saves only a factor of \(\log n\); it does not reduce the problem to finitely or even polynomially many coordinates in \(T=\log n\).

A fresh attempt should combine Route 3 with arithmetic pruning of the sets \(S_p\), rather than seek full high-dimensional torus equidistribution. The concrete missing theorem would be a uniform bound showing that, for most \(n\), only a much smaller family of primes \(p\le n/\log n\) can satisfy \(p\mid U_{\lfloor n/p\rfloor}\), together with a sieve or recurrence argument for that reduced family. Without such pruning, Route 3 remains blocked at a growing-dimensional transcendence and discrepancy barrier.