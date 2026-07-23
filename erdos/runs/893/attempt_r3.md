STATUS: BLOCKED

## Result

Route 3 succeeds completely for the Zsigmondy lower-bound surrogate: if \(G(n)=\sum_{k\le n}2^{\tau(k)}\), then
\[
\frac{G(2n)-G(n)}{G(n)}\longrightarrow\infty.
\]
Thus every dyadic interval contains enough divisor-rich exponents to dominate all earlier such certificates. However, this does not control \(f(n)\), because the excess of \(\tau(2^k-1)\) over its primitive-prime certificate can concentrate at arithmetically poor exponents. I isolate the missing weighted anti-concentration statement, prove several exact reductions, and construct an abstract sequence satisfying the Route 3 lower bounds, divisibility monotonicity, and doubling inequality while having bounded dyadic ratios along a subsequence. Therefore Route 3, using only its advertised ingredients, is blocked.

## Complete Argument

### 1. The primitive-prime certificate

Define
\[
\lambda(k)=2^{\tau(k)-1-\mathbf 1_{6\mid k}}.
\]

#### Lemma 1
For every \(k\ge1\),
\[
b_k=\tau(2^k-1)\ge \lambda(k).
\]

#### Proof
For every divisor \(d\mid k\) with \(d>1\) and \(d\ne6\), Bang–Zsigmondy supplies a prime \(p_d\mid 2^d-1\) that divides no \(2^j-1\) with \(1\le j<d\). Hence
\[
\operatorname{ord}_{p_d}(2)=d.
\]
As \(d\mid k\), every \(p_d\) divides \(2^k-1\). The primes \(p_d\) are distinct because they have distinct orders.

There are
\[
\tau(k)-1-\mathbf 1_{6\mid k}
\]
eligible divisors \(d\). Consequently \(2^k-1\) has at least that many distinct prime factors and therefore at least
\[
2^{\tau(k)-1-\mathbf 1_{6\mid k}}
\]
squarefree divisors. This proves the claim. For \(k=1\), both sides equal \(1\). ∎

Let
\[
H(n)=\sum_{k\le n}\lambda(k),
\qquad
G(n)=\sum_{k\le n}2^{\tau(k)}.
\]
Termwise,
\[
\frac14\,2^{\tau(k)}
\le \lambda(k)\le \frac12\,2^{\tau(k)},
\]
so
\[
\frac14G(n)\le H(n)\le\frac12G(n).
\]

The exceptional case is harmless but necessary: for example,
\[
\lambda(6)=2^{4-1-1}=4\le b_6=6.
\]

---

### 2. Every dyadic interval contains an improved divisor maximum

Put
\[
D(n)=\max_{k\le n}\tau(k).
\]

#### Lemma 2
If \(m\le n\) satisfies \(\tau(m)=D(n)\), then \(m>n/2\). Writing
\[
m=2^a u,\qquad u\ \text{odd},
\]
one has
\[
\tau(2m)=D(n)+\frac{D(n)}{a+1},
\]
where
\[
a+1\le \log_2 n+1.
\]

#### Proof
If \(2m\le n\), then
\[
\tau(2m)=\frac{a+2}{a+1}\tau(m)>\tau(m)=D(n),
\]
contradicting the definition of \(D(n)\). Hence \(n<2m\le2n\).

Since
\[
\tau(m)=(a+1)\tau(u),
\qquad
\tau(2m)=(a+2)\tau(u),
\]
we obtain
\[
\tau(2m)-\tau(m)=\tau(u)=\frac{D(n)}{a+1}.
\]
Finally \(2^a\le m\le n\), so \(a\le\log_2n\). ∎

We need a crude but sufficiently rapid lower bound for \(D(n)\).

#### Lemma 3
For \(n\) sufficiently large,
\[
D(n)\ge 2^{\lfloor\sqrt{\log_2 n}\rfloor}.
\]

#### Proof
Let \(p_i\) be the \(i\)-th prime. Bertrand’s postulate implies inductively that
\[
p_i\le2^i.
\]
Set
\[
s=\lfloor\sqrt{\log_2n}\rfloor.
\]
Then
\[
\prod_{i=1}^s p_i
\le 2^{s(s+1)/2}\le n
\]
for sufficiently large \(n\). This product is squarefree with \(s\) prime factors, so it has \(2^s\) divisors. Hence \(D(n)\ge2^s\). ∎

---

### 3. Route 3 completely solves the exponent surrogate

#### Theorem 4
One has
\[
\boxed{
\frac{\sum_{n<k\le2n}2^{\tau(k)}}
{\sum_{k\le n}2^{\tau(k)}}\longrightarrow\infty.
}
\]
The same conclusion holds with \(2^{\tau(k)}\) replaced by \(\lambda(k)\):
\[
\boxed{
\frac{H(2n)-H(n)}{H(n)}\longrightarrow\infty.
}
\]

#### Proof
Choose \(m\le n\) with \(\tau(m)=D(n)\), and write \(m=2^au\). By Lemma 2, \(2m\in(n,2n]\). Therefore
\[
G(2n)-G(n)\ge2^{\tau(2m)}
=2^{D(n)+D(n)/(a+1)}.
\]
On the other hand,
\[
G(n)\le n\,2^{D(n)}.
\]
It follows that
\[
\frac{G(2n)-G(n)}{G(n)}
\ge
\frac{2^{D(n)/(a+1)}}{n}
\ge
\frac{2^{D(n)/(\log_2n+1)}}{n}.
\]

Let \(x=\log_2n\). Lemma 3 gives
\[
D(n)\ge 2^{\lfloor\sqrt{x}\rfloor}.
\]
Thus the base-\(2\) logarithm of the last lower bound is at least
\[
\frac{2^{\lfloor\sqrt{x}\rfloor}}{x+1}-x,
\]
which tends to \(+\infty\), because \(2^{\sqrt{x}}\) grows faster than every power of \(x\). This proves the first assertion.

For the second, use
\[
H(2n)-H(n)\ge\frac14\bigl(G(2n)-G(n)\bigr),
\qquad
H(n)\le\frac12G(n).
\]
Hence
\[
\frac{H(2n)-H(n)}{H(n)}
\ge
\frac12\frac{G(2n)-G(n)}{G(n)}
\longrightarrow\infty.
\]
∎

In particular, the divisor-rich exponents in every dyadic interval are not lacunary when measured by Route 3’s own certificate. This removes one possible failure mode of Route 3.

---

### 4. The precise missing comparison with \(f(n)\)

By Lemma 1,
\[
f(n)\ge H(n).
\]
Define the uncontrolled excess factor
\[
Q(n)=\frac{f(n)}{H(n)}\ge1
\]
and the certified dyadic amplification
\[
A(n)=\frac{H(2n)-H(n)}{H(n)}.
\]
Theorem 4 proves \(A(n)\to\infty\), quantitatively
\[
A(n)\ge
\frac{2^{D(n)/(\log_2n+1)-1}}{n}.
\]

Since
\[
f(2n)-f(n)
=\sum_{n<k\le2n}b_k
\ge H(2n)-H(n),
\]
we obtain the rigorous lower bound
\[
\boxed{
R(n)\ge1+\frac{A(n)}{Q(n)}.
}
\]

Thus Route 3 would solve the problem if one could prove, for example,
\[
Q(n)=o(A(n)).
\]
No such estimate is currently available.

The scale mismatch is severe. Wigert’s theorem applied to the exponents themselves gives
\[
D(n)=
\exp\!\left((\log2+o(1))
\frac{\log n}{\log\log n}\right)
=n^{o(1)}.
\]
Consequently
\[
\log H(2n)=n^{o(1)}.
\]
In contrast, the available generic upper bound for \(f(n)\) is
\[
\log f(n)\le
\left((\log2)^2+o(1)\right)\frac n{\log n}.
\]
Therefore the known upper bound for \(Q(n)\) is exponentially larger than the Route 3 amplification that has just been proved. The estimates do not come close to crossing.

---

### 5. Exact doubling-chain structure and the weighted obstruction

For
\[
c_k=\tau(2^k+1),
\]
we have
\[
b_{2k}=b_kc_k.
\]

The primitive-prime lower bound for \(c_k\) can be proved precisely.

#### Lemma 5
Write \(k=2^\alpha u\) with \(u\) odd. Then
\[
c_k\ge
2^{\tau(u)-\mathbf 1_{\alpha=0,\ 3\mid u}}.
\]

#### Proof
For every \(e\mid u\), consider
\[
r=2^{\alpha+1}e.
\]
Except when \(r=6\), Bang–Zsigmondy supplies a prime \(p_e\) with
\[
\operatorname{ord}_{p_e}(2)=r.
\]
Since \(r\) is even,
\[
2^{r/2}\equiv-1\pmod{p_e}.
\]
Moreover,
\[
k=\frac r2\frac ue
\]
and \(u/e\) is odd, so
\[
2^k\equiv(-1)^{u/e}\equiv-1\pmod{p_e}.
\]
Thus \(p_e\mid2^k+1\).

The primes obtained from different \(e\) are distinct because their orders \(r\) are distinct. The only omitted case is
\[
2^{\alpha+1}e=6,
\]
equivalently \(\alpha=0\) and \(e=3\). The asserted divisor-count lower bound follows. ∎

There is also an exact coprime factorization along each fixed odd part.

#### Lemma 6
For \(k=2^au\), \(u\) odd,
\[
b_{2^au}
=
b_u\prod_{i=0}^{a-1}c_{2^iu}.
\]

#### Proof
Set \(x=2^u\). Then
\[
x^{2^a}-1=(x-1)\prod_{i=0}^{a-1}(x^{2^i}+1).
\]
The factors are pairwise coprime. Indeed, if \(i<j\), then modulo \(x^{2^i}+1\),
\[
x^{2^j}\equiv1,
\]
so
\[
\gcd(x^{2^i}+1,x^{2^j}+1)\mid2.
\]
Both factors are odd, so the gcd is \(1\). Similarly,
\[
\gcd(x-1,x^{2^i}+1)=1.
\]
Multiplicativity of \(\tau\) on these coprime factors gives the formula. ∎

In the special case \(u=1\),
\[
b_{2^a}
=\prod_{i=0}^{a-1}\tau(F_i),
\qquad
c_{2^a}=\tau(F_a),
\]
where \(F_i=2^{2^i}+1\) is the \(i\)-th Fermat number. Thus a very large divisor count from one Fermat factor followed by a prime or almost-prime Fermat factor is not excluded by any Route 3 estimate.

There is an exact sufficient weighted condition. Since the even-indexed terms give
\[
f(2n)\ge\sum_{k\le n}b_{2k}
=\sum_{k\le n}b_kc_k,
\]
let
\[
W_T(n)=
\frac{\displaystyle
\sum_{\substack{k\le n\\
\tau(\operatorname{oddpart}(k))\le T}}b_k}
{f(n)}.
\]
On the complementary set, Lemma 5 gives \(c_k\ge2^T\); universally \(c_k\ge2\). Therefore
\[
\boxed{
R(n)\ge
2W_T(n)+2^T\bigl(1-W_T(n)\bigr).
}
\]
It would suffice to prove, for every fixed \(T\),
\[
W_T(n)\longrightarrow0.
\]
This is exactly the unavailable weighted anti-concentration statement: Route 3 constructs enormous values at divisor-rich exponents but gives no upper control on the \(b_k\)-mass carried by exponents with small odd part.

A related record-term formulation makes the same obstruction explicit.

#### Lemma 7
Let \(m\le n\) maximize \(b_m\) over \(1\le m\le n\). Then \(m>n/2\), and
\[
R(n)\ge1+\frac{c_m}{n}.
\]

#### Proof
If \(2m\le n\), then
\[
b_{2m}=b_mc_m\ge2b_m>b_m,
\]
contradicting maximality. Thus \(2m\in(n,2n]\). Also
\[
f(n)\le nb_m.
\]
Hence
\[
f(2n)-f(n)\ge b_{2m}=b_mc_m,
\]
and so
\[
R(n)\ge1+\frac{b_mc_m}{nb_m}
=1+\frac{c_m}{n}.
\]
∎

Consequently, if a maximizing exponent always had
\[
\tau(\operatorname{oddpart}(m))-\log_2 n\longrightarrow\infty,
\]
the problem would be solved. There is no known reason this must hold; a maximizing term could lie on a low-odd-part doubling chain.

---

### 6. An abstract countermodel to the coarse Route 3 mechanism

The following does not model actual Mersenne divisor counts. It rigorously shows that the primitive-prime lower bounds, divisibility monotonicity, and the doubling inequality alone cannot prove the desired conclusion.

#### Proposition 8
There is a sequence of positive integers \(\widetilde b_k\) such that

1. \(\widetilde b_k\ge\lambda(k)\);
2. \(d\mid k\) implies \(\widetilde b_d\le\widetilde b_k\);
3. \(\widetilde b_{2k}\ge2\widetilde b_k\);

but, writing
\[
\widetilde f(n)=\sum_{k\le n}\widetilde b_k,
\]
one has
\[
\liminf_{n\to\infty}
\frac{\widetilde f(2n)}{\widetilde f(n)}
\le3.
\]

#### Proof
First note that \(\lambda\) itself is monotone under divisibility. If \(d\mid k\) properly, then \(\tau(k)>\tau(d)\). The possible additional subtraction of \(1\) when \(6\mid k\) can at worst cancel one unit of this strict increase. Thus
\[
\lambda(d)\le\lambda(k).
\]

Also,
\[
\lambda(2k)\ge2\lambda(k).
\]
Indeed, if \(k=2^au\) with \(u\) odd, then
\[
\tau(2k)-\tau(k)=\tau(u)\ge1.
\]
The exceptional indicator changes from \(0\) to \(1\) only when \(k\) is odd and divisible by \(3\), in which case \(\tau(u)=\tau(k)\ge2\). Hence the exponent defining \(\lambda\) always increases by at least \(1\).

Set
\[
N_j=4^j.
\]
We recursively choose positive integers \(A_j\). Define
\[
s_j(k)=
\begin{cases}
A_j\,2^{v_2(k/N_j)},&N_j\mid k,\\
0,&N_j\nmid k.
\end{cases}
\]
Suppose \(A_1,\ldots,A_{j-1}\) have been chosen, and put
\[
C_j=
\sum_{k\le2N_j}
\left(\lambda(k)+\sum_{i<j}s_i(k)\right).
\]
Choose \(A_j>jC_j\). Finally define
\[
\widetilde b_k=\lambda(k)+\sum_{j\ge1}s_j(k).
\]
For fixed \(k\), only finitely many summands are nonzero.

Each \(s_j(k)\) is monotone under divisibility. Moreover,
\[
s_j(2k)\ge2s_j(k):
\]
there is equality if \(N_j\mid k\), while the right side is zero otherwise. Thus \(\widetilde b_k\) has all three stated properties.

Because \(N_{j+1}=4N_j>2N_j\), no future spike contributes below \(2N_j\). In the interval up to \(2N_j\), the \(j\)-th spike contributes only
\[
s_j(N_j)=A_j,\qquad s_j(2N_j)=2A_j.
\]
Hence, for some \(0\le C'_j\le C_j\),
\[
\widetilde f(N_j)=A_j+C'_j,
\qquad
\widetilde f(2N_j)=3A_j+C_j.
\]
It follows that
\[
\frac{\widetilde f(2N_j)}{\widetilde f(N_j)}
\le
3+\frac{C_j}{A_j}
<3+\frac1j.
\]
Therefore the dyadic ratio is bounded along \(N_j\), proving the proposition. ∎

This countermodel does not satisfy all exact Mersenne identities. Its role is narrower: it proves that Route 3’s lower certificates and basic divisibility properties cannot by themselves control denominator spikes. The exact doubling-chain formula shows an analogous obstruction remains arithmetically plausible unless one proves new information about consecutive factors \(2^{2^iu}+1\).

## Self-Audit

1. **The argument invokes Bang–Zsigmondy and Bertrand’s postulate rather than reproving them.** Both are standard unconditional theorems. The sole Zsigmondy exception relevant to \(2^r-1\), namely \(r=6\), is explicitly removed, and \(r=1\) is never assigned a primitive prime.

2. **The surrogate theorem depends on the maximizer \(m\) lying in \((n/2,n]\).** This point is potentially easy to reverse accidentally, but the contradiction is exact: if \(m\le n/2\), then \(2m\le n\) and \(\tau(2m)>\tau(m)\). The resulting quantitative increment is computed exactly from \(v_2(m)\).

3. **The abstract countermodel is not a counterexample to the Erdős problem.** It omits the exact arithmetic requirement \(\widetilde b_{2k}=\widetilde b_k\tau(2^k+1)\) and the exact-order structure. I use it only to prove insufficiency of the coarse Route 3 inequalities, not to infer anything about the actual limit.

The decisive missing claim—weighted negligibility of low-odd-part exponents—is not proved or presented as likely enough to use. It is the block.

## Computations To Verify

The first script verifies the purely exponent-theoretic theorem without factoring any Mersenne numbers.

```python
from fractions import Fraction

def tau_sieve(N):
    t = [0] * (N + 1)
    for d in range(1, N + 1):
        for k in range(d, N + 1, d):
            t[k] += 1
    return t

def v2(k):
    a = 0
    while k % 2 == 0:
        a += 1
        k //= 2
    return a

N = 200000
tau = tau_sieve(2 * N)

lam = [0] * (2 * N + 1)
Gterm = [0] * (2 * N + 1)
for k in range(1, 2 * N + 1):
    lam[k] = 2 ** (tau[k] - 1 - int(k % 6 == 0))
    Gterm[k] = 2 ** tau[k]

H = [0] * (2 * N + 1)
G = [0] * (2 * N + 1)
for k in range(1, 2 * N + 1):
    H[k] = H[k - 1] + lam[k]
    G[k] = G[k - 1] + Gterm[k]

for n in range(2, N + 1):
    D = max(tau[1:n + 1])
    maximizers = [m for m in range(1, n + 1) if tau[m] == D]

    # Lemma 2
    assert all(2 * m > n for m in maximizers)

    m = maximizers[0]
    a = v2(m)
    assert tau[2 * m] == D + D // (a + 1)

    # Explicit lower bound for the H-shell ratio:
    # (H(2n)-H(n))/H(n) >= 2^(D/(a+1)-1)/n.
    diff = D // (a + 1)
    lhs = Fraction(H[2*n] - H[n], H[n])
    rhs = Fraction(2 ** diff, 2 * n)
    assert lhs >= rhs

    # Comparison of H and G.
    assert 4 * H[n] >= G[n]
    assert 2 * H[n] <= G[n]

for n in [10, 100, 1000, 10000, 100000]:
    print(
        n,
        float(Fraction(G[2*n] - G[n], G[n])),
        float(Fraction(H[2*n] - H[n], H[n]))
    )
```

For exact Mersenne computations, Sage should be used with proof flags enabled. This is expensive and intended only for moderate cutoffs.

```python
# Run in SageMath.
from sage.all import *
proof.all(True)

def dc_certified(x):
    x = ZZ(x)
    fac = x.factor()       # factors and certifies prime factors with proof.all(True)
    ans = ZZ(1)
    for p, e in fac:
        ans *= e + 1
    return ans

def oddpart(k):
    k = ZZ(k)
    while k % 2 == 0:
        k //= 2
    return k

N = 200   # increase only as certified factorization resources permit

# Integer divisor counts for exponents.
tau_exp = [ZZ(0)] * (2 * N + 1)
for k in range(1, 2 * N + 1):
    tau_exp[k] = ZZ(k).number_of_divisors()

lam = [ZZ(0)] * (2 * N + 1)
for k in range(1, 2 * N + 1):
    lam[k] = ZZ(2) ** (
        tau_exp[k] - 1 - ZZ(1 if k % 6 == 0 else 0)
    )

b = [ZZ(0)] * (2 * N + 1)
c = [ZZ(0)] * (2 * N + 1)

for k in range(1, 2 * N + 1):
    b[k] = dc_certified(ZZ(2) ** k - 1)
    c[k] = dc_certified(ZZ(2) ** k + 1)

    # Zsigmondy certificates
    assert b[k] >= lam[k]

    u = oddpart(k)
    alpha = ZZ(k).valuation(2)
    eps = 1 if alpha == 0 and u % 3 == 0 else 0
    assert c[k] >= ZZ(2) ** (tau_exp[u] - eps)

# Exact doubling identities
for k in range(1, N + 1):
    assert b[2*k] == b[k] * c[k]

# Exact 2-adic chain decomposition
for k in range(1, 2 * N + 1):
    u = oddpart(k)
    a = ZZ(k).valuation(2)
    rhs = b[u]
    for i in range(a):
        rhs *= c[(2 ** i) * u]
    assert rhs == b[k]

f = [ZZ(0)] * (2 * N + 1)
H = [ZZ(0)] * (2 * N + 1)
for k in range(1, 2 * N + 1):
    f[k] = f[k - 1] + b[k]
    H[k] = H[k - 1] + lam[k]

for n in range(1, N + 1):
    R = QQ(f[2*n]) / f[n]
    A = QQ(H[2*n] - H[n]) / H[n]
    Q = QQ(f[n]) / H[n]

    # Route-3 lower bound R >= 1 + A/Q.
    assert R >= 1 + A / Q

    # Actual maximum-term criterion.
    B = max(b[1:n + 1])
    maximizers = [m for m in range(1, n + 1) if b[m] == B]
    assert all(2*m > n for m in maximizers)

    for m in maximizers:
        assert R >= 1 + QQ(c[m]) / n

    if n in [10, 20, 50, 100, 200]:
        print("n =", n, "R =", R.n(12), "A =", A.n(12), "Q =", Q.n(12))
        for T in [1, 2, 3, 4, 6, 8]:
            low_mass = sum(
                b[k] for k in range(1, n + 1)
                if tau_exp[oddpart(k)] <= T
            )
            W = QQ(low_mass) / f[n]
            weighted_bound = 2 * W + (ZZ(2) ** T) * (1 - W)
            print("  T =", T, "W_T =", W.n(10),
                  "weighted lower bound =", weighted_bound.n(10))
```

The most informative quantities to plot are
\[
A(n)=\frac{H(2n)-H(n)}{H(n)},\qquad
Q(n)=\frac{f(n)}{H(n)},\qquad
W_T(n),
\]
especially at local minima of \(R(n)\). Route 3 succeeds only if \(A(n)\) outgrows \(Q(n)\), or if \(W_T(n)\to0\) for every fixed \(T\).

## Route Diagnosis

**Proved ledger**

- The Zsigmondy certificate \(b_k\ge\lambda(k)\), with all exceptions handled.
- Every divisor-count maximizer below \(n\) lies in \((n/2,n]\), and doubling it gives a quantitatively larger divisor count inside \((n,2n]\).
- The full Route 3 surrogate satisfies
  \[
  \frac{\sum_{n<k\le2n}2^{\tau(k)}}
  {\sum_{k\le n}2^{\tau(k)}}\to\infty.
  \]
- Exact lower bounds for \(\tau(2^k+1)\) in terms of the odd part of \(k\).
- Exact coprime doubling-chain factorization.
- An abstract countermodel showing that Route 3 lower bounds, divisibility monotonicity, and doubling alone do not force divergence.

**Plausible but unproved claims**

- For every fixed \(T\),
  \[
  \sum_{\substack{k\le n\\
  \tau(\operatorname{oddpart}(k))\le T}}b_k=o(f(n)).
  \]
- Equivalently in Route 3 language, the excess
  \[
  Q(n)=\frac{f(n)}{H(n)}
  \]
  grows more slowly than the certified shell amplification \(A(n)\).
- Large \(b_k\) should positively correlate with large \(c_k=\tau(2^k+1)\).

Each would essentially solve the original problem and is presently unsupported.

**Dead ends**

- Comparing the best Zsigmondy lower bound in \((n,2n]\) with Wigert’s upper bound for \(f(n)\): the logarithmic scales differ by almost \(n/\log n\).
- Choosing a maximizer of \(b_k\): it only gives \(R(n)\ge1+c_m/n\), and \(c_m\) can have no known growing lower bound when \(m\) has small odd part.
- Mapping old terms to divisible exponents in the next block: for an old exponent \(m>n/2\), the only multiple in \((n,2n]\) is \(2m\), so this again reduces to controlling \(c_m\).
- Relying on powers of two: the exact Fermat-number chain shows that consecutive amplification factors may be as small as \(2\), and no unconditional theorem rules out isolated huge divisor spikes followed by such a small factor.

A fresh affirmative attempt must prove a genuine correlation theorem between \(b_k\) and \(c_k\), or show that exact-order mass concentrated at a low-odd-part exponent necessarily creates much larger mass elsewhere in the next dyadic block. A negative attempt would need to realize the low-odd-part spike mechanism in actual Mersenne or Fermat values and control an entire following block, for which present upper-bound technology is inadequate.