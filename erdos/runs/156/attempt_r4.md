STATUS: BLOCKED

## Result

Route 4 does not presently yield a complete solution. I proved that the obvious Cartesian/mixed-radix product is intrinsically non-Sidon, and that the natural repair by an auxiliary checksum cannot support an optimal no-carry digitwise covering: an extreme-digit argument forces too many representations in the outer gadget. I then developed a more promising non-Cartesian composition using families of Golomb rulers with pairwise disjoint difference sets. Such families exist explicitly at the correct cubic scale via a finite-field construction. This completely resolves the Sidonicity part of a balanced composition, but the remaining exact-coverage requirement becomes a highly structured design problem of essentially the original strength. Carries can partially remove the extreme-digit obstruction, and I give the exact carry equations, but I cannot construct gadgets satisfying them uniformly.

## Complete Argument

All intervals below are temporarily zero-based. Translation by \(1\) converts a construction in \(\{0,\dots,N-1\}\) to one in \([N]\).

### 1. Plain Cartesian composition is impossible

Let \(X,Y\) be sets with \(|X|,|Y|\ge 2\). The Cartesian product
\[
X\times Y
\]
is not Sidon in the product group.

Indeed, choose distinct \(x_1,x_2\in X\) and distinct \(y_1,y_2\in Y\). Then
\[
(x_1,y_1)+(x_2,y_2)
=
(x_1,y_2)+(x_2,y_1),
\]
and the two unordered pairs are different.

Consequently, any additive or no-carry mixed-radix encoding of the full Cartesian product also fails. In particular, sets of the form
\[
\{Ma+b:a\in A,\ b\in B\}
\]
are never Sidon when \(|A|,|B|\ge2\), regardless of how large \(M\) is.

This is not a carry issue: the displayed rectangle is already an exact integer equality.

---

### 2. Exact characterization of the checksum repair

A standard proposed repair is to append a checksum.

Let \(X,Y\) be Sidon subsets of abelian groups and let
\[
\chi:X\times Y\longrightarrow K
\]
take values in another abelian group. Define
\[
\Gamma_\chi:=\{(x,y,\chi(x,y)):x\in X,\ y\in Y\}.
\]

#### Lemma 2.1: Rectangle criterion

The set \(\Gamma_\chi\) is Sidon if and only if, for every \(x\ne x'\) and \(y\ne y'\),
\[
\chi(x,y)+\chi(x',y')
\ne
\chi(x,y')+\chi(x',y).
\tag{2.1}
\]

#### Proof

Suppose two unordered pairs of points of \(\Gamma_\chi\) have the same sum. Equality of the first coordinates and the Sidonicity of \(X\) imply that the multisets of first coordinates agree. The same is true of the second coordinates by the Sidonicity of \(Y\).

If either coordinate is repeated, or if the two coordinate pairings agree, the two pairs of graph points are identical as multisets. The only possible nontrivial equality is therefore the crossed pairing
\[
(x,y),(x',y')
\quad\text{versus}\quad
(x,y'),(x',y),
\]
and the third-coordinate equality is exactly the negation of (2.1). ∎

#### Lemma 2.2: A checksum needs an unbounded alphabet

If \(\chi\) is integer-valued and
\[
0\le \chi(x,y)\le R,
\]
then
\[
2R+1\ge \max\{|X|,|Y|\}.
\tag{2.2}
\]

#### Proof

Fix distinct \(x,x'\). By (2.1), the integers
\[
\chi(x,y)-\chi(x',y),\qquad y\in Y,
\]
are pairwise distinct. They all lie in \([-R,R]\), which contains \(2R+1\) integers. Hence \(|Y|\le2R+1\). Interchanging \(X,Y\) gives the other inequality. ∎

The bound is qualitatively sharp: over a prime field, the checksum
\[
\chi(i,j)=ij
\]
has nonzero alternating rectangle difference
\[
(i-i')(j-j').
\]
However, the extra checksum digit creates a serious coverage obstruction.

---

### 3. A rigorous no-carry lifting lemma

The following gives a clean way to transfer a vector gadget to a genuine interval.

Let
\[
D=\prod_{j=1}^d\{0,\dots,M_j\}
\]
and define radices and weights by
\[
R_j=2M_j+1,\qquad
W_1=1,\qquad
W_j=\prod_{\ell<j}R_\ell.
\]
For \(v=(v_1,\dots,v_d)\), put
\[
E(v)=\sum_{j=1}^d v_jW_j,
\qquad
P=\prod_{j=1}^d R_j.
\]

#### Lemma 3.1: No-carry interval lift

Suppose \(C\subseteq D\) satisfies:

1. \(C\) is Sidon under coordinatewise addition;
2. every
   \[
   t\in D^*:=\prod_{j=1}^d\{0,\dots,2M_j\}
   \]
   satisfies either
   \[
   t+p=q+r
   \tag{3.1}
   \]
   coordinatewise for some \(p,q,r\in C\), or
   \[
   2t=q+r
   \tag{3.2}
   \]
   coordinatewise for some \(q,r\in C\).

Then
\[
A:=\{E(c)+1:c\in C\}
\]
is a maximal Sidon set in \([P]\).

#### Proof

Each coordinate sum of two elements of \(C\) lies in
\[
\{0,\dots,2M_j\}=\{0,\dots,R_j-1\}.
\]
Thus pair sums have carry-free base-\((R_1,\dots,R_d)\) expansions. Therefore
\[
E(c_1)+E(c_2)=E(c_3)+E(c_4)
\]
implies
\[
c_1+c_2=c_3+c_4
\]
coordinatewise. Vector Sidonicity makes the integer equality trivial.

Every integer in \(\{0,\dots,P-1\}\) has a unique expansion \(E(t)\) with \(t\in D^*\). If (3.1) holds, then
\[
(E(t)+1)+(E(p)+1)
=
(E(q)+1)+(E(r)+1).
\]
If (3.2) holds, then
\[
2(E(t)+1)=(E(q)+1)+(E(r)+1).
\]
Thus every point of \([P]\) is blocked. ∎

This lemma shows exactly what an ideal no-carry digit construction would need. Unfortunately, the checksum graph cannot satisfy its full-box hypothesis efficiently.

---

### 4. Extreme-digit obstruction for checksum products

Let \(A\) be an \(m\)-element outer set, let \(B\subseteq[0,M]\) have \(n\) elements, and let
\[
0\le \chi(a,b)\le R.
\]
Consider the graph
\[
C=\{(a,b,\chi(a,b)):a\in A,\ b\in B\}.
\]

For an integer \(x\), let
\[
\rho_A(x)
=
\#\{(a_0,\{a_1,a_2\}):x+a_0=a_1+a_2,\ a_i\in A\},
\]
where the summand pair is unordered.

#### Lemma 4.1: Corner-fiber obstruction

Suppose the vector blocker of \(C\) covers
\[
T\times\{2M\}\times\{0,\dots,2R\}
\]
for some set \(T\) of outer targets and \(M>0\). Then
\[
\rho_A(x)\ge 2R+1
\qquad\text{for every }x\in T.
\tag{4.1}
\]

#### Proof

Fix \(x\in T\) and \(h\in\{0,\dots,2R\}\). A triple obstruction for \((x,2M,h)\) has second-coordinate equation
\[
2M+b_0=b_1+b_2,
\qquad b_i\in B\subseteq[0,M].
\]
Since the right side is at most \(2M\), necessarily
\[
b_0=0,\qquad b_1=b_2=M.
\]
If either endpoint is absent from \(B\), the point cannot be covered at all.

For a fixed outer representation
\[
x+a_0=a_1+a_2,
\]
the checksum target is then forced to be
\[
h=\chi(a_1,M)+\chi(a_2,M)-\chi(a_0,0).
\]
Thus one outer representation supplies at most one value of \(h\).

A midpoint obstruction is impossible because it would require
\[
4M=b_1+b_2\le2M.
\]
Hence all \(2R+1\) checksum targets require at least \(2R+1\) outer representations. ∎

Summing over \(x\in T\), there are at most
\[
m\binom{m+1}{2}=\frac{m^2(m+1)}2
\]
formal outer triples. Therefore
\[
|T|(2R+1)\le \frac{m^2(m+1)}2.
\tag{4.2}
\]
If the graph is Sidon, Lemma 2.2 gives \(2R+1\ge n\), and hence
\[
|T|\,n\le \frac{m^2(m+1)}2.
\tag{4.3}
\]

In a balanced composition \(m\asymp n\to\infty\), an efficient outer gadget should have \(|T|\asymp m^3\). Inequality (4.3) would instead require
\[
m^3n\ll m^3,
\]
which is impossible for unbounded \(n\).

Thus:

> A full Cartesian product repaired by an independent checksum cannot simultaneously have optimal cubic outer coverage and support the full no-carry box lift of Lemma 3.1.

This rules out the most direct implementation of Route 4. It does not rule out constructions that deliberately use carries or replace the identical inner copy by row-dependent gadgets.

---

### 5. Row-dependent gadgets: the pairing problem can be solved

Let \(A\) be Sidon. For each \(a\in A\), choose a set \(B_a\subseteq\mathbb Z\), and define
\[
C=\{(a,b):a\in A,\ b\in B_a\}.
\]

#### Lemma 5.1: Exact Sidonicity criterion

The set \(C\) is Sidon under coordinatewise addition if and only if:

1. every \(B_a\) is Sidon;
2. for distinct \(a,a'\),
   \[
   (B_a-B_a)\cap(B_{a'}-B_{a'})=\{0\}.
   \tag{5.1}
   \]

#### Proof

Suppose
\[
(a,b)+(a',b')=(c,d)+(c',d').
\]
Since \(A\) is Sidon,
\[
\{a,a'\}=\{c,c'\}.
\]

If \(a=a'\), all four low coordinates lie in the same \(B_a\), and the assertion follows from the Sidonicity of \(B_a\).

If \(a\ne a'\), reorder the right side so that \(c=a,c'=a'\). Then
\[
b+b'=d+d',
\]
and therefore
\[
b-d=d'-b'.
\]
The left side belongs to \(B_a-B_a\), and the right side belongs to \(B_{a'}-B_{a'}\). Condition (5.1) forces both to vanish.

Conversely, a nonzero common difference in (5.1) directly supplies a crossed pair-sum collision. ∎

If every \(B_a\) has \(n\) elements and lies in \([0,M]\), then all positive differences occurring inside all rows are distinct. Hence
\[
|A|\binom n2\le M.
\tag{5.2}
\]
For \(m=|A|\asymp n\), the optimal possible scale is therefore
\[
M\asymp mn^2\asymp n^3.
\]
This is exactly the scale needed for a balanced cubic composition.

---

### 6. Explicit optimal-order disjoint-difference families

The Sidonicity requirement in Lemma 5.1 can be met at the correct order.

Let \(q\) be an odd prime. For \(i,t\in\mathbb F_q\), define
\[
v_i(t)=(t,t^2,it)\in\mathbb F_q^3.
\]

#### Lemma 6.1: All directed nonzero row differences are distinct

If \(s\ne t\), then the map
\[
(i,s,t)\longmapsto v_i(s)-v_i(t)
\]
is injective.

#### Proof

Suppose
\[
v_i(s)-v_i(t)=v_j(u)-v_j(v).
\]
The first coordinate gives
\[
d:=s-t=u-v\ne0.
\]
The second coordinate gives
\[
d(s+t)=d(u+v),
\]
so \(s+t=u+v\). Since \(q\) is odd, the sum and difference determine the ordered pair, and therefore
\[
s=u,\qquad t=v.
\]
The third coordinate now gives
\[
id=jd,
\]
so \(i=j\). ∎

To obtain integer rulers, set
\[
R=2q-1
\]
and encode
\[
E(x,y,z)=x+Ry+R^2z
\]
using representatives in \(\{0,\dots,q-1\}\). Put
\[
B_i=\{E(t,t^2,it):t\in\mathbb F_q\}.
\]

If two integer directed differences from these rows agree, subtracting their coordinate differences gives coefficients of absolute value at most \(2q-2<R\). Reduction successively modulo \(R\) therefore shows that the three coordinate differences agree as integers, hence modulo \(q\). Lemma 6.1 then identifies the directed differences.

Thus the \(q\) sets \(B_i\) are \(q\)-mark Golomb rulers with pairwise disjoint nonzero difference sets. Moreover,
\[
B_i\subseteq[0,M_q],
\]
where
\[
M_q\le(q-1)(1+R+R^2)<4q^3.
\tag{6.1}
\]

This is within a constant factor of the lower bound
\[
q\binom q2\sim\frac{q^3}{2}.
\]

Therefore the coordinate-pairing/Sidonicity component of a balanced composition has an explicit optimal-order solution.

---

### 7. The exact remaining coverage condition

For the row construction,
\[
(x,y)\in C+C-C
\]
holds exactly when there are \(a_0,a_1,a_2\in A\) such that
\[
x+a_0=a_1+a_2
\]
and
\[
y\in B_{a_1}+B_{a_2}-B_{a_0}.
\tag{7.1}
\]
Likewise, a midpoint obstruction requires
\[
2x=a_1+a_2,\qquad
2y\in B_{a_1}+B_{a_2}.
\tag{7.2}
\]

Thus a successful row-family composition needs two simultaneous properties:

1. all within-row difference sets are disjoint, to guarantee Sidonicity;
2. the cross-row triple sets in (7.1), distributed according to outer representations of \(x\), cover every low digit.

The first property has been solved above. I do not know how to obtain the second without logarithmic waste.

---

### 8. A finite-field diagnostic: each natural row triple covers only half

For the finite-field rows \(v_i(t)=(t,t^2,it)\), fix three pairwise distinct row indices \(i_0,i_1,i_2\). The image of a low-coordinate triple is
\[
(r,s,t)\longmapsto
\left(
s+t-r,\,
s^2+t^2-r^2,\,
i_1s+i_2t-i_0r
\right).
\tag{8.1}
\]

#### Lemma 8.1

The image of (8.1) has cardinality
\[
q^2\frac{q+1}{2}.
\]

#### Proof

Fix the first and third outputs \(u,w\). Since \(i_1\ne i_2\), the equations
\[
s+t-r=u,
\qquad
i_1s+i_2t-i_0r=w
\]
express \(s,t\) as affine functions of \(r\):
\[
s=\alpha+\beta r,\qquad
t=u-\alpha+(1-\beta)r,
\]
where
\[
\beta=\frac{i_0-i_2}{i_1-i_2}.
\]
Because the three row indices are distinct,
\[
\beta\ne0,1.
\]
The second output becomes a quadratic polynomial in \(r\), whose quadratic coefficient is
\[
\beta^2+(1-\beta)^2-1=-2\beta(1-\beta)\ne0.
\]
A nonconstant quadratic over an odd finite field takes exactly \((q+1)/2\) distinct values. There are \(q^2\) choices of \((u,w)\), giving the stated image size. ∎

Thus one natural row triple covers approximately half the low-coordinate group. A constant number of specially coordinated outer representations might conceivably cover everything, but generic choices are expected to leave common quadratic-character holes. Proving that constant coverage is impossible would require a classification of the associated discriminant quadratic forms; I have not proved such a classification.

---

### 9. Carries remove the simplest boundary obstruction

The no-carry full-box condition is too rigid, but ordinary base expansion permits one controlled carry.

Let all \(B_a\subseteq[0,M]\) and put
\[
S=2M+1.
\]
Encode
\[
(a,b)\longmapsto Sa+b.
\tag{9.1}
\]

By Lemma 5.1, the encoded set is Sidon. Indeed, an equal pair sum gives
\[
S(a_1+a_2-a_3-a_4)
=
-(b_1+b_2-b_3-b_4),
\]
and the right side has absolute value at most \(2M<S\). Hence both sides vanish.

Now write a target integer as
\[
n=Sx+y,\qquad 0\le y<S.
\]
For a triple witness, set
\[
d=b_1+b_2-b_0\in[-M,2M].
\]
Then
\[
n+(Sa_0+b_0)=(Sa_1+b_1)+(Sa_2+b_2)
\]
is equivalent to exactly one of
\[
\begin{cases}
x+a_0=a_1+a_2,\\
d=y,
\end{cases}
\tag{9.2}
\]
or
\[
\begin{cases}
x+1+a_0=a_1+a_2,\\
d=y-S.
\end{cases}
\tag{9.3}
\]
There are no other cases because
\[
d-y\in[-3M,2M]
\]
and the only multiples of \(S=2M+1\) in this interval are \(0\) and \(-S\).

Similarly, a midpoint witness
\[
2n=(Sa_1+b_1)+(Sa_2+b_2)
\]
is equivalent to either
\[
\begin{cases}
2x=a_1+a_2,\\
2y=b_1+b_2,
\end{cases}
\tag{9.4}
\]
or
\[
\begin{cases}
2x+1=a_1+a_2,\\
2y-S=b_1+b_2.
\end{cases}
\tag{9.5}
\]

Equations (9.2)–(9.5) are an exact carry-compatible composition criterion. In particular, a high low-digit target can be covered using a negative triple value and a representation of the adjacent outer digit. This avoids the corner obstruction of Lemma 4.1.

However, I cannot construct disjoint-difference row families for which (9.2)–(9.5) cover every pair \((x,y)\) while the outer gadget also remains cubic-scale and recursively composable.

---

### 10. Ledger

**Proved lemmas**

1. Full Cartesian products are never Sidon once both factors are nontrivial.
2. The checksum graph is Sidon exactly under the nonzero-rectangle condition.
3. An integer checksum alphabet has size at least the larger factor.
4. The full no-carry vector-box lifting lemma.
5. The extreme-digit obstruction for checksum products.
6. The exact disjoint-difference criterion for row-family Sidonicity.
7. Explicit \(q\)-row, \(q\)-mark disjoint-difference families of scope \(<4q^3\).
8. Each proper finite-field row triple above covers exactly \(q^2(q+1)/2\) of the \(q^3\) low-coordinate targets.
9. The exact one-carry composition equations (9.2)–(9.5).

**Plausible but unproved**

1. A bounded number of generic finite-field row-triple images cannot cover \(\mathbb F_q^3\); character-sum methods should leave simultaneous nonsquare discriminants unless the forms satisfy exceptional dependencies.
2. Special exceptional families of row triples might nevertheless cover with a constant number of images.
3. A carry-compatible cyclic difference-family amplifier may be more promising than a no-carry Cartesian gadget.

**Dead ends**

1. Plain Cartesian or separable mixed-radix products: killed by rectangle identities.
2. Cartesian products with an independent no-carry checksum: killed quantitatively by Lemma 4.1.
3. Direct no-carry lifting of the finite-field row family to a full digit box: extreme coordinates freeze too many low parameters.
4. Modular saturation alone: wrap-around does not provide the required integer equality.

## Self-Audit

1. **The obstruction is not universal.** Lemma 4.1 rules out only a natural checksum-graph/no-carry implementation, not every conceivable multiscale composition. I believe the stated obstruction itself is sound because its proof uses only the forced equality \(2M+b_0=b_1+b_2\), but it cannot justify a negative answer to the original problem.

2. **The explicit finite-field construction solves only packing, not covering.** Its disjoint-difference and half-image claims are fully proved, but there is no theorem showing that a constant collection of its row-triple images can or cannot cover all targets. The quadratic calculation is exact; any stronger conclusion from it remains conjectural.

3. **The carry equations do not constitute a construction.** Equations (9.2)–(9.5) are exact and show how a successful composition would work, but finding row families and outer witnesses satisfying them is a new unsolved design problem. I regard the reduction as reliable because it follows by listing all possible multiples of \(2M+1\), but it is comparable in difficulty to the original exact-coverage problem.

## Computations To Verify

```python
from itertools import combinations_with_replacement, product

def is_sidon(A):
    A = sorted(A)
    seen = {}
    for i, a in enumerate(A):
        for b in A[i:]:
            s = a + b
            if s in seen:
                return False, (seen[s], (a, b), s)
            seen[s] = (a, b)
    return True, None

def is_maximal_sidon(N, A):
    A = sorted(A)
    ok, witness = is_sidon(A)
    if not ok:
        return False, ("not Sidon", witness)

    blocked = [False] * (N + 1)
    for i, b in enumerate(A):
        for c in A[i:]:
            s = b + c
            for a in A:
                x = s - a
                if 1 <= x <= N:
                    blocked[x] = True
            if s % 2 == 0 and 1 <= s // 2 <= N:
                blocked[s // 2] = True

    holes = [x for x in range(1, N + 1) if not blocked[x]]
    return len(holes) == 0, holes
```

Verify the explicit disjoint-difference family:

```python
def finite_field_rows(q):
    # q must be an odd prime for this implementation.
    R = 2*q - 1

    def enc(x, y, z):
        return x + R*y + R*R*z

    rows = []
    for i in range(q):
        row = []
        for t in range(q):
            row.append(enc(t, (t*t) % q, (i*t) % q))
        rows.append(sorted(row))
    return rows

def verify_disjoint_differences(q):
    rows = finite_field_rows(q)
    seen = {}
    for i, row in enumerate(rows):
        for s, x in enumerate(row):
            for t, y in enumerate(row):
                if s == t:
                    continue
                d = x - y
                if d in seen:
                    return False, (d, seen[d], (i, s, t))
                seen[d] = (i, s, t)

    expected = q*q*(q-1)
    return len(seen) == expected, (len(seen), expected, rows)

for q in [3, 5, 7, 11]:
    print(q, verify_disjoint_differences(q)[0])
```

Verify the half-image formula:

```python
def triple_image(q, i0, i1, i2):
    image = set()
    for r, s, t in product(range(q), repeat=3):
        image.add((
            (s + t - r) % q,
            (s*s + t*t - r*r) % q,
            (i1*s + i2*t - i0*r) % q
        ))
    return image

for q in [3, 5, 7, 11]:
    for i0, i1, i2 in product(range(q), repeat=3):
        if len({i0, i1, i2}) == 3:
            size = len(triple_image(q, i0, i1, i2))
            assert size == q*q*(q+1)//2
    print("half-image verified for q =", q)
```

Find the minimum number of proper row-triple images covering \(\mathbb F_q^3\), using OR-Tools CP-SAT:

```python
from ortools.sat.python import cp_model

def minimum_image_cover(q):
    universe = list(product(range(q), repeat=3))
    triples = []
    images = []

    # Summand rows are unordered at the outer level.
    for i0 in range(q):
        for i1 in range(q):
            for i2 in range(i1, q):
                if len({i0, i1, i2}) == 3:
                    triples.append((i0, i1, i2))
                    images.append(triple_image(q, i0, i1, i2))

    model = cp_model.CpModel()
    choose = [model.NewBoolVar(f"z_{j}") for j in range(len(triples))]

    for point in universe:
        carriers = [choose[j] for j, I in enumerate(images) if point in I]
        model.Add(sum(carriers) >= 1)

    model.Minimize(sum(choose))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300
    status = solver.Solve(model)

    selected = [
        triples[j] for j in range(len(triples))
        if solver.Value(choose[j])
    ]
    return solver.StatusName(status), len(selected), selected

for q in [3, 5, 7]:
    print(q, minimum_image_cover(q))
```

Test a complete composed integer set once an outer set and row assignment are proposed:

```python
def compose_rows(outer_A, rows):
    assert len(outer_A) == len(rows)
    M = max(max(row) for row in rows)
    S = 2*M + 1
    C = []
    for a, row in zip(outer_A, rows):
        for b in row:
            C.append(S*a + b)
    return sorted(C)

# Example: this tests Sidonicity only, not maximality.
q = 5
rows = finite_field_rows(q)
outer_A = [0, 1, 4, 10, 12]  # Replace by any verified q-element Sidon set.
assert is_sidon(outer_A)[0]
C = compose_rows(outer_A, rows)
print("composite size:", len(C))
print("composite Sidon:", is_sidon(C)[0])
```

The decisive computational experiment is the minimum-image-cover calculation. If the optimum grows with \(q\), especially like \(\log q\), this finite-field amplifier is unlikely to remove the logarithm. If it remains bounded and the selected triples have a recognizable algebraic pattern, that pattern is the most promising next lead.

## Route Diagnosis

The naive form of Route 4 is blocked by an exact incompatibility: coordinatewise product coverage wants a Cartesian product, while Sidonicity forbids its rectangles. An auxiliary checksum repairs Sidonicity but creates an extra digit whose extreme fibers cannot be covered with only constant outer representation multiplicity. The best surviving variant is the row-family construction: replace identical inner copies by a family of Golomb rulers with globally disjoint differences. Finite fields provide such families at the optimal cubic scope, so the pairing problem itself is not fatal.

The remaining block is exact cross-row coverage. One needs balanced families \(B_a\subseteq[0,O(mn^2)]\) such that their differences are globally disjoint and, for every outer digit \(x\), the triple sets associated with representations of \(x\) and \(x+1\) satisfy the carry-compatible conditions (9.2)–(9.5). This is a design problem with only constant average witness multiplicity and is therefore comparable in strength to the original Erdős problem. Even if such an amplifier were found for prime scales, recursive preservation and interpolation to every sufficiently large \(N\) would still require proof.

A fresh attempt should first classify the discriminant forms arising from the finite-field row triples and determine whether a bounded number can cover \(\mathbb F_q^3\). A positive classification would give a concrete amplifier candidate; a negative character-sum theorem would decisively eliminate this algebraic version of Route 4 and suggest returning to semirandom or direct covering-ruler methods.