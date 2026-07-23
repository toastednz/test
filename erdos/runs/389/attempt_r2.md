STATUS: BLOCKED

## Result

Route 2 is impossible for every nontrivial parameter \(m>0\): writing \(x=m+k\), the cyclotomic exponent at the automatically available index \(d=x\) is always
\[
e_x(m,k)=-1.
\]
Thus the Gaussian-binomial quotient is never a polynomial for any \(k\) when \(m>0\). In fact, if \(g=\gcd(m,x)\), its reduced cyclotomic denominator contains
\[
\frac{q^x-1}{q^g-1},
\]
of degree \(x-g\). Even the weaker repair requiring \(e_{p^a}\ge0\) only at prime powers fails for \(m=1\), so cancellation between different powers of the same prime is essential. I also prove exact residue, forced-denominator, prime-power capacity, and large-prime localization lemmas. These do not establish the original Erdős–Straus assertion; the route is therefore blocked rather than solved.

## Complete Argument

### 1. Exact residue form of the cyclotomic exponent

Put
\[
x=m+k,
\qquad x>m,
\qquad N=2x-m=m+2k.
\]
Then
\[
R_m(k)=\frac{N!\,m!}{x!^2}.
\]
For \(d\ge2\), the relevant cyclotomic exponent is
\[
e_d(m,x)
=
\left\lfloor\frac{2x-m}{d}\right\rfloor
+
\left\lfloor\frac m d\right\rfloor
-
2\left\lfloor\frac x d\right\rfloor.
\]

Write
\[
x=bd+r,\qquad m=ad+s,
\qquad 0\le r,s<d.
\]
Then
\[
2x-m=(2b-a)d+(2r-s),
\]
and consequently
\[
\begin{aligned}
e_d(m,x)
&=2b-a+\left\lfloor\frac{2r-s}{d}\right\rfloor+a-2b\\
&=\boxed{\left\lfloor\frac{2(x\bmod d)-(m\bmod d)}d\right\rfloor}.
\end{aligned}
\]

Since
\[
-(d-1)\le 2r-s\le 2d-2,
\]
one always has
\[
e_d(m,x)\in\{-1,0,1\}.
\]
In particular,
\[
e_d(m,x)\ge0
\quad\Longleftrightarrow\quad
2(x\bmod d)\ge m\bmod d.
\]

This is the exact residue criterion underlying Route 2.

---

### 2. Decisive obstruction to Route 2

Suppose \(m>0\). Since \(x>m\), at \(d=x\) one has
\[
x\bmod x=0,\qquad m\bmod x=m.
\]
Therefore
\[
e_x(m,x)
=
\left\lfloor-\frac m x\right\rfloor
=-1.
\]

Equivalently, directly from the floor definition,
\[
e_x(m,x)
=
\left\lfloor\frac{2x-m}{x}\right\rfloor
+
\left\lfloor\frac m x\right\rfloor
-2\left\lfloor\frac x x\right\rfloor
=1+0-2=-1.
\]
Here \(d=x\ge2\) is a valid cyclotomic index and \(x\le N\).

Thus:

\[
\boxed{
m>0,\ x>m
\quad\Longrightarrow\quad
e_x(m,x)=-1.
}
\]

Hence, for every \(m>0\) and every \(k\ge1\),
\[
\frac{\binom{m+2k}{k}_q}{\binom{m+k}{k}_q}\notin\mathbb Z[q].
\]

The key lemma proposed by Route 2,
\[
\forall m\ge0\ \exists k\ge1\ \forall d\ge2,\qquad e_d(m,k)\ge0,
\]
is therefore false for every \(m>0\).

For completeness, \(m=0\) is different: then
\[
e_d(0,x)=\left\lfloor\frac{2(x\bmod d)}d\right\rfloor\ge0,
\]
as expected from the fact that the quotient is the Gaussian central binomial coefficient.

---

### 3. The Gaussian obstruction is much larger than one factor

Let
\[
g=\gcd(m,x).
\]
If \(d\mid x\), then \(x\bmod d=0\). Hence
\[
e_d(m,x)
=
\left\lfloor-\frac{m\bmod d}{d}\right\rfloor
=
\begin{cases}
0,&d\mid m,\\
-1,&d\nmid m.
\end{cases}
\]

Therefore every divisor \(d\mid x\) which does not divide \(m\) contributes a cyclotomic factor \(\Phi_d(q)\) to the reduced denominator.

Using
\[
q^t-1=\prod_{d\mid t}\Phi_d(q),
\]
and observing that the common divisors of \(m\) and \(x\) are exactly the divisors of \(g\), we obtain
\[
\prod_{\substack{d\mid x\\d\nmid m}}\Phi_d(q)
=
\frac{\prod_{d\mid x}\Phi_d(q)}
     {\prod_{d\mid g}\Phi_d(q)}
=
\boxed{\frac{q^x-1}{q^g-1}}.
\]

Thus, if the Gaussian quotient is written in reduced form \(P(q)/Q(q)\), then
\[
\boxed{\frac{q^x-1}{q^g-1}\mid Q(q)}.
\]
For \(m>0\), \(g\le m<x\), so this forced denominator has degree
\[
x-g\ge x-m=k.
\]
Route 2 is therefore not failing because of one isolated accidental index: the Gaussian quotient has a forced denominator of degree at least \(k\).

At \(q=1\),
\[
\lim_{q\to1}\frac{q^x-1}{q^g-1}=\frac{x}{g}.
\]
This does not obstruct ordinary integrality, because values at \(q=1\) of distinct cyclotomic factors can have common prime divisors.

---

### 4. Prime-power termwise positivity also fails

One might try to repair Route 2 by imposing positivity only at prime powers:
\[
e_{p^a}(m,x)\ge0
\qquad\text{for every prime power }p^a.
\]
This is still too strong.

If \(p\mid x\) but \(p\nmid m\), then
\[
x\bmod p=0,\qquad m\bmod p\ne0,
\]
so
\[
e_p(m,x)=-1.
\]
Consequently, prime-power termwise positivity would force
\[
\operatorname{rad}(x)\mid m.
\]

For \(m=1\), every \(x>1\) has a prime divisor not dividing \(m\). Thus:

\[
\boxed{
m=1,\ x>1
\quad\Longrightarrow\quad
e_p(1,x)=-1
\text{ for some prime }p.
}
\]

Hence even positivity at each individual prime-power level cannot prove the already-settled case \(m=1\). Cancellation between different powers \(p,p^2,\ldots\) is indispensable.

---

### 5. Exact illustration of essential cancellation

Take \(m=1\) and \(x=6\), corresponding to \(k=5\). Then \(N=11\), and
\[
R_1(5)=\frac{11!}{6!^2}=77.
\]

The nonzero cyclotomic exponents are
\[
e_2=e_3=e_6=-1,
\qquad
e_7=e_8=e_9=e_{10}=e_{11}=1.
\]
Thus the Gaussian quotient is
\[
\frac{\Phi_7(q)\Phi_8(q)\Phi_9(q)\Phi_{10}(q)\Phi_{11}(q)}
     {\Phi_2(q)\Phi_3(q)\Phi_6(q)}.
\]
It is not a polynomial. Nevertheless, at \(q=1\),
\[
\Phi_2(1)=2,\quad \Phi_3(1)=3,\quad \Phi_6(1)=1,
\]
while
\[
\Phi_8(1)=2,\quad \Phi_9(1)=3.
\]
The negative \(2\)-adic and \(3\)-adic contributions are canceled at higher powers:
\[
v_2(R_1(5))=e_2+e_4+e_8=-1+0+1=0,
\]
and
\[
v_3(R_1(5))=e_3+e_9=-1+1=0.
\]
The remaining factors give
\[
v_7(R_1(5))=v_{11}(R_1(5))=1,
\]
hence \(R_1(5)=7\cdot11=77\).

This shows concretely why cyclotomic positivity cannot merely be weakened slightly: the original problem fundamentally uses aggregation along each prime-power chain.

---

### 6. A forced prime-power capacity condition

Let \(m>0\), let \(p\) be prime, and put
\[
\alpha=v_p(x),\qquad \beta=v_p(m),
\]
and
\[
L=\max\{a:p^a\le N\}.
\]

If \(\alpha>\beta\), then for every
\[
\beta<a\le\alpha
\]
we have \(p^a\mid x\) but \(p^a\nmid m\), so
\[
e_{p^a}(m,x)=-1.
\]
There are \(\alpha-\beta\) such forced negative terms.

For \(a>\alpha\), each exponent is at most \(1\). There are only \(L-\alpha\) such levels available before \(p^a>N\). Therefore
\[
v_p(R_m(k))
=\sum_{a=1}^{L}e_{p^a}(m,x)
\le-(\alpha-\beta)+(L-\alpha).
\]
A necessary condition for \(v_p(R_m(k))\ge0\) is consequently
\[
L\ge 2\alpha-\beta.
\]
Equivalently,
\[
\boxed{
\alpha>\beta
\quad\Longrightarrow\quad
p^{\,2\alpha-\beta}\le 2x-m
}
\]
for every successful \(x\).

For \(m=1\), this says that if \(p^\alpha\Vert x\), then necessarily
\[
p^{2\alpha}\le2x-1.
\]
In particular, \(x\) cannot be a prime power.

This condition remains only necessary: the available higher powers must also occur with the correct residues to contribute \(+1\).

---

### 7. Complete prime-chain criterion when \(m=1\)

For \(m=1\), the residue formula simplifies to
\[
e_d(1,x)=\left\lfloor\frac{2(x\bmod d)-1}{d}\right\rfloor.
\]
Thus
\[
e_d(1,x)=-1
\quad\Longleftrightarrow\quad
x\bmod d=0
\quad\Longleftrightarrow\quad
d\mid x.
\]
Also,
\[
e_d(1,x)=1
\quad\Longleftrightarrow\quad
2(x\bmod d)\ge d+1.
\]

It follows that the reduced Gaussian denominator is exactly
\[
\prod_{\substack{d\mid x\\d>1}}\Phi_d(q)
=\frac{q^x-1}{q-1}=[x]_q.
\]

More importantly, if \(p^\alpha\Vert x\), then
\[
v_p(R_1(x-1))
=
-\alpha+
\#\left\{
a>\alpha:
p^a\le2x-1,\ 
2(x\bmod p^a)\ge p^a+1
\right\}.
\]
Primes not dividing \(x\) have no negative terms. Therefore
\[
\boxed{
R_1(x-1)\in\mathbb Z
}
\]
if and only if, for every \(p^\alpha\Vert x\),
\[
\#\left\{
a>\alpha:
p^a\le2x-1,\ 
2(x\bmod p^a)\ge p^a+1
\right\}
\ge\alpha.
\]

For \(x=6\), the negative level \(2\) is compensated by \(8\), and the negative level \(3\) is compensated by \(9\).

---

### 8. Localization of all large negative indices

Let
\[
h=\left\lfloor\frac{m-1}{2}\right\rfloor.
\]
For \(d>m\), one has \(m\bmod d=m\). Hence
\[
e_d(m,x)=-1
\quad\Longleftrightarrow\quad
2(x\bmod d)<m.
\]
Since \(x\bmod d\) is an integer, this is equivalent to
\[
x\bmod d\in\{0,1,\ldots,h\}.
\]
Therefore
\[
\boxed{
d>m,\ e_d(m,x)=-1
\quad\Longleftrightarrow\quad
d\mid x-r
\text{ for some }0\le r\le h.
}
\]

Thus all negative prime-power levels exceeding \(m\) are localized among the prime-power divisors of
\[
x(x-1)\cdots(x-h).
\]

As a consequence, suppose a prime \(p\) satisfies
\[
p>m,\qquad p^2>2x-m,
\qquad p\mid x-r
\]
for some \(0\le r\le h\). Then
\[
e_p(m,x)=-1,
\]
and every higher \(p\)-power exceeds \(N=2x-m\). Hence
\[
\boxed{v_p(R_m(x-m))=-1}.
\]

A necessary condition for success is therefore that every prime factor of every number
\[
x,x-1,\ldots,x-h
\]
be at most
\[
\max\{m,\sqrt{2x-m}\}.
\]

Merely forcing these numbers to be composite is not enough. For example, when \(m=1\), let \(x=2q\) with \(q\ge5\) prime. Although \(x\) is composite,
\[
q\mid x,\qquad q^2>4q-1=2x-1,
\]
so \(v_q(R_1(x-1))=-1\).

---

### 9. Ledger

**Proved**

1. Exact residue formula
   \[
   e_d=\left\lfloor\frac{2(x\bmod d)-(m\bmod d)}d\right\rfloor.
   \]
2. \(e_d\in\{-1,0,1\}\).
3. For every \(m>0\) and every \(k\ge1\),
   \[
   e_{m+k}=-1.
   \]
4. The reduced Gaussian denominator contains
   \[
   (q^x-1)/(q^{\gcd(m,x)}-1).
   \]
5. Prime-power termwise positivity forces \(\operatorname{rad}(x)\mid m\), and is impossible for \(m=1\).
6. The prime-power capacity bound
   \[
   p^{2v_p(x)-v_p(m)}\le2x-m
   \]
   whenever \(v_p(x)>v_p(m)\) and \(R_m(x-m)\) is integral.
7. A complete prime-chain criterion for \(m=1\).
8. Localization of every negative index \(d>m\) among divisors of
   \[
   x(x-1)\cdots\left(x-\left\lfloor\frac{m-1}{2}\right\rfloor\right).
   \]
9. The corresponding terminal large-prime obstruction.

**Plausible but unproved**

- A direct construction might arrange that every forced negative \(p^a\)-level is followed by enough positive higher \(p\)-power levels. No simultaneous construction is known here.
- Smoothness of the short falling block above, together with controlled small-prime residues, might be useful, but it is not known to be sufficient.

**Dead ends**

1. Full cyclotomic positivity: false for every \(m>0\), because \(e_x=-1\).
2. Positivity at every prime-power level: already false for every \(x>1\) when \(m=1\).
3. CRT constructions producing only a run of composite numbers: insufficient, because a composite \(x-r\) can retain an unbalanced prime factor exceeding \(\sqrt{2x-m}\).

## Self-Audit

1. **The main obstruction uses the moving index \(d=x=m+k\).** This could be missed if one checks only fixed or small \(d\). It is nevertheless valid because \(x\ge2\) for \(m>0\), and \(x<2x-m\), so \(d=x\) is among the relevant cyclotomic indices. Both the residue calculation and the original floor formula give \(e_x=-1\).

2. **The forced factor \((q^x-1)/(q^g-1)\) concerns the polynomial denominator, not automatically the numerical denominator after \(q=1\).** I make no inference of ordinary nonintegrality from it. The polynomial statement follows from unique cyclotomic factorization, while the \(m=1,x=6\) example explicitly demonstrates numerical cancellation after specialization.

3. **The smoothness and prime-power capacity conditions are only necessary.** They do not control medium primes or guarantee that available higher powers contribute \(+1\). I believe the stated conditions themselves hold because each follows from an exact negative term together with the bound \(e_{p^a}\le1\); no sufficiency claim is used.

## Computations To Verify

```python
from math import gcd, factorial
from fractions import Fraction
from sympy import primerange, factorint, divisors
from sympy import symbols, Poly, cyclotomic_poly, div

def e_floor(m, x, d):
    # x = m+k, N = 2*x-m
    return (2*x - m)//d + m//d - 2*(x//d)

def e_residue(m, x, d):
    # Python // is floor division, including for negative numerators
    return (2*(x % d) - (m % d)) // d

def vp_R(m, x, p):
    N = 2*x - m
    ans = 0
    pa = p
    while pa <= N:
        ans += e_floor(m, x, pa)
        pa *= p
    return ans

def is_integral(m, x):
    N = 2*x - m
    return all(vp_R(m, x, p) >= 0 for p in primerange(2, N + 1))

def gaussian_negative_indices(m, x):
    N = 2*x - m
    return [d for d in range(2, N + 1) if e_floor(m, x, d) < 0]

# 1. Verify the residue identity and e_d in {-1,0,1}.
for m in range(0, 50):
    for x in range(max(1, m + 1), m + 80):
        N = 2*x - m
        for d in range(2, N + 20):
            assert e_floor(m, x, d) == e_residue(m, x, d)
            assert e_floor(m, x, d) in (-1, 0, 1)

# 2. Decisive failure of Route 2.
for m in range(1, 100):
    for x in range(m + 1, m + 100):
        assert e_floor(m, x, x) == -1

# For m=0, all exponents are nonnegative.
for x in range(1, 200):
    assert all(e_floor(0, x, d) >= 0 for d in range(2, 2*x + 1))

# 3. Verify forced negative divisor indices.
for m in range(1, 60):
    for x in range(m + 1, m + 100):
        neg = set(gaussian_negative_indices(m, x))
        forced = {
            d for d in divisors(x)
            if d >= 2 and m % d != 0
        }
        assert forced <= neg

# 4. Symbolically verify that (q^x-1)/(q^g-1) divides
#    the reduced cyclotomic denominator.
q = symbols('q')
for m in range(1, 12):
    for x in range(m + 1, m + 20):
        neg = gaussian_negative_indices(m, x)

        Q = Poly(1, q)
        for d in neg:
            Q *= Poly(cyclotomic_poly(d, q), q)

        g = gcd(m, x)
        H, rem = div(Poly(q**x - 1, q), Poly(q**g - 1, q))
        assert rem.is_zero

        quo, rem = div(Q, H)
        assert rem.is_zero

# 5. Exact m=1 denominator: negative indices are exactly divisors of x.
for x in range(2, 1000):
    neg = set(gaussian_negative_indices(1, x))
    expected = {d for d in divisors(x) if d > 1}
    assert neg == expected

# 6. Exact m=1 prime-chain criterion.
def m1_chain_condition(x):
    N = 2*x - 1
    for p, alpha in factorint(x).items():
        count = 0
        pa = p ** (alpha + 1)
        while pa <= N:
            if 2*(x % pa) >= pa + 1:
                count += 1
            pa *= p
        if count < alpha:
            return False
    return True

for x in range(2, 10000):
    assert m1_chain_condition(x) == is_integral(1, x)

# Known examples.
assert is_integral(1, 6)   # m=1, k=5
assert is_integral(2, 6)   # m=2, k=4
assert is_integral(1, 15)  # another m=1 solution

assert Fraction(factorial(11), factorial(6)**2) == 77

# Nonzero e_d for m=1, x=6 should be:
nonzero = [(d, e_floor(1, 6, d)) for d in range(2, 12)
           if e_floor(1, 6, d) != 0]
assert nonzero == [
    (2, -1), (3, -1), (6, -1),
    (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)
]

# 7. Verify the prime-power capacity condition on all finite successes.
for m in range(1, 30):
    for x in range(m + 1, 3000):
        if not is_integral(m, x):
            continue
        N = 2*x - m
        fm = factorint(m)
        for p, alpha in factorint(x).items():
            beta = fm.get(p, 0)
            if alpha > beta:
                assert p ** (2*alpha - beta) <= N

# 8. Verify large-negative-index localization.
for m in range(1, 40):
    h = (m - 1)//2
    for x in range(m + 1, m + 500):
        N = 2*x - m

        # Every negative d>m divides some x-r, 0<=r<=h.
        for d in range(m + 1, N + 1):
            if e_floor(m, x, d) == -1:
                assert any((x-r) % d == 0 for r in range(h + 1))

        # Terminal large-prime factors give exact valuation -1.
        for r in range(h + 1):
            for p in factorint(x-r):
                if p > m and p*p > N:
                    assert vp_R(m, x, p) == -1
                    assert not is_integral(m, x)

# Composite x=2q is not enough for m=1.
for q0 in list(primerange(5, 500)):
    x = 2*q0
    assert vp_R(1, x, q0) == -1
    assert not is_integral(1, x)
```

## Route Diagnosis

The exact Route 2 target is categorically false: the index \(d=m+k\) always contributes \(-1\) when \(m>0\). Moreover, the Gaussian quotient carries a large forced denominator, and deleting non-prime-power indices does not repair the method because \(m=1\) already requires cancellation between \(e_p,e_{p^2},\ldots\).

The useful remnant of the cyclotomic analysis is bookkeeping along prime-power chains. Forced negative levels arise from divisors of \(x\), and more generally every negative level \(d>m\) divides one of
\[
x,x-1,\ldots,x-\left\lfloor\frac{m-1}{2}\right\rfloor.
\]
A fresh attempt should therefore abandon coefficientwise cyclotomic positivity and seek an aggregate compensation theorem: construct \(x\) so that every forced negative \(p^a\)-level is followed by enough positive higher powers of the same prime. The precise block is the familiar circularity: congruences controlling known primes enlarge \(x\), introducing new prime divisors of the short falling block and hence new uncontrolled chains. Merely imposing a CRT run of composite numbers does not solve this, because large cofactor primes remain terminal obstructions.