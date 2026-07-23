STATUS: BLOCKED

## Result

I proved a composite-modulus-free version of Route 2 by reducing modulo a suitably chosen external prime \(p\), rather than modulo \(n\). This gives an exact universal upper bound and, for every fixed \(0<c<1\),
\[
M_c(n)\le U(c)n+o(n),
\qquad
U(c):=\min_{h\ge1}\max\left(\frac1h,c-\frac1h\right).
\]
Writing \(k=\lfloor 2/c\rfloor\), this is
\[
U(c)=
\begin{cases}
c/2,&2/c\in\mathbb Z,\\[1mm]
\min\!\left(\dfrac1k,c-\dfrac1{k+1}\right),&2/c\notin\mathbb Z.
\end{cases}
\]
Consequently, for \(c=2/k\), \(k\ge3\),
\[
\boxed{\limsup_{n\to\infty}\frac{M_c(n)}n=\frac1k=\frac c2},
\]
because odd \(n\) admit the construction of all even elements. I also prove a multi-block restricted-sumset lifting lemma, giving a family of weighted density constraints potentially stronger than the one-block bound. These results do not determine \(M_c(n)\) for general \(c\), nor the liminf even at \(c=2/k\); Route 2 remains blocked at the point where one must combine different subset cardinalities or classify sums lifting to \(2n,3n,\ldots\).

## Complete Argument

### 1. External-prime lifting lemma

The key observation is that reducing modulo \(n\) is unnecessary. A prime modulus can instead be chosen so that the only integer in the possible range of \(h\)-term sums congruent to \(n\) is \(n\) itself.

#### Lemma 1

Let \(1\le N<n\), let \(1\le h\le N\), and define
\[
L_h:=\frac{h(h+1)}2,
\qquad
U_h:=hN-\frac{h(h-1)}2.
\]
Let \(p\) be a prime satisfying
\[
p>N,\qquad n-p<L_h,\qquad U_h<n+p.
\]
If \(A\subseteq[N]\) contains no subset summing to \(n\), then
\[
|A|\le \left\lfloor\frac{p+h^2-2}{h}\right\rfloor.
\]

#### Proof

Write \(m=|A|\). If \(m<h\), then the claimed inequality is automatic, since \(p\ge2\) gives
\[
\left\lfloor\frac{p+h^2-2}{h}\right\rfloor\ge h.
\]

Suppose therefore that \(m\ge h\). Since \(p>N\), the elements of \(A\) are distinct modulo \(p\). The Dias da Silva–Hamidoune theorem gives
\[
|h^{\wedge}A|
\ge
\min\{p,hm-h^2+1\}
\]
in \(\mathbb Z/p\mathbb Z\).

If
\[
hm-h^2+1\ge p,
\]
then \(h^{\wedge}A=\mathbb Z/p\mathbb Z\). In particular, there are distinct
\[
a_1,\dots,a_h\in A
\]
such that
\[
a_1+\cdots+a_h\equiv n\pmod p.
\]
Any \(h\) distinct elements of \([N]\) have sum \(s\) satisfying
\[
L_h\le s\le U_h.
\]
The hypotheses on \(p\) say
\[
n-p<L_h\le s\le U_h<n+p.
\]
Since \(s\equiv n\pmod p\), the only possibility in this interval is \(s=n\). That contradicts admissibility.

Hence
\[
hm-h^2+1\le p-1,
\]
so
\[
hm\le p+h^2-2,
\]
which proves the assertion. ∎

The standard prime-modulus argument from the brief is the special case \(p=n\) when \(n\) is prime and \(U_h<2n\).

---

### 2. An exact upper bound for every \(N<n\)

Define
\[
Q_h(N,n):=
\max\left\{
N,\,
n-\frac{h(h+1)}2,\,
hN-\frac{h(h-1)}2-n
\right\},
\]
and let \(p_h(N,n)\) be the least prime strictly greater than \(Q_h(N,n)\).

Then \(p_h>N\), and
\[
n-p_h<L_h,\qquad U_h<n+p_h.
\]
Lemma 1 therefore gives the following exact bound.

#### Corollary 2

For every \(1\le N<n\),
\[
\boxed{
M(N,n)\le
\min_{1\le h\le N}
\min\left\{
N,\,
\left\lfloor
\frac{p_h(N,n)+h^2-2}{h}
\right\rfloor
\right\}.
}
\]

This bound is valid for composite and prime \(n\), with no stabilizer analysis in \(\mathbb Z/n\mathbb Z\).

---

### 3. Asymptotic optimization

Fix \(0<c<1\) and set \(N=\lfloor cn\rfloor\). For fixed \(h\),
\[
\frac{Q_h(N,n)}n
=
\max\{c,1,hc-1\}+o(1)
=
\max\{1,hc-1\}+o(1),
\]
because \(c<1\).

The prime number theorem implies that the least prime greater than \(x\) is \(x+o(x)\). Indeed, for every fixed \(\varepsilon>0\),
\[
\pi((1+\varepsilon)x)-\pi(x)>0
\]
for all sufficiently large \(x\). Thus
\[
\frac{p_h(N,n)}n
=
\max\{1,hc-1\}+o(1).
\]
Corollary 2 yields
\[
\frac{M_c(n)}n
\le
\frac{\max\{1,hc-1\}}h+o(1)
=
\max\left\{\frac1h,c-\frac1h\right\}+o(1).
\]
Since this holds for every fixed positive integer \(h\),
\[
M_c(n)\le U(c)n+o(n),
\]
where
\[
U(c):=
\min_{h\ge1}
\max\left\{\frac1h,c-\frac1h\right\}.
\]

To evaluate this minimum, put \(r=2/c\). If \(h\le r\), then \(hc\le2\), so
\[
\max\left\{\frac1h,c-\frac1h\right\}=\frac1h,
\]
which decreases with \(h\). If \(h\ge r\), then it equals
\[
c-\frac1h,
\]
which increases with \(h\). Hence only the integers immediately adjacent to \(2/c\) matter.

#### Corollary 3

For \(0<c<1\), let \(k=\lfloor2/c\rfloor\). Then
\[
\boxed{
U(c)=
\begin{cases}
\dfrac c2,&2/c\in\mathbb Z,\\[2mm]
\min\!\left\{\dfrac1k,\ c-\dfrac1{k+1}\right\},
&2/c\notin\mathbb Z.
\end{cases}}
\]

For example,
\[
U(c)=
\begin{cases}
c-\frac13,&\frac23<c\le\frac56,\\[1mm]
\frac12,&\frac56\le c<1,
\end{cases}
\]
and
\[
U(c)=
\begin{cases}
c-\frac14,&\frac12<c\le\frac7{12},\\[1mm]
\frac13,&\frac7{12}\le c\le\frac23.
\end{cases}
\]

Notice that
\[
U(c)\ge \frac c2,
\]
because for every \(h\),
\[
\max\left\{\frac1h,c-\frac1h\right\}\ge\frac c2.
\]
Equality is possible precisely when \(1/h=c/2\), i.e. when \(c=2/h\).

---

### 4. Exact determination of a family of limsups

Suppose
\[
c=\frac2k
\]
for an integer \(k\ge3\). Corollary 3 gives
\[
M_c(n)\le \frac nk+o(n)
\]
through all positive integers \(n\).

For odd \(n\), let
\[
A=2\mathbb Z\cap[\lfloor cn\rfloor].
\]
Every subset sum of \(A\) is even, so no subset sum equals the odd integer \(n\). Moreover,
\[
|A|
=
\left\lfloor\frac{\lfloor cn\rfloor}{2}\right\rfloor
=
\frac c2n+O(1)
=
\frac nk+O(1).
\]
It follows that, as \(n\to\infty\) through odd integers,
\[
\frac{M_c(n)}n\longrightarrow\frac1k.
\]
Together with the all-\(n\) upper bound, this proves:

#### Corollary 4

For every integer \(k\ge3\),
\[
\boxed{
\limsup_{n\to\infty}
\frac{M_{2/k}(n)}n
=
\frac1k.
}
\]

This does not determine the liminf. In particular, it does not prove arithmetic irregularity: the even and highly divisible subsequences might still have the same limit.

For arbitrary \(c\), the same parity construction gives
\[
\frac c2
\le
\limsup_{n\to\infty}\frac{M_c(n)}n
\le U(c).
\]

---

### 5. A multi-block restricted-sumset lemma

The one-block argument uses the same number \(h\) of summands from all of \(A\). A stronger form permits prescribed numbers of summands from disjoint portions of \(A\).

#### Lemma 5

Let \(J_i=[\ell_i,u_i]\cap\mathbb Z\), \(1\le i\le r\), be pairwise disjoint intervals contained in \([N]\). Let
\[
B_i\subseteq J_i,\qquad m_i:=|B_i|,
\]
and choose integers \(1\le h_i\le m_i\).

Set
\[
S_-:=
\sum_{i=1}^r
\left(h_i\ell_i+\binom{h_i}{2}\right),
\qquad
S_+:=
\sum_{i=1}^r
\left(h_i u_i-\binom{h_i}{2}\right).
\]
Let \(p\) be a prime satisfying
\[
p>N,\qquad n-p<S_-,\qquad S_+<n+p.
\]
If \(\bigcup_iB_i\) has no subset summing to \(n\), then
\[
\boxed{
\sum_{i=1}^r h_i m_i
\le
p+\sum_{i=1}^r h_i^2-2.
}
\]

#### Proof

Work in \(\mathbb Z/p\mathbb Z\). Put
\[
C_i:=h_i^{\wedge}B_i.
\]
The Dias da Silva–Hamidoune theorem gives
\[
|C_i|
\ge
\min\{p,h_i m_i-h_i^2+1\}.
\]

If some \(C_i\) is all of \(\mathbb Z/p\mathbb Z\), then
\[
C_1+\cdots+C_r=\mathbb Z/p\mathbb Z,
\]
since every other \(C_j\) is nonempty. Otherwise, repeated application of Cauchy–Davenport gives
\[
|C_1+\cdots+C_r|
\ge
\min\left\{
p,\,
\sum_{i=1}^r|C_i|-(r-1)
\right\}
\]
and hence
\[
|C_1+\cdots+C_r|
\ge
\min\left\{
p,\,
\sum_{i=1}^r h_i m_i-\sum_{i=1}^r h_i^2+1
\right\}.
\]

Consequently, if
\[
\sum_i h_i m_i-\sum_i h_i^2+1\ge p,
\]
the combined restricted sumset is all of \(\mathbb Z/p\mathbb Z\). We may then choose \(h_i\) distinct elements from each \(B_i\) whose total sum \(s\) satisfies
\[
s\equiv n\pmod p.
\]

Because the intervals are disjoint, all chosen elements are globally distinct. Their total satisfies
\[
S_-\le s\le S_+.
\]
The conditions on \(p\) imply
\[
n-p<S_-\le s\le S_+<n+p.
\]
Thus \(s=n\), contradicting admissibility.

Therefore
\[
\sum_i h_i m_i-\sum_i h_i^2+1\le p-1,
\]
which is the asserted inequality. ∎

For intervals of the form
\[
J_i=[\alpha_i n,\beta_i n]+O(1),
\]
the least admissible prime has asymptotic size
\[
\max\left\{
c,\,
1-\sum_i h_i\alpha_i,\,
\sum_i h_i\beta_i-1
\right\}n+o(n).
\]
Thus Lemma 5 produces explicit weighted linear constraints on the densities of an admissible set in any fixed interval partition. This is the strongest rigorous extension of the one-cardinality argument obtained here.

---

### 6. Why reduction modulo \(n\) itself is insufficient

Two concrete obstructions were checked.

First, the prime Dias da Silva–Hamidoune inequality does not extend unchanged to composite cyclic groups. In \(\mathbb Z/8\mathbb Z\), take
\[
A=\{1,3,5,7\}.
\]
Then
\[
2^{\wedge}A=\{0,2,4,6\},
\]
so
\[
|2^{\wedge}A|=4
<
2|A|-2^2+1=5.
\]
This is a genuine subgroup/coset stabilizer obstruction.

Second, even for prime \(n\), a modular zero need not lift to \(n\) once the sum range reaches \(2n\). Let
\[
n=11,\qquad A=\{2,4,6,8,10\}.
\]
No subset of \(A\) sums to \(11\), since every subset sum is even, but
\[
4+8+10=22\equiv0\pmod{11}.
\]
Thus merely proving \(0\in h^{\wedge}A\pmod n\) is inadequate without a lifting interval.

The external-prime lemma removes both defects, but its resulting upper bound does not generally match known constructions.

## Self-Audit

1. **The proof invokes Dias da Silva–Hamidoune and Cauchy–Davenport as established theorems.**  
   These are not reproved here. They are standard results, and Dias da Silva–Hamidoune is explicitly included among the permitted context in the brief. Every hypothesis—prime modulus, injectivity modulo \(p\), and distinct summands—is checked.

2. **The passage from the exact bound to \(p_h=(1+o(1))Q_h\) uses the prime number theorem.**  
   This is the only analytic number-theoretic input. It is valid because \(Q_h\asymp_c n\) for each fixed \(h\), and the PNT guarantees a prime in \((x,(1+\varepsilon)x)\) for every fixed \(\varepsilon>0\) and sufficiently large \(x\). The exact bound itself does not depend on any asymptotic prime-gap estimate.

3. **The limsup result at \(c=2/k\) is deliberately limited to a limsup.**  
   The lower bound is supplied only on the infinite odd subsequence. Nothing here proves the same lower bound for even or highly divisible \(n\). The limsup conclusion nevertheless follows rigorously from the all-\(n\) upper bound and the odd-\(n\) construction.

## Computations To Verify

```python
from itertools import combinations
from math import isqrt, floor

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d += 2
    return True

def next_prime_strict(q):
    x = max(2, q + 1)
    while not is_prime(x):
        x += 1
    return x

def valid(A, n):
    """Exact distinct-subset-sum test, truncated at n."""
    R = 1
    mask = (1 << (n + 1)) - 1
    for a in A:
        R |= (R << a) & mask
    return ((R >> n) & 1) == 0

def external_bound(N, n, h):
    """Corollary 2."""
    L = h * (h + 1) // 2
    U = h * N - h * (h - 1) // 2
    Q = max(N, n - L, U - n)
    p = next_prime_strict(Q)
    return min(N, (p + h * h - 2) // h)

def best_external_bound(N, n):
    return min(external_bound(N, n, h) for h in range(1, N + 1))

def exact_M(N, n):
    """
    Exact branch-and-bound optimizer.
    Intended for N up to roughly 30-40 depending on the instance.
    """
    order = list(range(N, 0, -1))
    target = 1 << n
    mask = (1 << (n + 1)) - 1

    best = 0
    best_set = []
    chosen = []
    memo = {}

    def dfs(i, R, count):
        nonlocal best, best_set

        if count > best:
            best = count
            best_set = chosen.copy()

        if i == len(order):
            return
        if count + len(order) - i <= best:
            return

        key = (i, R)
        if memo.get(key, -1) >= count:
            return
        memo[key] = count

        a = order[i]
        newR = R | ((R << a) & mask)

        if (newR & target) == 0:
            chosen.append(a)
            dfs(i + 1, newR, count + 1)
            chosen.pop()

        dfs(i + 1, R, count)

    dfs(0, 1, 0)
    return best, sorted(best_set)

# Verify the exact external-prime bound on small instances.
for n in range(3, 23):
    for N in range(1, n):
        m, A = exact_M(N, n)
        b = best_external_bound(N, n)
        assert m <= b, (N, n, m, A, b)

def restricted_sums_mod(A, h, modulus):
    return {
        sum(S) % modulus
        for S in combinations(A, h)
    }

# Composite-modulus counterexample to the prime DdS lower bound.
A8 = [1, 3, 5, 7]
R8 = restricted_sums_mod(A8, 2, 8)
assert R8 == {0, 2, 4, 6}
assert len(R8) == 4
assert min(8, 2 * len(A8) - 2**2 + 1) == 5

# Modular zero lifting to 2n rather than n.
A11 = [2, 4, 6, 8, 10]
assert valid(A11, 11)
assert 0 in restricted_sums_mod(A11, 3, 11)
assert 4 + 8 + 10 == 22

def U_of_c(c):
    r = 2.0 / c
    k = floor(r)
    if abs(r - round(r)) < 1e-12:
        return c / 2.0
    return min(1.0 / k, c - 1.0 / (k + 1))

# Examine convergence at resonant c=2/k.
for k in range(3, 9):
    c = 2.0 / k
    for n in range(21, 60, 2):  # odd n
        N = floor(c * n)
        parity_lower = N // 2
        bound = best_external_bound(N, n)
        assert parity_lower <= bound
        # For smaller N one may also call exact_M(N,n).
```

A direct finite test of Lemma 5 can be implemented as follows:

```python
def multiblock_constraint(A, N, n, intervals, hs):
    """
    intervals = [(lo_i, hi_i), ...], pairwise disjoint.
    Returns True if Lemma 5's conclusion holds whenever applicable.
    """
    blocks = [
        [a for a in A if lo <= a <= hi]
        for lo, hi in intervals
    ]
    if any(len(B) < h for B, h in zip(blocks, hs)):
        return True  # lemma not invoked

    Smin = sum(
        h * lo + h * (h - 1) // 2
        for (lo, hi), h in zip(intervals, hs)
    )
    Smax = sum(
        h * hi - h * (h - 1) // 2
        for (lo, hi), h in zip(intervals, hs)
    )
    Q = max(N, n - Smin, Smax - n)
    p = next_prime_strict(Q)

    lhs = sum(h * len(B) for h, B in zip(hs, blocks))
    rhs = p + sum(h * h for h in hs) - 2
    return lhs <= rhs

# Exhaustive small verification for selected block patterns.
for n in range(8, 18):
    for N in range(4, n):
        for maskA in range(1 << N):
            A = [a + 1 for a in range(N) if (maskA >> a) & 1]
            if not valid(A, n):
                continue
            cut = N // 2
            intervals = [(1, cut), (cut + 1, N)]
            for hs in [(1, 1), (1, 2), (2, 1), (2, 2)]:
                assert multiblock_constraint(
                    A, N, n, intervals, hs
                )
```

The most useful next computation is to generate all Lemma 5 inequalities for interval partitions with rational endpoints of denominator at most \(20\), solve the resulting linear program for density profiles, and compare its optimum against exact ILP values of \(M(N,n)/n\).

## Route Diagnosis

### What worked

- Passing to an external prime completely removes composite stabilizers.
- Choosing the prime according to the entire possible integer range of \(h\)-term sums also handles lifts to \(2n,3n,\ldots\).
- The resulting exact upper bound is uniform in \(n\).
- Its asymptotic optimization determines the limsup for the infinite family \(c=2/k\).
- The multi-block lemma extends Route 2 to weighted interval-density constraints and is a concrete framework for further finite-dimensional optimization.

### Precise block

The one-block method requires a prime of asymptotic size at least
\[
\max\{n,hN-n\}.
\]
Dias da Silva–Hamidoune then forces the threshold
\[
|A|\lesssim
\max\left\{\frac nh,N-\frac nh\right\}.
\]
Optimizing over integral \(h\) gives \(U(c)\). Except when \(2/c\) is an integer, there is a genuine cardinality-rounding gap:
\[
U(c)>\frac c2.
\]
No known construction in the brief generally matches \(U(c)\), and the modular theorem alone gives no mechanism to combine the two adjacent cardinalities \(\lfloor2/c\rfloor\) and \(\lceil2/c\rceil\).

Even at the resonant values \(c=2/k\), the matching construction currently applies only when \(n\) is odd. Determining the liminf would require controlling highly divisible \(n\), where the parity construction disappears.

### Ledger

**Proved**

1. External-prime lifting lemma.
2. Exact upper bound via the least prime above \(Q_h(N,n)\).
3. Universal asymptotic bound \(M_c(n)\le U(c)n+o(n)\).
4. Exact formula for \(U(c)\).
5. \(\limsup M_{2/k}(n)/n=1/k\) for every \(k\ge3\).
6. Multi-block restricted-sumset lifting lemma.

**Plausible but unproved**

1. Combining adjacent subset cardinalities may improve \(U(c)\), possibly down to \(c/2\) on odd or prime subsequences.
2. A sufficiently rich collection of multi-block inequalities, together with the pair constraints, may characterize the leading extremal density.
3. Extremizers on highly divisible \(n\) may require periodic or mixed interval-periodic structure not visible to a single fixed-cardinality sumset.

**Dead ends**

1. Direct transplantation of the prime restricted-sumset lower bound to composite \(\mathbb Z/n\mathbb Z\): false, as shown in \(\mathbb Z/8\mathbb Z\).
2. Treating a zero sum modulo \(n\) as a representation of \(n\) when \(hN\ge2n\): false, as shown by the even set for \(n=11\).
3. Optimizing only over a single cardinality and a single external prime: rigorously stops at \(U(c)\), which does not match available lower bounds except at special resonant limsups.

A fresh attempt should first computationally optimize the multi-block inequalities and compare them with exact extremizers. If they remain separated, Route 2 by itself is insufficient; the next step should combine it with hypergraph pair constraints or an inverse theorem distinguishing representations of \(n\) from representations of \(2n\).