STATUS: BLOCKED

## Result

Route 3 yields a sharper general polynomial-inertia bound
\[
n\le \binom{s+3}{3}
\]
for an \(s\)-distance set in \(\mathbb R^3\), together with exact matrix formulations of convex position and complete-framework stresses. However, these remain polynomial rather than linear in \(s\). The decisive obstruction is that ordinary Euclidean-distance-matrix rank, inertia, interpolation, and stress dimensions also hold for three-dimensional grids, which have \(s=o(n)\); convexity enters only through a sign condition on the affine-dependence space. On a sphere, the natural low-rank exposing matrix is simply \(Q/2\), so extremality supplies no additional algebraic identity. Thus the route reduces to an unproved “balanced-kernel few-entry EDM theorem” essentially equivalent in strength to the original problem.

## Complete Argument

### 1. Basic Euclidean distance matrix structure

Let \(x_1,\dots,x_n\in\mathbb R^3\), let \(X\) be the \(n\times3\) matrix whose \(i\)-th row is \(x_i^{\mathsf T}\), and set
\[
d_i=\|x_i\|^2,\qquad
Q_{ij}=\|x_i-x_j\|^2.
\]
Then
\[
Q=d\mathbf1^{\mathsf T}+\mathbf1d^{\mathsf T}-2XX^{\mathsf T},
\]
so
\[
\operatorname{rank}Q\le 5.
\]

Moreover, if \(z^{\mathsf T}\mathbf1=0\), then
\[
z^{\mathsf T}Qz=-2\|X^{\mathsf T}z\|^2\le0.
\]
Thus \(Q\) has at most one positive eigenvalue. Since all off-diagonal entries are positive,
\[
\mathbf1^{\mathsf T}Q\mathbf1>0,
\]
so \(Q\) has exactly one positive eigenvalue.

These facts use no convexity.

---

### 2. A sharpened polynomial-inertia bound

The elementary interpolation argument in the brief gives a cubic bound with a comparatively large constant. The special signature of radial polynomial kernels improves it as follows.

#### Theorem 2.1

If a finite set \(X\subset\mathbb R^3\) has \(n\) points and determines exactly \(s\) positive distances, then
\[
\boxed{n\le \binom{s+3}{3}}.
\]

Consequently,
\[
s\ge (6n)^{1/3}-O(1).
\]

#### Proof

Let the distinct positive squared distances be
\[
a_1,\dots,a_s,
\]
and define the monic polynomial
\[
F(t)=\prod_{r=1}^s(t-a_r).
\]
Consider the symmetric polynomial kernel
\[
K(x,y)=F(\|x-y\|^2).
\]
On the given point set,
\[
K(x_i,x_j)=
\begin{cases}
F(0),&i=j,\\
0,&i\ne j.
\end{cases}
\]
Hence
\[
[K(x_i,x_j)]_{i,j=1}^n=F(0)I_n,
\qquad
\operatorname{sgn}F(0)=(-1)^s.
\]

We now calculate the inertia of the ambient bilinear form represented by \(K\).

Let \(\mathcal H_\ell\) denote the space of homogeneous harmonic polynomials of degree \(\ell\) in three variables. It has dimension
\[
\dim\mathcal H_\ell=2\ell+1.
\]
Repeated Fischer decomposition gives the polynomial space
\[
\mathcal W_s=
\bigoplus_{\ell=0}^s
\bigoplus_{j=0}^{s-\ell}
\|x\|^{2j}\mathcal H_\ell.
\]
Every polynomial \(x\mapsto K(x,y)\) belongs to \(\mathcal W_s\).

Because \(K\) is invariant under simultaneous rotations of \(x\) and \(y\), its coefficient bilinear form is block diagonal with respect to harmonic degree \(\ell\). For each fixed harmonic basis vector of degree \(\ell\), the corresponding radial block is indexed by
\[
j=0,\dots,s-\ell.
\]
Set
\[
m_\ell=s-\ell+1.
\]

A coefficient coupling
\[
\|x\|^{2j}H_\ell(x)
\quad\text{and}\quad
\|y\|^{2k}H_\ell(y)
\]
can occur only if
\[
\ell+j+k\le s.
\]
Thus each radial block is anti-triangular: its entries vanish when
\[
j+k>s-\ell.
\]

On the anti-diagonal \(j+k=s-\ell\), only the leading term
\[
\|x-y\|^{2s}
=(\|x\|^2+\|y\|^2-2x\cdot y)^s
\]
contributes. The relevant term is a positive multiple of
\[
(-2)^\ell
\|x\|^{2j}\|y\|^{2k}(x\cdot y)^\ell.
\]
The projection of \((x\cdot y)^\ell\) onto the degree-\(\ell\) harmonic reproducing kernel has positive coefficient. Hence every nonzero anti-diagonal entry in the \(\ell\)-block has sign
\[
(-1)^\ell.
\]

A real symmetric anti-triangular \(m\times m\) matrix with nonzero anti-diagonal is nonsingular. Congruence elimination pairs the outermost coordinates into hyperbolic planes. Therefore:

- if \(m\) is even, its inertia is \((m/2,m/2)\);
- if \(m\) is odd, the one unpaired sign is the sign of its central anti-diagonal entry.

For \(m_\ell=s-\ell+1\), oddness means \(s-\ell\) is even, hence
\[
(-1)^\ell=(-1)^s.
\]
Therefore the index having sign \((-1)^s\) equals
\[
\sum_{\ell=0}^s
(2\ell+1)
\left\lceil\frac{s-\ell+1}{2}\right\rceil.
\]

To evaluate this sum, use
\[
\sum_{\ell\ge0}(2\ell+1)z^\ell
=\frac{1+z}{(1-z)^2}
\]
and
\[
\sum_{k\ge0}
\left\lceil\frac{k+1}{2}\right\rceil z^k
=\frac{1+z}{(1-z^2)^2}
=\frac1{(1-z)^2(1+z)}.
\]
Their product is
\[
\frac1{(1-z)^4}.
\]
Thus the coefficient of \(z^s\) is
\[
\binom{s+3}{3}.
\]

Write
\[
K(x,y)=\phi(x)^{\mathsf T}C\phi(y)
\]
in a basis of \(\mathcal W_s\). Since
\[
\Phi C\Phi^{\mathsf T}=F(0)I_n,
\]
the image of \(\Phi^{\mathsf T}\) is an \(n\)-dimensional subspace on which the form \(C\) is definite with sign \((-1)^s\). Its dimension cannot exceed the corresponding inertia index of \(C\), namely \(\binom{s+3}{3}\). Therefore
\[
n\le\binom{s+3}{3}.
\]
∎

For reference, the opposite inertia index is
\[
\binom{s+2}{3},
\]
and hence
\[
\dim\mathcal W_s
=
\binom{s+3}{3}+\binom{s+2}{3}.
\]

This is a genuine improvement over using all polynomials of degree at most \(2s\), but its order remains cubic.

---

### 3. The spherical specialization remains only quadratic

Suppose \(\|x_i\|=R\) for all \(i\). Distances correspond bijectively to inner products
\[
x_i\cdot x_j=\alpha_r.
\]
For each \(i\), let
\[
p_i(x)=\prod_{r=1}^s(x_i\cdot x-\alpha_r).
\]
Then
\[
p_i(x_j)=0\quad(i\ne j),
\]
while
\[
p_i(x_i)=\prod_{r=1}^s(R^2-\alpha_r)>0.
\]
The restrictions to \(S^2\) of polynomials of degree at most \(s\) have dimension
\[
\sum_{\ell=0}^s(2\ell+1)=(s+1)^2.
\]
Therefore
\[
n\le(s+1)^2.
\]

This recovers the standard spherical absolute bound. Polynomial interpolation alone therefore gives only
\[
s\ge\sqrt n-1
\]
in the spherical subclass, even though every spherical point is automatically extreme.

---

### 4. Exact algebraic encoding of convexity

Let
\[
J=I-\frac1n\mathbf1\mathbf1^{\mathsf T},
\qquad
B=-\frac12JQJ.
\]
After translating the centroid to the origin,
\[
B=XX^{\mathsf T}\succeq0,
\qquad
\operatorname{rank}B=3.
\]

An affine dependence is a vector \(w\in\mathbb R^n\) satisfying
\[
\mathbf1^{\mathsf T}w=0,
\qquad
X^{\mathsf T}w=0.
\]
Since \(B=XX^{\mathsf T}\),
\[
X^{\mathsf T}w=0
\iff Bw=0.
\]
Thus the affine-dependence space is
\[
\mathcal K
=
\ker B\cap\mathbf1^\perp.
\]

#### Lemma 4.1: sign characterization of convex position

The points \(x_1,\dots,x_n\) are all vertices of their convex hull if and only if every nonzero \(w\in\mathcal K\) has at least two positive and at least two negative coordinates.

#### Proof

Every nonzero vector in \(\mathcal K\) has both signs because its coordinates sum to zero.

Suppose \(w\in\mathcal K\) has exactly one positive coordinate, say \(w_i>0\). Then
\[
w_ix_i=-\sum_{j\ne i}w_jx_j.
\]
All \(w_j\le0\), and
\[
\sum_{j\ne i}\frac{-w_j}{w_i}=1.
\]
Hence
\[
x_i=\sum_{j\ne i}\frac{-w_j}{w_i}x_j,
\]
so \(x_i\) is not extreme. The same conclusion follows from exactly one negative coordinate after replacing \(w\) by \(-w\).

Conversely, if \(x_i\) is not extreme, write
\[
x_i=\sum_{j\ne i}\lambda_jx_j,
\qquad
\lambda_j\ge0,\quad \sum_{j\ne i}\lambda_j=1.
\]
Then the vector
\[
w_i=1,\qquad w_j=-\lambda_j
\]
lies in \(\mathcal K\) and has exactly one positive coordinate. ∎

Accordingly, the original problem can be expressed purely in distance-matrix language as follows:

> Let \(Q\) be an EDM with \(s\) distinct positive off-diagonal entries, let \(B=-JQJ/2\) be positive semidefinite of rank \(3\), and suppose every nonzero vector in \(\ker B\cap\mathbf1^\perp\) has at least two positive and two negative coordinates. Must
> \[
> n\le 2s+o(s)?
> \]

This is exact, but it is not a simplification: the sign-balanced-kernel condition contains the full oriented-matroid content of convex position.

---

### 5. Low-rank exposing matrices

For each vertex \(x_i\), choose a vector \(u_i\) strictly exposing it:
\[
u_i\cdot x_i>u_i\cdot x_j\qquad(j\ne i).
\]
Define
\[
H_{ij}=u_i\cdot(x_i-x_j).
\]
Then
\[
H_{ii}=0,\qquad H_{ij}>0\quad(i\ne j).
\]
If \(U\) has rows \(u_i^{\mathsf T}\) and \(c_i=u_i\cdot x_i\), then
\[
H=c\mathbf1^{\mathsf T}-UX^{\mathsf T},
\]
so
\[
\operatorname{rank}H\le4.
\]

This looks like useful extra low-rank information, but it degenerates completely in the spherical case. If all points lie on a sphere centered at the origin, take \(u_i=x_i\). Then
\[
H_{ij}=R^2-x_i\cdot x_j
=\frac12\|x_i-x_j\|^2
=\frac12Q_{ij}.
\]
Thus, for the substantial spherical subclass, the exposing matrix gives no information beyond the EDM itself.

There is also no general lower-rank theorem based only on the sign pattern
\[
H_{ii}=0,\quad H_{ij}>0.
\]
For a regular \(n\)-gon on the unit circle,
\[
H_{ij}=1-\cos\frac{2\pi(i-j)}n
\]
has rank at most \(3\), despite \(n\) being arbitrary.

---

### 6. Why rank and stress information alone cannot suffice

Consider the grid
\[
G_t=\{0,1,\dots,t-1\}^3.
\]
It has
\[
n=t^3
\]
points. Every squared distance is a positive integer at most
\[
3(t-1)^2,
\]
so the number \(s_t\) of distinct distances satisfies
\[
s_t\le 3(t-1)^2=o(t^3)=o(n).
\]

Nevertheless, its EDM has rank at most \(5\) and exactly one positive eigenvalue, just like every three-dimensional EDM. It also has the standard complete-framework stress space described below. The only missing hypothesis is that most grid points are not extreme.

This proves that any argument using only:

- rank \(Q\le5\);
- conditional negative definiteness of \(Q\);
- a small alphabet of off-diagonal values;
- ordinary complete-graph stress dimensions;

cannot produce a linear lower bound. It must use the sign-balanced affine kernel, or an equivalent genuinely convex-geometric condition.

There is another deceptive reformulation which also loses convexity: the rows of every EDM are themselves in convex position in their row space. Indeed, row \(i\) uniquely minimizes the \(i\)-th coordinate because
\[
Q_{ii}=0<Q_{ji}\qquad(j\ne i).
\]
Thus “the rows of \(Q\) are exposed” is automatic for every set of distinct points and does not encode extremality of the original \(x_i\).

---

### 7. Complete-framework stresses do not see the distance count

Let \(E=\binom n2\), and let \(R\) be the rigidity matrix of the complete framework. Its action is
\[
(Rv)_{ij}=(x_i-x_j)\cdot(v_i-v_j).
\]

#### Lemma 7.1

If the points affinely span \(\mathbb R^3\), then
\[
\operatorname{rank}R=3n-6.
\]

#### Proof

Every infinitesimal Euclidean motion
\[
v_i=Ax_i+b,\qquad A^{\mathsf T}=-A,
\]
lies in \(\ker R\), giving a six-dimensional subspace.

Choose four affinely independent points. Any velocities on these four points extend uniquely to an affine velocity field
\[
v(x)=Lx+b.
\]
The six edge constraints on the tetrahedron imply that the symmetric part of \(L\) vanishes: applying the constraints to a basis of three edge vectors gives the diagonal entries of the symmetric part, and applying them to pairwise differences gives the mixed entries. Hence \(L\) is skew-symmetric.

Subtract this infinitesimal Euclidean motion. The four anchor velocities are now zero. For any remaining point \(x_i\), the constraints to the four anchors imply
\[
(x_i-x_j)\cdot v_i=0
\]
for all four anchors \(x_j\). Differences of these four vectors span \(\mathbb R^3\), so \(v_i=0\). Thus the kernel consists exactly of the six infinitesimal Euclidean motions, proving the claimed rank. ∎

Therefore the equilibrium stress space has dimension
\[
\binom n2-(3n-6)
=\frac{(n-3)(n-4)}2.
\]
This dimension is the same for every full-dimensional complete framework, convex or not, and is independent of the number of distance classes.

If \(\mathcal C\subset\mathbb R^E\) denotes the \(s\)-dimensional space of edge-vectors constant on each distance class, then distance-class-preserving infinitesimal motions solve
\[
Rv\in\mathcal C.
\]
The scaling motion \(v_i=x_i\) always gives such a vector because
\[
(Rv)_{ij}=\|x_i-x_j\|^2.
\]
Beyond this unavoidable similarity direction, raw dimension counting gives no useful lower bound on \(s\), since
\[
\dim(\operatorname{im}R)+\dim\mathcal C-\binom n2
\]
is negative for the relevant range. Thus ordinary rigidity and stress counts do not approach the required constant.

---

### 8. Distance-class adjacency matrices

Let \(A_r\) be the adjacency matrix of the graph formed by pairs at squared distance \(a_r\). Then
\[
Q=\sum_{r=1}^s a_rA_r.
\]

For a fixed \(r\), put
\[
F_r(t)=\prod_{k\ne r}(t-a_k).
\]
Entrywise evaluation gives
\[
[F_r(Q_{ij})]
=
F_r(0)I+F_r(a_r)A_r.
\]
Since this is a radial polynomial kernel of degree \(s-1\),
\[
\operatorname{rank}\bigl(F_r(0)I+F_r(a_r)A_r\bigr)
\le
\binom{s+2}{3}+\binom{s+1}{3}.
\]
Equivalently,
\[
n-\operatorname{mult}_{A_r}
\left(-\frac{F_r(0)}{F_r(a_r)}\right)
\le
\binom{s+2}{3}+\binom{s+1}{3}.
\]

This identifies a possible spectral route: one would need strong simultaneous restrictions on the exceptional eigenvalue multiplicities of the distance graphs \(A_r\). No such restriction follows from ordinary graph theory. For example, a matching has eigenvalues \(1\) and \(-1\), each with linear multiplicity, and matching distance classes occur in regular even polygons and related polytopes. Moreover, the \(A_r\) need not commute or generate a low-dimensional association algebra.

Thus the adjacency-matrix approach is not dead in principle, but it requires a new theorem coupling all the \(A_r\) simultaneously to the rank-three positive semidefinite Gram matrix and the balanced affine kernel.

---

### 9. Ledger

#### Proved lemmas

1. Every three-dimensional EDM has rank at most \(5\) and exactly one positive eigenvalue.
2. Every \(s\)-distance set in \(\mathbb R^3\) satisfies
   \[
   n\le\binom{s+3}{3}.
   \]
3. Every spherical \(s\)-distance set on \(S^2\) satisfies
   \[
   n\le(s+1)^2.
   \]
4. Convex position is equivalent to every nonzero affine dependence having at least two positive and two negative coefficients.
5. Convex position provides a hollow, strictly positive off-diagonal matrix of rank at most \(4\).
6. For spherical configurations, the natural exposing matrix is exactly \(Q/2\).
7. The complete rigidity matrix has rank \(3n-6\), and the stress space has dimension \((n-3)(n-4)/2\).
8. Three-dimensional grids show that EDM rank, inertia, entry count, and ordinary stress dimensions alone cannot yield a linear bound.
9. Omitting one interpolation root gives the exact adjacency-eigenvalue identity in Section 8.

#### Plausible but unproved claims

1. A genuinely new theorem may exist coupling the balanced affine kernel to the spectra of the distance-class matrices.
2. Large spherical configurations with unusually few distances may be forced toward cyclic or dihedral structure.
3. If the distance-class adjacency matrices generate a low-dimensional semisimple algebra, a classification might imply \(n\le2s+O(1)\), apart from finitely many Platonic-type exceptions.

#### Dead ends

1. **EDM rank alone:** defeated by \(t\times t\times t\) grids with \(s=O(t^2)=o(t^3)\).
2. **Ordinary polynomial interpolation:** gives only cubic, or quadratic on the sphere.
3. **Sign-rank from exposing matrices:** regular polygons have arbitrarily large order but rank-three hollow positive matrices.
4. **Ordinary stress dimension counting:** the stress dimension is determined by \(n\), not by the distance partition.
5. **Convexity of the rows of \(Q\):** automatic for every EDM and therefore vacuous.
6. **Treating distance graphs separately:** individual distance graphs can have linear eigenvalue multiplicities; simultaneous structure is essential.

## Self-Audit

1. **The harmonic-kernel inertia calculation is the most technical point.** Its weak spot is the use of the standard harmonic decomposition and rotational block diagonalization. The anti-triangular structure, anti-diagonal signs, and generating-function count are given explicitly, and they agree with the checks \(s=1\), giving inertia \((1,4)\), and \(s=2\), giving \((10,4)\).

2. **The convexity criterion is only a reformulation, not progress toward the target constant.** It is nevertheless exact: a singleton sign in an affine dependence is precisely a convex-combination certificate for a nonvertex, and every nonvertex gives such a dependence.

3. **The conclusion that Route 3 is blocked is not an impossibility theorem.** A sufficiently subtle theorem could still combine rank, distance classes, and oriented affine dependencies. The diagnosis is justified because all currently extracted identities collapse either on grids or on the spherical subclass, leaving a balanced-kernel theorem essentially as strong as the original problem.

## Computations To Verify

The following exact or certified checks test the main lemmas and likely failure modes.

### 1. Exact EDM statistics and interpolation identity

```python
import itertools
import sympy as sp

def squared_distance_matrix(points):
    n = len(points)
    return sp.Matrix(n, n, lambda i, j:
        sum((points[i][k] - points[j][k])**2
            for k in range(len(points[i]))))

def edm_stats(points):
    Q = squared_distance_matrix(points)
    n = len(points)
    values = sorted({
        sp.factor(Q[i, j])
        for i in range(n) for j in range(i)
        if Q[i, j] != 0
    })

    J = sp.eye(n) - sp.ones(n, n) / sp.Rational(n)
    B = -sp.Rational(1, 2) * J * Q * J

    F0 = sp.prod(-a for a in values)
    K = Q.applyfunc(lambda z: sp.prod(z - a for a in values))

    assert K == F0 * sp.eye(n)

    return {
        "n": n,
        "s": len(values),
        "rank_Q": Q.rank(),
        "rank_B": B.rank(),
        "distance_values": values
    }

def grid(t):
    return [
        tuple(map(sp.Integer, p))
        for p in itertools.product(range(t), repeat=3)
    ]

for t in range(2, 5):
    data = edm_stats(grid(t))
    print(t, data["n"], data["s"],
          data["rank_Q"], data["rank_B"])
```

Expected:

- \(\operatorname{rank}Q\le5\);
- \(\operatorname{rank}B=3\);
- \(s\le3(t-1)^2\);
- \(F[Q]=F(0)I\) exactly.

### 2. Numerical verification of the kernel signature

```python
import itertools
import numpy as np
import sympy as sp
from math import comb

def exponent_tuples(d, max_degree):
    out = []
    for e in itertools.product(range(max_degree + 1), repeat=d):
        if sum(e) <= max_degree:
            out.append(e)
    return out

def radial_kernel_coefficient_matrix(d, s):
    xs = sp.symbols("x0:" + str(d))
    ys = sp.symbols("y0:" + str(d))
    r2 = sum((xs[i] - ys[i])**2 for i in range(d))

    roots = list(range(1, s + 1))
    expr = sp.expand(sp.prod(r2 - a for a in roots))

    mons = exponent_tuples(d, 2 * s)
    index = {e: i for i, e in enumerate(mons)}
    C = sp.zeros(len(mons))

    poly = sp.Poly(expr, *(xs + ys))
    for exponents, coeff in poly.terms():
        ex = exponents[:d]
        ey = exponents[d:]
        C[index[ex], index[ey]] += coeff

    assert C == C.T
    return C

for s in range(1, 4):
    C = radial_kernel_coefficient_matrix(3, s)
    A = np.array(C.tolist(), dtype=float)
    ev = np.linalg.eigvalsh(A)
    tol = 1e-8 * max(1.0, np.max(np.abs(ev)))

    pos = np.sum(ev > tol)
    neg = np.sum(ev < -tol)
    zero = len(ev) - pos - neg

    expected_selected = comb(s + 3, 3)
    expected_other = comb(s + 2, 3)

    print("s =", s, "inertia =", pos, neg, zero)
    if s % 2 == 0:
        assert pos == expected_selected
        assert neg == expected_other
    else:
        assert neg == expected_selected
        assert pos == expected_other
```

### 3. Rigidity-matrix rank

```python
def rigidity_matrix(points):
    n = len(points)
    rows = []

    for i in range(n):
        for j in range(i + 1, n):
            row = [sp.Integer(0)] * (3 * n)
            diff = [
                points[i][k] - points[j][k]
                for k in range(3)
            ]
            for k in range(3):
                row[3*i + k] = diff[k]
                row[3*j + k] = -diff[k]
            rows.append(row)

    return sp.Matrix(rows)

pts = grid(2)  # Cube vertices
R = rigidity_matrix(pts)
assert R.rank() == 3 * len(pts) - 6
print("stress dimension =", R.rows - R.rank())
```

### 4. Numerical vertex test

```python
import numpy as np
from scipy.optimize import linprog

def all_points_are_vertices(points, tol=1e-9):
    P = np.asarray(points, dtype=float)
    n, d = P.shape

    for i in range(n):
        others = [j for j in range(n) if j != i]
        Aeq = np.vstack([
            np.ones(len(others)),
            P[others].T
        ])
        beq = np.concatenate(([1.0], P[i]))

        result = linprog(
            c=np.zeros(len(others)),
            A_eq=Aeq,
            b_eq=beq,
            bounds=[(0, None)] * len(others),
            method="highs"
        )

        if result.success and np.linalg.norm(Aeq @ result.x - beq) < tol:
            return False, i

    return True, None

print(all_points_are_vertices(np.array(grid(2), dtype=float)))
print(all_points_are_vertices(np.array(grid(3), dtype=float)))
```

The cube should pass; the \(3^3\) grid should fail.

### 5. Distance-class adjacency spectra

```python
def distance_class_matrices(points):
    Q = squared_distance_matrix(points)
    n = len(points)
    vals = sorted({
        Q[i, j]
        for i in range(n) for j in range(i)
        if Q[i, j] != 0
    })

    matrices = []
    for a in vals:
        A = sp.Matrix(n, n, lambda i, j:
            1 if i != j and Q[i, j] == a else 0)
        matrices.append((a, A))

    return Q, vals, matrices

def verify_omitted_root_identity(points):
    Q, vals, matrices = distance_class_matrices(points)
    n = len(points)

    for r, (a, A) in enumerate(matrices):
        other = [vals[k] for k in range(len(vals)) if k != r]
        Fr0 = sp.prod(-b for b in other)
        Fra = sp.prod(a - b for b in other)
        M = Q.applyfunc(
            lambda z: sp.prod(z - b for b in other)
        )
        assert M == Fr0 * sp.eye(n) + Fra * A

verify_omitted_root_identity(grid(2))
```

### 6. Exact cyclic two-orbit spectrum search in SageMath

```python
def two_latitude_spectrum(m, h2, shifted=False):
    # h2 and 1-h2 should be rational.
    K.<zeta> = CyclotomicField(2*m)
    r2 = K(1 - h2)
    h2 = K(h2)

    shift = [0, 1 if shifted else 0]
    heights = [1, -1]  # Actual squared height difference uses h2.

    values = set()

    for a in range(2):
        for b in range(a, 2):
            for k in range(m):
                for l in range(m):
                    if a == b and k == l:
                        continue

                    exponent = (2*k + shift[a]) - (2*l + shift[b])
                    cosine = (zeta**exponent + zeta**(-exponent)) / 2
                    vertical = 0 if a == b else 4*h2
                    q = 2*r2*(1 - cosine) + vertical
                    values.add(q)

    return len(values), values

for m in range(5, 31):
    for h2 in [QQ(1)/10, QQ(1)/4, QQ(1)/2]:
        s, _ = two_latitude_spectrum(m, h2, shifted=False)
        print(m, h2, s, "ratio", RR(s)/(2*m))
```

This tests whether two spherical cyclic orbits can drive the ratio persistently below \(1/2\), using exact cyclotomic arithmetic.

## Route Diagnosis

The successful part of Route 3 is the exact radial-kernel identity
\[
F[Q]=F(0)I
\]
and its inertia analysis. It improves the standard ambient polynomial dimension but still yields only \(s=\Omega(n^{1/3})\). Rigidity contributes a large stress space, but its dimension is universal and does not interact with the number of distance classes. Convexity can be encoded exactly by the balanced-sign condition on
\[
\ker B\cap\mathbf1^\perp,
\]
yet no rank or interpolation argument found here converts that oriented condition into a linear bound.

The sharp block is the spherical subclass. There, all points are exposed automatically and the natural exposing matrix is \(Q/2\), while standard harmonic interpolation gives only \(n\le(s+1)^2\). Therefore any successful continuation must establish a new structural theorem for rank-three Gram matrices with few off-diagonal values, not merely refine generic polynomial dimension counts.

A fresh Route 3 attempt should focus on the simultaneous distance-class matrices
\[
Q=\sum_{r=1}^s a_rA_r,\qquad
B=-\frac12JQJ\succeq0,\quad \operatorname{rank}B=3,
\]
and seek a theorem coupling their common algebra to the balanced affine kernel. A plausible concrete target is a stability result: unless the generated algebra is asymptotically cyclic or dihedral, the number of classes must exceed \(n/2-o(n)\). In parallel, exact cyclic multi-orbit searches are warranted because a spherical counterexample would bypass the general convexity difficulty entirely.