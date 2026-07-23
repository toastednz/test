STATUS: BLOCKED

## Result

Route 3 yields a clean rational reformulation and several rigorous structural results, but not the required balanced bicliques. I prove that fixed distinct rows \(a_1,\dots,a_m\) are parametrized by a curve of genus \(1+2^{m-1}(m-2)\); consequently, three fixed rows have only finitely many common rational Pythagorean partners. I also prove that the seemingly harmless pair \(\{1,2\}\) has no positive rational common partner, so a universal extension lemma is false. In the opposite direction, the fixed pair \(\{240,252\}\) has infinitely many rational common partners, giving integral \(K_{2,n}\) Pythagorean bicliques for every \(n\). Additional obstructions rule out square cross-ratios and rank-one hypotenuse ansätze. The unresolved step is exactly the production, for unbounded \(k\), of specially varying genus-\(1+2^{k-1}(k-2)\) curves with at least \(k-1\) suitable rational points; none of the elliptic, multiplicative, or composition mechanisms found here controls those simultaneous lifts.

## Complete Argument

### 1. Exact Route 3 reduction

Suppose there are distinct positive rationals
\[
r_1,\dots,r_k,\qquad e_1,\dots,e_{k-1}
\]
and rationals \(h_{ij}>0\) satisfying
\[
r_i^2+e_j^2=h_{ij}^2
\qquad(1\le i\le k,\ 1\le j\le k-1).
\]
Choose a positive integer \(L\) clearing all denominators and put
\[
R_i=Lr_i,\qquad E_j=Le_j,\qquad H_{ij}=Lh_{ij}.
\]
Then all these quantities are positive integers and
\[
R_i^2+E_j^2=H_{ij}^2.
\]
Set
\[
N_i=R_i^2,\qquad d_0=0,\qquad d_j=2E_j.
\]
Now
\[
4N_i+d_0^2=(2R_i)^2
\]
and
\[
4N_i+d_j^2
=4R_i^2+4E_j^2
=(2H_{ij})^2.
\]
Thus \(0,2E_1,\dots,2E_{k-1}\) belong to every \(D(N_i)\). Positivity and distinctness of the \(r_i,e_j\) imply distinctness of the \(N_i,d_j\).

Hence Route 3 would solve the problem if it produced \(K_{k,k-1}\) Pythagorean bicliques over \(\mathbb Q\) for unbounded \(k\).

For later use, after dividing by \(e_j^2\), an edge is equivalently
\[
1+\left(\frac{r_i}{e_j}\right)^2
 =\left(\frac{h_{ij}}{e_j}\right)^2.
\]
Thus the cross-ratios \(r_i/e_j\) must belong to
\[
\mathcal S=\{q\in\mathbb Q_{>0}:1+q^2\text{ is a rational square}\}.
\]
Equivalently, putting \(A_i=r_i^2\) and \(B_j=e_j^{-2}\), Route 3 asks for square rationals \(A_i,B_j\) such that
\[
A_iB_j+1
\]
is a rational square for every \(i,j\).

---

### 2. The common-partner curve and its genus

Fix distinct positive rationals \(a_1,\dots,a_m\). Their common rational Pythagorean partners are the \(x\)-coordinates on
\[
C_{\mathbf a}:\qquad
y_i^2=x^2+a_i^2,\qquad 1\le i\le m.
\]

#### Proposition 2.1

The smooth projective model of \(C_{\mathbf a}\) is geometrically connected and has genus
\[
g_m=1+2^{m-1}(m-2).
\]

#### Proof

Consider the map \(C_{\mathbf a}\to\mathbb P^1_x\). Its function field is
\[
\overline{\mathbb Q}(x)
 \bigl(\sqrt{x^2+a_1^2},\dots,\sqrt{x^2+a_m^2}\bigr).
\]
The \(2m\) branch points
\[
x=\pm ia_1,\dots,\pm ia_m
\]
are distinct. Because each square class \(x^2+a_i^2\) has branch points not occurring in any of the other classes, these \(m\) square classes are independent in
\[
\overline{\mathbb Q}(x)^\times/
\overline{\mathbb Q}(x)^{\times 2}.
\]
The cover therefore has degree \(2^m\) and Galois group \((\mathbb Z/2\mathbb Z)^m\).

There is no ramification over infinity because every \(x^2+a_i^2\) has an even-order pole there. Over each of the \(2m\) finite branch points, the inertia group has order \(2\), so its total contribution to Riemann–Hurwitz is \(2^{m-1}\). Therefore
\[
2g_m-2
=2^m(-2)+(2m)2^{m-1}
=2^m(m-2),
\]
which gives
\[
g_m=1+2^{m-1}(m-2).
\]
∎

In particular,
\[
g_1=0,\qquad g_2=1,\qquad g_3=5.
\]

#### Corollary 2.2

Any fixed set of at least three distinct positive rational rows has only finitely many common rational Pythagorean partners.

#### Proof

For \(m\ge3\), Proposition 2.1 gives \(g_m>1\). Faltings’ theorem then gives finiteness of \(C_{\mathbf a}(\mathbb Q)\). Since \(x:C_{\mathbf a}\to\mathbb P^1\) has finite fibers, only finitely many rational \(x\) occur. ∎

This does not give a uniform bound as the \(a_i\) vary, but it rules out an amplification scheme that keeps three or more rows fixed while producing infinitely many new columns.

---

### 3. A universal extension lemma is false

The degenerate common partner \(x=0\) always exists. It is not generally possible to replace it by a positive rational partner.

#### Proposition 3.1

There is no positive rational \(x\) such that both
\[
x^2+1\quad\text{and}\quad x^2+4
\]
are rational squares.

#### Proof

Suppose
\[
u^2=x^2+1,\qquad v^2=x^2+4.
\]
Put
\[
X=x^2,\qquad Y=xuv.
\]
Then
\[
Y^2=X(X+1)(X+4),
\]
so \((X,Y)\) is a rational point on
\[
E:\qquad Y^2=X^3+5X^2+4X.
\]

We determine \(E(\mathbb Q)\).

For a curve
\[
F:y^2=x^3+Ax^2+Bx
\]
with its rational point \((0,0)\) of order \(2\), the standard \(2\)-isogenous curve is
\[
F':y^2=x^3-2Ax^2+(A^2-4B)x.
\]
The \(2\)-isogeny descent maps associate to a point with \(x\ne0\) the square class of its \(x\)-coordinate. A squarefree divisor \(d\) of \(B\) can occur only if
\[
Z^2=dU^4+AU^2V^2+\frac BdV^4
\tag{1}
\]
has a primitive integral solution. The corresponding descent images satisfy
\[
2^{\operatorname{rank}F(\mathbb Q)}
=\frac{|\operatorname{im}\alpha_F|\,
       |\operatorname{im}\alpha_{F'}|}{4}.
\tag{2}
\]

For \(E\), we have \(A=5,B=4\), and
\[
E':\qquad y^2=x^3-10x^2+9x=x(x-1)(x-9).
\]

On \(E\), the points
\[
(-1,0),\quad (2,6),\quad (-2,2)
\]
show that all four possible square classes
\[
1,-1,2,-2
\]
occur. Hence
\[
|\operatorname{im}\alpha_E|=4.
\]

For \(E'\), the only possible square classes are \(1,-1,3,-3\). Since
\[
x(x-1)(x-9)<0
\]
for \(x<0\), all rational points of \(E'\) have \(x\ge0\), so only the classes \(1\) and \(3\) can occur. If the class \(3\) occurred, equation (1) would give a primitive integral solution of
\[
Z^2=3U^4-10U^2V^2+3V^4.
\tag{3}
\]
If exactly one of \(U,V\) is odd, the right side of (3) is \(3\pmod8\), impossible for a square. If both are odd, it is \(12\pmod{16}\), also impossible. Both cannot be even in a primitive solution. Hence class \(3\) does not occur and
\[
|\operatorname{im}\alpha_{E'}|=1.
\]
Equation (2) now gives
\[
\operatorname{rank}E(\mathbb Q)=0.
\]

It remains to determine the torsion. The curve has good reduction at \(5\) and \(7\), and direct counting gives
\[
|E(\mathbb F_5)|=|E(\mathbb F_7)|=8.
\]
Thus the rational torsion has order at most \(8\). The following eight rational points are already present:
\[
O,\quad (0,0),\quad(-1,0),\quad(-4,0),
\quad(2,\pm6),\quad(-2,\pm2).
\]
Consequently these are all the rational points on \(E\).

Since \(X=x^2\ge0\), the only possible coordinates in the list are \(X=0\) and \(X=2\). The latter is not a square in \(\mathbb Q\). Hence \(X=0\), so \(x=0\). No positive rational common partner exists. ∎

Thus even a \(2\)-row configuration need not admit any positive new column. Any induction must preserve a very special arithmetic locus; it cannot extend arbitrary existing configurations.

---

### 4. The elliptic case can nevertheless give infinitely many columns

The preceding obstruction is not universal. There are fixed pairs with infinitely many common rational partners.

#### Proposition 4.1

The pair
\[
a=240,\qquad b=252
\]
has infinitely many distinct positive rational common Pythagorean partners. Consequently, integral Pythagorean \(K_{2,n}\) bicliques exist for every \(n\).

#### Proof

Consider
\[
C:\qquad
u^2=e^2+240^2,\qquad
v^2=e^2+252^2.
\]
By Proposition 2.1, its smooth projective model has genus \(1\). It has the rational base point
\[
Q=(0,240,252)
\]
and the additional point
\[
P=(275,365,373),
\]
because
\[
240^2+275^2=365^2,\qquad
252^2+275^2=373^2.
\]

There is a nonconstant morphism
\[
f:C\longrightarrow E_{240,252},
\qquad
(e,u,v)\longmapsto (e^2,euv),
\]
where
\[
E_{240,252}:\quad
Y^2=X(X+240^2)(X+252^2).
\]
The image of \(P\) is
\[
P_E=(275^2,\,275\cdot365\cdot373).
\]

The discriminant of this integral Weierstrass equation is
\[
\Delta
=16\cdot240^4\cdot252^4
  \bigl(240^2-252^2\bigr)^2.
\]
Now
\[
240^2-252^2=-5904=-2^4\cdot3^2\cdot41,
\]
so the prime divisors of \(\Delta\) lie in
\[
\{2,3,5,7,41\}.
\]
But \(11\mid275\), and hence \(11\mid Y(P_E)\).

By the Nagell–Lutz divisibility criterion, a nonzero \(Y\)-coordinate of a rational torsion point on an integral Weierstrass curve can have prime divisors only among the prime divisors of the discriminant. Therefore \(P_E\) is nontorsion.

The point \(f(Q)=(0,0)\) is torsion. Translating \(f\) by \(-f(Q)\) produces a morphism of elliptic curves sending \(Q\) to the identity. Such a nonconstant morphism is an isogeny. Since
\[
f(P)-f(Q)
\]
is nontorsion, \(P\) is nontorsion in \(C(\mathbb Q)\). Therefore \(C(\mathbb Q)\) is infinite.

The rational function \(e:C\to\mathbb P^1\) is nonconstant and has finite fibers. Hence infinitely many distinct rational values of \(e\) occur. Discarding \(e=0\) and replacing negative values by their positives gives infinitely many distinct positive rational common partners.

For any prescribed \(n\), choose \(n\) of them and clear all denominators uniformly. This gives two distinct positive integer rows and \(n\) distinct positive integer columns satisfying all Pythagorean equations. ∎

This proves arbitrarily large bicliques on one side only. It does not approach the needed \(K_{k,k-1}\) balance once the number of rows exceeds two.

---

### 5. A global obstruction to multiplicative ansätze

#### Proposition 5.1

If \(r,e>0\) are rational and \(r^2+e^2\) is a rational square, then \(r/e\) is not a rational square.

#### Proof

It suffices to recall Fermat’s classical theorem that
\[
A^4+B^4=C^2
\tag{4}
\]
has no solution in positive integers.

For completeness, suppose a primitive solution of (4) with minimal \(C\) existed. Exactly one of \(A,B\) is even; say \(A\) is odd and \(B\) is even. Parametrizing the primitive Pythagorean triple
\[
A^2+B^2=C^2
\]
gives
\[
A^2=m^2-n^2,\qquad B^2=2mn,\qquad C=m^2+n^2,
\]
where \(m>n\) are coprime and of opposite parity. Here \(m\) is odd and \(n\) is even. Since
\[
(B/2)^2=m(n/2)
\]
and \(m,n/2\) are coprime, there are positive integers \(r,s\) with
\[
m=r^2,\qquad n=2s^2.
\]
Then
\[
A^2+(2s^2)^2=r^4.
\]
This is again a primitive Pythagorean triple, so
\[
A=p^2-q^2,\qquad 2s^2=2pq,\qquad r^2=p^2+q^2
\]
with coprime \(p,q\). Since \(pq=s^2\), both \(p\) and \(q\) are squares, say \(p=u^2,q=v^2\). Therefore
\[
u^4+v^4=r^2,
\]
a new positive solution of (4) with hypotenuse \(r<C\), contradicting minimality.

Now suppose \(r/e=(A/B)^2\) in lowest terms and
\[
1+(r/e)^2=H^2.
\]
Then
\[
A^4+B^4=(HB^2)^2.
\]
An integer which is a rational square is an integer square, contradicting (4). ∎

Consequently, in every Route 3 biclique the square classes represented by the rows and columns in
\[
\mathbb Q^\times/\mathbb Q^{\times2}
\]
must be disjoint. This rules out geometric constructions in which any cross-ratio is forced to be a rational square.

---

### 6. A rank-one hypotenuse ansatz is degenerate

#### Proposition 6.1

There is no nondegenerate \(2\times2\) Pythagorean biclique for which the hypotenuses factor as
\[
h_{ij}=\alpha_i\beta_j.
\]

#### Proof

Suppose
\[
r_i^2+e_j^2=\alpha_i^2\beta_j^2.
\]
Subtracting the equations for \(j=1,2\) gives
\[
e_1^2-e_2^2
=\alpha_i^2(\beta_1^2-\beta_2^2).
\]
If \(e_1\ne e_2\), both sides are nonzero, so \(\alpha_1^2=\alpha_2^2\). It follows from
\[
r_i^2=\alpha_i^2\beta_1^2-e_1^2
\]
that \(r_1^2=r_2^2\), hence \(r_1=r_2\) for positive rows. This is degenerate. ∎

This blocks a natural attempt to make the hyperbola group law separable: any construction requiring normalized or unnormalized hypotenuses to have rank one collapses the rows.

---

### 7. There is no local obstruction

For completeness, the balanced Pythagorean systems are locally soluble in all sizes.

Fix a prime \(p\). Choose distinct \(p\)-adic units \(r_i\). For odd \(p\), choose distinct nonzero \(e_j\in p\mathbb Z_p\). Then
\[
r_i^2+e_j^2
=r_i^2\left(1+(e_j/r_i)^2\right),
\]
and the second factor has a square root by Hensel’s lemma near \(1\). For \(p=2\), choose \(e_j\in4\mathbb Z_2\); then
\[
1+(e_j/r_i)^2\equiv1\pmod8,
\]
so it is a square in \(\mathbb Q_2\). Over \(\mathbb R\), positivity gives square roots directly.

Thus every finite balanced system has nondegenerate points over every completion separately. The obstruction is genuinely global and rational, not an elementary congruence obstruction.

---

### 8. Ledger

**Proved lemmas**

1. Rational \(K_{k,k-1}\) Pythagorean bicliques imply \(P(k)\) after uniform denominator clearing.
2. The common-partner curve for \(m\) fixed distinct rows has genus
   \[
   1+2^{m-1}(m-2).
   \]
3. Three or more fixed rows have only finitely many common rational partners.
4. The rows \(1,2\) have no positive rational common partner.
5. The rows \(240,252\) have infinitely many rational common partners, giving integral \(K_{2,n}\) for every \(n\).
6. No Pythagorean cross-ratio can be a rational square.
7. A rank-one hypotenuse matrix forces degeneracy.
8. Nondegenerate systems of every finite size exist over every completion \(\mathbb Q_p\) and over \(\mathbb R\).

**Plausible but unproved**

- Specially chosen higher-genus common-partner curves may have enough rational points for balanced bicliques.
- The elliptic curve behind \(\{240,252\}\) may contain additional arithmetic structure useful for producing further rows, but no such structure was established.

**Dead ends**

- **Universal induction:** false, by the exact pair \(\{1,2\}\).
- **Keep a fixed core and add infinitely many columns:** impossible once the core has three distinct rows, by Faltings.
- **Geometric/multiplicative square-ratio families:** blocked by Proposition 5.1.
- **Rank-one hypotenuse separation:** forces repeated rows.
- **Naive Pythagorean norm composition:** in
  \[
  (r^2+e^2)(R^2+E^2)
  =(rR-eE)^2+(rE+eR)^2,
  \]
  both new legs depend on both old row and column indices, so neither is a row-only or column-only parameter except in degenerate cases.

## Self-Audit

1. **The central balanced construction remains completely unresolved.**  
   The \(K_{2,n}\) theorem is genuinely one-sided and cannot be presented as evidence of a proof for \(K_{k,k-1}\). I make no such inference; the status is explicitly BLOCKED.

2. **Proposition 3.1 uses the standard \(2\)-isogeny descent formula.**  
   The only non-elementary ingredient in its rank computation is the exact index formula (2). The relevant descent images are nevertheless determined explicitly, including the complete mod-\(16\) obstruction for the only questionable class. The result can also be independently certified by an exact Sage/Magma \(2\)-descent.

3. **Proposition 4.1 uses Nagell–Lutz and the genus-one group structure rather than writing an explicit sequence of common partners.**  
   Nagell–Lutz applies after passing, if desired, to an integral short Weierstrass model; this introduces only powers of \(2\) and \(3\), while the decisive prime is \(11\), which is absent from the discriminant. A nontorsion rational point on the genus-one curve rigorously supplies infinitely many rational points, and a nonconstant coordinate function takes infinitely many values.

## Computations To Verify

```python
from math import isqrt, gcd
from fractions import Fraction
from itertools import combinations

def is_square_int(n):
    if n < 0:
        return False
    s = isqrt(n)
    return s*s == n

def is_square_frac(q):
    q = Fraction(q)
    return q >= 0 and is_square_int(q.numerator) and is_square_int(q.denominator)

# Verify the Euler-brick point used in Proposition 4.1.
a, b, e = 240, 252, 275
u, v = 365, 373
assert a*a + e*e == u*u
assert b*b + e*e == v*v

# Discriminant prime support.
from sympy import factorint
Delta = 16 * a**4 * b**4 * (a*a - b*b)**2
Y = e*u*v
print(factorint(Delta))
print(factorint(Y))
assert 11 in factorint(Y)
assert 11 not in factorint(Delta)

# Count E: y^2=x(x+1)(x+4) over finite fields.
def count_E_mod_p(p):
    count = 1  # point at infinity
    residues = {(y*y) % p for y in range(p)}
    for x in range(p):
        rhs = (x*(x+1)*(x+4)) % p
        if rhs == 0:
            count += 1
        elif rhs in residues:
            count += 2
    return count

assert count_E_mod_p(5) == 8
assert count_E_mod_p(7) == 8

# Verify the eight rational points listed on E.
points = [
    None, (0, 0), (-1, 0), (-4, 0),
    (2, 6), (2, -6), (-2, 2), (-2, -2)
]
for P in points[1:]:
    x, y = P
    assert y*y == x*(x+1)*(x+4)

# Exhaust the residue obstruction for the d=3 descent quartic.
square_mod_16 = {(z*z) % 16 for z in range(16)}
for U in range(16):
    for V in range(16):
        if gcd(gcd(U, V), 16) == 1:
            rhs = (3*U**4 - 10*U*U*V*V + 3*V**4) % 16
            assert rhs not in square_mod_16

# Bounded rational check for common partners of 1 and 2.
def bounded_common_partners(max_num, max_den):
    ans = set()
    for den in range(1, max_den + 1):
        for num in range(1, max_num + 1):
            if gcd(num, den) != 1:
                continue
            x = Fraction(num, den)
            if is_square_frac(x*x + 1) and is_square_frac(x*x + 4):
                ans.add(x)
    return sorted(ans)

assert bounded_common_partners(500, 500) == []

# Bounded integer Pythagorean-biclique search.
def neighbors(B):
    adj = {}
    for r in range(1, B + 1):
        adj[r] = set()
        for e in range(1, B + 1):
            if is_square_int(r*r + e*e):
                adj[r].add(e)
    return adj

def find_biclique(B, rows_needed, cols_needed):
    adj = neighbors(B)
    for rows in combinations(range(1, B + 1), rows_needed):
        common = set.intersection(*(adj[r] for r in rows))
        if len(common) >= cols_needed:
            return rows, tuple(sorted(common)[:cols_needed])
    return None

# Example experimental call:
# print(find_biclique(2000, 5, 4))
```

Exact Sage verification:

```python
# Run in SageMath.

E = EllipticCurve(QQ, [0, 5, 0, 4, 0])
assert E.rank(proof=True) == 0
print(E.torsion_subgroup())
print(E.torsion_points())

a, b, e, u, v = 240, 252, 275, 365, 373
Ebig = EllipticCurve(QQ, [0, a*a + b*b, 0, a*a*b*b, 0])
P = Ebig(e*e, e*u*v)
print(P.order())             # should be +Infinity
assert not P.has_finite_order()
```

Genus check in Magma:

```magma
Q := Rationals();
P3<E,U,V,W> := ProjectiveSpace(Q,3);
a := 240; b := 252;
C := Curve(P3, [
    U^2 - E^2 - a^2*W^2,
    V^2 - E^2 - b^2*W^2
]);
assert Genus(C) eq 1;
```

## Route Diagnosis

Route 3 works completely for one fixed row and, on suitable elliptic curves, for two fixed rows; it fails to amplify automatically beyond that. The exact obstruction is the transition from genus \(1\) to genus \(5\): with three fixed rows, common columns lie on a high-genus multiquadratic curve and are finite, while the pair \(\{1,2\}\) shows that even genus \(1\) need not supply a single nondegenerate point. The remaining lemma needed is therefore not a routine rank argument but a family-level construction of varying high-genus curves carrying linearly many prescribed rational points. That is essentially the original Route 3 problem and is of comparable strength, so the route is BLOCKED.

A fresh attempt should either:

1. search for special \(C_{\mathbf a}\) with large automorphism groups and elliptic quotients whose rational points provably lift through every covering condition;
2. seek a composition law directly for bipartite rational Diophantine square-tuples \(A_iB_j+1=\square\), avoiding rank-one separation;
3. mine exact \(K_{5,4}\) examples and inspect their Jacobian decompositions for a reusable family.

No superior alternative emerged from the present analysis.