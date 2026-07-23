STATUS: BLOCKED

## Result

Route 2 yields two rigorous, uniform partial results. First, if
\[
L_A(N):=\max\!\left(1,\max_{n\le N}r_A(n)\right),
\]
then for all sufficiently large \(N\),
\[
E_A(N)L_A(N)\gg \sqrt{\frac{N}{\log N}}.
\]
Consequently Q1 holds for every \(A\) satisfying \(L_A(N)=N^{o(1)}\). Second, without any multiplicity hypothesis,
\[
E_A(N)\gg \log N
\]
uniformly for every \(A\) and all sufficiently large \(N\). The argument uses the generating-function identity on the negative real axis, where a positive diagonal term survives, followed by localization and a multiscale charging argument. This falls far short of the required \(N^{1/2-o(1)}\) support bound. The precise obstruction is concentration: one exceptional sum can have multiplicity \(\asymp\sqrt N\), enough to absorb the entire discrepancy visible to the negative-axis argument. I also give an explicit finite family with \(E(N)=3\sqrt N+O(1)\) and a single coefficient of size \(\asymp\sqrt N\), and prove that reduction modulo \(2\) is completely blind to the problem.

## Complete Argument

### 1. Generating functions on the negative real axis

Write
\[
h(n)=r_A(n)-1,
\qquad
H(z)=\sum_{n\ge1}h(n)z^n,
\qquad
F(z)=\sum_{a\in A}z^a.
\]
Since \(r_A(n)\le \lfloor n/2\rfloor\), we have \(|h(n)|\le n\), so \(H(z)\) converges absolutely for \(|z|<1\).

The standard identity gives
\[
\frac{F(z)^2+F(z^2)}2
=
\frac{z}{1-z}+H(z).
\]
Putting \(z=-\rho\), where \(0<\rho<1\), yields
\[
H(-\rho)
=
\frac{F(-\rho)^2+F(\rho^2)}2+\frac{\rho}{1+\rho}.
\]
Because \(F(-\rho)\) is real,
\[
\boxed{H(-\rho)\ge \frac12F(\rho^2).}
\tag{1}
\]

Define the favorable part of \(h\) by
\[
q_n=\max\bigl((-1)^nh(n),0\bigr).
\]
Thus \(q_n>0\) only if \(n\) is exceptional. More explicitly, favorable terms are:

- even \(n\) with \(r_A(n)\ge2\), contributing \(r_A(n)-1\);
- odd \(n\) with \(r_A(n)=0\), contributing \(1\).

Since
\[
H(-\rho)=\sum_{n\ge1}(-1)^nh(n)\rho^n
\le \sum_{n\ge1}q_n\rho^n,
\]
equation (1) gives
\[
\boxed{\sum_{n\ge1}q_n\rho^n\ge \frac12F(\rho^2).}
\tag{2}
\]

This is the main analytic inequality.

---

### 2. Elementary bounds for \(A(x)\) and exceptional multiplicities

Let
\[
A(x)=|A\cap[1,x]|.
\]

#### Lemma 1: Lower bound from coverage

For every integer \(M\ge1\),
\[
\frac{A(M)(A(M)+1)}2\ge M-E_A(M).
\tag{3}
\]

#### Proof

Each represented \(n\le M\) has a representing pair whose two entries lie in \(A\cap[1,M]\). Distinct represented integers require distinct pairs because a pair has only one sum. There are \(M-E_A(M)\) represented integers and \(A(M)(A(M)+1)/2\) unordered pairs. ∎

In particular, if \(E_A(M)\le M/2\) and \(M\ge4\), then
\[
A(M)\ge \frac12\sqrt M.
\tag{4}
\]

Indeed, otherwise \(A(M)<\sqrt M/2\), and then
\[
\frac{A(M)(A(M)+1)}2<\frac M2
\]
for \(M\ge4\), contradicting (3).

#### Lemma 2: Multiplicity bound in terms of support

For every \(n\ge1\),
\[
r_A(n)\le \sqrt{2n}+2E_A(n).
\tag{5}
\]
Consequently,
\[
q_n\le \sqrt{2n}+2E_A(n).
\tag{6}
\]

#### Proof

Set
\[
m=A(\lfloor n/2\rfloor).
\]
Every representation of \(n\) is determined by its smaller summand, which belongs to \(A\cap[1,n/2]\), so
\[
r_A(n)\le m.
\tag{7}
\]

All \(m(m+1)/2\) unordered pairs from \(A\cap[1,n/2]\) have sum at most \(n\). Therefore
\[
\frac{m(m+1)}2
\le \sum_{j\le n}r_A(j).
\]
Writing
\[
Z(n)=|\{j\le n:r_A(j)=0\}|,
\qquad
\Delta(n)=\sum_{\substack{j\le n\\r_A(j)\ge2}}(r_A(j)-1),
\]
we have
\[
\sum_{j\le n}r_A(j)=n-Z(n)+\Delta(n)\le n+\Delta(n).
\]
For every \(j\le n\),
\[
r_A(j)\le A(j/2)\le m.
\]
There are at most \(E_A(n)\) positive terms in \(\Delta(n)\), hence
\[
\Delta(n)\le E_A(n)m.
\]
Thus
\[
\frac{m(m+1)}2\le n+E_A(n)m.
\]
Solving the resulting quadratic inequality gives
\[
m
\le
\frac{2E_A(n)-1+
\sqrt{(2E_A(n)-1)^2+8n}}2
\le 2E_A(n)+\sqrt{2n}.
\]
Together with (7), this proves (5). If \(q_n\) comes from a missing odd integer, then \(q_n=1\); otherwise \(q_n\le r_A(n)\). This proves (6). ∎

---

### 3. Localization of the negative-axis inequality

The full series in (2) includes exceptions beyond \(N\). We suppress them by taking a radius whose effective scale is \(N/\log N\).

#### Lemma 3: Localized favorable mass

There are absolute constants \(c_0>0\) and \(N_0\) such that the following holds. Let \(N\ge N_0\), let \(M\) be an integer satisfying
\[
4\le M\le \frac{N}{8\log N},
\]
and suppose
\[
E_A(N)\le \frac M2.
\]
Then
\[
\boxed{
\sum_{n\le N}q_ne^{-n/M}\ge c_0\sqrt M.
}
\tag{8}
\]

#### Proof

Take \(\rho=e^{-1/M}\). By (2),
\[
\sum_{n\le N}q_n\rho^n
\ge
\frac12F(\rho^2)-\sum_{n>N}q_n\rho^n.
\tag{9}
\]

Since \(M\le N\),
\[
E_A(M)\le E_A(N)\le M/2.
\]
By (4),
\[
A(M)\ge \frac12\sqrt M.
\]
Every \(a\le M\) satisfies \(\rho^{2a}\ge e^{-2}\), so
\[
F(\rho^2)\ge e^{-2}A(M)\ge \frac{e^{-2}}2\sqrt M.
\tag{10}
\]

For the tail, \(q_n\le |h(n)|\le n\). Hence
\[
\sum_{n>N}q_n\rho^n
\le \sum_{n>N}ne^{-n/M}.
\]
Writing \(\rho=e^{-1/M}\), the exact geometric-series formula gives
\[
\sum_{n=N+1}^\infty n\rho^n
=
\frac{\rho^{N+1}\bigl((N+1)-N\rho\bigr)}{(1-\rho)^2}.
\]
For \(M\ge1\),
\[
1-\rho\ge \frac1{2M},
\qquad
(N+1)-N\rho\le 1+\frac NM.
\]
It follows that
\[
\sum_{n>N}ne^{-n/M}
\le 4(M^2+MN)e^{-N/M}.
\]
Because \(N/M\ge8\log N\) and \(M\le N\),
\[
4(M^2+MN)e^{-N/M}
\le 8N^2N^{-8}=8N^{-6}.
\]
For sufficiently large \(N\), this is at most
\[
\frac{e^{-2}}8\sqrt M.
\]
Combining this with (9) and (10),
\[
\sum_{n\le N}q_ne^{-n/M}
\ge
\frac{e^{-2}}4\sqrt M-\frac{e^{-2}}8\sqrt M
=
\frac{e^{-2}}8\sqrt M.
\]
Thus one may take \(c_0=e^{-2}/8\). ∎

---

### 4. A support–multiplicity tradeoff

Define
\[
L_A(N)=\max\!\left(1,\max_{n\le N}r_A(n)\right).
\]

#### Theorem 1

There are absolute constants \(c>0\) and \(N_0\) such that for every \(A\subseteq\mathbb N\) and \(N\ge N_0\),
\[
\boxed{
E_A(N)L_A(N)\ge c\sqrt{\frac{N}{\log N}}.
}
\tag{11}
\]

#### Proof

Let
\[
k=E_A(N),
\qquad
M=\left\lfloor\frac{N}{8\log N}\right\rfloor.
\]
For sufficiently large \(N\),
\[
M\ge4,
\qquad
M\gg \frac{N}{\log N}.
\]

If \(k>M/2\), then \(L_A(N)\ge1\), so
\[
kL_A(N)\ge \frac M2\gg \sqrt M.
\]

Suppose instead that \(k\le M/2\). Lemma 3 gives
\[
c_0\sqrt M
\le \sum_{n\le N}q_ne^{-n/M}.
\]
There are at most \(k\) nonzero \(q_n\), and each satisfies
\[
q_n\le L_A(N).
\]
Therefore
\[
c_0\sqrt M\le kL_A(N).
\]
Since \(M\gg N/\log N\), equation (11) follows. ∎

#### Corollary 1

If
\[
L_A(N)=N^{o(1)},
\]
then for every \(\epsilon>0\),
\[
E_A(N)\gg_\epsilon N^{1/2-\epsilon}
\]
for all sufficiently large \(N\).

#### Proof

By Theorem 1,
\[
E_A(N)
\gg
\frac{N^{1/2}}{\sqrt{\log N}\,L_A(N)}.
\]
For every fixed \(\epsilon>0\), eventually
\[
L_A(N)\le N^{\epsilon/2},
\qquad
\sqrt{\log N}\le N^{\epsilon/2}.
\]
The conclusion follows. ∎

Thus a counterexample to Q1 must necessarily exhibit large concentrated multiplicities. More precisely, if along some sequence
\[
E_A(N)=o(N^{1/2-\epsilon}),
\]
then along that sequence
\[
L_A(N)\gg
\frac{N^\epsilon}{\sqrt{\log N}}\,
\frac{N^{1/2-\epsilon}}{E_A(N)}.
\]

---

### 5. An unconditional logarithmic support lower bound

The same negative-axis inequality can be applied at many dyadic scales. An exceptional coefficient can substantially support only \(O(1)\) such scales after normalization.

#### Kernel estimate

There is an absolute \(C_1\) such that for all \(u>0\),
\[
\sum_{j\ge0}\sqrt{\frac{u}{2^j}}
\exp\!\left(-\frac{u}{2^j}\right)
\le C_1.
\tag{12}
\]

To see this, if \(u\le1\), discard the exponential and sum a geometric series. If \(u>1\), split at \(j_0=\lfloor\log_2u\rfloor\). For \(j\ge j_0\), the terms are bounded by a geometric series in \(2^{-(j-j_0)/2}\). For \(j<j_0\), the terms are bounded by
\[
C\,2^{(j_0-j)/2}e^{-c2^{j_0-j}},
\]
whose sum converges absolutely.

#### Theorem 2

There are absolute constants \(c>0\) and \(N_0\) such that, for every \(A\subseteq\mathbb N\) and every \(N\ge N_0\),
\[
\boxed{E_A(N)\ge c\log N.}
\tag{13}
\]

#### Proof

Set
\[
k=E_A(N).
\]
Let \(M_0\) be the least power of \(2\) satisfying
\[
M_0\ge\max(4,k^2).
\]
Then \(M_0\ge2k\). Consider the dyadic scales
\[
M_j=2^jM_0
\]
which satisfy
\[
M_j\le \frac{N}{8\log N}.
\]
Let \(J\) be their number.

Since \(k\le M_j/2\), Lemma 3 gives at each such scale
\[
c_0\sqrt{M_j}
\le
\sum_{n\le N}q_ne^{-n/M_j}.
\]
Divide by \(\sqrt{M_j}\) and sum over \(j\):
\[
c_0J
\le
\sum_{\substack{n\le N\\q_n>0}}
q_n
\sum_{j=0}^{J-1}\frac{e^{-n/M_j}}{\sqrt{M_j}}.
\tag{14}
\]

By Lemma 2 and monotonicity of \(E_A\),
\[
q_n\le \sqrt{2n}+2E_A(n)\le \sqrt{2n}+2k.
\]
The contribution of \(\sqrt{2n}\) for one fixed \(n\) is, by (12),
\[
\sum_j
\frac{\sqrt{2n}}{\sqrt{M_j}}e^{-n/M_j}
\le \sqrt2\,C_1.
\]
The contribution of \(2k\) is at most
\[
2k\sum_{j\ge0}M_j^{-1/2}
\le
\frac{C_2k}{\sqrt{M_0}}.
\]
There are at most \(k\) indices with \(q_n>0\), and \(\sqrt{M_0}\ge k\). Therefore the right side of (14) is at most
\[
C_3k+C_2\frac{k^2}{\sqrt{M_0}}
\le C_4k.
\]
Hence
\[
J\le C_5k.
\tag{15}
\]

It remains to compare \(J\) with \(\log N\). If
\[
M_0>\frac{N}{8\log N},
\]
then, since \(M_0<2\max(4,k^2)\), for sufficiently large \(N\) we have
\[
k\gg\sqrt{\frac{N}{\log N}}\gg\log N,
\]
and we are done.

Otherwise,
\[
J
\ge
\log_2\!\left(\frac{N}{8M_0\log N}\right).
\]
Suppose, toward a contradiction, that \(k<c\log N\), with \(c>0\) sufficiently small. Then
\[
M_0\ll k^2+1\ll(\log N)^2,
\]
and hence, for all sufficiently large \(N\),
\[
J\ge c_6\log N.
\]
Equation (15) now gives
\[
k\ge \frac{c_6}{C_5}\log N.
\]
Choosing \(c<c_6/C_5\) is a contradiction. This proves (13). ∎

---

### 6. Why reduction modulo \(2\) cannot help

One natural attempt is to reduce the coefficients \(r_A(n)-1\) modulo a prime, thereby removing large amplitudes. Modulo \(2\), however, there is no obstruction at all.

#### Proposition 3

There exists a unique set \(A\subseteq\mathbb N\) with \(1\in A\) such that
\[
r_A(n)\equiv1\pmod2
\]
for every \(n\ge2\).

#### Proof

Let \(x_m=1_A(m)\). Set \(x_1=1\), which makes \(r_A(2)=1\).

Suppose \(x_1,\ldots,x_{m-1}\) have been chosen. In \(r_A(m+1)\), the pair \(1+m\) contributes exactly \(x_m\). Every other possible pair summing to \(m+1\) uses elements at most \(m-1\), so its contribution is already known. Thus
\[
r_A(m+1)\equiv x_m+s_m\pmod2
\]
for a determined \(s_m\in\{0,1\}\). There is a unique choice
\[
x_m\equiv1-s_m\pmod2
\]
making \(r_A(m+1)\) odd. Induction gives existence and uniqueness. ∎

The beginning of this sequence is
\[
1_A(1),1_A(2),\ldots
=
1,1,0,1,0,1,1,\ldots.
\]
At \(n=8\), for example, the three representations
\[
1+7,\qquad 2+6,\qquad 4+4
\]
show that \(r_A(8)=3\). Thus all multiplicity defects can be invisible modulo \(2\).

---

### 7. An explicit finite concentration model

The concentration obstruction is not merely hypothetical.

#### Proposition 4

For every integer \(m\ge3\), define
\[
L_m=\{1,\ldots,m\},
\qquad
H_m=\{2m,3m,\ldots,(m+1)m\},
\]
and
\[
X_m=L_m\cup H_m,
\qquad
N_m=m(m+2).
\]
Then
\[
E_{X_m}(N_m)=3m-5,
\tag{16}
\]
while
\[
r_{X_m}(N_m)=\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{17}
\]

Thus \(E_{X_m}(N_m)=O(\sqrt{N_m})\), but a single exceptional coefficient has size \(\asymp\sqrt{N_m}\).

#### Proof

Every pair is of one of the types \(L_m+L_m\), \(L_m+H_m\), or \(H_m+H_m\).

For \(L_m+L_m\), all sums lie in \([2,2m]\). For \(m\ge3\), the uniquely represented sums in \([1,2m]\) are exactly
\[
2,\quad 3,\quad 2m-1,\quad 2m.
\]
Indeed, for \(2\le n\le m+1\),
\[
r_{L_m}(n)=\left\lfloor\frac n2\right\rfloor,
\]
and for \(m+2\le n\le2m\),
\[
r_{L_m}(n)=
\left\lfloor\frac n2\right\rfloor-(n-m)+1.
\]
Hence there are
\[
2m-4
\]
exceptions in \([1,2m]\).

For a mixed pair, write the high element as \(jm\), where \(2\le j\le m+1\). Then
\[
jm+\{1,\ldots,m\}
=
[jm+1,(j+1)m].
\]
These intervals are disjoint and together cover
\[
[2m+1,(m+2)m]=[2m+1,N_m].
\]
Thus every integer in this interval has exactly one mixed representation.

Finally, every high-high sum is a multiple
\[
(j+k)m
\]
with \(2\le j\le k\le m+1\). Among sums at most \(N_m\), the possible multiples are exactly
\[
4m,5m,\ldots,(m+2)m.
\]
There are \(m-1\) of them. Each already has its unique mixed representation and acquires at least one high-high representation, so these are precisely the additional exceptions in \([2m+1,N_m]\). Therefore
\[
E_{X_m}(N_m)=(2m-4)+(m-1)=3m-5.
\]

At \(N_m=(m+2)m\), the mixed representation is
\[
m+(m+1)m.
\]
The high-high representations correspond to
\[
j+k=m+2,\qquad 2\le j\le k,
\]
of which there are
\[
\left\lfloor\frac{m+2}{2}\right\rfloor-1.
\]
Adding the mixed representation proves (17). ∎

This family is not a counterexample to either question, but it demonstrates exactly why an \(L^2\) or pointwise analytic discrepancy need not imply large support.

---

### 8. Ledger

**Proved**

1. Negative-axis positivity:
   \[
   \sum q_n\rho^n\ge \frac12F(\rho^2).
   \]
2. Multiplicity bound:
   \[
   r_A(n)\le\sqrt{2n}+2E_A(n).
   \]
3. Uniform support–multiplicity tradeoff:
   \[
   E_A(N)L_A(N)\gg\sqrt{N/\log N}.
   \]
4. Q1 for sets with \(L_A(N)=N^{o(1)}\).
5. Uniform unconditional lower bound:
   \[
   E_A(N)\gg\log N.
   \]
6. Modulo \(2\), one can force every representation count to be odd.
7. An explicit finite family with \(E(N)=3\sqrt N+O(1)\) and multiplicity \(\asymp\sqrt N\).

**Plausible but unproved**

1. If a sum has multiplicity \(t\) in a configuration with \(E_A(N)=o(N)\), the additive structure producing those \(t\) representations should force many other exceptional sums. No quantitative theorem strong enough for Q1 was obtained.
2. For odd primes \(p>N\), the truncated congruence
   \[
   F(z)^2+F(z^2)
   \equiv 2\sum_{n=1}^Nz^n+2H(z)
   \pmod{z^{N+1},p}
   \]
   may admit a sparse-polynomial lower bound. A bound of order \(N^{1/2-o(1)}\), however, is essentially the desired finite extremal theorem.
3. Multiple independent phase or character inequalities might prevent a single exceptional reservoir from absorbing all discrepancy. The negative real character supplies only one such positive inequality.

**Dead ends**

1. Plain Parseval or \(L^2\) arguments: exceptional coefficients may be of order \(\sqrt N\).
2. Reduction modulo \(2\): Proposition 3 shows it detects no defects at all.
3. A single negative-axis evaluation: it forces weighted mass \(\asymp\sqrt N\), but one coefficient can supply that mass.
4. Standard Erdős–Fuchs cumulative-error estimates: the total positive excess can be as large as \(E_A(N)\sqrt N\), far exceeding the error regime where those theorems apply.

## Self-Audit

1. **Localization from the infinite series to \(n\le N\).** This is the most delicate analytic step because later elements of \(A\) affect \(H(-\rho)\). I believe it is sound because the universal bound \(|h(n)|\le n\) gives an explicit geometric tail \(O(N^2e^{-N/M})\), and choosing \(M\le N/(8\log N)\) makes that tail negligible.

2. **The multiscale charging estimate.** The proof depends on each exceptional coefficient contributing only \(O(1)\) normalized mass through its \(\sqrt n\) part and \(O(k/\sqrt{M_0})\) through its \(2k\) part. The dyadic kernel estimate (12) and the choice \(M_0\ge k^2\) justify these bounds; no unproved regularity of \(A\) is used.

3. **The diagnosis that Route 2 is genuinely blocked at the square-root scale.** The explicit family proves that large coefficient concentration occurs, but it does not prove that every possible analytic refinement must fail. Thus the impossibility claim is methodological, not a theorem. What is rigorously established is only that the negative-axis inequality and generic \(L^p\)-to-support arguments cannot by themselves distinguish one \(\sqrt N\)-sized reservoir from \(\sqrt N\) unit defects.

## Computations To Verify

```python
from math import isqrt, sqrt, log, exp
from itertools import combinations_with_replacement

def reps(A, N):
    """Exact unordered representation counts."""
    A = sorted(a for a in set(A) if a <= N)
    r = [0] * (N + 1)
    for ii, a in enumerate(A):
        for b in A[ii:]:
            s = a + b
            if s > N:
                break
            r[s] += 1
    return r

def exceptional_data(A, N):
    r = reps(A, N)
    exc = [n for n in range(1, N + 1) if r[n] != 1]
    missing = [n for n in exc if r[n] == 0]
    multiple = [n for n in exc if r[n] >= 2]
    return {
        "E": len(exc),
        "exceptions": exc,
        "missing": missing,
        "multiple": multiple,
        "L": max([1] + r[1:]),
        "histogram": {k: sum(v == k for v in r[1:])
                      for k in set(r[1:])}
    }

def concentration_example(m):
    L = set(range(1, m + 1))
    H = {j * m for j in range(2, m + 2)}
    A = L | H
    N = m * (m + 2)
    return A, N

for m in range(3, 30):
    A, N = concentration_example(m)
    data = exceptional_data(A, N)
    r = reps(A, N)
    assert data["E"] == 3 * m - 5
    assert r[N] == (m + 2) // 2

def parity_odd_set(M):
    """
    Construct x_1,...,x_M recursively so that r(n) is odd
    for every 2 <= n <= M+1.
    """
    x = [0] * (M + 1)
    x[1] = 1
    for m in range(2, M + 1):
        n = m + 1
        s = 0
        # All pairs other than (1,m) use already chosen variables.
        for a in range(2, n // 2 + 1):
            b = n - a
            if a > b:
                break
            if b <= m - 1:
                s += x[a] * x[b]
        x[m] = (1 - s) % 2
    return {i for i in range(1, M + 1) if x[i]}

A = parity_odd_set(500)
r = reps(A, 501)
assert all(r[n] % 2 == 1 for n in range(2, 502))

def brute_D(N):
    """
    Exhaustive finite optimization. Practical only for small N.
    x_N is irrelevant for sums <= N, so search [1,N-1].
    """
    best = N + 1
    minimizers = []
    for mask in range(1 << (N - 1)):
        A = {i + 1 for i in range(N - 1) if (mask >> i) & 1}
        E = exceptional_data(A, N)["E"]
        if E < best:
            best = E
            minimizers = [A]
        elif E == best:
            minimizers.append(A)
    return best, minimizers

# Example:
# for N in range(2, 22):
#     D, mins = brute_D(N)
#     print(N, D, D / sqrt(N), len(mins))

def verify_negative_axis(A, rho, cutoff=10000):
    """
    For a finite A, verify H(-rho) =
       (F(-rho)^2 + F(rho^2))/2 + rho/(1+rho)
    by summing h through cutoff. Past 2*max(A), h=-1.
    """
    A = set(A)
    max_sum = 2 * max(A, default=0)
    K = max(cutoff, max_sum)
    r = reps(A, K)

    H_partial = sum((r[n] - 1) * ((-rho) ** n)
                    for n in range(1, K + 1))
    # For n > K, r(n)=0 because A is finite.
    tail = -sum(((-rho) ** n) for n in range(K + 1, K + 50000))
    H_numeric = H_partial + tail

    F_minus = sum(((-rho) ** a) for a in A)
    F_square_arg = sum((rho ** (2 * a)) for a in A)
    H_formula = 0.5 * (F_minus ** 2 + F_square_arg) + rho / (1 + rho)
    return H_numeric, H_formula

def support_multiplicity_ratio(A, N):
    data = exceptional_data(A, N)
    return data["E"] * data["L"] / sqrt(N / log(N))

# Search for small-scale candidates minimizing the proved tradeoff:
# for N in range(5, 23):
#     D, mins = brute_D(N)
#     ratios = [support_multiplicity_ratio(A, N) for A in mins]
#     print(N, D, min(ratios))
```

A more serious computational test should optimize not only \(E_A(N)\), but the pair
\[
\left(E_A(N),\,\max_{n\le N}r_A(n)\right),
\]
to determine whether near-minimizers necessarily have multiplicity comparable to \(\sqrt N\). That is the central unresolved concentration question.

## Route Diagnosis

The useful part of Route 2 is the order-two real character \(z=-\rho\). It converts the diagonal term \(F(\rho^2)\) into an unavoidable positive discrepancy and, after localization, proves that exceptional coefficients must carry weighted mass \(\gg\sqrt M\) at every scale. Multiscale summation turns this into \(E_A(N)\gg\log N\), while a one-scale estimate gives the support–multiplicity tradeoff.

The route is blocked because the forced mass is only of size \(\sqrt M\), exactly the maximum natural size of one concentrated representation count. Neither Parseval nor the negative-axis identity distinguishes one exceptional coefficient of size \(\sqrt M\) from \(\sqrt M\) exceptional coefficients of size \(1\). The explicit \(X_m\) family confirms that such multiplicity concentration really occurs in \(O(\sqrt N)\)-defect constructions.

Reduction modulo \(2\) is a dead end, and reduction modulo a large odd prime merely reformulates the finite extremal problem as a sparse-polynomial problem:
\[
\#\operatorname{supp}_{[1,N]}
\left(
\frac{F(z)^2+F(z^2)}2-\sum_{n=1}^Nz^n
\right).
\]
A square-root sparsity theorem for this expression would essentially be the missing finite lower bound itself.

A fresh attempt should therefore combine the analytic mass inequality with structural information about a highly represented exceptional sum. The most promising next step is a Sidon-stability or classification theorem showing that if \(r_A(s)=t\) absorbs the analytic discrepancy, then the \(t\) complementary pairs summing to \(s\) force many other exceptional sums unless they lie in a rigid direct-sum/difference-set configuration. Classifying those rigid configurations and proving that they cannot persist compatibly across scales appears more promising than further generic \(L^2\) manipulation.