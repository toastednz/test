STATUS: BLOCKED

## Result

I obtained a complete description of the natural quotient structure of the multiquadratic curve attached to fixed columns. Its Jacobian is isogenous over \(\mathbb Q\) to a product of Jacobians of explicit even hyperelliptic curves, each of which splits further into two lower-genus factors. For five columns, the resulting genus-\(17\) curve has \(15\) automatic elliptic factors and one genus-\(2\) factor; under an explicit reciprocal condition on the four column shifts, that genus-\(2\) factor also splits, making the entire Jacobian isogenous to a product of \(17\) elliptic curves. This is a strong realization of Route 4 and explains why elliptic methods can remain relevant beyond \(k=4\). It does not solve the problem: positive rank on these quotients does not ensure rational points lift to the original curve, and arranging simultaneous lifts is exactly a transposed multiquadratic problem of comparable strength.

## Complete Argument

### 1. The fixed-column curve and its rational points

Let
\[
0\le d_1<d_2<\cdots<d_r
\]
be rational numbers, put
\[
a=d_1,\qquad c_j=d_{j+1}^2-a^2>0\quad(1\le j\le n:=r-1),
\]
and consider the normal projective model \(C_n\) of
\[
C_n:\qquad y_j^2=x^2+c_j,\quad 1\le j\le n. \tag{1}
\]

A rational point on \(C_n\) with \(x^2>a^2\) gives a rational row
\[
T=x^2-a^2>0
\]
because
\[
x^2=T+d_1^2,\qquad y_j^2=T+d_{j+1}^2.
\]
Distinct values of \(x^2\) give distinct \(T\). Conversely, every rational row for these columns gives a rational point of \(C_n\).

There is always a rational boundary point at
\[
x=a,\qquad y_j=d_{j+1},
\]
but it corresponds to \(T=0\), not to a positive \(N\).

Thus, for \(r\) fixed columns, the desired construction requires at least \(r\) rational points on \(C_{r-1}\) with distinct values of \(x^2>a^2\).

---

### 2. Smoothness, genus, and the tower of double covers

The function field of \(C_n\) is
\[
\mathbb Q(x)\bigl(\sqrt{x^2+c_1},\ldots,\sqrt{x^2+c_n}\bigr).
\]
The square classes of the functions \(x^2+c_j\) are independent over
\(\overline{\mathbb Q}(x)^\times/\overline{\mathbb Q}(x)^{\times2}\): if a nonempty product were a square, a zero of one factor \(x^2+c_j\) would occur with odd valuation, since the \(c_j\) are nonzero and pairwise distinct. Hence
\[
[C_n:\mathbb P^1_x]=2^n
\]
and its deck group is
\[
G\cong(\mathbb Z/2\mathbb Z)^n.
\]

The branch points on \(\mathbb P^1_x\) are
\[
x=\pm\sqrt{-c_j},\qquad 1\le j\le n.
\]
There are \(2n\) distinct geometric branch points. Above each, there are \(2^{n-1}\) points of ramification index \(2\). There is no ramification above infinity because each \(x^2+c_j\) has a pole of even order there.

Riemann–Hurwitz gives
\[
2g(C_n)-2
=-2\cdot 2^n+(2n)2^{n-1}
=2^n(n-2).
\]
Therefore
\[
\boxed{g(C_n)=1+2^{n-1}(n-2).} \tag{2}
\]

Equivalently, for \(r=n+1\) columns,
\[
g=1+2^{r-2}(r-3).
\]

There is also a useful tower
\[
C_n\longrightarrow C_{n-1}
\]
obtained by forgetting \(y_n\). It is a degree-\(2\) cover obtained by adjoining
\[
\sqrt{x^2+c_n}.
\]
The zeros of \(x^2+c_n\) lift to
\[
2\cdot 2^{n-1}=2^n
\]
distinct points of \(C_{n-1}\), all simple zeros, while its poles have even order. Thus this map is branched at exactly \(2^n\) geometric points.

In particular,
\[
C_2\ \text{has genus }1,
\]
but
\[
C_3\longrightarrow C_2
\]
is branched at eight points and \(C_3\) has genus \(5\). Consequently, adding a third nontrivial square condition is never an unramified isogeny in the nondegenerate setting.

---

### 3. Complete natural Jacobian decomposition

For every nonempty subset \(S\subseteq\{1,\ldots,n\}\), define
\[
H_S:\qquad z_S^2=\prod_{j\in S}(x^2+c_j). \tag{3}
\]
If \(m=|S|\), then \(H_S\) is a hyperelliptic curve defined by a squarefree polynomial of degree \(2m\), so
\[
g(H_S)=m-1. \tag{4}
\]

Let
\[
\chi_S:G\longrightarrow\{\pm1\},
\qquad
\chi_S(\varepsilon_1,\ldots,\varepsilon_n)
=\prod_{j\in S}\varepsilon_j.
\]
The quotient of \(C_n\) by \(\ker\chi_S\) is \(H_S\), via
\[
z_S=\prod_{j\in S}y_j.
\]

The pullbacks of the holomorphic differentials on \(H_S\) lie in the \(\chi_S\)-eigenspace of \(H^0(C_n,\Omega^1)\). Since the quotient by all of \(G\) is \(\mathbb P^1\), the trivial eigenspace is zero. Moreover,
\[
\sum_{\varnothing\ne S\subseteq[n]}g(H_S)
=\sum_{\varnothing\ne S}(|S|-1)
=n2^{n-1}-(2^n-1)
=1+2^{n-1}(n-2),
\]
which equals \(g(C_n)\).

It follows that the pullbacks of the differentials from all \(H_S\) form a direct sum equal to \(H^0(C_n,\Omega^1)\). Therefore the induced homomorphism
\[
\prod_{\varnothing\ne S\subseteq[n]}\operatorname{Jac}(H_S)
\longrightarrow \operatorname{Jac}(C_n)
\]
has an isomorphism on tangent spaces and equal-dimensional source and target. Hence it is an isogeny:

\[
\boxed{
\operatorname{Jac}(C_n)
\sim_{\mathbb Q}
\prod_{\substack{\varnothing\ne S\subseteq[n]\\|S|\ge2}}
\operatorname{Jac}(H_S).
} \tag{5}
\]

The singleton factors have genus zero and may be omitted.

---

### 4. Splitting each even hyperelliptic factor

Write
\[
P_S(u)=\prod_{j\in S}(u+c_j),\qquad m=|S|.
\]
The curve
\[
H_S:\quad z^2=P_S(x^2)
\]
has involutions
\[
\sigma:(x,z)\mapsto(-x,z)
\]
and
\[
\tau:(x,z)\mapsto(-x,-z).
\]

Their quotient curves are
\[
A_S:\qquad v^2=P_S(u),\quad u=x^2, \tag{6}
\]
and
\[
B_S:\qquad w^2=uP_S(u),\quad u=x^2,\quad w=xz. \tag{7}
\]

Their genera are
\[
g(A_S)=\left\lfloor\frac{m-1}{2}\right\rfloor,\qquad
g(B_S)=\left\lfloor\frac m2\right\rfloor,
\]
whose sum is \(m-1=g(H_S)\).

This splitting can be checked directly on differentials. A basis of
\(H^0(H_S,\Omega^1)\) is
\[
\frac{x^k\,dx}{z},\qquad 0\le k\le m-2.
\]
The pullbacks from \(A_S\) are the odd-\(k\) differentials:
\[
\frac{u^\ell\,du}{v}
=\frac{2x^{2\ell+1}\,dx}{z},
\]
while the pullbacks from \(B_S\) are the even-\(k\) differentials:
\[
\frac{u^\ell\,du}{w}
=\frac{2x^{2\ell}\,dx}{z}.
\]
They span complementary subspaces. Therefore
\[
\boxed{
\operatorname{Jac}(H_S)
\sim_{\mathbb Q}
\operatorname{Jac}(A_S)\times\operatorname{Jac}(B_S).
} \tag{8}
\]

Combining (5) and (8) decomposes the exponentially large Jacobian of \(C_n\) into Jacobians of hyperelliptic curves of genus at most \(\lfloor n/2\rfloor\).

For small subset sizes:

- \(m=2\): \(A_S\) has genus \(0\), \(B_S\) is elliptic;
- \(m=3\): both \(A_S\) and \(B_S\) are elliptic;
- \(m=4\): \(A_S\) is elliptic and \(B_S\) has genus \(2\).

For \(n=3\), corresponding to four columns, every factor is elliptic. Indeed,
\[
3\binom{3}{2}\text{-subset dimensions}+\text{the two triple factors}
=3+2=5=g(C_3).
\]
This gives a structural explanation for the effectiveness of elliptic methods in the known \(k=4\) case.

---

### 5. Five columns: only one genus-\(2\) obstruction remains

For five columns, \(n=4\) and
\[
g(C_4)=1+2^3\cdot2=17.
\]
The decomposition has:

- six elliptic factors from the six \(2\)-subsets;
- eight elliptic factors from the four \(3\)-subsets;
- one elliptic factor \(A_{\{1,2,3,4\}}\);
- one genus-\(2\) factor
  \[
  B_{\{1,2,3,4\}}:\quad
  w^2=u\prod_{i=1}^4(u+c_i). \tag{9}
  \]

Thus
\[
\operatorname{Jac}(C_4)
\sim
E_1\times\cdots\times E_{15}\times\operatorname{Jac}(B_{\{1,2,3,4\}}),
\]
where the remaining Jacobian has dimension \(2\).

That last factor also splits under an explicit reciprocal condition.

---

### 6. Reciprocal splitting of the remaining genus-\(2\) factor

Assume, after relabeling, that
\[
c_1c_2=c_3c_4=K=s^2,\qquad s\in\mathbb Q_{>0}. \tag{10}
\]
Set
\[
\alpha=c_1+c_2,\qquad \beta=c_3+c_4.
\]
Then (9) becomes
\[
w^2
=u(u^2+\alpha u+K)(u^2+\beta u+K). \tag{11}
\]

Put
\[
v=u+\frac Ku.
\]
Since
\[
u^2+\alpha u+K=u(v+\alpha),
\]
and similarly for \(\beta\), equation (11) becomes
\[
w^2=u^3(v+\alpha)(v+\beta). \tag{12}
\]

Define
\[
W_+=\frac{w(u+s)}{u^2},
\qquad
W_-=\frac{w(u-s)}{u^2}.
\]
Using \(K=s^2\),
\[
\frac{(u\pm s)^2}{u}
=u+\frac{s^2}{u}\pm2s
=v\pm2s.
\]
Therefore
\[
W_+^2=(v+2s)(v+\alpha)(v+\beta), \tag{13}
\]
and
\[
W_-^2=(v-2s)(v+\alpha)(v+\beta). \tag{14}
\]

These are elliptic curves
\[
E_+:\quad W_+^2=(v+2s)(v+\alpha)(v+\beta),
\]
\[
E_-:\quad W_-^2=(v-2s)(v+\alpha)(v+\beta).
\]

The underlying involution on (11) is
\[
\iota:(u,w)\longmapsto
\left(\frac Ku,\frac{s^3w}{u^3}\right).
\]
Equation (13) is the quotient by \(\iota\), while (14) is the quotient by the product of \(\iota\) and the hyperelliptic involution. The two quotient pullbacks span the two-dimensional differential space of the genus-\(2\) curve, hence
\[
\boxed{
\operatorname{Jac}(B_{\{1,2,3,4\}})
\sim_{\mathbb Q}E_+\times E_-.
} \tag{15}
\]

Because the \(c_i\) are positive and distinct, \(\alpha,\beta>2s\) and \(\alpha\ne\beta\), so the cubics in (13) and (14) have distinct roots.

Combining all factors gives:

\[
\boxed{
c_1c_2=c_3c_4=s^2
\quad\Longrightarrow\quad
\operatorname{Jac}(C_4)
\text{ is isogenous over }\mathbb Q
\text{ to a product of }17\text{ elliptic curves}.
} \tag{16}
\]

An explicit valid column family is obtained by taking \(d_1=0\) and
\[
(d_2,d_3,d_4,d_5)
=\left(p,q,r,\frac{pq}{r}\right).
\]
Then
\[
(c_1,c_2,c_3,c_4)
=\left(p^2,q^2,r^2,\frac{p^2q^2}{r^2}\right),
\]
with
\[
c_1c_2=c_3c_4=(pq)^2.
\]

For example, the columns
\[
\{0,1,2,3,6\}
\]
give shifts
\[
\{1,4,9,36\},
\]
paired as
\[
1\cdot36=4\cdot9=36.
\]
Here \(s=6\), \(\alpha=37\), and \(\beta=13\), so the final genus-\(2\) factor splits into
\[
W_+^2=(v+12)(v+37)(v+13)
\]
and
\[
W_-^2=(v-12)(v+37)(v+13).
\]

This proves complete elliptic decomposability of the Jacobian, but it does not prove the existence of even one positive row for these particular columns.

---

### 7. Why positive-rank elliptic quotients do not solve the lifting problem

For \(n\ge3\), equation (2) gives \(g(C_n)>1\). By Faltings’ theorem,
\[
C_n(\mathbb Q)
\]
is finite for every fixed nondegenerate choice of the \(c_j\).

Therefore, if
\[
\pi:C_n\longrightarrow E
\]
is any elliptic quotient, then even when \(E(\mathbb Q)\) has positive rank, only finitely many points of \(E(\mathbb Q)\) can lift to \(C_n(\mathbb Q)\). Positive rank of \(E\) does not produce an infinite liftable subset.

The tower calculation makes the obstruction explicit. Starting from the genus-\(1\) curve \(C_2\), adding a third nontrivial square condition gives a degree-\(2\) cover
\[
C_3\longrightarrow C_2
\]
branched at eight points. It is therefore a genus-\(5\) curve, not an elliptic curve isogenous to \(C_2\).

Faltings does not settle the Erdős problem because the curve varies with the columns and only finitely many points are required. It does, however, rule out the proposed mechanism in which an infinite positive-rank subgroup of an elliptic quotient lifts through all remaining covers.

---

### 8. Selecting liftable elliptic points transposes the original problem

Suppose a chosen elliptic quotient supplies rational points whose corresponding \(x\)-coordinates have distinct squares
\[
q_1,\ldots,q_M,
\qquad q_i=x_i^2>a^2.
\]
To add a new column shift \(c>0\), one needs
\[
q_i+c=z_i^2\qquad(1\le i\le M)
\]
and also
\[
a^2+c=z_0^2,
\]
so that the new column itself is rational.

Eliminating \(c=z_0^2-a^2\), these become
\[
z_i^2=z_0^2+(q_i-a^2),\qquad 1\le i\le M. \tag{17}
\]
Because the \(q_i\) are distinct and exceed \(a^2\), this is another nondegenerate multiquadratic curve, now of genus
\[
1+2^{M-1}(M-2).
\]

Moreover, rational points \(z_0\) on (17) are exactly admissible new columns, and distinct values of \(z_0^2\) give distinct columns. Thus constructing many extra columns that split over selected elliptic points is literally the row-column transpose of the original square-grid problem.

This is the precise block: the lifting condition does not reduce to elliptic arithmetic; it recreates a multiquadratic problem of comparable strength.

---

### 9. Limit of the reciprocal strategy

The reciprocal condition for a four-set says that its elements can be paired with equal products. This particular recipe cannot be imposed on every four-subset of five distinct positive shifts.

Indeed, let
\[
0<c_1<c_2<c_3<c_4
\]
and put \(x_i=\log c_i\). Among the three possible pairings, the equal-product condition can only be
\[
x_1+x_4=x_2+x_3.
\]
The alternatives
\[
x_1+x_2=x_3+x_4
\]
and
\[
x_1+x_3=x_2+x_4
\]
are impossible by strict ordering.

Now suppose \(0<c_1<\cdots<c_5\) and every four-subset admitted such a pairing. Applying the preceding observation to
\(\{c_1,c_2,c_3,c_4\}\) gives
\[
x_1+x_4=x_2+x_3,
\]
while applying it to \(\{c_1,c_2,c_3,c_5\}\) gives
\[
x_1+x_5=x_2+x_3.
\]
Hence \(x_4=x_5\), a contradiction.

Thus the simple reciprocal splitting mechanism does not scale by forcing every four-subset factor to split in the same way. This does not rule out other genus-\(2\) involutions or more global decompositions.

---

### 10. A bound on rational branch-automorphism amplification

Let
\[
\mathcal B=\{\pm\sqrt{-c_j}:1\le j\le n\}\subset\mathbb P^1(\overline{\mathbb Q})
\]
and let
\[
\Gamma=\{\phi\in\operatorname{PGL}_2(\mathbb Q):\phi(\mathcal B)=\mathcal B\}.
\]
For \(n\ge2\), this is finite because an element fixing three points is the identity.

There is a uniform, though crude, bound on \(|\Gamma|\). The adjoint representation embeds
\[
\operatorname{PGL}_2(\mathbb Q)\hookrightarrow
\operatorname{GL}(\mathfrak{sl}_2(\mathbb Q))
\cong\operatorname{GL}_3(\mathbb Q).
\]
Every finite subgroup of \(\operatorname{GL}_3(\mathbb Q)\) preserves some full lattice, hence is conjugate into \(\operatorname{GL}_3(\mathbb Z)\). Reduction modulo \(3\) is injective on finite subgroups of \(\operatorname{GL}_3(\mathbb Z)\): the principal congruence subgroup modulo \(3\) is torsion-free, as follows by expanding
\[
(I+3^mA)^q
\]
for an element of prime order \(q\).

Consequently,
\[
|\Gamma|\le |\operatorname{GL}_3(\mathbb F_3)|
=(27-1)(27-3)(27-9)=11232. \tag{18}
\]

Thus no construction that obtains all row values from the orbit of one point under rational automorphisms descending to the \(x\)-line can give unbounded grid sizes. This does not cover automorphisms that fail to descend to the \(x\)-line, nor does it bound unrelated rational points.

## Self-Audit

1. **The Jacobian decompositions involve normalizations and points at infinity.**  
   These are the most technically delicate statements. I believe they are correct because the quotient function fields are explicit, the differential eigenspaces are explicit, and their dimensions sum exactly to the genus. A homomorphism of equal-dimensional abelian varieties whose differential is an isomorphism is an isogeny.

2. **The reciprocal genus-\(2\) splitting is strong but says nothing by itself about rational points on the genus-\(17\) curve.**  
   This is not a hidden gap: equations (13)–(15) prove only a Jacobian isogeny. Rational points on a curve do not decompose as products of rational points on its Jacobian factors. I have deliberately made no \(P(5)\) claim.

3. **The route diagnosis is not an impossibility theorem for Route 4 as a whole.**  
   It rules out infinite lifting from a fixed elliptic quotient, shows exact transposition of the finite lifting problem, and bounds one automorphism-orbit mechanism. A different parameterized family with many independently constructed rational sections could still succeed. This limitation is why the status is BLOCKED rather than SOLVED-DISPROOF.

## Computations To Verify

### 1. Exact rational search in the completely split five-column family

This searches families
\[
d=\left\{0,p,q,r,\frac{pq}{r}\right\}
\]
and rational \(x\) of bounded height.

```python
from fractions import Fraction
from math import gcd, isqrt
from itertools import combinations

def is_qsquare(z):
    z = Fraction(z)
    if z < 0:
        return False
    a, b = z.numerator, z.denominator
    ra, rb = isqrt(a), isqrt(b)
    return ra * ra == a and rb * rb == b

def positive_rationals(H):
    R = set()
    for den in range(1, H + 1):
        for num in range(1, H + 1):
            if gcd(num, den) == 1:
                R.add(Fraction(num, den))
    return sorted(R)

def common_x_levels(ds, H):
    """Return distinct x^2 with x of numerator/denominator <= H."""
    levels = set()
    for x in positive_rationals(H):
        if all(is_qsquare(x*x + d*d) for d in ds):
            levels.add(x*x)
    return sorted(levels)

def search_reciprocal_family(param_height=15, x_height=100):
    R = positive_rationals(param_height)
    best = (0, None, None)

    for p, q, r in combinations(R, 3):
        fourth = p*q/r
        ds = (p, q, r, fourth)

        if len(set(ds)) != 4:
            continue

        levels = common_x_levels(ds, x_height)
        if len(levels) > best[0]:
            best = (len(levels), ds, levels)
            print("new best:", best)

        if len(levels) >= 5:
            # Rational P(5) witness with columns [0] + ds and T_i=levels[i].
            print("RATIONAL P(5) CANDIDATE")
            print("columns =", (Fraction(0),) + ds)
            print("T values =", levels[:5])
            return ds, levels[:5]

    return best
```

Every reported candidate should be rechecked by:

```python
def verify_rational_grid(Ts, ds):
    columns = (Fraction(0),) + tuple(ds)
    assert len(set(Ts)) == len(Ts)
    assert len(set(columns)) == len(columns)
    assert all(T > 0 for T in Ts)
    assert all(d >= 0 for d in columns)

    for T in Ts:
        for d in columns:
            assert is_qsquare(T + d*d)
    return True
```

---

### 2. Exact verification of the reciprocal quotient identities in SageMath

```python
Q = QQ
R.<u> = PolynomialRing(QQ)

c1, c2, c3, c4 = QQ(1), QQ(36), QQ(4), QQ(9)
K = c1*c2
s = QQ(6)
alpha = c1 + c2
beta  = c3 + c4

assert c3*c4 == K
assert s*s == K

F = u*(u+c1)*(u+c2)*(u+c3)*(u+c4)
v = u + K/u

lhs_plus  = F*(u+s)^2/u^4
rhs_plus  = (v+2*s)*(v+alpha)*(v+beta)

lhs_minus = F*(u-s)^2/u^4
rhs_minus = (v-2*s)*(v+alpha)*(v+beta)

assert (lhs_plus-rhs_plus).simplify_rational() == 0
assert (lhs_minus-rhs_minus).simplify_rational() == 0
```

---

### 3. Construct the seventeen elliptic factors and compute rank bounds

```python
from itertools import combinations

R.<u> = PolynomialRing(QQ)
c = [QQ(1), QQ(36), QQ(4), QQ(9)]

def elliptic_from_cubic(f):
    """
    For y^2 = a*x^3+b*x^2+c*x+d, use
    X=a*x, Y=a*y:
    Y^2 = X^3+b*X^2+a*c*X+a^2*d.
    """
    f = R(f)
    assert f.degree() == 3
    a, b, cc, d = f[3], f[2], f[1], f[0]
    return EllipticCurve(QQ, [0, b, 0, a*cc, a*a*d])

def quartic_to_cubic(f, root):
    """
    If f(root)=0, substitute u=root+1/X and multiply by X^4.
    """
    T.<t> = PolynomialRing(QQ)
    X.<X> = PolynomialRing(QQ)
    h = T(f(root + t))
    assert h[0] == 0
    g = sum(h[k] * X**(4-k) for k in range(1, 5))
    assert g.degree() == 3
    return g

elliptic_factors = []

# |S| = 2: B_S is cubic elliptic.
for S in combinations(range(4), 2):
    fA = prod(u + c[i] for i in S)
    fB = u*fA
    elliptic_factors.append(elliptic_from_cubic(fB))

# |S| = 3: A_S cubic; B_S quartic.
for S in combinations(range(4), 3):
    fA = prod(u + c[i] for i in S)
    fB = u*fA
    elliptic_factors.append(elliptic_from_cubic(fA))
    gB = quartic_to_cubic(fB, QQ(0))
    elliptic_factors.append(elliptic_from_cubic(gB))

# |S| = 4: A_S quartic.
fA4 = prod(u + ci for ci in c)
gA4 = quartic_to_cubic(fA4, -c[0])
elliptic_factors.append(elliptic_from_cubic(gA4))

# Reciprocal splitting of B_S into E+ and E-.
s = QQ(6)
alpha = QQ(37)
beta = QQ(13)

fplus  = (u + 2*s)*(u + alpha)*(u + beta)
fminus = (u - 2*s)*(u + alpha)*(u + beta)

elliptic_factors.append(elliptic_from_cubic(fplus))
elliptic_factors.append(elliptic_from_cubic(fminus))

assert len(elliptic_factors) == 17

for i, E in enumerate(elliptic_factors, 1):
    print(i, E)
    try:
        print("rank bounds:", E.rank_bounds())
    except Exception as err:
        print("rank computation failed:", err)
```

A useful follow-up is to compute generators, Selmer groups, and images of known points under every quotient map. Positive ranks alone are not enough; every proposed full-curve point must still be checked directly.

---

### 4. Verify the genus and dimension sums

```python
from math import comb

for n in range(1, 12):
    genus = 1 + 2**(n-1)*(n-2)
    quotient_sum = sum(comb(n, m)*(m-1) for m in range(2, n+1))
    assert genus == quotient_sum

    split_sum = 0
    for m in range(2, n+1):
        gA = (m-1)//2
        gB = m//2
        assert gA + gB == m-1
        split_sum += comb(n, m)*(gA+gB)

    assert split_sum == genus
    print(n, genus)
```

## Route Diagnosis

### What worked

- The multiquadratic curve has a fully explicit character-quotient decomposition.
- Every natural hyperelliptic quotient splits further because its defining polynomial is even.
- For \(k=4\), the genus-\(5\) Jacobian is automatically completely elliptic.
- For \(k=5\), only one genus-\(2\) factor remains.
- The reciprocal condition
  \[
  c_1c_2=c_3c_4=s^2
  \]
  splits that factor and produces a genus-\(17\) curve with completely decomposable Jacobian.

### Precise block

The missing statement is not a Jacobian decomposition or a rank computation. One must prove that the original high-genus curve has at least \(r\) rational points with distinct positive \(x^2-a^2\). Positive rank on any quotient does not imply this. Requiring selected quotient points to lift through the remaining square conditions produces the transposed multiquadratic curve (17), of comparable genus and difficulty. Thus Route 4 currently reduces the problem to another instance of essentially the same problem.

### Ledger

**Proved lemmas**

1. The fixed-column curve \(C_n\) has genus \(1+2^{n-1}(n-2)\).
2. The forgetful map \(C_n\to C_{n-1}\) is branched at exactly \(2^n\) geometric points.
3. The character decomposition (5) of \(\operatorname{Jac}(C_n)\).
4. The even-polynomial splitting (8) of every factor.
5. For five columns, there are \(15\) automatic elliptic factors and one genus-\(2\) factor.
6. Under \(c_1c_2=c_3c_4=s^2\), the genus-\(2\) factor splits into the explicit curves \(E_\pm\).
7. Selecting simultaneous lifts of prescribed row points is exactly a transposed multiquadratic problem.
8. The simple reciprocal recipe cannot hold for every four-subset of five distinct positive shifts.
9. Rational automorphisms descending to the \(x\)-line have uniformly bounded orbit size.

**Plausible but unproved**

- Some reciprocal five-column family may contain five positive rational row levels and yield a \(P(5)\) example.
- Special higher-dimensional branch configurations may make all low-genus factors split further.
- A parameterized family might possess finitely many explicit rational sections whose number grows with the number of columns.

**Dead ends**

- Infinite lifting from a positive-rank elliptic quotient: impossible for a fixed nondegenerate curve of genus \(>1\).
- Amplification from one rational point using a single reciprocal involution: it produces at most two finite \(x^2\)-levels per orbit.
- Scaling the reciprocal genus-\(2\) splitting by imposing equal-product pairings on every four-subset: impossible for five distinct positive shifts.
- Merely proving complete decomposability of the Jacobian: insufficient to produce rational points on the curve.

A fresh Route 4 attempt should search for a parameter family with explicitly constructed rational sections, not merely elliptic factors of positive rank. For \(k=5\), the reciprocal two-parameter family is the sharpest test bed: exact rank computations, elliptic Chabauty, and direct lifting searches are realistic. For unbounded \(k\), an affirmative solution would require a new mechanism forcing a growing finite set of quotient points to split simultaneously without recreating the transposed square-grid problem.