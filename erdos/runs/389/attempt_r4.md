STATUS: BLOCKED

## Result

Route 4 yields substantial structural information but not a complete solution. Writing \(x=m+k\), I prove an exact residue formula for every floor contribution, completely classify negative contributions for primes \(p>m\), and show that a successful \(x\) forces each of the \(\lceil m/2\rceil\) integers \(x,x-1,\ldots,x-\lceil m/2\rceil+1\) to avoid large prime-power divisors. In particular, each must have no prime factor exceeding \(\sqrt{2x-m}\). Such a large-prime obstruction occurs for a proportion \(\log 2+o(1)\) of the integers at any one endpoint. On the positive side, I prove that for some \(\eta>0\), almost every \(x\in[X,2X]\) satisfies all valuation inequalities for primes \(p\le \exp(\eta\sqrt{\log X})\). Thus the analytic problem is genuinely concentrated in moving medium and large prime factors of a fixed block of consecutive integers. The route is blocked because obtaining a lower bound for simultaneous avoidance of those large-prime obstructions—and then imposing the remaining higher-digit balance—is a shifted friable-correlation problem not resolved by the argument.

## Complete Argument

The case \(m=0\) is already solved, since \(R_0(k)=\binom{2k}{k}\). Hence assume \(m\ge1\), and put
\[
x=m+k>m.
\]
Then
\[
R_m(k)=\frac{(2x-m)!\,m!}{x!^2}.
\]

For every integer \(q\ge2\), define
\[
E_q(m,x):=
\left\lfloor\frac{2x-m}{q}\right\rfloor
+\left\lfloor\frac mq\right\rfloor
-2\left\lfloor\frac xq\right\rfloor.
\]
Thus
\[
D_p(m,x):=v_p(R_m(x-m))
=\sum_{a\ge1}E_{p^a}(m,x).
\]

### 1. Exact residue description

Write
\[
m=uq+b,\qquad x=vq+r,\qquad 0\le b,r<q.
\]
Then
\[
2x-m=(2v-u)q+(2r-b),
\]
and therefore
\[
E_q(m,x)=\left\lfloor\frac{2r-b}{q}\right\rfloor. \tag{1}
\]

Since \(-q<2r-b<2q\), this gives \(E_q\in\{-1,0,1\}\), with
\[
E_q=-1\iff 2r<b, \tag{2}
\]
and
\[
E_q=1\iff 2r\ge q+b. \tag{3}
\]

This formula is the useful local normal form: all floor contributions depend only on \(m\bmod q\) and \(x\bmod q\).

As an immediate consequence, the Gaussian-binomial strengthening from Route 2 cannot work for any \(m\ge1\). Indeed, taking \(q=x\),
\[
E_x(m,x)
=
\left\lfloor\frac{2x-m}{x}\right\rfloor
+\left\lfloor\frac mx\right\rfloor-2
=1+0-2=-1,
\]
because \(0<m<x\). Thus every positive-\(k\) instance has a negative cyclotomic exponent at \(d=x=m+k\). Any ordinary integrality must use cancellation among different powers of the same prime.

### 2. Complete description for primes \(p>m\)

Let
\[
H:=\left\lceil\frac m2\right\rceil.
\]
For \(q>m\), equation (2) becomes
\[
E_q(m,x)=-1
\iff x\bmod q\in\{0,1,\ldots,H-1\}. \tag{4}
\]

Now fix a prime \(p>m\). If any \(E_{p^a}\) is negative, then for some \(j\in\{0,\ldots,H-1\}\),
\[
p^a\mid x-j.
\]
Moreover, the same \(j\) must occur at every negative level: if \(a<b\) and
\[
x\bmod p^a=j_a,\qquad x\bmod p^b=j_b,
\]
with \(0\le j_a,j_b<H<p^a\), then \(j_a\equiv j_b\pmod{p^a}\), hence \(j_a=j_b\).

Because \(H<p\), at most one \(j\in\{0,\ldots,H-1\}\) can satisfy \(p\mid x-j\). If no such \(j\) exists, all \(E_{p^a}\ge0\), so
\[
D_p(m,x)\ge0. \tag{5}
\]

If such a \(j\) exists, put
\[
t:=v_p(x-j).
\]
Then exactly the levels \(a=1,\ldots,t\) are negative. All later contributions are zero or positive. Hence the exact formula is
\[
D_p(m,x)
=
-t+
\#\left\{
a>t:
x\bmod p^a\ge
\left\lceil\frac{p^a+m}{2}\right\rceil
\right\}. \tag{6}
\]
Only powers \(p^a\le2x-m\) can contribute positively.

This proves the following obstruction.

**Lemma 1.**  
If \(p>m\), \(0\le j<H\), \(t=v_p(x-j)\ge1\), and
\[
p^{2t}>2x-m,
\]
then
\[
D_p(m,x)<0.
\]

**Proof.** Let \(L\) be the largest exponent with \(p^L\le2x-m\). The displayed assumption gives \(L\le2t-1\). Formula (6) has \(t\) negative terms, while there are at most
\[
L-t\le t-1
\]
possible positive terms. Thus \(D_p\le-1\). ∎

Consequently, every successful \(x\) must satisfy
\[
p^{v_p(x-j)}\le \sqrt{2x-m}
\qquad
(0\le j<H,\ p>m). \tag{7}
\]

In particular, if
\[
p>\sqrt{2x-m}
\quad\text{and}\quad
p\mid x-j
\]
for some \(j<H\), then \(D_p=-1\). Thus every successful \(x\) satisfies
\[
P^+(x-j)\le\sqrt{2x-m}
\qquad(0\le j<H), \tag{8}
\]
where \(P^+(n)\) denotes the largest prime factor of \(n\).

Condition (8) is only necessary, not sufficient. For example, take \(m=1\) and \(x=30\), so \(k=29\). All prime factors of \(30\) are below \(\sqrt{59}\), but for \(p=3\),
\[
E_3=-1,\qquad E_9=0,\qquad E_{27}=0,
\]
and all later terms vanish. Hence \(D_3=-1\). This counterexample rules out any claim that square-root smoothness alone settles the valuation conditions.

### 3. The top-level obstruction has nonzero density

For one fixed endpoint, the large-prime obstruction is not rare.

**Lemma 2.**  
Let
\[
B(N):=\#\{n\le N:\text{some prime }p\mid n\text{ has }p^2>2n\}.
\]
Then
\[
B(N)=(\log 2)N+o(N). \tag{9}
\]

**Proof.** Write \(n=ap\). The condition \(p^2>2n\) is equivalent to
\[
p>2a.
\]
There can be at most one such prime divisor, since two distinct primes both exceeding \(\sqrt{2n}\) would have product greater than \(2n>n\).

Therefore
\[
B(N)
=
\sum_{p\le N}
\min\left(
\left\lfloor\frac{p-1}{2}\right\rfloor,
\left\lfloor\frac Np\right\rfloor
\right).
\]
For \(p\le\sqrt{2N}\), the first term is the minimum, and
\[
\sum_{p\le\sqrt{2N}}p=O\left(\frac{N}{\log N}\right).
\]
For \(p>\sqrt{2N}\), the second term is the minimum, giving
\[
\sum_{\sqrt{2N}<p\le N}\left\lfloor\frac Np\right\rfloor
=
N\sum_{\sqrt{2N}<p\le N}\frac1p+O(\pi(N)).
\]
Mertens' theorem for primes yields
\[
\sum_{\sqrt{2N}<p\le N}\frac1p
=
\log\log N-\log\log\sqrt{2N}+o(1)
=
\log2+o(1).
\]
Also \(\pi(N)=O(N/\log N)\), proving (9). ∎

For a fixed \(j<H\), put \(n=x-j\). The threshold in the original obstruction is
\[
p^2>2x-m=2n+2j-m.
\]
Since \(2j-m<0\) is fixed, this differs from \(p^2>2n\) for only \(O_m(1)\) exceptional pairs \((n,p)\). Indeed, if
\[
2n+2j-m<p^2\le2n,
\]
then
\[
0\le 2n-p^2<m-2j.
\]
Writing \(n=ap\), the left side is \(p(2a-p)\). For \(p>m-2j\), this is either zero or at least \(p>m-2j\); the zero case \(p=2a\) only permits \(p=2\). Thus only bounded primes can contribute to the discrepancy.

It follows that, for each individual endpoint \(x-j\), the top large-prime obstruction occurs for a proportion
\[
\log2+o(1), \tag{10}
\]
while the proportion surviving it is
\[
1-\log2+o(1).
\]

For \(H\ge2\), however, this does not give a simultaneous lower bound. The union bound gives only
\[
1-H\log2+o(1),
\]
which is already negative when \(H\ge2\). Controlling the intersections requires information about large prime factors of several shifted integers.

### 4. Small and moderately small primes are almost always harmless

The following is the main positive result from Route 4.

**Theorem 3.**  
For each fixed \(m\ge1\), there is a constant \(\eta=\eta(m)>0\) such that, as \(X\to\infty\),
\[
\#\left\{
x\in[X,2X]:
D_p(m,x)\ge0
\text{ for every prime }
p\le e^{\eta\sqrt{\log X}}
\right\}
=
X-o(X). \tag{11}
\]

In fact the constants below can be chosen uniformly once \(m\) is fixed.

**Proof.**

Let
\[
V_p(x):=\max_{0\le j<H}v_p(x-j).
\]
Choose a constant \(C_m\) larger than the number of powers \(p^a\le m\), uniformly over all primes \(p\). For example,
\[
C_m=2+\lfloor\log_2m\rfloor
\]
suffices.

For powers \(p^a>m\), every negative contribution corresponds by (4) to a congruence
\[
x\equiv j\pmod{p^a}
\]
for some \(0\le j<H\). As above, all such negative levels for a fixed \(p\) use the same \(j\). Therefore their total number is at most \(V_p(x)\). The lower levels contribute at worst \(-C_m\).

We now select a family of easily recognized positive contributions.

Suppose first that \(p\) is odd. Write
\[
x\bmod p^A=d_0+d_1p+\cdots+d_{A-1}p^{A-1}.
\]
For a position \(i\) with \(p^i\ge m\), if
\[
d_i\ge\frac{p+1}{2},
\]
then for \(q=p^{i+1}\),
\[
x\bmod q\ge \frac{p+1}{2}p^i
=\frac q2+\frac{p^i}{2}
\ge\frac{q+m}{2}.
\]
By (3), \(E_q=1\).

For a uniformly distributed residue modulo \(p^A\), the digits are independent, and the probability that a digit meets this condition is
\[
\frac{p-1}{2p}\ge\frac13.
\]

For \(p=2\), use disjoint pairs of adjacent binary digits. If the two highest digits below \(q=2^{i+1}\) are both \(1\), then
\[
x\bmod q\ge 2^i+2^{i-1}=\frac{3q}{4}.
\]
When \(2^i\ge m\),
\[
\frac{3q}{4}\ge\frac{q+m}{2},
\]
so again \(E_q=1\). On disjoint pairs these events are independent and have probability \(1/4\).

It follows from the Chernoff bound that there are absolute constants \(c_0,c_1>0\), depending at most on the finitely many initial positions determined by \(m\), such that among residues modulo \(p^A\),
\[
\Pr(Z_p<c_0A)\le e^{-c_1A}, \tag{12}
\]
where \(Z_p\) is the number of selected positive contributions.

On the other hand, for \(T<A\),
\[
\Pr(V_p(x)>T)
\le
\sum_{j=0}^{H-1}
\Pr\bigl(p^{\lfloor T\rfloor+1}\mid x-j\bigr)
\le H p^{-\lfloor T\rfloor-1}
\le H2^{-T}. \tag{13}
\]

Every contribution not selected as positive is at least zero, except for the at most \(V_p(x)+C_m\) negative contributions already accounted for. Hence
\[
D_p(m,x)\ge Z_p-V_p(x)-C_m. \tag{14}
\]
For sufficiently large \(A\), if
\[
Z_p\ge c_0A
\quad\text{and}\quad
V_p(x)\le\frac{c_0A}{2},
\]
then the right side of (14) is nonnegative. Equations (12) and (13) therefore give constants \(c,C_m'>0\) such that
\[
\Pr_{r\bmod p^A}\bigl(D_p(m,r)<0\bigr)
\le C_m'e^{-cA}. \tag{15}
\]

To transfer this estimate to \(x\in[X,2X]\), set
\[
A=A_p(X):=\lfloor\log_pX\rfloor-1.
\]
Then
\[
p^A\le \frac Xp.
\]
Consequently \([X,2X]\) contains at least \(p\) complete periods modulo \(p^A\), and the density of any set of residues in this interval is at most twice its density in a complete period. Thus
\[
\frac1X
\#\{x\in[X,2X]:D_p(m,x)<0\}
\le 2C_m'e^{-cA_p(X)}. \tag{16}
\]

Now let
\[
Y=\exp(\eta\sqrt{\log X}).
\]
For every \(p\le Y\),
\[
A_p(X)\ge\frac{\log X}{\log Y}-2
=\frac{\sqrt{\log X}}{\eta}-2.
\]
Using the union bound over at most \(Y\) primes, the exceptional proportion is at most
\[
2C_m'Y
\exp\left(
-c\left(\frac{\sqrt{\log X}}{\eta}-2\right)
\right).
\]
Its logarithm is at most
\[
\left(\eta-\frac c\eta\right)\sqrt{\log X}+O_m(1).
\]
Choose \(\eta>0\) with \(\eta^2<c\). The last expression tends to \(-\infty\), proving (11). ∎

A fixed-prime consequence is worth recording:
\[
\#\{x\le X:D_p(m,x)<0\}
=O_{m,p}(X^{1-\delta_p})
\]
for some \(\delta_p>0\). Thus no fixed finite collection of primes can perpetually obstruct almost all \(x\).

### 5. The remaining analytic block

Combining Theorem 3 with the classification for \(p>m\), almost every \(x\in[X,2X]\) can fail only because of a prime
\[
p>\exp(\eta\sqrt{\log X})
\]
dividing one of
\[
x,x-1,\ldots,x-H+1,
\]
with too few positive higher-power contributions to cancel the initial negative contribution.

The very top range
\[
p>\sqrt{2x-m}
\]
already forces the necessary conditions
\[
P^+(x-j)\le\sqrt{2x-m}
\qquad(0\le j<H).
\]
Even after these are met, the example \(m=1,x=30\) shows that medium primes can still cause a deficit through unfavorable higher base-\(p\) digits.

Therefore a Route 4 proof still needs a lower-bound sieve for a family of shifted friability and digit-balance constraints. No such lower bound is obtained above. In particular, the fact that each individual endpoint survives its top obstruction with density \(1-\log2\) does not imply that all \(H\) endpoints survive simultaneously.

## Self-Audit

1. **The weakest technical point is the uniformity in Theorem 3 as \(p\) grows with \(X\).**  
   The proof avoids assuming global equidistribution modulo a huge product: it treats one prime at a time modulo \(p^{A_p(X)}\), whose modulus is at most \(X/p\), and then uses only a union bound. The selected digit events are genuinely independent within one complete residue system, and the interval contains at least \(p\) complete periods. Thus the claimed range \(p\le e^{\eta\sqrt{\log X}}\) is justified.

2. **The prime-power obstruction has a strict inequality \(p^{2t}>2x-m\).**  
   Equality cannot be included automatically: at \(p^{2t}=2x-m\), the level \(a=2t\) may provide the final positive contribution needed to cancel \(t\) negatives. The proof only uses the strict form and therefore does not lose an endpoint case.

3. **The passage from the top obstruction to “shifted friability” is only a necessary condition.**  
   I do not infer integrality from it. The explicit counterexample \(m=1,x=30,p=3\) demonstrates the missing medium-prime condition. Thus the diagnosis is deliberately weaker than a solution, not a hidden sufficiency claim.

## Computations To Verify

The following Python/SymPy code checks all local identities, searches for solutions, verifies the \(p>m\) classification, and measures the obstruction statistics.

```python
from math import isqrt, ceil, exp, sqrt, log
from sympy import primerange, factorint

def E(m, x, q):
    return (2*x - m)//q + m//q - 2*(x//q)

def E_residue(m, x, q):
    b = m % q
    r = x % q
    return (2*r - b)//q

def D(m, x, p):
    """v_p((2x-m)! m! / x!^2), where x=m+k."""
    q = p
    ans = 0
    while q <= 2*x - m:
        ans += E(m, x, q)
        q *= p
    return ans

def all_valuations(m, x):
    return {p: D(m, x, p) for p in primerange(2, 2*x-m+1)}

def good(m, x):
    assert x > m
    return all(v >= 0 for v in all_valuations(m, x).values())

def vp(n, p):
    t = 0
    while n % p == 0:
        n //= p
        t += 1
    return t

def largest_prime_factor(n):
    if n == 1:
        return 1
    return max(factorint(n))

# 1. Verify the residue identity exhaustively.
def check_residue_identity(M=50, X=500, Q=500):
    for m in range(1, M+1):
        for x in range(m+1, X+1):
            for q in range(2, Q+1):
                assert E(m, x, q) == E_residue(m, x, q)
                assert E(m, x, q) in (-1, 0, 1)

# 2. Verify the exact p>m classification.
def check_large_prime_classification(M=30, X=2000):
    for m in range(1, M+1):
        H = (m + 1)//2
        for x in range(m+1, X+1):
            for p in primerange(m+1, 2*x-m+1):
                js = [j for j in range(H) if (x-j) % p == 0]
                assert len(js) <= 1
                actual = D(m, x, p)

                if not js:
                    assert actual >= 0
                    continue

                j = js[0]
                t = vp(x-j, p)
                positive = 0
                q = p
                a = 1
                while q <= 2*x-m:
                    if a > t and E(m, x, q) == 1:
                        positive += 1
                    q *= p
                    a += 1

                assert actual == -t + positive

                if p**(2*t) > 2*x-m:
                    assert actual < 0

# 3. Every successful x must pass the top obstruction.
def check_top_obstruction(M=30, X=10000):
    for m in range(1, M+1):
        H = (m+1)//2
        for x in range(m+1, X+1):
            if good(m, x):
                for j in range(H):
                    for p in factorint(x-j):
                        if p > m:
                            assert p*p <= 2*x-m

# 4. Confirm the examples and the square-root-smooth counterexample.
assert good(1, 6)       # m=1, k=5
assert good(2, 6)       # m=2, k=4
assert D(1, 30, 3) == -1
assert not good(1, 30)

# 5. Verify that the Gaussian/cyclotomic strengthening always fails at d=x.
def check_gaussian_failure(M=100, X=1000):
    for m in range(1, M+1):
        for x in range(m+1, X+1):
            assert E(m, x, x) == -1

# 6. Search statistics: successful and near-successful x.
def search_stats(m, X):
    successes = []
    near = []
    obstruction_hist = {}
    H = (m+1)//2

    for x in range(m+1, X+1):
        vals = all_valuations(m, x)
        bad = [(p, v) for p, v in vals.items() if v < 0]

        if not bad:
            successes.append(x)
        elif len(bad) == 1:
            near.append((x, bad[0]))

        for p, v in bad:
            obstruction_hist[p] = obstruction_hist.get(p, 0) + 1

        # A successful x must have no top prime obstruction.
        if not bad:
            for j in range(H):
                assert all(p*p <= 2*x-m for p in factorint(x-j) if p > m)

    return {
        "m": m,
        "X": X,
        "successes": successes,
        "near_successes": near,
        "obstruction_histogram": obstruction_hist,
    }

# 7. Measure how often any small prime is bad.
def small_prime_bad_fraction(m, X, eta=0.05):
    Y = int(exp(eta * sqrt(log(X))))
    bad_count = 0
    for x in range(X, 2*X):
        if any(D(m, x, p) < 0 for p in primerange(2, Y+1)):
            bad_count += 1
    return Y, bad_count / X

# 8. Measure the top obstruction at each endpoint and jointly.
def top_obstruction_stats(m, X):
    H = (m+1)//2
    endpoint_bad = [0]*H
    joint_survivors = 0

    for x in range(X, 2*X):
        survives_all = True
        for j in range(H):
            bad = any(p*p > 2*x-m for p in factorint(x-j))
            endpoint_bad[j] += int(bad)
            survives_all &= not bad
        joint_survivors += int(survives_all)

    return {
        "endpoint_bad_fractions": [c/X for c in endpoint_bad],
        "joint_survival_fraction": joint_survivors/X,
        "expected_single_bad_limit": log(2),
        "naive_independence_survival": (1-log(2))**H,
    }
```

Recommended finite experiments:

1. Run `check_large_prime_classification(50, 100000)`.
2. For fixed \(m=5,10,20,50\), compare `small_prime_bad_fraction` over geometrically increasing \(X\).
3. Compare the measured joint top-survival frequency with \((1-\log2)^H\); large deviations would warn against the independence heuristic.
4. For every failed \(x\), group the smallest obstructing prime by the range
   \[
   X^{1/(r+1)}<p\le X^{1/r}.
   \]
   Test whether conditional deficit frequencies decay exponentially in \(r\).
5. Among top-surviving \(x\), measure how often the remaining obstruction is caused by \(p^2,p^3,\ldots\) and record the exact positive levels in formula (6).

## Route Diagnosis

**Proved ledger**

- Exact residue formula
  \[
  E_q(m,x)=\left\lfloor\frac{2(x\bmod q)-(m\bmod q)}q\right\rfloor.
  \]
- Complete classification of negative levels for every prime \(p>m\).
- Prime-power obstruction:
  \[
  p^{2v_p(x-j)}>2x-m\Longrightarrow D_p(m,x)<0.
  \]
- Necessary simultaneous square-root smoothness of
  \[
  x,x-1,\ldots,x-\lceil m/2\rceil+1.
  \]
- A single endpoint has a top obstruction with density \(\log2\).
- Almost every \(x\in[X,2X]\) satisfies all local conditions for
  \[
  p\le e^{\eta\sqrt{\log X}}.
  \]
- The Gaussian-binomial strengthening is impossible for every \(m\ge1,k\ge1\), because \(E_{m+k}=-1\).

**Plausible but unproved**

- The local model suggests a positive limiting density of successful \(x\) for each fixed \(m\). For primes in
  \[
  X^{1/(r+1)}<p\le X^{1/r},
  \]
  a prime dividing an endpoint has only \(r\) or so relevant power levels, while the probability of receiving too few positive upper-digit contributions should decay exponentially in \(r\).
- The top smoothness conditions may behave approximately independently, suggesting a joint factor near
  \[
  (1-\log2)^H,
  \]
  but this independence is not justified.
- A multidimensional Buchstab or shifted-friable sieve might produce the required lower bound, but it must retain enough residue information to enforce formula (6), not merely smoothness.

**Dead ends**

- Requiring \(E_d\ge0\) for every \(d\) is not merely too strong; it is impossible because \(E_x=-1\).
- Eliminating only primes in the short interval near \(x\) misses large prime factors of composite endpoint values.
- Square-root smoothness is not sufficient, as \(m=1,x=30,p=3\) shows.
- A union bound over the \(H\) endpoints fails once \(H\ge2\).
- A naïve CRT treatment remains circular: forcing conditions modulo many prime powers enlarges \(x\) and introduces a new uncontrolled prime range.

**Precise block**

A successful analytic sieve must establish a positive lower bound for integers \(x\) satisfying simultaneous shifted large-prime restrictions on
\[
\prod_{j=0}^{H-1}(x-j),
\]
and must then impose the higher-power digit balance in (6). Theorem 3 removes all fixed and subexponentially small primes for almost every \(x\), but gives no control over intersections of the moving large-prime events. That intersection problem is the exact obstruction to completing Route 4.

A fresh attempt should focus on a multidimensional Buchstab decomposition of the consecutive linear forms \(x-j\), with the local weight for a prime \(p\) defined by the exact deficit condition \(D_p<0\). Merely counting smooth consecutive integers will not suffice, but it is the unavoidable first layer.