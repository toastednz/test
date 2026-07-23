STATUS: BLOCKED

## Result

I did not obtain the required classification. Route 4 yields a sharp negative diagnosis: the apparent excess of equal-distance equations does not itself create exceptional algebraic rigidity. For any hypothetical configuration, the complete-graph rigidity matrix automatically has at least
\[
\frac{(n-5)(n-2)}2
\]
color-balanced equilibrium stresses, exactly accounting for the nominal overdetermination. Thus a solution may be infinitesimally isolated modulo similarities without any forbidden collinearity or concyclicity. I give a precise rank criterion, an exact reformulation in terms of rank-two centered Euclidean distance matrices, a Schur-complement reduction useful for finite computation, and a secondary lower bound on the number of disjoint equal-length segment pairs. The remaining obstruction—excluding all positive rank-two colored Euclidean distance matrices with class sizes \(1,\dots,n-1\)—is of comparable strength to the original problem.

## Complete Argument

### 1. The colored rigidity matrix

Let \(P=(p_1,\dots,p_n)\) affinely span \(\mathbb R^2\), and let
\[
E=\binom n2.
\]
Suppose the edges of \(K_n\) are partitioned into \(k\) nonempty distance classes. Write
\[
c:\binom{[n]}2\to[k]
\]
for the coloring, and let \(\lambda_a>0\) be the common squared distance of color \(a\).

Let \(C\) be the \(E\times k\) color-incidence matrix
\[
C_{e,a}=
\begin{cases}
1,&c(e)=a,\\
0,&c(e)\ne a.
\end{cases}
\]
Its columns have disjoint nonempty supports, so
\[
\operatorname{rank}C=k.
\]

Let \(R(P)\) be the squared-distance rigidity matrix. For \(e=\{i,j\}\), its row has
\[
2(p_i-p_j)
\]
in the two columns belonging to \(p_i\),
\[
2(p_j-p_i)
\]
in the columns belonging to \(p_j\), and zero elsewhere. If
\[
\ell=(\|p_i-p_j\|^2)_{\{i,j\}}\in\mathbb R^E,
\]
then
\[
\ell=C\lambda.
\]

#### Lemma 1: Complete-graph rigidity

If \(P\) contains a noncollinear triple, then
\[
\operatorname{rank}R(P)=2n-3.
\]

**Proof.**
Suppose \(v_1,\dots,v_n\in\mathbb R^2\) satisfy
\[
(p_i-p_j)\cdot(v_i-v_j)=0
\]
for every \(i,j\). Choose noncollinear \(p_1,p_2,p_3\).

Subtract a suitable infinitesimal translation and rotation so that \(v_1=v_2=0\). The constraints on \(13\) and \(23\) then give
\[
(p_3-p_1)\cdot v_3=(p_3-p_2)\cdot v_3=0.
\]
The two displayed direction vectors are linearly independent, so \(v_3=0\).

For every \(i\ge4\), the constraints on \(i1,i2,i3\) give
\[
(p_i-p_a)\cdot v_i=0,\qquad a=1,2,3.
\]
Subtracting the equations for \(a=1\) from those for \(a=2,3\) yields
\[
(p_2-p_1)\cdot v_i=(p_3-p_1)\cdot v_i=0.
\]
Again the two vectors are independent, so \(v_i=0\). Thus the kernel consists exactly of the three-dimensional space of infinitesimal translations and rotations. ∎

### 2. Universal color-balanced stresses

An equilibrium stress is a vector
\[
\omega\in\ker R(P)^T.
\]
Equivalently, at each vertex \(i\),
\[
\sum_{j\ne i}\omega_{ij}(p_i-p_j)=0.
\]

A stress is color-balanced if additionally
\[
C^T\omega=0,
\]
meaning
\[
\sum_{e:c(e)=a}\omega_e=0
\]
for every color \(a\).

The crucial point is that a large space of such stresses is automatic.

#### Lemma 2: The stress image has one universal relation

For every equilibrium stress \(\omega\),
\[
\lambda^TC^T\omega=0.
\]

**Proof.**
Let \(p\in\mathbb R^{2n}\) denote the stacked coordinate vector. By direct calculation,
\[
R(P)p=2\ell=2C\lambda.
\]
Therefore, if \(R(P)^T\omega=0\),
\[
0=\frac12\omega^TR(P)p
  =\omega^TC\lambda
  =\lambda^TC^T\omega.
\]
∎

Consequently, the image of the map
\[
C^T:\ker R(P)^T\longrightarrow\mathbb R^k
\]
is contained in the \((k-1)\)-dimensional hyperplane \(\lambda^\perp\).

By Lemma 1,
\[
\dim\ker R(P)^T=E-(2n-3).
\]
It follows that
\[
\dim\bigl(\ker R(P)^T\cap\ker C^T\bigr)
\ge E-(2n-3)-(k-1),
\]
or
\[
\boxed{
\dim\bigl(\ker R(P)^T\cap\ker C^T\bigr)
\ge E-2n-k+4.}
\]

For the problem at hand, \(k=n-1\), and hence
\[
\boxed{
\dim\bigl(\ker R(P)^T\cap\ker C^T\bigr)
\ge \frac{(n-5)(n-2)}2.}
\]

This is exactly the number suggested by the naive equation surplus.

### 3. Exact tangent-rank criterion

For every color class, choose one reference edge and impose equality of every other edge in that class with the reference edge. This gives
\[
m=E-k
\]
equal-distance equations.

Let
\[
L:\mathbb R^E\to\mathbb R^{E-k}
\]
be the corresponding difference map. Its kernel is precisely
\[
\ker L=\operatorname{im}C,
\]
because \(Lx=0\) says that \(x\) is constant on every color class.

The Jacobian of the equal-distance equations is therefore
\[
J_{\rm eq}=LR(P).
\]

Define
\[
t=\dim\bigl(\operatorname{im}R(P)\cap\operatorname{im}C\bigr).
\]

Since
\[
C\lambda=\ell=\frac12R(P)p,
\]
the nonzero vector \(C\lambda\) belongs to both spaces, so
\[
t\ge1.
\]

Now
\[
\ker J_{\rm eq}
=\{v:R(P)v\in\operatorname{im}C\}.
\]
The kernel of \(R(P)\) has dimension \(3\), and the preimage of the \(t\)-dimensional intersection contributes \(t\) additional dimensions. Thus
\[
\dim\ker J_{\rm eq}=3+t,
\]
and hence
\[
\boxed{\operatorname{rank}J_{\rm eq}=2n-3-t.}
\]

In particular,
\[
\operatorname{rank}J_{\rm eq}\le2n-4.
\]

Moreover:

- \(t=1\) exactly when the only color-compatible infinitesimal motions are Euclidean motions and dilation;
- \(t>1\) exactly when there is a nonsimilarity infinitesimal motion in which all edges of each color have the same first-order squared-length variation.

For \(k=n-1\), the number of equation dependencies is therefore at least
\[
m-(2n-4)
=\frac{(n-1)(n-2)}2-(2n-4)
=\boxed{\frac{(n-5)(n-2)}2}.
\]

If \(t=1\), equality holds. Thus the entire nominal overdetermination can be accounted for by universal complete-graph stresses and dilation. No forbidden geometric degeneracy is needed.

Equivalently, introduce the squared-distance variables themselves and use the augmented Jacobian
\[
J_{\rm aug}=[R(P)\;-\!C].
\]
Its left kernel is exactly the space of color-balanced equilibrium stresses, and
\[
\operatorname{rank}J_{\rm aug}
=(2n-3)+k-t.
\]

This invalidates the basic hoped-for mechanism of Route 4: merely proving that many equality equations are dependent cannot imply nonexistence, because the required dependencies exist at every hypothetical solution.

### 4. Exact Euclidean distance matrix reformulation

For a coloring \(c\), let \(A_a\) be the symmetric \(0\)-\(1\) adjacency matrix of color \(a\), with zero diagonal. Define
\[
D(\lambda)=\sum_{a=1}^k\lambda_a A_a.
\]
Thus \(D_{ij}\) is the proposed squared distance between \(p_i\) and \(p_j\).

#### Lemma 3: Rank four and nonconcyclic quadruples

If \(P\subset\mathbb R^2\) contains a noncollinear triple, then its squared-distance matrix \(D\) has rank at most \(4\). If \(P\) is not contained in one circle, then
\[
\operatorname{rank}D=4.
\]

Moreover, for any four points with no three collinear,
\[
\det D_S=0
\]
if and only if those four points are concyclic.

**Proof.**
Write \(p_i=(x_i,y_i)\) and \(u_i=x_i^2+y_i^2\). Let \(M\) be the \(n\times4\) matrix whose \(i\)-th row is
\[
(1,x_i,y_i,u_i).
\]
Then
\[
D=MKM^T,
\]
where
\[
K=
\begin{pmatrix}
0&0&0&1\\
0&-2&0&0\\
0&0&-2&0\\
1&0&0&0
\end{pmatrix}.
\]
The matrix \(K\) is invertible, so \(\operatorname{rank}D\le4\).

Because the points affinely span the plane, the first three columns of \(M\) are independent. Thus \(\operatorname{rank}M<4\) precisely when
\[
x_i^2+y_i^2=a+bx_i+cy_i
\]
for all \(i\), which says that all points lie on a common circle. Therefore a nonconcyclic configuration has rank \(4\).

Apply the same factorization to a four-point subset \(S\). Since \(M_S\) and \(K\) are square,
\[
\det D_S=\det(M_S)^2\det K.
\]
Under the no-three-collinear assumption, the first three columns of \(M_S\) have rank \(3\). Hence \(\det M_S=0\) exactly when the fourth column is an affine combination of the first three, which is exactly the common-circle equation above. ∎

Thus every desired configuration with \(n\ge4\) satisfies
\[
\operatorname{rank}D=4
\]
and
\[
\det D_S\ne0
\]
for every four-element subset \(S\).

#### Lemma 4: Exact centered-Gram criterion

Let
\[
H=I-\frac1n\mathbf1\mathbf1^T
\]
and
\[
G=-\frac12HDH.
\]
A symmetric hollow matrix \(D\) is the squared-distance matrix of points in \(\mathbb R^2\) if and only if
\[
G\succeq0,\qquad \operatorname{rank}G\le2.
\]

**Proof.**
For a point configuration translated to have centroid zero, its Gram matrix is \(G=XX^T\), and direct expansion gives \(G=-HDH/2\).

Conversely, suppose \(G\succeq0\) and \(\operatorname{rank}G\le2\). Factor
\[
G=XX^T
\]
with \(X\) having at most two columns, and let \(D'\) be the squared-distance matrix of its rows. Then
\[
HD'H=-2G=HDH.
\]
Thus \(K=D-D'\) satisfies \(HKH=0\). Every symmetric matrix with this property has the form
\[
K=\mathbf1a^T+a\mathbf1^T.
\]
Both \(D\) and \(D'\) are hollow, so \(K_{ii}=2a_i=0\) for every \(i\). Hence \(a=0\), and \(D=D'\). ∎

It follows that a fixed coloring with the required class sizes is realizable exactly when there are pairwise distinct positive numbers \(\lambda_1,\dots,\lambda_{n-1}\) such that:

1. \(G(\lambda)=-HD(\lambda)H/2\) is positive semidefinite of rank \(2\);
2. for every triple with squared side lengths \(a,b,c\),
   \[
   2ab+2ac+2bc-a^2-b^2-c^2>0;
   \]
3. for every four-set \(S\),
   \[
   \det D(\lambda)_S\ne0.
   \]

This removes the coordinate variables entirely. It is an exact semialgebraic reformulation, not merely a necessary condition.

### 5. Schur-complement reduction

Choose any four vertices \(S\). In a desired configuration,
\[
A=D_S
\]
is invertible. After reordering vertices, write
\[
D=
\begin{pmatrix}
A&B\\
B^T&C
\end{pmatrix}.
\]
Since \(\operatorname{rank}D=\operatorname{rank}A=4\), the Schur complement vanishes:
\[
C=B^TA^{-1}B.
\]

For each outside vertex \(v\), let \(b_v\) be the vector of its four squared distances to the anchor vertices. Then
\[
\boxed{b_v^TA^{-1}b_v=0}
\]
and, for outside vertices \(u\ne v\),
\[
\boxed{D_{uv}=b_u^TA^{-1}b_v.}
\]

Clearing denominators gives polynomial equations
\[
b_v^T\operatorname{adj}(A)b_v=0
\]
and
\[
\det(A)D_{uv}
-b_u^T\operatorname{adj}(A)b_v=0.
\]

For \(n=9\), this produces \(5\) diagonal equations and \(10\) off-diagonal equations in the eight squared-distance variables, before normalization by scale. These equations are dependent, as the stress calculation predicts. They nevertheless provide a practical fixed-coloring prefilter.

Rank four is not by itself sufficient: a rank-four hollow matrix can represent, for example, a spherical configuration in three dimensions. The centered-Gram PSD and rank-two conditions must still be imposed.

### 6. Exact \(n=4\) benchmark showing nontrivial tangent behavior

For \(a>0\), put
\[
A=(-1,0),\quad B=(1,0),\quad C=(0,a),\quad
O=\left(0,\frac{a^2-1}{2a}\right).
\]
Then \(O\) is the circumcenter of \(ABC\), and
\[
AB^2=4,
\]
\[
AC^2=BC^2=1+a^2,
\]
\[
AO^2=BO^2=CO^2=\frac{(a^2+1)^2}{4a^2}.
\]

The three values are distinct unless
\[
a^2\in
\left\{
3,\ \frac13,\ 7-4\sqrt3,\ 7+4\sqrt3
\right\}.
\]
No three selected points are collinear unless \(a=1\). The four points are not concyclic because \(A,B,C\) lie on a circle centered at \(O\), while \(O\) does not lie on that nondegenerate circle.

At \(a=2\), this is the configuration in the brief. The three equality equations may be taken as
\[
AC^2-BC^2,\qquad AO^2-BO^2,\qquad AO^2-CO^2.
\]
Their Jacobian rows are independent. Indeed, in the two coordinate columns of \(C\), the first and third rows respectively have entries
\[
(4,0),\qquad (0,-5/2),
\]
while the second row is zero there. A linear relation therefore first forces the coefficients of the first and third rows to vanish, and then the coefficient of the nonzero second row vanishes.

Thus
\[
\operatorname{rank}J_{\rm eq}=3.
\]
Since \(\operatorname{rank}R=5\),
\[
t=5-3=2.
\]
So this general-position example has a genuine nonsimilarity color-compatible infinitesimal deformation. It does not refute a possible large-\(n\) theorem, but it demonstrates that rank deficiency need not arise from collinearity or concyclicity.

### 7. A secondary consequence of the multiplicity moment

Let \(A(P)\) be the number of unordered pairs of equal-length edges sharing a vertex, and let \(B(P)\) be the number of unordered pairs of equal-length disjoint edges. The prescribed spectrum gives
\[
A(P)+B(P)
=\sum_r\binom{\mu_P(r)}2
=\binom n3.
\]

At a fixed vertex \(v\), let \(d_{v,r}\) be its degree in the distance graph of \(r\). No four concyclic implies
\[
d_{v,r}\le3,
\]
and
\[
\sum_r d_{v,r}=n-1.
\]
Therefore
\[
\sum_r\binom{d_{v,r}}2
\le
\alpha_n,
\]
where
\[
\alpha_n=
\begin{cases}
n-1,&3\mid n-1,\\
n-2,&3\nmid n-1.
\end{cases}
\]
This follows by packing the integers \(d_{v,r}\le3\) into as many groups of size \(3\) as possible.

Summing over vertices,
\[
A(P)\le n\alpha_n,
\]
and hence
\[
\boxed{
B(P)\ge \binom n3-n\alpha_n.}
\]
For example, any hypothetical \(n=9\) configuration has at least
\[
\binom93-9\cdot7=21
\]
pairs of equal-length disjoint segments.

This is rigorous but far too weak to force a forbidden configuration.

## Self-Audit

1. **The stress calculation is only first-order.**  
   It does not imply that a maximal-rank solution exists or that an infinitesimally isolated solution is algebraically realizable. I believe every stated rank identity is correct because it follows directly from \(\operatorname{rank}R=2n-3\), \(R(P)p=2C\lambda\), and elementary subspace-dimension formulas. I make no global-existence inference from it.

2. **The principal-distance determinant criterion uses the no-three-collinear hypothesis.**  
   Without that hypothesis, \(\det D_S=0\) can arise from affine degeneracy rather than concyclicity. The problem supplies no three collinear, and the factorization \(D_S=M_SKM_S^T\) proves the criterion under exactly that assumption.

3. **The rank-four/Gram reformulation does not produce a uniform obstruction.**  
   It replaces coordinates by \(n-1\) distance variables but leaves positivity, rank-two, and exponentially many colorings. I believe the reformulation is genuinely equivalent because the centered-Gram converse was proved above; nevertheless, solving these semialgebraic systems uniformly remains essentially the original problem.

## Computations To Verify

### 1. Exact check of the \(n=4\) example and all rank formulas

```python
import itertools
import sympy as sp

def exact_matrices(P, color):
    n = len(P)
    edges = list(itertools.combinations(range(n), 2))
    edge_index = {e: q for q, e in enumerate(edges)}
    E = len(edges)
    k = max(color.values()) + 1

    R = sp.zeros(E, 2*n)
    C = sp.zeros(E, k)
    ell = sp.zeros(E, 1)
    D = sp.zeros(n, n)

    for q, (i, j) in enumerate(edges):
        xi, yi = P[i]
        xj, yj = P[j]
        dx, dy = xi-xj, yi-yj
        d2 = sp.expand(dx**2 + dy**2)

        ell[q] = d2
        D[i, j] = D[j, i] = d2

        R[q, 2*i]     = 2*dx
        R[q, 2*i + 1] = 2*dy
        R[q, 2*j]     = -2*dx
        R[q, 2*j + 1] = -2*dy

        C[q, color[(i, j)]] = 1

    eq_rows = []
    for a in range(k):
        ids = [q for q, e in enumerate(edges) if color[e] == a]
        ref = ids[0]
        for q in ids[1:]:
            eq_rows.append(R.row(q) - R.row(ref))

    Jeq = (sp.Matrix.vstack(*eq_rows)
           if eq_rows else sp.zeros(0, 2*n))
    Jaug = R.row_join(-C)

    t_intersection = R.rank() + C.rank() - R.row_join(C).rank()

    return edges, ell, D, R, C, Jeq, Jaug, t_intersection

P = [
    (sp.Rational(-1), sp.Rational(0)),   # A
    (sp.Rational(1),  sp.Rational(0)),   # B
    (sp.Rational(0),  sp.Rational(2)),   # C
    (sp.Rational(0),  sp.Rational(3,4))  # O
]

color = {
    (0,1): 0,                 # multiplicity 1
    (0,2): 1, (1,2): 1,      # multiplicity 2
    (0,3): 2, (1,3): 2, (2,3): 2  # multiplicity 3
}

edges, ell, D, R, C, Jeq, Jaug, t = exact_matrices(P, color)

print("squared distances:", list(ell))
print("rank R:", R.rank())
print("rank equality Jacobian:", Jeq.rank())
print("rank augmented Jacobian:", Jaug.rank())
print("intersection dimension t:", t)
print("rank D:", D.rank())

# General-position determinants.
for T in itertools.combinations(range(4), 3):
    M = sp.Matrix([[P[i][0], P[i][1], 1] for i in T])
    assert M.det() != 0

for S in itertools.combinations(range(4), 4):
    M = sp.Matrix([
        [P[i][0]**2 + P[i][1]**2, P[i][0], P[i][1], 1]
        for i in S
    ])
    assert M.det() != 0
    assert D.extract(S, S).det() != 0

assert list(ell) == [
    4, 5, sp.Rational(25,16),
    5, sp.Rational(25,16), sp.Rational(25,16)
]
assert R.rank() == 5
assert Jeq.rank() == 3
assert Jaug.rank() == 6
assert t == 2
assert D.rank() == 4
```

Expected rank output:
```text
rank R: 5
rank equality Jacobian: 3
rank augmented Jacobian: 6
intersection dimension t: 2
rank D: 4
```

### 2. Rank and stress audit for any exact candidate

Given exact coordinates and a proposed coloring, run:

```python
E = len(edges)
k = C.cols
n = len(P)

stress_dim = E - R.rank()
color_balanced_stress_dim = E - Jaug.rank()

assert R.rank() == 2*n - 3
assert t >= 1
assert Jeq.rank() == 2*n - 3 - t
assert Jaug.rank() == (2*n - 3) + k - t
assert color_balanced_stress_dim >= E - 2*n - k + 4

if k == n-1:
    assert color_balanced_stress_dim >= (n-5)*(n-2)//2
```

This should be applied to exact versions of the Pomerance and Palásti configurations once their coordinates are extracted.

### 3. Fixed-coloring algebraic infeasibility test

For a fixed coloring of \(K_n\), construct
\[
D(s)=\sum_a s_aA_a,\qquad
G_{\rm num}=(nI-\mathbf1\mathbf1^T)D(s)(nI-\mathbf1\mathbf1^T).
\]
The scalar factor and sign are irrelevant for rank. Impose all \(3\times3\) minors of \(G_{\rm num}\) to force centered Gram rank at most \(2\).

Sage-style pseudocode:

```python
from itertools import combinations
from sage.all import *

def colored_edm_ideal(n, cmap):
    k = n - 1
    names = [f"s{i}" for i in range(k)] + ["z"]
    R = PolynomialRing(QQ, names=names, order="degrevlex")
    gens = R.gens()
    s = gens[:k]
    z = gens[-1]

    D = matrix(R, n, n, 0)
    for i, j in combinations(range(n), 2):
        a = cmap[(i, j)]
        D[i,j] = D[j,i] = s[a]

    Hnum = n*identity_matrix(R, n) - matrix(R, n, [1]*(n*n))
    Gnum = Hnum * D * Hnum

    eqs = []

    # Centered Gram rank <= 2.
    triples = list(combinations(range(n), 3))
    for rows in triples:
        for cols in triples:
            eqs.append(Gnum.matrix_from_rows_and_columns(rows, cols).det())

    Q = R.one()

    # Positive/nonzero distances and pairwise distinct distance values.
    for a in range(k):
        Q *= s[a]
    for a, b in combinations(range(k), 2):
        Q *= s[a] - s[b]

    # No collinear triples: saturate by Heron/Cayley-Menger factors.
    for i, j, l in combinations(range(n), 3):
        a = D[i,j]
        b = D[i,l]
        c = D[j,l]
        phi = 2*a*b + 2*a*c + 2*b*c - a*a - b*b - c*c
        Q *= phi

    # No concyclic quadruples.
    for S in combinations(range(n), 4):
        Q *= D.matrix_from_rows_and_columns(S, S).det()

    # Normalize scale and saturate all required nonvanishing factors.
    eqs.append(s[0] - 1)
    eqs.append(z*Q - 1)

    return R.ideal(eqs)

I = colored_edm_ideal(9, cmap)
GB = I.groebner_basis()
print(any(g == 1 for g in GB))
```

If the Gröbner basis contains \(1\), that coloring has no complex nondegenerate rank-two centered distance matrix and therefore no desired real realization. If it does not contain \(1\), one must still solve the real system and certify PSD and the strict signs.

### 4. Abstract \(n=9\) coloring enumeration

A CP-SAT model can enumerate necessary combinatorial patterns:

```python
from ortools.sat.python import cp_model
from itertools import combinations

n = 9
colors = range(1, n)  # color c must occur c times
edges = list(combinations(range(n), 2))
edge_id = {e:q for q,e in enumerate(edges)}

def eid(i, j):
    return edge_id[tuple(sorted((i,j)))]

model = cp_model.CpModel()
x = {
    (e,c): model.NewBoolVar(f"x_{e}_{c}")
    for e in range(len(edges)) for c in colors
}

# Exactly one color per edge.
for e in range(len(edges)):
    model.Add(sum(x[e,c] for c in colors) == 1)

# Prescribed multiplicities.
for c in colors:
    model.Add(sum(x[e,c] for e in range(len(edges))) == c)

# Degree at most 3 in each color.
for v in range(n):
    for c in colors:
        model.Add(sum(x[eid(v,w),c] for w in range(n) if w != v) <= 3)

# No monochromatic K_{2,3}.
for a, b in combinations(range(n), 2):
    outside = [v for v in range(n) if v not in (a,b)]
    for T in combinations(outside, 3):
        for c in colors:
            model.Add(sum(
                x[eid(a,v),c] + x[eid(b,v),c] for v in T
            ) <= 5)
```

Every surviving coloring should then be passed to the exact Euclidean-distance-matrix test above.

## Route Diagnosis

**Proved ledger.**

- The complete-graph squared-distance rigidity matrix has rank \(2n-3\) in the presence of a noncollinear triple.
- Every hypothetical \(k\)-distance realization has at least
  \[
  E-2n-k+4
  \]
  color-balanced equilibrium stresses.
- For \(k=n-1\), this is exactly
  \[
  (n-5)(n-2)/2,
  \]
  the nominal equation surplus.
- The equality-Jacobian rank is exactly
  \[
  2n-3-t,\qquad
  t=\dim(\operatorname{im}R\cap\operatorname{im}C)\ge1.
  \]
- Fixed-color realizability is equivalent to a positive, pairwise-distinct, rank-two centered Euclidean distance matrix satisfying explicit nondegeneracy inequalities.
- Every desired squared-distance matrix has rank \(4\), every principal \(4\times4\) minor is nonzero, and it obeys the stated Schur-complement equations.
- A hypothetical \(n=9\) configuration has at least \(21\) pairs of disjoint equal-length segments.

**Plausible but unproved claims.**

- The \(n=9\) fixed-coloring systems may be computationally finite and tractable after stronger symmetry reduction.
- Known \(n=5,6,7,8\) examples may be maximal-rank, meaning \(t=1\); exact coordinates are needed to test this.
- Minimal-support color-balanced stresses might force a small forbidden metric pattern, but no such theorem was established.

**Dead ends.**

- Raw equation counting fails: the expected dependencies are universal.
- Treating all stress dependencies as evidence of collinearity or concyclicity is false in principle; the \(n=4\) general-position family already has \(t>1\).
- Rank four of the uncentered distance matrix is insufficient because it also admits nonplanar spherical Euclidean distance matrices.
- The disjoint equal-segment lower bound is much too small to force a geometric contradiction.

**Precise block.**

After removing the misleading dimension count, Route 4 requires proving that no coloring with class sizes \(1,\dots,n-1\) admits pairwise distinct positive \(\lambda_a\) for which
\[
-\frac12H\left(\sum_a\lambda_aA_a\right)H
\]
is PSD of rank \(2\) and all general-position determinants are nonzero. No rank argument obtained here excludes such matrices for any \(n\ge9\), let alone uniformly. This is essentially the original realizability problem in a cleaner algebraic form, so the route is blocked rather than solved.

A fresh attempt should first extract exact \(n=5,6,7,8\) coordinates and compute \(t\), stress supports, and Schur systems. For the finite frontier, the best next step is SAT enumeration for \(n=9\) followed by the centered-Gram Gröbner/interval test. For an asymptotic argument, one needs genuinely new information about the signs or supports of color-balanced stresses, or a geometric obstruction to the many required disjoint equal-length segment pairs; further rank counting alone cannot succeed.