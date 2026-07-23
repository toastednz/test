STATUS: BLOCKED

## Result

Route 1 yields a strong but non-pointwise result. I prove an exact mean-square estimate for the number of \(z\)-rough integers in any interval of \(H\) consecutive offsets, averaged over the translation modulo the primorial \(Q_z=\prod_{p\le z}p\). As a consequence, for every fixed \(c<1\),
\[
\#\{X\le n\le 2X:D(n)\le c\log n\}
\ll_c \frac{X\log\log X}{\log X}.
\]
Thus \(D(n)\to\infty\) in density, and indeed \(D(n)\ge (1-o(1))\log n\) in the density sense. This does not prove the required pointwise convergence. The obstruction is genuine: at every fixed logarithmic sieve scale there are arbitrarily large translations with no rough survivors at all, and standard lower-bound sieve methods operate below their nontrivial range when the interval length and sieve threshold are comparable.

## Complete Argument

### 1. Route 1 in fixed-threshold form

For an integer \(z\ge3\), define
\[
Q_z=\prod_{p\le z}p,
\qquad
V(z)=\frac{\varphi(Q_z)}{Q_z}
=\prod_{p\le z}\left(1-\frac1p\right).
\]

Let \(\mathcal I\) be an interval of \(H\) consecutive integer offsets, all at most \(z\), and set
\[
S_{z,\mathcal I}(n)
=
\#\{d\in\mathcal I:\gcd(n+d,Q_z)=1\}.
\]

If \(n>z\), then every number counted by \(S_{z,\mathcal I}(n)\) has no prime divisor at most \(z\). Hence
\[
S_{z,\mathcal I}(n)
=
\#\{d\in\mathcal I:n+d\text{ is prime}\}
+
\#\{d\in\mathcal I:n+d\text{ is composite},\ P^-(n+d)>z\}.
\]
Because \(d\le z\), every composite in the second set is a valid witness:
\[
P^-(n+d)>z\ge d.
\]

For the exact dyadic proposal in Route 1, take \(z=2y\) and
\[
\mathcal I=[y,2y]\cap\mathbb Z.
\]
Then the excess of rough values over primes is exactly the number of composite witnesses produced by that dyadic range.

---

### 2. Mean-square theorem for rough survivors

#### Lemma 1

Uniformly for integers \(z\ge3\), \(H\ge1\), and every interval \(\mathcal I\) of \(H\) consecutive integers,
\[
\frac1{Q_z}\sum_{a\bmod Q_z}S_{z,\mathcal I}(a)=H V(z),
\]
and
\[
\operatorname{Var}_{a\bmod Q_z} S_{z,\mathcal I}(a)
\ll H V(z)+H V(z)^2\log z.
\]
Consequently,
\[
\frac1{Q_z}
\#\left\{a\bmod Q_z:
S_{z,\mathcal I}(a)<\frac12HV(z)\right\}
\ll \frac{\log z}{H}.
\]

#### Proof

Translation of \(\mathcal I\) does not affect any of the calculations, so write
\[
\mathcal I=\{1,\dots,H\}.
\]

For each fixed \(d\), exactly \(\varphi(Q_z)\) residue classes \(a\bmod Q_z\) satisfy
\[
\gcd(a+d,Q_z)=1.
\]
Thus
\[
\mathbb E S_{z,\mathcal I}=HV(z).
\]

For \(h\ne0\), define
\[
C_z(h)=
\frac1{Q_z}
\#\{a\bmod Q_z:(a,Q_z)=(a+h,Q_z)=1\}.
\]
By the Chinese remainder theorem, this factors into local densities. For a prime \(p\le z\),

- if \(p\mid h\), one residue class modulo \(p\) is forbidden, giving local density \(1-1/p\);
- if \(p\nmid h\), two distinct residue classes are forbidden, giving local density \(1-2/p\).

Hence
\[
C_z(h)
=
\prod_{\substack{p\le z\\p\mid h}}\left(1-\frac1p\right)
\prod_{\substack{p\le z\\p\nmid h}}\left(1-\frac2p\right).
\]

Put
\[
T_z(h)=\frac{C_z(h)}{V(z)^2}.
\]
If \(h\) is odd, the local factor at \(p=2\) vanishes, so \(T_z(h)=0\). If \(h\) is even, then
\[
T_z(h)
=
2c_z
\prod_{\substack{2<p\le z\\p\mid h}}
\left(1+\frac1{p-2}\right),
\]
where
\[
c_z=\prod_{2<p\le z}\frac{p(p-2)}{(p-1)^2}.
\]
Expanding the product gives
\[
T_z(h)
=
2c_z\,1_{2\mid h}
\sum_{\substack{d\mid h\\d\mid Q_z/2}}
g(d),
\qquad
g(d)=\prod_{p\mid d}\frac1{p-2}.
\]

Therefore, for every \(L\ge1\),
\[
\begin{aligned}
\sum_{h\le L}T_z(h)
&=
2c_z
\sum_{d\mid Q_z/2}
g(d)\left\lfloor\frac{L}{2d}\right\rfloor\\
&=
c_zL\sum_{d\mid Q_z/2}\frac{g(d)}d
+
O\left(c_z\sum_{d\mid Q_z/2}g(d)\right).
\end{aligned}
\]

The main Euler product equals one:
\[
\begin{aligned}
c_z\sum_{d\mid Q_z/2}\frac{g(d)}d
&=
\prod_{2<p\le z}
\frac{p(p-2)}{(p-1)^2}
\left(1+\frac1{p(p-2)}\right)\\
&=
\prod_{2<p\le z}
\frac{p(p-2)+1}{(p-1)^2}
=1.
\end{aligned}
\]

For the error term,
\[
\sum_{d\mid Q_z/2}g(d)
=
\prod_{2<p\le z}\left(1+\frac1{p-2}\right).
\]
For \(p\ge5\),
\[
\frac1{p-2}=\frac1p+O\left(\frac1{p^2}\right).
\]
Using the classical bound
\[
\sum_{p\le z}\frac1p\le \log\log z+O(1),
\]
we obtain
\[
\prod_{2<p\le z}\left(1+\frac1{p-2}\right)\ll\log z.
\]
It follows that, uniformly in \(L\),
\[
\sum_{h\le L}T_z(h)=L+O(\log z).
\]

By summation,
\[
\begin{aligned}
\sum_{h=1}^{H-1}(H-h)T_z(h)
&=
\sum_{L=1}^{H-1}\sum_{h\le L}T_z(h)\\
&=
\sum_{L=1}^{H-1}\bigl(L+O(\log z)\bigr)\\
&=
\frac{H(H-1)}2+O(H\log z).
\end{aligned}
\]

There are \(H-h\) ordered pairs of offsets at positive difference \(h\). Thus
\[
\begin{aligned}
\mathbb E S_{z,\mathcal I}^2
&=
HV(z)+2\sum_{h=1}^{H-1}(H-h)C_z(h)\\
&=
HV(z)+V(z)^2H(H-1)
+O\bigl(V(z)^2H\log z\bigr).
\end{aligned}
\]
Subtracting \(H^2V(z)^2\) gives
\[
\operatorname{Var} S_{z,\mathcal I}
\ll HV(z)+HV(z)^2\log z.
\]

By Mertens’ theorem,
\[
V(z)\asymp\frac1{\log z}.
\]
Therefore
\[
\frac{\operatorname{Var}S_{z,\mathcal I}}
{H^2V(z)^2}
\ll \frac{\log z}{H}.
\]
Chebyshev’s inequality now gives
\[
\frac1{Q_z}
\#\left\{a:
S_{z,\mathcal I}(a)<\frac12HV(z)\right\}
\le
4\frac{\operatorname{Var}S_{z,\mathcal I}}
{H^2V(z)^2}
\ll\frac{\log z}{H}.
\]
This proves the lemma. ∎

---

### 3. Almost-all logarithmic witnesses

#### Theorem 2

For every fixed \(c<1\),
\[
\#\{n\in[X,2X]\cap\mathbb Z:D(n)\le c\log n\}
\ll_c \frac{X\log\log X}{\log X}.
\]

In particular, for every fixed \(B\),
\[
\#\{n\le X:D(n)\le B\}=o(X).
\]

#### Proof

Fix \(c<1\). Choose constants \(\lambda,\eta\in(0,1)\) such that
\[
(1-\eta)\lambda>c.
\]
For example, first choose \(c<\lambda<1\), then choose \(\eta>0\) sufficiently small.

Put
\[
z=\lfloor\lambda\log X\rfloor,
\qquad
H=\lfloor\eta z\rfloor,
\]
and take the offsets
\[
\mathcal I=\{z-H+1,\dots,z\}.
\]
For all sufficiently large \(X\), every \(d\in\mathcal I\) satisfies
\[
d>c\log n
\qquad(X\le n\le2X).
\]

Let
\[
Q=Q_z,\qquad \mu=H V(z).
\]
By the prime number theorem in the form
\[
\log Q=\vartheta(z)=z+o(z),
\]
we have
\[
Q=X^{\lambda+o(1)}=o(X).
\]

By Lemma 1, the number of residue classes \(a\bmod Q\) for which
\[
S_{z,\mathcal I}(a)<\frac12\mu
\]
is
\[
\ll Q\frac{\log z}{H}.
\]
Each residue class modulo \(Q\) occurs at most \(X/Q+1\) times in \([X,2X]\). Hence the number of \(n\in[X,2X]\) satisfying
\[
S_{z,\mathcal I}(n)<\frac12\mu
\]
is
\[
\ll (X+Q)\frac{\log z}{H}
\ll \frac{X\log\log X}{\log X}.
\]

It remains to consider \(n\) for which
\[
S_{z,\mathcal I}(n)\ge\frac12\mu
\quad\text{and}\quad
D(n)\le c\log n.
\]
For each offset \(d\) counted by \(S_{z,\mathcal I}(n)\), the integer \(n+d\) has no prime factor at most \(z\). If \(n+d\) were composite, then
\[
P^-(n+d)>z\ge d>c\log n,
\]
so \(d\) would be a valid witness contradicting \(D(n)\le c\log n\). Therefore all the \(S_{z,\mathcal I}(n)\) survivors must be prime.

The total number of pairs
\[
(n,d),\qquad X\le n\le2X,\quad d\in\mathcal I,\quad n+d\text{ prime},
\]
is at most
\[
H\pi(3X)\ll \frac{HX}{\log X},
\]
using the standard Chebyshev upper bound for \(\pi(x)\).

Every exceptional \(n\) presently under consideration contributes at least \(\mu/2\) such pairs. Their number is therefore at most
\[
\frac{2}{\mu}\frac{HX}{\log X}
\ll
\frac{X}{V(z)\log X}
\ll
\frac{X\log z}{\log X}
\ll
\frac{X\log\log X}{\log X}.
\]

Combining the two exceptional sets proves the theorem. ∎

This is stronger than merely showing \(D(n)\to\infty\) in density: for each fixed \(c<1\), almost all \(n\) satisfy
\[
D(n)>c\log n.
\]

---

### 4. A pointwise obstruction at every fixed logarithmic scale

The averaging in Lemma 1 cannot be upgraded to a uniform positive lower bound at one fixed scale.

#### Proposition 3

Let \(z\ge3\), and suppose
\[
Q_z\mid n.
\]
Then for every integer \(d\) with
\[
2\le d\le z,
\]
one has
\[
\gcd(n+d,Q_z)>1.
\]
Thus there are no \(z\)-rough values among \(n+2,\dots,n+z\).

#### Proof

Choose any prime \(q\mid d\). Then \(q\le d\le z\), so \(q\mid Q_z\), and consequently \(q\mid n\). Since also \(q\mid d\),
\[
q\mid n+d.
\]
Thus \(\gcd(n+d,Q_z)\ge q>1\). ∎

This obstruction occurs at the natural logarithmic scale for arbitrarily large \(n\). Fix \(0<\lambda<1\), and define
\[
n_z
=
Q_z\left\lceil\frac{\exp(z/\lambda)}{Q_z}\right\rceil.
\]
Since
\[
Q_z=\exp((1+o(1))z)
=o\bigl(\exp(z/\lambda)\bigr),
\]
we have
\[
n_z=\exp(z/\lambda)(1+o(1))
\]
and therefore
\[
\lambda\log n_z=z+o(1).
\]
Moreover \(\lambda\log n_z\ge z\), so eventually
\[
\lfloor\lambda\log n_z\rfloor=z.
\]
Yet all offsets \(2\le d\le z\) are blocked by Proposition 3.

For even \(z=2y\), this includes the exact Route 1 range
\[
y\le d\le2y.
\]
Hence no pointwise theorem can simply prescribe one scale \(2y\sim\lambda\log n\) and assert the existence of even a rough survivor, let alone a composite one. Other scales may still work, so this is not a disproof of the original problem.

## Self-Audit

1. **The mean-square proof relies on classical Mertens and prime-number estimates rather than reproving them.**  
   Specifically, I use \(V(z)\asymp1/\log z\), \(\sum_{p\le z}1/p\le\log\log z+O(1)\), and \(\vartheta(z)\sim z\). These are standard unconditional theorems. The argument needs no unproved hypothesis, and weaker classical versions would suffice after choosing a smaller constant in the logarithmic scale.

2. **The singular-series calculation is the most delicate algebraic step, especially at \(p=2\).**  
   The parity factor is treated separately: \(T_z(h)=0\) for odd \(h\), while even \(h\) contributes an extra factor \(2\). The Euler-product cancellation
   \[
   \frac{p(p-2)}{(p-1)^2}
   \left(1+\frac1{p(p-2)}\right)=1
   \]
   is exact. This calculation can also be checked exhaustively for small primorials using the code below.

3. **The almost-all theorem gives no control over the individual exceptional translations.**  
   The counting argument is valid because it exhaustively splits exceptional \(n\) into those with too few rough survivors and those for which every survivor is prime. However, the bound remains of order \(X\log\log X/\log X\), which is enormous compared with \(1\). Nothing proved here excludes infinitely many exceptional \(n\), so this cannot be promoted to a solution.

## Computations To Verify

The following code verifies \(D(n)\), the exact rough/prime decomposition, the mean and variance formulas, and the CRT obstruction.

```python
from math import gcd, isqrt, log, prod
from fractions import Fraction

def primes_upto(N):
    sieve = bytearray(b"\x01") * (N + 1)
    if N >= 0:
        sieve[0] = 0
    if N >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(N) + 1):
        if sieve[p]:
            sieve[p*p:N+1:p] = b"\x00" * (((N - p*p) // p) + 1)
    return [p for p in range(2, N + 1) if sieve[p]]

def spf_sieve(N):
    spf = list(range(N + 1))
    if N >= 1:
        spf[1] = 1
    for p in range(2, isqrt(N) + 1):
        if spf[p] == p:
            for m in range(p*p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf

def D_value(n, spf):
    ans = 0
    d = 1
    while d*d < n + d:
        m = n + d
        if spf[m] < m and spf[m] > d:
            ans = d
        d += 1
    return ans
```

Exact verification of the mean-square setup:

```python
def verify_moments(z, H, start=1):
    ps = primes_upto(z)
    Q = prod(ps)
    I = list(range(start, start + H))

    S = [
        sum(gcd(a + d, Q) == 1 for d in I)
        for a in range(Q)
    ]

    V = Fraction(1, 1)
    for p in ps:
        V *= Fraction(p - 1, p)

    mean = Fraction(sum(S), Q)
    second = Fraction(sum(s*s for s in S), Q)
    variance = second - mean*mean

    assert mean == H * V

    # Verify every pair-correlation formula directly.
    for h in range(1, H):
        direct = Fraction(
            sum(gcd(a, Q) == 1 and gcd(a + h, Q) == 1
                for a in range(Q)),
            Q
        )

        local = Fraction(1, 1)
        for p in ps:
            if h % p == 0:
                local *= Fraction(p - 1, p)
            else:
                local *= Fraction(p - 2, p)
        assert direct == local

    return {
        "Q": Q,
        "mean": mean,
        "variance": variance,
        "relative_variance": float(variance / (mean*mean))
    }

for z in [5, 7, 11, 13, 17, 19]:
    print(z, verify_moments(z, H=max(2, z // 2)))
```

Verification that rough survivors minus primes equals rough composites:

```python
def route1_counts(n, y, spf):
    z = 2*y
    rough = []
    rough_primes = []
    rough_composites = []

    for d in range(y, 2*y + 1):
        m = n + d
        if spf[m] > z:
            rough.append(d)
            if spf[m] == m:
                rough_primes.append(d)
            else:
                rough_composites.append(d)
                assert spf[m] > d  # valid witness

    assert len(rough) - len(rough_primes) == len(rough_composites)
    return rough, rough_primes, rough_composites
```

Empirical test of the almost-all logarithmic conclusion:

```python
def test_dyadic_block(X, c=0.4, lam=0.8, eta=0.25):
    z = int(lam * log(X))
    H = int(eta * z)
    offsets = range(z - H + 1, z + 1)

    M = 2*X + z + 10
    spf = spf_sieve(M)

    few_rough = 0
    no_composite_survivor = 0
    exact_low_D = 0

    ps = primes_upto(z)
    V = 1.0
    for p in ps:
        V *= 1.0 - 1.0/p
    mu = H * V

    for n in range(X, 2*X + 1):
        rough = [d for d in offsets if spf[n+d] > z]
        comp = [d for d in rough if spf[n+d] < n+d]

        if len(rough) < mu / 2:
            few_rough += 1
        if not comp:
            no_composite_survivor += 1
        if D_value(n, spf) <= c * log(n):
            exact_low_D += 1

    return {
        "X": X,
        "z": z,
        "few_rough": few_rough,
        "no_composite_survivor": no_composite_survivor,
        "D_le_c_log_n": exact_low_D
    }
```

CRT obstruction:

```python
def verify_crt_obstruction(z, multiplier=1):
    Q = prod(primes_upto(z))
    n = multiplier * Q
    assert all(gcd(n + d, Q) > 1 for d in range(2, z + 1))
    return n, Q

for z in [10, 20, 30]:
    print(verify_crt_obstruction(z))
```

A decisive pointwise computation should scan multiple scales rather than one:

```python
def successful_route1_scales(n, spf, y_min, y_max):
    out = []
    for y in range(y_min, y_max + 1):
        comp = []
        for d in range(y, 2*y + 1):
            m = n + d
            if spf[m] < m and spf[m] > 2*y:
                comp.append(d)
        if comp:
            out.append((y, max(comp)))
    return out

# For dyadic blocks [X,2X], record n for which this list is empty
# over y_min <= y <= n**alpha, with alpha < 1/2.
```

## Route Diagnosis

**Proved ledger**

1. The Route 1 excess
   \[
   \#\{\text{\(z\)-rough values}\}-\#\{\text{prime values}\}
   \]
   is exactly the number of rough composite witnesses when all offsets are at most \(z\).

2. The rough-survivor count has mean \(HV(z)\) and relative variance
   \[
   \ll \frac{\log z}{H}
   \]
   over translations modulo \(Q_z\).

3. For every \(c<1\),
   \[
   D(n)>c\log n
   \]
   for all but \(O_c(X\log\log X/\log X)\) integers \(n\in[X,2X]\).

4. Every fixed logarithmic sieve scale has arbitrarily large CRT translations with no rough survivors.

**Plausible but unproved claims**

- A multi-scale statement may hold: for every sufficiently large \(n\), some \(z=o(\sqrt n)\) may have substantially more rough survivors than primes.
- Exceptional sets at many nested primorial scales may have sufficiently weak intersection to yield a pointwise result.
- Neither claim follows from the present second-moment estimates.

**Dead ends**

1. **Uniform lower-bound sieve at one scale.**  
   Here the interval length \(H\) and sieve threshold \(z\) are comparable. The natural distribution level is at most about \(H\), so the linear-sieve parameter
   \[
   s=\frac{\log D}{\log z}
   \]
   is approximately \(1\). The lower-bound linear sieve is trivial for \(s\le2\). Proposition 3 shows this is not merely a defect in constants: some translations have no survivors.

2. **Pointwise comparison with primes.**  
   Brun–Titchmarsh-type upper bounds in an interval of length \(H\) are of order \(H/\log H\), the same scale as the expected rough count. They do not exploit the much smaller expected prime density \(1/\log n\) when \(H=n^{o(1)}\). Averaging over \(n\) resolves this, but pointwise control remains a parity-type obstacle.

3. **Fixing \(z\asymp\log n\).**  
   The explicit primorial construction defeats every prescribed scale \(z=\lfloor\lambda\log n\rfloor\) with \(0<\lambda<1\).

The route is therefore blocked precisely at the transition from average translation control to a statement for every translation. A fresh Route 1 attempt should study intersections of exceptional sets across many sieve scales, rather than improve the one-scale variance. Failing that, the most promising change is Route 3: exploit bilinear structure in
\[
p\left\lceil\frac np\right\rceil
\]
to manufacture compositeness directly, since ordinary one-dimensional sieving cannot cross the prime/composite parity barrier here.