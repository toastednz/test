STATUS: BLOCKED

## Result

Route 3 yields exact carry and digit-sum formulations, several rigorous localization lemmas, and a strong obstruction to any argument using only a predetermined finite set of prime bases. In the crucial two-block square-binomial subfamily, the factorial contributions cancel modulo \(2\), and the desired conclusion becomes exactly the assertion that \(\binom n\ell\) has an odd Kummer carry count in some base for all sufficiently large \(\ell\). This is the unresolved uniform square-binomial problem highlighted in the brief. I also prove, using Sylvester’s theorem, that any \(q\)-th-power binomial coefficient with \(n\ge 2\ell\) must satisfy \(n\ge(\ell+1)^q\), showing that possible obstructions necessarily occur with endpoints extremely large relative to the block lengths.

## Complete Argument

### 1. Exact factorial, carry, and digit-sum formulas

Write an interval as
\[
I=[x+1,x+\ell],\qquad x\ge 0,\quad \ell\ge1.
\]
Then
\[
\prod_{m\in I}m
=\frac{(x+\ell)!}{x!}
=\ell!\binom{x+\ell}{\ell}.
\]

For a prime \(p\) and \(j\ge1\), define
\[
\delta_{p,j}(x,\ell)
=
\left\lfloor\frac{x+\ell}{p^j}\right\rfloor
-\left\lfloor\frac{x}{p^j}\right\rfloor
-\left\lfloor\frac{\ell}{p^j}\right\rfloor.
\]

Writing \(x=up^j+r\) and \(\ell=vp^j+s\), with \(0\le r,s<p^j\), gives
\[
\delta_{p,j}(x,\ell)
=\left\lfloor\frac{r+s}{p^j}\right\rfloor\in\{0,1\}.
\]
Thus
\[
\delta_{p,j}(x,\ell)=1
\quad\Longleftrightarrow\quad
(x\bmod p^j)+(\ell\bmod p^j)\ge p^j.
\]

Legendre’s formula now gives
\[
\begin{aligned}
v_p\left(\prod_{m=x+1}^{x+\ell}m\right)
&=\sum_{j\ge1}
\left(
\left\lfloor\frac{x+\ell}{p^j}\right\rfloor
-\left\lfloor\frac{x}{p^j}\right\rfloor
\right)\\
&=\sum_{j\ge1}\left\lfloor\frac{\ell}{p^j}\right\rfloor
+\sum_{j\ge1}\delta_{p,j}(x,\ell)\\
&=v_p(\ell!)+\kappa_p(x,\ell),
\end{aligned}
\]
where
\[
\kappa_p(x,\ell):=\sum_{j\ge1}\delta_{p,j}(x,\ell)
=v_p\binom{x+\ell}{\ell}.
\]
By Kummer’s theorem, \(\kappa_p(x,\ell)\) is the number of carries when adding \(x\) and \(\ell\) in base \(p\).

For \(r\) intervals
\[
I_i=[x_i+1,x_i+\ell_i],
\]
we therefore have the exact identity
\[
v_p(P)
=
\sum_{i=1}^r v_p(\ell_i!)
+\sum_{i=1}^r\kappa_p(x_i,\ell_i).
\tag{1}
\]
After ordering the intervals, disjointness says only
\[
x_i+\ell_i\le x_{i+1}.
\tag{2}
\]
In particular, it imposes no direct congruence relation between the \(x_i\) modulo powers of \(p\).

There is also an exact digit-sum form. Let \(s_p(n)\) denote the sum of the base-\(p\) digits of \(n\). Since
\[
v_p(n!)=\frac{n-s_p(n)}{p-1},
\]
we obtain
\[
(p-1)v_p\left(\frac{(x+\ell)!}{x!}\right)
=
\ell+s_p(x)-s_p(x+\ell).
\]
Consequently, with \(L=\sum_i\ell_i\),
\[
(p-1)v_p(P)
=
L+\sum_{i=1}^r s_p(x_i)
-\sum_{i=1}^r s_p(x_i+\ell_i).
\tag{3}
\]

Thus \(P\) is a \(q\)-th power if and only if, for every prime \(p\),
\[
L+\sum_i s_p(x_i)-\sum_i s_p(x_i+\ell_i)
\equiv0\pmod{q(p-1)}.
\tag{4}
\]
Equations (1) and (4) are exact; the difficulty is forcing one of these congruences to fail uniformly over arbitrary \(x_i\).

---

### 2. What genuinely large bases can detect

Let
\[
B=\max_i b_i,\qquad U=\bigcup_i I_i.
\]

#### Lemma 1: Square-root localization

If \(p>\sqrt B\), then
\[
v_p(P)=|U\cap p\mathbb Z|.
\tag{5}
\]

#### Proof

Every selected integer \(m\) satisfies \(m\le B<p^2\). Hence \(v_p(m)\) is either \(0\) or \(1\), according as \(p\nmid m\) or \(p\mid m\). Summing over \(m\in U\) proves (5). ∎

Therefore, if \(P\) is a \(q\)-th power and
\[
p>\max\{\sqrt B,B/q\},
\]
then \(U\) contains no multiple of \(p\). Indeed, if it contained one, then
\[
1\le v_p(P)=|U\cap p\mathbb Z|
\le \left\lfloor\frac Bp\right\rfloor<q,
\]
contradicting \(q\mid v_p(P)\).

In particular, for every perfect power \(P\),
\[
U\cap\{p:\ p\text{ prime},\ B/2<p\le B\}=\varnothing.
\tag{6}
\]
This holds independently of the exponent.

If \(L_{\max}=\max_i\ell_i\) and
\[
p>\max\{L_{\max},\sqrt B\},
\]
then each interval contains at most one multiple of \(p\), so
\[
0\le v_p(P)\le r.
\]
Hence, for a \(q\)-th power with \(q>r\), every such valuation must be zero.

This is a correct large-base carry principle, but it is insufficient because the rightmost interval may be an arbitrarily short additive interval relative to \(B\), even while its absolute length tends to infinity.

#### Corollary 2: A terminal interval occupying the upper half is decisive

Suppose the rightmost interval is \([a,B]\) and
\[
a\le \left\lfloor\frac B2\right\rfloor+1,
\]
equivalently its length is at least \(\lceil B/2\rceil\). Then \(P\) is not a perfect power.

#### Proof

By Bertrand’s postulate, with the cases \(B\le3\) checked directly, there is a prime
\[
\frac B2<p\le B.
\]
The condition on \(a\) puts this prime in \([a,B]\). It is the only positive multiple of \(p\) at most \(B\), and \(p^2>B\), so
\[
v_p(P)=1.
\]
Thus the gcd of all nonzero valuations is \(1\). ∎

This handles only configurations whose final block has positive relative size; it gives no endpoint-uniform threshold in terms of absolute block length.

---

### 3. Predetermined finite collections of bases can be neutralized

The following theorem gives a rigorous obstruction to any Route 3 argument that inspects only a finite set of prime bases bounded in terms of the lengths.

#### Theorem 3: Finite-base evasion

Let \(q\ge2\), let \(\ell\ge1\), and let \(S\) be any finite set of primes. There exist \(q\) pairwise disjoint positive intervals \(I_1,\dots,I_q\), each of length \(\ell\), such that

1. for every \(p\in S\),
   \[
   v_p\left(\prod_{i=1}^q\prod_{m\in I_i}m\right)\equiv0\pmod q;
   \]
2. the total product is nevertheless not a perfect power; indeed, some prime has total valuation exactly \(1\).

#### Proof

For each \(p\in S\), choose \(T_p\) such that
\[
p^{T_p}>\ell,
\]
and put
\[
M=\prod_{p\in S}p^{T_p},
\]
with \(M=1\) if \(S=\varnothing\).

Choose a prime \(P>\ell\) with \(P\notin S\). By the Chinese remainder theorem, there is an integer \(x_1\) satisfying
\[
x_1\equiv0\pmod M,\qquad
x_1\equiv P-1\pmod{P^2}.
\tag{7}
\]
Choose \(x_2,\dots,x_q\), all divisible by \(MP^2\), sufficiently large and sufficiently spaced that
\[
x_i+\ell\le x_{i+1}.
\]
Set
\[
I_i=[x_i+1,x_i+\ell].
\]

Fix \(p\in S\). Since \(p^{T_p}\mid x_i\) and \(p^{T_p}>\ell\), for every \(1\le j\le\ell\),
\[
v_p(x_i+j)=v_p(j).
\tag{8}
\]
Indeed, if \(u=v_p(j)<T_p\), then
\[
\frac{x_i+j}{p^u}
=
\frac{x_i}{p^u}+\frac{j}{p^u},
\]
where the first summand is divisible by \(p\) and the second is not. Thus the sum is not divisible by \(p\).

It follows from (8) that
\[
v_p\left(\prod_{m\in I_i}m\right)=v_p(\ell!)
\]
for every \(i\), and hence the total valuation is
\[
q\,v_p(\ell!)\equiv0\pmod q.
\]

Now consider the prime \(P\). From (7),
\[
x_1+1\equiv P\pmod{P^2},
\]
so
\[
v_P(x_1+1)=1.
\]
For \(2\le j\le\ell<P\),
\[
x_1+j\equiv j-1\not\equiv0\pmod P.
\]
For \(i\ge2\), \(P\mid x_i\), and hence
\[
x_i+j\equiv j\not\equiv0\pmod P
\qquad(1\le j\le\ell<P).
\]
Thus precisely one selected integer is divisible by \(P\), and it is divisible exactly once:
\[
v_P\left(\prod_{i=1}^q\prod_{m\in I_i}m\right)=1.
\]
The total product is therefore not any perfect power. ∎

In carry language, all the additions \(x_i+\ell\) have no carries in the bases \(p\in S\), while one deliberately chosen new base \(P\) has exactly one carry.

Taking \(S\) to be all primes at most an arbitrary function \(F(\ell)\) shows:

> There is no function depending only on the block length such that every nonpower configuration can be certified by a prime base below that function.

The prime witnessing nonpower may be forced beyond any prescribed finite range.

For example, with \(\ell=3\), \(S=\{2,3\}\), and \(q=2\), one can take \(M=36\), \(P=5\), \(x_1=504\), and \(x_2=900\). The two intervals are
\[
[505,507],\qquad[901,903].
\]
Their total \(2\)- and \(3\)-adic valuations are even, while \(505\) contributes \(v_5=1\) and no other selected integer is divisible by \(5\).

---

### 4. The square-binomial slice becomes a pure carry problem

Take
\[
I_1=[1,\ell],\qquad I_2=[n-\ell+1,n],
\qquad n\ge2\ell.
\]
Then
\[
P
=\ell!\frac{n!}{(n-\ell)!}
=(\ell!)^2\binom n\ell.
\tag{9}
\]
For every prime \(p\),
\[
v_p(P)
=
2v_p(\ell!)
+\kappa_p(n-\ell,\ell).
\tag{10}
\]
Therefore
\[
P\text{ is a square}
\quad\Longleftrightarrow\quad
\kappa_p(n-\ell,\ell)\equiv0\pmod2
\quad\text{for every prime }p.
\tag{11}
\]
Equivalently,
\[
P\text{ is a square}
\quad\Longleftrightarrow\quad
\binom n\ell\text{ is a square}.
\]

Thus the factorial contribution, which Route 3 hoped would supply rigidity, vanishes completely modulo \(2\) in this family. A carry-based proof of the \(r=2\) case must, among other things, establish
\[
\exists K\ \forall\ell\ge K\ \forall n\ge2\ell\
\exists p:\quad
\kappa_p(n-\ell,\ell)\ \text{is odd}.
\tag{12}
\]
Statement (12) is exactly the assertion that square binomial coefficients in the lower half of Pascal’s triangle have bounded lower index.

The known examples exhibit completely synchronized even carry chains:

- For \((n,\ell)=(9,2)\),
  \[
  \binom92=36=2^2 3^2.
  \]
  The addition \(7+2=9\) has two carries in base \(2\) and two carries in base \(3\).

- For \((n,\ell)=(50,3)\),
  \[
  \binom{50}{3}=19600=2^4 5^2 7^2.
  \]
  The addition \(47+3=50\) has four carries in base \(2\), two in base \(5\), and two in base \(7\).

These are not isolated failures of a numerical estimate: they are exact parity cancellations in every prime base.

---

### 5. A rigorous endpoint lower bound for power binomial coefficients

The following gives some genuine uniform information, though not enough to settle (12).

I use the classical Sylvester theorem:

> If \(k\) consecutive integers are all greater than \(k\), their product has a prime divisor greater than \(k\).

#### Proposition 4

Suppose
\[
n\ge2\ell,\qquad
\binom n\ell=y^q,\qquad q\ge2.
\]
Then
\[
n\ge(\ell+1)^q.
\tag{13}
\]

#### Proof

Consider the numerator
\[
A=(n-\ell+1)(n-\ell+2)\cdots n.
\]
Its \(\ell\) factors are all greater than \(\ell\). By Sylvester’s theorem, some prime \(p>\ell\) divides \(A\).

Since \(p>\ell\), the denominator \(\ell!\) is not divisible by \(p\). Moreover, at most one of the \(\ell\) consecutive factors in \(A\) is divisible by \(p\), because the difference between any two of them is less than \(p\). Let \(m\) be this unique factor.

Now
\[
0<v_p\binom n\ell=v_p(m).
\]
Because \(\binom n\ell=y^q\), this valuation is a positive multiple of \(q\), and hence
\[
v_p(m)\ge q.
\]
Thus
\[
p^q\mid m,\qquad p^q\le m\le n.
\]
Since \(p\ge\ell+1\), this gives
\[
n\ge p^q\ge(\ell+1)^q.
\]
∎

In Kummer language, Sylvester supplies a base \(p>\ell\) with a positive carry chain. If the binomial coefficient is a \(q\)-th power, that chain must have length at least \(q\).

For the square-binomial interval construction, Proposition 4 gives
\[
n\ge(\ell+1)^2.
\tag{14}
\]
Consequently, the omitted gap between the two intervals has size
\[
n-2\ell\ge \ell^2+1.
\tag{15}
\]
Thus any unbounded square-binomial counterexample family necessarily lives in the regime where the block lengths are tiny relative to the endpoints and gaps. This is precisely the regime in which disjointness supplies almost no useful control on base-\(p\) digits.

More generally, if \(p>\ell\) divides \(\binom n\ell\), then it divides exactly one of the numerator factors, and
\[
\kappa_p(n-\ell,\ell)
=v_p(m).
\]
For a \(q\)-th power, every such positive carry chain has length divisible by \(q\). Equivalently, the part of every numerator factor supported on primes greater than \(\ell\) must itself be a \(q\)-th power.

---

### 6. Why the straightforward induction on components fails

For a prime \(q\), let
\[
V_q(I)=
\left(
v_p\left(\prod_{m\in I}m\right)\bmod q
\right)_p.
\]
Removing the last component from a putative \(q\)-th power gives
\[
V_q(I_1)+\cdots+V_q(I_{r-1})=-V_q(I_r).
\]
An induction hypothesis saying that neither side is zero gives no contradiction: two nonzero vectors can be negatives of one another.

This cancellation occurs exactly in the known examples. Modulo \(2\),
\[
\prod_{m=1}^2m=2
\]
has parity vector supported only at \(2\), while
\[
8\cdot9=2^3 3^2
\]
has the same parity vector. Their sum is zero.

Likewise,
\[
1\cdot2\cdot3=2\cdot3,
\]
whereas
\[
48\cdot49\cdot50
=2^5\cdot3\cdot5^2\cdot7^2,
\]
so the two blocks again have identical parity vectors. No prime coordinate is private to the extreme interval modulo \(2\).

These finite examples do not disprove a sufficiently-large-length separation theorem, but the square-binomial reduction shows that proving such a theorem uniformly would already settle the unresolved assertion (12).

---

### Ledger

**Proved here**

1. The exact carry decomposition (1) and digit-sum identity (3).
2. The square-root localization formula (5).
3. The resulting high-prime exclusion for a \(q\)-th power.
4. Nonpower when the terminal interval occupies the upper half of the ambient range.
5. The finite-base evasion theorem, including a forced valuation-one prime outside any prescribed finite set.
6. The exact pure-carry characterization (11) of the square-binomial family.
7. Using classical Sylvester, the bound
   \[
   \binom n\ell=y^q,\ n\ge2\ell
   \Longrightarrow n\ge(\ell+1)^q.
   \]

**Plausible but unproved**

1. The carry assertion (12), equivalently boundedness of the lower index of square binomial coefficients.
2. A bounded-component allocation theorem forcing some aggregate carry count to be nonzero modulo \(q\).
3. An induction lemma separating the valuation vector of an extreme long block from every union of \(r-1\) other long blocks.

**Dead ends**

1. **Predetermined small bases:** rigorously defeated by Theorem 3.
2. **A private coordinate for the extreme interval:** defeated in its naive form by the two known square examples.
3. **Only using primes above \(\sqrt B\):** gives clean incidence counts but fails when all blocks are short relative to \(B\).
4. **Using only factorial rigidity:** in the square-binomial slice the factorial terms are doubled and disappear modulo \(2\).

## Self-Audit

1. **Proposition 4 invokes Sylvester’s theorem rather than reproving it.** This is a genuine external input, but it is a classical unconditional theorem explicitly within the large-prime context of the brief. All deductions from it are proved in full.

2. **The finite-base evasion theorem does not defeat an adaptive argument that chooses primes after seeing the endpoints.** I use it only to rule out proofs based on a finite prime range depending solely on the lengths. Its construction and that limited conclusion are exact.

3. **The induction obstruction examples have lengths only \(2\) and \(3\).** They refute only naive “private carry” or “nonzero blocks cannot cancel” claims, not a possible asymptotic separation lemma. The actual asymptotic block is instead the exact square-binomial carry assertion (12).

## Computations To Verify

```python
from math import comb, isqrt, gcd

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return [p for p in range(2, n + 1) if sieve[p]]

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def next_prime_strict(n):
    m = n + 1
    while not is_prime(m):
        m += 1
    return m

def vp_factorial(n, p):
    ans = 0
    while n:
        n //= p
        ans += n
    return ans

def vp_interval(a, b, p):
    ans = 0
    d = p
    while d <= b:
        ans += b // d - (a - 1) // d
        d *= p
    return ans

def kummer_by_valuations(n, k, p):
    return vp_factorial(n, p) - vp_factorial(k, p) - vp_factorial(n-k, p)

def kummer_by_digits(n, k, p):
    x = n - k
    carry = 0
    count = 0
    while x or k or carry:
        z = (x % p) + (k % p) + carry
        carry = int(z >= p)
        count += carry
        x //= p
        k //= p
    return count

# Verify the exact interval/carry decomposition.
for x in range(0, 100):
    for ell in range(1, 30):
        for p in primes_upto(x + ell):
            lhs = vp_interval(x + 1, x + ell, p)
            rhs = vp_factorial(ell, p) + kummer_by_digits(x + ell, ell, p)
            assert lhs == rhs
            assert kummer_by_digits(x + ell, ell, p) == \
                   kummer_by_valuations(x + ell, ell, p)

# Known carry patterns.
assert [(p, kummer_by_digits(9, 2, p))
        for p in primes_upto(9)
        if kummer_by_digits(9, 2, p)] == [(2, 2), (3, 2)]

assert [(p, kummer_by_digits(50, 3, p))
        for p in primes_upto(50)
        if kummer_by_digits(50, 3, p)] == [(2, 4), (5, 2), (7, 2)]

# Search square binomial coefficients.
def square_binomial_search(L, N):
    hits = []
    for ell in range(2, L + 1):
        for n in range(2*ell, N + 1):
            z = comb(n, ell)
            y = isqrt(z)
            if y*y == z:
                hits.append((n, ell, y))
                # Computational check of Proposition 4 for q=2.
                assert n >= (ell + 1)**2
    return hits

hits = square_binomial_search(20, 10000)
assert (9, 2, 6) in hits
assert (50, 3, 140) in hits
print(hits)

# Construct the finite-base evasion configuration.
def finite_base_evasion(ell, S, q):
    S = sorted(set(S))
    M = 1
    for p in S:
        pp = p
        while pp <= ell:
            pp *= p
        M *= pp

    P = next_prime_strict(max([ell] + S))

    # x1 = M*t == P-1 mod P^2
    modulus = P*P
    t = ((P - 1) * pow(M, -1, modulus)) % modulus
    x1 = M*t

    step = M*modulus
    x2 = ((x1 + ell + step - 1)//step)*step
    xs = [x1]
    for i in range(1, q):
        xs.append(x2 + (i - 1)*step)

    intervals = [(x + 1, x + ell) for x in xs]

    for i in range(q - 1):
        assert intervals[i][1] < intervals[i+1][0]

    for p in S:
        total = sum(vp_interval(a, b, p) for a, b in intervals)
        assert total % q == 0
        for a, b in intervals:
            assert vp_interval(a, b, p) == vp_factorial(ell, p)

    assert sum(vp_interval(a, b, P) for a, b in intervals) == 1
    return intervals, P

print(finite_base_evasion(3, [2, 3], 2))
# One valid output is equivalent to:
# intervals [(505, 507), (901, 903)], witness prime 5.

# Verify square-root localization on bounded configurations.
def verify_large_prime_localization(intervals):
    B = max(b for a, b in intervals)
    for p in primes_upto(B):
        if p*p > B:
            lhs = sum(vp_interval(a, b, p) for a, b in intervals)
            rhs = sum(b//p - (a-1)//p for a, b in intervals)
            assert lhs == rhs

verify_large_prime_localization([(1, 3), (48, 50)])

# Squarefree-kernel collision search for two equal-length intervals.
def parity_signature(a, ell, primes):
    return tuple(
        p for p in primes
        if vp_interval(a, a + ell - 1, p) % 2
    )

def collision_search(max_ell, max_endpoint):
    primes = primes_upto(max_endpoint)
    out = []
    for ell in range(2, max_ell + 1):
        first = {}
        for a in range(1, max_endpoint - ell + 2):
            sig = parity_signature(a, ell, primes)
            if sig in first and first[sig] + ell - 1 < a:
                out.append((ell, first[sig], a, sig))
                break
            first.setdefault(sig, a)
    return out

print(collision_search(10, 200))
# This should find, among others, length 2 starts 1 and 8,
# and length 3 starts 1 and 48.
```

## Route Diagnosis

The factorial/Kummer route works cleanly at the level of exact identities but does not presently supply the necessary global noncancellation theorem. Disjointness gives inequalities between endpoints but no usable control over their residues modulo prime powers; Theorem 3 makes this obstruction explicit by neutralizing any prescribed finite collection of bases through CRT. Large bases become simple incidence coordinates, but arbitrary long intervals can still be negligible relative to their endpoints, so no prime is guaranteed in the relevant additive ranges.

The decisive block is the family
\[
[1,\ell],\qquad[n-\ell+1,n].
\]
For squares, all factorial valuations disappear modulo \(2\), leaving exactly the carry parity problem for \(\binom n\ell\). Any complete affirmative treatment of Route 3 must prove the unresolved statement (12), or prove a stronger theorem that contains it. This is an unproved problem of comparable strength, so the route is BLOCKED rather than merely incomplete.

A fresh attempt should seek a genuinely global, endpoint-adaptive prime-allocation theorem. The most concrete target is to exploit the fact that, if \(\binom n\ell\) is a \(q\)-th power, every prime \(p>\ell\) appearing in the numerator occurs to exponent divisible by \(q\) in one individual numerator term. One would need to show uniformly that a long run cannot have all of its \(\ell\)-rough parts be \(q\)-th powers in the required manner. Existing carry identities, finite-base analysis, and elementary large-prime localization do not achieve this. Route 4 is essentially the same obstruction in valuation-vector language, while Route 6—searching for unbounded square-binomial or squarefree-kernel collision families—remains the clearest possible route to a disproof.