STATUS: BLOCKED

## Result

Route 2 reduces exactly to finding prime lattice points \((p,\lceil n/p\rceil)\) in a unit-width hyperbolic strip. I prove that such semiprime witnesses are abundant on average: for every fixed \(B\), their total number over \(n\le X\) is asymptotic to \(\frac83X^{3/2}/(\log X)^2\), implying at least \((\frac43+o(1))X/\log X\) integers \(n\le X\) have a semiprime witness of depth \(>B\). I also prove that the residue-depth condition costs at most \(B\) candidates per \(n\), establish the sharp relation \(\limsup D_2(n)/\sqrt n=\limsup D(n)/\sqrt n=1\), and exhibit a parity obstruction near perfect squares which rules out relying only on primes extremely close to \(\sqrt n\). None of these results controls every sufficiently large \(n\); the route remains blocked at a pointwise lower bound for a prime-prime reciprocal sum.

## Complete Argument

### 1. Exact formulation of Route 2

Define the semiprime version of \(D(n)\) by
\[
D_2(n)=\max\Bigl(
\{pq-n:\ p,q\text{ prime},\ p\le q,\ p(q-1)<n<pq\}
\cup\{0\}
\Bigr).
\]
Every pair counted here gives
\[
d=pq-n,\qquad 1\le d<p.
\]
Since \(P^-(pq)=p\), it is an admissible witness for the original problem. Thus
\[
D_2(n)\le D(n).
\]

Let
\[
C(n)=\#\{(p,q):p,q\text{ prime},\ p\le q,\ p(q-1)<n<pq\},
\]
and, for a fixed integer \(B\ge0\),
\[
C_B(n)=\#\{(p,q)\text{ counted by }C(n):pq-n>B\}.
\]
Then
\[
C_B(n)>0\quad\Longleftrightarrow\quad D_2(n)>B.
\]

#### Lemma 1: reciprocal parameterization

For each prime \(p\), a pair counted by \(C(n)\) exists with first coordinate \(p\) precisely when
\[
p(p-1)<n,\qquad p\nmid n,\qquad
q=\left\lceil\frac np\right\rceil\text{ is prime}.
\]
In this case \(q\ge p\), and
\[
pq-n=p-(n\bmod p).
\]

**Proof.**

Suppose
\[
p(q-1)<n<pq.
\]
Dividing by \(p\) gives
\[
q-1<\frac np<q,
\]
so
\[
q=\left\lceil\frac np\right\rceil.
\]
The strict upper inequality implies \(p\nmid n\). Since \(q\ge p\),
\[
n>p(q-1)\ge p(p-1).
\]
Writing \(n=ap+r\), \(1\le r\le p-1\), gives \(q=a+1\), and hence
\[
pq-n=p(a+1)-(ap+r)=p-r.
\]

Conversely, suppose \(p(p-1)<n\), \(p\nmid n\), and \(q=\lceil n/p\rceil\) is prime. Then \(n/p>p-1\), so \(q\ge p\). Since \(p\nmid n\),
\[
q-1<\frac np<q,
\]
and therefore
\[
p(q-1)<n<pq.
\]
This proves the characterization. ∎

Consequently,
\[
C(n)=
\sum_{\substack{p\ \mathrm{prime}\\p(p-1)<n\\p\nmid n}}
1_{\mathbb P}\!\left(\left\lceil\frac np\right\rceil\right).
\]

The interval for \(q\), with \(p\) fixed, has exact width one:
\[
n<pq<n+p
\quad\Longleftrightarrow\quad
\frac np<q<\frac np+1.
\]
This explains why ordinary prime-gap results do not address Route 2.

---

### 2. The depth condition costs at most \(B\) candidates

#### Lemma 2

For every \(n\) and \(B\ge0\),
\[
0\le C(n)-C_B(n)\le B.
\]
In particular,
\[
C(n)>B\quad\Longrightarrow\quad D_2(n)>B.
\]

**Proof.**

Associate to each pair \((p,q)\) counted by \(C(n)\) its depth
\[
d=pq-n\in\mathbb N.
\]
This map is injective. Indeed, if two canonical pairs \(p\le q\) and \(p'\le q'\) have the same depth, then
\[
pq=n+d=p'q'.
\]
The uniqueness of prime factorization, together with the ordering of the two prime factors, gives
\[
(p,q)=(p',q').
\]

There are only \(B\) possible integer depths \(1\le d\le B\). Hence at most \(B\) candidates are removed in passing from \(C(n)\) to \(C_B(n)\). If \(C(n)>B\), at least one candidate has depth \(>B\). ∎

Thus a uniform theorem \(C(n)\to\infty\) would solve the original problem through Route 2. The residue condition \(p-(n\bmod p)>B\) is not the main obstacle once sufficiently many prime lattice points are available.

---

### 3. Average abundance of Route-2 witnesses

#### Theorem 3

For every fixed integer \(B\ge0\),
\[
\boxed{
\sum_{n\le X}C_B(n)
\sim
\frac83\,\frac{X^{3/2}}{(\log X)^2}
}
\qquad (X\to\infty).
\]

In particular, the same asymptotic holds with \(C_B\) replaced by \(C\).

**Proof.**

First consider
\[
T(X)=\sum_{n\le X}C(n).
\]
A fixed pair of primes \(p\le q\) contributes for exactly the integers
\[
p(q-1)+1,\ldots,pq-1,
\]
an interval of length \(p-1\).

All pairs with \(pq\le X\) therefore contribute fully. Put
\[
A(X)=
\sum_{\substack{p,q\ \mathrm{prime}\\p\le q\\pq\le X}}(p-1).
\]
Then \(T(X)\ge A(X)\).

If a pair contributes to \(T(X)-A(X)\), then
\[
X<pq<X+p.
\]
For fixed \(p\), this places \(q\) in
\[
\frac Xp<q<\frac Xp+1,
\]
which contains at most one integer. Moreover, \(p\le q\) and \(p(q-1)<X\) imply
\[
p(p-1)<X,
\]
so \(p<\sqrt X+1\). Hence
\[
0\le T(X)-A(X)
\le \sum_{p<\sqrt X+1}p
=O(X),
\]
where even summing over all integers \(p\), rather than only primes, suffices.

Now replace \(p-1\) by \(p\):
\[
S(X)=
\sum_{\substack{p,q\ \mathrm{prime}\\p\le q\\pq\le X}}p.
\]
The difference \(S(X)-A(X)\) is the number of prime pairs in the sum. Crude counting gives
\[
0\le S(X)-A(X)
\le \sum_{2\le p\le\sqrt X}\frac Xp
=O(X\log X)
=o\!\left(\frac{X^{3/2}}{(\log X)^2}\right).
\]
It remains to evaluate \(S(X)\).

Write
\[
R=\sqrt X,\qquad L=\log X=2\log R.
\]
Fix \(0<\delta<1\), and first restrict to \(p\ge\delta R\). Set
\[
K_\delta=
\{(u,v):\delta\le u\le1,\ u\le v\le 1/u\}.
\]
The prime number theorem implies the weak convergence
\[
\frac{\log R}{R}\sum_{p\ \mathrm{prime}}\delta_{p/R}
\ \Longrightarrow\ 
\text{Lebesgue measure}
\]
on every compact subinterval of \((0,\infty)\). Indeed, for fixed \(0<a<b\),
\[
\frac{\log R}{R}\bigl(\pi(bR)-\pi(aR)\bigr)\longrightarrow b-a.
\]
Taking product measures and using that the boundary of \(K_\delta\) has two-dimensional measure zero yields
\[
\sum_{\substack{p,q\ \mathrm{prime}\\
(p/R,q/R)\in K_\delta}}p
\sim
\frac{R^3}{(\log R)^2}
\iint_{K_\delta}u\,du\,dv.
\]
The integral is
\[
\begin{aligned}
\iint_{K_\delta}u\,du\,dv
&=\int_\delta^1u\left(\frac1u-u\right)\,du\\
&=\int_\delta^1(1-u^2)\,du\\
&=\frac23-\delta+\frac{\delta^3}{3}.
\end{aligned}
\]
Since \((\log R)^2=L^2/4\), the truncated sum is therefore
\[
\left(
4\left(\frac23-\delta+\frac{\delta^3}{3}\right)+o(1)
\right)
\frac{X^{3/2}}{L^2}.
\]

It remains to bound \(p<\delta R\). By the standard Chebyshev upper bound
\[
\pi(y)\ll \frac y{\log y},
\]
for fixed \(\delta\) and sufficiently large \(X\),
\[
\begin{aligned}
\sum_{\substack{p<\delta R\\p\ \mathrm{prime}}}
p\,\pi(X/p)
&\ll
\sum_{p<\delta R}\frac{X}{\log(X/p)}\\
&\ll
\frac X{L}\pi(\delta R)\\
&\ll
\delta\frac{XR}{L^2}.
\end{aligned}
\]
Thus the contribution from \(p<\delta R\) is
\[
O\!\left(\delta\frac{X^{3/2}}{L^2}\right).
\]
Letting \(X\to\infty\) and then \(\delta\to0\), we obtain
\[
S(X)\sim
4\cdot\frac23\frac{X^{3/2}}{L^2}
=
\frac83\frac{X^{3/2}}{(\log X)^2}.
\]
The estimates comparing \(S(X),A(X)\), and \(T(X)\) prove
\[
\sum_{n\le X}C(n)
\sim
\frac83\frac{X^{3/2}}{(\log X)^2}.
\]

Finally, Lemma 2 gives pointwise
\[
0\le C(n)-C_B(n)\le B.
\]
Therefore
\[
0\le
\sum_{n\le X}\bigl(C(n)-C_B(n)\bigr)
\le BX,
\]
and
\[
BX=o\!\left(\frac{X^{3/2}}{(\log X)^2}\right).
\]
The same asymptotic follows for \(C_B\). ∎

A dyadic version follows by subtraction:
\[
\sum_{X<n\le2X}C_B(n)
\sim
\frac83(2^{3/2}-1)\frac{X^{3/2}}{(\log X)^2}.
\]

---

### 4. A quantitative support consequence

#### Corollary 4

For every fixed \(B\ge0\),
\[
\#\{n\le X:D_2(n)>B\}
\ge
\left(\frac43+o(1)\right)\frac X{\log X}.
\]

**Proof.**

If \(n\le X\), any pair counted by \(C(n)\) has
\[
p(p-1)<n\le X,
\]
so \(p<\sqrt X+1\). For fixed \(p\), the corresponding \(q\) is uniquely \(\lceil n/p\rceil\). Hence
\[
C_B(n)\le C(n)\le\pi(\sqrt X+1)
=(2+o(1))\frac{\sqrt X}{\log X}.
\]
Writing
\[
E_B(X)=\#\{n\le X:C_B(n)>0\},
\]
Theorem 3 gives
\[
\frac83(1+o(1))\frac{X^{3/2}}{(\log X)^2}
\le
E_B(X)(2+o(1))\frac{\sqrt X}{\log X}.
\]
Rearranging proves the claim. ∎

This is only a lower bound on the number of successful \(n\). It gives no upper bound on the exceptional set and therefore has no pointwise consequence.

---

### 5. The square-root scale is attained along an infinite sequence

#### Proposition 5

Both the full problem and its semiprime restriction satisfy
\[
\limsup_{n\to\infty}\frac{D_2(n)}{\sqrt n}
=
\limsup_{n\to\infty}\frac{D(n)}{\sqrt n}
=1.
\]

**Proof.**

The general necessary bound from the problem statement gives
\[
D(n)<\frac{1+\sqrt{1+4n}}2=\sqrt n+O(1),
\]
and the same upper bound applies to \(D_2(n)\).

For every prime \(p\), take
\[
n=p^2-p+1.
\]
Then
\[
m=p^2=n+(p-1),
\]
and
\[
P^-(m)=p>p-1.
\]
Thus
\[
D_2(n)\ge p-1.
\]
Since
\[
\frac{p-1}{\sqrt{p^2-p+1}}\longrightarrow1
\]
along the infinite sequence of primes, both limsups are at least \(1\), while the general upper bound makes them at most \(1\). ∎

This confirms that the problem is purely about uniform lower behavior, not the possible size of large values.

---

### 6. A parity obstruction near perfect squares

A tempting simplification of Route 2 is to search only for \(p\) extremely close to \(\sqrt n\). Perfect squares refute this.

#### Proposition 6

Let \(n=N^2\), and let
\[
A_N=\max\{a\in\mathbb N:a^2+a<N\}.
\]
For sufficiently large \(N\), no Route-2 candidate has
\[
N-A_N\le p\le N.
\]
Since \(A_N=\sqrt N+O(1)\), this excludes a window of length
\[
\asymp \sqrt N=n^{1/4}
\]
immediately below \(\sqrt n\).

**Proof.**

The choice \(p=N\) gives \(p\mid n\), hence depth zero.

Now write
\[
p=N-a,\qquad 1\le a\le A_N.
\]
Then
\[
a^2<N-a=p,
\]
and
\[
\frac{N^2}{N-a}
=
N+a+\frac{a^2}{N-a}.
\]
The final fraction lies strictly between \(0\) and \(1\), so
\[
q=\left\lceil\frac{N^2}{p}\right\rceil=N+a+1.
\]
Consequently
\[
p+q=(N-a)+(N+a+1)=2N+1,
\]
which is odd. For sufficiently large \(N\), both \(p\) and \(q\) exceed \(2\). If they were both prime, they would both be odd and their sum would be even, a contradiction. ∎

Thus any argument using only the nearest \(n^{1/4}\)-sized neighborhood below \(\sqrt n\) fails for every sufficiently large perfect square.

---

### 7. Where Route 2 stops

By Lemma 1, the required pointwise object is
\[
C(n)=
\sum_{\substack{p\ \mathrm{prime}\\p(p-1)<n\\p\nmid n}}
1_{\mathbb P}\!\left(\left\lceil\frac np\right\rceil\right).
\]
A uniform estimate such as
\[
C(n)\sim 4\frac{\sqrt n}{(\log n)^2}
\]
would be more than enough, as would merely
\[
C(n)\longrightarrow\infty.
\]
Theorem 3 proves only the corresponding first-moment statement. A first moment cannot rule out an infinite sparse exceptional sequence on which \(C(n)\) is zero or bounded.

The obstruction is exact rather than a matter of ordinary prime gaps: once \(p\) is chosen, \(q\) must be the single integer \(\lceil n/p\rceil\). Proving that both are prime for every \(n\) is a pointwise prime-prime problem on a discontinuous reciprocal sequence. I do not have a lower-bound sieve, dispersion estimate, or other argument that supplies such a pointwise bound.

There is also a precise structural reason Route 3 is genuinely different. If a general witness has
\[
m=pb,\qquad p=P^-(m),
\]
and \(b\) is composite, then all prime factors of \(b\) are at least \(p\), so
\[
b\ge p^2,\qquad m=pb\ge p^3.
\]
Therefore:

> If \(P^-(m)>m^{1/3}\), then \(m\) is necessarily a semiprime.

Thus Route 2 captures all witnesses with least prime factor above the cube-root scale. Any advantage from rough composite cofactors must come from \(p\le m^{1/3}\).

## Self-Audit

1. **The constant \(\frac83\) is sensitive to the two-dimensional prime integral.**  
   The calculation uses the prime number theorem through weak convergence of rescaled prime measures. I believe it is secure because the truncated domain is compact with boundary measure zero, the integral is explicitly
   \[
   \int_0^1u(1/u-u)\,du=\frac23,
   \]
   and the conversion \((\log\sqrt X)^{-2}=4(\log X)^{-2}\) gives the factor \(8/3\).

2. **The passage from complete semiprime intervals to \(n\le X\) has a boundary term.**  
   This could easily cause an incorrect main term if the boundary were large. Here it is rigorously \(O(X)\): for each \(p\), the relevant \(q\) lies in an interval of length one, and \(p<\sqrt X+1\). This is negligible compared with \(X^{3/2}/(\log X)^2\).

3. **The diagnosis that Route 2 is blocked is methodological, not an impossibility theorem.**  
   A new pointwise bilinear prime theorem could overcome it. I have not proved that such a theorem is inaccessible; I have proved only average abundance and a local parity obstruction. I therefore make no claim that Route 2 is hopeless, only that the remaining pointwise estimate is of essentially the same strength as the desired semiprime subproblem.

## Computations To Verify

The following Python computes \(C(n)\), \(C_B(n)\), and \(D_2(n)\), checks the average asymptotic, searches for large exceptional \(n\), and verifies the perfect-square obstruction.

```python
from math import isqrt, log
from bisect import bisect_left, bisect_right

def spf_sieve(M):
    spf = list(range(M + 1))
    if M >= 1:
        spf[1] = 1
    for p in range(2, isqrt(M) + 1):
        if spf[p] == p:
            for m in range(p * p, M + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def route2_counts(N, B=0):
    """
    Returns exact arrays C[n], C_B[n], D2[n] for 1 <= n <= N.
    C and C_B are filled efficiently by interval additions.
    D2 is filled directly from the reciprocal parameterization.
    """
    spf = spf_sieve(N + 2)
    isprime = [False] * (N + 3)
    primes = []
    for x in range(2, N + 3):
        if spf[x] == x:
            isprime[x] = True
            primes.append(x)

    diff_C = [0] * (N + 3)
    diff_CB = [0] * (N + 3)

    # A pair p <= q covers n in [p(q-1)+1, pq-1].
    for p in primes:
        if p * (p - 1) >= N:
            break
        qmax = (N - 1) // p + 1  # largest q whose interval can meet n <= N
        i0 = bisect_left(primes, p)
        i1 = bisect_right(primes, qmax)

        for q in primes[i0:i1]:
            lo = p * (q - 1) + 1
            hi = min(N, p * q - 1)
            if lo <= hi:
                diff_C[lo] += 1
                diff_C[hi + 1] -= 1

            # Depth pq-n > B means n <= pq-B-1.
            hiB = min(N, p * q - B - 1)
            if lo <= hiB:
                diff_CB[lo] += 1
                diff_CB[hiB + 1] -= 1

    C = [0] * (N + 1)
    CB = [0] * (N + 1)
    running_C = running_CB = 0
    for n in range(1, N + 1):
        running_C += diff_C[n]
        running_CB += diff_CB[n]
        C[n] = running_C
        CB[n] = running_CB

    # Direct reciprocal computation of D2.
    small_primes = [p for p in primes if p <= isqrt(N) + 2]
    D2 = [0] * (N + 1)
    for n in range(1, N + 1):
        count_check = 0
        countB_check = 0
        for p in small_primes:
            if p * (p - 1) >= n:
                break
            q = (n + p - 1) // p
            d = p * q - n
            if d == 0:
                continue
            if isprime[q]:
                assert q >= p
                assert 1 <= d < p
                count_check += 1
                if d > B:
                    countB_check += 1
                    D2[n] = max(D2[n], d)

        assert count_check == C[n]
        assert countB_check == CB[n]
        assert C[n] - CB[n] <= B

    return C, CB, D2

def original_D(N):
    """Directly computes the full D(n), allowing more than two prime factors."""
    M = N + isqrt(N) + 5
    spf = spf_sieve(M)
    D = [0] * (N + 1)

    for n in range(1, N + 1):
        d = 1
        while d * d < n + d:
            m = n + d
            if spf[m] < m and spf[m] > d:
                D[n] = d
            d += 1
    return D

def check_average(N, B=0):
    C, CB, D2 = route2_counts(N, B)
    predicted = (8.0 / 3.0) * (N ** 1.5) / (log(N) ** 2)

    print("N =", N, "B =", B)
    print("sum C / prediction   =", sum(C[1:]) / predicted)
    print("sum C_B / prediction =", sum(CB[1:]) / predicted)
    print("number with D2 > B    =", sum(d > B for d in D2[1:]))
    print("lower-bound scale X/log X =", N / log(N))

    exceptions = [n for n in range(1, N + 1) if D2[n] <= B]
    print("largest tested exception =", max(exceptions) if exceptions else None)
    print("C(10), C(100) =", C[10] if N >= 10 else None,
          C[100] if N >= 100 else None)

def square_obstruction(Nroot):
    """
    For n=Nroot^2, checks that there is no prime-prime candidate
    p=Nroot-a with a^2+a<Nroot.
    """
    spf = spf_sieve(2 * Nroot + 5)
    isprime = lambda x: x >= 2 and spf[x] == x

    forbidden_hits = []
    n = Nroot * Nroot

    for p in range(3, Nroot):
        if not isprime(p):
            continue
        a = Nroot - p
        if a * a + a < Nroot:
            q = (n + p - 1) // p
            assert q == Nroot + a + 1
            if isprime(q):
                forbidden_hits.append((p, q, a))

    return forbidden_hits  # must always be []

# Suggested runs:
#
# for N in [10**3, 10**4, 10**5, 10**6]:
#     check_average(N, B=10)
#
# for root in [100, 1000, 10000]:
#     assert square_obstruction(root) == []
#
# N = 200000
# C, CB, D2 = route2_counts(N, B=20)
# D = original_D(N)
# for X in [1000, 2000, 5000, 10000, 20000, 50000, 100000]:
#     if 2*X <= N:
#         print(X,
#               "min D2 on [X,2X] =", min(D2[X:2*X+1]),
#               "min D on [X,2X]  =", min(D[X:2*X+1]),
#               "C=0 count =", sum(C[n] == 0 for n in range(X,2*X+1)))
```

The most informative computational outputs are:

1. the largest \(n\le N\) with \(C_B(n)=0\);
2. \(\min_{X\le n\le2X}D_2(n)\) and \(\min_{X\le n\le2X}D(n)\);
3. whether low-\(C(n)\) cases concentrate near squares or special residue patterns;
4. the scales of successful \(p\), especially whether \(p\ll\sqrt n\) materially contributes.

## Route Diagnosis

**Proved ledger**

- Exact bijection between Route-2 witnesses and primes \(p\) for which \(\lceil n/p\rceil\) is prime.
- Distinct candidates have distinct depths, so at most \(B\) candidates have depth at most \(B\).
- For fixed \(B\),
  \[
  \sum_{n\le X}C_B(n)\sim \frac83\frac{X^{3/2}}{(\log X)^2}.
  \]
- Consequently at least \((\frac43+o(1))X/\log X\) integers \(n\le X\) have \(D_2(n)>B\).
- The maximal square-root scale is attained:
  \[
  \limsup D_2(n)/\sqrt n=\limsup D(n)/\sqrt n=1.
  \]
- Perfect squares create a parity-free zone of width \(\asymp n^{1/4}\) immediately below \(\sqrt n\).
- Any non-semiprime witness must have least prime factor at most \(m^{1/3}\).

**Plausible but unproved**

- The pointwise heuristic
  \[
  C(n)\asymp\frac{\sqrt n}{(\log n)^2},
  \]
  and more specifically \(C(n)\sim4\sqrt n/(\log n)^2\).
- Even the weaker statement \(C(n)\to\infty\).
- Eventual positivity \(C(n)>0\), i.e. eventual coverage using semiprimes alone.

**Dead ends**

- Searching only in an \(n^{1/4}\)-neighborhood of \(\sqrt n\): rigorously defeated by the perfect-square parity obstruction.
- Using ordinary prime-gap theorems: for fixed \(p\), the permitted \(q\)-interval has width exactly one.
- Using the first moment to infer uniformity: it permits an infinite sparse exceptional set and therefore cannot settle the problem.
- Treating the values \(\lceil n/p\rceil\) as independent random integers: this supplies the correct average heuristic but no pointwise control.

**Recommended next direction**

A fresh Route-2 attempt would need a genuinely pointwise lower bound for
\[
\sum_{\substack{p(p-1)<n\\p\ \mathrm{prime}}}
1_{\mathbb P}\!\left(\left\lceil\frac np\right\rceil\right),
\]
probably through a dispersion or bilinear method capable of retaining a fixed parameter \(n\). If that remains inaccessible, Route 3 is the most meaningful alternative: work at \(p\le n^{1/3}\), where the cofactor can be composite and \(p\)-rough. That regime is not covered by the semiprime analysis and may offer additional convolutional flexibility, though it still faces a severe pointwise sieve problem.