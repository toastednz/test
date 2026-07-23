STATUS: BLOCKED

## Result

Route 2 yields an exact reformulation but not a solution. For the projections
\[
v_t=(1,t,t^2),\qquad
\pi_t(x,y,z)=(y-tx,\ z-ty),
\]
let \(E_t(S)\) be the maximum length of an \(S\)-word whose projected prefix sums are pairwise distinct and contain no three collinear points. Each \(E_t(S)\) is finite by the planar Gerver–Ramsey theorem. I prove, however, that the three-dimensional extremal length is exactly
\[
L_S=\sup_{t\in\mathbb Z}E_t(S)
     =\lim_{|t|\to\infty}E_t(S)
\]
in the extended integers. Thus the open problem is precisely whether the pointwise-finite planar bounds are uniformly bounded over this one-parameter family of projections. I also prove a quantitative obstruction: if an infinite three-dimensional counterexample exists and \(B=\max_{s\in S}\|s\|_\infty\), then
\[
E_t(S)\ge 1+\left\lfloor\sqrt{\frac{|t|-2}{2B^2}}\right\rfloor.
\]
Consequently, projected collinear triples must escape to scales \(\gg\sqrt{|t|}\), so naive synchronization cannot work. A common uniform finite projection bound would synchronize by a direct pigeonhole argument, but establishing such a bound is equivalent in strength to the original problem.

## Complete Argument

### 1. The moment-curve family of projections

For \(t\in\mathbb Z\), define
\[
v_t=(1,t,t^2)
\]
and
\[
\pi_t:\mathbb Z^3\longrightarrow\mathbb Z^2,\qquad
\pi_t(x,y,z)=(y-tx,\ z-ty).
\]

Its kernel is exactly \(\mathbb Z v_t\). Indeed,
\[
\pi_t(x,y,z)=0
\]
is equivalent to
\[
y=tx,\qquad z=ty=t^2x,
\]
and hence
\[
(x,y,z)=x(1,t,t^2).
\]

For \(u,w\in\mathbb Z^3\), direct expansion gives
\[
\det(\pi_tu,\pi_tw)
=(u\times w)\cdot v_t.
\]
Writing \(c=u\times w=(c_1,c_2,c_3)\), this is
\[
\det(\pi_tu,\pi_tw)=c_1+c_2t+c_3t^2. \tag{1}
\]

Therefore, if three points \(a_i,a_j,a_k\) have
\[
u=a_j-a_i,\qquad w=a_k-a_i,
\]
then their \(\pi_t\)-images are collinear exactly when
\[
c_1+c_2t+c_3t^2=0,\qquad c=u\times w. \tag{2}
\]

In particular:

**Lemma 1.** If a fixed triple is projection-collinear for three distinct integers \(t\), then it is actually collinear in \(\mathbb Z^3\).

**Proof.** The polynomial in (2) has degree at most two. Three distinct roots force \(c_1=c_2=c_3=0\), so \(u\times w=0\). ∎

Thus the algebraic synchronization mechanism itself is perfect: the obstruction is forcing the same triple to arise for three projections.

---

### 2. A quantitative generic-projection lemma

Call a finite \(S\)-walk **good** if its vertices are pairwise distinct and contain no three collinear points.

Set
\[
B=\max\left(1,\max_{s\in S}\|s\|_\infty\right).
\]

Consider a good \(S\)-walk
\[
a_1,\ldots,a_N.
\]
For \(i<j<k\), put
\[
u=a_j-a_i,\qquad w=a_k-a_i,\qquad c=u\times w.
\]
Since at most \(N-1\) steps occur between any two of these vertices,
\[
\|u\|_\infty,\|w\|_\infty\le B(N-1).
\]
Consequently every coordinate of \(c\) satisfies
\[
|c_r|\le 2B^2(N-1)^2. \tag{3}
\]
Let
\[
C_N=2B^2(N-1)^2.
\]

Suppose the projected triple is collinear. Since the original path is good, \(c\ne0\), and by (2)
\[
c_1+c_2t+c_3t^2=0.
\]

If \(c_3\ne0\), then with \(x=|t|\),
\[
x^2\le C_Nx+C_N.
\]
This is impossible for \(x>C_N+1\). If \(c_3=0\) but \(c_2\ne0\), then
\[
|t|=\left|\frac{c_1}{c_2}\right|\le C_N.
\]
Finally, if \(c_3=c_2=0\), the equation would force \(c_1=0\), contradicting \(c\ne0\).

It remains to exclude collisions under projection. If
\[
\pi_t(a_i)=\pi_t(a_j),
\]
then, since \(\ker\pi_t=\mathbb Zv_t\),
\[
a_j-a_i=q(1,t,t^2)
\]
for some nonzero \(q\in\mathbb Z\). Hence
\[
t^2\le |q|t^2\le B(N-1).
\]
This also cannot occur when \(|t|>C_N+1\).

We have proved:

**Lemma 2 (uniform generic projection for finite paths).**  
If \(a_1,\ldots,a_N\) is a good \(S\)-walk and
\[
|t|>2B^2(N-1)^2+1, \tag{4}
\]
then
\[
\pi_t(a_1),\ldots,\pi_t(a_N)
\]
are pairwise distinct and contain no three collinear points. ∎

The important feature is that the bound depends only on \(S\) and \(N\), not on the particular path.

---

### 3. Exact extremal reformulation

Let \(L_S\in\mathbb N\cup\{\infty\}\) be the supremum of the numbers of vertices in good \(S\)-walks starting at \(0\).

Because the tree of finite good \(S\)-walks is finitely branching, König’s infinity lemma gives:
\[
L_S=\infty
\quad\Longleftrightarrow\quad
\text{there exists an infinite good \(S\)-walk}. \tag{5}
\]

For \(t\in\mathbb Z\), let \(E_t(S)\) be the supremum of those \(N\) for which there is an \(S\)-word whose prefix sums
\[
a_1=0,a_2,\ldots,a_N
\]
have the property that
\[
\pi_t(a_1),\ldots,\pi_t(a_N)
\]
are pairwise distinct and contain no three collinear points.

Each \(E_t(S)\) is finite. Otherwise, König’s lemma applied to the finitely branching tree of such words would give an infinite injective \(\pi_t(S)\)-walk in \(\mathbb Z^2\) with no collinear triple, contradicting the planar Gerver–Ramsey theorem.

We now compare \(E_t(S)\) and \(L_S\).

**Lemma 3.**
\[
E_t(S)\le L_S\qquad\text{for every }t. \tag{6}
\]

**Proof.** Let an \(S\)-word have a projected path that is injective and triple-free. If two original prefix sums were equal, their projections would be equal, so the original path is injective. If three original vertices were collinear, their projected images would also be collinear; because the projected path is injective, these would be three distinct projected points. Thus the lifted path is good. ∎

Conversely, Lemma 2 shows that every finite good three-dimensional path is seen faithfully by all sufficiently large \(t\).

**Lemma 4.** If \(N\le L_S\), then
\[
E_t(S)\ge N
\]
whenever
\[
|t|>2B^2(N-1)^2+1. \tag{7}
\]

**Proof.** Choose a good \(S\)-walk of \(N\) vertices and apply Lemma 2. ∎

Combining Lemmas 3 and 4 gives the principal exact reformulation.

**Theorem 5 (exact projection-extremal identity).**
\[
L_S=\sup_{t\in\mathbb Z}E_t(S)
    =\lim_{|t|\to\infty}E_t(S)
\]
in \(\mathbb N\cup\{\infty\}\).

More explicitly:

1. If \(L_S<\infty\), then
   \[
   E_t(S)=L_S
   \]
   for all
   \[
   |t|>2B^2(L_S-1)^2+1.
   \]

2. If \(L_S=\infty\), then \(E_t(S)\to\infty\), and for \(|t|\ge2\),
   \[
   E_t(S)\ge
   1+\left\lfloor
   \sqrt{\frac{|t|-2}{2B^2}}
   \right\rfloor. \tag{8}
   \]

**Proof.** If \(L_S<\infty\), choose a good path of length \(L_S\). Lemma 4 gives \(E_t(S)\ge L_S\) for all sufficiently large \(t\), while Lemma 3 gives the reverse inequality.

If \(L_S=\infty\), Lemma 4 applies for every \(N\). For (8), put
\[
r=\left\lfloor\sqrt{\frac{|t|-2}{2B^2}}\right\rfloor,\qquad N=r+1.
\]
Then
\[
2B^2(N-1)^2\le |t|-2,
\]
so (7) applies. ∎

This proves the exact fixed-\(S\) equivalence
\[
\boxed{
\text{No infinite good \(S\)-walk}
\iff
\sup_{t\in\mathbb Z}E_t(S)<\infty.
} \tag{9}
\]

It also gives the quantitative criterion
\[
L_S<\infty
\iff
\liminf_{|t|\to\infty}\frac{E_t(S)}{\sqrt{|t|}}=0. \tag{10}
\]
Indeed, finite \(L_S\) makes the quotient tend to zero, while \(L_S=\infty\) and (8) give
\[
\liminf_{|t|\to\infty}\frac{E_t(S)}{\sqrt{|t|}}
\ge \frac1{\sqrt2\,B}.
\]

Thus a sufficiently strong quantitative planar estimate for the special alphabets
\[
\pi_t(S)=\{(y-tx,z-ty):(x,y,z)\in S\}
\]
would solve the problem. Pointwise finiteness alone does not.

---

### 4. What every projection supplies in a hypothetical counterexample

Assume now, for diagnosis, that
\[
(a_n)_{n\ge1}
\]
is an infinite good \(S\)-walk.

Let \(v\in\mathbb Z^3\) be primitive and let
\[
\pi_v:\mathbb Z^3\to\mathbb Z^2
\]
be an integer quotient map with kernel \(\mathbb Zv\).

Every fiber of \(\pi_v\) is an affine line parallel to \(v\). Since the original walk contains no three collinear points, each fiber contains at most two vertices of the walk. Therefore the projected image is infinite.

Applying the planar Gerver–Ramsey theorem to any tail gives three distinct projected points which are collinear. For the corresponding original points, with
\[
c=(a_j-a_i)\times(a_k-a_i),
\]
we have
\[
c\cdot v=0.
\]
Since the original walk is good, \(c\ne0\).

Hence:

**Lemma 6 (normal-plane covering property).**  
For every primitive \(v\in\mathbb Z^3\) and every starting index \(n_0\), there are
\[
n_0\le i<j<k
\]
such that
\[
c=(a_j-a_i)\times(a_k-a_i)\ne0
\]
and
\[
c\cdot v=0. \tag{11}
\]

Thus, in every tail, the orthogonal planes of the nonzero triangle normals cover all primitive integer directions.

For \(v_t=(1,t,t^2)\), each nonzero normal covers at most two values of \(t\), by Lemma 1. Consequently, the planar theorem must produce infinitely many genuinely different triples as \(t\) varies.

There is also a scale restriction. If a triple with index span
\[
\ell=k-i
\]
is \(\pi_t\)-collinear, then the proof of Lemma 2 gives
\[
|t|\le 2B^2\ell^2+1.
\]
Therefore
\[
\ell\ge
\sqrt{\frac{|t|-1}{2B^2}}. \tag{12}
\]

So in a hypothetical counterexample, every projection-collinear triple for a large \(t\) necessarily occurs over a long index scale. This quantitatively explains why fixed-window synchronization fails.

---

### 5. Syndetic projected triples and the exact synchronization obstruction

For fixed \(t\), define \(F_t(S)\) to be the maximum length of a labeled \(\pi_t(S)\)-walk satisfying:

1. every projected point occurs at most twice;
2. the projected image has no three distinct collinear points.

This number is finite. Otherwise, König’s lemma would produce an infinite projected walk with infinite image—every point occurs at most twice—and no collinear triple, contradicting the planar theorem.

In the hypothetical three-dimensional counterexample, every projected point occurs at most twice. Hence every block of
\[
F_t(S)+1
\]
consecutive original indices contains a triple of distinct \(\pi_t\)-images that is collinear. Thus projected-collinear triples are syndetic for each fixed projection, although the syndeticity constants may depend arbitrarily on \(t\).

The quantities \(F_t\) can be bounded in terms of \(E_t\). Let \(D=|S|\). In any sequence counted by \(F_t\), form the directed graph whose vertices are the distinct projected points and whose directed edges are the observed transitions. Every vertex is reachable from the initial point. A shortest directed path to any vertex is simple, and hence has at most \(E_t(S)\) vertices. Since the out-degree is at most \(D\),
\[
|\operatorname{image}|
\le \sum_{r=0}^{E_t(S)-1}D^r.
\]
Each point occurs at most twice, so
\[
F_t(S)\le
2\sum_{r=0}^{E_t(S)-1}D^r. \tag{13}
\]

Now suppose, hypothetically, that one had a uniform bound
\[
F_t(S)<Q\qquad\text{for every }t\in\mathbb Z. \tag{14}
\]
Choose more than
\[
2\binom Q3
\]
distinct integers \(t\). For each such \(t\), the first \(Q\) vertices contain a projected-collinear triple. If there is no actual collinear triple, each fixed index triple can be projection-collinear for at most two \(t\)'s. But only \(\binom Q3\) index triples are available, giving at most
\[
2\binom Q3
\]
projection incidences, a contradiction.

Thus a uniform bound would complete Route 2. By (13), a uniform bound on \(E_t(S)\) would suffice. But Theorem 5 shows that
\[
\sup_tE_t(S)<\infty
\]
is itself equivalent to the desired fixed-\(S\) conclusion. The synchronization problem has therefore reduced exactly to a uniformity statement of comparable strength.

---

### 6. Ledger

#### Proved lemmas

1. The determinant identity
   \[
   \det(\pi_tu,\pi_tw)=(u\times w)\cdot(1,t,t^2).
   \]
2. A fixed noncollinear triple is projection-collinear for at most two values of \(t\).
3. Every good \(N\)-vertex \(S\)-walk projects injectively and triple-freely for
   \[
   |t|>2B^2(N-1)^2+1.
   \]
4. The exact extremal identity
   \[
   L_S=\sup_tE_t(S)=\lim_{|t|\to\infty}E_t(S).
   \]
5. Under a counterexample,
   \[
   E_t(S)\gg_S\sqrt{|t|}.
   \]
6. Every tail of a hypothetical counterexample supplies nonzero triangle normals whose orthogonal planes cover every primitive integer direction.
7. For each fixed projection, projected-collinear triples occur with bounded gaps, but the bound may depend on the projection.
8. A uniform family of planar bounds would synchronize and prove the theorem.

#### Plausible but unproved claims

1. For each fixed \(S\), the special planar extremal quantities \(E_t(S)\) might admit an upper bound \(o_S(\sqrt{|t|})\) along some unbounded sequence of \(t\). By (10), this would solve the fixed-\(S\) problem.
2. The two-scale form
   \[
   \pi_t(x,y,z)=(y-tx,z-ty)
   \]
   may permit a stronger planar theorem than is available for arbitrary step sets of coordinate size \(O(t)\).
3. A quantitative version of the Gerver–Ramsey proof might control \(E_t(S)\) in terms of arithmetic invariants of \(\pi_t(S)\), but no suitable estimate was derived.

#### Dead ends

1. **Three projections without a common bound.**  
   A common triple for three \(t\)'s would work, but the planar theorem may choose entirely different triples. Pointwise existence gives no finite pigeonhole set.

2. **Incidence counting over many projections.**  
   It succeeds only if the relevant projected triples all occur in a common bounded prefix. Under a counterexample, their necessary scales grow at least as \(\sqrt{|t|}\).

3. **Generic irrational projection.**  
   A generic real direction avoids all countably many nonzero triangle-normal planes, producing a triple-free planar projection. The projected subgroup is no longer a rank-two lattice, so the planar theorem is unavailable. Baire-category genericity therefore does not create a contradiction.

4. **Taking \(t\to\infty\).**  
   After rescaling, \(\pi_t(S)\) approaches a planar projection of \(S\), but exact collinearity is not stable under perturbation: an arbitrarily small second-order term can destroy every finite collection of collinearities.

## Self-Audit

1. **The decisive uniform bound is not proved.**  
   This is not a minor gap: Theorem 5 shows that uniform boundedness of \(E_t(S)\) is equivalent to the fixed-\(S\) instance of the original problem. I have no justification for asserting it, which is why the status is BLOCKED.

2. **Finiteness of \(E_t\) and \(F_t\) uses the planar Gerver–Ramsey theorem as an external input.**  
   Given that theorem, the deductions are sound: arbitrary finite depths form a finitely branching hereditary tree, and an infinite branch would have infinite image and no projected collinear triple.

3. **The quantitative projection threshold must handle both collinear projected triples and pair collisions.**  
   Both were checked separately. Triple collinearity is controlled by the quadratic polynomial (2); a pair collision forces a difference to equal \(q(1,t,t^2)\), whose third coordinate already exceeds the allowed \(B(N-1)\) range for sufficiently large \(t\).

## Computations To Verify

The following exact Python code tests the determinant identity, finite good paths, projected extremal paths, and projection-triple intersections.

```python
from itertools import product, combinations
from math import gcd, isqrt

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def det2(u, v):
    return u[0]*v[1] - u[1]*v[0]

def canonical_direction(d):
    g = 0
    for x in d:
        g = gcd(g, abs(x))
    assert g != 0
    d = tuple(x // g for x in d)
    for x in d:
        if x != 0:
            if x < 0:
                d = tuple(-y for y in d)
            break
    return d

def can_add_good(path, q):
    """Exact test: path already injective/triple-free."""
    if q in path:
        return False
    seen = set()
    for p in path:
        d = canonical_direction(sub(p, q))
        if d in seen:
            return False
        seen.add(d)
    return True

def pi_t(p, t):
    x, y, z = p
    return (y - t*x, z - t*y)

def projected_path(path3, t):
    return [pi_t(p, t) for p in path3]

def is_good(path):
    built = []
    for q in path:
        if not can_add_good(built, q):
            return False
        built.append(q)
    return True

def exists_good_3d(S, N):
    """Exhaustive DFS. Returns one N-vertex path or None."""
    def rec(path):
        if len(path) == N:
            return path
        for s in S:
            q = add(path[-1], s)
            if can_add_good(path, q):
                ans = rec(path + [q])
                if ans is not None:
                    return ans
        return None
    return rec([(0, 0, 0)])

def exists_projected_good(S, t, N):
    """
    Searches labeled S-words whose pi_t-prefixes are injective
    and contain no three collinear points.
    """
    projected_steps = [pi_t(s, t) for s in S]

    def rec(path2):
        if len(path2) == N:
            return path2
        for ds in projected_steps:
            q = add(path2[-1], ds)
            if can_add_good(path2, q):
                ans = rec(path2 + [q])
                if ans is not None:
                    return ans
        return None

    return rec([(0, 0)])

def projected_collinear_triples(path3, t):
    p2 = projected_path(path3, t)
    out = set()
    for i, j, k in combinations(range(len(path3)), 3):
        if len({p2[i], p2[j], p2[k]}) < 3:
            continue
        u = sub(p2[j], p2[i])
        w = sub(p2[k], p2[i])
        if det2(u, w) == 0:
            out.add((i, j, k))
    return out

def actual_collinear(path3, I):
    i, j, k = I
    u = sub(path3[j], path3[i])
    w = sub(path3[k], path3[i])
    return cross(u, w) == (0, 0, 0)

def verify_determinant_identity(bound=5):
    vals = range(-bound, bound + 1)
    for u in product(vals, repeat=3):
        for w in product(vals, repeat=3):
            c = cross(u, w)
            for t in range(-bound, bound + 1):
                lhs = det2(pi_t(u, t), pi_t(w, t))
                rhs = c[0] + t*c[1] + t*t*c[2]
                assert lhs == rhs

def verify_projection_threshold(S, N):
    """
    Exhaustively checks every S-word of length N-1.
    Intended only for small N.
    """
    B = max(1, max(max(abs(x) for x in s) for s in S))
    T = 2 * B * B * (N - 1) * (N - 1) + 2

    for word in product(S, repeat=N-1):
        path = [(0, 0, 0)]
        for s in word:
            path.append(add(path[-1], s))
        if not is_good(path):
            continue
        for t in (T, -T):
            p2 = projected_path(path, t)
            assert is_good(p2)

def test_projection_overlap(path3, t_values):
    """
    For a triple-free 3D path, checks that each index triple
    is projection-collinear for at most two tested t-values.
    """
    incidence = {}
    for t in t_values:
        for I in projected_collinear_triples(path3, t):
            incidence.setdefault(I, []).append(t)

    for I, ts in incidence.items():
        if not actual_collinear(path3, I):
            assert len(ts) <= 2
    return incidence

# Suggested candidate step sets for experiments:
S1 = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, -1, -1),
]

S2 = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
]

# Example finite experiments:
# verify_determinant_identity(2)
# verify_projection_threshold(S1, 6)
#
# for t in range(1, 30):
#     for N in range(2, 20):
#         if exists_projected_good(S1, t, N) is None:
#             print("Certified E_t <", N, "for t =", t)
#             break
```

For testing the repeated-point extremal quantity \(F_t\):

```python
def can_add_image_point(image_points, q):
    """image_points is a set already containing no collinear triple."""
    if q in image_points:
        return True
    seen = set()
    for p in image_points:
        d = canonical_direction(sub(p, q))
        if d in seen:
            return False
        seen.add(d)
    return True

def exists_projected_multiplicity2(S, t, N):
    projected_steps = [pi_t(s, t) for s in S]

    def rec(last, counts, seq_len):
        if seq_len == N:
            return True
        for ds in projected_steps:
            q = add(last, ds)
            old = counts.get(q, 0)
            if old >= 2:
                continue
            if old == 0 and not can_add_image_point(set(counts), q):
                continue
            counts[q] = old + 1
            if rec(q, counts, seq_len + 1):
                return True
            if old == 0:
                del counts[q]
            else:
                counts[q] = old
        return False

    return rec((0, 0), {(0, 0): 1}, 1)
```

The most informative experiments would compute, for fixed rank-three \(S\),

1. the largest certified \(E_t(S)\) for \(1\le t\le T\);
2. the ratio \(E_t(S)/\sqrt t\);
3. the first projection-collinear triple for each \(t\);
4. pairwise and triple intersections of the corresponding hypergraphs;
5. whether first failures occur at spans comparable to the lower bound in (12).

## Route Diagnosis

The projection algebra works exceptionally cleanly: three synchronized moment-curve projections force actual collinearity, and every individual projection supplies projected collinear triples with bounded gaps. The failure is entirely one of uniformity. The planar theorem gives a finite bound for each \(\pi_t(S)\), but no control uniform in \(t\); Theorem 5 shows that obtaining such control is equivalent to solving the original problem for \(S\). Moreover, under a counterexample the extremal projected lengths must grow at least as \(\sqrt{|t|}\), so projected triples necessarily move to larger scales as the kernel direction varies.

A fresh attempt on Route 2 should therefore not seek mere abundance for each fixed projection. It should target one of the following genuinely stronger statements:

1. an upper bound
   \[
   E_t(S)=o_S(\sqrt{|t|})
   \]
   along some unbounded sequence of \(t\);
2. a common-prefix theorem for many \(t\)'s that is stronger than separate planar Gerver–Ramsey bounds;
3. arithmetic control of the special two-scale alphabets
   \[
   \pi_t(S)=\{(y-tx,z-ty):(x,y,z)\in S\};
   \]
4. a mechanism forcing substantial overlap between the projected-collinearity hypergraphs, rather than merely many triples in each one.

No superior alternative route emerged from this analysis. The route is therefore blocked precisely at a uniform quantitative strengthening of the planar theorem, not at the projection algebra or compactness steps.