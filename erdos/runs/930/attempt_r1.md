STATUS: BLOCKED
## Result

I did not solve Erdős Problem #930. Pursuing the Erdős–Selfridge prime-allocation mechanism identifies its precise failure for disconnected sets: a prime larger than every block length can divide one integer in each component, so its valuations can cancel across components instead of being allocated to one term. I prove an exact factorial-prefix-vector reformulation, a large-prime allocation lemma, a finite-CRT obstruction to any argument using only prescribed primes, and necessary conditions on the rightmost block. In a restricted equal-length regime I also bound the relevant prime exponent by \(r\). The central remaining requirement is an ordered bounded-sum/Sidon-type property for factorial valuation vectors; already for \(r=2,q=2\) it contains the unresolved uniform square-binomial problem.

## Complete Argument

### 1. Factorial-prefix valuation vectors

Fix a prime \(q\). For \(n\ge 0\), define
\[
\Phi_q(n)=\bigl(v_p(n!)\bmod q\bigr)_p
\in \bigoplus_p\mathbb F_q,
\]
where \(0!=1\), so \(\Phi_q(0)=0\).

Order the intervals from left to right and put
\[
s_i=a_i-1,\qquad t_i=b_i.
\]
Then
\[
0\le s_1<t_1\le s_2<t_2\le\cdots\le s_r<t_r,
\]
where equality \(t_i=s_{i+1}\) corresponds to adjacent intervals.

For one interval,
\[
v_p\!\left(\prod_{m=a_i}^{b_i}m\right)
=v_p(t_i!)-v_p(s_i!).
\]
Therefore
\[
P=\prod_{i=1}^r\prod_{m=a_i}^{b_i}m
\]
is a \(q\)-th power if and only if
\[
\boxed{\ \sum_{i=1}^r\bigl(\Phi_q(t_i)-\Phi_q(s_i)\bigr)=0.\ }
\tag{1}
\]

This is an exact reformulation, not merely a necessary condition.

If \(m>n\), then
\[
\Phi_q(m)=\Phi_q(n)
\]
if and only if
\[
(n+1)(n+2)\cdots m
\]
is a \(q\)-th power. Consequently, the Erdős–Selfridge theorem gives
\[
m-n\ge2\quad\Longrightarrow\quad \Phi_q(m)\ne\Phi_q(n).
\tag{2}
\]
For \(m=n+1\), equality holds precisely when \(m\) itself is a \(q\)-th power.

Thus the one-interval theorem says that the factorial-prefix path has no repeated values across a chord of length at least two. For \(r\ge2\), however, one needs much more: the absence of ordered alternating relations of the form (1). Injectivity does not imply such a Sidon-type property.

If \(t_i=s_{i+1}\), the two corresponding terms in (1) cancel, exactly reflecting the fact that adjacent intervals may be merged. Hence configurations in which all intervals are adjacent reduce to the known \(r=1\) theorem.

---

### 2. The square-binomial obstruction is an additive parallelogram

Take
\[
I_1=[1,\ell],\qquad I_2=[n-\ell+1,n],
\qquad n\ge2\ell.
\]
Their prefix endpoints are
\[
(s_1,t_1,s_2,t_2)=(0,\ell,n-\ell,n).
\]
For \(q=2\), condition (1) becomes
\[
\Phi_2(\ell)+\Phi_2(n-\ell)+\Phi_2(n)=0,
\tag{3}
\]
since subtraction equals addition in \(\mathbb F_2\).

Now
\[
\ell!\frac{n!}{(n-\ell)!}
=(\ell!)^2\binom n\ell,
\]
so (3) holds if and only if \(\binom n\ell\) is a square. Thus the required extension of the prefix-vector no-repetition theorem would in particular have to prove
\[
\ell\ \text{sufficiently large},\quad n\ge2\ell
\quad\Longrightarrow\quad
\Phi_2(0)+\Phi_2(\ell)+\Phi_2(n-\ell)+\Phi_2(n)\ne0.
\tag{4}
\]

There are already short parallelogram relations:
\[
[1,2]\cup[8,9]:
\quad (1\cdot2)(8\cdot9)=144,
\]
and
\[
[1,3]\cup[48,50]:
\quad (1\cdot2\cdot3)(48\cdot49\cdot50)=840^2.
\]
Therefore no abstract deduction from the injectivity statement (2) can suffice: the factorial-prefix path is not globally Sidon.

An induction on the number of components also stalls here. Isolating the last interval in (1) yields
\[
\Phi_q(t_r)-\Phi_q(s_r)
=-\sum_{i<r}\bigl(\Phi_q(t_i)-\Phi_q(s_i)\bigr).
\]
Erdős–Selfridge only says that the left side is nonzero for a long interval; it gives no reason it cannot lie in the \((r-1)\)-fold sumset on the right.

---

### 3. Exact large-prime allocation lemma

Let
\[
L=\max_i |I_i|.
\]

**Lemma 1.** If \(p>L\), then each interval \(I_i\) contains at most one multiple of \(p\). If it contains one, call it \(x_{i,p}\) and put
\[
e_{i,p}=v_p(x_{i,p});
\]
otherwise put \(e_{i,p}=0\). Then
\[
v_p(P)=\sum_{i=1}^r e_{i,p}.
\tag{5}
\]
Hence, if \(P\) is a \(q\)-th power,
\[
\sum_{i=1}^r e_{i,p}\equiv0\pmod q.
\tag{6}
\]

**Proof.**
Two distinct multiples of \(p\) differ by at least \(p>L\), while the difference between any two elements of \(I_i\) is at most
\[
|I_i|-1<L.
\]
Thus there is at most one multiple in each interval. Summing its valuation over the intervals gives (5), and divisibility of every valuation by \(q\) gives (6). ∎

For \(r=1\), this gives
\[
e_{1,p}\equiv0\pmod q
\]
for every \(p>L\). Therefore, if a selected integer \(m\) is written
\[
m=c_m z_m^q,
\]
with \(c_m\) \(q\)-th-power-free, then every prime divisor of \(c_m\) is at most \(L\). This is the basic smooth-cofactor allocation available in the one-interval Erdős–Selfridge proof.

For \(r\ge2\), (6) permits cross-component cancellation. For example, modulo \(q\), one block may contribute \(1\) and another \(q-1\). The individual \(q\)-free parts are therefore no longer \(L\)-smooth.

This is the exact point where connectedness is used by the prime-allocation mechanism.

---

### 4. A consequence for exponents \(q>r\)

The preceding lemma gives a limited but rigorous exponent reduction.

**Lemma 2.** Suppose \(P\) is a \(q\)-th power with \(q>r\). If
\[
p>L,\qquad p^2>B:=\max_i b_i,
\]
then \(p\nmid P\).

**Proof.**
If \(p\mid P\), Lemma 1 shows that \(p\) divides at most one selected integer in each interval. Since every selected integer is at most \(B<p^2\), none is divisible by \(p^2\). Hence every nonzero \(e_{i,p}\) equals \(1\), and
\[
1\le v_p(P)\le r<q.
\]
This is not divisible by \(q\), contradicting that \(P\) is a \(q\)-th power. ∎

Equivalently, for \(q>r\), every prime divisor \(p>L\) of \(P\) must satisfy \(p^2\le B\), or must occur squared in at least one selected integer.

This does not yield a uniform threshold because \(B\) is unrestricted and may be arbitrarily large compared with \(L\).

---

### 5. The rightmost block must be a composite run

Let the rightmost interval be
\[
I_r=[a,B].
\]

**Lemma 3.** If \(P>1\) is a perfect power, then
\[
a>\frac B2,
\]
and every integer in \(I_r\) is composite.

**Proof.**
Suppose first that \(a\le B/2\). Bertrand’s postulate, in the form
\[
\text{for every }B\ge2\text{ there is a prime }p
\text{ with }B/2<p\le B,
\]
gives such a prime \(p\). It belongs to \([a,B]\). Since \(2p>B\), the only positive multiple of \(p\) not exceeding \(B\) is \(p\) itself. Thus
\[
v_p(P)=1,
\]
which is impossible for a perfect power.

It follows that \(a>B/2\). If some \(m\in[a,B]\) were prime, then again \(2m>B\), so \(m\) would be the unique selected multiple of the prime \(m\), giving \(v_m(P)=1\), a contradiction. ∎

This condition is compatible with arbitrarily long blocks. For example, for \(N\ge4\),
\[
[N!+2,N!+N]
\]
has length \(N-1\), lies above half its upper endpoint, and consists entirely of composite integers: \(N!+j\) is divisible by \(j\) for \(2\le j\le N\). Thus a topmost-prime argument alone cannot establish \(K(r)\).

---

### 6. A restricted exponent bound for equal-length blocks

The following illustrates what the large-prime allocation mechanism can still prove when the upper endpoint is not too large relative to the common length.

**Proposition 4.** Suppose all \(r\) intervals have the same length \(L\ge2\), the largest selected integer is \(B\), and \(P\) is a \(q\)-th power for a prime \(q>r\). Then
\[
B>L^2.
\]

**Proof.**
Write the rightmost interval as
\[
[a,B],\qquad a=B-L+1.
\]
By Lemma 3, \(a>B/2\), whence \(B\ge2L-1\).

If \(B=2L-1\), then \(a=L\). Bertrand’s postulate supplies a prime
\[
L<p<2L,
\]
and hence \(p\in[L,2L-1]=[a,B]\), contradicting Lemma 3. Therefore
\[
B\ge2L,\qquad a\ge L+1.
\]

The Sylvester–Schur theorem says that a product of \(L\) consecutive integers, all greater than \(L\), has a prime divisor \(p>L\). Applying it to
\[
a(a+1)\cdots B
\]
produces a prime \(p>L\) dividing \(P\).

If \(B\le L^2\), then
\[
p^2>L^2\ge B.
\]
Lemma 2 now contradicts \(q>r\). Thus \(B>L^2\). ∎

This proposition covers only a restricted endpoint regime. The known square-binomial examples evade it: their relevant exponent is \(q=2\le r\), and their upper endpoints already exceed \(\ell^2\).

---

### 7. Finite-prime cancellation can be engineered by CRT

The obstruction from disconnectedness is not merely hypothetical.

**Lemma 5.** Fix a length \(L\), a number of blocks \(r\), and a finite set \(S\) of primes, all larger than \(L\). For each \(i\) and \(p\in S\), prescribe either:

1. that \(p\) divide no element of the \(i\)-th block; or
2. a position \(j_{i,p}\in\{0,\ldots,L-1\}\) and an exponent \(e_{i,p}\ge1\), with the requirement
   \[
   v_p(a_i+j_{i,p})=e_{i,p}.
   \]

Then there exist positive, pairwise disjoint intervals
\[
I_i=[a_i,a_i+L-1]
\]
realizing every prescription.

**Proof.**
For an exact-valuation prescription impose
\[
a_i\equiv p^{e_{i,p}}-j_{i,p}\pmod {p^{e_{i,p}+1}}.
\tag{7}
\]
Then
\[
a_i+j_{i,p}\equiv p^{e_{i,p}}
\pmod {p^{e_{i,p}+1}},
\]
so its \(p\)-adic valuation is exactly \(e_{i,p}\).

For a nondivisibility prescription, choose a residue \(c_{i,p}\pmod p\) outside
\[
\{0,-1,\ldots,-(L-1)\}\pmod p.
\]
Such a residue exists because \(p>L\). Impose
\[
a_i\equiv c_{i,p}\pmod p.
\]

For each fixed \(i\), the moduli belonging to distinct primes are coprime. The Chinese remainder theorem therefore gives a solution \(a_i\) modulo a positive period \(M_i\). Replacing \(a_i\) by \(a_i+kM_i\) preserves all prescriptions. Choose the integers \(k\) recursively large enough that the starts are positive and
\[
a_{i+1}>a_i+L-1.
\]
The resulting intervals are pairwise disjoint.

Finally, because \(p>L\), no interval of length \(L\) can contain two multiples of \(p\). Thus the designated multiple is the only one. ∎

In particular, for any fixed finite collection of primes one can prescribe valuation patterns whose sums are \(0\bmod q\). For \(q>r\), for example, one can assign positive exponents
\[
q-r+1,1,\ldots,1
\]
to the \(r\) blocks, totaling \(q\).

This does not construct a perfect power, because uncontrolled primes remain. It does rigorously show that no argument inspecting only a predetermined finite set of primes can establish the theorem uniformly in the endpoints.

---

### 8. Ledger

#### Proved lemmas

1. The exact factorial-prefix relation (1).
2. Erdős–Selfridge gives only the no-long-repetition property (2).
3. The square-binomial family is exactly an ordered four-point relation for \(\Phi_2\).
4. For \(p\) larger than every block length, there is at most one \(p\)-multiple per block and valuations obey (5)–(6).
5. If \(q>r\), no prime \(p>L\) with \(p^2>B\) can divide a \(q\)-th-power product.
6. The rightmost block of a perfect-power configuration lies above \(B/2\) and is entirely composite.
7. For equal-length blocks, a \(q\)-th power with \(q>r\) must have \(B>L^2\).
8. Any finite prescribed large-prime incidence and valuation pattern can be realized by CRT.

#### Plausible but unproved targets

1. An eventual ordered \(B_r\)-type property for the vectors \(\Phi_q(n)\), forbidding (1) when every chord is long. This is essentially the original problem in additive form.
2. A global theorem forcing a prime \(p>L\) whose selected multiples all have \(p\)-adic valuation \(1\). This would handle \(q>r\), but it is false for short blocks and no uniform version was proved.
3. Uniform boundedness of the lower index of square binomial coefficients. This is already required by the \(r=2,q=2\) special family.

#### Dead ends

1. **Prefix-vector injectivity:** no repeated prefix vectors does not prohibit parallelograms; the two known square examples give explicit parallelograms.
2. **Induction on components:** isolating one chord reduces the problem to excluding it from an \((r-1)\)-fold sumset, which is of comparable strength.
3. **A valuation-one strengthening:** even one consecutive interval can be a nonpower with no prime valuation equal to \(1\):
   \[
   8\cdot9=2^3 3^2.
   \]
4. **Topmost primes:** the rightmost block must be prime-free, but arbitrarily long composite runs exist.
5. **Predetermined large primes:** finite-prime cancellation patterns are realizable by CRT.
6. **Applying Erdős–Selfridge blockwise:** squarefree or \(q\)-free parts can cancel between blocks, as the explicit square examples demonstrate.

## Self-Audit

1. **The restricted exponent proposition invokes the Sylvester–Schur theorem rather than reproving it.** This is a classical unconditional theorem, and it is used only for Proposition 4, not for the main blockage diagnosis. Removing Proposition 4 leaves all other conclusions intact.

2. **The CRT lemma controls only finitely many primes.** It does not show that all prime valuations can be made divisible by \(q\), so it is not a counterexample construction. I use it only to rule out proof strategies based on a fixed finite prime set.

3. **The conclusion “blocked” depends on recognizing the square-binomial uniformity problem as unresolved.** The mathematical reduction itself is exact and proved above. I do not claim that the reduction proves impossibility of a future Route 1 argument—only that the present argument reaches an unresolved statement of comparable strength and provides no mechanism to pass it.

## Computations To Verify

The following pure Python performs the principal finite checks.

```python
from math import gcd, comb, isqrt
from collections import defaultdict

def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def interval_valuations(intervals):
    v = defaultdict(int)
    for a, b in intervals:
        for n in range(a, b + 1):
            for p, e in factorint(n).items():
                v[p] += e
    return dict(v)

def power_gcd(intervals):
    v = interval_valuations(intervals)
    if not v:
        return 0
    g = 0
    for e in v.values():
        g = gcd(g, e)
    return g

def is_perfect_power_product(intervals):
    return power_gcd(intervals) >= 2

# Known examples and failure of the valuation-one strengthening.
assert interval_valuations([(1, 2), (8, 9)]) == {2: 4, 3: 2}
assert power_gcd([(1, 2), (8, 9)]) == 2

assert interval_valuations([(1, 3), (48, 50)]) == {
    2: 6, 3: 2, 7: 2, 5: 2
}
assert power_gcd([(1, 3), (48, 50)]) == 2

assert interval_valuations([(8, 9)]) == {2: 3, 3: 2}
assert power_gcd([(8, 9)]) == 1
assert 1 not in interval_valuations([(8, 9)]).values()


def factorial_valuations(n):
    v = defaultdict(int)
    for m in range(2, n + 1):
        for p, e in factorint(m).items():
            v[p] += e
    return dict(v)

def endpoint_relation(intervals, q):
    """Returns sum_i(Phi_q(b_i)-Phi_q(a_i-1))."""
    out = defaultdict(int)
    for a, b in intervals:
        for p, e in factorial_valuations(b).items():
            out[p] = (out[p] + e) % q
        for p, e in factorial_valuations(a - 1).items():
            out[p] = (out[p] - e) % q
    return {p: e for p, e in out.items() if e % q}

assert endpoint_relation([(1, 2), (8, 9)], 2) == {}
assert endpoint_relation([(1, 3), (48, 50)], 2) == {}


def square_binomial_search(max_l, max_n):
    ans = []
    for l in range(2, max_l + 1):
        for n in range(2 * l, max_n + 1):
            c = comb(n, l)
            y = isqrt(c)
            if y * y == c:
                ans.append((n, l, y))
    return ans

hits = square_binomial_search(20, 1000)
assert (9, 2, 6) in hits
assert (50, 3, 140) in hits
print("Square binomial hits:", hits)


def isprime(n):
    if n < 2:
        return False
    return len(factorint(n)) == 1 and next(iter(factorint(n).values())) == 1

# Brute-force verification of Lemma 3 for all two-block
# perfect-power configurations with upper endpoint at most max_B.
def verify_top_block_lemma(max_B=80):
    examples = []
    for a in range(1, max_B + 1):
        for b in range(a, max_B + 1):
            for c in range(b + 1, max_B + 1):
                for d in range(c, max_B + 1):
                    intervals = [(a, b), (c, d)]
                    if is_perfect_power_product(intervals):
                        assert 2 * c > d
                        assert all(not isprime(n) for n in range(c, d + 1))
                        examples.append(intervals)
    return examples

print("Small perfect-power configurations:",
      verify_top_block_lemma(60)[:20])


def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def crt_pairwise_coprime(congruences):
    """congruences is a list of (residue, modulus)."""
    x, M = 0, 1
    for a, m in congruences:
        inv = pow(M, -1, m)
        t = ((a - x) * inv) % m
        x += M * t
        M *= m
        x %= M
    return x, M

def realize_exact_patterns(L, specifications):
    """
    specifications[i] is a dictionary
       p -> (j, e)
    requiring v_p(a_i+j)=e.
    All p must exceed L.
    """
    intervals = []
    previous_end = 0

    for spec in specifications:
        congruences = []
        for p, (j, e) in spec.items():
            assert p > L
            assert 0 <= j < L
            congruences.append(((p ** e - j) % (p ** (e + 1)),
                                p ** (e + 1)))

        a, M = crt_pairwise_coprime(congruences)
        if a < 1:
            a += M
        if a <= previous_end:
            k = (previous_end - a) // M + 1
            a += k * M

        intervals.append((a, a + L - 1))
        previous_end = a + L - 1

    # Verify exact valuations and uniqueness of the p-multiple.
    for i, spec in enumerate(specifications):
        a, b = intervals[i]
        for p, (j, e) in spec.items():
            assert vp(a + j, p) == e
            assert sum(n % p == 0 for n in range(a, b + 1)) == 1

    return intervals

# For q=5 and r=2, prescribe 1+4=5 for two primes.
specs = [
    {11: (0, 1), 13: (3, 1)},
    {11: (5, 4), 13: (7, 4)},
]
crt_intervals = realize_exact_patterns(10, specs)
print("CRT intervals:", crt_intervals)
v = interval_valuations(crt_intervals)
assert v[11] % 5 == 0
assert v[13] % 5 == 0
# Other primes are uncontrolled, as expected.
```

A useful larger search would hash
\[
\operatorname{sf}\left(\prod_{j=0}^{L-1}(a+j)\right)
\]
for every interval in a bounded range and report disjoint collisions. Such collisions are precisely square products of two blocks.

## Route Diagnosis

Route 1 successfully isolates where the one-component proof uses connectedness: for \(p\) larger than the interval length, the prime belongs to at most one selected term, forcing its exponent in that term to be divisible by \(q\). With multiple components, the same prime can occur once per block and cancel modulo \(q\); arbitrary gaps provide enough freedom for any finite such pattern to be imposed by CRT.

The route is blocked at the need to control all large primes globally. In factorial-prefix language, one must prove that the path \(\Phi_q(n)\) has no ordered alternating \(2r\)-term relation with long chords. Erdős–Selfridge proves only the two-term no-repetition case. For \(r=2,q=2\), the required four-term assertion already implies a uniform bound on square binomial coefficients with \(n\ge2\ell\), so the remaining statement is of comparable unresolved strength.

A fresh attempt should either:

1. obtain a genuinely global bound on shared large-prime kernels, perhaps through resultants or products of cross-block differences, strong enough to defeat unrestricted CRT-sized gaps; or
2. switch to the disproof direction and search for an unbounded family of square-binomial coefficients or more general squarefree-kernel collisions.

No argument developed here closes either gap.