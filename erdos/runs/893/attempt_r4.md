STATUS: BLOCKED

## Result

Route 4 yields a rigorous strengthening of the universal bound:
\[
\boxed{f(2n)\ge 3f(n)\quad\text{for every }n\ge1.}
\]
The proof uses primitive prime divisors to duplicate, inside the next dyadic block, every divisor occurrence counted by \(f(n)\). I also derive stronger lower bounds involving the number of primitive-order divisors of cyclotomic values and products of primitive primes of several orders. These reduce the conjecture to a weighted multiplicative-order growth statement. However, that statement remains unproved and appears to encounter a sharp obstruction at powers of \(2\), where the relevant amplification is exactly \(\tau(F_j)-1\) for a Fermat number \(F_j\). Thus this does not prove \(f(2n)/f(n)\to\infty\).

## Complete Argument

### 1. A primitive-extension inequality for exact-order mass

Recall
\[
a(r)=\#\{d\ge1:d\text{ odd and }\operatorname{ord}_d(2)=r\},
\]
so that
\[
b_k=\tau(2^k-1)=\sum_{r\mid k}a(r).
\]

For \(t>1\), put
\[
B(t)=\sum_{\substack{r\mid t\\r<t}}a(r)=b_t-a(t).
\]

Thus \(B(t)\) is the number of divisors of \(2^t-1\) whose order is a proper divisor of \(t\).

#### Lemma 1
For every \(t>1\),
\[
\boxed{a(t)\ge B(t).}
\]

#### Proof

First suppose \(t\ne6\). By Bang–Zsigmondy, \(2^t-1\) has a primitive prime divisor \(q_t\). Hence
\[
\operatorname{ord}_{q_t}(2)=t.
\]

Let \(d\) be any odd integer with
\[
\operatorname{ord}_d(2)=r,\qquad r\mid t,\qquad r<t.
\]
Then \(d\mid2^r-1\), hence \(d\mid2^t-1\). Also \(q_t\nmid d\), because otherwise
\[
t=\operatorname{ord}_{q_t}(2)\mid\operatorname{ord}_d(2)=r,
\]
which is impossible since \(r<t\).

Therefore \(dq_t\mid2^t-1\), and, because \(\gcd(d,q_t)=1\),
\[
\operatorname{ord}_{dq_t}(2)
=\operatorname{lcm}\bigl(\operatorname{ord}_d(2),\operatorname{ord}_{q_t}(2)\bigr)
=\operatorname{lcm}(r,t)=t.
\]
The map \(d\mapsto dq_t\) is injective, proving \(a(t)\ge B(t)\).

It remains to check \(t=6\). The divisors of \(63\) having exact order \(6\) are
\[
9,\quad21,\quad63,
\]
so \(a(6)=3\). Also
\[
B(6)=a(1)+a(2)+a(3)=1+1+1=3.
\]
Thus the inequality also holds for \(t=6\). ∎

---

### 2. Every old divisor occurrence produces two occurrences in the next dyadic block

Define
\[
Q(n)=\sum_{n<t\le2n}B(t),
\qquad
S(n)=\sum_{n<t\le2n}a(t).
\]

Every proper divisor \(r<t\) of an integer \(t\le2n\) satisfies
\[
r\le \frac t2\le n.
\]
Consequently,
\[
\begin{aligned}
Q(n)
&=\sum_{n<t\le2n}\sum_{\substack{r\mid t\\r<t}}a(r)\\
&=\sum_{r\le n}a(r)
 \#\{t:n<t\le2n,\ r\mid t\}\\
&=\sum_{r\le n}a(r)
 \left(
 \left\lfloor\frac{2n}{r}\right\rfloor
 -
 \left\lfloor\frac nr\right\rfloor
 \right).
\end{aligned}
\]

For every real \(x\ge0\),
\[
\lfloor2x\rfloor-\lfloor x\rfloor\ge\lfloor x\rfloor.
\]
Applying this with \(x=n/r\) gives
\[
Q(n)\ge
\sum_{r\le n}a(r)\left\lfloor\frac nr\right\rfloor
=f(n).
\]

On the other hand, Lemma 1 gives
\[
S(n)=\sum_{n<t\le2n}a(t)
\ge
\sum_{n<t\le2n}B(t)
=Q(n).
\]

Finally,
\[
\begin{aligned}
f(2n)-f(n)
&=\sum_{n<t\le2n}b_t\\
&=\sum_{n<t\le2n}\bigl(B(t)+a(t)\bigr)\\
&=Q(n)+S(n)\\
&\ge2Q(n)\\
&\ge2f(n).
\end{aligned}
\]

We have therefore proved:

#### Theorem 2
For every positive integer \(n\),
\[
\boxed{f(2n)\ge3f(n).}
\]
Equivalently,
\[
\boxed{R(n)\ge3.}
\]

This improves the elementary bound \(R(n)\ge2\), but is still only a fixed lower bound.

---

### 3. Counting all primitive-order divisors

The preceding argument used only one primitive prime of each order. One can use all of them.

For \(t\ge1\), define the primitive part
\[
P_t=
\prod_{\substack{p\mid2^t-1\\ \operatorname{ord}_p(2)=t}}
p^{v_p(2^t-1)}
\]
and
\[
C_t=\tau(P_t)-1.
\]

Thus \(C_t\) counts the nontrivial divisors supported entirely on primes whose order modulo \(2\) is exactly \(t\).

#### Lemma 3
For every \(t\ge1\),
\[
\boxed{a(t)\ge C_t B(t).}
\]

#### Proof

Let \(d\) have exact order \(r<t\), where \(r\mid t\), and let \(y>1\) divide \(P_t\).

No prime dividing \(P_t\) can divide \(d\), since such a prime has order \(t\), while every prime divisor of \(d\) has order dividing \(r<t\). Thus \(\gcd(d,y)=1\).

If \(p^j\mid P_t\), then \(p^j\mid2^t-1\), so
\[
\operatorname{ord}_{p^j}(2)\mid t.
\]
Reduction modulo \(p\) shows
\[
t=\operatorname{ord}_p(2)\mid\operatorname{ord}_{p^j}(2).
\]
Hence \(\operatorname{ord}_{p^j}(2)=t\). It follows that every nontrivial \(y\mid P_t\) has exact order \(t\).

Therefore
\[
\operatorname{ord}_{dy}(2)=\operatorname{lcm}(r,t)=t.
\]
The factorization \(dy\) uniquely recovers \(d\) and \(y\), because their prime supports are disjoint. Hence the \(B(t)C_t\) products are distinct exact-order-\(t\) divisors. ∎

For \(t\ne1,6\), Bang–Zsigmondy gives \(C_t\ge1\).

Summing Lemma 3 over a dyadic shell gives the Route 4 inequality
\[
\boxed{
S(n)\ge
\sum_{r\le n}a(r)
\sum_{\substack{n<t\le2n\\r\mid t}}C_t.
}
\]

Thus the conjecture would follow from
\[
\frac{1}{f(n)}
\sum_{r\le n}a(r)
\sum_{\substack{n<t\le2n\\r\mid t}}C_t
\longrightarrow\infty.
\]
This is a precise weighted multiplicative-order target, but I cannot prove it.

---

### 4. Relation with cyclotomic values

The primitive part \(P_t\) is almost the whole cyclotomic value \(\Phi_t(2)\).

#### Lemma 4
There is a squarefree integer \(Q_t\mid\operatorname{rad}(t)\) such that
\[
\boxed{\Phi_t(2)=P_tQ_t.}
\]

#### Proof

Let \(p\mid\Phi_t(2)\), and let \(m=\operatorname{ord}_p(2)\). Then \(m\mid t\). Write \(t=mu\).

Using
\[
v_p(\Phi_t(2))
=
\sum_{d\mid t}\mu(t/d)v_p(2^d-1)
\]
and noting that \(p\mid2^d-1\) precisely when \(m\mid d\), we obtain
\[
v_p(\Phi_t(2))
=
\sum_{e\mid u}\mu(u/e)v_p(2^{me}-1).
\]
Since \(p\) is odd, the lifting-the-exponent formula gives
\[
v_p(2^{me}-1)=v_p(2^m-1)+v_p(e).
\]

If \(u=1\), then \(m=t\), so \(p\) is primitive and occurs in \(P_t\) with its full exponent.

If \(u>1\), the constant term cancels because \(\sum_{e\mid u}\mu(u/e)=0\), leaving
\[
\sum_{e\mid u}\mu(u/e)v_p(e).
\]
This equals \(1\) when \(u\) is a positive power of \(p\), and \(0\) otherwise. Therefore every nonprimitive prime divisor of \(\Phi_t(2)\) occurs to the first power and divides \(t\). This proves the stated factorization. ∎

Consequently,
\[
C_t+1=\tau(P_t)
\ge \frac{\tau(\Phi_t(2))}{2^{\omega(t)}}.
\]

Unfortunately, the large size of \(\Phi_t(2)\) does not force \(\tau(P_t)\) to grow: \(P_t\) could be prime. This is the central analytic obstruction.

---

### 5. Products of primitive primes of several orders

There is another unconditional amplification mechanism.

Let \(r\mid t\), \(r<t\), and assume \(t\ne6\). Define
\[
\mathcal E(t,r)
=
\{s:s\mid t,\ s\nmid r,\ s>1,\ s\ne6\}.
\]
Choose one primitive prime \(q_s\) of order \(s\) for each \(s\in\mathcal E(t,r)\).

For every divisor \(d\mid2^r-1\) and every subset
\[
U\subseteq\mathcal E(t,r),\qquad t\in U,
\]
the number
\[
d\prod_{s\in U}q_s
\]
divides \(2^t-1\) and has exact order \(t\). All these numbers are distinct. Therefore
\[
\boxed{
a(t)\ge b_r\,2^{|\mathcal E(t,r)|-1}.
}
\]

For \(t=2r\), write \(r=2^\alpha u\) with \(u\) odd. If \(r\ne3\), then
\[
|\mathcal E(2r,r)|
=
\tau(u)-\mathbf 1_{\alpha=0,\ 3\mid u}.
\]
Hence
\[
\boxed{
a(2r)\ge
b_r\,
2^{\tau(u)-1-\mathbf 1_{\alpha=0,\ 3\mid u}}.
}
\]

There is also a useful comparison between \(f(n)\) and its final half-block. Since
\[
b_{2k}\ge2b_k,
\]
partition the integers \(k\le n\) according to the unique number
\[
r=2^jk\in(n/2,n].
\]
For a fixed \(r\), all preimages are among \(r/2^j\), and
\[
b_{r/2^j}\le2^{-j}b_r.
\]
Thus
\[
\boxed{
f(n)\le
2\sum_{n/2<r\le n}b_r.
}
\]

Combining these inequalities, for \(n>6\),
\[
S(n)\ge
\sum_{n/2<r\le n}
b_r\,
2^{\tau(\operatorname{odd}(r))-1-
\mathbf1_{r\text{ odd},\,3\mid r}}.
\]

A sufficient condition for the conjecture would therefore be: for each fixed \(H\),
\[
\sum_{\substack{n/2<r\le n\\
\tau(\operatorname{odd}(r))-
\mathbf1_{r\text{ odd},\,3\mid r}\le H}}
b_r=o(f(n)).
\]
I cannot establish this. In particular, the \(b_r\)-mass could conceivably concentrate near powers of \(2\), where the displayed amplification factor is only \(1\).

---

### 6. The exact Fermat-number obstruction

Let
\[
F_j=2^{2^j}+1.
\]
For \(n=2^j\),
\[
2^n-1=\prod_{i=0}^{j-1}F_i,
\]
and the Fermat numbers are pairwise coprime.

Every nontrivial divisor of \(F_i\) has exact order \(2^{i+1}\): if \(y>1\) divides \(F_i\), then
\[
2^{2^i}\equiv-1\pmod y,
\]
so the order divides \(2^{i+1}\) but not \(2^i\).

It follows exactly that
\[
b_{2^j}=\prod_{i=0}^{j-1}\tau(F_i)
\]
and
\[
\boxed{
a(2^j)
=
\bigl(\tau(F_{j-1})-1\bigr)b_{2^{j-1}}.
}
\]

Moreover, for \(t=2^{j+1}\), the entire primitive part is \(F_j\), so
\[
C_{2^{j+1}}=\tau(F_j)-1
\]
and
\[
\boxed{
a(2^{j+1})
=
\bigl(\tau(F_j)-1\bigr)b_{2^j}.
}
\]

Thus, if \(F_j\) is prime, the exact-order mass at \(2^j\) receives only one copy at exact order \(2^{j+1}\). This does not disprove the conjecture, because other orders in the shell may contribute greatly. It does show that a proof based solely on direct descendants of old order mass would require information not presently available uniformly for Fermat and related cyclotomic values.

---

### 7. Why the basic primitive-extension recurrence is insufficient

The inequality \(a(t)\ge B(t)\) by itself cannot imply divergence.

Indeed, consider an abstract nonnegative integer sequence \(\widehat a\) defined recursively by
\[
\widehat a(1)=1,\qquad
\widehat a(m)=
\sum_{\substack{d\mid m\\d<m}}\widehat a(d)+h(m),
\]
where \(h(m)\ge0\). Define
\[
\widehat f(N)=
\sum_{r\le N}\widehat a(r)\left\lfloor\frac Nr\right\rfloor.
\]

Choose \(n_j=3^j\), and let \(h\) vanish except at the \(n_j\). Once the earlier values have been fixed, set temporarily \(h(n_j)=0\) and let \(A_j\) be the resulting value of \(\widehat f(2n_j)\). Choose
\[
h(n_j)=H_j\ge jA_j.
\]

The contribution of \(H_j\) to \(\widehat a(m)\) for \(m\le2n_j\) occurs only at \(m=n_j\) and \(m=2n_j\), with coefficient \(1\) at each. Hence its contribution to \(\widehat f(n_j)\) is \(H_j\), while its contribution to \(\widehat f(2n_j)\) is \(3H_j\). Later innovations do not affect this range because \(n_{j+1}>2n_j\). Therefore
\[
\frac{\widehat f(2n_j)}{\widehat f(n_j)}
\le
3+\frac{A_j}{H_j}
\le3+\frac1j.
\]

This is only an abstract model, not a counterexample involving Mersenne numbers. It rigorously shows that the one-primitive-prime recurrence, even though sufficient for \(R(n)\ge3\), cannot by itself prove divergence.

## Self-Audit

1. **Primitive-prime duplication is the most delicate proved step.**  
   It relies on the product \(dq_t\) still dividing \(2^t-1\) and having exact order \(t\). This holds because \(d\mid2^r-1\mid2^t-1\), \(q_t\nmid d\), and multiplicative orders over coprime moduli combine by least common multiple. The exceptional order \(6\) was checked directly.

2. **The weighted primitive-part bound may be far from the true \(a(t)\).**  
   Products of primes of several proper orders can have least common multiple \(t\), so \(C_tB(t)\) does not capture all exact-order mass. This is harmless for the stated lower bound, but it means failure to control \(C_t\) does not prove the conjecture false.

3. **The Fermat discussion is an obstruction to this method, not an obstruction to the conjecture.**  
   Even if \(\tau(F_j)-1\) is small, unrelated orders in \((2^j,2^{j+1}]\) might still dominate \(f(2^j)\). I use the Fermat identities only to show why direct order-doubling cannot be uniformly amplified with current information.

## Computations To Verify

The following uses complete factorizations; for proof-level data, `factorint` should be replaced or supplemented by certified primality and factorization records.

```python
from sympy import factorint, divisors, n_order

def tau_from_factorization(fac):
    ans = 1
    for e in fac.values():
        ans *= (e + 1)
    return ans

def compute_data(K):
    # Computes all data through K.
    fac = [None] * (K + 1)
    b = [0] * (K + 1)
    a = [0] * (K + 1)
    f = [0] * (K + 1)

    for k in range(1, K + 1):
        M = (1 << k) - 1
        fac[k] = factorint(M)
        b[k] = tau_from_factorization(fac[k])
        a[k] = b[k] - sum(a[d] for d in divisors(k) if d < k)
        assert a[k] >= 0
        f[k] = f[k - 1] + b[k]

    return fac, b, a, f

N = 100
fac, b, a, f = compute_data(2 * N)

# Verify exact-order inversion and the new universal bound.
for k in range(1, 2 * N + 1):
    assert b[k] == sum(a[d] for d in divisors(k))

for n in range(1, N + 1):
    Bshell = sum(
        sum(a[d] for d in divisors(t) if d < t)
        for t in range(n + 1, 2 * n + 1)
    )
    Sshell = sum(a[t] for t in range(n + 1, 2 * n + 1))

    Q = sum(
        a[r] * ((2 * n) // r - n // r)
        for r in range(1, n + 1)
    )

    assert Bshell == Q
    assert Q >= f[n]
    assert Sshell >= Q
    assert f[2 * n] >= 3 * f[n]

# Primitive parts P_t and C_t.
C = [0] * (2 * N + 1)
for t in range(1, 2 * N + 1):
    primitive_tau = 1
    for p, e in fac[t].items():
        if n_order(2, p) == t:
            primitive_tau *= (e + 1)
    C[t] = primitive_tau - 1

    proper_mass = sum(a[d] for d in divisors(t) if d < t)
    assert a[t] >= C[t] * proper_mass

    if t not in (1, 6):
        assert C[t] >= 1

# Weighted Route 4 lower bound.
for n in range(6, N + 1):
    W = sum(
        C[t] * sum(a[d] for d in divisors(t) if d < t)
        for t in range(n + 1, 2 * n + 1)
    )
    S = sum(a[t] for t in range(n + 1, 2 * n + 1))
    assert S >= W
    print(n, "R =", f[2*n] / f[n], "W/f =", W / f[n], "S/f =", S / f[n])

# Multi-order primitive-prime lower bound for t = 2r.
for r in range(1, N + 1):
    if r == 3:
        continue
    u = r
    alpha = 0
    while u % 2 == 0:
        u //= 2
        alpha += 1
    delta = int(alpha == 0 and u % 3 == 0)
    exponent = tau_from_factorization(factorint(u)) - 1 - delta
    rhs = b[r] * (2 ** exponent)
    assert a[2 * r] >= rhs

# Final-half mass comparison.
for n in range(1, N + 1):
    top = sum(b[r] for r in range(n // 2 + 1, n + 1)
              if 2 * r > n)
    # More directly enforce n/2 < r <= n:
    top = sum(b[r] for r in range(1, n + 1) if 2 * r > n)
    assert f[n] <= 2 * top

# Fermat identities for feasible j.
for j in range(1, 7):
    n = 2 ** j
    Fj_minus_1 = (1 << (2 ** (j - 1))) + 1
    tau_F_prev = tau_from_factorization(factorint(Fj_minus_1))
    assert a[n] == (tau_F_prev - 1) * b[n // 2]

    Fj = (1 << (2 ** j)) + 1
    tau_F = tau_from_factorization(factorint(Fj))
    assert a[2 * n] == (tau_F - 1) * b[n]
```

The most informative experimental quantities are:

```python
# Weighted mass on exponents with simple odd part.
for H in range(1, 8):
    for n in range(10, N + 1):
        low = 0
        for r in range(1, n + 1):
            if 2 * r <= n:
                continue
            u = r
            alpha = 0
            while u % 2 == 0:
                u //= 2
                alpha += 1
            h = tau_from_factorization(factorint(u))
            if alpha == 0 and u % 3 == 0:
                h -= 1
            if h <= H:
                low += b[r]
        print(H, n, low / f[n])
```

If these weighted exceptional proportions fail to decrease near local minima of \(R(n)\), the multi-order amplification route is unlikely to close the problem.

## Route Diagnosis

**Proved ledger**

- \(a(t)\ge\sum_{r\mid t,\ r<t}a(r)\) for every \(t>1\).
- The next dyadic block contains at least two copies, in aggregate, of all divisor occurrences counted by \(f(n)\).
- Consequently,
  \[
  f(2n)\ge3f(n)
  \]
  for every \(n\).
- If \(P_t\) is the primitive part of \(\Phi_t(2)\), then
  \[
  a(t)\ge(\tau(P_t)-1)\sum_{r\mid t,\ r<t}a(r).
  \]
- The nonprimitive part of \(\Phi_t(2)\) is squarefree and divides \(\operatorname{rad}(t)\).
- Products of selected primitive primes give
  \[
  a(2r)\ge
  b_r\,2^{\tau(\operatorname{odd}(r))-1-
  \mathbf1_{r\text{ odd},\,3\mid r}}
  \]
  apart from the explicitly excluded \(r=3\).
- At powers of \(2\), the exact amplification is governed by consecutive Fermat numbers.

**Plausible but unproved claims needed to finish**

- The weighted primitive amplification
  \[
  \sum_{r\le n}a(r)
  \sum_{\substack{n<t\le2n\\r\mid t}}C_t
  \]
  dominates \(f(n)\) by a factor tending to infinity.
- Equivalently in the multi-order approach, \(b_r\)-mass in the final half-block does not concentrate on exponents whose odd parts have bounded divisor count.
- Large recent exact-order spikes necessarily force substantial unrelated exact-order mass elsewhere in the following dyadic shell.

**Dead ends**

- One primitive prime per order gives the sharp fixed-factor mechanism \(R(n)\ge3\), but an abstract lacunary-innovation model shows that this recurrence alone permits bounded dyadic ratios.
- The size of \(\Phi_t(2)\) does not force many primitive prime factors or many divisors.
- Direct descendants of order \(2^j\) are controlled exactly by \(\tau(F_j)-1\), for which no useful uniform growth theorem is known.
- Route 1 reappears as the weighted exceptional-set criterion above and has the same concentration obstruction.
- Route 6 would require upper bounds on entire Mersenne blocks, for which current tools are markedly weaker.

A fresh attempt should seek a collision-free way to use products of several proper-order primitive factors simultaneously across all \(r\mid t\), not merely primitive factors of exact order \(t\). The critical case to attack is recent mass concentrated at exponents \(2^\alpha u\) with \(\tau(u)\) bounded; without controlling that case, Route 4 remains blocked.