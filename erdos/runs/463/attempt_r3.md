STATUS: BLOCKED

## Result

Route 3 admits a clean exact parametrization and a useful reduction: for a dyadic prime scale \(P\), it is enough to prove that uniformly in \(n\), many primes \(p\in[P,2P]\) have \(p\)-rough cofactors \(\lceil n/p\rceil\). The residue requirement \(p-(n\bmod p)>B\) is then essentially harmless: only \(O_B(\log n/\log P)\) candidate primes can fail it. I also prove that the genuinely new part of Route 3—composite rather than prime cofactors—is confined to \(p^3-p+1\le n\), hence \(p\lesssim n^{1/3}\); above that scale Route 3 collapses to the semiprime route. For each fixed \(p\), the successful \(n\) form an explicit periodic set of density asymptotic to \(e^{-\gamma}/\log p\), and the average number of successful \(p\in[Y,2Y]\) tends to infinity. However, primorial multiples produce exact pointwise holes for every bounded collection of \(p\), so these average statements cannot yield the required uniform conclusion. The remaining task is a pointwise lower-bound sieve for the reciprocal sequence \(\lceil n/p\rceil\), at essentially full sieve depth; I do not prove such an estimate, and it appears comparable in difficulty to the original problem.

## Complete Argument

### 1. Exact Route 3 parametrization

For a prime \(p\), define
\[
b_p(n)=\left\lceil\frac np\right\rceil,\qquad
d_p(n)=p\,b_p(n)-n.
\]
Then
\[
0\le d_p(n)\le p-1.
\]

#### Lemma 1

Let \(p\) be prime. Suppose
\[
b_p(n)\ge p
\]
and every prime factor of \(b_p(n)\) is at least \(p\). If \(d_p(n)>0\), then
\[
m=p\,b_p(n)
\]
is an admissible witness for \(n\), with distance \(d_p(n)\). Conversely, every admissible witness arises uniquely in this way by taking \(p=P^-(m)\).

#### Proof

Put \(b=b_p(n)\) and \(d=pb-n\). Under the hypotheses, \(b\ge p\ge2\), so \(m=pb\) is composite. Since \(p\) is prime and every prime factor of \(b\) is at least \(p\),
\[
P^-(m)=p.
\]
If \(d>0\), then
\[
n<m=n+d
\]
and, since \(d\le p-1\),
\[
d<P^-(m).
\]
Thus \(m\) is admissible.

Conversely, let \(m=n+d\) be admissible and set
\[
p=P^-(m),\qquad b=\frac mp.
\]
Every prime factor of \(b\) is at least \(p\). Also \(b\ge p\), because \(m\) is composite and \(p\) is its least prime factor. Since \(0<d<p\),
\[
\frac np=b-\frac dp\in(b-1,b).
\]
Therefore
\[
b=\left\lceil\frac np\right\rceil,
\]
and \(d=pb-n=d_p(n)\). The prime \(p=P^-(m)\) is uniquely determined. ∎

Thus Route 3 is not merely a sufficient construction: searching over all eligible \(p\) is exactly equivalent to searching over all witnesses.

---

### 2. Composite cofactors occur only below the cube-root scale

The distinction between Route 2 and Route 3 is whether \(b_p(n)\) is prime or composite.

#### Lemma 2

Suppose \(p\) yields a Route 3 witness and \(b=b_p(n)\) has at least \(k\) prime factors counted with multiplicity. Then
\[
n\ge p^{k+1}-p+1.
\]
In particular, if \(b\) is composite, then
\[
n\ge p^3-p+1.
\]

#### Proof

Every prime factor of \(b\) is at least \(p\). Hence, if \(\Omega(b)\ge k\),
\[
b\ge p^k.
\]
Since \(1\le d_p(n)\le p-1\),
\[
n=pb-d_p(n)
  \ge p^{k+1}-(p-1)
  =p^{k+1}-p+1.
\]
For composite \(b\), one has \(\Omega(b)\ge2\), giving the stated special case. ∎

Consequently, whenever
\[
p^3-p+1>n,
\]
the cofactor \(b_p(n)\) must be prime. Thus for \(p\gtrsim n^{1/3}\), Route 3 gives no enlargement over the semiprime construction \(m=pq\). Any genuinely bilinear rough-cofactor argument must therefore operate at
\[
p\lesssim n^{1/3}.
\]

More generally, witnesses for which \(b\) has at least \(k\) prime factors are restricted to \(p\lesssim n^{1/(k+1)}\).

---

### 3. Exact periodic structure for one fixed prime

Fix \(B\ge0\) and a prime \(p>B+1\). Let
\[
W_{<p}=\prod_{\substack{q<p\\q\ \mathrm{prime}}}q.
\]

Write
\[
n=pa+r,\qquad 0\le r<p.
\]
If \(r>0\), then
\[
b_p(n)=a+1,\qquad d_p(n)=p-r.
\]
Therefore
\[
d_p(n)>B
\quad\Longleftrightarrow\quad
1\le r\le p-B-1.
\]
Moreover,
\[
P^-(b_p(n))\ge p
\quad\Longleftrightarrow\quad
\gcd(a+1,W_{<p})=1,
\]
provided \(b_p(n)\ge p\).

#### Lemma 3

For all sufficiently large \(n\), a fixed prime \(p>B+1\) is a successful Route 3 parameter exactly when
\[
n=pa+r,
\]
where
\[
1\le r\le p-B-1
\]
and
\[
\gcd(a+1,W_{<p})=1.
\]
This condition is periodic in \(n\) with period
\[
pW_{<p}=\prod_{q\le p}q,
\]
and its natural density is
\[
\delta_{p,B}
=
\frac{p-B-1}{p}
\prod_{q<p}\left(1-\frac1q\right).
\]

#### Proof

The characterization follows from the calculations above and Lemma 1. The condition \(b_p(n)\ge p\) holds once \(n>p(p-1)\).

Under the shift \(n\mapsto n+pW_{<p}\), the residue \(r\pmod p\) is unchanged, while \(a\) is replaced by \(a+W_{<p}\). Hence the condition is periodic with the asserted period.

In one complete period, there are \(p-B-1\) allowable choices of \(r\), and there are
\[
\varphi(W_{<p})
\]
allowable choices of \(a\bmod W_{<p}\). Thus the number of successful residue classes is
\[
(p-B-1)\varphi(W_{<p}),
\]
out of \(pW_{<p}\) classes. This gives
\[
\delta_{p,B}
=
\frac{p-B-1}{p}\frac{\varphi(W_{<p})}{W_{<p}}
=
\frac{p-B-1}{p}
\prod_{q<p}\left(1-\frac1q\right).
\]
∎

By Mertens’ theorem,
\[
\delta_{p,B}\sim \frac{e^{-\gamma}}{\log p}
\]
as \(p\to\infty\) with \(B\) fixed.

In particular, for every fixed \(B\), there is a positive-density set of \(n\) for which a prescribed prime \(p>B+1\) supplies a witness of distance greater than \(B\). This is far short of pointwise coverage.

---

### 4. A divergent first moment, but exact pointwise holes

For \(Y>B+1\), let
\[
S_{Y,B}(n)
=
\#\left\{
p\in(Y,2Y]:
p\text{ prime and }p\text{ is a successful Route 3 parameter for }n
\right\}.
\]
Let
\[
L_Y=\prod_{q\le2Y}q.
\]
Every individual condition from Lemma 3 has period dividing \(L_Y\).

#### Lemma 4

Over any sufficiently high complete block of length \(L_Y\),
\[
\frac1{L_Y}\sum_{n=M L_Y}^{(M+1)L_Y-1}S_{Y,B}(n)
=
\sum_{\substack{Y<p\le2Y\\p\ \mathrm{prime}}}
\frac{p-B-1}{p}
\prod_{q<p}\left(1-\frac1q\right).
\]
Consequently,
\[
\frac1{L_Y}\sum_{n=M L_Y}^{(M+1)L_Y-1}S_{Y,B}(n)
\sim e^{-\gamma}\frac{Y}{(\log Y)^2}.
\]

#### Proof

For sufficiently large \(M\), the condition \(b_p(n)\ge p\) holds throughout the block for all \(p\le2Y\). The exact identity follows by summing the indicator of each prime \(p\) and applying Lemma 3.

Uniformly for \(Y<p\le2Y\), Mertens’ theorem gives
\[
\prod_{q<p}\left(1-\frac1q\right)
\sim \frac{e^{-\gamma}}{\log Y},
\]
and
\[
\frac{p-B-1}{p}=1+o(1).
\]
The prime number theorem gives
\[
\pi(2Y)-\pi(Y)\sim \frac{Y}{\log Y}.
\]
Multiplication yields the asserted asymptotic. ∎

Thus the average number of Route 3 candidates in one dyadic prime block tends to infinity.

This does not imply pointwise coverage. Indeed, at
\[
n=M L_Y
\]
every prime \(p\le2Y\) divides \(n\), so
\[
d_p(n)=0.
\]
Therefore
\[
S_{Y,B}(M L_Y)=0
\]
for every \(M\), despite the divergent mean.

---

### 5. Primorial obstruction to every bounded-\(p\) argument

The preceding example has a stronger formulation.

#### Lemma 5

Let
\[
W(P)=\prod_{q\le P}q.
\]
If \(W(P)\mid n\), then:

1. no witness for \(n\) can have least prime factor at most \(P\);
2. no distance \(d\) with \(2\le d\le P\) can be admissible.

#### Proof

Suppose \(m=n+d\) is admissible and let \(p=P^-(m)\le P\). Since \(W(P)\mid n\), one has \(p\mid n\). Also \(p\mid m\), so \(p\mid d=m-n\). But admissibility requires
\[
0<d<p,
\]
which is impossible if \(p\mid d\). This proves the first assertion.

Now suppose \(2\le d\le P\). Let \(q\) be any prime divisor of \(d\). Then
\[
q\le d\le P,
\]
so \(q\mid n\). Since also \(q\mid d\), one has \(q\mid n+d\), whence
\[
P^-(n+d)\le q\le d.
\]
Thus \(d\) is not admissible. ∎

Hence any proof using only finitely many primes \(p\), with the finite set depending on \(B\) but not on \(n\), must fail. It also explains why highly divisible \(n\) have an all-or-nothing character: apart from the possible witness \(d=1\), every witness must jump beyond the primorial cutoff.

Taking \(n=W(P)\) and using \(\log W(P)\sim P\), one obtains arbitrarily large \(n\) for which there is no Route 3 candidate with
\[
p\le (1-o(1))\log n.
\]
Thus a universal Route 3 scale must at least be capable of moving beyond logarithmic primorial obstructions.

---

### 6. The residue-depth condition is not the main obstacle

Define
\[
R(n,P)=
\#\left\{
p\in[P,2P]:
\begin{array}{l}
p\text{ prime},\\
P^-\!\left(\left\lceil n/p\right\rceil\right)\ge p
\end{array}
\right\}.
\]
Assume
\[
n\ge4P^2.
\]
Then for every \(p\in[P,2P]\),
\[
\left\lceil\frac np\right\rceil\ge p.
\]

#### Lemma 6

Fix \(B\ge0\). If \(n\ge4P^2\) and
\[
R(n,P)>
\frac{(B+1)\log(n+B)}{\log P},
\]
then \(n\) has an admissible witness at distance greater than \(B\).

#### Proof

For each prime counted by \(R(n,P)\), put
\[
b=\left\lceil\frac np\right\rceil,\qquad d=pb-n.
\]
Then \(0\le d<p\). By Lemma 1, the prime \(p\) gives a valid witness unless \(d=0\); and it gives a witness with distance greater than \(B\) unless \(d\in\{0,1,\dots,B\}\).

If \(d=j\in\{0,\dots,B\}\), then
\[
p\mid n+j.
\]
Thus every bad candidate prime divides
\[
\prod_{j=0}^{B}(n+j).
\]
If there are \(K\) distinct bad primes in \([P,2P]\), then
\[
P^K
\le
\prod_{j=0}^{B}(n+j)
\le
(n+B)^{B+1}.
\]
Taking logarithms gives
\[
K\le\frac{(B+1)\log(n+B)}{\log P}.
\]
If \(R(n,P)\) exceeds this number, at least one candidate has \(d>B\), and Lemma 1 completes the proof. ∎

In particular, if
\[
P=n^\alpha,\qquad 0<\alpha<\frac12,
\]
then the number of candidates lost to \(d\le B\) is at most
\[
\frac{B+1}{\alpha}+o_B(1).
\]
Therefore, for any fixed \(\alpha<1/2\), the uniform estimate
\[
R(n,n^\alpha)\longrightarrow\infty
\]
would solve the problem.

This isolates the real obstruction: obtaining uniformly many \(p\)-rough reciprocal cofactors. The complementary-residue condition costs only \(O_B(1)\) candidates at a polynomial scale.

---

### 7. Separation into a lower-bound sieve and a bilinear correction

For \(b_p=\lceil n/p\rceil\), define
\[
S_0(n,P)
=
\#\left\{
p\in[P,2P]:
p\text{ prime and }P^-(b_p)\ge P
\right\}
\]
and
\[
H(n,P)
=
\#\left\{
p\in[P,2P]:
p\text{ prime and }
P\le P^-(b_p)<p
\right\}.
\]
Then exactly
\[
R(n,P)=S_0(n,P)-H(n,P).
\]

The expected estimates are
\[
S_0(n,P)\gg \frac{P}{(\log P)^2},
\qquad
H(n,P)=o\!\left(\frac{P}{(\log P)^2}\right),
\]
uniformly in \(n\), at a scale such as \(P=n^\alpha\) with \(\alpha<1/3\). Together with Lemma 6, these would solve the problem.

Neither estimate is proved here.

The first is a lower-bound sieve problem for the sequence
\[
\mathcal A_{n,P}
=
\left\{
\left\lceil\frac np\right\rceil:
P\le p\le2P,\ p\text{ prime}
\right\}.
\]
The second requires controlling cofactors whose least prime factor lies in the moving interval \([P,p)\); this is the specifically bilinear correction.

---

### 8. Exact form of the required divisibility counts

For an integer \(d\ge1\), let
\[
A_d(n,P)
=
\#\left\{
p\in[P,2P]:
p\text{ prime and }
d\mid\left\lceil\frac np\right\rceil
\right\}.
\]
Writing \(\lceil n/p\rceil=kd\), one has
\[
\left\lceil\frac np\right\rceil=kd
\quad\Longleftrightarrow\quad
\frac{n}{kd}\le p<\frac{n}{kd-1}.
\]
Consequently,
\[
A_d(n,P)
=
\sum_{k\ge1}
\#\left\{
p\in[P,2P]\cap
\left[
\left\lceil\frac{n}{kd}\right\rceil,
\left\lceil\frac{n}{kd-1}\right\rceil-1
\right]:
p\text{ prime}
\right\},
\]
where terms with \(kd=1\) are omitted.

For relevant \(k\), one has \(kd\asymp n/P\), and each component interval has length
\[
\frac{n}{kd-1}-\frac{n}{kd}
=
\frac{n}{kd(kd-1)}
\asymp \frac{P^2}{n}.
\]
If \(P=o(\sqrt n)\), these component intervals eventually have length less than one. Thus ordinary estimates for primes in intervals do not control \(A_d(n,P)\): one is asking whether a large collection of isolated, arithmetically positioned integers are prime.

A standard lower-bound linear sieve for \(S_0(n,P)\) would seek approximations resembling
\[
A_d(n,P)\approx \frac{\pi(2P)-\pi(P)}d
\]
on average over squarefree \(d\) up to a level \(D>P^{2+\varepsilon}\). The threshold \(D>P^2\) is where the usual one-dimensional lower-bound sieve function becomes positive when sifting to \(P\). Establishing such a pointwise level of distribution for the reciprocal sequence above, followed by a uniform upper bound for \(H(n,P)\), is the unresolved analytic step.

This is not a routine application of existing prime-distribution theorems: the component intervals are generally subunit, and the parameter \(n\) must remain completely pointwise.

## Self-Audit

1. **The average asymptotic uses the prime number theorem and Mertens’ product theorem without reproving them.**  
   These are classical unconditional theorems. The exact periodic density formula in Lemma 3 and exact first-moment identity in Lemma 4 do not depend on their asymptotic forms.

2. **The assertion that a standard lower-bound sieve would require level beyond \(P^2\) is methodological, not an impossibility theorem.**  
   It refers specifically to the usual dimension-one linear-sieve framework, where the lower sieve function is positive only for sieve parameter \(s=\log D/\log P>2\). A different method could bypass this requirement; I do not claim otherwise.

3. **The diagnosis that the remaining reciprocal-sieve estimate is “comparable to the original problem” is not itself proved.**  
   What is rigorous is Lemma 6: a sufficiently large uniform lower bound for \(R(n,P)\) solves the problem. The assessment of difficulty is based on the exact subunit-interval formula for \(A_d(n,P)\), the primorial pointwise holes, and the need for uniformity in every \(n\), but it is not a formal no-go theorem.

## Computations To Verify

The following code computes \(D(n)\), enumerates the exact Route 3 parameters, checks Lemma 1 computationally, separates prime and composite cofactors, and measures the proposed sieve quantities.

```python
from math import isqrt, gcd, log, prod

def spf_sieve(N):
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def prime_list_from_spf(spf):
    return [p for p in range(2, len(spf)) if spf[p] == p]

def direct_witnesses(n, spf):
    """Returns all admissible (d,m,least_prime_factor)."""
    out = []
    d = 1
    while d * d < n + d:
        m = n + d
        if spf[m] < m and spf[m] > d:
            out.append((d, m, spf[m]))
        d += 1
    return out

def D_value(n, spf):
    W = direct_witnesses(n, spf)
    return max((d for d, m, p in W), default=0)

def route3_witnesses(n, spf, primes):
    """
    Enumerates all p for which:
      b = ceil(n/p) >= p,
      every prime factor of b is >= p,
      d = pb-n is positive.
    """
    out = []
    for p in primes:
        # Once p^2 is too large, b < p.
        if p * p > n + p:
            break
        b = (n + p - 1) // p
        d = p * b - n
        if d == 0 or b < p:
            continue
        if spf[b] >= p:
            out.append({
                "p": p,
                "b": b,
                "d": d,
                "m": p * b,
                "cofactor_composite": spf[b] < b
            })
    return out

def verify_route3_equivalence(N):
    # Enough for all m=n+d and all b <= n.
    limit = N + isqrt(N) + 10
    spf = spf_sieve(limit)
    primes = prime_list_from_spf(spf)

    for n in range(1, N + 1):
        direct = {(d, spf[n+d]) for d, m, p in direct_witnesses(n, spf)}
        route = {(x["d"], x["p"]) for x in route3_witnesses(n, spf, primes)}
        assert direct == route, (n, direct, route)
    return True
```

Check the cube-root restriction:

```python
def verify_composite_cofactor_bound(N):
    limit = N + isqrt(N) + 10
    spf = spf_sieve(limit)
    primes = prime_list_from_spf(spf)

    for n in range(1, N + 1):
        for x in route3_witnesses(n, spf, primes):
            if x["cofactor_composite"]:
                p = x["p"]
                assert p**3 - p + 1 <= n, (n, x)
    return True
```

Check the exact fixed-\(p\) periodic density:

```python
def primes_below(p):
    spf = spf_sieve(p)
    return [q for q in range(2, p) if spf[q] == q]

def fixed_p_period_check(p, B):
    assert p > B + 1
    qs = primes_below(p)
    W = prod(qs)
    period = p * W

    count = 0
    for n in range(period):
        a, r = divmod(n, p)
        if 1 <= r <= p - B - 1 and gcd(a + 1, W) == 1:
            count += 1

    expected = (p - B - 1) * sum(1 for a in range(W) if gcd(a + 1, W) == 1)
    assert count == expected
    return {
        "period": period,
        "count": count,
        "density": count / period,
        "formula_density": ((p - B - 1) / p) *
                           prod((q - 1) / q for q in qs)
    }
```

Compute \(S_0,H,R\), and the number of candidates lost only because of small depth:

```python
def route3_scale_counts(n, P, B, spf, primes):
    S0 = 0   # least factor of b >= P
    H = 0    # P <= least factor of b < p
    R = 0    # least factor of b >= p
    bad_depth = 0
    composite_cofactor_R = 0

    for p in primes:
        if p < P:
            continue
        if p > 2 * P:
            break

        b = (n + p - 1) // p
        if b < p:
            continue

        lam = spf[b]
        d = p * b - n

        if lam >= P:
            S0 += 1
        if P <= lam < p:
            H += 1
        if lam >= p:
            R += 1
            if d <= B:
                bad_depth += 1
            if lam < b:
                composite_cofactor_R += 1

    assert R == S0 - H
    return {
        "S0": S0,
        "H": H,
        "R": R,
        "bad_depth": bad_depth,
        "good_depth": R - bad_depth,
        "composite_cofactor_R": composite_cofactor_R,
        "residue_bound":
            (B + 1) * log(n + B) / log(P) if P > 1 else None
    }
```

Compute the decisive block minima and determine which \(p\)-scales supply witnesses:

```python
def block_statistics(N, B_values=(0, 1, 2, 5, 10)):
    limit = N + isqrt(N) + 10
    spf = spf_sieve(limit)
    primes = prime_list_from_spf(spf)

    D = [0] * (N + 1)
    source = [None] * (N + 1)

    for n in range(1, N + 1):
        W = route3_witnesses(n, spf, primes)
        if W:
            best = max(W, key=lambda x: x["d"])
            D[n] = best["d"]
            source[n] = best

    X = 1
    blocks = []
    while 2 * X <= N:
        vals = D[X:2*X + 1]
        row = {
            "X": X,
            "min_D": min(vals),
            "argmin": X + vals.index(min(vals)),
            "counts_low": {
                B: sum(1 for v in vals if v <= B)
                for B in B_values
            }
        }
        blocks.append(row)
        X *= 2

    return D, source, blocks
```

Test the primorial obstruction:

```python
def primorial_obstruction(P, multiplier=1):
    spf_small = spf_sieve(P)
    small_primes = prime_list_from_spf(spf_small)
    n = multiplier * prod(small_primes)

    for p in small_primes:
        b = (n + p - 1) // p
        d = p * b - n
        assert d == 0

    # Directly verify that 2 <= d <= P cannot work using a factor of d.
    for d in range(2, P + 1):
        q = spf_small[d]
        assert n % q == 0
        assert (n + d) % q == 0
        assert q <= d

    return n
```

The most informative numerical outputs would be:

1. \(\min_{X\le n\le2X}D(n)\);
2. \(\min_{X\le n\le2X}R(n,\lfloor n^\alpha\rfloor)\);
3. the ratio \(H/S_0\) for low-\(R\) values of \(n\);
4. the proportion of Route 3 witnesses with composite cofactors, grouped by \(p/n^{1/3}\);
5. arithmetic structure, especially primorial divisibility, of values attaining block-minimal \(R\) or \(D\).

## Route Diagnosis

**Proved ledger.**

- Every witness is represented uniquely by a prime \(p\) and the rough cofactor \(\lceil n/p\rceil\).
- Composite cofactors force \(p^3-p+1\le n\); hence Route 3 differs from the semiprime route only below the cube-root scale.
- For fixed \(p\), successful \(n\) form an explicitly periodic set of density
  \[
  \frac{p-B-1}{p}\prod_{q<p}\left(1-\frac1q\right).
  \]
- The mean number of successful \(p\in[Y,2Y]\) is asymptotic to
  \[
  e^{-\gamma}Y/(\log Y)^2.
  \]
- Multiples of the primorial through \(P\) have no witness with least factor at most \(P\), and no admissible distance in \([2,P]\).
- At polynomial \(P\), only \(O_B(1)\) rough-cofactor candidates can be lost because their distance is at most \(B\).

**Plausible but unproved claims.**

- At some scale \(P=n^\alpha\), preferably \(\alpha<1/3\),
  \[
  S_0(n,P)\gg P/(\log P)^2
  \]
  uniformly in every \(n\).
- Uniformly,
  \[
  H(n,P)=o(P/(\log P)^2).
  \]
- Equivalently, \(R(n,P)\to\infty\) uniformly at some polynomial scale.

These claims would solve the problem by Lemma 6, but they are pointwise reciprocal-sieve statements of essentially the same strength as the desired conclusion.

**Dead ends.**

- A finite family of primes \(p\) cannot cover all \(n\): multiples of its primorial defeat every member simultaneously.
- A divergent average number of candidates does not give pointwise coverage; primorial multiples are exact holes even inside a period with very large mean.
- Taking \(p\) near \(\sqrt n\) does not exploit composite cofactors; there Route 3 is just the semiprime problem.
- A routine lower-bound sieve is blocked by the need to control divisibility of \(\lceil n/p\rceil\) to level beyond \(P^2\), while the relevant prime sets are unions of subunit intervals.
- Switching to Route 1 does not remove the obstruction: a Route 3 candidate at scale \(P\) is precisely a composite \(P\)-rough number in a translated interval of length \(O(P)\), with its least factor in the chosen scale.

**Best next attempt.**

A fresh analytic attempt should choose \(P=n^\alpha\) with \(\alpha<1/3\), and likely \(\alpha<1/4\), then:

1. establish a dispersion or Harman-sieve estimate for
   \[
   A_d(n,P)=
   \sum_{\substack{P<p\le2P\\p\ \mathrm{prime}}}
   1_{d\mid\lceil n/p\rceil}
   \]
   averaged over squarefree \(d\) beyond \(P^2\), uniformly in the pointwise parameter \(n\);
2. apply a lower-bound sieve to obtain many \(P\)-rough cofactors;
3. use Buchstab decomposition and a bilinear upper bound to remove cofactors with least factor in \([P,p)\);
4. invoke Lemma 6 to discard the boundedly many candidates with distance at most \(B\).

Absent such a reciprocal level-of-distribution theorem, Route 3 is blocked rather than completed.