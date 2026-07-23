STATUS: BLOCKED

## Result

Route 3 yields several rigorous structural reductions but not a complete solution. I prove that a counterexample cannot lie, even for arbitrarily long bounded-gap stretches, in a bounded-width rational slab or in any finite union of affine planes. More precisely, for fixed \(S\), every triple-free \(S\)-walk must escape every translated rational slab in a uniform piecewise-syndetic sense. I also prove that no infinite bounded-step walk contained in a bounded-distance tube around any real affine line can be a counterexample; in fact it contains a three-term arithmetic progression. Finally, any hypothetical counterexample can be replaced by a uniformly recurrent one, and every return-word renormalization of such a minimal counterexample must still have rank \(3\) and at least four distinct effective step vectors. The route is blocked because bounded-step walks need not produce long fixed-width planar or linear pieces, and the descending full-rank return lattices supplied by renormalization need not stabilize or drop rank.

## Complete Argument

I index vertices as
\[
p_0,p_1,p_2,\ldots,\qquad p_{n+1}-p_n\in S,
\]
which is only a shift of the notation in the problem.

### 1. The planar finite extremal input

I will use the following consequence of the Gerver–Ramsey theorem.

**Planar finite extremal fact.**  
If \(T\) is a finite subset of a free abelian subgroup \(H\leq \mathbb Z^3\) of rank at most \(2\), then there is an integer \(N(T)\) such that every injective \(T\)-walk of \(N(T)\) vertices contains three collinear points.

**Justification.** If no such \(N(T)\) existed, the finitely branching tree of all finite injective, triple-free \(T\)-walks starting at \(0\) would have vertices at every depth. König’s infinity lemma would give an infinite injective triple-free \(T\)-walk in an affine copy of a rank-\(\leq2\) lattice, contradicting the planar Gerver–Ramsey theorem. ∎

### 2. Piecewise-syndetic extraction

A set \(A\subseteq\mathbb Z\) is called **thick** if it contains intervals of arbitrarily large finite length. It is **piecewise syndetic** if \(A+F\) is thick for some finite \(F\subseteq\mathbb Z\).

We need two elementary facts.

**Lemma 2.1 — finite partitions preserve one piecewise-syndetic cell.**  
If a piecewise-syndetic set \(P\) is partitioned into finitely many sets
\[
P=C_1\cup\cdots\cup C_r,
\]
then at least one \(C_i\) is piecewise syndetic. In particular, in every finite coloring of \(\mathbb N\), one color class is piecewise syndetic.

**Proof.** It suffices to prove the assertion for a partition \(P=A\cup B\). Choose finite \(F\) such that
\[
P+F=(A+F)\cup(B+F)
\]
is thick. If \(A\) is piecewise syndetic, there is nothing to prove. Otherwise \(A+F\) is not thick, so there is some \(q\geq1\) such that \(A+F\) contains no interval of \(q\) consecutive integers.

Let \(I\) be an arbitrarily long interval contained in \(P+F\). Every interval of \(q\) consecutive integers contained in \(I\) has a point outside \(A+F\), and that point necessarily belongs to \(B+F\). Consequently, for every \(x\) sufficiently far from the right endpoint of \(I\), there are \(y\in B+F\) and \(t\in\{0,\ldots,q-1\}\) such that
\[
x=y-t.
\]
Thus
\[
B+F-\{0,\ldots,q-1\}
\]
contains intervals of arbitrarily large length. Hence \(B\) is piecewise syndetic. Induction proves the finite-partition assertion. ∎

**Lemma 2.2 — bounded-gap characterization.**  
A set \(A\subseteq\mathbb Z\) is piecewise syndetic if and only if there is \(R<\infty\) such that, for every \(L\), there are
\[
n_1<n_2<\cdots<n_L,\qquad n_i\in A,
\]
with
\[
n_{i+1}-n_i\leq R.
\]

**Proof.**

If such chains exist, then \(A+\{0,\ldots,R\}\) contains the entire interval \([n_1,n_L]\), whose length tends to infinity with \(L\). Thus \(A\) is piecewise syndetic.

Conversely, suppose \(A+F\) is thick. Put
\[
D=\max F-\min F.
\]
Given an arbitrarily long interval \([u,u+M]\subseteq A+F\), choose for each integer \(x\) in this interval a representation
\[
x=a_x+f_x,\qquad a_x\in A,\quad f_x\in F.
\]
Then
\[
|a_{x+1}-a_x|
 =|1+f_x-f_{x+1}|
 \leq D+1.
\]
Moreover,
\[
a_{u+M}-a_u\geq M-D.
\]
The set of values visited by the integer sequence \(a_x\) therefore contains a chain from near \(a_u\) to near \(a_{u+M}\) whose successive ordered values differ by at most \(D+1\). As \(M\to\infty\), these chains have arbitrarily many distinct elements. ∎

### 3. No counterexample lies in a finite union of affine planes

**Theorem 3.1.**  
Let \(S\subseteq\mathbb Z^3\) be finite. An infinite injective \(S\)-walk contained in a finite union
\[
(x_1+H_1)\cup\cdots\cup(x_r+H_r),
\]
where each \(H_c\leq\mathbb Z^3\) has rank at most \(2\), contains three collinear points.

The same conclusion holds if the image is contained in a finite union of arbitrary proper affine planes in \(\mathbb R^3\).

**Proof.** Assign each index \(n\) a color \(c\) such that
\[
p_n\in x_c+H_c.
\]
By Lemmas 2.1 and 2.2, there are a color \(c\) and \(R<\infty\) such that for every \(L\) one can find indices
\[
n_1<\cdots<n_L,\qquad n_{j+1}-n_j\leq R,
\]
with all \(p_{n_j}\in x_c+H_c\).

Define the finite set
\[
T_R=
\left\{
s_1+\cdots+s_q:
1\leq q\leq R,\ s_i\in S
\right\}.
\]
Then
\[
p_{n_{j+1}}-p_{n_j}\in T_R\cap H_c.
\]
Thus
\[
p_{n_1},\ldots,p_{n_L}
\]
is an injective \((T_R\cap H_c)\)-walk in an affine rank-\(\leq2\) lattice. Taking
\[
L\geq N(T_R\cap H_c)
\]
and applying the planar finite extremal fact gives three collinear points among these vertices.

For a proper affine plane \(P\subseteq\mathbb R^3\), choose one lattice point \(x\in P\cap\mathbb Z^3\), if this intersection is nonempty. Then
\[
P\cap\mathbb Z^3=x+\bigl((P-P)\cap\mathbb Z^3\bigr),
\]
and the latter subgroup has rank at most \(2\). Hence the first assertion applies. ∎

**Corollary 3.2 — rational slabs are impossible.**  
Let \(\ell:\mathbb Z^3\to\mathbb Z\) be a nonzero integer linear functional. If an infinite injective bounded-step walk satisfies
\[
c\leq \ell(p_n)\leq c+B
\]
for all \(n\), then it contains three collinear points.

**Proof.** The image lies in the finite union of affine planes
\[
\bigcup_{j=c}^{c+B}\{x:\ell(x)=j\}.
\]
Apply Theorem 3.1. ∎

In particular, if \(H\leq\mathbb Z^3\) has rank \(2\), then a bounded-distance neighborhood of an affine copy of \(H\) lies in finitely many level planes of an integer functional vanishing on \(H\). Thus such a neighborhood cannot contain a counterexample.

### 4. A uniform slab-escape theorem for fixed \(S\)

The preceding result has a useful finite extremal strengthening.

**Theorem 4.1 — uniform piecewise-syndetic slab escape.**  
Fix finite \(S\subseteq\mathbb Z^3\), a nonzero integer functional \(\ell\), and integers \(B,R\geq1\). There is
\[
K=K(S,\ell,B,R)
\]
such that the following cannot occur in an injective triple-free \(S\)-walk: indices
\[
n_1<\cdots<n_K,\qquad n_{j+1}-n_j\leq R,
\]
for which all the values \(\ell(p_{n_j})\) lie in one interval of length \(B\).

**Proof.** Suppose no such \(K\) existed. For arbitrarily large \(L\), select
\[
n_1<\cdots<n_L
\]
as in the statement. The selected vertices form an injective triple-free \(T_R\)-walk, where \(T_R\) is as in Theorem 3.1.

Translate its first vertex to \(0\). Since all selected \(\ell\)-values lie in an interval of length \(B\), every translated vertex \(q\) satisfies
\[
|\ell(q)|\leq B.
\]
Thus there are arbitrarily long injective triple-free \(T_R\)-walks starting at \(0\) and contained in
\[
\bigcup_{j=-B}^{B}\{x:\ell(x)=j\}.
\]
By König’s infinity lemma there is an infinite such walk, contradicting Theorem 3.1. ∎

Taking \(R=1\) gives the direct Route 3 conclusion:

**Corollary 4.2.**  
For fixed \(S,\ell,B\), there is a finite bound on the length of any contiguous triple-free \(S\)-subwalk whose \(\ell\)-range is at most \(B\).

Thus the “planar branch” of the proposed Route 3 dichotomy is completely handled: if one can force arbitrarily long subwalks in one fixed-width rational slab, the original problem follows.

The obstruction is that bounded-step motion alone does not force such subwalks. For instance,
\[
p_n=(n,\lfloor \alpha n\rfloor,\lfloor\beta n\rfloor),
\]
with \(1,\alpha,\beta\) linearly independent over \(\mathbb Q\), satisfies
\[
\ell(p_n)=c_\ell n+O(1),\qquad c_\ell\neq0
\]
for every nonzero integer functional \(\ell\). Hence every fixed-width rational slab contains only a bounded consecutive portion of this walk. This example does contain collinear triples, as proved below, but it refutes the proposed purely slab-based structural lemma.

### 5. Bounded tubes around arbitrary real lines

The preceding digital-line example suggests replacing rational slabs by tubes around real lines. In rank one this can be done completely.

**Theorem 5.1.**  
Let \((p_n)\subseteq\mathbb Z^d\) be an infinite bounded-step walk with infinite image. If its image is contained in a bounded-distance neighborhood of a real affine line, then its image contains a nontrivial three-term arithmetic progression.

**Proof.** Write the line, after permuting and possibly reversing coordinates, as
\[
L=\{(t,\alpha_2t+\beta_2,\ldots,\alpha_dt+\beta_d):t\in\mathbb R\}.
\]
The first-coordinate values of the walk are unbounded in at least one direction, since a bounded segment of the tube contains only finitely many lattice points. Assume they are unbounded above.

Let
\[
D=\max_{s\in S}|s_1|.
\]
For every sufficiently large integer \(m\), let \(n\) be the first index with \((p_n)_1\geq m\). Then
\[
(p_{n-1})_1<m,\qquad (p_n)_1\leq m+D-1.
\]
Consequently, the set
\[
X=\{(p_n)_1:n\geq0\}
\]
meets every sufficiently far-out interval of \(D\) consecutive integers. Thus \(X\) is syndetic on a ray, hence piecewise syndetic.

For each \(x\in X\), choose one walk vertex \(p(x)\) whose first coordinate is \(x\). Since all points lie in a fixed-radius tube around \(L\), for each \(j=2,\ldots,d\) the integer
\[
e_j(x)=p_j(x)-\lfloor\alpha_jx+\beta_j\rfloor
\]
belongs to a fixed finite set. Partition \(X\) according to the finite vector
\[
e(x)=(e_2(x),\ldots,e_d(x)).
\]
By Lemma 2.1, one cell \(X_0\) is piecewise syndetic.

Partition \([0,1)\) into four half-open intervals of length \(1/4\). Further color each \(x\in X_0\) according to the boxes containing
\[
\{\alpha_jx+\beta_j\},\qquad j=2,\ldots,d.
\]
Again, one resulting cell \(C\subseteq X_0\) is piecewise syndetic.

Every piecewise-syndetic subset of \(\mathbb Z\) contains a nontrivial three-term arithmetic progression. Indeed, choose finite \(F\) such that \(C+F\) is thick. In a sufficiently long interval \(I\subseteq C+F\), color \(m\in I\) by one \(f\in F\) for which \(m-f\in C\). The finite van der Waerden theorem supplies
\[
m,m+r,m+2r
\]
of one color \(f\); subtracting \(f\) gives a three-term progression in \(C\).

Choose, therefore,
\[
x_0<x_1<x_2,\qquad x_0+x_2=2x_1,
\]
all in \(C\). Their error vectors \(e(x_i)\) are equal. For each \(j\geq2\), put
\[
y_i=\alpha_jx_i+\beta_j,\qquad f_i=\{y_i\}.
\]
Then
\[
y_0+y_2=2y_1.
\]
Moreover, \(f_0,f_1,f_2\) belong to one interval of length \(1/4\), so
\[
|f_0+f_2-2f_1|\leq\frac12<1.
\]
But
\[
\lfloor y_0\rfloor+\lfloor y_2\rfloor-2\lfloor y_1\rfloor
=-(f_0+f_2-2f_1)
\]
is an integer. It must therefore be \(0\). Adding the common error \(e_j\) shows
\[
p_j(x_0)+p_j(x_2)=2p_j(x_1).
\]
This also holds in the first coordinate, so
\[
p(x_0)+p(x_2)=2p(x_1).
\]
These are three distinct vertices of the original walk. ∎

**Corollary 5.2.**  
For arbitrary real \(\alpha,\beta,\gamma,\delta\), the walk
\[
p_n=(n,\lfloor\alpha n+\gamma\rfloor,\lfloor\beta n+\delta\rfloor)
\]
contains a three-term arithmetic progression.

Thus “digital irrational lines” cannot provide counterexamples.

### 6. Reduction to a uniformly recurrent counterexample

Finite local complexity gives another rigorous renormalization.

**Theorem 6.1.**  
If a counterexample exists, then one exists whose step word is uniformly recurrent.

**Proof.** Let
\[
x=s_0s_1s_2\cdots\in S^{\mathbb N}
\]
be the step word of a counterexample. Let \(X\) be the closure of its forward shift orbit in the compact space \(S^{\mathbb N}\). Choose a minimal nonempty closed shift-invariant subset \(Y\subseteq X\), and choose \(y\in Y\).

Minimality implies uniform recurrence: for every cylinder set \(U\subseteq Y\), the sets
\[
\sigma^{-n}U,\qquad n\geq0,
\]
cover \(Y\). A finite subcover shows that every orbit visits \(U\) with bounded gaps. Applying this to cylinders specified by finite factors gives uniform recurrence of \(y\).

Every finite prefix of \(y\) occurs as a factor of \(x\). If the walk generated by \(y\) had a repeated vertex, the corresponding finite factor would have sum \(0\), and its occurrence in \(x\) would give a repeated vertex there. Similarly, a collinear triple among finitely many prefix sums of \(y\) would transfer, by translation, to a collinear triple in the original walk. Hence the walk generated by \(y\) is again injective and triple-free. ∎

### 7. Return-word renormalization must remain genuinely rank three

Let \(y\) be a uniformly recurrent counterexample and let \(w\) be a finite factor of \(y\). Let
\[
0\leq k_0<k_1<k_2<\cdots
\]
be its occurrence positions, after shifting \(y\) if necessary. Uniform recurrence gives
\[
k_{i+1}-k_i\leq G(w)
\]
for all \(i\).

Let \(q_n\) be the prefix-sum walk generated by \(y\), and define
\[
D(w)=\{q_{k_{i+1}}-q_{k_i}:i\geq0\}.
\]
This is a finite set because the gaps are bounded and the original step alphabet is finite.

**Theorem 7.1.**  
For every factor \(w\) of a uniformly recurrent counterexample:

1. the subgroup generated by \(D(w)\) has rank \(3\);
2. \(D(w)\) contains at least four distinct vectors.

**Proof.** The occurrence-start sequence
\[
q_{k_0},q_{k_1},q_{k_2},\ldots
\]
is an infinite injective \(D(w)\)-walk and is triple-free because it is a subsequence of the original vertex set.

If \(\langle D(w)\rangle\) had rank at most \(2\), the planar Gerver–Ramsey theorem would give a collinear triple, a contradiction.

If \(D(w)\) had at most three distinct step vectors, the known abelian-square result for alphabets of size at most three would give a three-term arithmetic progression in this derived walk, again a contradiction. ∎

There is also a nested-lattice structure. If \(v\) is an extension of \(w\) beginning at the same alignment, then every occurrence of \(v\) is an occurrence of \(w\), and every return displacement between consecutive \(v\)-occurrences is a sum of return displacements for \(w\). Hence
\[
H_v:=\langle D(v)\rangle\subseteq \langle D(w)\rangle=:H_w.
\]
In a minimal counterexample this gives a descending family of full-rank sublattices
\[
H_{w_1}\supseteq H_{w_2}\supseteq H_{w_3}\supseteq\cdots
\]
along nested factors. Route 3 would succeed if one could prove that some sufficiently deep return lattice has rank at most \(2\), or that full-rank persistence forces parallel adjacent return sums. Neither implication is presently established; descending full-rank sublattices such as
\[
\mathbb Z^3\supset 2\mathbb Z^3\supset 6\mathbb Z^3\supset\cdots
\]
show that a purely group-theoretic stabilization argument is impossible.

## Self-Audit

1. **Dependence on the planar Gerver–Ramsey theorem and its finite compactness consequence.**  
   I have not reproved the planar theorem. It is explicitly part of the problem brief’s known background. The finite extremal version follows rigorously from König’s infinity lemma and finite branching.

2. **The piecewise-syndetic extraction is the most delicate combinatorial transfer.**  
   A mistake here would invalidate the finite-union-of-planes theorem. I gave a direct proof that piecewise syndeticity is partition regular and a direct bounded-gap characterization; the effective-step set is finite because selected index gaps are uniformly bounded.

3. **The bounded-line-tube theorem relies on selecting one point for each attained coordinate and then applying van der Waerden after real fractional-part coloring.**  
   The selection does not preserve the original index order, but only membership in the image is needed: once three selected points are collinear, their original occurrence indices can be sorted. The floor calculation is exact because its second difference is an integer of absolute value strictly less than \(1\).

The central weakness is not a hidden proof step but the missing global structural theorem: nothing proved here forces a general bounded-step path to spend long bounded-gap stretches in a fixed-width slab or tube.

## Computations To Verify

The following code performs exact incremental collinearity checks, slab diagnostics, return-displacement rank tests, and digital-line tests.

```python
from math import gcd
from functools import reduce
from fractions import Fraction

def gcd3(a, b, c):
    return reduce(gcd, (abs(a), abs(b), abs(c)))

def canonical_direction(d):
    """Primitive direction modulo sign."""
    if d == (0, 0, 0):
        raise ValueError("zero direction")
    g = gcd3(*d)
    v = tuple(x // g for x in d)
    for x in v:
        if x:
            if x < 0:
                v = tuple(-y for y in v)
            break
    return v

def first_collinear_extension(path, q):
    """
    Assumes path itself is triple-free.
    Returns two old indices collinear with q, or None.
    """
    seen = {}
    for i, p in enumerate(path):
        d = tuple(p[j] - q[j] for j in range(3))
        if d == (0, 0, 0):
            return ("repeat", i)
        v = canonical_direction(d)
        if v in seen:
            return (seen[v], i)
        seen[v] = i
    return None

def is_triple_free(path):
    built = []
    for q in path:
        if first_collinear_extension(built, q) is not None:
            return False
        built.append(q)
    return True

def dfs_path(S, target):
    """Find one triple-free S-walk of target vertices, if found."""
    start = (0, 0, 0)
    path = [start]
    used = {start}

    def rec():
        if len(path) == target:
            return path.copy()
        p = path[-1]
        for s in S:
            q = tuple(p[j] + s[j] for j in range(3))
            if q in used:
                continue
            if first_collinear_extension(path, q) is not None:
                continue
            path.append(q)
            used.add(q)
            ans = rec()
            if ans is not None:
                return ans
            used.remove(q)
            path.pop()
        return None

    return rec()
```

For a finite candidate path, this measures the largest bounded-gap cluster of visits to a translated slab:

```python
def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def max_slab_chain(path, ell, B, R):
    """
    Maximum number of indices in one component under index gaps <= R,
    among vertices whose ell-values lie in some interval [c,c+B].
    """
    h = [dot(ell, p) for p in path]
    best = 0
    for c in range(min(h) - B, max(h) + 1):
        inds = [i for i, x in enumerate(h) if c <= x <= c + B]
        run = 0
        prev = None
        for i in inds:
            if prev is None or i - prev <= R:
                run += 1
            else:
                run = 1
            best = max(best, run)
            prev = i
    return best
```

Return-displacement ranks for a long word can be inspected with exact integer linear algebra:

```python
from sympy import Matrix

def prefix_sums(steps):
    p = [(0, 0, 0)]
    for s in steps:
        p.append(tuple(p[-1][j] + s[j] for j in range(3)))
    return p

def occurrence_positions(word, pattern):
    m = len(pattern)
    return [i for i in range(len(word)-m+1)
            if word[i:i+m] == pattern]

def return_displacement_data(word, vectors, pattern):
    steps = [vectors[a] for a in word]
    p = prefix_sums(steps)
    occ = occurrence_positions(word, pattern)
    D = set()
    gaps = []
    for i, j in zip(occ, occ[1:]):
        gaps.append(j-i)
        D.add(tuple(p[j][k] - p[i][k] for k in range(3)))
    rank = Matrix(list(D)).rank() if D else 0
    return {
        "occurrences": occ,
        "max_gap": max(gaps) if gaps else None,
        "displacements": D,
        "number_of_steps": len(D),
        "rank": rank,
    }
```

The following exact check tests the direct digital-line obstruction. For rational test parameters it searches for \(r\) with both fractional parts in the outer thirds and verifies
\[
p_r+p_{3r}=2p_{2r}.
\]

```python
def frac(x):
    return x - (x.numerator // x.denominator)

def floor_fraction(x):
    return x.numerator // x.denominator

def outer_third(t):
    return t < Fraction(1, 3) or t >= Fraction(2, 3)

def digital_point(n, alpha, beta):
    return (
        n,
        floor_fraction(alpha*n),
        floor_fraction(beta*n),
    )

def find_digital_AP(alpha, beta, bound=100000):
    for r in range(1, bound+1):
        ta, tb = frac(alpha*r), frac(beta*r)
        if outer_third(ta) and outer_third(tb):
            p1 = digital_point(r, alpha, beta)
            p2 = digital_point(2*r, alpha, beta)
            p3 = digital_point(3*r, alpha, beta)
            assert all(p1[j] + p3[j] == 2*p2[j] for j in range(3))
            return r, p1, p2, p3
    return None
```

The most informative computational experiment for Route 3 is:

1. search long triple-free paths for small rank-three \(S\);
2. compute `max_slab_chain` for many primitive \(\ell\), widths \(B\), and gaps \(R\);
3. identify repeated factors in their step words;
4. compute the ranks and covolumes of their return-displacement lattices.

Persistent rank \(3\) with rapidly increasing covolume would directly support the diagnosed obstruction.

## Route Diagnosis

**Proved ledger**

- A finite coloring of indices has a piecewise-syndetic color class.
- No infinite bounded-step counterexample can lie in a finite union of affine planes.
- For fixed \(S,\ell,B,R\), visits to any translated rational slab of width \(B\) have uniformly bounded \(R\)-connected components in index space.
- No infinite bounded-step walk in a fixed-radius tube around any real affine line is triple-free; it contains a three-term arithmetic progression.
- A counterexample, if one exists, can be chosen uniformly recurrent.
- Every return-word renormalization of a uniformly recurrent counterexample has at least four effective step vectors and generates a rank-three subgroup.
- Return lattices along nested factors form a descending chain of full-rank sublattices.

**Plausible but unproved claims**

- Some nested return factor must eventually have rank-\(\leq2\) displacement lattice.
- Alternatively, persistent full-rank return lattices might force adjacent return blocks with parallel sums.
- A quantitative planar theorem combined with bounds on return-lattice covolumes might establish one of these claims.

These are currently unproved and appear comparable in difficulty to the original problem.

**Dead ends**

- A general bounded-step path need not have arbitrarily long fixed-width rational-slab subwalks; digital irrational lines already refute that structural assertion.
- Generic finite projections preserve noncollinearity only when projection coefficients depend on the path length. The resulting planar step set also changes with length, making the finite planar bound circular.
- Coloring modulo a large sublattice gives a renormalized counterexample, but the bounded-gap constant can grow arbitrarily faster than the modulus, so no norm contraction follows.
- Uniform recurrence alone does not imply periodicity or rank drop; aperiodic minimal subshifts can have arbitrarily complicated return-word systems.
- Digital or Beatty-line constructions are ruled out by Theorem 5.1 rather than furnishing counterexamples.

**Precise block**

Route 3 would be complete if one could prove that every sufficiently long fixed-\(S\) triple-free walk has either:

1. a bounded-gap segment in a fixed-width neighborhood of a proper affine subspace; or
2. a return-word renormalization of lower rank.

The first alternative is not forced by bounded steps, and the second is exactly where the argument stops: all return lattices may remain rank \(3\) while their indices grow without bound. A fresh attempt should focus on the geometry of these nested full-rank return lattices—especially whether rapidly growing covolume is compatible with bounded original steps, uniform recurrence, and the prohibition of parallel adjacent block sums.