STATUS: BLOCKED

## Result

Route 2 does not presently yield a complete solution. I proved that unrestricted exact-one-agreement codes are exactly equivalent to arbitrary PBDs, so the coding formulation alone gives no extra structure. I then ruled out several major algebraic subclasses: equifibered mixed orthogonal arrays and subgroup-coset constructions have multiplicity at least \(n/\tau(n)\), while dense restrictions of affine or projective planes have a block-size spike \(\Omega(n^{3/4})\). Independent refinement of their fibers cannot remove such a spike by more than a factor of two. I also isolated a sharper nonlinear subproblem: a bounded-frequency exact difference family of partial permutations would solve all square orders \(n=q^2\). Affine partial permutations cannot do this, and the nonlinear difference-family statement remains unproved; moreover, square orders alone would not settle all sufficiently large \(n\).

## Complete Argument

### 1. Preliminary: the de Bruijn–Erdős bound

Let \(\mathcal A=(A_1,\dots,A_m)\) be a nontrivial PBD on a set \(X\) of \(n\) points. Let \(N\) be its point-block incidence matrix, and let \(r_x\) be the number of blocks containing \(x\).

Every \(r_x\ge 2\). Indeed, if \(x\) lay in only one block \(A\), then every pair \(\{x,y\}\) would force every \(y\in X\) into \(A\), so \(A=X\), contrary to nontriviality.

Distinct points occur together in exactly one block, so
\[
NN^{\mathsf T}=J+\operatorname{diag}(r_x-1).
\]
For every nonzero real vector \(z=(z_x)_{x\in X}\),
\[
z^{\mathsf T}NN^{\mathsf T}z
=
\left(\sum_x z_x\right)^2+\sum_x(r_x-1)z_x^2>0.
\]
Thus \(NN^{\mathsf T}\) has rank \(n\), whence \(N\) has at least \(n\) columns:
\[
m\ge n.
\tag{9}
\]

This will be used repeatedly below.

---

### 2. Exact-one-agreement codes are equivalent to arbitrary PBDs

#### Lemma 1

Let \(X\) be a finite set. Suppose maps
\[
f_j:X\to\Sigma_j,\qquad j=1,\dots,r,
\]
satisfy
\[
\bigl|\{j:f_j(x)=f_j(y)\}\bigr|=1
\quad\text{for all distinct }x,y\in X.
\tag{10}
\]
Then all non-singleton fibers \(f_j^{-1}(a)\) form a PBD on \(X\).

Conversely, every PBD on \(X\) arises in this way, with exactly the same non-singleton fibers and therefore the same block-size histogram.

#### Proof

For the forward direction, take all fibers \(f_j^{-1}(a)\) having size at least two. Given distinct \(x,y\), condition (10) gives exactly one coordinate \(j\) for which \(f_j(x)=f_j(y)\). In that coordinate there is exactly one fiber containing both points. Hence every pair belongs to exactly one non-singleton fiber.

For the converse, let \(\mathcal A=(A_1,\dots,A_m)\) be a PBD. For each \(i\), introduce a symbol \(\star_i\) not belonging to \(X\), and define
\[
f_i(x)=
\begin{cases}
\star_i,&x\in A_i,\\
x,&x\notin A_i.
\end{cases}
\]
For distinct \(x,y\),
\[
f_i(x)=f_i(y)
\quad\Longleftrightarrow\quad
x,y\in A_i.
\]
Indeed, two distinct points outside \(A_i\) receive their distinct point labels, and a point inside and a point outside receive different kinds of symbols. Since each pair lies in exactly one \(A_i\), the maps satisfy (10). The only non-singleton fiber of \(f_i\) is \(A_i\). ∎

#### Consequence

Without further hypotheses—such as balanced fibers, bounded alphabets, algebraicity, or a small number of coordinates—Route 2 is not a simplification of the original problem. It is an exact reformulation.

---

### 3. Balanced mixed-level arrays and coset constructions fail badly

Call a coordinate \(f_j:X\to\Sigma_j\) **equifibered** if all its nonempty fibers have the same size \(k_j\). Then \(k_j\mid n\), and that coordinate contributes \(n/k_j\) blocks of size \(k_j\).

#### Lemma 2

Suppose a nontrivial exact-one-agreement code on \(n\) points has every nontrivial coordinate equifibered. Let
\[
M=\max_t b_t.
\]
Then
\[
M\ge \frac{n}{d(n)},
\tag{11}
\]
where \(d(n)\) is the number of proper divisors \(t\) of \(n\) satisfying \(2\le t\le n-1\). In particular,
\[
M\ge \frac{n}{\tau(n)}.
\tag{12}
\]

If \(n=p^e\) with \(e\ge2\), then
\[
M\ge \frac{p^e}{e-1}.
\tag{13}
\]

#### Proof

By Lemma 1, the non-singleton fibers form a nontrivial PBD. Therefore their total number \(m\) satisfies \(m\ge n\) by (9).

Every meaningful fiber size \(t\) divides \(n\), and there are at most \(d(n)\) possible such sizes. Thus
\[
m=\sum_t b_t\le d(n)M.
\]
Combining this with \(m\ge n\) proves (11). Since \(d(n)\le\tau(n)\), (12) follows. For \(n=p^e\), the only proper nontrivial divisor sizes are
\[
p,p^2,\dots,p^{e-1},
\]
giving (13). ∎

There is also an exact numerical identity. Each equifibered coordinate of fiber size \(k_j\) covers
\[
\frac{n}{k_j}\binom{k_j}{2}
=\frac n2(k_j-1)
\]
pairs. Consequently,
\[
\sum_j(k_j-1)=n-1.
\tag{14}
\]

#### Corollary 2.1: subgroup-coset constructions

Let \(G\) be a group of order \(n\), and suppose the coordinates are coset maps associated with subgroups \(H_j\le G\). Every fiber has size \(|H_j|\), which divides \(n\). Hence every nontrivial exact-one-agreement code of this form satisfies (11)–(13).

In particular, along \(n=2^e\),
\[
\frac{M}{\sqrt n}
\ge
\frac{2^{e/2}}{e-1}\longrightarrow\infty.
\]
Thus group-linear, homomorphic, and coset-partition versions of Route 2 cannot solve the problem.

For prime \(n\), this subclass cannot even produce a nontrivial design, because there is no proper subgroup of size at least two.

---

### 4. Dense deletion from any uniform \(2\)-design forces an \(\Omega(n^{3/4})\) spike

The finite-plane obstruction extends to every uniform \(2\)-\((v,k,1)\) design.

#### Lemma 3: exact intersection variance

Let \(\mathcal D\) be a \(2\)-\((v,k,1)\) design with \(b\) blocks, and let \(S\) be a set of \(s\) points. For a uniformly random block \(B\), put
\[
T=|B\cap S|,\qquad \alpha=\frac{s}{v}.
\]
Then
\[
\mathbb E T=\frac{sk}{v}
\tag{15}
\]
and
\[
\operatorname{Var}(T)
=
k\alpha(1-\alpha)\frac{v-k}{v-1}.
\tag{16}
\]

#### Proof

In a \(2\)-\((v,k,1)\) design,
\[
r=\frac{v-1}{k-1},
\qquad
b=\frac{v(v-1)}{k(k-1)}.
\]
Counting incidences between \(S\) and blocks gives
\[
\sum_{B} |B\cap S|=sr,
\]
so
\[
\mathbb E T=\frac{sr}{b}=\frac{sk}{v}.
\]

Counting ordered pairs of distinct points of \(S\) lying in a block gives
\[
\sum_B |B\cap S|(|B\cap S|-1)=s(s-1).
\]
Therefore
\[
\mathbb E[T(T-1)]
=
\frac{s(s-1)}b
=
\frac{s(s-1)k(k-1)}{v(v-1)}.
\]
Using
\[
\operatorname{Var}(T)
=
\mathbb E[T(T-1)]+\mathbb ET-(\mathbb ET)^2
\]
and simplifying gives (16). ∎

#### Lemma 4: quantitative concentration

Fix \(0<\delta\le1\). Under the hypotheses of Lemma 3, suppose
\[
s\ge\delta v,\qquad s>k,\qquad k\ge \frac{4}{\delta^2}.
\tag{17}
\]
Let
\[
h_t=\bigl|\{B:|B\cap S|=t\}\bigr|.
\]
Then for some \(t\) with \(2\le t\le s-1\),
\[
h_t\ge \frac{b}{4\sqrt k}.
\tag{18}
\]

#### Proof

Write
\[
\mu=\mathbb ET,\qquad \sigma^2=\operatorname{Var}(T).
\]
By (15) and \(s\ge\delta v\),
\[
\mu\ge\delta k.
\]
By (16),
\[
\sigma^2\le k\alpha(1-\alpha)\le\frac k4,
\]
so
\[
2\sigma\le\sqrt k.
\]
The lower endpoint of the interval \((\mu-2\sigma,\mu+2\sigma)\) is at least
\[
\delta k-\sqrt k.
\]
The assumption \(k\ge4/\delta^2\) implies
\[
\sqrt k\le\frac{\delta k}{2},
\]
and hence
\[
\delta k-\sqrt k\ge\frac{\delta k}{2}\ge2.
\tag{19}
\]

If \(\sigma=0\), every block has the same intersection size \(\mu\), so \(h_\mu=b\), and the conclusion is immediate.

Assume \(\sigma>0\). Chebyshev's inequality gives
\[
\Pr(|T-\mu|\ge2\sigma)\le\frac14.
\]
Thus at least \(3b/4\) blocks have intersection size in the interval
\[
|T-\mu|<2\sigma.
\]
This interval contains at most
\[
4\sigma+1\le2\sqrt k+1\le3\sqrt k
\]
integer values. Therefore one value \(t\) occurs at least
\[
\frac{3b/4}{3\sqrt k}=\frac{b}{4\sqrt k}
\]
times.

By (19), this \(t\ge2\). Also \(T\le k<s\), so \(t\le s-1\). ∎

Intersections of size at least two form a PBD on \(S\), since every pair of points of \(S\) lies in its unique original design block. Thus the \(h_t\) in Lemma 4 are actual PBD block multiplicities.

#### Corollary 4.1: affine and projective planes

For an affine plane of order \(q\),
\[
v=q^2,\qquad k=q,\qquad b=q(q+1).
\]
For every \(S\) of size \(s\ge\delta q^2\), and all sufficiently large \(q\),
\[
\max_t h_t
\ge
\frac{q(q+1)}{4\sqrt q}
=\Omega(q^{3/2})
=\Omega_\delta(s^{3/4}).
\tag{20}
\]

For a projective plane of order \(q\),
\[
v=q^2+q+1,\qquad k=q+1,\qquad b=v,
\]
and the same conclusion holds:
\[
\max_t h_t=\Omega_\delta(s^{3/4}).
\tag{21}
\]

Since \(\sqrt s=\Theta(q)\), both lower bounds exceed every fixed multiple of \(\sqrt s\) for sufficiently large \(q\).

This applies directly to the affine exact-one-agreement code consisting of affine functions
\[
x\longmapsto ax+b.
\]
Selecting a dense subset of these functions is exactly restricting the dual affine plane to a dense point set.

---

### 5. Independent fiber refinement cannot repair a large spike

A natural reaction to the preceding concentration is to refine every over-repeated fiber by a separate PBD. This also fails.

#### Lemma 5: refinement preserves at least half of a spike

Suppose a PBD contains \(h\) blocks
\[
B_1,\dots,B_h
\]
of the same size \(k\ge3\). Form a new PBD only by, independently for each \(B_i\), either:

1. retaining \(B_i\); or
2. replacing all pairs inside \(B_i\) by a nontrivial PBD on \(B_i\).

Let \(M\) be the maximum final block-size multiplicity. Then
\[
M>\frac h2.
\tag{22}
\]

#### Proof

Let \(u\) of the \(h\) parent blocks be retained. Since each retained block has size \(k\),
\[
u\le M.
\tag{23}
\]

Every one of the remaining \(h-u\) parent blocks is replaced by a nontrivial PBD on \(k\) points. By (9), each such ingredient contains at least \(k\) blocks. No ingredient block has size \(k\), so all its blocks have one of the \(k-2\) sizes
\[
2,3,\dots,k-1.
\]
Therefore the refined parents produce at least
\[
(h-u)k
\]
blocks distributed among only \(k-2\) possible sizes. Consequently,
\[
M\ge \frac{(h-u)k}{k-2}.
\tag{24}
\]
Equations (23) and (24) imply
\[
h
=
u+(h-u)
\le
M+M\frac{k-2}{k}
=
2M-\frac{2M}{k}<2M.
\]
Hence \(M>h/2\). ∎

The blocks produced inside distinct parents are genuinely distinct: two original PBD blocks intersect in at most one point, so no child block of size at least two can lie in two parents.

For \(k=2\), no nontrivial refinement is possible, and the stronger bound \(M\ge h\) holds.

#### Corollary 5.1

Take a dense restriction of an affine or projective plane. Lemma 4 supplies \(h=\Omega(s^{3/4})\) blocks of one size. Any construction obtained by independently refining or retaining these fibers still satisfies
\[
M=\Omega(s^{3/4}).
\tag{25}
\]

Therefore deletion followed by coordinate-wise or fiber-wise concatenation cannot solve the problem. Any successful repair would have to use trades that mix pairs from different original fibers.

---

### 6. A sharper nonlinear target: partial-permutation difference families

The most promising structure uncovered inside Route 2 is the following square-order reduction.

Let
\[
V=\mathbb Z_q\times[q].
\]
Regard a point \((r,c)\) as an edge between row vertex \(r\) and column vertex \(c\) in \(K_{q,q}\).

For every row \(r\), take the row block
\[
R_r=\{(r,c):c\in[q]\},
\]
and for every column \(c\), take the column block
\[
C_c=\{(r,c):r\in\mathbb Z_q\}.
\]
These \(2q\) blocks cover exactly the pairs of cells sharing a row or a column.

A partial injection is a map
\[
\phi:S\to\mathbb Z_q,\qquad S\subseteq[q],
\]
whose values are distinct. For \(a\in\mathbb Z_q\), define the developed matching block
\[
M_{\phi,a}
=
\{(\phi(c)+a,c):c\in S\}.
\tag{26}
\]
This is a set of cells with distinct rows and distinct columns.

Fix an ordering of the columns. For \(c<c'\) in \(S\), associate to \(\phi\) the requirement
\[
(c,c',\phi(c')-\phi(c)).
\tag{27}
\]
The difference is nonzero because \(\phi\) is injective.

#### Lemma 6: difference-family reduction

Suppose a family \(\mathcal F\) of partial injections has the property that every triple
\[
(c,c',d),
\qquad c<c',\quad d\in\mathbb Z_q\setminus\{0\},
\tag{28}
\]
occurs in exactly one member of \(\mathcal F\) through (27). Then the row blocks, column blocks, and all developed blocks
\[
\{M_{\phi,a}:\phi\in\mathcal F,\ a\in\mathbb Z_q\}
\]
form a PBD on \(q^2\) points.

If at most \(L\) members of \(\mathcal F\) have any given domain size, then
\[
\max_t b_t\le (L+2)q.
\tag{29}
\]

#### Proof

Consider two distinct cells.

If they share a row, they lie together in their unique row block. No developed block contains them because a partial injection has distinct row values.

If they share a column, they lie together in their unique column block. No developed block contains two cells from the same column.

Otherwise write the cells as
\[
(r,c),\qquad (r',c'),\qquad c<c'.
\]
Their rows and columns are both distinct, so
\[
d=r'-r\ne0.
\]
By hypothesis, there is a unique \(\phi\in\mathcal F\) with
\[
c,c'\in\operatorname{dom}\phi,
\qquad
\phi(c')-\phi(c)=d.
\]
There is then a unique translate
\[
a=r-\phi(c)
\]
for which both cells lie in \(M_{\phi,a}\). Hence every pair is covered exactly once.

Each base injection of size \(t\) produces exactly \(q\) developed blocks of size \(t\). Thus it contributes at most \(Lq\) blocks to any size. The row and column blocks add \(2q\) further blocks only at size \(q\), proving (29). ∎

The total number of requirements is
\[
\binom q2(q-1).
\]
A base injection of size \(k\) covers \(\binom k2\) requirements. Therefore, if at most \(L\) base injections of each size are used, necessarily
\[
L\sum_{k=2}^q\binom k2
\ge
\binom q2(q-1).
\]
Since
\[
\sum_{k=2}^q\binom k2=\binom{q+1}{3},
\]
one must have
\[
L\ge
\frac{\binom q2(q-1)}{\binom{q+1}{3}}
=
\frac{3(q-1)}{q+1}.
\tag{30}
\]
Thus \(L\ge3\) for \(q\ge6\). A bound such as \(L=3\) or \(4\) would be asymptotically optimal and, by Lemma 6, would solve the problem for square orders.

No such bounded-\(L\) construction is currently proved here.

---

### 7. Affine partial permutations cannot realize the difference family

The standard finite-field idea remains too rigid even after allowing partial domains.

#### Lemma 7

Let \(q\) be a prime power, identify both rows and columns with \(\mathbb F_q\), and suppose every base partial injection in Lemma 6 is the restriction of an affine map
\[
c\longmapsto ac+b,\qquad a\ne0.
\tag{31}
\]
Then some base size occurs at least \((q-1)/2\) times. Consequently, after development, some block size occurs at least
\[
\frac{q(q-1)}2
\tag{32}
\]
times.

#### Proof

For fixed distinct columns \(c,c'\), an affine map of slope \(a\) gives difference
\[
a(c'-c).
\]
As \(a\) ranges over \(\mathbb F_q^\times\), these are exactly the \(q-1\) nonzero differences, each once.

Therefore, for each fixed slope \(a\), the supports of the selected affine maps of slope \(a\) must contain every pair \(\{c,c'\}\) exactly once. In other words, the supports for each slope form a PBD on the \(q\) columns.

For a given slope this PBD is either:

- trivial, consisting of one support of size \(q\); or
- nontrivial, and therefore has at least \(q\) supports by (9).

Let \(T\) be the number of slopes with the trivial support design.

If
\[
T\ge\frac{q-1}{2},
\]
then size \(q\) occurs among the base blocks at least \((q-1)/2\) times.

Otherwise more than \((q-1)/2\) slopes are nontrivial. They contribute more than
\[
\frac{q(q-1)}2
\]
base blocks, all of sizes \(2,\dots,q-1\). There are only \(q-2\) such sizes, so one size occurs more than
\[
\frac{q(q-1)}{2(q-2)}>\frac q2
\]
times.

Thus in all cases some base size has multiplicity at least \((q-1)/2\). Development multiplies this multiplicity by \(q\), proving (32). ∎

This rules out the entire strategy of merely restricting standard affine permutations on different supports. A successful partial-permutation difference family must use genuinely nonlinear labels.

---

### 8. Ledger

**Proved lemmas**

1. Every nontrivial PBD has at least \(n\) blocks.
2. Unrestricted exact-one-agreement codes are precisely arbitrary PBDs with singleton padding.
3. Equifibered mixed arrays and subgroup-coset codes satisfy \(M\ge n/\tau(n)\), and \(M\ge p^e/(e-1)\) on \(p^e\) points.
4. Dense restrictions of uniform \(2\)-designs have a size multiplicity at least \(b/(4\sqrt k)\).
5. In particular, dense affine- and projective-plane restrictions have \(M=\Omega(n^{3/4})\).
6. Independent block refinement cannot reduce a multiplicity spike below half its original size.
7. A bounded-frequency partial-permutation difference family would produce the desired bound for \(n=q^2\).
8. Partial affine maps cannot supply such a difference family.

**Plausible but unproved**

- There may exist an absolute \(L\) such that for every \(q\), the requirement set (28) has an exact cover by partial injections with at most \(L\) injections of each size. The numerical lower bound suggests \(L=3\) or \(4\), but no proof is available.
- Even if the square-order statement holds, a robust extension from \(q^2\) to every nearby \(n\) is still needed.

**Dead ends**

- Balanced mixed orthogonal arrays: too few possible fiber sizes.
- Group and subgroup-coset codes: the same divisor obstruction.
- Dense deletion from affine or projective codes: exact variance forces \(\Omega(n^{3/4})\) concentration.
- Independent fiber refinement or ordinary concatenation: Lemma 5 preserves at least half the spike.
- Restricting affine permutations to varying domains: Lemma 7 forces \(\Omega(q^2)\) repetition after development.

## Self-Audit

1. **The concentration theorem has deliberately restricted scope.** It applies only to dense restrictions of uniform \(2\)-designs, not to arbitrary nonlinear exact-one codes. Within that scope, the conclusion follows from exact first and second moment identities and Chebyshev's inequality; no randomness assumption on the selected point set is used.

2. **The refinement obstruction excludes only independent refinements.** Cross-fiber trades could evade Lemma 5 by moving pairs between different parent blocks. The lemma itself is sound because every independently refined parent contributes a complete nontrivial PBD on \(k\) points, hence at least \(k\) final blocks among only \(k-2\) possible sizes.

3. **The partial-permutation construction is only a reduction, not an existence theorem.** The exact-cover condition in Lemma 6 has been checked pair by pair, so the implication is rigorous. What is missing is the bounded-frequency difference family itself, followed by an all-orders extension. I do not treat either as established.

## Computations To Verify

The following searches the partial-permutation difference-family problem. It works for every integer \(q\), using the cyclic row group \(\mathbb Z_q\). Translating a partial injection lets us normalize its value at the least domain element to zero.

```python
from itertools import combinations, permutations
from collections import defaultdict, Counter
from ortools.sat.python import cp_model

def difference_candidates(q):
    """
    Candidate base partial injections phi:S -> Z_q, modulo row translation.
    Each candidate is (rows_dict, requirement_tuple).
    """
    candidates = []

    for k in range(2, q + 1):
        for cols in combinations(range(q), k):
            anchor = cols[0]

            # Normalize phi(anchor)=0. Other values must be distinct and nonzero.
            for vals in permutations(range(1, q), k - 1):
                phi = {anchor: 0}
                for c, value in zip(cols[1:], vals):
                    phi[c] = value

                reqs = []
                for a, b in combinations(cols, 2):
                    d = (phi[b] - phi[a]) % q
                    assert d != 0
                    reqs.append((a, b, d))

                candidates.append((phi, tuple(reqs)))

    return candidates

def solve_difference_family(q, time_limit=300):
    candidates = difference_candidates(q)

    universe = [
        (a, b, d)
        for a in range(q)
        for b in range(a + 1, q)
        for d in range(1, q)
    ]

    containing = defaultdict(list)
    by_size = defaultdict(list)

    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{i}") for i in range(len(candidates))]

    for i, (phi, reqs) in enumerate(candidates):
        by_size[len(phi)].append(i)
        for req in reqs:
            containing[req].append(i)

    # Exact coverage of every column-pair/difference requirement.
    for req in universe:
        model.Add(sum(x[i] for i in containing[req]) == 1)

    L = model.NewIntVar(0, len(universe), "L")
    for k in range(2, q + 1):
        model.Add(sum(x[i] for i in by_size[k]) <= L)

    model.Minimize(L)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8

    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    selected = [
        candidates[i][0]
        for i in range(len(candidates))
        if solver.Value(x[i])
    ]
    return solver.Value(L), selected
```

The following develops a returned family into a claimed PBD on \(q^2\) points and checks every pair directly.

```python
def check_pbd(n, blocks):
    pair_count = defaultdict(int)

    for B in blocks:
        B = sorted(B)
        assert 2 <= len(B) <= n - 1
        for u, v in combinations(B, 2):
            pair_count[(u, v)] += 1

    for u in range(n):
        for v in range(u + 1, n):
            assert pair_count[(u, v)] == 1, (u, v, pair_count[(u, v)])

    hist = Counter(map(len, blocks))
    return hist

def develop_square_pbd(q, bases):
    def point_id(r, c):
        return r * q + c

    blocks = []

    # Row and column stars.
    for r in range(q):
        blocks.append({point_id(r, c) for c in range(q)})
    for c in range(q):
        blocks.append({point_id(r, c) for r in range(q)})

    # Developed partial injections.
    for phi in bases:
        for shift in range(q):
            B = {
                point_id((row + shift) % q, col)
                for col, row in phi.items()
            }
            blocks.append(B)

    hist = check_pbd(q * q, blocks)
    return blocks, hist

# Suggested experiment:
for q in range(3, 9):
    ans = solve_difference_family(q, time_limit=300)
    if ans is None:
        print(q, "no result")
    else:
        L, bases = ans
        blocks, hist = develop_square_pbd(q, bases)
        print("q =", q, "L =", L,
              "base histogram =", Counter(map(len, bases)),
              "PBD histogram =", hist)
```

A bounded sequence of optimum values \(L\), ideally \(L\le4\), would provide strong evidence for the square-order conjecture. Growth of \(L\) would refute this particular symmetric subroute.

The exact affine-plane moment identities can be checked for arbitrary subsets \(S\) when \(q\) is prime:

```python
from fractions import Fraction
from collections import Counter

def affine_restriction(q, S):
    """
    q should be prime.
    Points of the dual affine plane are affine functions x -> a*x+b.
    """
    S = list(S)
    s = len(S)
    all_fiber_sizes = []
    blocks = []

    # Evaluation coordinates x in F_q.
    for x in range(q):
        fibers = [[] for _ in range(q)]
        for idx, (a, b) in enumerate(S):
            y = (a * x + b) % q
            fibers[y].append(idx)
        all_fiber_sizes.extend(map(len, fibers))
        blocks.extend(set(F) for F in fibers if len(F) >= 2)

    # Coordinate at infinity: common slope.
    slope_fibers = [[] for _ in range(q)]
    for idx, (a, b) in enumerate(S):
        slope_fibers[a].append(idx)
    all_fiber_sizes.extend(map(len, slope_fibers))
    blocks.extend(set(F) for F in slope_fibers if len(F) >= 2)

    v = q * q
    b_design = q * (q + 1)

    assert len(all_fiber_sizes) == b_design
    assert sum(all_fiber_sizes) == s * (q + 1)
    assert sum(t * (t - 1) for t in all_fiber_sizes) == s * (s - 1)

    mean = Fraction(sum(all_fiber_sizes), b_design)
    empirical_var = sum(
        (Fraction(t) - mean) ** 2 for t in all_fiber_sizes
    ) / b_design

    alpha = Fraction(s, v)
    theoretical_var = (
        q * alpha * (1 - alpha) * Fraction(v - q, v - 1)
    )
    assert empirical_var == theoretical_var

    if s > q:
        hist = check_pbd(s, blocks)
    else:
        hist = Counter(map(len, blocks))

    return hist, all_fiber_sizes
```

For random dense subsets \(S\), this should display a maximum histogram entry on the order of \(q^{3/2}\), but the variance assertion is exact for every \(S\), including highly structured ones.

## Route Diagnosis

The coding language worked as a diagnostic tool but not as a solution engine. Its unrestricted form is exactly equivalent to the original PBD problem. The natural structured subclasses are now sharply blocked: balanced mixed arrays have a divisor obstruction, finite-geometry deletion has an exact variance obstruction, and independent concatenation cannot disperse the resulting spike. The most concrete remaining Route 2 target is Lemma 6’s nonlinear partial-permutation difference family. Proving bounded base multiplicity there would settle square orders with the optimal \(\Theta(q)\) scale, but this is itself a growing-clique exact decomposition problem, and affine labels provably fail. A fresh attempt should first run the stated exact-cover search to determine whether the optimum base cap appears bounded. If it does, the next tasks are to identify nonlinear trades generating those solutions and then develop a robust near-square/all-orders extension. If it does not, Route 2 should be abandoned in favor of a genuinely nonsymmetric prescribed-clique decomposition with absorption.