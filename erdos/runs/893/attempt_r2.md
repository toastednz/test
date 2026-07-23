STATUS: BLOCKED

## Result

Route 2 yields a sharper exact reformulation but not a resolution. Let \(A(N)=\sum_{r\le N}a(r)\). I prove that \(A(N)\le f(N)\le2A(N)\), that \(f(2n)\ge3f(n)\) for every \(n\), and—more importantly—that the surviving conjecture is equivalent to each of
\[
\frac{A(2n)}{A(n)}\to\infty,\qquad
\frac{\sum_{n<r\le2n}a(r)}{f(n)}\to\infty,
\qquad
\frac{\sum_{n<r\le2n}(2a(r)-b_r)}{f(n)}\to\infty.
\]
The last formulation isolates the mass beyond the single-primitive-divisor baseline. I also prove a substantial amplification lemma at doubled exponents, giving uniformly superpolynomial absolute excess in every dyadic shell. However, comparison with the accumulated \(f(n)\) remains blocked by a weighted anti-concentration problem: one must rule out concentration of recent exact-order mass on exponents whose odd parts have boundedly many divisors, especially powers of \(2\) and \(2^\alpha p\). Current divisor and primitive-divisor estimates do not do this.

## Complete Argument

### 1. Primitive divisors imply \(b_r\le 2a(r)\)

Write
\[
P(r)=\sum_{\substack{d\mid r\\d<r}}a(d)=b_r-a(r).
\]
Thus \(P(r)\) is the number of divisors \(x\mid M_r\) whose exact order is strictly smaller than \(r\).

For \(r>1\), \(r\ne6\), choose a primitive prime divisor \(p_r\mid M_r\), so
\[
\operatorname{ord}_{p_r}(2)=r.
\]
If \(x\mid M_r\) has order \(<r\), then \(p_r\nmid x\). Hence \(p_rx\mid M_r\), and
\[
\operatorname{ord}_{p_rx}(2)
=\operatorname{lcm}\bigl(\operatorname{ord}_x(2),r\bigr)=r.
\]
The map \(x\mapsto p_rx\) is injective, so
\[
P(r)\le a(r).
\]
Consequently,
\[
b_r=a(r)+P(r)\le2a(r).
\]

The exceptional cases are direct:

- \(r=1\): \(b_1=a(1)=1\);
- \(r=6\): \(b_6=6\), \(a(6)=3\), so equality holds.

Therefore, for every \(r\ge1\),
\[
\boxed{a(r)\le b_r\le2a(r).}
\]

Define
\[
A(N)=\sum_{r\le N}a(r).
\]
Summing the pointwise inequalities gives
\[
\boxed{A(N)\le f(N)\le2A(N).}
\]

This already shows that accumulated exact-order mass and the original sum are comparable within an absolute factor \(2\).

---

### 2. Exact decomposition of the dyadic ratio

Set
\[
S(n)=\sum_{n<r\le2n}a(r)=A(2n)-A(n)
\]
and, for \(r\le n\),
\[
\varepsilon_n(r)
=
\left\lfloor\frac{2n}{r}\right\rfloor
-2\left\lfloor\frac nr\right\rfloor.
\]
Writing \(n/r=q+\theta\), \(0\le\theta<1\), gives
\[
\varepsilon_n(r)=\lfloor2\theta\rfloor\in\{0,1\}.
\]
Define
\[
T(n)=\sum_{r\le n}a(r)\varepsilon_n(r).
\]
Then
\[
0\le T(n)\le A(n)\le f(n).
\]

For \(n<r\le2n\), the coefficient in the dyadic defect is exactly \(1\). Thus the exact-order formula gives
\[
\boxed{f(2n)-2f(n)=S(n)+T(n).}
\]
Equivalently,
\[
\boxed{R(n)=2+\frac{S(n)+T(n)}{f(n)}.}
\]
Since \(0\le T(n)/f(n)\le1\),
\[
2+\frac{S(n)}{f(n)}
\le R(n)
\le3+\frac{S(n)}{f(n)}.
\]
Therefore
\[
\boxed{
R(n)\to\infty
\iff
\frac{S(n)}{f(n)}\to\infty.
}
\]
Thus Route 2 shell dominance is not merely sufficient: it is necessary and sufficient.

Because \(A(n)\le f(n)\le2A(n)\),
\[
\frac{A(2n)/A(n)-1}{2}
\le
\frac{S(n)}{f(n)}
\le
\frac{A(2n)}{A(n)}-1.
\]
Hence
\[
\boxed{
R(n)\to\infty
\iff
\frac{A(2n)}{A(n)}\to\infty.
}
\]

---

### 3. Removing the unavoidable one-primitive-prime baseline

Define the nonnegative excess
\[
h(r)=2a(r)-b_r=a(r)-P(r)\ge0
\]
and its shell sum
\[
H(n)=\sum_{n<r\le2n}h(r).
\]

Since
\[
f(2n)-f(n)=\sum_{n<r\le2n}b_r
\]
and
\[
f(2n)=2f(n)+S(n)+T(n),
\]
we have
\[
\sum_{n<r\le2n}b_r=f(n)+S(n)+T(n).
\]
Therefore
\[
\begin{aligned}
H(n)
&=2S(n)-\sum_{n<r\le2n}b_r\\
&=S(n)-f(n)-T(n).
\end{aligned}
\]
Thus
\[
\boxed{S(n)=f(n)+T(n)+H(n)}
\]
and
\[
\boxed{f(2n)=3f(n)+2T(n)+H(n).}
\]
In particular,
\[
\boxed{f(2n)\ge3f(n)\quad\text{for every }n\ge1.}
\]

Moreover,
\[
\boxed{
R(n)=3+\frac{2T(n)+H(n)}{f(n)}.
}
\]
Because \(0\le2T(n)/f(n)\le2\),
\[
\boxed{
R(n)\to\infty
\iff
\frac{H(n)}{f(n)}\to\infty.
}
\]

This is the sharpest form of Route 2 obtained here: the conjecture asks whether the exact-order mass beyond that forced by one primitive prime dominates the entire past in every dyadic shell.

A further consequence is
\[
S(n)\ge f(n)\ge A(n),
\]
so
\[
A(2n)\ge2A(n).
\]
For arbitrary \(n\), applying this with \(\lfloor n/2\rfloor\) gives
\[
\boxed{
A(n)-A(\lfloor n/2\rfloor)\ge\frac12A(n).
}
\]
At least half of \(A(n)\) lies in the most recent half-interval.

---

### 4. Amplification at doubled exponents

Let
\[
d=2^\alpha u,\qquad u\ \text{odd},
\]
and assume \(d>3\). Define
\[
t(d)=
\#\left\{
e:e\mid u,\ e<u,\ 2^{\alpha+1}e\ne6
\right\}.
\]
Explicitly,
\[
t(d)=
\tau(u)-1-
\mathbf 1_{\alpha=0,\ 3\mid u,\ u>3}.
\]

#### Lemma

For every \(d>3\),
\[
\boxed{
h(2d)\ge a(d)\bigl(2^{t(d)}-1\bigr).
}
\]

#### Proof

Put \(r=2d\). Since \(r\ne6\), fix a primitive prime \(p_r\) of order \(r\).

For each proper divisor \(e<u\) with
\[
s_e=2^{\alpha+1}e\ne6,
\]
choose a primitive prime \(q_e\) satisfying
\[
\operatorname{ord}_{q_e}(2)=s_e.
\]
The primes \(q_e\) are distinct because their orders are distinct. They are also distinct from \(p_r\), since \(s_e<r\).

Let \(x\) be any divisor of exact order \(d\). For every nonempty subset \(J\) of the eligible divisors \(e\), define
\[
y=x\prod_{e\in J}q_e.
\]
No \(q_e\) divides \(x\), since \(s_e\) has \(2\)-adic valuation \(\alpha+1\), whereas every order dividing \(d\) has \(2\)-adic valuation at most \(\alpha\). Hence \(y\mid M_{2d}\).

Furthermore,
\[
\operatorname{ord}_y(2)
=
\operatorname{lcm}\bigl(d,(s_e)_{e\in J}\bigr)=2d:
\]
the order \(d\) supplies the full odd part \(u\), and any nonempty \(J\) supplies \(2\)-adic valuation \(\alpha+1\).

Every such \(y\) avoids \(p_r\). Different choices of \(x\) and \(J\) produce different \(y\), because the selected \(q_e\)'s do not divide \(x\).

On the other hand, multiplying every non-exact-order divisor of \(M_r\) by \(p_r\) gives \(P(r)\) exact-order divisors, all divisible by \(p_r\). Hence every exact-order divisor avoiding \(p_r\) contributes to the surplus
\[
h(r)=a(r)-P(r).
\]
There are \(a(d)(2^{t(d)}-1)\) constructed divisors, proving the lemma. \(\square\)

Consequently,
\[
\boxed{
H(n)\ge
\sum_{\lfloor n/2\rfloor<d\le n}
a(d)\bigl(2^{t(d)}-1\bigr)
}
\]
for all sufficiently large \(n\), because the indices \(2d\) are distinct and lie in \((n,2n]\).

This is the main concrete amplification found by Route 2.

---

### 5. A precise sufficient condition—and the exact obstruction

For fixed \(T\), define the exceptional recent mass
\[
L_T(n)=
\sum_{\substack{\lfloor n/2\rfloor<d\le n\\t(d)<T}}a(d).
\]

If, for every fixed \(T\),
\[
\boxed{L_T(n)=o(A(n)),}
\]
then the conjecture follows. Indeed, at least \(A(n)/2\) lies in the recent half-interval, so
\[
\sum_{\substack{\lfloor n/2\rfloor<d\le n\\t(d)\ge T}}a(d)
\ge \frac12A(n)-o(A(n)).
\]
The amplification lemma and \(f(n)\le2A(n)\) then give
\[
\frac{H(n)}{f(n)}
\ge
(2^T-1)\left(\frac14-o(1)\right).
\]
Since \(T\) is arbitrary,
\[
H(n)/f(n)\to\infty,
\]
and therefore \(R(n)\to\infty\).

Conversely, suppose that along an infinite sequence \(n_j\),
\[
R(n_j)\le C.
\]
As \(R(n)\ge3\), assume \(C\ge3\). The exact identity gives
\[
H(n_j)\le(C-3)f(n_j)\le2(C-3)A(n_j).
\]
Therefore
\[
\sum_{\substack{\lfloor n_j/2\rfloor<d\le n_j\\t(d)\ge T}}a(d)
\le
\frac{2(C-3)}{2^T-1}A(n_j).
\]
Since the total recent mass is at least \(A(n_j)/2\),
\[
\boxed{
L_T(n_j)
\ge
\left(
\frac12-\frac{2(C-3)}{2^T-1}
\right)A(n_j).
}
\]
For fixed \(T\) large enough in terms of \(C\), the right side is at least \(A(n_j)/4\).

Thus any disproof must exhibit substantial concentration of exact-order mass on exponents \(d\) for which \(t(d)\) is bounded—that is, whose odd parts have bounded divisor count.

This weighted anti-concentration is the unresolved step.

---

### 6. Every shell nevertheless has superpolynomial absolute excess

Although relative domination remains unavailable, the amplification lemma gives a strong uniform absolute bound.

There exists \(c>0\) such that, for all sufficiently large \(n\),
\[
\boxed{
\log H(n)\ge
\exp\left(c\frac{\log n}{\log\log n}\right).
}
\]
In particular, \(H(n)>n^C\) eventually for every fixed \(C\).

To prove this, use standard Chebyshev bounds: for some constants \(c_1,C_1>0\),
\[
\pi(x)\ge c_1\frac{x}{\log x},
\qquad
\sum_{p\le x}\log p\le C_1x.
\]
Choose
\[
x=\frac{\log n}{4C_1}
\]
and let \(Q\) be the product of the odd primes at most \(x\). Then
\[
Q\le n^{1/4}
\]
for all sufficiently large \(n\), while
\[
\tau(Q)=2^{\pi(x)-1}
\ge
\exp\left(c_2\frac{\log n}{\log\log n}\right)
\]
for some \(c_2>0\).

Choose
\[
d=Q\left\lfloor\frac nQ\right\rfloor.
\]
Then \(n/2<d\le n\), and the odd part \(u\) of \(d\) is divisible by \(Q\). Hence
\[
t(d)\ge\tau(u)-2\ge\tau(Q)-2.
\]
Since \(h(2d)\) is a term of \(H(n)\),
\[
H(n)\ge h(2d)\ge2^{t(d)}-1.
\]
Taking logarithms proves the claimed estimate.

This does not settle the problem because the generic upper bound
\[
\log f(n)=O\!\left(\frac n{\log n}\right)
\]
is vastly larger than the lower bound obtained for \(\log H(n)\).

---

### 7. The power-of-two obstruction is genuine

Let \(d=2^j\) and
\[
F=2^d+1.
\]
Then
\[
M_{2d}=M_dF,\qquad \gcd(M_d,F)=1.
\]
Every nontrivial divisor \(v\mid F\) has exact order \(2d\): its order divides \(2d\), does not divide \(d\), and \(2d\) is a power of \(2\). Therefore
\[
a(2d)=b_d\bigl(\tau(F)-1\bigr),
\qquad
b_{2d}=b_d\tau(F),
\]
and hence
\[
\boxed{
h(2d)=b_d\bigl(\tau(2^d+1)-2\bigr).
}
\]
In particular, if the Fermat number \(2^d+1\) is prime, then
\[
h(2d)=0.
\]
Thus the doubled-exponent surplus can vanish completely at powers of \(2\). Even proving that the divisor counts of Fermat numbers tend to infinity is presently unavailable, and Route 2 must somehow prove that exact-order mass cannot concentrate on these or analogous low-\(t(d)\) exponents.

---

### 8. Why the primitive-divisor inequalities alone cannot finish the problem

Consider the formal nonnegative coefficient sequence
\[
\widetilde a(n)=n^2,\qquad
\widetilde b(n)=\sum_{d\mid n}\widetilde a(d)=\sigma_2(n).
\]
Then
\[
\frac{\widetilde b(n)}{\widetilde a(n)}
=
\sum_{q\mid n}\frac1{q^2}
\le\zeta(2)<2,
\]
so it satisfies the analogue of \(b_n\le2a(n)\), with positive surplus. It is also multiplicative and divisibility-monotone.

Nevertheless,
\[
\widetilde f(N)=\sum_{n\le N}\sigma_2(n)
=\frac{\zeta(3)}3N^3+O(N^2),
\]
obtained by writing
\[
\widetilde f(N)
=
\sum_{m\le N}\sum_{d\le N/m}d^2.
\]
Consequently,
\[
\frac{\widetilde f(2N)}{\widetilde f(N)}\to8,
\]
not infinity.

This is not a counterexample to the Mersenne problem, but it proves that positivity, the exact-order transform, \(b\le2a\), divisibility monotonicity, and even multiplicativity-type structure do not alone force the desired conclusion. The additional Mersenne amplification must be used quantitatively.

## Self-Audit

1. **The proof of \(b_r\le2a(r)\) depends on the precise primitive-divisor exception list.**  
   Bang–Zsigmondy is used only for \(r>1,\ r\ne6\). The two omitted cases \(r=1,6\) are checked directly, so no exceptional exponent is silently included.

2. **The doubled-exponent amplification lemma has a subtle surplus count.**  
   The constructed exact-order divisors avoid a fixed primitive prime \(p_{2d}\), while the baseline injection of all lower-order divisors produces exact-order divisors containing \(p_{2d}\). These two families are disjoint, which justifies counting the former inside \(h(2d)\). The case \(2d=6\) is explicitly excluded.

3. **The uniform superpolynomial lower bound uses standard prime-counting estimates.**  
   Only Chebyshev-level estimates are required, not the prime number theorem. The chosen odd primorial is at most \(n^{1/4}\), ensuring that a multiple lies in \((n/2,n]\), and its divisor count has the stated exponential-in-\(\log n/\log\log n\) size.

The decisive weighted anti-concentration assertion \(L_T(n)=o(A(n))\) is not proved and is not being presented as likely enough to count as a solution.

## Computations To Verify

The following Sage/Python code uses certified integer factorization and checks all identities and inequalities above.

```python
# Run in SageMath.

from sage.all import ZZ, QQ, prod, divisors

def tau_certified(m):
    m = ZZ(m)
    if m == 1:
        return ZZ(1)
    fac = m.factor(proof=True)
    return prod(e + 1 for p, e in fac)

def exact_data(max_k):
    b = [ZZ(0)] * (max_k + 1)
    a = [ZZ(0)] * (max_k + 1)
    h = [ZZ(0)] * (max_k + 1)

    for k in range(1, max_k + 1):
        b[k] = tau_certified(ZZ(2)^k - 1)
        proper = sum(a[d] for d in divisors(k) if d < k)
        a[k] = b[k] - proper
        assert a[k] >= 0

        h[k] = 2*a[k] - b[k]
        assert h[k] >= 0, (k, a[k], b[k])

    F = [ZZ(0)] * (max_k + 1)
    A = [ZZ(0)] * (max_k + 1)
    for k in range(1, max_k + 1):
        F[k] = F[k-1] + b[k]
        A[k] = A[k-1] + a[k]
        assert A[k] <= F[k] <= 2*A[k]

    return b, a, h, F, A

def odd_part_and_v2(d):
    alpha = 0
    u = ZZ(d)
    while u % 2 == 0:
        alpha += 1
        u //= 2
    return alpha, u

def t_value(d):
    alpha, u = odd_part_and_v2(d)
    return sum(
        1 for e in divisors(u)
        if e < u and (ZZ(2)^(alpha + 1))*e != 6
    )

def verify(N):
    b, a, h, F, A = exact_data(2*N)

    # Check b_k = sum_{d|k} a(d).
    for k in range(1, 2*N + 1):
        assert b[k] == sum(a[d] for d in divisors(k))

    # Check dyadic identities.
    ratios = {}
    for n in range(1, N + 1):
        S = sum(a[r] for r in range(n + 1, 2*n + 1))
        T = sum(
            a[r] * ((2*n)//r - 2*(n//r))
            for r in range(1, n + 1)
        )
        H = sum(h[r] for r in range(n + 1, 2*n + 1))

        assert all(
            ((2*n)//r - 2*(n//r)) in (0, 1)
            for r in range(1, n + 1)
        )
        assert F[2*n] - 2*F[n] == S + T
        assert H == S - F[n] - T
        assert F[2*n] == 3*F[n] + 2*T + H
        assert F[2*n] >= 3*F[n]
        assert S >= F[n] + T

        ratios[n] = QQ(F[2*n]) / F[n]

    # Check the doubled-exponent amplification lemma.
    for d in range(4, N + 1):
        t = t_value(d)
        assert h[2*d] >= a[d] * (ZZ(2)^t - 1), (
            d, t, h[2*d], a[d]
        )

    # Inspect local minima and the Route-2 quantities.
    local_minima = []
    for n in range(2, N):
        if ratios[n] <= ratios[n-1] and ratios[n] <= ratios[n+1]:
            S = A[2*n] - A[n]
            H = sum(h[r] for r in range(n + 1, 2*n + 1))
            local_minima.append((
                n,
                ratios[n],
                QQ(S) / F[n],
                QQ(H) / F[n],
                QQ(A[2*n]) / A[n]
            ))

    print("Local minima: n, R, S/f, H/f, A(2n)/A(n)")
    for row in local_minima[-30:]:
        print(row)

    # Weighted exceptional recent mass.
    for T0 in [1, 2, 3, 4, 5, 8, 12]:
        print("\nThreshold", T0)
        for n in [N//8, N//4, N//2, N]:
            if n < 8:
                continue
            low = sum(
                a[d] for d in range(n//2 + 1, n + 1)
                if t_value(d) < T0
            )
            recent = A[n] - A[n//2]
            print(
                "n =", n,
                "low/A =", QQ(low)/A[n],
                "low/recent =", QQ(low)/recent
            )

    return b, a, h, F, A, ratios

# Example:
# b, a, h, F, A, ratios = verify(200)
```

A more focused counterexample search should record, at every local minimum of \(R(n)\),

```python
for T0 in [2, 3, 4, 5, 8, 12, 16]:
    low = sum(
        a[d] for d in range(n//2 + 1, n + 1)
        if t_value(d) < T0
    )
    print(T0, QQ(low)/A[n])
```

If bounded-ratio subsequences exist, the proved obstruction predicts a persistent positive proportion for some fixed threshold \(T_0\).

## Route Diagnosis

**Proved ledger**

- \(a(r)\le b_r\le2a(r)\) for every \(r\).
- \(A(N)\le f(N)\le2A(N)\).
- Exact identity
  \[
  f(2n)=3f(n)+2T(n)+H(n).
  \]
- Universal improvement
  \[
  f(2n)\ge3f(n).
  \]
- The original conjecture is equivalent to shell dominance, to \(A(2n)/A(n)\to\infty\), and to \(H(n)/f(n)\to\infty\).
- Doubled-exponent amplification
  \[
  h(2d)\ge a(d)(2^{t(d)}-1).
  \]
- Every shell has uniformly superpolynomial absolute surplus \(H(n)\).
- Any bounded-ratio subsequence forces positive recent \(a\)-mass on exponents with bounded odd-part divisor count.

**Plausible but unproved**

- For each fixed \(T\),
  \[
  L_T(n)=o(A(n)).
  \]
  This would solve the problem immediately, but present estimates do not control the \(a(d)\)-weights on this exceptional set.
- A weaker possible target is that large \(a(d)\) forces the non-primitive cofactor of \(2^d+1\) to have many divisors. This is a Mersenne/Fermat correlation statement not currently available.

**Dead ends**

- Nonnegativity and the exact-order transform alone are insufficient.
- The one-primitive-prime injection yields the sharp baseline \(R(n)\ge3\), but no divergence.
- Uniformly superpolynomial absolute shell mass is far below available upper bounds for \(f(n)\).
- Divisibility monotonicity and coprime supermultiplicativity do not amplify mass at a recent dominant exponent \(d\), because the only multiple of \(d\) in the next shell may be \(2d\).
- Powers of \(2\) are a concrete obstruction: if \(2^{2^j}+1\) is prime, the corresponding surplus \(h(2^{j+1})\) is zero.

**Diagnosis**

Route 2 successfully isolates the exact missing arithmetic phenomenon, but it is blocked at a weighted anti-concentration theorem of essentially the same uniform difficulty as the original problem. A fresh attempt should either:

1. prove that recent exact-order mass cannot concentrate on \(2^\alpha u\) with bounded \(\tau(u)\); or
2. combine Route 2 with Route 1 by proving that large \(a(d)\) forces substantial divisor mass in the cofactor of \(2^d+1\) after removing one primitive prime; or
3. extract an anti-lacunarity mechanism from the Kovač–Luca limsup construction that rules out repeated concentration on these low-\(t(d)\) exponents.