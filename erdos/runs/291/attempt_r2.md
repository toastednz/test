STATUS: BLOCKED
## Result

Route 2 does not currently yield a complete solution. I proved three relevant facts: (i) every finite collection of prime obstructions can be simultaneously avoided on arbitrarily large multiplicative intervals of fixed ratio, unconditionally and without logarithmic-independence assumptions; (ii) any prime witnessing \(p\mid g_n\) satisfies the asymptotic cutoff \(p\ll n\log\log n/\log n\), and witnesses above \(\sqrt n\) are exactly large prime divisors of numerators of smaller harmonic numbers; and (iii) logarithmic leading-digit events for two distinct primes are unconditionally pairwise independent, although the higher-order independence needed by a lower-bound sieve reaches the stated reciprocal-logarithm barrier. I also show explicitly why a conventional natural-density sieve fails already for \(p=3\), and why elementary size bounds for harmonic numerators give no usable large-prime tail estimate. Thus the route is blocked by two separate unresolved inputs: uniform arithmetic control of the sets \(S_p\), and growing-dimensional joint-count estimates/tail control.

## Complete Argument

### 1. Setup

For a prime \(p\le n\), write

\[
p^{e_p(n)}\le n<p^{e_p(n)+1},
\qquad
d_p(n)=\left\lfloor\frac{n}{p^{e_p(n)}}\right\rfloor.
\]

Let

\[
S_p=\{1\le d\le p-1:H_d\equiv0\pmod p\}.
\]

The local criterion from the brief gives

\[
p\mid g_n\quad\Longleftrightarrow\quad d_p(n)\in S_p.
\tag{1}
\]

I use (1) throughout.

A minor unconditional restriction on \(S_p\) is worth recording.

#### Lemma 1: No two consecutive digits lie in \(S_p\)

For every prime \(p\), if \(1\le d\le p-2\), then \(d\) and \(d+1\) cannot both belong to \(S_p\).

**Proof.**
If both belonged to \(S_p\), then modulo \(p\),

\[
0=H_{d+1}-H_d=\frac1{d+1},
\]

which is impossible because \(d+1<p\). ∎

Thus \(|S_p|\le \lceil (p-1)/2\rceil\). This is far too weak for a sieve: it allows local bad sets of order-one size.

---

### 2. Every finite local sieve leaves arbitrarily large multiplicative intervals

This is the strongest unconditional structural result obtained from Route 2.

#### Theorem 2: Robust simultaneous finite-prime avoidance

Let \(P\) be any finite set of primes. There exist arbitrarily large real numbers \(T\) such that every integer \(n\) satisfying

\[
e^T2^{1/4}\le n\le e^T2^{3/4}
\tag{2}
\]

has

\[
d_p(n)=1
\qquad\text{for every }p\in P.
\tag{3}
\]

Consequently, no prime in \(P\) divides \(g_n\) for any such \(n\).

In particular, every finite collection \(\bigcup_{p\in P}\mathcal B_p\) has arbitrarily large complementary intervals containing a positive proportion

\[
1-\frac1{\sqrt2}
\]

of all integers up to the right endpoint.

**Proof.**
The prime \(2\) can be omitted because \(S_2=\varnothing\). Suppose therefore that every \(p\in P\) is odd. Put

\[
b=\log 2,\qquad z=\max P,\qquad r=|P|.
\]

Fix an arbitrarily large \(R\ge1\), and define

\[
\eta=\frac{b}{4\log z}.
\]

Choose an integer

\[
Q\ge \frac{2(R+1)}{\eta}.
\]

By simultaneous Dirichlet approximation, applied to the \(r\) real numbers \(1/\log p\), there is an integer \(q\), \(1\le q\le Q^r\), such that

\[
\left\|\frac q{\log p}\right\|\le \frac1Q
\qquad(p\in P),
\tag{4}
\]

where \(\|x\|\) denotes distance to the nearest integer.

If \(q\ge R\), set \(T=q\). If \(q<R\), set

\[
m=\left\lceil\frac Rq\right\rceil,\qquad T=mq.
\]

Then \(T\ge R\). Moreover, using \(\|mx\|\le m\|x\|\), when \(q<R\) we have

\[
\left\|\frac T{\log p}\right\|
\le m\left\|\frac q{\log p}\right\|
\le \left(\frac Rq+1\right)\frac1Q
\le \frac{R+1}{Q}
\le \frac{\eta}{2}.
\]

When \(q\ge R\), the stronger bound \(1/Q\le\eta/(2(R+1))\) holds. Thus, in either case,

\[
\left\|\frac T{\log p}\right\|\le \frac{\eta}{2}.
\]

For each \(p\in P\), there is therefore an integer \(k_p\) such that

\[
|T-k_p\log p|
\le \frac{\eta\log p}{2}
\le \frac{\eta\log z}{2}
=\frac b8.
\tag{5}
\]

Now let

\[
T+\frac b4\le t\le T+\frac{3b}{4}.
\]

By (5),

\[
\frac b8
\le t-k_p\log p
\le \frac{7b}{8}.
\]

Since \(p\ge3\), we have \(b=\log2<\log p\). Hence

\[
0<t-k_p\log p<\log2.
\]

Exponentiating gives

\[
1<\frac{e^t}{p^{k_p}}<2.
\]

Thus the leading base-\(p\) digit of \(e^t\), and hence of every integer \(n=e^t\) in the stated logarithmic interval, is \(1\). This proves (3).

Because \(1\notin S_p\), equation (1) shows that no \(p\in P\) divides \(g_n\).

Finally, the interval in (2) has length

\[
e^T\bigl(2^{3/4}-2^{1/4}\bigr)\to\infty,
\]

so it contains integers for all sufficiently large \(T\). Its length divided by its right endpoint tends to

\[
1-\frac{2^{1/4}}{2^{3/4}}
=1-\frac1{\sqrt2}.
\]

Since \(R\) was arbitrary, such intervals occur arbitrarily far out. ∎

A quantitative bound implicit in the proof is

\[
R\le T\le R+
\left\lceil\frac{8(R+1)\log z}{\log2}\right\rceil^{|P|}.
\tag{6}
\]

This bound is enormous when \(P\) contains all primes up to \(z\), but it is completely unconditional.

#### Consequence for Route 2

No finite set of primes can produce an eventual covering. More strongly, after sieving by any fixed finite set of primes, the survivor set repeatedly contains intervals of length comparable to their location.

This also demonstrates that the local events can have extremely strong positive correlations on selected scales. A conventional product-of-local-densities model cannot hold uniformly in the upper endpoint.

---

### 3. Ordinary natural densities already fail for one prime

A standard combinatorial or Selberg sieve normally starts from stable local densities. Those do not exist here in ordinary counting.

#### Proposition 3: \(\mathcal B_3\) has no natural density

Since \(S_3=\{2\}\),

\[
\mathcal B_3
=
\bigcup_{e\ge1}[2\cdot3^e,3^{e+1})\cap\mathbb Z.
\]

For

\[
x_E=2\cdot3^E-1,
\]

only the intervals with \(1\le e\le E-1\) have been completed. Hence

\[
\#(\mathcal B_3\cap[1,x_E])
=\sum_{e=1}^{E-1}3^e
=\frac{3^E-3}{2},
\]

and therefore

\[
\lim_{E\to\infty}
\frac{\#(\mathcal B_3\cap[1,x_E])}{x_E}
=\frac14.
\]

On the other hand, for

\[
y_E=3^{E+1}-1,
\]

the intervals through \(e=E\) have been completed, so

\[
\#(\mathcal B_3\cap[1,y_E])
=\sum_{e=1}^{E}3^e
=\frac{3^{E+1}-3}{2},
\]

and

\[
\lim_{E\to\infty}
\frac{\#(\mathcal B_3\cap[1,y_E])}{y_E}
=\frac12.
\]

Thus the natural density does not exist. ∎

Therefore an estimate of the form

\[
\#\{n\le x:n\in\mathcal B_p\}
=x\delta_p+o(x)
\]

with a fixed \(\delta_p\) is false even for \(p=3\). Any genuine sieve must either be phase-dependent in \(x\), work on logarithmic averages, or use carefully chosen multiplicative ranges.

---

### 4. Logarithmic densities and unconditional pairwise independence

On logarithmic time \(t=\log n\), the event attached to a fixed prime is periodic.

Define the periodic subset of \(\mathbb R\)

\[
A_p
=
\bigcup_{k\in\mathbb Z}
\bigcup_{d\in S_p}
[k\log p+\log d,\;k\log p+\log(d+1)).
\]

Apart from the irrelevant initial range \(n<p\),

\[
\log n\in A_p
\quad\Longleftrightarrow\quad
n\in\mathcal B_p.
\]

Let

\[
W_p=\sum_{d\in S_p}\log\left(1+\frac1d\right),
\qquad
\rho_p=\frac{W_p}{\log p}.
\tag{7}
\]

Then \(\rho_p\) is the time proportion occupied by \(A_p\) in one period.

#### Proposition 4: Exact one- and two-prime logarithmic densities

For distinct primes \(p\ne q\),

\[
\lim_{T\to\infty}\frac1T
\operatorname{meas}(A_p\cap[0,T])
=\rho_p
\tag{8}
\]

and

\[
\lim_{T\to\infty}\frac1T
\operatorname{meas}(A_p\cap A_q\cap[0,T])
=\rho_p\rho_q.
\tag{9}
\]

The same formulas hold for logarithmically weighted integers:

\[
\lim_{X\to\infty}
\frac1{\log X}
\sum_{\substack{n\le X\\n\in\mathcal B_p}}\frac1n
=\rho_p,
\tag{10}
\]

and

\[
\lim_{X\to\infty}
\frac1{\log X}
\sum_{\substack{n\le X\\n\in\mathcal B_p\cap\mathcal B_q}}\frac1n
=\rho_p\rho_q.
\tag{11}
\]

**Proof.**
Equation (8) follows immediately from periodicity: the bad subintervals in one period have total length \(W_p\).

For (9), consider the linear flow

\[
t\longmapsto
\left(\frac t{\log p},\frac t{\log q}\right)\pmod1.
\]

By the Weyl criterion, this flow is equidistributed on the two-dimensional torus provided

\[
\frac m{\log p}+\frac n{\log q}\ne0
\]

for every nonzero \((m,n)\in\mathbb Z^2\). If such a relation existed with \(mn\ne0\), then

\[
\frac{\log p}{\log q}=-\frac mn\in\mathbb Q.
\]

Writing this positive rational number as \(a/b\) would give \(p^b=q^a\), contrary to unique factorization. The cases \(m=0\) or \(n=0\) are immediate. Thus the flow is equidistributed.

The indicator functions of the relevant unions of intervals are Riemann integrable on the torus, so their joint time average is the product of their measures. This proves (9).

For (10) and (11), substitute \(u=e^t\), so \(dt=du/u\). On every interval \([a,b)\) in logarithmic coordinates,

\[
\sum_{e^a\le n<e^b}\frac1n
=(b-a)+O(e^{-a})
\]

by the integral test. For a fixed finite collection of primes, the number of interval endpoints in each unit interval of \(t\) is bounded. Summing the errors \(O(e^{-a})\) over all components therefore gives \(O(1)\). Dividing by \(\log X\) transfers (8) and (9) to (10) and (11). ∎

#### Why this does not give a lower-bound sieve

For three or more primes \(p_1,\dots,p_r\), full torus equidistribution would follow from

\[
\sum_{j=1}^r\frac{m_j}{\log p_j}\ne0
\qquad
\text{for every nonzero }(m_1,\dots,m_r)\in\mathbb Z^r.
\tag{12}
\]

For \(r=2\), (12) follows from unique factorization. For general \(r\), it is precisely the unproved reciprocal-logarithm independence highlighted in the brief.

Even qualitative validity of (12) for every fixed set would not suffice for a growing-dimensional sieve. One would also need discrepancy estimates depending effectively on \(r\), which in Fourier analysis require quantitative lower bounds for

\[
\left|\sum_{j=1}^r\frac{m_j}{\log p_j}\right|.
\tag{13}
\]

No such bounds are presently available in the necessary range.

Pairwise independence alone cannot give a lower bound for the probability of avoiding all events. Abstractly, pairwise independent events can have empty total complement.

---

### 5. Exact arithmetic description of large-prime witnesses

Let

\[
H_d=\frac{U_d}{V_d}
\]

be in lowest terms.

#### Lemma 5: Witnesses above \(\sqrt n\)

If \(p>\sqrt n\) and \(p\mid g_n\), then

\[
e_p(n)=1,\qquad d=\left\lfloor\frac np\right\rfloor\ge2,
\qquad p\mid U_d.
\tag{14}
\]

Conversely, if \(p>\sqrt n\), \(d=\lfloor n/p\rfloor\), and \(p\mid U_d\), then \(p\mid g_n\).

**Proof.**
The inequality \(p>\sqrt n\) gives \(p^2>n\), hence \(e_p(n)=1\). Therefore \(d_p(n)=\lfloor n/p\rfloor\). The equivalence now follows directly from (1). Since \(1\notin S_p\), a witness must have \(d\ge2\). ∎

Thus the high-prime part of the sieve can be reversed: instead of first fixing \(p\), one fixes \(d\) and considers the prime divisors of \(U_d\).

#### Lemma 6: A universal upper cutoff for prime witnesses

For all sufficiently large \(n\), every prime \(p\mid g_n\) satisfies

\[
p\le
4\,\frac{n\log\log n}{\log n}.
\tag{15}
\]

**Proof.**
If \(p\le\sqrt n\), then (15) holds for all sufficiently large \(n\).

Suppose \(p>\sqrt n\). By Lemma 5, \(p\mid U_d\), where \(d=\lfloor n/p\rfloor\ge2\).

Because \(V_d\mid\operatorname{lcm}(1,\dots,d)\mid d!\),

\[
U_d=H_dV_d\le H_d\,d!.
\]

The crude bounds \(H_d\le d\) and \(d!\le d^d\) give

\[
U_d\le d^{d+1}.
\]

Since \(p\mid U_d\) and \(U_d>0\),

\[
\log p\le(d+1)\log d\le2d\log d.
\tag{16}
\]

Put \(L=\log n\) and \(\ell=\log L\). Since \(p>\sqrt n\),

\[
\log p>\frac L2.
\]

Combining this with (16),

\[
d\log d>\frac L4.
\tag{17}
\]

If \(d<L/(4\ell)\), then \(d<L\), so \(\log d<\ell\), and consequently

\[
d\log d<\frac{L}{4\ell}\ell=\frac L4,
\]

contradicting (17). Hence

\[
d\ge\frac{L}{4\ell}.
\]

Since \(d=\lfloor n/p\rfloor\le n/p\),

\[
p\le\frac nd
\le4\,\frac{n\ell}{L}.
\]

This proves (15). ∎

The bound is only a modest reduction: the sieve level is still nearly linear in \(n\).

A fixed-relative-range consequence is cleaner.

#### Corollary 7: Fixed top ranges are eventually witness-free

Fix \(D\ge1\). Then, for all sufficiently large \(n\), no witness prime satisfies

\[
p>\frac{n}{D+1}.
\]

**Proof.**
Let \(M_D\) be the largest prime divisor of

\[
\prod_{d=1}^D U_d,
\]

taking \(M_D=1\) if the product has no prime divisor. If

\[
n>\max\{(D+1)^2,(D+1)M_D\}
\]

and \(p>n/(D+1)\), then \(p>\sqrt n\). Lemma 5 applies, and

\[
d=\left\lfloor\frac np\right\rfloor\le D.
\]

If \(p\) were a witness, then \(p\mid U_d\), so \(p\le M_D\). But \(p>n/(D+1)>M_D\), a contradiction. ∎

This rigorously confirms that primes very close to \(n\) are harmless. It does not control primes down to \(n^\alpha\) for any fixed \(\alpha<1\).

---

### 6. Why elementary harmonic-numerator bounds do not control the tail

One might hope to sieve by primes \(p\le y\) and remove the remaining primes \(p>y\) by a union bound. The reverse description in Lemma 5 shows why the available estimates are inadequate.

Let \(x\ge1\) and \(y\ge\sqrt x\). Every bad interval below \(x\) arising from \(p>y\) has \(e=1\) and is of the form

\[
[dp,(d+1)p),\qquad
d\le\frac{x}{y},\qquad p\mid U_d.
\]

Its length is \(p\), and \(dp\le x\) implies \(p\le x/d\). The number of distinct prime divisors \(p>y\) of \(U_d\) is at most

\[
\frac{\log U_d}{\log y}
\le\frac{2d\log d}{\log y}.
\]

Therefore the union bound gives only

\[
\begin{aligned}
\#\{n\le x:\exists p>y,\ p\mid g_n\}
&\le
\sum_{2\le d\le x/y}
\sum_{\substack{p>y\\p\mid U_d\\dp\le x}}p\\
&\le
\sum_{2\le d\le x/y}
\frac{x}{d}\frac{2d\log d}{\log y}\\
&\le
\frac{2x}{\log y}
\left\lfloor\frac{x}{y}\right\rfloor
\log\left(\frac{x}{y}\right).
\tag{18}
\end{aligned}
\]

For \(y=\sqrt x\), the right side is of order \(x^{3/2}\). Even for

\[
y=\frac{x}{\log x},
\]

it is of order \(x\log\log x\). Thus the elementary size estimate for \(U_d\) does not even produce an \(o(x)\) tail bound.

A successful implementation of Route 2 needs genuine average information about the large prime factors of the numerators \(U_d\), not merely their sizes.

---

### 7. The already-settled non-coprime half

For completeness, for every \(e\ge1\), take

\[
n=2\cdot3^e.
\]

Then \(d_3(n)=2\), and

\[
H_2=\frac32\equiv0\pmod3.
\]

By (1),

\[
3\mid g_n.
\]

Hence \(\{n:g_n>1\}\) is infinite.

The unresolved requirement remains proving infinitely many \(n\) for which no prime witnesses divisibility.

## Self-Audit

1. **Finite-prime interval theorem.**  
   The delicate point is that simultaneous approximation returns \(T/\log p\) near either side of an integer, whereas digit \(1\) requires a one-sided interval. The shift by \(\frac12\log2\), together with the explicit \(\frac18\log2\) margin, resolves both signs. The proof also checks that the shifted residues remain below \(\log2<\log p\), so there is no wraparound for odd \(p\).

2. **Large-prime cutoff.**  
   The bound \(p\ll n\log\log n/\log n\) is very coarse, and it would be easy to confuse \(U_d\) with the unreduced numerator. Here \(U_d\) is explicitly the reduced numerator. The estimate \(U_d\le H_d d!\le d^{d+1}\) follows because the reduced denominator divides \(d!\), so the argument is valid despite its weakness.

3. **Pairwise independence statement.**  
   This is only logarithmic-density independence, not ordinary natural-density independence and not mutual independence. I believe the stated result holds because the two-frequency Weyl criterion reduces exactly to irrationality of \(\log p/\log q\), which follows from unique factorization. I have not used it to infer any higher-order sieve conclusion.

## Computations To Verify

```python
from math import gcd, isqrt, log, exp, ceil, floor
from fractions import Fraction

def primes_upto(N):
    sieve = bytearray(b"\x01") * (N + 1)
    if N >= 0:
        sieve[0] = 0
    if N >= 1:
        sieve[1] = 0
    for a in range(2, isqrt(N) + 1):
        if sieve[a]:
            sieve[a*a:N+1:a] = b"\x00" * (((N - a*a)//a) + 1)
    return [p for p in range(2, N + 1) if sieve[p]]

def harmonic_zero_set(p):
    h = 0
    S = set()
    for d in range(1, p):
        h = (h + pow(d, -1, p)) % p
        if h == 0:
            S.add(d)
    return S

# Verify the listed small zero sets and the no-consecutive lemma.
for p in primes_upto(1000):
    S = harmonic_zero_set(p)
    assert all(d + 1 not in S for d in S)
    if p > 2:
        assert p - 1 in S
    for d in S:
        if d <= p - 2:
            assert p - 1 - d in S

assert harmonic_zero_set(2) == set()
assert harmonic_zero_set(3) == {2}
assert harmonic_zero_set(5) == {4}
assert harmonic_zero_set(7) == {6}
assert harmonic_zero_set(11) == {3, 7, 10}
```

An interval sieve verifying the local criterion:

```python
def interval_sieve(X):
    bad = [False] * (X + 1)
    witness = [None] * (X + 1)

    for p in primes_upto(X):
        S = harmonic_zero_set(p)
        q = p
        while q <= X:
            for d in S:
                lo = d * q
                if lo > X:
                    continue
                hi = min((d + 1) * q - 1, X)
                for n in range(lo, hi + 1):
                    bad[n] = True
                    if witness[n] is None:
                        witness[n] = p
            if q > X // p:
                break
            q *= p

    return bad, witness

bad, witness = interval_sieve(10000)
assert not bad[1]
assert not bad[2]
assert not bad[3]
assert not bad[4]
assert not bad[5]
assert bad[6] and witness[6] == 3
assert not bad[9]
```

Directly test the large-prime description:

```python
def leading_digit(n, p):
    q = p
    while q <= n // p:
        q *= p
    return n // q

def witness_primes(n, primes, S_cache):
    out = []
    for p in primes:
        if p > n:
            break
        d = leading_digit(n, p)
        if d in S_cache[p]:
            out.append(p)
    return out

X = 20000
P = primes_upto(X)
S_cache = {p: harmonic_zero_set(p) for p in P}

H = Fraction(0, 1)
harmonic_numerators = [1] * (isqrt(X) + 2)
for d in range(1, len(harmonic_numerators)):
    H += Fraction(1, d)
    harmonic_numerators[d] = H.numerator

for n in range(2, X + 1):
    for p in witness_primes(n, P, S_cache):
        if p > isqrt(n):
            d = n // p
            assert harmonic_numerators[d] % p == 0
```

Check the cutoff numerically:

```python
for n in range(100, X + 1):
    W = witness_primes(n, P, S_cache)
    if W and log(log(n)) > 0:
        largest = max(W)
        bound = 4 * n * log(log(n)) / log(n)
        if n >= 1000:
            assert largest <= bound + 1e-12
```

Search for the simultaneous-return intervals in Theorem 2:

```python
def circ_dist(x, period):
    r = x % period
    return min(r, period - r)

def find_finite_prime_safe_interval(P, start, stop):
    b = log(2)
    for T in range(start, stop + 1):
        if all(circ_dist(T, log(p)) <= b/8 for p in P if p > 2):
            lo = ceil(exp(T + b/4))
            hi = floor(exp(T + 3*b/4))
            return T, lo, hi
    return None

def check_digit_one_interval(P, lo, hi, sample_cap=100000):
    if hi - lo <= sample_cap:
        samples = range(lo, hi + 1)
    else:
        step = max(1, (hi - lo) // sample_cap)
        samples = range(lo, hi + 1, step)
    for n in samples:
        for p in P:
            if p <= n and p > 2:
                assert leading_digit(n, p) == 1

ans = find_finite_prime_safe_interval([3, 5, 7, 11], 1, 10_000_000)
if ans:
    T, lo, hi = ans
    check_digit_one_interval([3, 5, 7, 11], lo, hi)
    print(T, lo, hi, (hi - lo) / hi)
```

Test logarithmic pair correlations:

```python
def bad_at_log_time(t, p, S):
    r = t % log(p)
    d = int(exp(r))   # away from boundaries
    return d in S

def log_time_correlation(p, q, T=100000.0, steps=5_000_000):
    Sp = harmonic_zero_set(p)
    Sq = harmonic_zero_set(q)
    cp = cq = cpq = 0
    for k in range(steps):
        t = (k + 0.5) * T / steps
        bp = bad_at_log_time(t, p, Sp)
        bq = bad_at_log_time(t, q, Sq)
        cp += bp
        cq += bq
        cpq += bp and bq
    mp = cp / steps
    mq = cq / steps
    joint = cpq / steps
    return mp, mq, joint, mp * mq

print(log_time_correlation(3, 5))
print(log_time_correlation(3, 11))
print(log_time_correlation(5, 11))
```

Finally, the failure of natural density for \(\mathcal B_3\) can be checked exactly:

```python
for E in range(2, 20):
    x = 2 * 3**E - 1
    count_x = (3**E - 3) // 2
    y = 3**(E + 1) - 1
    count_y = (3**(E + 1) - 3) // 2
    print(E, count_x / x, count_y / y)
# The columns approach 1/4 and 1/2.
```

## Route Diagnosis

**Proved ledger**

1. No two consecutive elements occur in \(S_p\).
2. Every finite prime sieve has arbitrarily large complementary intervals of fixed multiplicative ratio \(\sqrt2\).
3. The ordinary local density does not exist even for \(p=3\).
4. Fixed-prime events have exact logarithmic densities \(\rho_p\).
5. Distinct-prime events are pairwise independent in logarithmic density.
6. Witnesses above \(\sqrt n\) correspond exactly to prime divisors \(p\mid U_{\lfloor n/p\rfloor}\).
7. Every witness satisfies \(p\ll n\log\log n/\log n\).
8. Elementary numerator-size estimates do not give a useful tail union bound.

**Plausible but unproved claims needed by Route 2**

- An average estimate of sieve dimension one, morally
  \[
  \rho_p\asymp\frac1p
  \quad\text{on average over }p,
  \]
  with control of primes having exceptional small digits in \(S_p\).
- Uniform joint-count or discrepancy estimates for prime sets whose size grows with the sieve level.
- A large-prime tail theorem substantially stronger than (18), likely requiring average control of prime divisors \(p>d\) of \(U_d\).
- A lower-bound sieve robust under the strong scale-dependent correlations demonstrated by Theorem 2.

**Dead ends**

1. A standard natural-density sieve is impossible without reformulation: \(\mathcal B_3\) itself has no natural density.
2. Pairwise equidistribution is insufficient for a lower-bound sieve; higher intersections encounter the unproved relations (12).
3. Finite-prime recurrence cannot be naively diagonalized. Making all primes \(p\le z\) safe may place the resulting interval at roughly doubly exponential height in \(z\), while relevant witnesses extend nearly up to \(n\).
4. Reversing the tail through \(p\mid U_d\) is structurally exact but quantitatively blocked: the bound \(\log U_d=O(d\log d)\) permits far too many large prime factors for a useful union estimate.

A fresh attempt should pursue a hybrid of Routes 1 and 2: prove an average theorem for the large prime divisors of the harmonic numerators \(U_d\), weighted according to intervals \(dp\le n<(d+1)p\), and combine it with a phase-dependent logarithmic sieve rather than a fixed-density sieve. Without such new arithmetic input, Route 2 remains blocked rather than merely technically incomplete.