STATUS: BLOCKED

## Result

Route 3 yields a rigorous and fairly strong tail theorem: for \(H_X=\sum_{p\le 2X}1/p\), the number of \(n\in[X,2X]\) having any violating offset \(j\ge R\) is at most
\[
4X\left(\frac{eH_X}{R+1}\right)^{R+1}
\qquad(R+1\ge 2H_X).
\]
Consequently, almost every endpoint \(n=q+1\) with \(q\) prime satisfies all barrier inequalities for \(j\ge 4\log\log X+O(1)\). I also give an exact completion criterion reducing the problem to a joint lower-tail estimate in a growing initial window, and an exact joint factorial-moment identity exposing the correlations among shifts. However, this does not solve the problem: the required lower bound is already blocked at the necessary two-offset condition that infinitely many prime powers \(q\) satisfy \(\omega(q-1)\le2\). A Zsigmondy argument sharply restricts possible exponents of such prime powers but leaves unresolved prime and Mersenne/Fermat-type families. Thus Route 3 is genuinely blocked by a lower-bound/parity problem, not by the large-offset tail.

## Complete Argument

### 1. A uniform large-deviation bound for late offsets

Put
\[
H(y)=\sum_{p\le y}\frac1p.
\]

#### Lemma 1: factorial-moment bound

For every real \(y\ge2\) and integer \(k\ge1\),
\[
\#\{m\le y:\omega(m)\ge k\}
\le
y\frac{H(y)^k}{k!}.
\]

#### Proof

For each \(m\),
\[
\mathbf 1_{\{\omega(m)\ge k\}}
\le \binom{\omega(m)}k.
\]
Moreover,
\[
\binom{\omega(m)}k
=
\sum_{\substack{d\mid m\\ d\ \mathrm{squarefree}\\ \omega(d)=k}}1.
\]
Therefore
\[
\begin{aligned}
\sum_{m\le y}\binom{\omega(m)}k
&=
\sum_{\substack{d\le y\\ d\ \mathrm{squarefree}\\ \omega(d)=k}}
\left\lfloor\frac yd\right\rfloor\\
&\le
y\sum_{\substack{d\le y\\ d\ \mathrm{squarefree}\\ \omega(d)=k}}\frac1d\\
&\le
\frac{y}{k!}\left(\sum_{p\le y}\frac1p\right)^k.
\end{aligned}
\]
The last inequality follows by expanding \(H(y)^k\): every product of \(k\) distinct primes occurs \(k!\) times, while terms involving repeated primes are nonnegative. ∎

Define the late-exceptional set
\[
\mathcal L_R(X)=
\left\{
n\in[X,2X]\cap\mathbb N:
\exists j,\ R\le j\le n-1,\ 
\omega(n-j)\ge j+1
\right\}.
\]

#### Theorem 2: late-offset tail estimate

Let
\[
H_X=H(2X).
\]
If \(R+1\ge2H_X\), then
\[
\boxed{
\#\mathcal L_R(X)
\le
4X\left(\frac{eH_X}{R+1}\right)^{R+1}.
}
\]

#### Proof

For a fixed \(j\), the map \(n\mapsto m=n-j\) is injective. Hence, by a union bound and Lemma 1,
\[
\begin{aligned}
\#\mathcal L_R(X)
&\le
\sum_{j=R}^{2X-1}
\#\{m\le2X:\omega(m)\ge j+1\}\\
&\le
2X\sum_{k=R+1}^{\infty}\frac{H_X^k}{k!}.
\end{aligned}
\]
Let \(k_0=R+1\). Since \(k_0\ge2H_X\), successive terms satisfy
\[
\frac{H_X^{k+1}/(k+1)!}{H_X^k/k!}
=\frac{H_X}{k+1}\le\frac12
\qquad(k\ge k_0).
\]
Thus
\[
\sum_{k=k_0}^{\infty}\frac{H_X^k}{k!}
\le 2\frac{H_X^{k_0}}{k_0!}.
\]
Using \(k_0!\ge(k_0/e)^{k_0}\),
\[
\#\mathcal L_R(X)
\le
4X\frac{H_X^{k_0}}{k_0!}
\le
4X\left(\frac{eH_X}{k_0}\right)^{k_0}.
\]
This is the claimed estimate. ∎

By Mertens’ theorem for reciprocal primes,
\[
H_X=\log\log X+O(1).
\]

#### Corollary 3

For fixed \(c>e\), let \(R=\lceil cH_X\rceil\). Then
\[
\#\mathcal L_R(X)
\ll_c
\frac{X}{(\log X)^{\beta(c)}},
\qquad
\beta(c)=c\log(c/e).
\]

Indeed,
\[
\left(\frac{eH_X}{R+1}\right)^{R+1}
\le
\exp\!\left(-(\beta(c)+o(1))H_X\right)
\asymp_c
(\log X)^{-\beta(c)}.
\]

For \(c=4\),
\[
\beta(4)=4\log(4/e)>1.
\]
The prime number theorem gives
\[
\#\{n\in[X,2X]:n-1\text{ is prime}\}
\sim\frac{X}{\log X}.
\]
It follows that, among such prime endpoints,
\[
\frac{
\#\{n:n-1\text{ prime and }n\in\mathcal L_{\lceil4H_X\rceil}(X)\}
}{
\#\{n\in[X,2X]:n-1\text{ prime}\}
}
\longrightarrow0.
\]

Thus:

\[
\boxed{
\text{For almost every prime }q\in[X,2X],\ n=q+1
\text{ satisfies }\omega(n-j)\le j
\text{ for every }j\ge4\log\log X+O(1).
}
\]

This is an unconditional Route 3 conclusion. It does not control the rare simultaneous lower-tail pattern in the first \(O(\log\log X)\) shifts.

---

### 2. Exact completion criterion

Let
\[
\mathcal C_R(X)=
\left\{
n\in[X,2X]:
\omega(n-j)\le j\quad(1\le j<R)
\right\}.
\]

Every \(n\in\mathcal C_R(X)\setminus\mathcal L_R(X)\) is a barrier: the defining inequalities hold for \(j<R\) by membership in \(\mathcal C_R(X)\), and for \(j\ge R\) by exclusion from \(\mathcal L_R(X)\). Therefore

\[
\boxed{
\#(\mathcal B_1\cap[X,2X])
\ge
\#\mathcal C_R(X)
-
4X\left(\frac{eH_X}{R+1}\right)^{R+1}.
}
\]

This makes the precise missing Route 3 lemma explicit.

There are two useful regimes.

#### Polynomial-scale regime

If for some fixed \(A\) and some \(c>e\) satisfying
\[
c\log(c/e)>A
\]
one could prove
\[
\#\mathcal C_{\lceil cH_X\rceil}(X)
\gg \frac{X}{(\log X)^A},
\]
then the tail error would be smaller and barriers would exist in all sufficiently large dyadic intervals.

Unfortunately, the simultaneous early pattern is heuristically much rarer than any fixed power of \(1/\log X\).

#### Large-deviation-scale regime

Let \(H=H_X\), and take
\[
R+1=
\left\lceil
D\frac{H^2}{\log H}
\right\rceil
\]
for fixed \(D>0\). Then
\[
\begin{aligned}
(R+1)\log\frac{R+1}{eH}
&=
\left(D+o(1)\right)H^2,
\end{aligned}
\]
and hence
\[
\#\mathcal L_R(X)
\le
X\exp\left(-(D+o(1))H^2\right).
\]

Consequently, if one could prove, for constants \(0\le\kappa<D\),
\[
\#\mathcal C_R(X)
\ge
X\exp\left(-(\kappa+o(1))H^2\right),
\]
then infinitely many barriers would follow.

This is a rigorous sufficient target for Route 3. The unproved part is precisely the lower bound for the joint lower-tail event.

---

### 3. Exact joint factorial-moment identity

The dependence among consecutive values of \(\omega\) can be written exactly.

Let \(h_1,\dots,h_s\) be distinct integers and \(r_1,\dots,r_s\ge0\). Let \(I\) be a finite interval on which every \(n-h_i\) is positive. Then
\[
\begin{aligned}
&\sum_{n\in I}
\prod_{i=1}^s
\binom{\omega(n-h_i)}{r_i}\\
&\quad=
\sum_{\substack{
d_i\ \mathrm{squarefree}\\
\omega(d_i)=r_i}}
N_I(d_1,\dots,d_s),
\end{aligned}
\]
where \(N_I(d_1,\dots,d_s)\) is the number of \(n\in I\) satisfying
\[
n\equiv h_i\pmod{d_i}\qquad(1\le i\le s).
\]

By the generalized Chinese remainder theorem, this system is soluble exactly when
\[
\gcd(d_i,d_\ell)\mid h_i-h_\ell
\qquad(1\le i,\ell\le s).
\]
When soluble,
\[
N_I(d_1,\dots,d_s)
=
\frac{|I|}{[d_1,\dots,d_s]}+O(1).
\]

The identity follows by expanding
\[
\binom{\omega(n-h_i)}{r_i}
=
\sum_{\substack{d_i\mid n-h_i\\d_i\text{ squarefree}\\\omega(d_i)=r_i}}1
\]
and interchanging the finite sums.

This identity makes the principal correlation explicit: the same small prime may occur in two shifted values only when it divides the difference of the shifts. It is suitable for joint upper moments, but it does not itself give a lower bound for simultaneous events
\[
\omega(n-j)\le j.
\]
Obtaining such a lower bound requires retaining mass after a lower-bound sieve, where the parity obstruction enters immediately.

---

### 4. The unavoidable first-two-offset obstruction

If \(n>2\) is a barrier, then the \(j=1\) inequality gives
\[
\omega(n-1)\le1.
\]
Thus
\[
q=n-1=p^a
\]
is a prime power. The \(j=2\) inequality then gives
\[
\omega(q-1)\le2.
\]

Therefore an affirmative solution necessarily proves:

\[
\boxed{
\text{There are infinitely many prime powers }q
\text{ such that }\omega(q-1)\le2.
}
\]

For the prime subfamily \(q=p\), every odd candidate has
\[
p-1=2^u
\quad\text{or}\quad
p-1=2^u\ell^v
\]
for an odd prime \(\ell\). Thus Route 3, when conditioned on \(n-1\) being prime, already needs infinitely many primes of the form
\[
p=1+2^u\ell^v.
\]
No lower bound for this union is obtained by the factorial-moment method above. Restricting to \(u=v=1\) gives the safe-prime/Sophie-Germain type pattern \(p=2\ell+1\), illustrating the parity difficulty, although the full union is broader and is not equivalent to that conjecture.

---

### 5. Zsigmondy restriction on higher prime powers

The higher-power alternatives do not obviously evade the bottleneck.

I use the classical Bang–Zsigmondy theorem:

> If \(A>B>0\) are coprime and \(d>1\), then \(A^d-B^d\) has a prime divisor that divides no \(A^k-B^k\) with \(1\le k<d\), except when \(d=2\) and \(A+B\) is a power of \(2\), or when \((A,B,d)=(2,1,6)\).

Such a divisor of \(p^d-1\) is called primitive for exponent \(d\). Primitive divisors associated with distinct exponents are distinct.

#### Proposition 4

Suppose \(q=p^a\) is a prime power and
\[
\omega(p^a-1)\le2.
\]

1. If \(p\) is odd, then
   \[
   a=1,\qquad a\text{ is prime},\qquad\text{or}\qquad a=4.
   \]
   In the last case necessarily \(p=3\).

2. If \(p=2\), then
   \[
   a=1,\qquad a=\ell,\qquad a=\ell^2
   \quad(\ell\text{ prime}),\qquad\text{or}\qquad a=6.
   \]

#### Proof for odd \(p\)

The prime \(2\) already divides \(p-1\). For every divisor \(d>1\) of \(a\), Zsigmondy supplies a primitive divisor of \(p^d-1\), except possibly for \(d=2\) when \(p+1\) is a power of \(2\).

Primitive divisors for distinct \(d\) are distinct, and none divides \(p-1\). Since \(p^a-1\) has at most two distinct prime divisors total, there can be at most one nonexceptional divisor \(d>1\) of \(a\).

If the \(d=2\) exception is unavailable, this gives
\[
\tau(a)-1\le1,
\]
so \(a=1\) or \(a\) is prime.

If \(2\mid a\) and \(p+1\) is a power of \(2\), the divisor \(d=2\) may be omitted, giving
\[
\tau(a)-2\le1.
\]
Thus \(\tau(a)\le3\), so \(a\) is \(1\), prime, or a square of a prime. The only even composite square of a prime is \(a=4\).

Suppose \(a=4\). The exceptional \(d=2\) case must occur, so \(p+1\) is a power of \(2\). Zsigmondy at \(d=4\) gives a primitive odd prime \(\ell\mid p^4-1\). If \(p-1\) had an odd prime divisor, it would be distinct from \(\ell\), producing at least three prime divisors together with \(2\). Hence \(p-1\) is also a power of \(2\). The only two powers of \(2\) differing by \(2\) are \(2\) and \(4\), so \(p=3\). ∎

#### Proof for \(p=2\)

For every divisor \(d>1\) of \(a\), there is a primitive divisor of \(2^d-1\), except at \(d=6\). Since only two distinct prime divisors are allowed,
\[
\#\{d:d\mid a,\ d>1,\ d\ne6\}\le2.
\]

If \(6\nmid a\), this says
\[
\tau(a)-1\le2,
\]
so \(\tau(a)\le3\). Therefore \(a=1\), \(a\) is prime, or \(a\) is the square of a prime.

If \(6\mid a\), then
\[
\tau(a)-2\le2,
\]
so \(\tau(a)\le4\). A number divisible by \(6\) has at least four divisors. A number with exactly four divisors is either a prime cube or a product of two distinct primes; divisibility by \(6\) forces the latter number to be \(6\). Thus \(a=6\). ∎

For example,
\[
2^6-1=63=3^2\cdot7,\qquad
3^4-1=80=2^4\cdot5,
\]
showing that the exceptional cases genuinely occur.

This restriction is useful but not constructive. It leaves, among others, prime exponents for \(2^a-1\) and the prime case \(a=1\), so it does not resolve the necessary first-two-offset problem.

## Self-Audit

1. **The tail estimate uses a very lossy union bound.**  
   It may overcount each bad \(n\) many times and ignores correlations. This affects sharpness, not validity: every implication is in the upper-bound direction, and the factorial-moment identity is exact.

2. **The “almost every prime endpoint” conclusion does not imply that almost every endpoint satisfying the rare early conditions has a safe tail.**  
   This distinction is essential. The rare early pattern is heuristically of size about \(X\exp(-\Theta((\log\log X)^2))\), much smaller than the exceptional set furnished by the \(R\asymp\log\log X\) bound. I therefore did not use this corollary to claim barriers; the larger \(R\asymp H_X^2/\log H_X\) completion criterion addresses the scale mismatch.

3. **The exponent classification invokes Bang–Zsigmondy rather than reproving it.**  
   The theorem is classical, and its two exceptional cases have been stated explicitly. Given that theorem, the divisor-count argument and the special \(a=4\) analysis are complete. The classification is auxiliary and is not needed for the tail theorem.

## Computations To Verify

```python
from math import ceil, e, exp, log, isqrt

def omega_sieve(N):
    omega = [0] * (N + 1)
    primes = []
    for p in range(2, N + 1):
        # At this point omega[p] == 0 iff no smaller prime divides p.
        if omega[p] == 0:
            primes.append(p)
            for m in range(p, N + 1, p):
                omega[m] += 1
    is_prime = [False] * (N + 1)
    for p in primes:
        is_prime[p] = True
    return omega, primes, is_prime

def barriers_up_to(N):
    omega, primes, is_prime = omega_sieve(N)
    ans = []
    prefix_max = -10**30
    for n in range(1, N + 1):
        if prefix_max <= n:
            ans.append(n)
        prefix_max = max(prefix_max, n + omega[n])
    return ans

def tail_experiment(X, c=4.0):
    omega, primes, is_prime = omega_sieve(2 * X)
    H = sum(1.0 / p for p in primes if p <= 2 * X)
    R = ceil(c * H)
    maxw = max(omega)

    late_bad = []
    prime_endpoints = 0
    prime_endpoint_late_bad = 0

    for n in range(X, 2 * X + 1):
        bad = False

        # A violation requires j+1 <= maxw.
        for j in range(R, min(n, maxw)):
            if omega[n - j] >= j + 1:
                bad = True
                break

        if bad:
            late_bad.append(n)

        if is_prime[n - 1]:
            prime_endpoints += 1
            if bad:
                prime_endpoint_late_bad += 1

    k = R + 1
    assert k >= 2 * H
    theoretical_bound = 4 * X * (e * H / k) ** k

    return {
        "X": X,
        "H": H,
        "R": R,
        "late_bad_count": len(late_bad),
        "theoretical_bound": theoretical_bound,
        "prime_endpoints": prime_endpoints,
        "prime_endpoint_late_bad": prime_endpoint_late_bad,
        "prime_bad_ratio":
            prime_endpoint_late_bad / max(1, prime_endpoints),
    }

def is_prime_trial(a):
    if a < 2:
        return False
    for d in range(2, isqrt(a) + 1):
        if a % d == 0:
            return False
    return True

def exponent_allowed(p, a):
    if p == 2:
        square_root = isqrt(a)
        return (
            a == 1
            or is_prime_trial(a)
            or (square_root * square_root == a
                and is_prime_trial(square_root))
            or a == 6
        )
    return a == 1 or is_prime_trial(a) or a == 4

def verify_zsigmondy_classification(N):
    omega, primes, is_prime = omega_sieve(N)
    examples = []

    for p in primes:
        q = p
        a = 1
        while q <= N:
            if omega[q - 1] <= 2:
                assert exponent_allowed(p, a), (p, a, q, omega[q - 1])
                if p % 2 == 1 and a == 4:
                    assert p == 3
                examples.append((p, a, q, omega[q - 1]))
            if q > N // p:
                break
            q *= p
            a += 1

    return examples

def shifted_prime_correlation(X, J):
    """
    For prime q in [X,2X], test
        omega(q-r) <= r+1, 1 <= r <= J.
    The r=0 condition is automatic because q is prime.
    """
    omega, primes, is_prime = omega_sieve(2 * X)
    qs = [q for q in primes if X <= q <= 2 * X and q > J]

    marginal = [0] * (J + 1)
    simultaneous = 0

    for q in qs:
        all_ok = True
        for r in range(1, J + 1):
            ok = omega[q - r] <= r + 1
            marginal[r] += int(ok)
            all_ok &= ok
        simultaneous += int(all_ok)

    N = len(qs)
    product_model = 1.0
    for r in range(1, J + 1):
        product_model *= marginal[r] / max(1, N)

    expected_independent = N * product_model
    correlation_ratio = (
        simultaneous / expected_independent
        if expected_independent > 0 else float("inf")
    )

    return {
        "prime_count": N,
        "simultaneous": simultaneous,
        "marginal_counts": marginal[1:],
        "independence_prediction": expected_independent,
        "correlation_ratio": correlation_ratio,
    }

# Checksums:
# print(barriers_up_to(20))
# Expected prefix:
# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 17, ...]
#
# print(tail_experiment(10**5, 4.0))
# print(verify_zsigmondy_classification(10**6))
# for J in range(1, 15):
#     print(J, shifted_prime_correlation(10**6, J))
```

The most informative empirical test for Route 3 is the last one: record how the ratio between the true simultaneous count and the product of measured marginals behaves as \(J\) grows. A rapidly vanishing ratio would quantitatively confirm that naive independence is unusable.

## Route Diagnosis

### Proved ledger

- A uniform factorial-moment upper bound for \(\omega\).
- A quantitative bound
  \[
  \#\mathcal L_R(X)
  \le4X\left(\frac{eH_X}{R+1}\right)^{R+1}
  \]
  for all late violations.
- Almost all prime endpoints pass every offset beyond \(4\log\log X+O(1)\).
- An exact completion inequality reducing barriers to an initial-window lower bound.
- An exact joint factorial-moment/CRT identity for shifted values of \(\omega\).
- Zsigmondy-based restrictions on exponents of prime powers satisfying the necessary second condition.

### Plausible but unproved

A Poisson lower-tail model suggests that the first \(H_X\) or so shifts impose a total cost of order
\[
\exp\bigl(-\kappa H_X^2\bigr).
\]
In the naive independent Poisson model,
\[
\kappa=\int_0^1(1-t+t\log t)\,dt=\frac14,
\]
but small-prime correlations can alter this constant. A lower bound of this scale, uniform for a growing family of shifts and surviving the prime-power condition on \(n-1\), would be the decisive new theorem.

### Dead ends

1. **Subtracting the \(R\asymp\log\log X\) tail from a heuristic early-pattern count.**  
   This fails quantitatively:
   \[
   X e^{-\Theta(H_X^2)}
   \ll
   X e^{-\beta H_X}.
   \]
   The unconditional exceptional set may contain every rare early-pattern candidate.

2. **Using joint factorial moments alone.**  
   They give useful upper bounds and encode correlations, but do not retain positive mass in the simultaneous lower tail. The needed conclusion is a lower-bound sieve statement.

3. **Escaping through higher prime powers.**  
   Zsigmondy sharply restricts their exponents, but leaves prime, prime-exponent Mersenne-type, and Fermat-type possibilities. It does not produce an infinite family.

### Precise block

Route 3 now reduces to proving a growing-dimensional lower bound for
\[
\omega(n-j)\le j\qquad(1\le j<R(X)),
\]
with \(n-1\) a prime power. Before any growing-dimensional issue, this entails proving infinitely many prime powers \(q\) with
\[
\omega(q-1)\le2.
\]
For prime \(q\), this is already a lower-bound sieve problem for primes
\[
q=1+2^u\ell^v.
\]
The available moment method has no mechanism to overcome this parity-sensitive lower-bound obstruction.

A fresh attempt should therefore pursue one of two genuinely new ingredients:

1. a lower-bound sieve specifically exploiting the union over the variable exponents \(u,v\), rather than fixing a Sophie-Germain-type form; or
2. a conditional-tail theorem relative to the rare early pattern, strong enough to replace the absolute union bound and reduce the required growing window from \(H_X^2/\log H_X\) back to \(O(H_X)\).

Without such an ingredient, Route 3 is blocked.