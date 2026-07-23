STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #660. Route 4 is blocked at two independent points: the required spherical estimate \(n\le 2s+o(s)\) remains unproved, and even such an estimate would not presently reduce general convex polytopes to the spherical case. I did prove a substantial symmetric spherical special case. If \(X\subset S^2\) is invariant under a rotation of order \(m\) and consists of \(q\) free cyclic orbits, plus possibly the two poles, then
\[
D(X)\ge \frac{qm}{2}-O(q^2).
\]
Consequently, whenever \(q=o(m)\),
\[
D(X)\ge \left(\frac12-o(1)\right)|X|.
\]
This rules out the proposed fixed-\(q\) cyclic/dihedral multi-orbit counterexample route. In particular, all unbounded vertex-transitive spherical families satisfy the conjectured asymptotic. The key input is the uniform torsion-point theorem for bounded-degree curves in \((\mathbb C^\times)^2\), which implies that two distinct affine cosine spectra have only \(O(1)\) common values. I also prove that a general convex polytope cannot be reduced by simply extracting a bounded number of exact concentric spherical layers: there are convex \(n\)-vertex configurations for which no five vertices are cospherical.

## Complete Argument

### 1. Why the standard spherical-harmonic argument stops at a quadratic bound

Let \(X=\{x_1,\dots,x_n\}\subset S^2\), and suppose its distinct inner products between different points are
\[
A=\{a_1,\dots,a_s\}.
\]
The number \(s\) is also the number of distinct positive chordal distances, since
\[
\|x-y\|^2=2-2x\cdot y.
\]

For each \(i\), define the polynomial function on \(S^2\)
\[
F_i(y)=\prod_{a\in A}(x_i\cdot y-a).
\]
If \(j\ne i\), then \(x_i\cdot x_j\in A\), so \(F_i(x_j)=0\). On the other hand,
\[
F_i(x_i)=\prod_{a\in A}(1-a)\ne0,
\]
because \(a<1\) for distinct unit vectors. Hence the restrictions \(F_i|_{S^2}\) are linearly independent.

Every \(F_i\) is the restriction of a polynomial of degree at most \(s\). The space of polynomial functions on \(S^2\) of degree at most \(s\) has dimension
\[
\sum_{\ell=0}^s(2\ell+1)=(s+1)^2.
\]
Therefore
\[
n\le (s+1)^2.
\]

This recovers the standard absolute bound. It does not approach the desired \(n\le2s+o(s)\). Moreover, every point of every finite subset of \(S^2\) is exposed: for distinct \(x,y\in S^2\),
\[
x\cdot x=1>x\cdot y.
\]
Thus convexity contributes no additional restriction inside the spherical subclass that can simply be appended to this interpolation argument.

---

### 2. A uniform overlap lemma for affine cosine spectra

For \(m\ge2\), let \(\mu_m\) denote the group of \(m\)-th roots of unity. Given \(A\in\mathbb R\), \(B>0\), and \(\rho\in S^1\), define
\[
\Sigma_m(A,B,\rho)
 =
 \left\{
 A-B\operatorname{Re}(\rho u):u\in\mu_m
 \right\}.
\]

The following established theorem is the only deep external input used below.

#### Uniform torsion-curve theorem

For every degree bound \(d\), there is a constant \(T(d)\) with the following property. If an algebraic curve
\[
C\subset(\mathbb C^\times)^2
\]
of degree at most \(d\) contains no translate of a positive-dimensional algebraic subtorus by a torsion point, then \(C\) contains at most \(T(d)\) torsion points.

This is the uniform bounded-degree torsion-point theorem for curves in a two-dimensional torus, due in this form to Beukers–Smyth and related uniform torsion results. Only the existence of \(T(3)\) is needed.

#### Lemma 2.1: Uniform spectral overlap

There is an absolute constant \(C_0\) such that, for every \(m\), every \(\rho,\sigma\in S^1\), and every two distinct parameter pairs
\[
(A,B)\ne(A',B'),\qquad B,B'>0,
\]
one has
\[
\left|
\Sigma_m(A,B,\rho)\cap
\Sigma_m(A',B',\sigma)
\right|
\le C_0.
\]

#### Proof

A common value gives \(u,v\in\mu_m\) satisfying
\[
A-\frac B2(\rho u+\rho^{-1}u^{-1})
=
A'-\frac {B'}2(\sigma v+\sigma^{-1}v^{-1}).
\]
Thus \((u,v)\) is a torsion point on the Laurent curve
\[
A-A'
-\frac B2(\rho U+\rho^{-1}U^{-1})
+\frac {B'}2(\sigma V+\sigma^{-1}V^{-1})
=0. \tag{2.1}
\]
After multiplication by \(UV\), this becomes an ordinary polynomial curve of total degree at most \(3\).

It remains to prove that, when \((A,B)\ne(A',B')\), the curve contains no positive-dimensional torsion coset. Such a coset has a parametrization
\[
U=\xi T^p,\qquad V=\eta T^q,
\]
where \(\xi,\eta\) are roots of unity, \(p,q\in\mathbb Z\) are coprime, and not both zero.

Substitution into (2.1) must give an identity in \(T\).

If \(p=0\), the nonzero coefficients of \(T^{q}\) and \(T^{-q}\) coming from the \(V\)-terms cannot vanish. Thus \(p\ne0\), and similarly \(q\ne0\).

The nonconstant exponents are \(\pm p,\pm q\). If \(|p|\ne|q|\), at least one of these exponents occurs only once, with nonzero coefficient, so no identity is possible. Therefore
\[
|p|=|q|.
\]
Since \(p,q\) are coprime,
\[
|p|=|q|=1.
\]

The constant coefficient then forces
\[
A=A'.
\]
Cancellation of the coefficients of \(T\) and \(T^{-1}\) forces, after taking absolute values,
\[
B=B',
\]
because \(\rho,\sigma,\xi,\eta\) all have modulus one. This contradicts \((A,B)\ne(A',B')\).

The curve therefore has no positive-dimensional torsion coset. The uniform torsion-curve theorem, with degree \(3\), bounds its torsion points by \(T(3)\). Choosing one representing pair \((u,v)\) for each common spectral value gives an injection from common values to torsion points. Hence the intersection has cardinality at most
\[
C_0:=T(3).
\]
∎

The important feature is that \(C_0\) is independent of \(m\), the phases, and all metric parameters.

---

### 3. Elementary structure of phase-shifted cosine grids

Let
\[
H_m=\left\{\frac{k}{m}\pmod 1:0\le k<m\right\}\subset\mathbb R/\mathbb Z.
\]

#### Lemma 3.1: Difference-set size

Let \(P,Q\subset\mathbb R/\mathbb Z\) be unions of respectively \(p\) and \(q\) distinct cosets modulo \(H_m\), represented by \(p\) and \(q\) points of the quotient \((\mathbb R/\mathbb Z)/H_m\). Then
\[
(P-Q)+H_m
\]
contains at least \(\max(p,q)\) distinct \(H_m\)-cosets. Consequently,
\[
\left|
\left\{
\cos(2\pi\theta):
\theta\in(P-Q)+H_m
\right\}
\right|
\ge \frac{\max(p,q)m}{2}.
\]

For \(P=Q\), after deleting the value corresponding to zero angular difference,
\[
\#\{\text{positive chord lengths within }P+H_m\}
\ge \frac{pm}{2}-1.
\]

#### Proof

Fix \(q_0\in Q\). The \(p\) quotient classes \(P-q_0\) remain distinct, so \(P-Q\) contains at least \(p\) quotient classes. Similarly it contains at least \(q\), proving the first assertion.

Each \(H_m\)-coset contains exactly \(m\) angular values. The map
\[
\theta\longmapsto\cos(2\pi\theta)
\]
has fibers of size at most two, since equal cosines imply \(\theta\equiv\pm\theta'\pmod1\). Thus \(L\) angular cosets determine at least \(Lm/2\) cosine values.

For \(P=Q\), the cosine value \(1\), corresponding to angular difference zero, may arise only from a point paired with itself when all input points are distinct on the same latitude. Deleting it loses at most one value. ∎

#### Lemma 3.2: Equal-or-disjoint grids with the same affine parameters

For \(\rho,\sigma\in S^1\), the two cosine sets
\[
\{\operatorname{Re}(\rho u):u\in\mu_m\},
\qquad
\{\operatorname{Re}(\sigma v):v\in\mu_m\}
\]
are either equal or disjoint.

#### Proof

If they have a common value, then for some \(u,v\in\mu_m\),
\[
\operatorname{Re}(\rho u)=\operatorname{Re}(\sigma v).
\]
Two points on the unit circle with equal real part are equal or complex conjugates. Hence
\[
\rho u=\sigma v
\quad\text{or}\quad
\rho u=\overline{\sigma v}.
\]
In the first case \(\rho\mu_m=\sigma\mu_m\); in the second,
\[
\rho\mu_m=\overline{\sigma\mu_m}.
\]
Either relation implies equality of the two real-part sets. ∎

---

### 4. Spherical configurations with a common cyclic symmetry

Consider a finite set \(X\subset S^2\) invariant under rotation by \(2\pi/m\) around the \(z\)-axis. Assume that \(X\) consists of \(q\) free orbits of size \(m\), together with possibly one or both poles.

Every free orbit has the form
\[
X_a=
\left\{
\left(
r_a\cos 2\pi(\theta_a+k/m),
r_a\sin 2\pi(\theta_a+k/m),
z_a
\right):
0\le k<m
\right\},
\]
where
\[
r_a>0,\qquad r_a^2+z_a^2=1.
\]

#### Theorem 4.1: Cyclic multi-orbit lower bound

There is an absolute constant \(C_0\) such that
\[
D(X)\ge
\frac{qm}{2}-q-C_0\binom q2.
\]
If \(p\in\{0,1,2\}\) poles are also present, then \(n=qm+p\) and hence
\[
D(X)\ge
\frac n2-\frac p2-q-C_0\binom q2.
\]

In particular, for any sequence with \(q=o(m)\),
\[
D(X)\ge\left(\frac12-o(1)\right)|X|.
\]

#### Proof

Group the free orbits according to their common horizontal radius \(r\). For a fixed \(r\), put
\[
z=\sqrt{1-r^2}.
\]
Let \(p_r\) be the number of orbits at height \(+z\), and \(t_r\) the number at height \(-z\). If \(z=0\), these are the same latitude, and all orbits are put into one of the two groups. Write
\[
q_r=p_r+t_r,
\qquad
\sum_r q_r=q.
\]

For two points on the same latitude with radius \(r\) and angular difference \(\alpha\), the squared distance is
\[
2r^2-2r^2\cos\alpha. \tag{4.1}
\]
Thus all same-latitude spectra have affine cosine parameters
\[
W_r=(A,B)=(2r^2,2r^2). \tag{4.2}
\]

For two points on opposite latitudes \(+z\) and \(-z\), the squared distance is
\[
2+2z^2-2r^2\cos\alpha
=
(4-2r^2)-2r^2\cos\alpha. \tag{4.3}
\]
Thus all opposite-latitude spectra have parameters
\[
C_r=(A,B)=(4-2r^2,2r^2). \tag{4.4}
\]

These parameter pairs are all distinct among the spectra that will be used:

1. \(W_r=W_s\) implies \(r=s\).
2. \(C_r=C_s\) implies \(r=s\).
3. \(W_r=C_s\) first forces \(r=s\) from equality of the \(B\)-coordinates, and then
   \[
   2r^2=4-2r^2,
   \]
   so \(r=1\). But then \(z=0\), and no opposite-latitude spectrum \(C_r\) exists.

Fix a radius \(r\).

If only one latitude is present, Lemma 3.1 gives at least
\[
\frac{q_rm}{2}-1 \tag{4.5}
\]
same-latitude positive squared distances.

Suppose both latitudes are present, and without loss of generality
\[
p_r\ge t_r.
\]
The distances within the upper latitude give at least
\[
\frac{p_rm}{2}-1 \tag{4.6}
\]
values. The upper-to-lower distances arise from the angular difference set between \(p_r\) and \(t_r\) phase cosets. Lemma 3.1 gives at least
\[
\frac{\max(p_r,t_r)m}{2}
=
\frac{p_rm}{2} \tag{4.7}
\]
such values. Therefore the sum of the cardinalities of the chosen same-latitude and cross-latitude spectra is at least
\[
p_rm-1
\ge \frac{(p_r+t_r)m}{2}-1
=\frac{q_rm}{2}-1. \tag{4.8}
\]

Each of these aggregate spectra is a union of elementary phase-shifted spectra \(\Sigma_m(A,B,\rho)\). By Lemma 3.2, elementary spectra with the same parameter pair \((A,B)\) are equal or disjoint.

Every elementary cosine spectrum has at least \(m/2\) values. For a same-latitude spectrum, deleting the zero squared distance can reduce one elementary component by at most one. It follows from (4.5) or (4.8) that, for the radius group \(r\), one can select at most \(q_r\) distinct elementary spectra whose cardinalities sum to at least
\[
\frac{q_rm}{2}-1. \tag{4.9}
\]
Indeed:

- if there are at most \(q_r\) available elementary components, select all of them;
- if there are more than \(q_r\), select any \(q_r\), each of size at least \(m/2\), except possibly one of size at least \(m/2-1\).

Doing this for every \(r\) produces at most
\[
\sum_r q_r=q
\]
elementary spectra, with total cardinality at least
\[
\sum_r\left(\frac{q_rm}{2}-1\right)
\ge \frac{qm}{2}-q. \tag{4.10}
\]

Two selected spectra with the same affine parameter pair are disjoint, because duplicate elementary spectra were selected only once. Two spectra with different parameter pairs intersect in at most \(C_0\) values by Lemma 2.1. Hence the union of all selected spectra has size at least
\[
\frac{qm}{2}-q-C_0\binom q2. \tag{4.11}
\]
Every selected value is an actual squared distance in \(X\), and passing from squared distances to distances preserves distinctness. Thus (4.11) proves the theorem.

The poles were not used. If \(p\) poles are present, \(n=qm+p\), giving the stated formulation in terms of \(n\).

Finally, if \(q=o(m)\), then
\[
\frac{q+C_0q^2}{qm}=O\!\left(\frac1m+\frac qm\right)=o(1),
\]
so
\[
D(X)\ge\left(\frac12-o(1)\right)|X|.
\]
∎

This directly rules out a counterexample of the form proposed in Route 6 with a fixed number \(q\) of cyclic latitude orbits.

---

### 5. Consequence for vertex-transitive spherical configurations

#### Corollary 5.1

Let \(X_j\subset S^2\) be spherical configurations whose Euclidean symmetry groups act transitively on \(X_j\), with \(|X_j|\to\infty\). Then
\[
D(X_j)\ge \frac{|X_j|}{2}-O(1).
\]

#### Proof

After fixing the center, a finite symmetry group is a subgroup of \(O(3)\). Its orientation-preserving subgroup has index at most two. The finite subgroups of \(SO(3)\) are:

- cyclic groups;
- dihedral rotation groups;
- the tetrahedral, octahedral, and icosahedral rotation groups.

The last three have bounded orders \(12,24,60\), so they cannot support transitive orbits of unbounded cardinality.

For a cyclic group \(C_m\), a nonpolar orbit is one free \(C_m\)-orbit.

For a dihedral rotation group \(D_m\), restriction to its cyclic subgroup \(C_m\) splits each orbit into at most two \(C_m\)-orbits.

Passing from a group in \(O(3)\) to its index-at-most-two orientation-preserving subgroup creates at most two orbits. Thus an unbounded transitive family decomposes under a common cyclic subgroup into at most four free cyclic orbits, plus poles. Apply Theorem 4.1 with \(q\le4\). ∎

This formalizes the heuristic that unbounded exact rotational symmetry in dimension three is essentially cyclic or dihedral and cannot produce a gap below \(n/2\).

---

### 6. Why extraction of exact spherical layers cannot be a general reduction

#### Proposition 6.1

For every sufficiently large \(n\), there exists a full-dimensional convex \(n\)-vertex configuration \(Y\subset\mathbb R^3\) such that no five points of \(Y\) lie on a common sphere. Consequently, for every center \(c\in\mathbb R^3\), each radial layer
\[
\{y\in Y:\|y-c\|=r\}
\]
has at most four points.

#### Proof

Begin with \(n\) distinct points
\[
x_1,\dots,x_n\in S^2
\]
whose affine hull is three-dimensional. Every \(x_i\) is strictly exposed by the functional \(u_i=x_i\), because
\[
x_i\cdot x_i=1>x_i\cdot x_j
\qquad(j\ne i).
\]
Since there are finitely many strict inequalities, sufficiently small independent perturbations
\[
y_i\approx x_i
\]
preserve them:
\[
x_i\cdot y_i>x_i\cdot y_j
\qquad(j\ne i).
\]
Thus the set of configurations in which every \(y_i\) is a vertex is an open neighborhood of the original configuration. Full affine dimension is also an open condition.

For every five-element index set \(I=\{i_1,\dots,i_5\}\), consider
\[
F_I(Y)=
\det
\begin{pmatrix}
\|y_{i_1}\|^2&y_{i_1,1}&y_{i_1,2}&y_{i_1,3}&1\\
\vdots&\vdots&\vdots&\vdots&\vdots\\
\|y_{i_5}\|^2&y_{i_5,1}&y_{i_5,2}&y_{i_5,3}&1
\end{pmatrix}.
\]
This is a polynomial in the coordinates. It is not identically zero: fix four affinely independent points, which determine a unique sphere, and choose the fifth point outside that sphere.

Therefore each zero set \(F_I=0\) has empty interior. There are only finitely many five-element sets \(I\), so their union cannot fill the open neighborhood in which all points remain vertices and the configuration remains three-dimensional. Choose a perturbation in that neighborhood for which every \(F_I\ne0\).

If five selected points lay on a sphere with center \(c\) and radius \(R\), they would all satisfy
\[
\|y\|^2-2c\cdot y+\|c\|^2-R^2=0.
\]
The corresponding nonzero coefficient vector would make the above five rows linearly dependent, forcing \(F_I=0\), a contradiction.

Thus no sphere contains five points. In particular, every exact radial layer about every center contains at most four points. ∎

This does not rule out a stability theorem specifically for configurations with few distances. It does rule out any unconditional pigeonhole reduction asserting that an arbitrary convex polytope has a spherical layer containing \(n-o(n)\) vertices.

---

### 7. Why standard transformations do not repair the reduction

For radial normalization about a center \(c\), write
\[
x_i-c=r_i u_i,\qquad u_i\in S^2.
\]
Then
\[
u_i\cdot u_j
=
\frac{r_i^2+r_j^2-\|x_i-x_j\|^2}{2r_ir_j}.
\]
Even if the original squared distances use only \(s\) values, varying endpoint radii can turn one original distance value into many different spherical inner products. Proposition 6.1 shows that the number of distinct radii cannot be bounded for arbitrary convex configurations.

Stereographic lifting has the same defect. The map
\[
\Phi(x)=
\frac{(2x,\|x\|^2-1)}{1+\|x\|^2}\in S^3
\]
satisfies
\[
\|\Phi(x)-\Phi(y)\|^2
=
\frac{4\|x-y\|^2}
{(1+\|x\|^2)(1+\|y\|^2)}.
\]
The endpoint-dependent denominator can split one original distance into quadratically many lifted distances. It also lands in \(S^3\), not \(S^2\).

Thus no known projection, radial normalization, or stereographic construction transfers the original distance-equality pattern to a spherical set with only \(o(n)\) additional values.

## Self-Audit

1. **The cyclic-orbit theorem uses a deep external torsion-point theorem.**  
   I did not reprove the Beukers–Smyth uniform torsion-curve theorem. The application is nevertheless rigorous if that established theorem is accepted: the relevant curve has degree three, and the proof explicitly excludes every possible positive-dimensional torsion coset. This is the single external input on which the \(O(1)\) overlap bound depends.

2. **The bookkeeping selecting at most \(q\) elementary spectra is delicate.**  
   The possible concern is double-counting phase grids or losing too much when zero distance is removed. Lemma 3.2 ensures same-parameter grids are equal or disjoint; duplicate grids are selected only once. Every component has at least \(m/2\) values, and at most one same-latitude component loses the zero value. This justifies the total \(\frac{qm}{2}-q\) before cross-parameter overlap losses.

3. **The generic no-five-cospherical proposition only blocks unconditional layer extraction.**  
   It does not exclude a future theorem saying that configurations with unusually few distances must have a large spherical subset. I believe the proposition itself is correct because exposedness is preserved under sufficiently small perturbations, while the finitely many five-point cosphericity determinants are proper polynomial equations. Its relevance must not be overstated.

## Computations To Verify

The following Sage/Python computations use exact cyclotomic arithmetic.

### 1. Exact multiplicity of nonzero translates of a cosine grid

This tests the special case underlying Lemma 2.1:
\[
\left|\{x\in C_m:x-t\in C_m\}\right|,
\qquad
C_m=\{\cos(2\pi k/m)\}.
\]

```python
from sage.all import *
from collections import defaultdict

def max_nonzero_difference_multiplicity(m):
    K = CyclotomicField(m)
    zeta = K.gen()

    C = list(set((zeta**k + zeta**(-k))/2 for k in range(m)))

    mult = defaultdict(int)
    for x in C:
        for y in C:
            if x != y:
                mult[x - y] += 1

    if not mult:
        return 0, None
    t = max(mult, key=mult.get)
    return mult[t], t

for m in range(3, 101):
    r, t = max_nonzero_difference_multiplicity(m)
    print(m, len(set([
        (CyclotomicField(m).gen()**k +
         CyclotomicField(m).gen()**(-k))/2
        for k in range(m)
    ])), r)
```

A failure of uniform boundedness here would contradict the stated torsion-curve consequence in this special translated-grid case.

### 2. Exact distance count for cyclic multi-orbit spherical sets

Use rational points \((r,z)\) on the unit circle and rational angular phases.

```python
from sage.all import *

def exact_cyclic_orbit_distance_count(m, orbit_data, add_north=False,
                                      add_south=False):
    """
    orbit_data is a list of triples (r, z, phase), all in QQ,
    satisfying r^2 + z^2 = 1.
    phase is measured in full turns.
    """
    denoms = [4, m]
    for r, z, phase in orbit_data:
        denoms.append(QQ(phase).denominator())
    L = lcm(denoms)

    K = CyclotomicField(L)
    w = K.gen()
    ii = w**(L // 4)

    points = []
    for r0, z0, phase0 in orbit_data:
        r0, z0, phase0 = QQ(r0), QQ(z0), QQ(phase0)
        assert r0 > 0
        assert r0**2 + z0**2 == 1

        for k in range(m):
            turn = phase0 + QQ(k)/m
            e = ZZ(turn * L)
            c = (w**e + w**(-e))/2
            s = (w**e - w**(-e))/(2*ii)
            points.append((K(r0)*c, K(r0)*s, K(z0)))

    if add_north:
        points.append((K(0), K(0), K(1)))
    if add_south:
        points.append((K(0), K(0), K(-1)))

    assert len(set(points)) == len(points)

    squared = set()
    for i in range(len(points)):
        for j in range(i):
            d2 = sum((points[i][t] - points[j][t])**2 for t in range(3))
            assert d2 != 0
            squared.add(d2)

    return len(points), len(squared)

for m in [7, 8, 9, 10, 12, 15]:
    data = [
        (QQ(3)/5,  QQ(4)/5, QQ(0)),
        (QQ(3)/5, -QQ(4)/5, QQ(1)/(2*m)),
        (QQ(4)/5,  QQ(3)/5, QQ(1)/(3*m)),
    ]
    n, D = exact_cyclic_orbit_distance_count(
        m, data, add_north=True
    )
    print("m =", m, "n =", n, "D =", D, "n/2 =", QQ(n)/2)
```

One should systematically enumerate rational Pythagorean latitude parameters and rational phases, checking whether any case violates
\[
D\ge \frac{qm}{2}-q-C\binom q2
\]
for a moderate empirical constant \(C\).

### 3. Direct exact overlap tests for distinct affine spectra

```python
from sage.all import *

def affine_cosine_spectrum(m, A, B, phase):
    phase = QQ(phase)
    L = lcm([4, m, phase.denominator()])
    K = CyclotomicField(L)
    w = K.gen()
    step = L // m
    e0 = ZZ(phase * L)

    return set(
        K(A) - K(B) * (w**(e0 + step*k) + w**(-e0 - step*k))/2
        for k in range(m)
    )

for m in range(5, 50):
    parameter_choices = [
        (QQ(1), QQ(1), QQ(0)),
        (QQ(2), QQ(1), QQ(0)),
        (QQ(1), QQ(2), QQ(1)/(2*m)),
        (QQ(3)/2, QQ(3)/4, QQ(1)/(3*m)),
    ]

    spectra = [
        affine_cosine_spectrum(m, A, B, phase)
        for A, B, phase in parameter_choices
    ]

    max_intersection = 0
    for i in range(len(spectra)):
        for j in range(i):
            if parameter_choices[i][:2] != parameter_choices[j][:2]:
                max_intersection = max(
                    max_intersection,
                    len(spectra[i].intersection(spectra[j]))
                )
    print(m, max_intersection)
```

### 4. Search for a convex rational configuration with no five cospherical

```python
# Pseudocode using exact QQ arithmetic.

# 1. Generate n rational points on S^2 by stereographic parametrization:
#       x(u,v) = (2u, 2v, 1-u^2-v^2)/(1+u^2+v^2).
#
# 2. Record the exact positive exposure margins
#       margin_i = min_{j != i} x_i . (x_i - x_j).
#
# 3. Add random rational perturbations e_i of norm much smaller than
#    min_i margin_i.
#
# 4. Check exact exposure:
#       x_i . (y_i - y_j) > 0 for all i != j.
#
# 5. For every 5-subset I, check exactly that
#       det([||y||^2, y_1, y_2, y_3, 1] for y in I) != 0.
#
# 6. Check one affine 4x4 determinant is nonzero to certify dimension 3.
#
# Repeat random perturbations until all tests pass.
```

## Route Diagnosis

**What worked**

- The spherical problem can be analyzed effectively when exact cyclic symmetry reduces distances to affine cosine grids.
- Bounded-degree torsion geometry gives a strong rigidity statement: two genuinely different affine cosine spectra have only \(O(1)\) common values.
- This proves
  \[
  D(X)\ge \frac{qm}{2}-O(q^2)
  \]
  for \(q\) cyclic orbits of order \(m\), settling the proposed fixed-\(q\) multi-orbit search in the affirmative direction.
- Finite rotation-group classification then handles all unbounded vertex-transitive spherical families.

**Precise block**

1. For arbitrary \(X\subset S^2\), the needed statement
   \[
   |X|\le 2D(X)+o(D(X))
   \]
   remains unproved. Harmonic interpolation gives only \(|X|\le(D+1)^2\). There is no orbit decomposition or bounded-degree torsion curve available without symmetry.

2. Even a complete proof of the spherical statement would not settle the original problem. Generic convex configurations have no spherical layer of more than four points, and radial or stereographic normalization does not preserve distance equalities.

Thus Route 4 reduces first to a substantial open spherical few-distance stability theorem and then to a second, independent reduction problem. This is a block of comparable strength, not a routine missing step.

**Plausible but unproved**

- Any spherical set with \(D(X)<(1/2-o(1))|X|\) may have to be asymptotically supported on a bounded number of cyclic or dihedral orbits.
- A convex polytope with near-minimal distance count may have much stronger cosphericity or projective rigidity than a generic convex configuration.
- The \(O(q^2)\) error in Theorem 4.1 may be reducible further by exploiting simultaneous rather than pairwise overlap constraints.

**Dead ends**

- Bare spherical-harmonic interpolation: quadratic dimension, no route to \(2s\).
- Unconditional extraction of a large exact spherical layer: disproved by Proposition 6.1.
- Radial projection and stereographic lifting: endpoint-dependent scaling destroys the distance-equality pattern.
- Finite symmetry classification alone: powerful for transitive or bounded-orbit families, but arbitrary few-distance sets need not have any nontrivial symmetry.

A fresh attempt should seek a genuine stability theorem for bounded-degree cosine/torsion phenomena without assuming a group action—for example, proving that many repeated spherical inner products force a large cyclic subsystem—or abandon spherical reduction and pursue a direct convex-geometric charging principle.