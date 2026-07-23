STATUS: BLOCKED

## Result

The exact second multiplicity moment admits a useful geometric decomposition. If \(A(P)\) denotes pairs of equal-length edges sharing a vertex and \(D(P)\) denotes pairs of equal-length vertex-disjoint edges, then every desired configuration satisfies
\[
A(P)+D(P)=\binom n3.
\]
I prove explicit bounds on \(A(P)\), forcing
\[
D(P)=\frac{n^3}{6}+O(n^2);
\]
in particular \(D(P)\ge23\) for \(n=9\). I also prove that a four-point set contributes at most two equal opposite-edge pairs; contribution two occurs exactly for a noncyclic parallelogram. Higher multiplicity moments similarly force almost \(\binom n{k+1}\) matchings of \(k\) equal-length edges for every fixed \(k\). These are strong necessary conditions but do not yield nonexistence: arbitrarily large equal-length matchings are compatible with general position, and for every \(n\) there are abstract edge-colorings with class sizes \(1,\dots,n-1\) and monochromatic maximum degree at most \(2\). The route is blocked at the need for a genuinely metric, cross-color upper bound on \(D(P)\) of leading constant below \(1/6\); the elementary general-position bound has leading constant \(3/8\).

## Complete Argument

### 1. Adjacent and disjoint equal-edge pairs

For each distance \(r\), let \(G_r\) be the graph on \(P\) whose edges are the pairs at distance \(r\), and write
\[
m_r=|E(G_r)|,\qquad d_r(p)=\deg_{G_r}(p).
\]

Because four neighbors of \(p\) in \(G_r\) would be four points on the circle of radius \(r\) centered at \(p\),
\[
d_r(p)\le 3.
\]

Define
\[
A(P)=\sum_{r}\sum_{p\in P}\binom{d_r(p)}2.
\]
This is exactly the number of unordered pairs of equal-length edges sharing one endpoint.

Define
\[
D(P)=\#\bigl\{\{e,f\}:e,f\subset P,\ e\cap f=\varnothing,\ |e|=|f|\bigr\}.
\]

Any two distinct edges of a complete graph either share exactly one endpoint or are vertex-disjoint. Therefore
\[
\sum_r\binom{m_r}{2}=A(P)+D(P).
\]
Under the target spectrum \(m_r\in\{1,\dots,n-1\}\), each once,
\[
\sum_r\binom{m_r}{2}
=\sum_{i=1}^{n-1}\binom i2
=\binom n3.
\]
Hence:

\[
\boxed{A(P)+D(P)=\binom n3.}
\tag{1}
\]

Thus Route 2 reduces first to understanding how much of \(\binom n3\) can be supplied by isosceles triangles and how much must come from disjoint equal segments.

---

### 2. A lower bound for the adjacent contribution

Let \(G_i\) be the distance graph whose class has exactly \(i\) edges, and put
\[
t_i=\sum_{p\in P}\binom{\deg_{G_i}(p)}2.
\]
Thus \(A(P)=\sum_{i=1}^{n-1}t_i\).

For any graph \(G\) with \(m\) edges on \(n\) vertices,
\[
\binom d2\ge d-1
\]
for every positive integer \(d\). If \(v_+(G)\) is the number of nonisolated vertices, then
\[
\sum_v\binom{d(v)}2
\ge \sum_{d(v)>0}(d(v)-1)
=2m-v_+(G)
\ge 2m-n.
\]
The left side is nonnegative, so
\[
t_i\ge \max(0,2i-n).
\]
Summing gives
\[
A(P)\ge\sum_{i=1}^{n-1}\max(0,2i-n)
=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
\tag{2}
\]

Indeed, if \(n=2k\), the positive terms are \(2,4,\dots,2k-2\), whose sum is \(k(k-1)\). If \(n=2k+1\), they are \(1,3,\dots,2k-1\), whose sum is \(k^2\). Both values equal the right side of (2).

Consequently,
\[
D(P)\le
\binom n3-\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
\tag{3}
\]

This upper bound is far too large to be contradictory, but it records the minimum amount of isosceles structure forced purely by the large distance classes.

---

### 3. An upper bound for the adjacent contribution

Set \(N=n-1\), and define
\[
B=\#\{(p,r):d_r(p)=1\text{ or }2\}.
\]

For \(d\in\{0,1,2,3\}\),
\[
\binom d2=
\begin{cases}
d,&d=3,\\
d-1,&d=1,2,\\
0,&d=0.
\end{cases}
\]
Moreover,
\[
\sum_{p,r}d_r(p)=n(n-1)=nN,
\]
because each point has \(N\) incident edges in total. It follows that
\[
A(P)=nN-B.
\tag{4}
\]

We now give lower bounds for \(B\).

For a fixed point \(p\), the positive numbers \(d_r(p)\) form a partition of \(N\) into parts of size at most \(3\).

- If \(N\not\equiv0\pmod3\), at least one part has size \(1\) or \(2\). Thus \(B\ge n\).
- Let \(r_1\) be the unique distance occurring once. Its graph has one edge, so its two endpoints each have a part of size \(1\).
- If \(N\equiv2\pmod3\), either endpoint of this edge must have at least two parts of size \(1\) or \(2\): one size-\(1\) part followed only by size-\(3\) parts would give total congruent to \(1\), not \(2\), modulo \(3\). Hence in this case
  \[
  B\ge n+2.
  \tag{5}
  \]
- If \(N\equiv0\pmod3\), each endpoint of the unique edge must again have at least two bad parts, because one size-\(1\) part and otherwise size-\(3\) parts would sum to \(1\bmod3\). Thus \(B\ge4\).

There is also a bound obtained by looking separately at each color. The sum of degrees in \(G_i\) is \(2i\). If all its positive degrees were \(3\), then \(3\mid2i\), hence \(3\mid i\). Therefore every \(i\) not divisible by \(3\) contributes at least one pair \((p,r)\) counted by \(B\). Thus
\[
B\ge N-\left\lfloor\frac N3\right\rfloor.
\tag{6}
\]

Combining these observations, define
\[
\beta_N=
\begin{cases}
\max\!\left(4,\dfrac{2N}{3}\right),&N\equiv0\pmod3,\\[2mm]
N+1=n,&N\equiv1\pmod3,\\[1mm]
N+3=n+2,&N\equiv2\pmod3.
\end{cases}
\]
Then
\[
B\ge\beta_N,
\]
and therefore
\[
\boxed{A(P)\le n(n-1)-\beta_{n-1}.}
\tag{7}
\]

Combining (1), (2), and (7) gives the rigorous interval
\[
\boxed{
\max\!\left(
0,\binom n3-n(n-1)+\beta_{n-1}
\right)
\le D(P)\le
\binom n3-\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
}
\tag{8}
\]

For the first unresolved values, the bounds are:

\[
\begin{array}{c|c|c|c}
n&\binom n3&A(P)\text{ upper bound}&D(P)\text{ lower bound}\\ \hline
8&56&48&8\\
9&84&61&23\\
10&120&84&36\\
11&165&99&66\\
12&220&118&102
\end{array}
\]

In particular, any \(n=9\) example must contain at least \(23\) pairs of equal-length vertex-disjoint segments.

Asymptotically,
\[
D(P)\ge \binom n3-O(n^2)=\frac{n^3}{6}+O(n^2).
\tag{9}
\]

Thus almost all of the required second moment must come from disjoint equal segments, not isosceles triangles.

---

### 4. Equal opposite edges on four points

For a four-element set
\[
X=\{p_1,p_2,p_3,p_4\},
\]
let \(d(X)\) be the number of true equalities among
\[
|p_1p_2|=|p_3p_4|,\qquad
|p_1p_3|=|p_2p_4|,\qquad
|p_1p_4|=|p_2p_3|.
\]

Every pair of disjoint equal-length edges has a unique four-point endpoint set, so
\[
D(P)=\sum_{\substack{X\subset P\\|X|=4}}d(X).
\tag{10}
\]

#### Lemma 1: \(d(X)\le2\)

Suppose the first two equalities hold. Translate so that the midpoint of \(p_2p_3\) is the origin, and write
\[
p_2=-w,\qquad p_3=w,\qquad p_1=u,\qquad p_4=v.
\]
The two squared-distance equalities are
\[
|u+w|^2=|v-w|^2,\qquad
|u-w|^2=|v+w|^2.
\]
Adding and subtracting them gives
\[
|u|=|v|,\qquad (u+v)\cdot w=0.
\]

Choose orthonormal coordinates with \(w\) on the first coordinate axis. Write
\[
u=(\alpha,\beta).
\]
The projection condition and equality of norms imply
\[
v=(-\alpha,\beta)\quad\text{or}\quad v=(-\alpha,-\beta)=-u.
\]

In the first case, \(\beta\ne0\), since otherwise all four points would be collinear. The four points
\[
(\pm|w|,0),\qquad (\pm\alpha,\beta)
\]
lie on the circle centered at
\[
\left(0,\frac{\alpha^2+\beta^2-|w|^2}{2\beta}\right).
\]
This contradicts the no-four-concyclic condition.

Thus necessarily \(v=-u\). Hence the four points are centrally symmetric:
\[
p_1+p_4=p_2+p_3.
\]

If the third opposite-edge equality also held, it would become
\[
|u-(-u)|=|(-w)-w|,
\]
so \(|u|=|w|\). Then all four points would lie on the circle centered at the origin with radius \(|u|\), again forbidden. Therefore all three equalities cannot hold, proving
\[
\boxed{d(X)\le2.}
\tag{11}
\]

The same argument gives the stronger characterization:

\[
\boxed{
d(X)=2
\iff
X\text{ is a centrally symmetric, noncyclic four-point set}.
}
\tag{12}
\]

Geometrically, these are nonrectangular parallelograms, with the remaining pairing being their diagonals.

---

### 5. Counting the \(d(X)=2\) quadruples by midpoints

Let \(N_2\) be the number of four-subsets \(X\) with \(d(X)=2\). For each point \(z\in\mathbb R^2\), let
\[
k_z=\#\left\{\{p,q\}\subset P:\frac{p+q}{2}=z\right\}.
\]

Two distinct pairs having the same midpoint are automatically disjoint. Their four endpoints form a centrally symmetric set. By no four concyclic, this set is noncyclic, so by (12) it has \(d(X)=2\). Conversely, every \(d(X)=2\) set has a unique pairing into diagonals with a common midpoint. Therefore
\[
\boxed{N_2=\sum_z\binom{k_z}{2}.}
\tag{13}
\]

Since the pairs counted by a fixed \(k_z\) are disjoint,
\[
k_z\le \left\lfloor\frac n2\right\rfloor=:K.
\]
Also
\[
\sum_z k_z=\binom n2.
\]
Using
\[
\binom{k_z}{2}\le \frac{K-1}{2}k_z
\]
gives
\[
N_2\le
\frac{K-1}{2}\binom n2.
\tag{14}
\]
Explicitly,
\[
N_2\le
\begin{cases}
\dfrac{n(n-1)(n-2)}8,&n\text{ even},\\[2mm]
\dfrac{n(n-1)(n-3)}8,&n\text{ odd}.
\end{cases}
\tag{15}
\]

If \(N_1\) denotes the number of four-subsets with \(d(X)=1\), then
\[
D(P)=N_1+2N_2.
\tag{16}
\]

Unfortunately, (15) is still large enough that it does not conflict with the forced lower bound (9).

---

### 6. What the higher moments force

For a graph \(G\), let \(M_k(G)\) denote its number of \(k\)-edge matchings. Let
\[
\mathcal M_k(P)=\sum_r M_k(G_r).
\]

A nonmatching \(k\)-edge subset contains a pair of adjacent edges. If
\[
t(G)=\sum_v\binom{d(v)}2,
\]
then the number of nonmatching \(k\)-subsets of \(E(G)\) is at most
\[
t(G)\binom{|E(G)|-2}{k-2}.
\]
Since every \(G_r\) has maximum degree at most \(3\),
\[
t(G_r)\le\sum_v d_r(v)=2m_r.
\]
Therefore, for a color class of size \(i\),
\[
M_k(G_i)\ge
\binom ik-2i\binom{i-2}{k-2}.
\]
Summing and using the target moment identity gives
\[
\mathcal M_k(P)
\ge
\binom n{k+1}
-2\sum_{i=1}^{n-1}i\binom{i-2}{k-2}.
\tag{17}
\]

The remaining sum has the exact evaluation
\[
\sum_{i=1}^{n-1}i\binom{i-2}{k-2}
=
k\binom{n-2}{k-1}
+(k-1)\binom{n-2}{k}.
\]
Hence
\[
\boxed{
\mathcal M_k(P)\ge
\binom n{k+1}
-2k\binom{n-2}{k-1}
-2(k-1)\binom{n-2}{k}.
}
\tag{18}
\]

For fixed \(k\),
\[
\mathcal M_k(P)
\ge \binom n{k+1}-O_k(n^k).
\tag{19}
\]

For example,
\[
\mathcal M_3(P)\ge
\binom n4
-6\binom{n-2}{2}
-4\binom{n-2}{3}.
\tag{20}
\]

Thus, for every fixed \(k\), almost the entire \(k\)-th moment must asymptotically come from \(k\) pairwise vertex-disjoint equal-length segments.

This does not by itself create a forbidden local configuration.

#### Lemma 2: Arbitrarily large equal-length matchings are compatible with general position

For every \(k\), there exist \(2k\) points in the plane satisfying:

1. no three are collinear;
2. no four are concyclic;
3. their unit-distance graph is exactly a matching of size \(k\).

To prove this, parameterize the \(j\)-th prescribed unit segment by
\[
p_j^\pm=c_j\pm\frac12(\cos\theta_j,\sin\theta_j),
\]
where \(c_j\in\mathbb R^2\) and \(\theta_j\in S^1\).

On the parameter space \((\mathbb R^2\times S^1)^k\), each unwanted condition is the zero set of a real-analytic function:

- equality of two points;
- a collinearity determinant;
- a concyclicity determinant;
- a cross-segment squared distance minus \(1\).

None of these functions is identically zero. For example, segment centers can first be placed very far apart to avoid all unwanted unit distances; a point can be moved away from any prescribed line or circle; and two translated parallel unit segments need not form a cyclic quadrilateral when the translation has nonzero component along the segment direction.

A nonzero real-analytic function has zero set with empty interior. A finite union of such sets cannot cover the parameter space. Therefore a choice avoiding every unwanted condition exists.

Hence the abundance of equal-edge matchings forced by (18) is not locally contradictory. A solution would need to exploit how the many matchings from different distance classes interact.

---

### 7. Abstract colorings show that moment and degree constraints alone are insufficient

#### Lemma 3

For every \(n\ge2\), the edges of \(K_n\) can be partitioned into classes
\[
C_1,\dots,C_{n-1}
\]
such that
\[
|C_i|=i
\]
and every monochromatic graph has maximum degree at most \(2\).

##### Odd \(n=2k+1\)

Use the standard Walecki decomposition of \(K_{2k+1}\) into \(k\) Hamilton cycles. With vertices
\[
\{\infty\}\cup\mathbb Z_{2k},
\]
one explicit cycle is
\[
\infty,\ j,\ j-1,\ j+1,\ j-2,\ j+2,\ldots,
j-(k-1),j+(k-1),j-k,\ \infty
\]
for \(j=0,\dots,k-1\), with arithmetic modulo \(2k\).

The infinity edges are partitioned because cycle \(j\) contains the edges from \(\infty\) to \(j\) and \(j-k\). The finite edges in cycle \(j\) have endpoint sum \(2j-1\) or \(2j\) modulo \(2k\). Each finite edge has exactly one such endpoint sum and hence lies in exactly one cycle. Thus these cycles partition \(E(K_n)\).

For \(i=1,\dots,k\), split the \(i\)-th Hamilton cycle into arbitrary sets of \(i\) and \(n-i\) edges, and label these sets \(C_i\) and \(C_{n-i}\). Every class is a subgraph of a cycle, so its maximum degree is at most \(2\).

##### Even \(n=2k\)

Use a one-factorization of \(K_{2k}\). With vertices
\[
\{\infty\}\cup\mathbb Z_{2k-1},
\]
define
\[
F_j=
\{\{\infty,j\}\}
\cup
\bigl\{\{j+t,j-t\}:1\le t\le k-1\bigr\},
\]
for \(j\in\mathbb Z_{2k-1}\).

Each \(F_j\) is a perfect matching. An edge \(\{a,b\}\) between finite vertices lies in the unique factor with
\[
j=\frac{a+b}{2}\pmod{2k-1},
\]
so the \(F_j\) partition \(E(K_n)\).

For each \(i=1,\dots,k-1\), take two unused factors. Their union has \(2k=n\) edges and maximum degree \(2\). Split that union into arbitrary sets of \(i\) and \(n-i\) edges and label them \(C_i,C_{n-i}\). Label the final unused factor \(C_k\).

This proves the lemma.

These abstract colorings satisfy:

- the exact multiplicity spectrum;
- all multiplicity moment identities;
- monochromatic maximum degree at most \(2\), stronger than the geometric bound \(3\);
- no monochromatic \(K_{2,3}\).

They are not claimed to be Euclidean realizations and may violate the four-point opposite-edge condition. Nevertheless, they prove that the moments together with the elementary graph restrictions cannot settle the problem.

---

### 8. Precise point at which Route 2 is blocked

For an arbitrary general-position set, let
\[
Q(P)=\sum_r\binom{m_r}{2}.
\]
The degree bound gives
\[
m_r\le L:=\left\lfloor\frac{3n}{2}\right\rfloor.
\]
Since \(\sum_r m_r=\binom n2\),
\[
Q(P)
\le
\frac{L-1}{2}\sum_r m_r
=
\frac{L-1}{2}\binom n2
=
\left(\frac38+o(1)\right)n^3.
\tag{21}
\]

Because \(D(P)\le Q(P)\), this gives only
\[
D(P)\le \left(\frac38+o(1)\right)n^3.
\]
But a target configuration requires
\[
D(P)\ge\left(\frac16+o(1)\right)n^3.
\]
The constants therefore do not contradict one another.

A sufficient new theorem for Route 2 would be, for example,
\[
D(P)<
\binom n3-n(n-1)+\beta_{n-1}
\tag{22}
\]
for all sufficiently large \(n\). Its leading term would need to be strictly below \(n^3/6\). I have no proof of such a theorem. Equal disjoint segments are not controlled directly by either no-three-collinear or no-four-concyclic, and the four-point estimate \(d(X)\le2\) sums only to \(O(n^4)\).

Thus the route has reduced the problem to a new equal-segment energy bound of essentially the same difficulty as the original asymptotic obstruction.

## Self-Audit

1. **The four-point classification is the most geometry-sensitive lemma.**  
   A labeling mistake could invalidate the parallelogram conclusion. I believe it is sound because the proof fixes two specific opposite-edge equalities, derives the exhaustive alternatives \(v=-u\) or \(v=(-\alpha,\beta)\), and explicitly shows the latter is cyclic. The third equality then makes the central case cyclic as well.

2. **The upper bound for \(A(P)\) combines row-wise and color-wise congruence arguments.**  
   There is a risk of incorrectly adding overlapping lower bounds for \(B\). I avoided that: in the \(N\equiv0\) case I take a maximum, not a sum; in the \(N\equiv2\) case the extra two contributions come specifically from the two distinct endpoints of the unique edge, over the baseline contribution at every vertex.

3. **The generic construction of an equal-length matching uses an open-dense argument rather than explicit coordinates.**  
   Such arguments fail if a forbidden determinant vanishes identically on the constrained parameter space. Here each possible degeneracy is demonstrably nonidentity: centers may be separated to avoid cross-unit distances, points can be moved off prescribed lines and circles, and two unit segments are not necessarily cyclic. The finite-union real-analytic argument is therefore applicable.

The decisive missing point is not hidden: no upper bound of the needed strength for \(D(P)\) has been proved, so this is not a solution of the classification problem.

## Computations To Verify

The following pure Python constructs and checks the abstract colorings from Lemma 3.

```python
from itertools import combinations
from collections import defaultdict
from math import comb

def E(a, b):
    return tuple(sorted((a, b)))

def one_factorization_even(n):
    # n = 2k, vertices 0,...,2k-2 and infinity=2k-1
    assert n % 2 == 0
    k = n // 2
    m = 2*k - 1
    inf = m
    factors = []
    for j in range(m):
        F = {E(inf, j)}
        for t in range(1, k):
            F.add(E((j+t) % m, (j-t) % m))
        factors.append(F)
    return factors

def walecki_cycles_odd(n):
    # n = 2k+1, vertices 0,...,2k-1 and infinity=2k
    assert n % 2 == 1
    k = (n-1)//2
    m = 2*k
    inf = m
    cycles = []
    for j in range(k):
        seq = [inf, j]
        for t in range(1, k):
            seq += [(j-t) % m, (j+t) % m]
        seq += [(j-k) % m]
        edges = [E(seq[t], seq[(t+1) % len(seq)])
                 for t in range(len(seq))]
        assert len(edges) == n
        cycles.append(edges)
    return cycles

def abstract_coloring(n):
    colors = {}
    if n % 2 == 1:
        k = (n-1)//2
        cycles = walecki_cycles_odd(n)
        for i in range(1, k+1):
            C = cycles[i-1]
            colors[i] = set(C[:i])
            colors[n-i] = set(C[i:])
    else:
        k = n//2
        factors = one_factorization_even(n)
        ptr = 0
        for i in range(1, k):
            U = list(factors[ptr] | factors[ptr+1])
            ptr += 2
            assert len(U) == n
            colors[i] = set(U[:i])
            colors[n-i] = set(U[i:])
        colors[k] = set(factors[ptr])
    return colors

def verify_abstract(n):
    colors = abstract_coloring(n)
    all_edges = {E(a,b) for a,b in combinations(range(n), 2)}

    seen = set()
    for i in range(1, n):
        assert len(colors[i]) == i
        assert seen.isdisjoint(colors[i])
        seen |= colors[i]

        deg = [0]*n
        for a,b in colors[i]:
            deg[a] += 1
            deg[b] += 1
        assert max(deg) <= 2

    assert seen == all_edges

    # Moment check
    for k in range(1, n):
        lhs = sum(comb(i, k) for i in range(1, n))
        rhs = comb(n, k+1)
        assert lhs == rhs

    # Adjacent/disjoint second-moment decomposition
    A = 0
    for i in range(1, n):
        deg = [0]*n
        for a,b in colors[i]:
            deg[a] += 1
            deg[b] += 1
        A += sum(comb(d, 2) for d in deg)

    D = sum(comb(i, 2) for i in range(1, n)) - A
    assert A + D == comb(n, 3)
    return A, D

for n in range(2, 31):
    print(n, verify_abstract(n))
```

This checks the forced \(D\)-interval:

```python
def beta(N):
    if N % 3 == 0:
        return max(4, 2*N//3)
    if N % 3 == 1:
        return N + 1
    return N + 3

def forced_D_interval(n):
    N = n - 1
    Q = comb(n, 3)
    A_min = (N*N)//4
    A_max = n*N - beta(N)
    return max(0, Q-A_max), Q-A_min

for n in range(8, 21):
    print(n, forced_D_interval(n))
```

An exact checker for the supplied \(n=4\) configuration:

```python
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
import sympy as sp

P = [
    (F(-1), F(0)),
    (F(1),  F(0)),
    (F(0),  F(2)),
    (F(0),  F(3,4)),
]

def dsq(p, q):
    return (p[0]-q[0])**2 + (p[1]-q[1])**2

dist = Counter(dsq(P[i], P[j]) for i,j in combinations(range(4), 2))
assert sorted(dist.values()) == [1,2,3]

for I in combinations(range(4), 3):
    M = sp.Matrix([[sp.Rational(P[i][0].numerator, P[i][0].denominator),
                    sp.Rational(P[i][1].numerator, P[i][1].denominator), 1]
                   for i in I])
    assert M.det() != 0

for I in combinations(range(4), 4):
    rows = []
    for i in I:
        x = sp.Rational(P[i][0].numerator, P[i][0].denominator)
        y = sp.Rational(P[i][1].numerator, P[i][1].denominator)
        rows.append([x*x+y*y, x, y, 1])
    assert sp.Matrix(rows).det() != 0
```

For \(n=9\), the following CP-SAT model should test whether the purely combinatorial necessary conditions—including \(d(X)\le2\)—are jointly feasible:

```python
from ortools.sat.python import cp_model
from itertools import combinations

def edge(a,b):
    return tuple(sorted((a,b)))

def necessary_coloring_model(n, optimize_A=False):
    V = range(n)
    E = list(combinations(V, 2))
    C = range(1, n)

    model = cp_model.CpModel()
    x = {(e,c): model.NewBoolVar(f"x_{e[0]}_{e[1]}_{c}")
         for e in E for c in C}

    # Every edge has exactly one color.
    for e in E:
        model.Add(sum(x[e,c] for c in C) == 1)

    # Color c has exactly c edges.
    for c in C:
        model.Add(sum(x[e,c] for e in E) == c)

    # Geometric degree bound.
    for v in V:
        for c in C:
            model.Add(sum(x[edge(v,w),c] for w in V if w != v) <= 3)

    # No monochromatic K_{2,3}.
    for u,v in combinations(V, 2):
        rest = [w for w in V if w not in (u,v)]
        for T in combinations(rest, 3):
            for c in C:
                model.Add(sum(x[edge(z,w),c]
                              for z in (u,v) for w in T) <= 5)

    # For each quadruple, at most two opposite pairings are equal.
    for a,b,c,d in combinations(V, 4):
        pairings = [
            (edge(a,b), edge(c,d)),
            (edge(a,c), edge(b,d)),
            (edge(a,d), edge(b,c)),
        ]
        same = []
        for idx,(e,f) in enumerate(pairings):
            zlist = []
            for col in C:
                z = model.NewBoolVar(
                    f"opp_{a}_{b}_{c}_{d}_{idx}_{col}")
                model.Add(z <= x[e,col])
                model.Add(z <= x[f,col])
                model.Add(z >= x[e,col] + x[f,col] - 1)
                zlist.append(z)
            y = model.NewBoolVar(f"same_{a}_{b}_{c}_{d}_{idx}")
            model.Add(y == sum(zlist))
            same.append(y)
        model.Add(sum(same) <= 2)

    if optimize_A:
        wedges = []
        for v in V:
            nbrs = [w for w in V if w != v]
            for a,b in combinations(nbrs, 2):
                e, f = edge(v,a), edge(v,b)
                for c in C:
                    y = model.NewBoolVar(f"w_{v}_{a}_{b}_{c}")
                    model.Add(y <= x[e,c])
                    model.Add(y <= x[f,c])
                    model.Add(y >= x[e,c] + x[f,c] - 1)
                    wedges.append(y)
        model.Maximize(sum(wedges))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 3600
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    return solver.StatusName(status), solver.ObjectiveValue()

print(necessary_coloring_model(9, optimize_A=True))
```

A feasible result would not imply Euclidean realizability. Infeasibility would prove \(n=9\) impossible, because every Euclidean realization satisfies all encoded constraints.

## Route Diagnosis

**Proved ledger**

- \(A(P)+D(P)=\binom n3\).
- \(\lfloor(n-1)^2/4\rfloor\le A(P)\le n(n-1)-\beta_{n-1}\).
- Any \(n=9\) example must have at least \(23\) disjoint equal-segment pairs.
- A four-set has at most two equal opposite-edge pairings.
- Two such pairings characterize a noncyclic parallelogram.
- The number of these parallelograms is exactly \(\sum_z\binom{k_z}{2}\).
- For fixed \(k\), the higher moments force \(\binom n{k+1}-O_k(n^k)\) equal-length \(k\)-matchings.
- Arbitrarily large equal-length matchings can occur in general position.
- Abstract colorings satisfying the spectrum and monochromatic maximum degree \(2\) exist for every \(n\).

**Plausible but unproved**

- A sufficiently strong upper bound on \(D(P)\) may follow from interactions among many different equal-length matchings, rather than from any one distance graph.
- Four-point midpoint structure may help if combined with restrictions on the \(d(X)=1\) quadruples.
- For \(n=9\), adding all known small unit-distance forbidden graphs to the SAT model may reduce the candidate colorings substantially.

**Dead ends**

- Bounding isosceles triangles alone loses an entire power of \(n\): \(A(P)=O(n^2)\), while the required second moment is \(\Theta(n^3)\).
- The local bound \(d(X)\le2\) gives only \(D(P)\le2\binom n4=O(n^4)\).
- Higher moments mostly force large matchings, but such matchings are individually compatible with general position.
- Multiplicity moments plus degree and \(K_{2,3}\) constraints are insufficient, as shown by the all-\(n\) abstract coloring construction.

**Precise block**

Route 2 now requires a new theorem controlling the number of disjoint equal-length segment pairs across all distances, with leading constant below \(1/6\). The available elementary estimate has leading constant \(3/8\). Proving the needed improvement appears to demand metric consistency across different colors and is comparable in difficulty to the original problem.

A fresh attempt should combine the forced \(D(P)\)-density with Euclidean distance-matrix rank or rigidity. For the finite frontier \(n=9\), the most concrete next step is SAT enumeration with \(d(X)\le2\), followed by exact rank/realizability tests for the surviving colorings.