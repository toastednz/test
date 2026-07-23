STATUS: BLOCKED

## Result

I constructed an explicit low-lcm smooth reservoir with genuine entropy surplus: for all sufficiently large \(B\), there are \(\gg B\log\log B\) pairwise nonadjacent dimers whose endpoints divide \(L_B^2\), whose total reciprocal weight can be made \(<1/20\), and for which every central run-count layer contains more than \(L_B^2\) admissible supports. After adjoining a separated “mass band,” the total available weight lies strictly between \(1\) and \(2\), so the original problem becomes an exact zero-residue problem modulo \(L_B^2\). This successfully removes the cardinality/lcm obstruction identified in Round 1. However, the high-entropy reservoir by itself has no nonempty zero-residue subset—because its total weight is \(<1\)—so entropy alone provably does not force the target residue. I derived an exact count-refined Fourier criterion and identified the remaining obstruction: order-\(p\) characters see only dimers attaining maximal \(p\)-valuation, and no sufficiently strong uniform mixing of these sparse top layers has been proved. Thus Route 3 is blocked precisely at a genuinely \(p\)-adic Fourier-mixing theorem, not at entropy generation.

## Complete Argument

### 1. A two-parameter source of smooth consecutive pairs

For integers \(a\ge 2\) and \(t\ge1\), define
\[
N(a,t):=(a+1)(at-1).
\]
Then
\[
N(a,t)+1=a((a+1)t-1),
\]
because
\[
a((a+1)t-1)-(a+1)(at-1)=1.
\tag{1}
\]

Thus \([N(a,t),N(a,t)+1]\) is a dimer whose two endpoints each factor into two controlled factors:
\[
N(a,t)=(a+1)(at-1),\qquad
N(a,t)+1=a((a+1)t-1).
\tag{2}
\]

If all four factors on the right are at most \(B\), then both endpoints divide
\[
M_B:=L_B^2,\qquad L_B=\operatorname{lcm}(1,\dots,B).
\]
Indeed, each factor divides \(L_B\), and a product of two divisors of \(L_B\) divides \(L_B^2\).

The square dimers \([a^2-1,a^2]\) are the special case \(t=1\). Allowing \(t\) to vary produces much more entropy.

---

### 2. Construction at one scale

Fix a sufficiently large constant \(A_0\). Let \(A\ge A_0\), with
\[
A\le B^{1/3}.
\]
For each prime
\[
A\le p\le 2A
\]
and each integer
\[
\left\lceil\frac{B}{4(p+1)}\right\rceil
\le t\le
\left\lfloor\frac{B}{2(p+1)}\right\rfloor,
\tag{3}
\]
form the dimer beginning at
\[
N(p,t)=(p+1)(pt-1).
\]

All four factors in (2) are at most \(B\). Specifically,
\[
p,p+1\le 2B^{1/3}+1<B
\]
for large \(B\), while (3) gives
\[
pt-1<\frac B2,\qquad (p+1)t-1\le\frac B2.
\]
Hence both endpoints divide \(M_B\).

Moreover, for large \(B\),
\[
\frac{AB}{5}\le N(p,t)\le AB.
\tag{4}
\]
The upper bound follows from
\[
N(p,t)<p(p+1)\frac{B}{2(p+1)}=\frac{pB}{2}\le AB.
\]
For the lower bound,
\[
N(p,t)\ge (p+1)\left(\frac{pB}{4(p+1)}-1\right)
=\frac{pB}{4}-(p+1)\ge\frac{AB}{5}
\]
once \(B\) is large.

Let \(P_A\) denote the number of parameter pairs \((p,t)\) at scale \(A\). By the prime number theorem in dyadic intervals,
\[
\#\{p\in[A,2A]:p\text{ prime}\}\asymp \frac{A}{\log A}.
\]
For each such prime, the interval (3) contains \(\gg B/A\) integers. Therefore
\[
P_A\gg \frac{B}{\log A}.
\tag{5}
\]

Different parameter pairs can yield the same starting point. We now bound those collisions.

---

### 3. Collision bound

For fixed prime \(p\),
\[
N(p,t)=p(p+1)t-(p+1),
\]
so distinct \(t\)'s give distinct starts, and every such start satisfies
\[
N\equiv -1\pmod p,\qquad N\equiv0\pmod{p+1}.
\tag{6}
\]

Consider distinct odd primes \(p,q\in[A,2A]\). If \(p\mid q+1\), then a common start would have to satisfy both
\[
N\equiv-1\pmod p
\]
from the \(p\)-family and
\[
N\equiv0\pmod p
\]
from the \(q\)-family, which is impossible. The analogous statement holds if \(q\mid p+1\).

Otherwise, the simultaneous congruences have period
\[
\operatorname{lcm}\bigl(p(p+1),q(q+1)\bigr)
=pq\,\operatorname{lcm}(p+1,q+1)\ge A^3.
\tag{7}
\]
All starts at scale \(A\) lie in an interval of length at most \(AB\), by (4). Hence two distinct prime families have at most
\[
\frac{AB}{A^3}+1=\frac{B}{A^2}+1
\tag{8}
\]
common starts.

The standard upper bound
\[
\#\{p\in[A,2A]\}\ll\frac{A}{\log A}
\]
therefore gives at most
\[
\ll \frac{A^2}{(\log A)^2}
\left(\frac{B}{A^2}+1\right)
\ll \frac{B+A^2}{(\log A)^2}
\tag{9}
\]
unordered colliding parameter pairs.

Let \(U_A\) be the number of distinct starts. If a start has multiplicity \(m\), then it contributes \(m-1\) to \(P_A-U_A\) and \(\binom m2\ge m-1\) collision pairs. Thus
\[
U_A\ge P_A-\#\{\text{collision pairs}\}.
\]
Combining (5) and (9), and using \(A^2\le B^{2/3}\), gives
\[
U_A\gg\frac{B}{\log A}
\tag{10}
\]
provided \(A_0\) and then \(B\) are sufficiently large.

From these distinct starts, select pairwise \(3\)-separated starts greedily. Choosing the smallest remaining start deletes at most that start and the next two possible integer starts. Hence at least one-third survive. We obtain
\[
R_A\gg\frac{B}{\log A}
\tag{11}
\]
pairwise nonadjacent dimers at scale \(A\).

---

### 4. Combining geometrically separated scales

Take
\[
A_j=A_0\,8^j
\]
over all \(j\ge0\) for which \(A_j\le B^{1/3}\).

By (4), the starts from scale \(A_j\) lie in
\[
\left[\frac{A_jB}{5},A_jB\right].
\]
The next scale begins above
\[
\frac{8A_jB}{5}>A_jB+2,
\]
so configurations from distinct scales are automatically nonadjacent.

Let \(\mathcal H_B\) be the union of the selected dimers over these scales. Then
\[
R_B:=|\mathcal H_B|
\gg B\sum_{A_j\le B^{1/3}}\frac1{\log A_j}.
\]
Since \(\log A_j=\log A_0+j\log8\),
\[
\sum_{A_j\le B^{1/3}}\frac1{\log A_j}
\gg \log\log B.
\]
Consequently,
\[
\boxed{R_B\gg B\log\log B.}
\tag{12}
\]

Every endpoint of every dimer in \(\mathcal H_B\) divides \(L_B^2\).

---

### 5. The remote reservoir can have arbitrarily small total weight

At scale \(A\), every start satisfies \(N\ge AB/5\), so
\[
d(N)=\frac1N+\frac1{N+1}<\frac2N\le\frac{10}{AB}.
\tag{13}
\]

There are trivially at most
\[
A\left(\frac{B}{4A}+2\right)\le\frac B3
\]
parameter pairs at scale \(A\), for sufficiently large \(B\). Therefore the reciprocal weight at that scale is at most
\[
\frac{10}{3A}.
\]
Summing over \(A_j=A_0 8^j\),
\[
W(\mathcal H_B)
\le \frac{10}{3}\sum_{j\ge0}\frac1{A_0 8^j}
=\frac{80}{21A_0}.
\tag{14}
\]

Choosing \(A_0\) sufficiently large gives, for example,
\[
\boxed{W(\mathcal H_B)<\frac1{20}.}
\tag{15}
\]

Thus we simultaneously have:

- \(R_B\gg B\log\log B\) independent legal dimers;
- all endpoints divide \(L_B^2\);
- their total reciprocal weight is \(<1/20\).

---

### 6. Genuine entropy surplus

Every subset of \(\mathcal H_B\) is an admissible support whose run count equals its number of selected dimers.

Since
\[
\log L_B=\psi(B)\sim B,
\]
we have
\[
\log M_B=2\log L_B=(2+o(1))B.
\tag{16}
\]
On the other hand,
\[
\log 2^{R_B}\gg B\log\log B.
\]
Therefore
\[
\boxed{2^{R_B}>M_B}
\tag{17}
\]
for all sufficiently large \(B\).

More strongly, fix any \(\eta\in(0,1/2)\). Uniformly for
\[
\eta R_B\le k\le(1-\eta)R_B,
\]
Stirling's formula gives
\[
\log\binom{R_B}{k}\gg_\eta R_B\gg B\log\log B,
\]
and hence
\[
\boxed{\binom{R_B}{k}>M_B}
\tag{18}
\]
for every central count layer.

This is the entropy/lcm inequality Route 3 sought. It is substantially stronger than the square-dimer family, for which the entropy rate was too small.

However, (15) also proves that no nonempty subset of \(\mathcal H_B\) can have integer reciprocal sum. Therefore none has residue zero modulo \(M_B\). Thus (17) and (18) do not by themselves approach the target residue: they only force many exact collisions between nonzero residues.

This is a rigorous counterexample to the inference “entropy greater than the modulus forces a nonempty zero-residue support.”

---

### 7. Adding enough real mass while retaining entropy

The case \(a=2\) in (1) gives
\[
N(2,t)=3(2t-1)=6t-3,\qquad
N(2,t)+1=2(3t-1)=6t-2.
\tag{19}
\]
These starts differ by \(6\), so the associated dimers are pairwise nonadjacent.

Let
\[
\frac{B}{400}\le t\le\frac{B}{4}.
\]
Both factors \(2t-1\) and \(3t-1\) are at most \(B\), so these endpoints also divide \(L_B^2\).

Call this mass band \(\mathcal M_B\). Its weight satisfies
\[
\begin{aligned}
W(\mathcal M_B)
&=\sum_{B/400\le t\le B/4}
\left(\frac1{6t-3}+\frac1{6t-2}\right)\\
&=\frac13\sum_{B/400\le t\le B/4}\frac1t+O(B^{-1})\\
&=\frac{\log100}{3}+O(B^{-1}).
\end{aligned}
\tag{20}
\]
Since
\[
\frac{\log100}{3}=1.535056\ldots,
\]
we have, for large \(B\),
\[
1.52<W(\mathcal M_B)<1.55.
\tag{21}
\]

The mass-band starts are at most \(3B/2+O(1)\), while the high reservoir begins beyond \(A_0B/5\). Taking \(A_0>10\) makes the two families nonadjacent.

Set
\[
\mathcal C_B:=\mathcal M_B\cup\mathcal H_B.
\]
By (15) and (21),
\[
\boxed{1<W(\mathcal C_B)<2.}
\tag{22}
\]

The family \(\mathcal C_B\) still contains \(\gg B\log\log B\) independent legal dimers and has common denominator \(M_B=L_B^2\).

For each dimer \(I=[n,n+1]\in\mathcal C_B\), define the integer coin
\[
c_I:=M_B\left(\frac1n+\frac1{n+1}\right).
\tag{23}
\]

For every nonempty subfamily \(\mathcal A\subseteq\mathcal C_B\),
\[
\sum_{I\in\mathcal A}c_I\equiv0\pmod{M_B}
\]
implies
\[
\sum_{I\in\mathcal A}w(I)\in\mathbb Z.
\]
By positivity and (22), this integer lies strictly between \(0\) and \(2\). Hence it equals \(1\).

Therefore:

> **Exact modular reduction.**  
> A nonempty zero-sum subset of the coins \(c_I\) modulo \(M_B\) is exactly an admissible representation of \(1\).

This realizes the proposed Route-3 architecture completely except for the zero-residue mixing theorem.

---

### 8. Exact Fourier formulation, including run count

Let \(\mathcal C_B=\{I_1,\dots,I_r\}\), and write \(c_i=c_{I_i}\). Let
\[
e_D(x):=\exp(2\pi i x/D).
\]

The number \(Z_k\) of \(k\)-element subfamilies satisfying
\[
\sum c_i\equiv0\pmod D
\]
is exactly
\[
\boxed{
Z_k=\frac1D\sum_{h=0}^{D-1}
[z^k]\prod_{i=1}^r\left(1+z\,e_D(hc_i)\right).
}
\tag{24}
\]
Here one can take \(D=M_B\), or preferably the actual lcm of the reduced dimer denominators.

The \(h=0\) contribution is
\[
\frac1D\binom rk.
\]
Thus (18) makes the expected main term large, but the nontrivial characters must still be controlled.

A useful sufficient criterion follows. Define
\[
S_h:=\sum_{i=1}^r
\sin^2\left(\frac{\pi h c_i}{D}\right).
\tag{25}
\]
Fix \(\eta\in(0,1/2)\), and suppose
\[
\eta r\le k\le(1-\eta)r.
\]
Put
\[
\rho=\frac{k}{r-k}.
\]
Cauchy's coefficient estimate and
\[
|1+\rho e^{2\pi ix}|
\le (1+\rho)
\exp\left(
-\frac{2\rho}{(1+\rho)^2}\sin^2(\pi x)
\right)
\]
give
\[
\left|
[z^k]\prod_i(1+z e_D(hc_i))
\right|
\le C_\eta\sqrt r\binom rk
\exp(-\lambda_\eta S_h)
\tag{26}
\]
for constants \(C_\eta,\lambda_\eta>0\).

Consequently,
\[
\boxed{
C_\eta\sqrt r
\sum_{h=1}^{D-1}e^{-\lambda_\eta S_h}<1
\quad\Longrightarrow\quad
Z_k>0.
}
\tag{27}
\]

In particular, a uniform estimate
\[
S_h\gg_\eta \log D+\log r
\qquad(1\le h<D)
\tag{28}
\]
would suffice.

No estimate of this strength has been proved for the constructed reservoir.

---

### 9. The precise \(p\)-adic obstruction to uniform Fourier mixing

Let \(D\) be the actual lcm of the reduced dimer denominators
\[
q_i=n_i(n_i+1),
\]
and let
\[
c_i=D\frac{2n_i+1}{n_i(n_i+1)}.
\]
For a prime \(p\), put
\[
a=v_p(D)=\max_i v_p(q_i).
\]

Because \(p\) divides at most one of \(n_i,n_i+1\), it never divides \(2n_i+1\) when it divides \(q_i\). Therefore
\[
p\nmid c_i
\quad\Longleftrightarrow\quad
v_p(q_i)=a.
\tag{29}
\]
All dimers below the maximal \(p\)-valuation layer contribute \(0\) modulo \(p\).

For the order-\(p\) character \(h=D/p\),
\[
e_D(hc_i)=e_p(c_i).
\]
Thus it sees precisely the dimers attaining maximal \(p\)-valuation. If their number is \(s_p\), then
\[
S_{D/p}\le s_p.
\tag{30}
\]

Hence the simple uniform criterion (28) would require
\[
s_p\gg\log D
\]
for every prime divisor \(p\) of \(D\). The construction supplies no such top-layer multiplicity. In natural lcm systems, maximal prime-power valuations are often attained only a few times.

This is the exact blocked point: the reservoir has more than enough entropy globally, but its entropy is not known to survive the successive maximal-valuation filters seen by low-order characters.

## Self-Audit

1. **The collision estimate uses asymptotic prime counts in every dyadic interval.**  
   This makes the threshold \(B_0\) ineffective as presented. The assertion itself is standard: the prime number theorem gives both upper and lower bounds \(\asymp A/\log A\), uniformly for all sufficiently large \(A\). No unproved number-theoretic hypothesis is used.

2. **The most delicate proved step is the lower bound on distinct starts.**  
   A hidden high-multiplicity collision could invalidate the entropy estimate. The proof avoids assuming bounded multiplicity: it counts unordered colliding parameter pairs and uses \(m-1\le\binom m2\) in each fiber. The period bound \(A^3\) follows directly from the congruences (6), with cross-divisibility cases explicitly excluded as inconsistent.

3. **The modular reformulation does not establish a zero-residue subset.**  
   It only proves that such a subset would be an exact solution. I believe the reformulation is exact because every endpoint divides \(L_B^2\), and the total available reciprocal weight is strictly between \(1\) and \(2\). The missing Fourier-mixing assertion is not being treated as proved; it is the reason for the BLOCKED status.

## Computations To Verify

The following Python constructs the determinant dimers, checks geometry and smooth divisibility, computes exact weights, and diagnoses maximal \(p\)-valuation layers.

```python
from fractions import Fraction
from math import gcd, lcm, log, sin, pi
from collections import defaultdict

def ceildiv(a, b):
    return -(-a // b)

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    p = 2
    while p * p <= n:
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
        p += 1
    return [i for i in range(2, n + 1) if sieve[i]]

def vp(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a

def greedy_separated(starts):
    """Select starts differing by at least 3."""
    out = []
    for n in sorted(set(starts)):
        if not out or n >= out[-1] + 3:
            out.append(n)
    return out

def build_high_family(B, A0=100):
    primes = primes_upto(2 * int(B ** (1/3)) + 100)
    high = []
    A = A0

    # A <= B^(1/3), with a little integer safety.
    while A ** 3 <= B:
        starts = []
        for p in primes:
            if p < A:
                continue
            if p > 2 * A:
                break
            lo = ceildiv(B, 4 * (p + 1))
            hi = B // (2 * (p + 1))
            for t in range(max(1, lo), hi + 1):
                n = (p + 1) * (p * t - 1)
                assert n + 1 == p * ((p + 1) * t - 1)
                assert p <= B and p + 1 <= B
                assert p * t - 1 <= B
                assert (p + 1) * t - 1 <= B
                starts.append(n)

        high.extend(greedy_separated(starts))
        A *= 8

    # Scales should already be separated, but canonicalize globally.
    return greedy_separated(high)

def build_mass_family(B):
    lo = ceildiv(B, 400)
    hi = B // 4
    starts = [6*t - 3 for t in range(lo, hi + 1)]
    return starts  # Starts differ by 6.

def exact_weight(starts):
    return sum(
        (Fraction(1, n) + Fraction(1, n + 1) for n in starts),
        Fraction(0, 1)
    )

def lcm_1_to_B(B):
    L = 1
    for n in range(1, B + 1):
        L = lcm(L, n)
    return L

def actual_dimer_lcm(starts):
    D = 1
    for n in starts:
        D = lcm(D, n * (n + 1))
    return D

def verify_family(B, A0=100):
    high = build_high_family(B, A0)
    mass = build_mass_family(B)
    starts = sorted(mass + high)

    # Geometry
    for n in starts:
        assert n >= 1
    for x, y in zip(starts, starts[1:]):
        assert y >= x + 3, (x, y)

    # Common denominator
    L = lcm_1_to_B(B)
    M = L * L
    for n in starts:
        assert M % n == 0
        assert M % (n + 1) == 0

    wh = exact_weight(high)
    wm = exact_weight(mass)
    wt = wh + wm

    print("B =", B)
    print("high dimers =", len(high))
    print("mass dimers =", len(mass))
    print("high weight =", wh, float(wh))
    print("mass weight =", wm, float(wm))
    print("total weight =", wt, float(wt))
    print("mass limit =", log(100) / 3)
    print("log(M) approximately =", M.bit_length() * log(2))

    return starts, M

def top_valuation_diagnostics(starts, B):
    """
    Use the actual lcm D. For each prime p, report:
      a_p = maximal v_p(n(n+1))
      s_p = number of dimers attaining that maximum
      S_{D/p} from the order-p character.
    """
    D = actual_dimer_lcm(starts)
    primes = primes_upto(B)
    rows = []

    coins = [D // n + D // (n + 1) for n in starts]

    for p in primes:
        a = max((vp(n * (n + 1), p) for n in starts), default=0)
        if a == 0:
            continue

        top = [
            i for i, n in enumerate(starts)
            if vp(n * (n + 1), p) == a
        ]
        S = sum(sin(pi * ((coins[i] % p) / p)) ** 2 for i in top)
        rows.append((len(top), p, a, S))

    rows.sort()
    print("Smallest maximal-valuation layers:")
    for row in rows[:30]:
        print("s_p=%d, p=%d, exponent=%d, S=%.6g" % row)

def residue_dp_by_count(starts, modulus, D=None):
    """
    Exact count/residue DP for small tests.
    If D is omitted, use the actual dimer lcm.
    """
    if D is None:
        D = actual_dimer_lcm(starts)
    assert D % modulus == 0

    coins = [(D // n + D // (n + 1)) % modulus for n in starts]
    dp = {(0, 0): 1}

    for c in coins:
        ndp = dict(dp)
        for (k, r), count in dp.items():
            key = (k + 1, (r + c) % modulus)
            ndp[key] = ndp.get(key, 0) + count
        dp = ndp

    zero_layers = {
        k: count for (k, r), count in dp.items()
        if r == 0 and k > 0
    }
    return zero_layers

# Suggested experiments:
#
# starts, M = verify_family(B=10_000_000, A0=100)
# top_valuation_diagnostics(starts, B=10_000_000)
#
# For much smaller truncated families:
# small = starts[:25]
# D = actual_dimer_lcm(small)
# for p in [2, 3, 5, 7, 11]:
#     print(p, residue_dp_by_count(small, p, D))
```

Additional computational priorities:

1. Replace the ambient modulus \(L_B^2\) by the actual dimer lcm \(D\).
2. For every prime power \(p^a\mid D\), compute the count-refined transfer matrix modulo \(p^a\).
3. Record \(s_p\), the number of dimers at maximal \(p\)-valuation.
4. Test whether count-conditioned zero-residue mass survives successive CRT combinations.
5. Search for modified determinant families in which each maximal \(p\)-valuation is attained by \(\gg\log D\) dimers.

## Route Diagnosis

### Proved ledger

- **Determinant dimer identity:**  
  \[
  (a+1)(at-1)+1=a((a+1)t-1).
  \]
- **Low-lcm entropy reservoir:**  
  There are \(\gg B\log\log B\) separated dimers with endpoints dividing \(L_B^2\).
- **Arbitrarily small total reservoir mass:**  
  The same reservoir can have total weight \(<\varepsilon\), for any fixed \(\varepsilon>0\).
- **Count-layer entropy surplus:**  
  Every central layer contains more than \(L_B^2\) configurations.
- **Mass augmentation:**  
  A separated \(a=2\) band raises total available weight into \((1,2)\).
- **Exact modular reduction:**  
  A nonempty zero residue modulo the common denominator gives an exact target-\(1\) representation.
- **Count-refined Fourier formula and sufficient criterion.**
- **Maximal-valuation Fourier localization:**  
  The order-\(p\) character sees only dimers attaining maximal \(p\)-valuation.

### Plausible but unproved

- A hierarchical, prime-power-by-prime-power mixing theorem may hold after replacing optional individual dimers by packets engineered to have many representatives at every maximal valuation.
- The determinant family may be rich enough to build such packets by fixing \(a=p^e\) and varying \(t\), while sieving away accidental higher \(p\)-powers.
- Count-conditioned CRT mixing might succeed even when the stronger absolute Fourier criterion fails.

### Dead ends established here

- **Pure entropy/pigeonhole:** dead.  
  The high reservoir has \(2^{R_B}>L_B^2\) but total weight \(<1\), so it has no nonempty zero residue.
- **Uniform Fourier mixing modulo an oversized ambient \(L_B^2\):** dead without first quotienting the annihilator from unused prime powers.
- **A generic bound based only on the number of local states:** dead.  
  The arithmetic position of the target residue is decisive.

### Precise block

The missing statement is not another entropy estimate. It is a theorem controlling the count-refined subset-sum distribution through every prime-power filtration of the actual lcm, despite sparse maximal-valuation layers. Proving such a theorem for the mass-plus-determinant family would be close in strength to solving the original problem, so the route is correctly marked BLOCKED.

A fresh attempt should retain the determinant construction but redesign the local states around prime powers. The immediate objective is: for every \(p^a\) attaining the lcm maximum, create many separated dimers whose reduced denominators attain exactly \(p^a\), with coefficients forming a quantitatively mixing set modulo \(p\), while preventing any other cluster from raising the \(p\)-valuation. This is more targeted than seeking still more global entropy, which is no longer the bottleneck.