STATUS: BLOCKED

## Result

Route 2 can be pushed rigorously through three common differences but presently breaks at the fourth. I prove that for every \(m\) there are \(m\) distinct integers \(N_i\) having the three common differences \(0,12Q,30Q\), for a suitable scale \(Q\). The first two differences arise exactly from many admissible factorizations of one difference of squares, while an explicit positive-rank elliptic curve forces the third. However, adding a fourth fixed difference produces a genus-\(5\) curve, so Faltings rules out extending this same family infinitely often. More generally, an affirmative solution would produce genus-\(5\) curves over \(\mathbb Q\) with arbitrarily many rational points, contrary to the standard uniform boundedness conjecture for fixed-genus curves. No unconditional uniform bound, nor a construction overcoming it, is obtained.

## Complete Argument

### 1. Exact divisor engineering for the first two columns

Let \(0\le d_1<d_2\), and set
\[
C=d_2^2-d_1^2.
\]

#### Lemma 1

Positive integers \(N\) satisfying \(d_1,d_2\in D(N)\) are in bijection with factorizations
\[
uv=C,\qquad 0<u<v,\qquad u\equiv v\pmod 2,
\]
such that
\[
x_1=\frac{v-u}{2}>d_1,\qquad x_1\equiv d_1\pmod 2.
\]
The corresponding row is
\[
N=\frac{x_1^2-d_1^2}{4}.
\]

#### Proof

If \(d_1,d_2\in D(N)\), let \(x_j>0\) be defined by
\[
x_j^2=4N+d_j^2.
\]
Since \(d_2>d_1\), we have \(x_2>x_1\). Put
\[
u=x_2-x_1,\qquad v=x_2+x_1.
\]
Then
\[
uv=x_2^2-x_1^2=d_2^2-d_1^2=C,
\]
and \(u,v\) have the same parity. Moreover,
\[
x_1=\frac{v-u}{2}.
\]
Because \(N>0\), \(x_1>d_1\), and since \(x_1^2-d_1^2=4N\), one has
\(x_1\equiv d_1\pmod2\).

Conversely, from such \(u,v\), define
\[
x_1=\frac{v-u}{2},\qquad x_2=\frac{v+u}{2}.
\]
Then
\[
x_2^2-x_1^2=uv=C=d_2^2-d_1^2.
\]
The parity and inequality assumptions give
\[
N=\frac{x_1^2-d_1^2}{4}\in\mathbb Z_{>0},
\]
and hence
\[
x_j^2=4N+d_j^2\qquad(j=1,2).
\]
Thus \(d_1,d_2\in D(N)\). The construction is reversible, proving the bijection. ∎

A particularly transparent specialization is \(d_1=0\), \(d_2=2M\).

#### Corollary 2

If \(M\) is odd, the pair of differences \(0,2M\) has exactly
\[
\frac{\tau(M^2)-1}{2}
\]
positive common rows of the form \(N=r^2\). They are
\[
r=\frac{B-A}{2},
\]
where
\[
AB=M^2,\qquad A<B.
\]

#### Proof

Every divisor pair \(AB=M^2\) consists of odd integers. Set
\[
r=\frac{B-A}{2},\qquad h=\frac{A+B}{2}.
\]
Then
\[
h^2-r^2=AB=M^2,
\]
so
\[
4r^2+(2M)^2=(2h)^2.
\]
Thus \(0,2M\in D(r^2)\). Conversely, Lemma 1 gives all rows in this manner. Since \(M^2\) is a square, the number of unordered factor pairs with \(A<B\) is
\[
\frac{\tau(M^2)-1}{2}.
\]
Different \(A<M\) give different \(r\), because \(M^2/A-A\) is strictly decreasing in \(A>0\). ∎

For example, if \(M\) is the product of \(s\) distinct odd primes, this gives
\[
\frac{3^s-1}{2}
\]
candidate rows. Thus the first two columns can be made to support arbitrarily many rows by pure divisor engineering.

This by itself gives no further alignment. For instance, \(M=15\) gives the four rows
\[
r=112,36,20,8.
\]
All four squares \(r^2\) contain \(0\) and \(30\) in their difference sets, but their total intersection is exactly \(\{0,30\}\). Indeed,
\[
D(64)=\{0,12,30,63\},
\]
while
\[
D(400)=\{0,9,30,42,75,96,198,399\}.
\]
Their intersection is already only \(\{0,30\}\).

---

### 2. An elliptic alignment producing arbitrarily many rows and three columns

The following is the main positive result obtained from Route 2.

#### Theorem 3

For every \(m\ge1\), there exist distinct positive integers
\[
N_1,\dots,N_m
\]
and a positive integer \(Q\) such that
\[
\{0,12Q,30Q\}\subseteq\bigcap_{i=1}^m D(N_i).
\]

Equivalently, there are arbitrarily large \(K_{m,3}\) in the incidence graph.

#### Proof

We first prove that there are infinitely many distinct positive rational numbers \(R\) for which both
\[
R^2+36,\qquad R^2+225
\]
are rational squares.

Parametrize the first equation by
\[
R=\frac{12t}{1-t^2},\qquad
H=\frac{6(1+t^2)}{1-t^2}.
\]
Then \(H^2=R^2+36\). The condition \(K^2=R^2+225\) becomes, after putting
\[
w=K(1-t^2),
\]
the quartic
\[
w^2=225t^4-306t^2+225. \tag{1}
\]

For \(t\ne0\), define
\[
X=\frac{w+15}{t^2},\qquad
Y=t(X^2-225).
\]
From (1),
\[
(w-15)(w+15)=t^2(225t^2-306).
\]
Using \(w+15=Xt^2\), one obtains
\[
t^2(X^2-225)=30X-306.
\]
Consequently,
\[
Y^2=(30X-306)(X^2-225).
\]

Now set
\[
u=30X,\qquad V=30Y.
\]
This gives the elliptic curve
\[
E:\quad V^2=(u-306)(u-450)(u+450). \tag{2}
\]
Conversely, outside the finitely many points for which the denominators vanish,
\[
t=\frac{30V}{u^2-202500},\qquad
X=\frac{u}{30},\qquad
w=Xt^2-15.
\]
Thus (1) and \(E\) are birational.

The quartic point
\[
t=\frac12,\qquad w=\frac{51}{4}
\]
corresponds to
\[
P=(3330,181440)\in E(\mathbb Q).
\]
Indeed,
\[
3330-306=3024,\quad
3330-450=2880,\quad
3330+450=3780,
\]
and
\[
3024\cdot2880\cdot3780=181440^2.
\]

We show that \(P\) has infinite order. Expanding (2),
\[
V^2=u^3-306u^2-202500u+61965000.
\]
Translate \(u=x+102\). This produces the integral short Weierstrass equation
\[
V^2=x^3-233712x+39187584. \tag{3}
\]
The tangent slope at \(P\), calculated in the original \(u\)-coordinate, is
\[
\lambda
 =\frac{3u^2-612u-202500}{2V}
 =\frac{31026240}{362880}
 =\frac{171}{2}.
\]
Hence
\[
u(2P)=\lambda^2+306-2u
=\frac{29241}{4}+306-6660
=\frac{3825}{4}.
\]
On (3), the \(x\)-coordinate of \(2P\) is therefore
\[
x(2P)=\frac{3825}{4}-102=\frac{3417}{4},
\]
which is not an integer.

By the Nagell–Lutz theorem, every rational torsion point on the integral short Weierstrass equation (3) has integral coordinates. If \(P\) were torsion, then \(2P\) would be a finite torsion point because \(P\) is not a point of order \(2\). This contradicts the nonintegrality of \(x(2P)\). Therefore \(P\) has infinite order.

It follows that \(E(\mathbb Q)\), and hence the quartic (1), has infinitely many rational points. Only finitely many are excluded by the birational formulas or by \(t=0,\pm1\).

For every remaining point define
\[
R=\frac{12t}{1-t^2},\qquad
H=\frac{6(1+t^2)}{1-t^2},\qquad
K=\frac{w}{1-t^2}.
\]
Then
\[
H^2=R^2+36,\qquad K^2=R^2+225. \tag{4}
\]

These points give infinitely many distinct values of \(R^2\). Indeed, for a fixed \(R\), the equation
\[
R(1-t^2)=12t
\]
has at most two values of \(t\), and each \(t\) has at most two corresponding values of \(w\). Thus a fixed \(R^2\) has only finitely many preimages on the quartic.

Choose \(m\) points with distinct positive values \(R_i^2\). Let \(Q\) be a positive common multiple of the denominators of all
\[
R_i,\ H_i,\ K_i.
\]
Set
\[
r_i=Q|R_i|,\qquad N_i=r_i^2,
\]
and define the three differences
\[
d_1=0,\qquad d_2=12Q,\qquad d_3=30Q.
\]
Equation (4) gives
\[
4N_i=(2r_i)^2,
\]
\[
4N_i+(12Q)^2
 =4Q^2(R_i^2+36)
 =(2QH_i)^2,
\]
and
\[
4N_i+(30Q)^2
 =4Q^2(R_i^2+225)
 =(2QK_i)^2.
\]
Thus
\[
0,12Q,30Q\in D(N_i)
\]
for every \(i\). The \(N_i\) are positive and distinct because the \(R_i^2\) are distinct. ∎

The first two rational rows obtained from \(P\) and \(2P\) are
\[
(R,H,K)=(8,10,17)
\]
and
\[
(R,H,K)=
\left(
\frac{61200}{1001},
\frac{61494}{1001},
\frac{63015}{1001}
\right).
\]
Taking \(Q=1001\) gives the integer rows
\[
N_1=8008^2,\qquad N_2=61200^2
\]
with common differences
\[
0,\quad12012,\quad30030.
\]

This construction is genuinely compatible with Route 2. For the initial pair \(0,12Q\), each row yields an admissible factorization
\[
(2H_i-2R_i)(2H_i+2R_i)=(12Q)^2
\]
after scaling. The elliptic curve selects many of those factor pairs that also support the third difference \(30Q\).

---

### 3. The obstruction at the fourth column

The preceding positive-rank argument cannot simply be continued with a fixed fourth difference.

#### Proposition 4

Let
\[
0\le d_1<d_2<d_3<d_4
\]
be distinct rational numbers. The smooth projective model of
\[
Y_j^2=X^2+d_j^2-d_1^2,\qquad j=2,3,4, \tag{5}
\]
is a geometrically connected curve of genus \(5\).

#### Proof

Put
\[
c_j=d_j^2-d_1^2.
\]
The \(c_j\) are distinct and nonzero. Over \(\overline{\mathbb Q}\), the branch points of
\[
Y_j^2=X^2+c_j
\]
are the two roots of \(X^2+c_j\). These six branch points are pairwise distinct.

The three square classes \(X^2+c_j\) are independent in
\[
\overline{\mathbb Q}(X)^\times/
\overline{\mathbb Q}(X)^{\times2}.
\]
Indeed, any nonempty product of them has odd valuation at a root belonging to one selected factor and hence cannot be a square. Thus the compositum has degree \(2^3=8\) over \(\overline{\mathbb Q}(X)\), proving geometric connectedness.

At each of the six branch points, there are four points above it, each with ramification index \(2\), so each branch point contributes \(4\) to the ramification divisor. There is no ramification at infinity because all three defining polynomials have even degree and square leading coefficient.

Riemann–Hurwitz therefore gives
\[
2g-2=8(-2)+6\cdot4=8,
\]
and hence \(g=5\). ∎

By Faltings’ theorem, a fixed quadruple \(d_1,d_2,d_3,d_4\) supports only finitely many rational rows. In particular, in Theorem 3 no fixed fourth rational difference can work for infinitely many of the elliptic-curve rows.

There is also a broader consequence.

#### Proposition 5

If the Erdős assertion holds for unbounded \(k\), then there are smooth genus-\(5\) curves over \(\mathbb Q\) with arbitrarily many rational points.

#### Proof

Given a \(k\times k\) solution with \(k\ge4\), retain any four columns
\[
d_1<d_2<d_3<d_4.
\]
By Proposition 4 they define a genus-\(5\) curve (5). Each row gives the rational point
\[
(X,Y_2,Y_3,Y_4)
 =(x_{i1},x_{i2},x_{i3},x_{i4}).
\]
These points are distinct: since
\[
X_i^2=4N_i+d_1^2,
\]
distinct positive \(N_i\) give distinct positive \(X_i\). Thus the curve has at least \(k\) rational points. Letting \(k\) be unbounded proves the assertion. ∎

Consequently, the full Erdős assertion would contradict the usual uniform boundedness conjecture asserting that the number of rational points on a genus-\(5\) curve over \(\mathbb Q\) is bounded solely in terms of the genus and the ground field. That conjecture is not proved, so this is not a disproof, but it precisely identifies the depth of the obstruction.

For the particular elliptic family above, if \(R_1,\dots,R_m\) are selected rows, a new Pythagorean column \(E\) would require
\[
Z_i^2=E^2+R_i^2\qquad(1\le i\le m). \tag{6}
\]
Assuming the \(R_i^2\) are distinct, the smooth model of (6) has genus
\[
g=1+2^{m-1}(m-2).
\]
Indeed, its degree over the \(E\)-line is \(2^m\), it has \(2m\) disjoint branch points, and each branch point contributes \(2^{m-1}\). Thus
\[
2g-2=-2^{m+1}+2m\,2^{m-1}
     =2^m(m-2).
\]
The curve already has the three known column values \(E=0,6,15\); the unresolved task is to force further distinct values of \(E\). This is a rapidly growing high-genus lifting problem, not something supplied by the positive rank of the original elliptic curve.

## Self-Audit

1. **Use of Nagell–Lutz.**  
   The proof of infinite rank depends on the standard Nagell–Lutz theorem. Its hypotheses hold because (3) is a nonsingular short Weierstrass equation with integral coefficients. The exact calculation \(x(2P)=3417/4\) then rules out torsion without any computational rank assumption.

2. **Passage from infinitely many elliptic points to infinitely many distinct positive \(R^2\).**  
   A birational map may exclude finitely many points, and different curve points can yield the same \(R\). However, the exceptional set is finite, while each fixed \(R^2\) has finitely many preimages because \(R(1-t^2)=12t\) is quadratic in \(t\). Thus infinitely many distinct \(R^2\) follow rigorously.

3. **The route diagnosis is not an impossibility theorem.**  
   Genus \(5\), Faltings, and conjectural uniformity explain why the fourth column is difficult, but they do not rule out arbitrarily large finite configurations with varying columns. I regard the diagnosis as compelling because Proposition 5 is rigorous, but it does not complete either a proof or a disproof.

## Computations To Verify

The following exact Python code verifies the elliptic curve, generates multiples of \(P\), converts them to rational rows, clears denominators, and checks the resulting integer square grid.

```python
from fractions import Fraction as F
from math import gcd, isqrt

A2 = F(-306)
A4 = F(-202500)
A6 = F(61965000)

def on_E(P):
    if P is None:
        return True
    u, v = P
    return v*v == (u - 306)*(u - 450)*(u + 450)

def ec_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2:
        if y1 + y2 == 0:
            return None
        assert y1 == y2
        if y1 == 0:
            return None
        slope = (3*x1*x1 + 2*A2*x1 + A4) / (2*y1)
    else:
        slope = (y2 - y1) / (x2 - x1)

    x3 = slope*slope - A2 - x1 - x2
    y3 = -y1 + slope*(x1 - x3)
    R = (x3, y3)
    assert on_E(R)
    return R

P = (F(3330), F(181440))
assert on_E(P)

P2 = ec_add(P, P)
assert P2[0] == F(3825, 4)
assert P2[1] == F(172125, 8)

def elliptic_to_row(P):
    """Return (R,H,K) with H^2=R^2+36 and K^2=R^2+225."""
    u, v = P
    den = u*u - 202500
    if den == 0:
        return None

    t = 30*v / den
    if t == 0 or t*t == 1:
        return None

    X = u / 30
    w = X*t*t - 15

    assert w*w == 225*t**4 - 306*t*t + 225

    R = 12*t / (1 - t*t)
    H = 6*(1 + t*t) / (1 - t*t)
    K = w / (1 - t*t)

    assert H*H == R*R + 36
    assert K*K == R*R + 225
    return (R, H, K)

row1 = elliptic_to_row(P)
row2 = elliptic_to_row(P2)

assert row1 == (F(8), F(10), F(17))
assert row2 == (
    F(61200, 1001),
    F(61494, 1001),
    F(63015, 1001)
)

def generate_rows(m):
    rows = []
    seen_squares = set()
    Q = None

    while len(rows) < m:
        Q = ec_add(Q, P)
        row = elliptic_to_row(Q)
        if row is None:
            continue
        R, H, K = row
        if R == 0 or R*R in seen_squares:
            continue
        seen_squares.add(R*R)
        rows.append(row)

    return rows

def lcm(a, b):
    return a // gcd(a, b) * b

def scale_and_verify(rows):
    L = 1
    for row in rows:
        for z in row:
            L = lcm(L, z.denominator)

    scaled = []
    for R, H, K in rows:
        r = abs(R) * L
        h = abs(H) * L
        k = abs(K) * L
        assert r.denominator == h.denominator == k.denominator == 1
        scaled.append((int(r), int(h), int(k)))

    Ns = [r*r for r, h, k in scaled]
    ds = [0, 12*L, 30*L]

    assert len(Ns) == len(set(Ns))
    assert len(ds) == len(set(ds))

    for N in Ns:
        for d in ds:
            q = 4*N + d*d
            x = isqrt(q)
            assert x*x == q

    return L, Ns, ds, scaled

rows = generate_rows(6)
L, Ns, ds, witnesses = scale_and_verify(rows)
print("scale =", L)
print("N rows =", Ns)
print("common differences =", ds)
```

The divisor-engineering count and the \(M=15\) failure of automatic third-column alignment can be checked by:

```python
def divisors(n):
    lo, hi = [], []
    a = 1
    while a*a <= n:
        if n % a == 0:
            lo.append(a)
            if a*a != n:
                hi.append(n // a)
        a += 1
    return lo + hi[::-1]

def difference_set(n):
    return {
        n // a - a
        for a in divisors(n)
        if a*a <= n
    }

def special_candidates(M):
    assert M % 2 == 1
    ans = []
    for A in divisors(M*M):
        B = M*M // A
        if A < B:
            assert (B - A) % 2 == 0
            r = (B - A) // 2
            h = (A + B) // 2
            assert h*h == r*r + M*M
            ans.append(r*r)
    assert len(ans) == (len(divisors(M*M)) - 1) // 2
    return ans

candidates = special_candidates(15)
common = set.intersection(*(difference_set(N) for N in candidates))

assert len(candidates) == 4
assert common == {0, 30}

print("candidate rows:", candidates)
print("full common intersection:", sorted(common))
```

A useful next experiment is to generate the first \(s\) elliptic rows, clear denominators, and compute whether their \(D(N_i)\) have any common differences beyond the three forced ones. Exact divisor factorization software should be used because the numbers grow rapidly.

## Route Diagnosis

**Proved ledger**

1. The first two columns are exactly controlled by admissible factor pairs of \(d_2^2-d_1^2\).
2. The pair \(0,2M\) can support arbitrarily many rows by choosing \(M\) with many divisors.
3. There are arbitrarily large configurations with \(m\) rows and the three common differences \(0,12Q,30Q\).
4. Every fixed set of four distinct rational columns defines a geometrically connected genus-\(5\) row curve and hence has only finitely many rational rows.
5. A full affirmative solution would produce genus-\(5\) curves over \(\mathbb Q\) with unboundedly many rational points.

**Plausible but unproved claims**

- Special choices of a fourth column and specially selected elliptic multiples might yield increasingly many rows. No mechanism forcing this was found.
- Standard uniformity conjectures suggest that an absolute bound should exist for four-column row curves, which would disprove the Erdős assertion. This remains conjectural and gives no explicit \(k_0\).

**Dead ends**

- A large divisor count for \(d_2^2-d_1^2\) alone does not force even one extra common difference; \(M=15\) already demonstrates complete failure beyond the initial pair.
- Keeping the three-column elliptic family fixed and adjoining one fixed fourth column cannot yield infinitely many rows, by Faltings.
- Positive rank on the three-column elliptic curve does not survive the new square condition: the lift is genus \(5\), and quotient points need not lift.

**Precise block**

Route 2 succeeds at selecting arbitrarily many factor pairs that align in one additional column. To reach the target, it must align those rows in arbitrarily many further columns. Already the first such extension would require genus-\(5\) curves with unboundedly many rational points as the parameters vary. That is an open problem of comparable or greater depth, so the route is BLOCKED rather than completed.

A fresh affirmative attempt should directly search for a special genus-\(5\) family with unbounded rational-point counts—probably via exceptional automorphisms or controlled low-genus quotients—and must verify simultaneous lifting. A fresh disproof attempt should seek an explicit uniform upper bound for rational points on the special curves
\[
Y_j^2=X^2+d_j^2-d_1^2,
\]
using the additional difference-of-squares and integrality structure; a general appeal to Faltings or conjectural uniformity is insufficient.