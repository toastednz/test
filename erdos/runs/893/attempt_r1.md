STATUS: BLOCKED

## Result

Route 1 reduces the problem to a genuine weighted-concentration obstruction that current tools do not control. I proved that \(\tau(2^k+1)\) tends to infinity on average and that, for every fixed \(T\), the indices with \(\tau(2^k+1)\le T\) have natural density zero. More strongly, exact-order decomposition shows that every part of \(f(n)\) arising from orders \(r\) having many multiples below \(n\) is amplified by an arbitrarily large average doubling factor. Consequently, if the Route 1 weighted average remains bounded along a subsequence, then almost all of \(f(n)\) must come from “terminal” exact orders \(r>n/K\), for every fixed large \(K\), and a positive proportion of \(f(n)\) must be concentrated on a density-zero set of terminal exponents whose odd parts have bounded divisor count. No available theorem excludes such terminal spikes; doing so appears comparable in difficulty to the original uniform problem.

## Complete Argument

Write

\[
b_k=\tau(2^k-1),\qquad c_k=\tau(2^k+1),
\]

and define the Route 1 lower bound

\[
L(n)=\frac{\sum_{k\le n}b_kc_k}{f(n)}.
\]

Since

\[
b_{2k}=b_kc_k,
\]

retaining only the even-indexed terms gives

\[
R(n)=\frac{f(2n)}{f(n)}\ge L(n).
\]

Thus \(L(n)\to\infty\) would solve the problem affirmatively.

### 1. A uniform lower bound for \(c_k\)

Write

\[
k=2^\alpha u,\qquad u\ \text{odd}.
\]

Then

\[
\boxed{
c_k\ge
2^{\tau(u)-\mathbf 1_{\alpha=0,\ 3\mid u}}
\ge 2^{\tau(u)-1}.
}
\tag{1}
\]

#### Proof

For every divisor \(e\mid u\), consider

\[
s=2^{\alpha+1}e.
\]

Except when \(s=6\), Bang–Zsigmondy provides a prime \(p_s\) dividing \(2^s-1\) but no earlier \(2^j-1\). Therefore

\[
\operatorname{ord}_{p_s}(2)=s.
\]

In the field \(\mathbb F_{p_s}\), the element \(2^{s/2}\) has order \(2\), hence equals \(-1\). Since

\[
k=\frac{s}{2}\frac{u}{e}
\]

and \(u/e\) is odd,

\[
2^k=\left(2^{s/2}\right)^{u/e}\equiv -1\pmod{p_s}.
\]

Thus \(p_s\mid 2^k+1\).

Different values of \(s\) give different primes because a prime has a unique multiplicative order. There are \(\tau(u)\) choices of \(e\), with precisely one possible exceptional choice: \(s=6\), which occurs exactly when \(\alpha=0\) and \(e=3\). Hence \(2^k+1\) has at least

\[
\tau(u)-\mathbf 1_{\alpha=0,\ 3\mid u}
\]

distinct prime factors, proving (1). ∎

### 2. Low doubling factors form a density-zero set

For fixed \(T\ge2\), let

\[
E_T=\{k\ge1:c_k\le T\}.
\]

Then

\[
\boxed{\#(E_T\cap[1,n])=o_T(n).}
\tag{2}
\]

#### Proof

If \(k=2^\alpha u\in E_T\), then (1) gives

\[
2^{\tau(u)-1}\le T,
\]

so

\[
\tau(u)\le 1+\log_2T.
\]

Since \(\tau(u)\ge 2^{\omega(u)}\), the number \(\omega(u)\) of distinct prime divisors of \(u\) is bounded in terms of \(T\).

We first prove that for every fixed \(s\), the set

\[
\mathcal S_s=\{m:\omega(m)\le s\}
\]

has natural density zero. Let \(p_1,\dots,p_J\) be the first \(J\) primes. Every \(m\in\mathcal S_s\) is divisible by at most \(s\) of these primes. By the Chinese remainder theorem, the density of integers divisible by exactly the primes indexed by \(I\subseteq\{1,\dots,J\}\) among these \(J\) primes is

\[
\prod_{i\in I}\frac1{p_i}
\prod_{i\notin I}\left(1-\frac1{p_i}\right).
\]

Therefore the upper density of \(\mathcal S_s\) is at most

\[
\delta_{J,s}
=
\prod_{i=1}^J\left(1-\frac1{p_i}\right)
\sum_{\substack{I\subseteq\{1,\dots,J\}\\ |I|\le s}}
\prod_{i\in I}\frac1{p_i-1}.
\]

Put \(\lambda_J=\sum_{i\le J}1/p_i\). Then

\[
\prod_{i=1}^J\left(1-\frac1{p_i}\right)
\le e^{-\lambda_J}.
\]

Also

\[
\sum_{i\le J}\frac1{p_i-1}\le 2\lambda_J,
\]

and hence, using the elementary-symmetric-polynomial bound,

\[
\sum_{|I|\le s}\prod_{i\in I}\frac1{p_i-1}
\le
\sum_{j=0}^s\frac{(2\lambda_J)^j}{j!}.
\]

Euler’s divergence \(\sum_p1/p=\infty\) now gives

\[
\delta_{J,s}\longrightarrow0.
\]

Thus \(\mathcal S_s\) has density zero.

Finally, every \(k\) has a unique representation \(k=2^\alpha u\) with \(u\) odd. If \(A(x)\) counts the admissible odd \(u\le x\), then \(A(x)=o(x)\), and

\[
\#(E_T\cap[1,n])
\le
\sum_{\alpha\ge0}A(n/2^\alpha).
\]

Given \(\varepsilon>0\), choose \(X_0\) such that \(A(x)\le\varepsilon x\) for \(x\ge X_0\). The terms with \(n/2^\alpha\ge X_0\) contribute at most

\[
\varepsilon n\sum_{\alpha\ge0}2^{-\alpha}\le2\varepsilon n.
\]

The remaining tail contributes \(O(X_0)\). Dividing by \(n\) and then sending \(\varepsilon\to0\) proves (2). ∎

This is only an unweighted density statement. It does not imply

\[
\sum_{\substack{k\le n\\c_k\le T}}b_k=o(f(n)).
\]

That missing weighted upgrade is precisely the main difficulty.

### 3. The unweighted mean of \(c_k\) diverges

Define

\[
h(j)=2^{\tau(\operatorname{odd}(j))-1},
\]

where \(\operatorname{odd}(j)\) is the odd part of \(j\). By (1),

\[
c_j\ge h(j).
\]

Moreover,

\[
\boxed{
\frac1X\sum_{j\le X}h(j)\longrightarrow\infty.
}
\tag{3}
\]

#### Proof

Let \(q_s\) be the product of the first \(s\) odd primes. It is squarefree and

\[
\tau(q_s)=2^s.
\]

For every multiple \(j\) of \(q_s\), its odd part is divisible by \(q_s\), so

\[
h(j)\ge 2^{2^s-1}.
\]

For \(X\ge2q_s\),

\[
\frac1X\sum_{j\le X}h(j)
\ge
\frac{\lfloor X/q_s\rfloor}{X}2^{2^s-1}
\ge
\frac{2^{2^s-2}}{q_s}.
\]

By Bertrand’s postulate, if the odd primes are \(p_1<p_2<\cdots\), then \(p_i<2^{i+1}\). Consequently

\[
q_s<2^{s(s+3)/2}.
\]

It follows that

\[
\log_2\left(\frac{2^{2^s-2}}{q_s}\right)
\ge
2^s-2-\frac{s(s+3)}2\longrightarrow\infty.
\]

Given any \(B\), choose \(s\) so that the displayed lower bound exceeds \(B\). It then holds for every \(X\ge2q_s\), proving (3). ∎

Thus the obstruction is not a scarcity of large \(c_k\); it is possible concentration of the weights \(b_k\) on the sparse exceptional set.

### 4. Dyadic chains show that \(f(n)\) is concentrated near \(n\)

For each odd \(u\le n\), let \(A_u\) be the largest integer such that

\[
2^{A_u}u\le n,
\]

and put

\[
x_{u,a}=b_{2^au}.
\]

Since \(x_{u,a+1}=x_{u,a}c_{2^au}\) and \(c_k\ge2\),

\[
x_{u,a+1}\ge2x_{u,a}.
\]

Consequently,

\[
\sum_{a=0}^{A_u}x_{u,a}<2x_{u,A_u}.
\]

The map \(u\mapsto2^{A_u}u\) is a bijection from the odd \(u\le n\) to the integers \(k\) satisfying \(n/2<k\le n\). Summing over \(u\) gives

\[
\boxed{
\sum_{n/2<k\le n}b_k
\le f(n)
<
2\sum_{n/2<k\le n}b_k.
}
\tag{4}
\]

Thus at least half of \(f(n)\) always lies in the terminal half interval.

There is also an exact chain identity. Since

\[
\sum_{k\le n}b_kc_k=\sum_{k\le n}b_{2k},
\]

we have

\[
\boxed{
\sum_{k\le n}b_kc_k-f(n)
=
\sum_{\substack{u\le n\\u\text{ odd}}}
\left(b_{2^{A_u+1}u}-b_u\right).
}
\tag{5}
\]

This identity does not itself force divergence: a dyadic chain can undergo a huge increase at one step and have its next multiplier \(c_k\) small.

### 5. A bounded Route 1 average forces terminal concentration on a sparse set

Suppose that for some \(n\),

\[
L(n)\le C.
\]

Since \(c_k\ge2\), necessarily \(C\ge2\). For every \(T>0\),

\[
T\sum_{\substack{k\le n\\c_k>T}}b_k
\le
\sum_{k\le n}b_kc_k
\le Cf(n),
\]

so

\[
\sum_{\substack{k\le n\\c_k>T}}b_k
\le \frac CTf(n).
\tag{6}
\]

Combining (4) and (6),

\[
\sum_{\substack{n/2<k\le n\\c_k\le T}}b_k
\ge
\left(\frac12-\frac CT\right)f(n).
\tag{7}
\]

In particular, choosing \(T=4C\),

\[
\boxed{
\sum_{\substack{n/2<k\le n\\c_k\le4C}}b_k
\ge\frac14f(n).
}
\tag{8}
\]

By (2), the set \(\{k:c_k\le4C\}\) has density zero. Thus a bounded subsequence of \(L(n)\) can exist only if at least one quarter of the entire weight \(f(n)\) repeatedly concentrates on a fixed density-zero subset of the terminal half interval. This is a much stronger requirement than ordinary unweighted exceptional behavior, but there is presently no upper bound for \(b_k\) strong enough to rule it out.

### 6. Exact-order averaging amplifies every nonterminal part of \(f(n)\)

Recall

\[
b_k=\sum_{r\mid k}a(r),\qquad
f(n)=\sum_{r\le n}a(r)\left\lfloor\frac nr\right\rfloor.
\]

Expanding the Route 1 numerator and interchanging finite sums gives

\[
\begin{aligned}
\sum_{k\le n}b_kc_k
&=
\sum_{k\le n}c_k\sum_{r\mid k}a(r)\\
&=
\sum_{r\le n}a(r)
\sum_{j\le n/r}c_{rj}.
\end{aligned}
\tag{9}
\]

The point is that the inner average diverges uniformly with the number of multiples. Indeed, the odd part of \(j\) divides the odd part of \(rj\), so (1) gives

\[
c_{rj}
\ge
2^{\tau(\operatorname{odd}(rj))-1}
\ge
2^{\tau(\operatorname{odd}(j))-1}
=h(j).
\tag{10}
\]

Set

\[
A(X)=\frac1X\sum_{j\le X}h(j),
\qquad
H(K)=\inf_{X\ge K}A(X).
\]

By (3),

\[
H(K)\longrightarrow\infty.
\tag{11}
\]

For an integer \(K\ge1\), define the contribution from exact orders with at least \(K\) multiples below \(n\):

\[
F_K(n)=
\sum_{r\le n/K}
a(r)\left\lfloor\frac nr\right\rfloor.
\]

If \(r\le n/K\), then \(X=\lfloor n/r\rfloor\ge K\), and (10) gives

\[
\sum_{j\le X}c_{rj}
\ge XH(K).
\]

For the remaining \(r\), we retain the universal bound \(c_{rj}\ge2\). Consequently, whenever \(H(K)\ge2\),

\[
\boxed{
L(n)\ge
2+\bigl(H(K)-2\bigr)\frac{F_K(n)}{f(n)}.
}
\tag{12}
\]

This yields a clean sufficient criterion:

> If there is a function \(K(n)\to\infty\) and a constant \(\delta>0\) such that
> \[
> F_{K(n)}(n)\ge\delta f(n)
> \]
> for all sufficiently large \(n\), then \(L(n)\to\infty\), hence \(R(n)\to\infty\).

Conversely, if \(L(n)\le C\), then (12) implies

\[
\boxed{
\frac{F_K(n)}{f(n)}
\le
\frac{C-2}{H(K)-2}.
}
\tag{13}
\]

Therefore, along any subsequence on which \(L(n)\le C\), for every \(\eta>0\) one may choose a fixed \(K\) such that

\[
\sum_{r>n/K}
a(r)\left\lfloor\frac nr\right\rfloor
\ge(1-\eta)f(n).
\tag{14}
\]

Thus failure of Route 1 requires almost all exact-order mass to come from orders having only \(O_K(1)\) multiples below \(n\). These are precisely fresh or terminal orders.

### 7. Why the terminal contribution is presently uncontrolled

Neither Bang–Zsigmondy nor generic divisor bounds control

\[
\sum_{r>n/K}a(r)\left\lfloor\frac nr\right\rfloor
\]

from above relative to \(f(n)\). Bang–Zsigmondy gives lower bounds for \(a(r)\) or \(b_r\), not upper bounds. Wigert’s theorem permits an individual terminal value \(b_r\) as large as

\[
\exp\!\left(O\!\left(\frac r{\log r}\right)\right),
\]

far beyond available uniform lower bounds for the accumulated nonterminal mass.

A representative obstruction is a dyadic endpoint. Iterating \(b_{2k}=b_kc_k\) gives

\[
b_{2^a}=\prod_{j=0}^{a-1}\tau(2^{2^j}+1).
\]

A very large divisor count for one Fermat number \(2^{2^{a-1}}+1\) can make \(b_{2^a}\) a fresh terminal spike, while the next factor

\[
c_{2^a}=\tau(2^{2^a}+1)
\]

could still be small. There is no unconditional theorem ruling out repeated behavior of this kind, nor a theorem showing that other exponents must provide enough competing \(b_k\)-mass.

### 8. A tempting exact-order identity for \(c_k\) is false

One might try to write, for \(k=2^\alpha u\),

\[
c_k\stackrel{?}=1+\sum_{e\mid u}a(2^{\alpha+1}e).
\]

This is false because a composite modulus can have order \(2^{\alpha+1}e\) without dividing \(2^k+1\): modulo a composite number, an element of order \(2\) need not equal \(-1\).

The first counterexample is \(k=3\). Here

\[
c_3=\tau(9)=3,
\]

while \(a(2)=1\) and \(a(6)=3\), so the proposed formula gives \(5\). The three exact-order-\(6\) divisors of \(63\) are \(9,21,63\), but only \(9\) divides \(2^3+1\). This kills a potentially stronger direct connection between terminal \(a(r)\) and \(c_r\).

## Self-Audit

1. **Use of Bang–Zsigmondy in (1).**  
   The proof depends on the primitive-divisor theorem, including its unique relevant exception \(s=6\). The passage from exact order \(s\) to divisibility of \(2^k+1\) is valid because it is performed modulo a prime, where the unique element of order \(2\) is \(-1\).

2. **The claims about sparse exceptional sets are only unweighted.**  
   Density zero does not imply negligible \(b_k\)-weight, and I have not used it as though it did. Equations (7)–(8) explicitly identify this gap rather than resolving it.

3. **The exact-order criterion (12) leaves the central terminal-mass estimate unproved.**  
   All interchanges in (9) are finite and (10) is termwise, so the reduction itself is rigorous. What is missing is any theorem ensuring that \(F_{K(n)}(n)\) is a nonvanishing fraction of \(f(n)\) for some \(K(n)\to\infty\). Establishing that appears to require new upper control on fresh exact-order spikes.

## Computations To Verify

The following Sage/Python code performs exact factorizations, checks all identities above, and measures the two obstructions. For rigorous data, Sage should be run with proof mode enabled and every factorization allowed to complete.

```python
from sage.all import *

proof.all(True)

def tau_exact(m):
    m = ZZ(m)
    if m == 1:
        return ZZ(1)
    fac = factor(m, proof=True)
    return prod(e + 1 for p, e in fac)

def odd_part_and_v2(k):
    k = ZZ(k)
    alpha = 0
    while k % 2 == 0:
        k //= 2
        alpha += 1
    return k, alpha

N = 100                  # increase only as complete factorization permits
MAXK = 2 * N

b = [ZZ(0)] * (MAXK + 1)
c = [ZZ(0)] * (MAXK + 1)

for k in range(1, MAXK + 1):
    b[k] = tau_exact(2**k - 1)
    c[k] = tau_exact(2**k + 1)

# Exact-order masses.
exact = [ZZ(0)] * (MAXK + 1)
for k in range(1, MAXK + 1):
    exact[k] = b[k] - sum(exact[d] for d in divisors(k) if d < k)
    assert exact[k] >= 0
    assert b[k] == sum(exact[d] for d in divisors(k))

# Prefix sums.
f = [ZZ(0)] * (MAXK + 1)
for k in range(1, MAXK + 1):
    f[k] = f[k - 1] + b[k]

# Check b_{2k} = b_k c_k and the Route 1 lower bound.
for k in range(1, N + 1):
    assert b[2*k] == b[k] * c[k]

for n in range(1, N + 1):
    numerator = sum(b[k] * c[k] for k in range(1, n + 1))
    L = QQ(numerator) / f[n]
    R = QQ(f[2*n]) / f[n]
    assert R >= L
    print("n =", n, "L =", L, "R =", R)

# Check the Zsigmondy lower bound for c_k.
for k in range(1, MAXK + 1):
    u, alpha = odd_part_and_v2(k)
    exception = 1 if (alpha == 0 and u % 3 == 0) else 0
    lower = 2**(tau_exact(u) - exception)
    assert c[k] >= lower

# Check the dyadic terminal-half estimate.
for n in range(1, N + 1):
    tail = sum(b[k] for k in range(n//2 + 1, n + 1)
               if 2*k > n)   # exactly n/2 < k <= n
    assert tail <= f[n]
    assert f[n] <= 2 * tail

# Check the exact dyadic-chain identity (5).
for n in range(1, N + 1):
    lhs = sum(b[k] * c[k] for k in range(1, n + 1)) - f[n]
    rhs = 0
    for u in range(1, n + 1, 2):
        A = 0
        while 2**(A + 1) * u <= n:
            A += 1
        rhs += b[2**(A + 1) * u] - b[u]
    assert lhs == rhs

# Check the exact-order expansion of the weighted numerator.
for n in range(1, N + 1):
    lhs = sum(b[k] * c[k] for k in range(1, n + 1))
    rhs = sum(
        exact[r] * sum(c[r*j] for j in range(1, n//r + 1))
        for r in range(1, n + 1)
    )
    assert lhs == rhs

# Check the termwise lower c_{rj} >= h(j).
h = [ZZ(0)] * (N + 1)
for j in range(1, N + 1):
    u, _ = odd_part_and_v2(j)
    h[j] = 2**(tau_exact(u) - 1)

for r in range(1, N + 1):
    for j in range(1, N//r + 1):
        assert c[r*j] >= h[j]

# Measure terminal exact-order concentration.
K_values = [2, 4, 8, 16]
for n in range(1, N + 1):
    numerator = sum(b[k] * c[k] for k in range(1, n + 1))
    L = QQ(numerator) / f[n]

    print("\nn =", n, "L =", L)
    for K in K_values:
        old = sum(
            exact[r] * (n // r)
            for r in range(1, n // K + 1)
        )
        recent = f[n] - old
        print(" K =", K,
              "old fraction =", QQ(old) / f[n],
              "recent fraction =", QQ(recent) / f[n])

# Measure b-weight on low-c terminal indices.
T_values = [2, 4, 8, 16]
for n in range(1, N + 1):
    for T in T_values:
        low_all = sum(b[k] for k in range(1, n + 1) if c[k] <= T)
        low_tail = sum(
            b[k] for k in range(1, n + 1)
            if 2*k > n and c[k] <= T
        )
        print("n =", n, "T =", T,
              "low/all =", QQ(low_all) / f[n],
              "low-tail/all =", QQ(low_tail) / f[n])

# Explicitly verify the false candidate formula at k=3.
assert c[3] == 3
assert exact[2] == 1
assert exact[6] == 3
assert 1 + exact[2] + exact[6] == 5 != c[3]
```

The most informative numerical outputs are:

1. Local minima of \(L(n)\).
2. At those minima, the fractions \(F_K(n)/f(n)\) for increasing \(K\).
3. The \(b_k\)-mass in \(n/2<k\le n\) with \(c_k\le T\).
4. Whether a single terminal value \(b_k\) dominates that exceptional mass.

## Route Diagnosis

**Proved ledger.**

- \(c_k\ge2^{\tau(\operatorname{odd}(k))-1}\), with the sharper stated Zsigmondy exception.
- For fixed \(T\), the set \(c_k\le T\) has density zero.
- The unweighted average of \(c_k\) tends to infinity.
- At least half of \(f(n)\) lies in \(n/2<k\le n\).
- If \(L(n)\) is bounded, a positive proportion of \(f(n)\) lies on a fixed density-zero set of low-\(c_k\) terminal indices.
- Every exact-order contribution repeated at least \(K\) times below \(n\) receives average amplification at least \(H(K)\to\infty\).
- Therefore bounded \(L(n)\) forces asymptotically complete concentration on terminal exact orders \(r>n/K\), for every fixed large \(K\).

**Plausible but unproved.**

- The \(b_k\)-weight of \(\{k:c_k\le T\}\) is \(o(f(n))\).
- Fresh exact orders \(r>n/K\) cannot account for almost all of \(f(n)\) once \(K\) is large.
- Terminal spikes at exponents with simple odd part are sufficiently diluted by related exponents.

Any one of these, in suitable quantitative form, would complete Route 1.

**Dead ends.**

- The proposed exact-order formula for \(c_k\) is false already at \(k=3\).
- Positive-correlation arguments for divisibility-monotone functions fail near a cutoff: for example, on \(\{1,\dots,5\}\), divisibility by \(2\) and divisibility by \(3\) each occur, but their intersection is empty.
- Multiplying a bad exponent by a fixed odd integer only transfers weights from \(k\le n/Q\); it gives no control over the terminal interval \(k>n/Q\).
- Generic divisor-function upper bounds are exponentially too weak to exclude one fresh terminal Mersenne spike.

The hybrid exact-order analysis is the strongest refinement of Route 1 found here, but it reaches the same central barrier as Route 2: uncontrolled mass newly appearing at orders comparable to the cutoff. No superior alternative emerged that bypasses this terminal-spike problem.