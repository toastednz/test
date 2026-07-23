STATUS: BLOCKED

## Result

Route 1 does not presently yield the required \(D(P)\ge n/2-o(n)\) bound. I proved three rigorous obstructions to its most natural implementations: a single great-circle support sweep may see only \(O(\sqrt n)\) of \(n\) vertices; a cyclically ordered set of vertices that projects to a convex polygon need not satisfy Altman’s distance conclusion; and normal-fan transitions can select linearly many equal-length edges. I also proved the conjecture for the facet-dominant class and, after the support route blocked, excluded a substantial family of potential cyclic multi-orbit counterexamples: aligned rational latitude orbits of prime order \(p\) on \(S^2\) always determine at least \((n-q)/2\) distances, where \(q\) is the number of orbits and \(n=qp\).

## Complete Argument

### 1. A positive support-geometric special case

**Lemma 1.** Let \(P\) be a three-dimensional convex polytope with \(n\) vertices. If one face of \(P\) contains \(f\) vertices, then
\[
D(P)\ge \left\lfloor\frac f2\right\rfloor.
\]
Consequently, if \(f=n-r\), then
\[
D(P)\ge \frac n2-\frac r2-\frac12.
\]

**Proof.** The \(f\) vertices of the face form a convex \(f\)-gon in the affine plane containing that face. By Altman’s planar theorem, they determine at least \(\lfloor f/2\rfloor\) distinct Euclidean distances. These are also distances between vertices of \(P\). The final inequality follows from
\[
\left\lfloor\frac f2\right\rfloor\ge \frac f2-\frac12.
\]
\(\square\)

Thus Route 1 proves the desired asymptotic bound whenever some face contains \(n-o(n)\) vertices. This includes the regular-pyramid extremizers, but not general simplicial polytopes.

---

### 2. A single rotating support-plane sweep can see only \(O(\sqrt n)\) vertices

For a finite \(X\subset S^2\), define the normal cell of \(x\in X\) by
\[
N_x=\{u\in S^2:u\cdot x\ge u\cdot y\text{ for every }y\in X\}.
\]
Since
\[
u\cdot x=\cos d_{S^2}(u,x),
\]
the cells \(N_x\) are exactly the closed spherical Voronoi cells of \(X\).

A support-plane sweep whose unit normals trace a great circle \(G\subset S^2\) can expose only vertices \(x\) for which \(N_x\cap G\neq\varnothing\).

**Proposition 2.** There is an infinite sequence of three-dimensional convex polytopes \(P_k\), with \(n_k\to\infty\), such that for every great circle \(G\subset S^2\), the corresponding support sweep encounters at most
\[
3\pi^2\sqrt{n_k}
\]
vertices.

**Proof.** Fix \(0<\delta<1\), and let \(X\subset S^2\) be a maximal \(\delta\)-separated set in spherical distance. Thus distinct points of \(X\) are at distance at least \(\delta\), and maximality implies that spherical caps of radius \(\delta\) centered at \(X\) cover \(S^2\).

Write \(n=|X|\) and
\[
a(\rho)=2\pi(1-\cos\rho)
\]
for the area of a spherical cap of radius \(\rho\). The radius-\(\delta/2\) open caps centered at points of \(X\) are pairwise disjoint, while the radius-\(\delta\) caps cover \(S^2\). Hence
\[
n\,a(\delta/2)\le 4\pi\le n\,a(\delta).
\]
In particular,
\[
\frac{2}{1-\cos\delta}\le n\le
\frac{2}{1-\cos(\delta/2)}.
\]
Therefore \(n=\Theta(\delta^{-2})\). Moreover, since \(1-\cos\delta\le \delta^2/2\),
\[
n\ge \frac4{\delta^2}.
\tag{1}
\]

Let \(G\) be any great circle, and let
\[
Y_G=\{x\in X:N_x\cap G\neq\varnothing\}.
\]
If \(x\in Y_G\), choose \(u\in N_x\cap G\). Because the radius-\(\delta\) caps cover the sphere, there is some \(y\in X\) with \(d(u,y)<\delta\). Since \(u\in N_x\), \(x\) is a nearest point of \(X\) to \(u\), so
\[
d(u,x)\le d(u,y)<\delta.
\]
Thus \(d(x,G)<\delta\).

Every radius-\(\delta/2\) cap centered at such an \(x\) lies in the spherical \(3\delta/2\)-neighborhood of \(G\). These caps are pairwise disjoint. The area of the spherical \(\rho\)-neighborhood of a great circle is
\[
4\pi\sin\rho
\qquad(0\le \rho\le\pi/2).
\]
Consequently,
\[
|Y_G|\,2\pi(1-\cos(\delta/2))
 \le 4\pi\sin(3\delta/2),
\]
and hence
\[
|Y_G|
 \le \frac{2\sin(3\delta/2)}{1-\cos(\delta/2)}.
\]
For \(0<\delta<1\),
\[
\sin(3\delta/2)\le\frac{3\delta}{2},
\]
while
\[
1-\cos(\delta/2)\ge \frac{\delta^2}{2\pi^2}.
\]
It follows that
\[
|Y_G|\le \frac{6\pi^2}{\delta}.
\]
By (1),
\[
\frac1\delta\le \frac{\sqrt n}{2},
\]
so
\[
|Y_G|\le 3\pi^2\sqrt n.
\]

It remains to verify that \(X\) is the vertex set of a three-dimensional convex polytope. Every \(x\in X\) is exposed by the functional \(y\mapsto x\cdot y\), because
\[
x\cdot x=1>x\cdot y
\]
for every distinct \(y\in X\). Thus every point of \(X\) is a vertex of \(\operatorname{conv}X\).

The hull is three-dimensional. Indeed, if \(X\) lay in an affine plane
\[
v\cdot x=c,
\]
then, according to the sign of \(c\), one of the poles \(v\) or \(-v\) would have spherical distance at least \(\pi/2\) from every point of \(X\). This contradicts the fact that the radius-\(\delta\) caps cover \(S^2\), since \(\delta<1<\pi/2\).

Taking \(\delta=1/k\) gives the required infinite sequence. \(\square\)

This rules out any proof that needs one fixed-axis rotation to produce \(n-o(n)\) cyclically ordered exposed vertices. It does not rule out a carefully coordinated collection of many sweeps.

---

### 3. Convexity of a projection does not transfer Altman’s distance mechanism

One might try to use the cyclic order of vertices appearing on the boundary of an orthogonal projection. The following exact example shows that planar convexity of the projection is insufficient.

**Proposition 3.** There are ten points in \(\mathbb R^3\) whose orthogonal projections form a regular decagon but which determine only three Euclidean distances.

**Proof.** Put
\[
r=\frac2{\sqrt5},\qquad z=\frac1{\sqrt5},
\]
and define
\[
U_j=\left(r\cos\frac{2\pi j}{5},
          r\sin\frac{2\pi j}{5},z\right),
\]
\[
L_j=\left(r\cos\frac{2\pi(j+1/2)}5,
          r\sin\frac{2\pi(j+1/2)}5,-z\right),
\qquad 0\le j<5.
\]
Together with \((0,0,\pm1)\), these are the vertices of a regular icosahedron.

The projections of the \(U_j,L_j\) onto the \(xy\)-plane all have radius \(r\), and their angular coordinates are precisely
\[
0,\frac{\pi}{5},\frac{2\pi}{5},\ldots,\frac{9\pi}{5}.
\]
They therefore form a regular decagon.

Direct substitution, using
\[
\cos\frac{\pi}{5}=\frac{1+\sqrt5}{4},
\qquad
\cos\frac{2\pi}{5}=\frac{\sqrt5-1}{4},
\]
shows that the inner product of any two distinct icosahedral vertices belongs to
\[
\left\{\frac1{\sqrt5},-\frac1{\sqrt5},-1\right\}.
\]
All three values occur among the ten ring vertices: adjacent vertices give \(1/\sqrt5\), suitable nonadjacent vertices give \(-1/\sqrt5\), and each ring vertex has its antipode in the other ring.

Since all points have norm one, their squared distances are therefore exactly
\[
2-\frac2{\sqrt5},\qquad
2+\frac2{\sqrt5},\qquad
4.
\]
Thus the ten spatial points determine three distances, even though their projections form a convex decagon. In particular,
\[
3<\left\lfloor\frac{10}{2}\right\rfloor.
\]
\(\square\)

This is a finite obstruction and therefore does not disprove a possible asymptotic theorem for projection-convex spatial cycles. It does, however, invalidate a direct transplantation of Altman’s planar statement or proof based only on projected cyclic order.

---

### 4. Normal-fan transitions can have unbounded distance multiplicity

For a generic great-circle sweep, consecutive exposed vertices correspond to adjacent normal cells and hence to edges of the polytope. Edge transitions alone cannot provide the required “at most twice per distance” collection.

**Proposition 4.** For every \(m\ge3\), there is a convex \(2m\)-vertex prism all \(3m\) of whose edges have the same length.

**Proof.** Let
\[
s=2\sin\frac{\pi}{m},
\]
and take the points
\[
v_j^\pm=
\left(\cos\frac{2\pi j}{m},
      \sin\frac{2\pi j}{m},
      \pm\frac s2\right),
\qquad 0\le j<m.
\]
Their convex hull is the Cartesian product of a regular \(m\)-gon and an interval, hence is a three-dimensional convex prism with exactly these \(2m\) vertices.

Each horizontal edge has length
\[
\left\|
v_{j+1}^\pm-v_j^\pm
\right\|
=2\sin\frac{\pi}{m}=s.
\]
Each vertical edge has length
\[
\|v_j^+-v_j^-\|=s.
\]
A prism has \(2m\) horizontal edges and \(m\) vertical edges, so all \(3m\) edges have the same length. \(\square\)

Thus any support-geometric rule which selects linearly many pairs solely from adjacent normal cells can select one numerical distance linearly many times. A successful Route 1 argument must use nonlocal chords or a multiscale hierarchy, not only normal-fan adjacency.

---

### 5. An alternative exact result for aligned cyclic spherical orbits

After the above obstructions, I examined the most natural potential disproof family from Route 6. The following result excludes aligned rational latitude orbits of increasing prime order.

#### 5.1 A cyclotomic disjointness lemma

Let \(p\ge5\) be an odd prime and put
\[
r_p=\frac{p-1}{2},
\qquad
C_p=\left\{\cos\frac{2\pi k}{p}:1\le k\le r_p\right\}.
\]

**Lemma 5.** Let \(A,B,A',B'\in\mathbb Q\) with \(B,B'>0\). If
\[
A-Bc=A'-B'c'
\]
for some \(c,c'\in C_p\), then
\[
A=A'\quad\text{and}\quad B=B'.
\]
Consequently, for distinct rational parameter pairs \((A,B)\), \(B>0\), the sets
\[
A-BC_p
\]
are pairwise disjoint.

**Proof.** Let
\[
K=\mathbb Q\left(\cos\frac{2\pi}{p}\right).
\]
The field \(K\) has degree \((p-1)/2\), and \(C_p\) is the full set of Galois conjugates of any of its elements \(\cos(2\pi k/p)\), \(k\not\equiv0\pmod p\).

Rearrange the assumed equality as
\[
c=\alpha+\beta c',
\qquad
\alpha=\frac{A-A'}B,\quad
\beta=\frac{B'}B>0.
\]
Applying every automorphism of \(K/\mathbb Q\) gives
\[
C_p=\alpha+\beta C_p
\]
as sets.

Write the elements of \(C_p\) in increasing order. Since \(x\mapsto\alpha+\beta x\) is strictly increasing and maps this finite ordered set onto itself, it maps its minimum to its minimum and its maximum to its maximum. Thus
\[
c_{\min}=\alpha+\beta c_{\min},
\qquad
c_{\max}=\alpha+\beta c_{\max}.
\]
Subtracting and using \(c_{\max}\ne c_{\min}\) gives \(\beta=1\), and then \(\alpha=0\). Hence \(B'=B\) and \(A'=A\). \(\square\)

#### 5.2 Application to latitude orbits

**Theorem 6.** Let \(p\ge5\) be an odd prime. Choose \(q\ge2\) distinct rational pairs
\[
(r_a,z_a)\in\mathbb Q^2,\qquad
r_a>0,\qquad r_a^2+z_a^2=1,
\quad 1\le a\le q.
\]
Define
\[
x_{a,k}=
\left(
r_a\cos\frac{2\pi k}{p},
r_a\sin\frac{2\pi k}{p},
z_a
\right),
\qquad 0\le k<p.
\]
Then these \(n=qp\) points are the vertices of a three-dimensional convex polytope and determine at least
\[
\frac{q(p-1)}2=\frac{n-q}{2}
\]
distinct distances.

**Proof.** All points lie on \(S^2\). They are distinct because the orbit parameters \((r_a,z_a)\) are distinct and each orbit has \(p\) distinct angular positions. Every point is exposed by its tangent plane to \(S^2\), so all are vertices.

Because \(q\ge2\), two orbit parameters have different heights: on the unit sphere, \(z\) determines the positive radius \(r=\sqrt{1-z^2}\). One orbit spans its horizontal plane, and a point of a different-height orbit lies outside that plane. Hence the affine hull is three-dimensional.

For two orbit types \(a,b\),
\[
\|x_{a,k}-x_{b,\ell}\|^2
=A_{ab}-B_{ab}
  \cos\frac{2\pi(k-\ell)}p,
\]
where
\[
A_{ab}=r_a^2+r_b^2+(z_a-z_b)^2\in\mathbb Q,
\qquad
B_{ab}=2r_ar_b\in\mathbb Q_{>0}.
\]
For every unordered pair \(a\le b\), all values in
\[
A_{ab}-B_{ab}C_p
\]
occur as positive squared distances: when \(a=b\), use nonzero angular differences; when \(a<b\), the same nonzero differences are available.

By Lemma 5, blocks associated with different parameter pairs \((A_{ab},B_{ab})\) are disjoint. It remains to show that at least \(q\) distinct parameter pairs occur.

Let \(g\) be the number of distinct radii among \(r_1,\ldots,r_q\). For each such radius \(r\), an internal orbit block has parameters
\[
(A,B)=(2r^2,2r^2).
\]
These give \(g\) distinct parameter pairs.

A fixed positive radius can occur for at most two distinct latitude orbits, corresponding to heights \(z\) and \(-z\). Let \(h\) be the number of radii occurring twice. If a radius occurs twice, then \(z\ne0\), because otherwise the two orbit parameters would be identical. The cross block between the two corresponding orbits has parameters
\[
(A,B)=(2r^2+4z^2,\,2r^2).
\]
Here \(A>B\), so this pair cannot equal an internal pair, all of which satisfy \(A=B\). Such cross pairs for distinct radii are distinct because their \(B\)-coordinates are distinct.

If \(s\) radii occur once and \(h\) occur twice, then
\[
g=s+h,\qquad q=s+2h,
\]
so
\[
g+h=q.
\]
We have therefore exhibited at least \(q\) distinct parameter pairs. Each contributes exactly \((p-1)/2\) mutually disjoint squared-distance values. Hence
\[
D(P)\ge q\frac{p-1}{2}
=\frac{n-q}{2}.
\]
\(\square\)

In particular, whenever \(p\to\infty\),
\[
D(P)\ge \left(\frac12-\frac1{2p}\right)n
=\frac n2-o(n).
\]
The alignment and rationality hypotheses are essential to the proof. The staggered latitude rings of the icosahedron show that angular phase offsets can create additional coincidences at small \(p\).

## Self-Audit

1. **The support-sweep obstruction covers great-circle sweeps, not arbitrary paths on the Gaussian sphere.** A deliberately chosen path could traverse every normal cell. I believe the stated proposition is correct because it quantifies only great circles and follows from an explicit cap-packing and tube-area argument; no conclusion about arbitrary support paths is claimed.

2. **The icosahedral example is only a finite obstruction.** It disproves a literal spatial version of Altman’s theorem for projection-convex cycles, but not a possible \(k/2-o(k)\) asymptotic version. The exact claim nevertheless holds because the coordinates give a regular projected decagon and the three inner-product values are verified algebraically.

3. **The cyclic-orbit theorem is highly restrictive.** It assumes prime orbit size, aligned angular grids, and rational latitude parameters. The Galois argument does not currently handle arbitrary phase offsets or coefficients lying inside the same cyclotomic field. Within the stated hypotheses, however, every coefficient is rational and the conjugacy argument proves exact disjointness of the spectral blocks.

## Computations To Verify

The following checks test the exact finite examples and numerically probe the support-sweep obstruction.

```python
# Exact icosahedral distance check
import sympy as sp

sqrt5 = sp.sqrt(5)
r = 2 / sqrt5
z = 1 / sqrt5
pi = sp.pi

north = (sp.Integer(0), sp.Integer(0), sp.Integer(1))
south = (sp.Integer(0), sp.Integer(0), sp.Integer(-1))

U, L = [], []
for j in range(5):
    a = 2*pi*j/5
    b = 2*pi*(sp.Rational(j) + sp.Rational(1, 2))/5
    U.append((r*sp.cos(a), r*sp.sin(a), z))
    L.append((r*sp.cos(b), r*sp.sin(b), -z))

pts = [north, south] + U + L
ring = U + L

def sqdist(x, y):
    raw = sum((x[i] - y[i])**2 for i in range(3))
    return sp.nsimplify(sp.trigsimp(sp.expand_trig(raw)), [sqrt5])

all_vals = {
    sqdist(pts[i], pts[j])
    for i in range(len(pts))
    for j in range(i+1, len(pts))
}
ring_vals = {
    sqdist(ring[i], ring[j])
    for i in range(len(ring))
    for j in range(i+1, len(ring))
}

expected = {
    2 - 2/sqrt5,
    2 + 2/sqrt5,
    sp.Integer(4)
}
assert all_vals == expected
assert ring_vals == expected
print(all_vals)
```

```python
# Equal-edge regular prisms
import numpy as np

for m in range(3, 30):
    s = 2*np.sin(np.pi/m)
    pts = []
    for sign in (-1, 1):
        for j in range(m):
            a = 2*np.pi*j/m
            pts.append(np.array([np.cos(a), np.sin(a), sign*s/2]))

    def idx(sign_index, j):
        return sign_index*m + (j % m)

    edges = []
    for sign_index in (0, 1):
        for j in range(m):
            edges.append((idx(sign_index, j), idx(sign_index, j+1)))
    for j in range(m):
        edges.append((idx(0, j), idx(1, j)))

    lengths = [np.linalg.norm(pts[i]-pts[j]) for i, j in edges]
    assert len(edges) == 3*m
    assert max(abs(x-s) for x in lengths) < 1e-10
```

An exact cyclotomic-field counter for Theorem 6:

```python
import sympy as sp

x = sp.symbols('x')

def latitude(t):
    # Rational parametrization of r^2 + z^2 = 1.
    t = sp.Rational(t)
    return (
        2*t/(1+t*t),
        (1-t*t)/(1+t*t)
    )

def canonical_cyclotomic_value(A, B, d, p):
    """
    Canonical representation in Q[x]/Phi_p(x) of
    A - B*cos(2*pi*d/p)
      = A - B*(zeta^d + zeta^{-d})/2.
    """
    d %= p
    phi = sp.Poly(sp.cyclotomic_poly(p, x), x, domain=sp.QQ)
    expr = A - B*(x**d + x**((-d) % p))/2
    rem = sp.Poly(expr, x, domain=sp.QQ).rem(phi)
    return tuple(rem.nth(i) for i in range(phi.degree()))

def count_aligned_spectrum(ts, p):
    latitudes = [latitude(t) for t in ts]
    q = len(latitudes)
    vals = set()
    params = set()

    for a in range(q):
        ra, za = latitudes[a]
        for b in range(a, q):
            rb, zb = latitudes[b]
            A = sp.factor(ra**2 + rb**2 + (za-zb)**2)
            B = sp.factor(2*ra*rb)
            params.add((A, B))

            differences = range(1, p) if a == b else range(p)
            for d in differences:
                vals.add(canonical_cyclotomic_value(A, B, d, p))

    return len(vals), len(params)

# t and 1/t give equal radii and opposite heights.
tests = [
    [sp.Rational(1, 2), sp.Rational(2), sp.Rational(2, 3)],
    [sp.Rational(1, 3), sp.Rational(3), sp.Rational(3, 4),
     sp.Rational(4, 3)]
]

for p in [5, 7, 11, 13]:
    for ts in tests:
        D, number_of_parameter_pairs = count_aligned_spectrum(ts, p)
        q = len(ts)
        n = q*p
        assert number_of_parameter_pairs >= q
        assert D >= q*(p-1)//2
        print("p =", p, "q =", q, "n =", n, "D =", D)
```

A numerical experiment for the number of vertices on random projected silhouettes:

```python
import numpy as np
from scipy.spatial import ConvexHull

def fibonacci_sphere(n):
    i = np.arange(n)
    z = 1 - 2*(i + 0.5)/n
    theta = np.pi*(3 - np.sqrt(5))*i
    r = np.sqrt(1-z*z)
    return np.column_stack((r*np.cos(theta), r*np.sin(theta), z))

def random_plane_basis():
    normal = np.random.normal(size=3)
    normal /= np.linalg.norm(normal)

    v = np.random.normal(size=3)
    v -= np.dot(v, normal)*normal
    v /= np.linalg.norm(v)
    w = np.cross(normal, v)
    return np.vstack((v, w))

for n in [400, 1600, 6400, 25600]:
    X = fibonacci_sphere(n)
    counts = []
    for _ in range(100):
        basis = random_plane_basis()
        projected = X @ basis.T
        hull = ConvexHull(projected)
        counts.append(len(hull.vertices))
    print(n, max(counts), "ratio to sqrt(n):",
          max(counts)/np.sqrt(n))
```

The final experiment is only numerical; Proposition 2 supplies the rigorous construction and bound.

## Route Diagnosis

**Proved ledger.**

- A face containing \(n-o(n)\) vertices gives the desired bound by Altman’s planar theorem.
- There are spherical \(n\)-vertex polytopes for which every great-circle support sweep sees only \(O(\sqrt n)\) vertices.
- A convex cyclic order in projection does not by itself control the original three-dimensional distances.
- Normal-fan adjacency is unusable as the sole pair-selection mechanism because arbitrarily large prisms can have all edges equal.
- Aligned rational prime-order latitude-orbit configurations satisfy
  \[
  D\ge\frac{n-q}{2},
  \]
  excluding this natural counterexample family when the orbit order tends to infinity.

**Dead ends.**

- **One support sweep:** blocked by Proposition 2.
- **Apply Altman after projection:** invalidated by the icosahedral decagon.
- **Select consecutive support vertices:** blocked by equal-edge prisms.
- **Sum over several sweeps or faces:** no control was found on overlaps between their numerical distance spectra.

**Plausible but unproved claims.**

- A successful support argument may require a two-dimensional, multiscale charging scheme over the entire normal fan rather than cyclic orders from individual sweeps.
- Nonidentical affine cosine spectra with arbitrary phase offsets may have only sublinear overlap as the orbit order grows.
- Near-extremal configurations may need to be asymptotically polygonal, pyramidal, cyclic, or dihedral.

**Precise block.** Covering the normal fan by many sweeps is easy, but no mechanism controls reuse of one numerical distance across different sweeps. Establishing a collection of \(n-o(n)\) support-selected pairs with multiplicity at most two would itself amount to essentially the missing global charging theorem. Local support geometry supplies neither the required total order nor the needed global control of equal-distance coincidences.

A fresh attempt should either develop a genuinely two-dimensional normal-fan charging principle involving nonlocal chords, or pursue the cyclotomic route by classifying intersections of phase-shifted cosine spectra. The latter now appears more concrete: the aligned rational case is rigid by Galois conjugacy, while the unresolved difficulty is exact spectral overlap caused by angular offsets and coefficients in cyclotomic extensions.