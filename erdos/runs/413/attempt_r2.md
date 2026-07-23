STATUS: BLOCKED

## Result

Route 2 encounters a genuine lower-bound sieve obstruction at its first nontrivial condition. In the prime branch \(n=q+1\), the requirement \(\omega(q-1)\le2\) says exactly that \(q-1=2^a\ell^b\) for some odd prime \(\ell\), allowing \(\ell\) to be absent. The stronger proposed target using \(\Omega\) would already imply infinitely many Sophie Germain primes and is therefore unusable unconditionally. I prove three additional reductions: nontrivial odd prime powers \(\ell^b\), \(b\ge2\), form a quantitatively sparse escape from the parity problem; Bang–Zsigmondy theory sharply restricts the possible exponents when \(q\) is a higher prime power; and all offsets beyond \(A\log\log x\) fail for only \(O_D(x/\log^D x)\) endpoints. The remaining block is a lower bound for the simultaneous early-offset conditions, already unknown for the first two offsets.

## Complete Argument

### 1. The first lower-bound sieve bottleneck

Let \(n>2\) be a barrier and put \(q=n-1\). The \(j=1\) condition gives
\[
\omega(q)\le1,
\]
so \(q=P^a\) for some prime \(P\) and integer \(a\ge1\).

Consider first the prime branch \(a=1\), so \(q\) is prime. Apart from the isolated case \(q=2\), it is odd. The \(j=2\) condition is
\[
\omega(q-1)\le2.
\]

#### Lemma 1

For an odd prime \(q\),
\[
\omega(q-1)\le2
\]
if and only if
\[
q-1=2^a
\quad\text{or}\quad
q-1=2^a\ell^b
\]
for some \(a,b\ge1\) and some odd prime \(\ell\).

#### Proof

Write
\[
q-1=2^a u,\qquad u\ \text{odd},\quad a\ge1.
\]
Since \(2\mid q-1\), at most one odd prime may divide \(u\). Hence either \(u=1\), or \(u\) is a power \(\ell^b\) of one odd prime. The converse is immediate. ∎

Thus even the first two offsets in the prime branch require infinitely many primes of the form
\[
q=1+2^a\ell^b.
\]

This is not a usual “\(P_2\)” condition: multiplicities are unrestricted, but the set of permitted prime species is extremely small.

---

### 2. Why replacing \(\omega\) by \(\Omega\) does not help

The brief suggests the stronger sufficient target
\[
\Omega(q-r)\le r+1.
\]
At the first nontrivial shift \(r=1\), this becomes
\[
\Omega(q-1)\le2.
\]

#### Lemma 2

For an odd prime \(q\), the condition \(\Omega(q-1)\le2\) implies that
\[
q\in\{3,5\}
\]
or
\[
q=2\ell+1
\]
where \(\ell\) and \(q\) are both prime. Consequently, infinitely many such \(q\) are equivalent to infinitely many Sophie Germain primes.

#### Proof

Because \(q-1\) is even, if it has no odd prime divisor then
\[
q-1=2^a.
\]
The condition \(\Omega(q-1)=a\le2\) gives \(q=3\) or \(q=5\).

Otherwise, write
\[
q-1=2^a\prod_i \ell_i^{b_i},
\]
where the \(\ell_i\) are odd primes. Since
\[
a+\sum_i b_i=\Omega(q-1)\le2
\]
and \(a\ge1\), necessarily \(a=1\), there is exactly one odd prime factor, and its exponent is one. Thus
\[
q-1=2\ell.
\]
Conversely, if \(\ell\) and \(2\ell+1\) are prime, then
\[
\Omega(q-1)=\Omega(2\ell)=2.
\]
∎

This stronger target is not merely technically inconvenient. It contains the Sophie Germain prime conjecture at the first shift. It also excludes genuine barriers: for example \(n=14\) is a barrier, but \(q=13\) has
\[
q-1=12,\qquad \omega(12)=2,\qquad \Omega(12)=3.
\]

Hence Route 2 must work directly with \(\omega\), not by replacing it globally with \(\Omega\).

---

### 3. Repeated odd prime powers are a sparse escape

The distinction between \(\omega\) and \(\Omega\) permits
\[
q-1=2^a\ell^b,\qquad b\ge2.
\]
However, these values are quantitatively sparse.

#### Lemma 3

The number of integers \(q\le x\) admitting a representation
\[
q-1=2^a\ell^b,
\qquad a\ge1,\quad b\ge2,\quad \ell\ \text{prime},
\]
is
\[
O\!\left(\sqrt{x}(\log x)^2\right).
\]

#### Proof

It suffices to count all triples \((a,b,\ell)\) satisfying
\[
2^a\ell^b\le x.
\]
Put \(L=\lfloor\log_2x\rfloor\). The number of such triples is at most
\[
\sum_{b=2}^{L}\sum_{a=1}^{L}
\left(\frac{x}{2^a}\right)^{1/b},
\]
where primality of \(\ell\) has been discarded.

For \(b=2\), this is at most
\[
\sqrt{x}\sum_{a\ge1}2^{-a/2}=O(\sqrt{x}).
\]
For \(b\ge3\),
\[
\sum_{a\ge1}2^{-a/b}
=\frac1{2^{1/b}-1}
\le \frac b{\log2},
\]
using \(e^t-1\ge t\). Therefore
\[
\sum_{b=3}^{L}\sum_{a=1}^{L}
\left(\frac{x}{2^a}\right)^{1/b}
\ll
\sum_{b=3}^{L}b\,x^{1/b}
\ll x^{1/3}L^2.
\]
This is \(O(\sqrt{x}(\log x)^2)\). ∎

The pure-power case \(q-1=2^a\) contributes only \(O(\log x)\) possibilities. Thus, apart from a sparse family, the first two conditions in the prime branch ask for
\[
\ell\ \text{prime},\qquad 2^a\ell+1\ \text{prime}.
\]
For every fixed \(a\), this is an admissible two-linear-form prime-tuples problem. The case \(a=1\) is exactly the Sophie Germain problem.

This does not prove that the variable-\(a\) problem implies the Sophie Germain conjecture: mere infinitude could be distributed among unbounded values of \(a\). It does show precisely where a conventional lower-bound sieve encounters parity.

---

### 4. The higher-prime-power branch is strongly restricted

One might hope to bypass the prime branch by taking
\[
q=P^a,\qquad a\ge2.
\]
The condition at \(j=2\) is then
\[
\omega(P^a-1)\le2.
\]

I use the classical Bang–Zsigmondy theorem in the following standard form:

> For \(P\ge2\) and \(d>1\), \(P^d-1\) has a prime divisor which divides no \(P^e-1\) with \(1\le e<d\), except when  
> (i) \(d=2\) and \(P+1\) is a power of \(2\), or  
> (ii) \(P=2,d=6\).

Such a divisor will be called primitive for exponent \(d\). Primitive divisors belonging to two distinct exponents are necessarily distinct.

#### Lemma 4

Suppose \(P\) is prime, \(a\ge2\), and
\[
\omega(P^a-1)\le2.
\]

1. If \(P=2\), then \(a\) is either a prime, the square of a prime, or \(a=6\).
2. If \(P\) is odd, then \(a\) is prime, except for the single possible nonprime case
   \[
   (P,a)=(3,4).
   \]

These are necessary conditions, not sufficient ones.

#### Proof

Let
\[
D(a)=\{d:d\mid a,\ d>1\}.
\]
For every nonexceptional \(d\in D(a)\), choose a primitive prime divisor \(r_d\) of \(P^d-1\). Since \(d\mid a\), each \(r_d\) divides \(P^a-1\). Distinct \(d\)'s give distinct primes.

Suppose first that \(P=2\). There is no prime divisor contributed by \(P-1=1\). The only possible exceptional divisor \(d\) is \(d=6\). Hence
\[
\#D(a)-\mathbf 1_{6\mid a}\le2.
\]
If \(6\nmid a\), then
\[
\tau(a)-1\le2,
\]
so \(\tau(a)\le3\). Therefore \(a\) is prime or a square of a prime.

If \(6\mid a\), then
\[
\tau(a)-2\le2,
\]
so \(\tau(a)\le4\). A multiple of \(6\) has the four divisors \(1,2,3,6\); equality can hold only for \(a=6\). This proves part 1.

Now let \(P\) be odd. The prime \(2\) divides \(P-1\), while no primitive divisor for \(d>1\) can divide \(P-1\). Therefore
\[
1+\#\{\text{nonexceptional }d\in D(a)\}\le2.
\]

If there is no exception, then
\[
1+(\tau(a)-1)\le2,
\]
hence \(\tau(a)\le2\), so \(a\) is prime.

The only possible exception is \(d=2\), requiring \(P+1\) to be a power of \(2\). In that case
\[
1+(\tau(a)-2)\le2,
\]
and therefore \(\tau(a)\le3\). Since \(2\mid a\), this leaves only \(a=2\) or \(a=4\). The exponent \(2\) is prime.

It remains to consider \(a=4\). There is a primitive prime divisor \(r_4\) of \(P^4-1\). To keep the total number of prime divisors at most two, \(P-1\) can have no prime divisor other than \(2\). Thus both \(P-1\) and \(P+1\) are powers of \(2\). Two powers of \(2\) differing by \(2\) must be \(2\) and \(4\), so \(P=3\). Conversely,
\[
3^4-1=80=2^4\cdot5
\]
indeed has two distinct prime divisors. ∎

There is a useful further restriction in the odd-prime-exponent case.

#### Corollary 5

Suppose \(P\) is odd, \(a\) is an odd prime, and
\[
\omega(P^a-1)\le2.
\]
Then
\[
P-1=2^u
\]
with \(u\) a power of \(2\), and
\[
\Phi_a(P)
\]
is a power of one odd prime.

#### Proof

A primitive divisor of \(P^a-1\) does not divide \(P-1\). Since \(2\mid P-1\), any odd prime divisor of \(P-1\) would, together with \(2\) and the primitive divisor, give at least three distinct prime divisors. Thus \(P-1=2^u\).

If \(P=2^u+1\) is prime and \(u\) has an odd divisor \(v>1\), write \(u=vw\). Then
\[
P=(2^w)^v+1
\]
is divisible by \(2^w+1\), a contradiction. Hence \(u\) is a power of \(2\).

Finally,
\[
P^a-1=(P-1)\Phi_a(P).
\]
Since \(a\) is odd, \(\Phi_a(P)\) is odd. Only one odd prime species can divide it, so it is a prime power. ∎

The exceptional exponent cases are genuine rather than artifacts. For example,
\[
64-1=63=3^2\cdot7,\qquad
81-1=80=2^4\cdot5.
\]
Indeed \(65\) and \(82\) are barriers: for each, \(K(n)=3\), so only \(j=1,2\) need checking.

This classification does not construct an infinite family. Prime exponents remain possible, and controlling the relevant cyclotomic value as a prime power is itself difficult.

---

### 5. A rigorous large-offset estimate

The growing number of offsets is a separate issue from the first two lower-bound conditions. It can be reduced considerably in the ambient set of all endpoints.

Let
\[
S(x)=\sum_{p\le x}\frac1p.
\]

#### Lemma 6

For every \(x\ge1\) and \(k\ge1\),
\[
\#\{m\le x:\omega(m)\ge k\}
\le
x\,\frac{S(x)^k}{k!}.
\]

#### Proof

If \(\omega(m)\ge k\), then
\[
1\le\binom{\omega(m)}k.
\]
Moreover,
\[
\binom{\omega(m)}k
=
\sum_{\substack{d\mid m\\d\ \mathrm{squarefree}\\\omega(d)=k}}1.
\]
Therefore
\[
\begin{aligned}
\#\{m\le x:\omega(m)\ge k\}
&\le
\sum_{m\le x}\binom{\omega(m)}k\\
&=
\sum_{\substack{d\le x\\d\ \mathrm{squarefree}\\\omega(d)=k}}
\left\lfloor\frac xd\right\rfloor\\
&\le
x\sum_{p_1<\cdots<p_k\le x}\frac1{p_1\cdots p_k}\\
&\le
\frac{x}{k!}\left(\sum_{p\le x}\frac1p\right)^k.
\end{aligned}
\]
∎

#### Lemma 7

Let \(B(x,H)\) be the number of \(n\le x\) for which there is an offset \(j\ge H\) satisfying
\[
j\le n-1,\qquad \omega(n-j)\ge j+1.
\]
If
\[
H+2\ge2S(x),
\]
then
\[
B(x,H)
\le
2x\left(\frac{eS(x)}{H+1}\right)^{H+1}.
\]

#### Proof

By the union bound and Lemma 6,
\[
\begin{aligned}
B(x,H)
&\le
\sum_{j=H}^{x-1}
\#\{n\le x:\omega(n-j)\ge j+1\}\\
&\le
x\sum_{j=H}^{\infty}\frac{S(x)^{j+1}}{(j+1)!}.
\end{aligned}
\]
Put \(k=j+1\). For \(k\ge H+1\), the ratio of consecutive summands is
\[
\frac{S(x)}{k+1}\le\frac12.
\]
Hence the tail is at most twice its first term:
\[
B(x,H)\le
2x\frac{S(x)^{H+1}}{(H+1)!}.
\]
Using
\[
(H+1)!\ge\left(\frac{H+1}{e}\right)^{H+1}
\]
gives the result. ∎

By the standard Mertens bound
\[
S(x)\le\log\log x+C_0
\]
for an absolute \(C_0\), this gives the following.

#### Corollary 8

For every \(D>0\), there is \(A=A(D)\) such that, with
\[
H(x)=\left\lceil A\bigl(\log\log x+C_0\bigr)\right\rceil,
\]
all but
\[
O_D\left(\frac{x}{(\log x)^D}\right)
\]
integers \(n\le x\) satisfy
\[
\omega(n-j)\le j
\qquad\text{for every }j\ge H(x).
\]

#### Proof

Choose \(A>2e\) such that
\[
A\log(A/e)>D.
\]
Then \(H(x)+1\ge A S(x)\), and Lemma 7 gives
\[
B(x,H(x))
\le
2x(e/A)^{H(x)+1}
\ll_D
\frac{x}{(\log x)^D}.
\]
∎

Thus the genuinely restrictive range can be reduced, for almost all endpoints, from
\[
O\!\left(\frac{\log x}{\log\log x}\right)
\]
to \(O_D(\log\log x)\). This is an ambient estimate, not an estimate conditioned on \(n-1\) being a prime power.

---

### 6. Exact quantitative target for a weighted sieve

The preceding estimate gives a precise sufficient lower-bound theorem that Route 2 would need.

For \(X>H\), let \(\mathcal C(X,H)\) be the primes \(q\) such that
\[
q+1\in[X,2X]
\]
and
\[
\omega(q-r)\le r+1
\qquad(1\le r\le H-2).
\]

Every endpoint \(n=q+1\) arising from \(\mathcal C(X,H)\) satisfies the barrier inequalities for \(1\le j<H\): \(j=1\) follows from \(q\) being prime, and for \(j\ge2\) one puts \(r=j-1\).

Consequently, if
\[
H+2\ge2S(2X)
\]
and
\[
\#\mathcal C(X,H)
>
4X\left(\frac{eS(2X)}{H+1}\right)^{H+1},
\]
then there is a barrier in \([X,2X]\).

Indeed, Lemma 7 bounds the total number of all endpoints \(n\le2X\) failing at some \(j\ge H\) by the right-hand side. If \(\mathcal C(X,H)\) is larger, at least one of its endpoints has no late failure.

This is a rigorous reduction, but no available lower-bound sieve proves the needed estimate. More seriously, even the infinitude of
\[
\mathcal C(X,3)
=
\{q:q\ \text{prime},\ \omega(q-1)\le2\}
\]
is not presently established by this analysis.

## Self-Audit

1. **Bang–Zsigmondy is quoted rather than reproved.**  
   The exponent classification depends on the exact exception list. I believe the application is sound because the quoted form is the classical theorem for \(P^d-1\), and each use explicitly separates the exceptions \(d=2\) and \((P,d)=(2,6)\).

2. **The large-offset estimate is unconditioned.**  
   It is rigorous, but it may be far too weak on the thin set where \(n-1\) is a prime power and the first \(O(\log\log x)\) inequalities hold. I believe the estimate itself is correct because it follows from an exact factorial-moment identity and a union bound; only its usefulness is limited.

3. **The claimed sieve obstruction is methodological, not an impossibility theorem.**  
   Variable \(v_2(q-1)\) might conceivably permit averaging unavailable for any fixed coefficient \(2^a\). I do not claim to prove that no weighted sieve can exploit this. The diagnosis is nevertheless strong because the dominant cases require simultaneous primality of \(\ell\) and \(2^a\ell+1\), while the stronger \(\Omega\)-version exactly contains the Sophie Germain problem.

## Computations To Verify

The following Python performs exact barrier enumeration, checks the exponent classification, compares \(\omega\) with \(\Omega\), and measures joint shifted conditions.

```python
from math import isqrt, log

def sieve_stats(N):
    spf = [0] * (N + 1)
    spf[1] = 1

    for p in range(2, N + 1):
        if spf[p] == 0:
            for m in range(p, N + 1, p):
                if spf[m] == 0:
                    spf[m] = p

    omega = [0] * (N + 1)
    Omega = [0] * (N + 1)
    for n in range(2, N + 1):
        p = spf[n]
        t = n // p
        Omega[n] = Omega[t] + 1
        omega[n] = omega[t] + (1 if t % p != 0 else 0)

    isprime = [False] * (N + 1)
    for n in range(2, N + 1):
        isprime[n] = (spf[n] == n)

    return spf, omega, Omega, isprime

def prime_power_data(n, spf):
    """Return (prime base, exponent) if n is a positive prime power."""
    if n < 2:
        return None
    p = spf[n]
    a = 0
    t = n
    while t % p == 0:
        t //= p
        a += 1
    return (p, a) if t == 1 else None

def small_is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def is_square_of_prime(n):
    r = isqrt(n)
    return r * r == n and small_is_prime(r)

def enumerate_barriers(N, omega):
    barriers = []
    prefix_max = -10**100
    for n in range(1, N + 1):
        # Test before inserting n + omega[n], since m=n is excluded.
        if prefix_max <= n:
            barriers.append(n)
        prefix_max = max(prefix_max, n + omega[n])
    return barriers

def check_zsigmondy_classification(N, spf, omega, isprime):
    primes = [p for p in range(2, N + 1) if isprime[p]]

    examples = []
    for p in primes:
        if p > N // p:
            continue
        q = p * p
        a = 2
        while q <= N:
            if omega[q - 1] <= 2:
                if p == 2:
                    allowed = (
                        small_is_prime(a)
                        or is_square_of_prime(a)
                        or a == 6
                    )
                else:
                    allowed = small_is_prime(a) or (p == 3 and a == 4)

                assert allowed, (p, a, q, omega[q - 1])
                examples.append((p, a, q, omega[q - 1]))

            if q > N // p:
                break
            q *= p
            a += 1

    return examples

def check_prime_branch_representation(N, spf, omega, isprime):
    """
    Verify: for odd prime q with omega(q-1)<=2,
    the odd part of q-1 is 1 or an odd prime power.
    """
    data = []
    for q in range(3, N + 1, 2):
        if not isprime[q] or omega[q - 1] > 2:
            continue

        t = q - 1
        a = 0
        while t % 2 == 0:
            t //= 2
            a += 1

        if t == 1:
            pp = None
        else:
            pp = prime_power_data(t, spf)
            assert pp is not None and pp[0] % 2 == 1

        data.append((q, a, t, pp))
    return data

def shifted_prime_counts(N, J, omega, isprime):
    """
    q corresponds to endpoint n=q+1.
    Shift r requires omega(q-r) <= r+1.
    """
    lo = max(J + 2, N // 2)
    primes = [q for q in range(lo, N + 1) if isprime[q]]

    marginal = []
    for r in range(1, J + 1):
        good = sum(omega[q - r] <= r + 1 for q in primes)
        marginal.append(good / len(primes) if primes else 0.0)

    joint_counts = []
    for j in range(1, J + 1):
        good = sum(
            all(omega[q - r] <= r + 1 for r in range(1, j + 1))
            for q in primes
        )
        joint_counts.append(good)

    product = 1.0
    ratios = []
    for j in range(1, J + 1):
        product *= marginal[j - 1]
        joint_rate = joint_counts[j - 1] / len(primes) if primes else 0.0
        ratios.append(joint_rate / product if product else None)

    return marginal, joint_counts, ratios

def empirical_late_failures(N, H, omega):
    """
    Count n<=N with a violating offset j>=H.
    A failure requires j+1 <= max omega, so only finitely many j are tested.
    """
    maxw = max(omega)
    bad = 0
    witnesses = []

    for n in range(1, N + 1):
        witness = None
        for j in range(H, min(n - 1, maxw - 1) + 1):
            if omega[n - j] >= j + 1:
                witness = (j, n - j, omega[n - j])
                break
        if witness is not None:
            bad += 1
            if len(witnesses) < 20:
                witnesses.append((n,) + witness)

    return bad, witnesses

if __name__ == "__main__":
    N = 2_000_000
    spf, omega, Omega, isprime = sieve_stats(N)

    barriers = enumerate_barriers(N, omega)
    print("first barriers:", barriers[:30])
    assert barriers[:12] == [1,2,3,4,5,6,8,9,10,12,14,17]
    assert 65 in barriers
    assert 82 in barriers

    zsig_examples = check_zsigmondy_classification(
        N, spf, omega, isprime
    )
    print("higher prime-power examples:", zsig_examples[:30])

    prime_branch = check_prime_branch_representation(
        N, spf, omega, isprime
    )
    print("prime-branch first-pair count:", len(prime_branch))

    # Genuine barriers excluded by the stronger Omega target.
    excluded = []
    barrier_set = set(barriers)
    for n in barriers:
        q = n - 1
        if q >= 3 and isprime[q] and omega[q - 1] <= 2:
            if Omega[q - 1] > 2:
                excluded.append((n, q, q - 1,
                                 omega[q - 1], Omega[q - 1]))
    print("barriers excluded by Omega target:", excluded[:20])

    marginal, joint, ratios = shifted_prime_counts(
        N, J=12, omega=omega, isprime=isprime
    )
    print("marginal rates:", marginal)
    print("joint counts:", joint)
    print("joint/product-marginal ratios:", ratios)

    for H in [4, 6, 8, 10, 12]:
        bad, witnesses = empirical_late_failures(N, H, omega)
        print("H =", H, "late failures =", bad,
              "sample witnesses =", witnesses[:5])
```

Particularly useful computations would be:

1. Count primes \(q\le X\) with \(\omega(q-1)\le2\), split by
   \[
   v_2(q-1),\qquad q-1=2^a\ell^b.
   \]
2. Determine empirically whether the \(b=1\) cases dominate.
3. For each \(J\), count primes satisfying
   \[
   \omega(q-r)\le r+1\qquad(1\le r\le J)
   \]
   and compare the joint rate with the product of marginal rates.
4. Check whether candidates with \(q=P^a\), \(a>1\), concentrate in the exponent classes allowed by Lemma 4.

## Route Diagnosis

**Proved ledger**

- In the prime branch, the first two conditions are exactly
  \[
  q\ \text{prime},\qquad q-1=2^a\ell^b
  \]
  with at most one odd prime species.
- The stronger \(\Omega\)-target at the first shift is equivalent, up to \(q=3,5\), to the Sophie Germain prime problem.
- Cases with \(b\ge2\) contribute only
  \[
  O(\sqrt{x}(\log x)^2)
  \]
  possible values up to \(x\).
- Bang–Zsigmondy restricts higher-prime-power exponents to:
  \[
  P=2:\quad a\text{ prime},\ a=\ell^2,\text{ or }a=6;
  \]
  \[
  P\text{ odd}:\quad a\text{ prime},\text{ or }(P,a)=(3,4).
  \]
- For every \(D\), all offsets beyond \(A(D)\log\log x\) pass for all but \(O_D(x/\log^D x)\) ambient endpoints.
- A precise lower bound for the early-offset candidate set would imply a barrier by comparison with the late-failure estimate.

**Plausible but unproved**

- Infinitely many primes \(q\) satisfy \(\omega(q-1)\le2\).
- Averaging over the power \(2^a\) might conceivably make
  \[
  \ell,\ 2^a\ell+1
  \]
  more tractable than any fixed-\(a\) prime pair.
- Given sufficiently strong quantitative control of the first \(O(\log\log x)\) shifts, the later shifts should be removable by a conditional version of Lemma 7 adapted to the sifted candidate set.

**Dead ends**

- Replacing \(\omega\) by \(\Omega\) dies immediately at the Sophie Germain conjecture.
- A conventional fixed-dimensional almost-prime sieve does not address the original \(j=2\) condition: after removing the power of \(2\), it must leave a prime power, and repeated powers are sparse.
- Cyclotomic factorization sharply restricts higher powers but does not construct infinitely many; prime exponents and prime-power cyclotomic values remain.
- The ambient late-offset estimate cannot by itself be intersected with the extremely thin early-offset candidate set.

**Precise block**

Route 2 is blocked before reaching the growing-dimensional part. No lower-bound argument has been obtained even for
\[
q\ \text{prime},\qquad \omega(q-1)\le2.
\]
In its dominant form this requires
\[
\ell\ \text{prime},\qquad 2^a\ell+1\ \text{prime},
\]
with \(a\) variable. For fixed \(a\), this is a two-prime linear-forms problem subject to the sieve parity barrier. The higher-prime-power alternative is restricted by Lemma 4 but remains at least comparably difficult.

A fresh Route 2 attempt should focus specifically on whether averaging over \(a=v_2(q-1)\), perhaps through bilinear switching or dispersion estimates uniform over powers of \(2\), can produce any lower bound for primes whose predecessor has only one odd prime divisor. Without such a new ingredient, adding the remaining shifted forms cannot begin.