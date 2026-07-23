STATUS: BLOCKED

## Result

Route 4 yields an exact and useful duality, but not a resolution. Writing \(A(n)=n-F_C(n)\), I prove
\[
\boxed{D(n)>B\iff A(n+B)>B}
\]
for every integer \(B\ge0\). Consequently,
\[
\boxed{D(n)\to\infty\iff n-F_C(n)\to\infty.}
\]
Thus the proposed asymptotic \(n-F_C(n)\sim c\sqrt n\), if proved, would settle Problem #463; in fact necessarily \(c=1\), and then \(D(n)\sim\sqrt n\). I also give an exact record-process formulation of the lower envelope. In that formulation the problem is equivalent to showing that overlaps between consecutive record intervals tend to infinity. This is an unproved statement of essentially the same strength, so the route is blocked. Moreover, the suggested theorem that exact minimizing intervals cannot hug \(n\) is false: for every prime \(p\), at \(n=p^2-1\) the unique minimizer is \(m=p^2=n+1\), despite \(n-F_C(n)=p-1\).

## Complete Argument

### 1. Basic properties of the lower envelope

For composite \(m\), put
\[
a(m)=m-P^-(m).
\]
Since \(P^-(m)\le \sqrt m\),
\[
a(m)\ge m-\sqrt m\longrightarrow\infty.
\]
Therefore
\[
F_C(n)=\min_{\substack{m>n\\m\text{ composite}}}a(m)
\]
is attained for every \(n\).

Every value \(a(m)\) is even. Indeed:

- if \(P^-(m)=2\), then \(m\) and \(P^-(m)\) are both even;
- if \(P^-(m)\) is odd, then \(m\) is odd, so again \(m-P^-(m)\) is even.

For \(n\ge2\), one also has \(F_C(n)\le n\). If \(n\) is even, take \(m=n+2\), whose least prime factor is \(2\), giving \(a(m)=n\). If \(n\) is odd and \(n\ge3\), take \(m=n+1\), giving \(a(m)=n-1\).

Hence, with
\[
A(n)=n-F_C(n),
\]
we have
\[
A(n)\ge0\qquad(n\ge2).
\]

---

### 2. Exact shifted duality between the two margins

#### Proposition 1

For every \(n\ge2\) and every integer \(B\ge0\),
\[
\boxed{D(n)>B\iff F_C(n+B)<n}
\]
and therefore
\[
\boxed{D(n)>B\iff A(n+B)>B.}
\]

#### Proof

Suppose first that \(D(n)>B\). Then there is an admissible distance \(d>B\) and a composite
\[
m=n+d
\]
such that
\[
P^-(m)>d.
\]
Since \(d>B\),
\[
m=n+d>n+B.
\]
Moreover,
\[
a(m)=m-P^-(m)<m-d=n.
\]
Thus \(m\) is a candidate in the definition of \(F_C(n+B)\), and
\[
F_C(n+B)\le a(m)<n.
\]

Conversely, suppose \(F_C(n+B)<n\), and let \(m>n+B\) be a composite minimizer. Put \(p=P^-(m)\) and \(d=m-n\). Then \(d>B\), while
\[
m-p=F_C(n+B)<n,
\]
so
\[
p>m-n=d.
\]
Thus \(m=n+d\) is an admissible witness at distance \(d>B\), proving \(D(n)>B\).

Finally,
\[
F_C(n+B)<n
\iff n+B-F_C(n+B)>B
\iff A(n+B)>B.
\]
\(\square\)

This also gives the generalized inverse formula
\[
\boxed{D(n)=\min\{k\ge0:A(n+k)\le k\}.}
\]
Indeed, Proposition 1 says \(D(n)>k\) exactly when \(A(n+k)>k\).

#### Corollary 2

\[
\boxed{D(n)\to\infty\iff A(n)=n-F_C(n)\to\infty.}
\]

#### Proof

If \(A(x)\to\infty\), fix \(B\). For all sufficiently large \(n\),
\[
A(n+B)>B,
\]
and Proposition 1 gives \(D(n)>B\).

Conversely, if \(D(n)\to\infty\), fix \(B\). For sufficiently large \(x\), put \(n=x-B\). Then \(D(n)>B\), so Proposition 1 gives
\[
A(x)=A(n+B)>B.
\]
Thus \(A(x)\to\infty\). \(\square\)

This corrects an important point in the brief: control of the left margin at the same argument does not control the right margin of the same minimizing interval, but uniform control of \(A(x)\) does control \(D(n)\) after the fixed shift \(x=n+B\).

---

### 3. Consequence of the proposed asymptotic

Suppose hypothetically that
\[
A(x)\sim c\sqrt x
\]
for some \(c>0\). Let \(\varepsilon>0\), and set
\[
B_-=\left\lfloor(c-\varepsilon)\sqrt n\right\rfloor,
\qquad
B_+=\left\lceil(c+\varepsilon)\sqrt n\right\rceil.
\]
Since \(B_\pm=O(\sqrt n)\),
\[
\sqrt{n+B_\pm}\sim\sqrt n.
\]
Therefore, for sufficiently large \(n\),
\[
A(n+B_-)>B_-,\qquad A(n+B_+)\le B_+.
\]
Proposition 1 then gives
\[
B_-<D(n)\le B_+.
\]
Letting \(\varepsilon\to0\),
\[
D(n)\sim c\sqrt n.
\]

In fact the only possible constant is \(c=1\), as shown below.

---

### 4. An arithmetic model for the lower envelope

For even \(a\ge2\), define
\[
\mathcal P(a)=
\left\{
p:
\begin{array}{l}
p\text{ prime},\ p\mid a,\\[2mm]
b=a/p+1\ge p,\\[1mm]
P^-(b)\ge p
\end{array}
\right\}.
\]
The set is nonempty because \(p=2\) always belongs to it: then
\[
b=a/2+1\ge2,
\]
and every prime factor of \(b\) is at least \(2\).

Define
\[
Q(a)=\max\mathcal P(a),\qquad R(a)=a+Q(a).
\]

#### Proposition 3

\(R(a)\) is the largest composite \(m\) satisfying \(a(m)=a\). Consequently,
\[
\boxed{F_C(n)=\min\{a\ge2:\ a\text{ even and }R(a)>n\}.}
\]

#### Proof

If \(p\in\mathcal P(a)\), put
\[
b=a/p+1,\qquad m=pb=a+p.
\]
All prime factors of \(b\) are at least \(p\), so \(P^-(m)=p\). Therefore
\[
a(m)=m-p=a.
\]

Conversely, suppose \(m\) is composite and \(a(m)=a\). Put \(p=P^-(m)\) and write \(m=pb\). Every prime factor of \(b\) is at least \(p\), and \(b\ge p\). Moreover,
\[
a=m-p=p(b-1),
\]
so \(p\mid a\) and \(b=a/p+1\). Thus \(p\in\mathcal P(a)\), and \(m=a+p\le a+Q(a)=R(a)\).

Hence \(R(a)\) is exactly the largest endpoint among intervals having left endpoint \(a\). There is a composite \(m>n\) with \(a(m)=a\) exactly when \(R(a)>n\), proving the formula for \(F_C(n)\). \(\square\)

---

### 5. The exact record-overlap criterion

Call an even \(a\) a record left endpoint if
\[
R(a)>\max_{\substack{2\le u<a\\u\text{ even}}}R(u).
\]
List these record values as
\[
a_1<a_2<a_3<\cdots
\]
and put
\[
R_j=R(a_j).
\]
The sequence \(R_j\) is strictly increasing and unbounded, because \(R(a)\ge a+2\).

For \(j\ge2\), define the overlap
\[
G_j=R_{j-1}-a_j.
\]
Since \(R(a_j-2)\ge a_j\), one has
\[
R_{j-1}\ge a_j,
\]
and hence \(G_j\ge0\).

#### Proposition 4

For every integer
\[
R_{j-1}\le n<R_j,
\]
one has
\[
F_C(n)=a_j,\qquad A(n)=n-a_j.
\]
In particular,
\[
\min_{R_{j-1}\le n<R_j}A(n)=G_j.
\]
Therefore
\[
\boxed{A(n)\to\infty\iff G_j\to\infty.}
\]

#### Proof

If \(u<a_j\), then by the record definition,
\[
R(u)\le R_{j-1}\le n.
\]
Thus no left endpoint \(u<a_j\) has an associated interval reaching beyond \(n\). On the other hand,
\[
R(a_j)=R_j>n.
\]
Proposition 3 therefore gives \(F_C(n)=a_j\).

It follows that
\[
A(n)=n-a_j,
\]
which is increasing in \(n\) throughout this block. Its minimum is attained at \(n=R_{j-1}\), where it equals \(G_j\).

The blocks cover all sufficiently large integers. Hence \(A(n)\to\infty\) exactly when their minima \(G_j\) tend to infinity. \(\square\)

Combining this with Corollary 2 gives the precise Route 4 target:
\[
\boxed{\text{Problem \#463 is equivalent to }G_j\to\infty.}
\]

A bounded subsequence gives an equally precise disproof criterion. If \(G_j\le B\) for infinitely many \(j\), then with
\[
x_j=R_{j-1},\qquad n_j=x_j-B,
\]
we have
\[
A(x_j)=G_j\le B.
\]
Proposition 1 gives
\[
D(n_j)\le B.
\]

Thus proving or disproving divergence of the record overlaps is not weaker than the original problem.

---

### 6. Exact minimizers necessarily hug the right endpoint infinitely often

The proposed exact-minimizer non-hugging lemma is false.

#### Proposition 5

For every record \(a_j\), at
\[
n=R_j-1
\]
the unique minimizer in the definition of \(F_C(n)\) is
\[
m=R_j=n+1.
\]
Its right depth is exactly \(1\).

#### Proof

If a composite \(m>R_j-1\) has left endpoint \(u<a_j\), then
\[
m\le R(u)\le R_{j-1}<R_j,
\]
a contradiction.

If its left endpoint is \(u=a_j\), then by definition \(m\le R(a_j)=R_j\), so \(m>R_j-1\) forces \(m=R_j\).

Every composite with left endpoint \(u>a_j\) has larger objective value. Thus \(R_j\) is the unique minimizer, at right depth \(1\). \(\square\)

This occurs in a particularly strong form at every prime square.

#### Proposition 6

For every prime \(p\),
\[
F_C(p^2-1)=p^2-p,
\]
and \(m=p^2\) is the unique minimizer. Hence
\[
A(p^2-1)=p-1,
\]
even though the minimizing interval has right depth \(1\).

#### Proof

The composite \(p^2\) has least prime factor \(p\), so it supplies the value
\[
p^2-p.
\]

Conversely, suppose \(m>p^2-1\) is composite and
\[
a(m)\le p^2-p.
\]
Put \(q=P^-(m)\). Writing \(m=qb\) with \(b\ge q\),
\[
a(m)=q(b-1)\ge q(q-1).
\]
Thus
\[
q(q-1)\le p(p-1),
\]
so \(q\le p\). Therefore
\[
m=a(m)+q\le p(p-1)+p=p^2.
\]
Since \(m>p^2-1\), equality must hold throughout:
\[
m=p^2,\qquad q=p,\qquad a(m)=p^2-p.
\]
This proves both the value and uniqueness. \(\square\)

Thus exact minimizing intervals can have left depth tending to infinity while hugging \(n\) at right depth \(1\).

---

### 7. Sharp limsup results

The preceding prime-square construction yields the strongest unconditional growth available from this route, but only along subsequences.

#### Proposition 7

\[
\limsup_{n\to\infty}\frac{A(n)}{\sqrt n}=1,
\qquad
\limsup_{n\to\infty}\frac{D(n)}{\sqrt n}=1.
\]

#### Proof for \(A\)

Choose a minimizing composite \(m\) with
\[
a(m)=F_C(n)=n-A(n).
\]
Put \(p=P^-(m)\). Since \(m=a(m)+p>n\),
\[
p>A(n).
\]
Also, writing \(m=pb\) with \(b\ge p\),
\[
a(m)=p(b-1)\ge p(p-1).
\]
Thus
\[
p(p-1)\le n-A(n)\le n,
\]
and
\[
A(n)\le p-1\le \frac{\sqrt{1+4n}-1}{2}.
\]
Therefore
\[
\limsup\frac{A(n)}{\sqrt n}\le1.
\]

At \(n=p^2-1\), Proposition 6 gives \(A(n)=p-1\), so
\[
\frac{A(p^2-1)}{\sqrt{p^2-1}}\longrightarrow1.
\]

#### Proof for \(D\)

Every valid \(d\) satisfies
\[
d<P^-(n+d)\le\sqrt{n+d},
\]
so
\[
d^2<n+d
\]
and consequently \(D(n)\le\sqrt n+O(1)\).

For prime \(p\), let
\[
n=p^2-p+1.
\]
Then
\[
m=p^2=n+(p-1)
\]
is composite and
\[
P^-(m)=p>p-1.
\]
Hence
\[
D(p^2-p+1)\ge p-1.
\]
Dividing by \(\sqrt{p^2-p+1}\) and letting \(p\to\infty\) proves the lower limsup. \(\square\)

It follows in particular that if an asymptotic
\[
A(n)\sim c\sqrt n
\]
exists, then necessarily \(c=1\). By Section 3, it would then imply
\[
D(n)\sim\sqrt n.
\]

These limsup results do not address the necessary uniform lower bound.

## Self-Audit

1. **The central overlap limit \(G_j\to\infty\) is unproved.**  
   I do not claim that it holds; it is precisely the block that forces the status `BLOCKED`. Proposition 4 shows rigorously that proving it would be equivalent to solving the original problem, rather than a genuine reduction in difficulty.

2. **The shifted duality is vulnerable to a strict-inequality/off-by-one error.**  
   This has been checked in both directions: \(d>B\) is exactly \(m>n+B\), and \(P^-(m)>d\) is exactly \(m-P^-(m)<n\). Thus the strict inequalities match perfectly.

3. **The reach function \(R(a)=a+Q(a)\) could conceivably omit composites with the same left endpoint.**  
   The factorization \(m=pb\), \(a=p(b-1)\), proves a bijection between such composites and the primes in \(\mathcal P(a)\). Maximizing \(p\) therefore really does maximize the endpoint. No primality convention for \(b\) is needed because \(b\ge p\ge2\).

## Computations To Verify

The following Python computes \(D\), \(F_C\), \(A\), the reach function \(R\), and the record overlaps. It also checks all proved identities on a finite range.

```python
from math import isqrt

def spf_sieve(M):
    spf = list(range(M + 1))
    if M >= 1:
        spf[1] = 1
    for p in range(2, isqrt(M) + 1):
        if spf[p] == p:
            for k in range(p * p, M + 1, p):
                if spf[k] == k:
                    spf[k] = p
    return spf

def compute(N=200000, Bmax=100):
    # F and A are needed through N+Bmax.
    X = N + Bmax

    # If a(m) <= X, then with p=P^-(m),
    # p(p-1) <= a(m) <= X and m=a(m)+p.
    # This is therefore a safe exact truncation.
    pmax = (1 + isqrt(1 + 4 * X)) // 2 + 2
    M = X + pmax + 2

    spf = spf_sieve(M)

    def composite(m):
        return m >= 4 and spf[m] < m

    # Exact suffix minima F[x] = min_{composite m>x} (m-spf[m]).
    INF = 10**30
    F = [INF] * (X + 1)
    argF = [-1] * (X + 1)
    run = INF
    run_arg = -1

    # Descending scan. On a tie, retain the already-seen larger m.
    for x in range(M - 1, -1, -1):
        m = x + 1
        if composite(m):
            a = m - spf[m]
            if a < run:
                run = a
                run_arg = m
        if x <= X:
            F[x] = run
            argF[x] = run_arg

    A = [None] * (X + 1)
    for n in range(2, X + 1):
        A[n] = n - F[n]
        assert A[n] >= 0
        assert F[n] % 2 == 0

    # Direct exact computation of D.
    D = [0] * (N + 1)
    for n in range(2, N + 1):
        d = 1
        while d * d < n + d:
            m = n + d
            if composite(m) and spf[m] > d:
                D[n] = d
            d += 1

    # Check D(n)>B iff A(n+B)>B.
    for n in range(2, N + 1):
        for B in range(Bmax + 1):
            if n + B <= X:
                assert (D[n] > B) == (A[n + B] > B)

    # Check generalized inverse formula.
    for n in range(2, N + 1):
        k = 0
        while A[n + k] > k:
            k += 1
        assert k == D[n]

    # R[a] = largest m with m-spf[m] = a.
    R = [-1] * (X + 1)
    for m in range(4, M + 1):
        if composite(m):
            a = m - spf[m]
            if 2 <= a <= X:
                R[a] = max(R[a], m)

    # Every even a has at least the p=2 endpoint a+2.
    for a in range(2, X + 1, 2):
        assert R[a] >= a + 2

    # Extract record left endpoints and their overlaps.
    records = []
    running_endpoint = -1
    for a in range(2, X + 1, 2):
        if R[a] > running_endpoint:
            previous_endpoint = running_endpoint
            q = R[a] - a
            G = None if previous_endpoint < 0 else previous_endpoint - a
            records.append((a, R[a], q, G, previous_endpoint))
            running_endpoint = R[a]

    # Verify the record-block formula and unique right-hugging minimizer.
    for idx in range(1, len(records)):
        a, endpoint, q, G, previous = records[idx]
        assert G >= 0

        lo = max(2, previous)
        hi = min(X + 1, endpoint)
        for n in range(lo, hi):
            assert F[n] == a
            assert A[n] == n - a

        n = endpoint - 1
        if n <= X:
            assert F[n] == a
            assert argF[n] == endpoint
            assert endpoint - n == 1

    # Verify the prime-square identities.
    for p in range(2, isqrt(X + 1) + 1):
        if spf[p] == p:
            n = p * p - 1
            if n <= X:
                assert F[n] == p * (p - 1)
                assert argF[n] == p * p
                assert A[n] == p - 1

    # Search for low-overlap records. Infinitely many with one fixed
    # bound B would disprove the conjecture.
    for B in [0, 1, 2, 5, 10, 20, 50, 100]:
        low = [
            rec for rec in records[1:]
            if rec[3] is not None and rec[3] <= B
        ]
        print("B =", B,
              "number of record overlaps <= B:", len(low),
              "last few:", low[-10:])

    # The decisive empirical statistics.
    X0 = 100
    while 2 * X0 <= N:
        print(
            "block", X0, 2 * X0,
            "min A =", min(A[X0:2 * X0 + 1]),
            "min D =", min(D[X0:2 * X0 + 1])
        )
        X0 *= 2

    return spf, F, A, D, R, records

# Example:
# spf, F, A, D, R, records = compute()
```

For a possible disproof search, the most relevant output is not merely low \(D(n)\), but record tuples
\[
(a_j,R_j,Q(a_j),G_j,R_{j-1})
\]
with bounded \(G_j\). If \(G_j\le B\), the corresponding explicitly testable candidate is
\[
n=R_{j-1}-B,
\]
for which the proved duality predicts \(D(n)\le B\).

## Route Diagnosis

**Proved ledger.**

- \(D(n)>B\iff A(n+B)>B\).
- \(D(n)\to\infty\iff A(n)\to\infty\).
- A positive asymptotic for \(A\) would solve the problem; any asymptotic constant must be \(1\).
- All lower endpoints are even, and \(A(n)\ge0\).
- The exact arithmetic reach model \(R(a)=a+Q(a)\).
- The record-overlap criterion \(A(n)\to\infty\iff G_j\to\infty\).
- Exact minimizers have right depth \(1\) infinitely often; prime squares give explicit examples with left depth tending to infinity.
- \(\limsup A(n)/\sqrt n=\limsup D(n)/\sqrt n=1\).

**Plausible but unproved.**

- The affirmative record statement
  \[
  \max_{u<a_j}R(u)-a_j=G_j\longrightarrow\infty.
  \]
- Any useful endpoint-separation theorem for uniformly near-minimizing, rather than exactly minimizing, intervals.
- The stronger conjecture \(A(n)\sim\sqrt n\).

**Dead ends.**

- Exact-minimizer non-hugging is false, already along \(n=p^2-1\).
- Large left depth at isolated arguments gives only limsup information.
- Abstract monotonicity of the lower envelope is insufficient: it gives no lower bound on the record overlaps.
- Restricting to a fixed finite set of possible least prime factors cannot work uniformly. If \(n\) is divisible by all of them, no valid witness can have one of those least factors, since \(p\mid n,m\) would force \(p\mid d\), contradicting \(0<d<p\).

**Precise block.**

The route has reduced the problem to
\[
G_j=R_{j-1}-a_j\to\infty,
\]
where
\[
R(a)=a+
\max\left\{
p:\ p\mid a,\ 
a/p+1\ge p,\ 
P^-(a/p+1)\ge p
\right\}.
\]
This is an exact reformulation, not a weaker theorem. No argument found forces previous record intervals to extend increasingly far past the next record left endpoint. Conversely, infinitely many bounded \(G_j\) would immediately yield a disproof.

A fresh attempt should focus directly on the arithmetic of low-overlap records \(a_j\): either prove they cannot persist using a bilinear/sieve analysis of nearby \(u=p(b-1)\), or identify a structured infinite family with bounded \(G_j\). Computations should prioritize record overlaps and their factorizations, not merely average values of \(D(n)\) or the right depth of the exact minimizer.