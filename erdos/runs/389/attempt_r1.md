STATUS: BLOCKED
## Result

I did not resolve Erdős Problem #389. I proved several structural results that sharply constrain Route 1. Most importantly, every nontrivial candidate \(x=m+k>m\) necessarily has a negative prime-power floor contribution \(e_{p^a}(m,k)=-1\); hence every genuine solution must use cancellation between different powers of the same prime. Finite sets of primes can be controlled by stable base-\(p\) residue conditions and CRT, but the simplest no-carry construction necessarily creates a new uncontrolled prime with a negative level. I also proved a quantitative necessary condition on \(v_p(x)\), an exact large-prime obstruction implying that roughly the last \(m/2\) integers before \(x\) must be \(\sqrt{2x}\)-smooth, and that the Gaussian-binomial strengthening is impossible for every \(m>0\).

## Complete Argument

The case \(m=0\) is already settled, since
\[
R_0(k)=\binom{2k}{k}\in\mathbb Z.
\]
Throughout the rest, assume
\[
m\ge1,\qquad k\ge1,\qquad x:=m+k>m,\qquad N:=2x-m=m+2k.
\]

For every integer \(d\ge2\), put
\[
e_d(m,x):=
\left\lfloor\frac{2x-m}{d}\right\rfloor
+\left\lfloor\frac md\right\rfloor
-2\left\lfloor\frac xd\right\rfloor.
\]
Thus for every prime \(p\),
\[
v_p(R_m(k))=\sum_{a\ge1}e_{p^a}(m,x).
\]

### 1. Exact residue formula for each valuation level

**Lemma 1.** If
\[
r:=x\bmod d,\qquad s:=m\bmod d,
\]
then
\[
\boxed{e_d(m,x)=\left\lfloor\frac{2r-s}{d}\right\rfloor.}
\]
Consequently \(e_d\in\{-1,0,1\}\), with
\[
e_d=-1\iff 2r<s,
\]
and
\[
e_d=1\iff 2r\ge d+s.
\]

**Proof.** Write
\[
x=qd+r,\qquad m=ad+s,
\]
where \(0\le r,s<d\). Then
\[
2x-m=(2q-a)d+(2r-s),
\]
so
\[
\left\lfloor\frac{2x-m}{d}\right\rfloor
=2q-a+\left\lfloor\frac{2r-s}{d}\right\rfloor.
\]
Substituting this and \(\lfloor m/d\rfloor=a\), \(\lfloor x/d\rfloor=q\) into the definition of \(e_d\) proves the formula. Since
\[
-d<2r-s<2d,
\]
its floor after division by \(d\) lies in \(\{-1,0,1\}\), and the stated characterizations follow. ∎

This formula exposes exactly where cross-level \(p\)-adic cancellation is needed.

---

### 2. A negative prime-power level is unavoidable

**Theorem 2.** For every \(m\ge1\) and every \(x>m\), there is a prime \(p\) and an exponent \(a\ge1\) such that
\[
e_{p^a}(m,x)=-1.
\]

More precisely, there is a prime \(p\) satisfying
\[
v_p(x)>v_p(m),
\]
and for every integer \(j\) with
\[
v_p(m)<j\le v_p(x),
\]
one has
\[
e_{p^j}(m,x)=-1.
\]

**Proof.** If \(v_p(x)\le v_p(m)\) for every prime \(p\), then \(x\mid m\), which is impossible because \(x>m\). Hence there is a prime \(p\) with
\[
a:=v_p(x)>b:=v_p(m).
\]

For \(b<j\le a\), the number \(p^j\) divides \(x\), so
\[
x\bmod p^j=0.
\]
But \(p^j\nmid m\), so
\[
s:=m\bmod p^j
\]
satisfies \(1\le s<p^j\). Lemma 1 therefore gives
\[
e_{p^j}(m,x)
=\left\lfloor\frac{-s}{p^j}\right\rfloor=-1.
\]
∎

Thus the stronger requirement
\[
e_{p^a}(m,x)\ge0\qquad\text{for every prime power }p^a
\]
has no solutions at all for \(m>0\). Every ordinary solution must compensate one or more negative levels by positive contributions at other powers of the same prime.

This is not merely an artifact of composite moduli.

---

### 3. Quantitative compensation constraint

The preceding unavoidable negative contributions give a useful necessary condition.

**Theorem 3.** Suppose \(R_m(k)\) is integral. Let \(p\) be a prime and put
\[
a:=v_p(x),\qquad b:=v_p(m).
\]
If \(a>b\), then
\[
\boxed{2a-b\le \left\lfloor\log_p(2x-m)\right\rfloor.}
\]
Equivalently,
\[
\boxed{p^{\,2a-b}\le 2x-m.}
\]

Moreover, at least \(a-b\) exponents \(j>a\) must satisfy
\[
2(x\bmod p^j)\ge p^j+(m\bmod p^j),
\]
i.e. \(e_{p^j}=1\).

**Proof.** By Theorem 2, the levels
\[
j=b+1,b+2,\ldots,a
\]
contribute \(a-b\) copies of \(-1\).

Let
\[
L:=\left\lfloor\log_p(2x-m)\right\rfloor.
\]
For \(j>L\), one has \(p^j>2x-m\), and therefore \(e_{p^j}=0\). For \(j\le a\), the residue of \(x\) modulo \(p^j\) is zero, so Lemma 1 shows that \(e_{p^j}\le0\). Thus all positive contributions must occur among
\[
j=a+1,\ldots,L.
\]
There are at most \(L-a\) such exponents, and each contributes at most \(1\). Since integrality requires
\[
\sum_{j\ge1}e_{p^j}\ge0,
\]
there must be at least \(a-b\) positive levels. Hence
\[
a-b\le L-a,
\]
which is the asserted inequality
\[
2a-b\le L.
\]
The residue condition for a positive level follows directly from Lemma 1. ∎

A particularly clean consequence is the following.

**Corollary 4.** If \(m\ge1\) and \(x=m+k\) is a prime power, then \(R_m(k)\) is not integral.

**Proof.** Suppose \(x=p^a\). Since \(m<x\),
\[
b:=v_p(m)<a.
\]
Theorem 3 would require
\[
p^{2a-b}\le 2p^a-m<2p^a.
\]
But \(2a-b\ge a+1\), so
\[
p^{2a-b}\ge p^{a+1}\ge2p^a,
\]
a contradiction. ∎

For example:

- \(m=1,x=4\), corresponding to \(k=3\), fails at \(p=2\);
- \(m=3,x=9\), corresponding to \(k=6\), fails at \(p=3\).

Theorem 3 also explains the successful case \(m=1,x=6\): for the excess prime factors \(2\) and \(3\), one has
\[
2^2\le11,\qquad 3^2\le11,
\]
so compensating higher powers are at least available. Indeed,
\[
e_2=-1,\quad e_8=1,
\]
and
\[
e_3=-1,\quad e_9=1.
\]

---

### 4. The Gaussian-binomial strengthening is universally impossible

The attack brief suggested testing the stronger condition \(e_d\ge0\) for every \(d\). It cannot work for any nonzero \(m\).

**Corollary 5.** For every \(m\ge1\) and every \(k\ge1\), the Gaussian-binomial quotient
\[
\frac{\binom{m+2k}{k}_q}{\binom{m+k}{k}_q}
\]
is not a polynomial in \(\mathbb Z[q]\).

**Proof.** Take \(d=x=m+k\). Since \(0<m<x\),
\[
e_x(m,x)
=
\left\lfloor\frac{2x-m}{x}\right\rfloor
+\left\lfloor\frac mx\right\rfloor
-2
=1+0-2=-1.
\]
Thus the cyclotomic exponent at \(\Phi_x(q)\) is negative. ∎

Therefore Route 2 is not just too rigid in some examples: it has no nontrivial instances whatsoever.

---

### 5. Exact large-prime endpoint obstruction

Let
\[
h:=\left\lceil\frac m2\right\rceil.
\]

**Theorem 6.** Let \(p\) be a prime satisfying
\[
p>m,\qquad p^2>2x-m.
\]
Then
\[
v_p(R_m(k))=-1
\]
if and only if
\[
p\mid x-r
\]
for some
\[
r\in\{0,1,\ldots,h-1\}.
\]

Equivalently,
\[
v_p(R_m(k))=-1
\iff
2(x\bmod p)<m.
\]

**Proof.** Since \(p^2>2x-m\), all levels \(p^a\) with \(a\ge2\) exceed \(2x-m\) and contribute zero. Therefore
\[
v_p(R_m(k))=e_p(m,x).
\]
Because \(p>m\), one has \(m\bmod p=m\). Writing \(r=x\bmod p\), Lemma 1 gives
\[
v_p(R_m(k))
=\left\lfloor\frac{2r-m}{p}\right\rfloor.
\]
This equals \(-1\) precisely when \(2r<m\), namely when
\[
r\in\{0,\ldots,\lceil m/2\rceil-1\}.
\]
Since \(r<p\), the condition \(x\bmod p=r\) is equivalent to \(p\mid x-r\). ∎

**Corollary 7.** If \(R_m(k)\) is integral, then for every
\[
0\le r<\left\lceil\frac m2\right\rceil,
\]
every prime factor of \(x-r\) is at most
\[
\boxed{\max\{m,\sqrt{2x-m}\}.}
\]

Thus every solution requires the consecutive integers
\[
x,\ x-1,\ \ldots,\ x-\left\lceil\frac m2\right\rceil+1
\]
to be \(\max\{m,\sqrt{2x-m}\}\)-smooth.

This is only a necessary condition. Even a run of composite integers is insufficient. For instance, take
\[
m=3,\qquad x=10,\qquad k=7.
\]
Both \(x=10\) and \(x-1=9\) are composite, but
\[
v_5(R_3(7))
=
\left\lfloor\frac{17}{5}\right\rfloor
-2\left\lfloor\frac{10}{5}\right\rfloor
=3-4=-1.
\]
Here \(5\mid x\) and \(5^2>17\).

---

### 6. Stable finite-prime digit control

Finite collections of primes really can be controlled by CRT. The difficulty is preventing new primes from appearing.

For a prime \(p\), let \(C_{p,A}(u,v)\) denote the number of carries generated in the first \(A\) base-\(p\) positions when adding \(u\) and \(v\), including a carry generated from position \(A-1\) into position \(A\).

**Lemma 8.** Let \(q=p^A>m\), and suppose
\[
0\le r<q-m.
\]
If
\[
C_{p,A}(r,r+m)\ge C_{p,A}(r,m),
\]
then every sufficiently large integer \(k\) satisfying
\[
k\equiv r\pmod q
\]
obeys
\[
c_p(k,m+k)\ge c_p(k,m).
\]

**Proof.** Write
\[
k=tq+r.
\]
Because \(r+m<q\),
\[
m+k=tq+(r+m),
\]
with no carry from the lower \(A\) digits into the higher digits.

In the addition \(k+m\), all carries occur among the lower \(A\) digits and their number is exactly
\[
C_{p,A}(r,m).
\]
Above those digits one is merely adding the base-\(p\) digits of \(t\) to zeros.

In the addition \(k+(m+k)\), the first \(A\) digits generate exactly
\[
C_{p,A}(r,r+m)
\]
carries. The higher digits may create additional carries, but cannot erase carries already counted. Hence
\[
c_p(k,m+k)\ge C_{p,A}(r,r+m)\ge C_{p,A}(r,m)=c_p(k,m).
\]
∎

The residue \(r=0\) is always admissible: then \(C_{p,A}(0,m)=0\). Consequently:

**Corollary 9.** Given any finite set \(S\) of primes, choose \(A_p\) so that \(p^{A_p}>m\), and put
\[
M_S:=\prod_{p\in S}p^{A_p}.
\]
Every positive multiple \(k\) of \(M_S\) satisfies
\[
v_p(R_m(k))\ge0\qquad(p\in S).
\]

**Proof.** In base \(p\), such a \(k\) has at least \(A_p\) trailing zero digits, while \(m<p^{A_p}\). Thus adding \(k+m\) creates no carries at all:
\[
c_p(k,m)=0.
\]
Kummer then gives
\[
v_p(R_m(k))=c_p(k,m+k)\ge0.
\]
∎

This proves the finite simultaneous digit-control part of Route 1.

---

### 7. Why the all-zero CRT construction necessarily exports a negative level

The finite construction cannot simply be enlarged until all primes are covered.

**Theorem 10.** In the setting of Corollary 9, let \(k\) be a positive multiple of \(M_S\) and put \(x=m+k\). Then there is a prime \(\ell\notin S\) such that
\[
v_\ell(x)>v_\ell(m).
\]
Consequently, at the prime-power level
\[
\ell^{v_\ell(m)+1},
\]
one has
\[
e_{\ell^{v_\ell(m)+1}}(m,x)=-1.
\]

**Proof.** For \(p\in S\), write \(b=v_p(m)\). Since \(p^{A_p}>m\), one has \(b<A_p\). Because \(p^{A_p}\mid k\),
\[
x=m+k\equiv m\pmod{p^{A_p}},
\]
and therefore
\[
v_p(x)=v_p(m)=b.
\]

On the other hand, because \(x>m\), it cannot be true that
\[
v_q(x)\le v_q(m)
\]
for every prime \(q\), since that would imply \(x\mid m\). Thus some prime \(\ell\) satisfies
\[
v_\ell(x)>v_\ell(m).
\]
It cannot lie in \(S\), by the preceding equality. The final assertion follows from Theorem 2. ∎

This does **not** prove that the new prime \(\ell\) is a total obstruction: its negative level may be canceled at a higher \(\ell\)-power. For example,
\[
m=1,\qquad k=14,\qquad x=15
\]
is a solution:
\[
\binom{15}{14}=15\mid\binom{29}{14}.
\]
Nevertheless, \(e_3=e_5=-1\); these are compensated by positive contributions at higher powers:
\[
e_9=1,\quad e_{27}=1,\qquad e_{25}=1.
\]

Thus the precise circularity is:

1. finite CRT can control any prescribed primes;
2. a positive solution cannot avoid denominator carries for every prime;
3. an all-zero CRT stage necessarily creates a new negative prime-power level;
4. success depends on arranging higher-power compensation for the new prime, whose identity depends on the newly enlarged \(k\).

That last step remains uncontrolled.

---

### 8. Ledger

#### Proved lemmas

1. The exact residue identity
   \[
   e_d=\left\lfloor\frac{2(x\bmod d)-(m\bmod d)}d\right\rfloor.
   \]
2. Every \(x>m\) has at least one negative prime-power level.
3. Every solution necessarily satisfies
   \[
   p^{2v_p(x)-v_p(m)}\le2x-m
   \]
   whenever \(v_p(x)>v_p(m)\).
4. No prime power \(x=m+k\) can be a solution.
5. The Gaussian-binomial strengthening has no solutions for any \(m>0\).
6. Exact classification of all large one-level obstruction primes.
7. Necessary simultaneous smoothness of the last \(\lceil m/2\rceil\) integers up to \(x\).
8. Stable finite-prime carry control by local residue conditions and CRT.
9. The all-zero CRT construction necessarily creates a new uncontrolled negative level.

#### Plausible but unproved

1. For fixed \(m\), there may be infinitely many \(x\) satisfying the necessary simultaneous smoothness condition from Corollary 7.
2. A successful construction might pair every negative level \(p^a\) with a higher positive level \(p^b\), using balanced factorizations of the integers \(x-r\).
3. More flexible safe residues from Lemma 8 may be substantially more useful than the residue \(0\), but no self-consistent choice controlling all primes has been found.

None of these claims is sufficient for the original problem, and none is asserted as a theorem.

#### Dead ends

1. **Levelwise nonnegativity:** impossible by Theorem 2.
2. **Gaussian-binomial positivity:** impossible because \(e_x=-1\).
3. **Choosing \(x\) to be a prime power:** impossible by Corollary 4.
4. **Merely forcing a composite endpoint interval:** insufficient; \(m=3,x=10\) is an explicit counterexample.
5. **Fixed dilation \(k=(A-1)m\):** no fixed \(A\ge2\) works for all \(m\). Indeed the corresponding Landau floor function is
   \[
   F_A(t)=\lfloor(2A-1)t\rfloor+\lfloor t\rfloor-2\lfloor At\rfloor.
   \]
   For \(t=1/A+\varepsilon\), with sufficiently small \(\varepsilon>0\),
   \[
   F_A(t)=1+0-2=-1.
   \]
6. **All-zero finite CRT followed by adding more primes:** each stage necessarily exports a new negative level outside the controlled set.

## Self-Audit

1. **The finite-residue carry lemma has a subtle boundary at the \(A\)-th digit.** The proof explicitly requires \(r+m<p^A\), so no denominator carry exits the controlled block. Numerator carries above the block can only increase the numerator’s total, which is why the stated one-sided conclusion remains valid.

2. **The valuation bound in Theorem 3 counts only available positive levels, not their actual occurrence.** This makes it merely necessary, not sufficient. The argument is nevertheless rigorous because the \(a-b\) forced negative levels must be offset by at least that many \(+1\) levels, and there are at most \(L-a\) places where those can occur.

3. **The claim that Route 1 is blocked is a diagnosis, not an impossibility theorem for all conceivable carry constructions.** A more sophisticated multiplicative construction could conceivably coordinate the newly introduced primes. What is proved is that the natural finite-prime/no-carry CRT strategy cannot close without a new theorem controlling higher-power compensation for primes arising from the factorization of \(x,x-1,\ldots\).

## Computations To Verify

The following Python uses exact arithmetic and `sympy`.

```python
from math import comb
from sympy import primerange, factorint
from sympy.ntheory.modular import crt

def vp_int(n, p):
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a

def e_level(m, x, d):
    return (2*x - m)//d + m//d - 2*(x//d)

def e_level_residue(m, x, d):
    return (2*(x % d) - (m % d)) // d

def D(m, x, p):
    """v_p(R_m(x-m))."""
    N = 2*x - m
    q = p
    ans = 0
    while q <= N:
        ans += e_level(m, x, q)
        q *= p
    return ans

def carries(a, b, p):
    total = 0
    carry = 0
    while a or b:
        s = (a % p) + (b % p) + carry
        if s >= p:
            total += 1
            carry = 1
        else:
            carry = 0
        a //= p
        b //= p
    return total

def carries_A(a, b, p, A):
    """Carries generated in positions 0,...,A-1."""
    total = 0
    carry = 0
    for _ in range(A):
        s = (a % p) + (b % p) + carry
        if s >= p:
            total += 1
            carry = 1
        else:
            carry = 0
        a //= p
        b //= p
    return total

def is_solution(m, k):
    x = m + k
    N = 2*x - m
    return all(D(m, x, p) >= 0 for p in primerange(2, N + 1))

# 1. Verify the residue formula.
for m in range(1, 40):
    for x in range(m + 1, 150):
        for d in range(2, 2*x - m + 2):
            assert e_level(m, x, d) == e_level_residue(m, x, d)

# 2. Verify Legendre against Kummer.
for m in range(1, 30):
    for k in range(1, 100):
        x = m + k
        for p in primerange(2, 2*x - m + 1):
            assert D(m, x, p) == carries(k, x, p) - carries(k, m, p)

# 3. Verify unavoidable negative levels.
for m in range(1, 50):
    for x in range(m + 1, 300):
        found = False
        fm = factorint(m)
        for p, a in factorint(x).items():
            b = fm.get(p, 0)
            if a > b:
                assert e_level(m, x, p**(b + 1)) == -1
                found = True
                break
        assert found

# 4. Verify the necessary exponent bound on all solutions in a finite box.
for m in range(1, 30):
    for k in range(1, 500):
        if not is_solution(m, k):
            continue
        x = m + k
        N = 2*x - m
        fm = factorint(m)
        for p, a in factorint(x).items():
            b = fm.get(p, 0)
            if a > b:
                assert p**(2*a - b) <= N

# 5. Verify prime-power x never works in a finite range.
for p in list(primerange(2, 50)):
    x = p
    while x <= 10000:
        for m in range(1, min(x, 100)):
            assert not is_solution(m, x - m)
        x *= p

# 6. Verify the exact large-prime obstruction.
for m in range(1, 30):
    h = (m + 1)//2
    for x in range(m + 1, 500):
        N = 2*x - m
        for p in primerange(m + 1, x + 1):
            if p*p > N:
                endpoint_hit = any((x - r) % p == 0 for r in range(h))
                assert (D(m, x, p) == -1) == endpoint_hit

# 7. Enumerate safe residues from Lemma 8.
def safe_residues(m, p, A):
    q = p**A
    assert q > m
    out = []
    for r in range(q - m):
        den = carries_A(r, m, p, A)
        num = carries_A(r, r + m, p, A)
        if num >= den:
            out.append(r)
    return out

# Test robustness for many extensions.
for m in range(1, 15):
    for p in list(primerange(2, 20)):
        A = 1
        while p**A <= m:
            A += 1
        q = p**A
        for r in safe_residues(m, p, A):
            for t in range(40):
                k = t*q + r
                if k >= 1:
                    x = m + k
                    assert D(m, x, p) >= 0

# 8. Test the all-zero CRT escape.
def zero_crt_experiment(m, Y):
    S = list(primerange(2, Y + 1))
    M = 1
    for p in S:
        q = p
        while q <= m:
            q *= p
        M *= q
    k = M
    x = m + k

    fm = factorint(m)
    excess = [
        p for p, a in factorint(x).items()
        if a > fm.get(p, 0)
    ]
    assert excess
    assert all(p not in S for p in excess)

    for p in excess:
        b = fm.get(p, 0)
        assert e_level(m, x, p**(b + 1)) == -1

    return M, x, excess

for m in range(1, 10):
    for Y in (2, 3, 5, 7, 11):
        zero_crt_experiment(m, Y)

# 9. Explicit examples mentioned above.
assert is_solution(1, 5)
assert is_solution(1, 14)
assert is_solution(2, 4)
assert not is_solution(3, 7)   # x=10, obstructed by p=5

assert comb(29, 14) % 15 == 0
assert D(3, 10, 5) == -1

# 10. Search for compensation profiles.
def profile(m, k):
    x = m + k
    N = 2*x - m
    data = {}
    for p in primerange(2, N + 1):
        levels = []
        q = p
        while q <= N:
            val = e_level(m, x, q)
            if val:
                levels.append((q, val))
            q *= p
        if levels:
            data[p] = (sum(v for _, v in levels), levels)
    return data

print(profile(1, 5))
print(profile(1, 14))
```

A particularly useful larger computation would, for each successful or near-successful \(x\), store every forced negative level \(p^a\), the higher \(p^b\) levels compensating it, and the factorizations of
\[
x,\ x-1,\ldots,x-\left\lceil\frac m2\right\rceil+1.
\]

## Route Diagnosis

Route 1 succeeds completely for any prescribed finite collection of primes: stable digit patterns can be imposed by congruences, and CRT combines them. The route fails at the archimedean closure step. Enlarging the CRT modulus enlarges \(k\), introduces new prime divisors of \(x=m+k\) and nearby endpoint integers, and necessarily creates a new negative prime-power level. The new prime is harmless only if a higher power lands in the correct residue range, a condition not controlled by the preceding CRT stage.

The strongest simple alternatives are also blocked or dead. Gaussian-binomial positivity is impossible for all \(m>0\); prime-power choices of \(x\) are impossible; and ordinary composite runs do not eliminate large prime-factor obstructions. A fresh attempt should therefore focus on a multiplicative construction of \(x\), not merely congruence control of \(k\): construct the endpoint integers \(x-r\) with balanced factorizations and simultaneously arrange explicit pairings
\[
e_{p^a}=-1\quad\longleftrightarrow\quad e_{p^b}=1,\qquad b>a.
\]
Absent a theorem providing such simultaneous prime-power compensation, Route 1 remains blocked.