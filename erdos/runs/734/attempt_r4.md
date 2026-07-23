STATUS: BLOCKED

## Result

Route 4 yields a clean exact reduction to bounded-frequency **partial difference matrices** under a semiregular group action. This reduction bypasses the prime-order obstruction by acting on \(qg\) points in \(g\) orbits of length \(q\), possibly with fewer than \(q\) fixed cleanup points. I prove the development criterion, its counting and Fourier constraints, an exact cleanup lemma for arbitrary orders, and two substantial no-go results: any construction whose cross-blocks remain pieces of affine lines has a block size occurring \(\Omega(n)\) times, and merely augmenting the uniform blocks of a transversal design with cleanup points also leaves \(\Omega(n)\) equal-sized blocks. What remains is the construction of genuinely direction-mixing partial difference families with bounded row-size multiplicity. This is an exact decomposition problem of essentially comparable strength to the original problem, so the route is blocked rather than solved.

## Complete Argument

### 1. Why full cyclic symmetry cannot work at prime order

Let \(p\) be prime, and suppose a PBD on \(\mathbb Z_p\) is invariant under all translations.

For any proper nonempty block \(B\), its stabilizer under translation is a subgroup of \(\mathbb Z_p\). Since \(p\) is prime, the stabilizer is either trivial or all of \(\mathbb Z_p\). The latter would make \(B\) translation-invariant, hence \(B=\mathbb Z_p\), which is forbidden. Thus every block has a translation orbit of length \(p\).

Consequently, if one block has size \(t\), its entire orbit gives at least \(p\) blocks of size \(t\). Hence
\[
\max_t b_t\ge p\gg \sqrt p.
\]
Thus full regular symmetry is unusable for prime orders.

The only plausible group-based approach is therefore partial symmetry: many point-orbits under a smaller group, or a group action on most but not all points.

---

### 2. The exact semiregular difference-family formulation

Let \(H\) be a finite group of order \(h\), let \(I\) be a set of \(g\ge2\) labels, and put
\[
X=H\times I.
\]
Let \(H\) act on \(X\) by left translation in the first coordinate:
\[
a\cdot(x,i)=(ax,i).
\]

For every \(i\in I\), let
\[
G_i=H\times\{i\}.
\]
We intend to use each \(G_i\) as a block. Therefore every other block must meet each \(G_i\) in at most one point.

Let \(\mathcal B\) be a family of transversal base blocks
\[
B=\{(x_i,i):i\in S_B\},
\qquad S_B\subseteq I,\quad |S_B|\ge2.
\]
Develop \(B\) under \(H\):
\[
aB=\{(ax_i,i):i\in S_B\},
\qquad a\in H.
\]

#### Lemma 2.1: Difference criterion

The blocks
\[
\{G_i:i\in I\}\cup\{aB:a\in H,\ B\in\mathcal B\}
\tag{9}
\]
form a PBD on \(X\) if and only if, for every two distinct labels \(i,j\in I\) and every \(d\in H\), there is exactly one base block \(B\in\mathcal B\) containing points \((x,i),(y,j)\) satisfying
\[
x^{-1}y=d.
\tag{10}
\]

#### Proof

Pairs within a single group \(G_i\) are covered exactly once by the block \(G_i\), and no transversal block contains two points from \(G_i\).

Now take a cross-pair
\[
\{(u,i),(v,j)\},\qquad i\ne j.
\]
Set \(d=u^{-1}v\). Suppose \(B\) contains \((x,i),(y,j)\) with \(x^{-1}y=d\). There is a unique \(a=ux^{-1}\in H\) such that
\[
ax=u.
\]
Then
\[
ay=ux^{-1}y=ud=v,
\]
so \(aB\) contains the desired pair.

Conversely, if \(aB\) contains \((u,i),(v,j)\), then the corresponding base points satisfy
\[
x^{-1}y=(ax)^{-1}(ay)=u^{-1}v.
\]
Thus uniqueness of pair coverage is exactly uniqueness in (10). ∎

Every transversal base block has trivial stabilizer: if \(aB=B\), then for each \(i\in S_B\), the unique point of \(B\) in \(G_i\) must be fixed, so \(ax_i=x_i\), hence \(a=1\). Thus every developed orbit has exactly \(h\) blocks.

Write
\[
c_t=\bigl|\{B\in\mathcal B:|B|=t\}\bigr|.
\]
Then the resulting PBD has
\[
b_t=h\,c_t+g\,\mathbf 1_{t=h}.
\tag{11}
\]

Therefore, when \(h\) and \(g\) are comparable and \(n=hg\), the desired bound would follow from
\[
\max_t c_t=O(1).
\tag{12}
\]

This is the central advantage of partial group symmetry: a bounded number of base blocks of each size develops into \(O(\sqrt n)\) final blocks of that size.

---

### 3. Necessary counting and linear-algebraic conditions

The difference criterion has several exact consequences.

#### Lemma 3.1: Underlying index-\(h\) design

For every pair \(i\ne j\) of labels, exactly \(h\) base blocks contain both \(i\) and \(j\).

#### Proof

There is exactly one such base-block occurrence for each \(d\in H\). ∎

Thus the domains \(S_B\) form a variable-block-size design of pair index \(h\). In particular,
\[
\sum_{B\in\mathcal B}\binom{|B|}{2}
=
h\binom g2,
\]
or equivalently
\[
\sum_{t=2}^g c_t\,t(t-1)=h\,g(g-1).
\tag{13}
\]

For each label \(i\),
\[
\sum_{B:i\in S_B}(|B|-1)=h(g-1).
\tag{14}
\]

Since \(|B|\le g\), equation (13) gives
\[
|\mathcal B|\ge h.
\tag{15}
\]
Equality forces every base block to have size \(g\), because equality in
\[
|B|(|B|-1)\le g(g-1)
\]
must hold for every base block. This is precisely the uniform generalized-Hadamard or transversal-design situation, which has disastrous size concentration.

If
\[
M_{\rm base}=\max_t c_t,
\]
then
\[
h\,g(g-1)
\le
M_{\rm base}\sum_{t=2}^g t(t-1)
=
M_{\rm base}\frac{g(g+1)(g-1)}3.
\]
Therefore
\[
M_{\rm base}\ge \frac{3h}{g+1}.
\tag{16}
\]
For \(h=g=q\ge3\),
\[
M_{\rm base}\ge3.
\tag{17}
\]
Thus bounded base multiplicity is numerically possible, but the best conceivable constant in this symmetric model is already at least \(3\).

#### Fourier constraint

Suppose \(H=\mathbb Z_q\), with \(q\) prime. Write each base block as a partial function
\[
f_B:S_B\longrightarrow\mathbb Z_q.
\]
For a nontrivial additive character
\[
\chi_a(x)=e^{2\pi iax/q},
\qquad a\ne0,
\]
form the \(|\mathcal B|\times g\) matrix
\[
V^{(a)}_{B,i}=
\begin{cases}
\chi_a(f_B(i)),&i\in S_B,\\
0,&i\notin S_B.
\end{cases}
\]
For \(i\ne j\),
\[
\bigl((V^{(a)})^*V^{(a)}\bigr)_{i,j}
=
\sum_{B:i,j\in S_B}
\chi_a\bigl(f_B(j)-f_B(i)\bigr).
\]
The differences range over every element of \(\mathbb Z_q\) exactly once, so this equals
\[
\sum_{d\in\mathbb Z_q}\chi_a(d)=0.
\]
On the diagonal,
\[
\bigl((V^{(a)})^*V^{(a)}\bigr)_{i,i}
=
r_i,
\]
where \(r_i\) is the number of base blocks whose domain contains \(i\). Hence
\[
(V^{(a)})^*V^{(a)}
=
\operatorname{diag}(r_i:i\in I).
\tag{18}
\]
In particular, its \(g\) columns are nonzero and mutually orthogonal, giving
\[
|\mathcal B|\ge g.
\tag{19}
\]

This is a useful strengthening for computation, but it does not itself force repeated row sizes.

---

### 4. A rigorous no-go theorem for affine-line pieces

The most obvious construction starts from affine functions
\[
x\longmapsto sx+c
\]
and attempts to split or truncate the corresponding affine lines. This entire subclass fails badly.

Let \(H=I=\mathbb F_q\). A transversal block is called **slope-pure** if it has the form
\[
B=\{(sx+c,x):x\in S\}
\tag{20}
\]
for some \(s,c\in\mathbb F_q\) and \(S\subseteq\mathbb F_q\), \(|S|\ge2\).

Vertical development changes \(c\), so each base orbit has a well-defined slope \(s\).

#### Theorem 4.1: Slope-pure constructions have linear repetition

Suppose a difference family on \(\mathbb F_q\times\mathbb F_q\) consists entirely of slope-pure base blocks. Then some final block size occurs at least \(q^2/2\) times.

#### Proof

Fix a slope \(s\). For any two coordinates \(x\ne y\), the difference corresponding to slope \(s\) is
\[
s(y-x).
\]
By the exact difference condition, there is exactly one base block of slope \(s\) whose domain contains \(\{x,y\}\). Therefore the domains of the slope-\(s\) base blocks form a PBD \(\mathcal D_s\) on the coordinate set \(\mathbb F_q\).

Each \(\mathcal D_s\) is either:

1. the trivial one-block PBD \(\{\mathbb F_q\}\); or
2. a nontrivial PBD, which has at least \(q\) blocks by de Bruijn–Erdős.

Let \(u\) be the number of slopes for which \(\mathcal D_s\) is trivial.

If \(u\ge q/2\), then there are at least \(q/2\) base blocks of size \(q\).

If \(u<q/2\), then more than \(q/2\) slopes give nontrivial PBDs. These contribute more than \(q^2/2\) base blocks, all of sizes \(2,\dots,q-1\). There are only \(q-2\) such sizes, so some size occurs more than
\[
\frac{q^2/2}{q-2}>\frac q2
\]
times among the base blocks.

In either case, some base size occurs at least \(q/2\) times. Every base block develops into \(q\) blocks of the same size, so the corresponding final multiplicity is at least
\[
q\cdot\frac q2=\frac{q^2}{2}.
\]
Since \(n=q^2\), this is \(\Omega(n)\), not \(O(\sqrt n)\). ∎

Therefore it is not enough to truncate affine lines, refine individual slope classes, or use a different PBD separately for every slope. Any successful difference-family construction must use base blocks whose secant differences mix many affine directions.

#### Small examples do not contradict the theorem

For \(q=3\), take two full affine maps
\[
f_0(x)=0,\qquad f_1(x)=x,
\]
and split the third slope into the three two-element domains. The base profile is
\[
c_2=3,\qquad c_3=2.
\]
After development and adding the three vertical groups,
\[
b_2=b_3=9.
\]
This gives a valid PBD on \(9\) points, but the ratio \(9/\sqrt9=3\) is only a small-order phenomenon.

For \(q=4\), over \(\mathbb F_4\), retain three slopes as full blocks and refine the fourth using a near-pencil on the four coordinate labels. The base profile is
\[
c_2=3,\qquad c_3=1,\qquad c_4=3.
\]
After development,
\[
b_2=12,\qquad b_3=4,\qquad b_4=16.
\]
Again this is valid, but the slope-pure theorem shows that this pattern cannot have a uniform asymptotic analogue.

---

### 5. Cleanup points do not flatten a uniform transversal design

One might begin with the standard uniform difference matrix and add extra points to selected blocks, hoping to turn blocks of size \(g\) into many different sizes. A simple incidence count rules this out.

Let \(X\) be a moving point set of size \(qg\), and suppose there are \(q^2\) cross-blocks, each containing exactly \(g\) moving points, as in a transversal design obtained from
\[
f_s(i)=si+c.
\]
Let \(Z\) be a set of \(r\le q\) new points. Suppose the only modification is to augment these \(q^2\) blocks by subsets of \(Z\), and suppose every pair \(\{z,x\}\), \(z\in Z\), \(x\in X\), is covered exactly once.

For each \(z\in Z\), the moving parts of the blocks containing \(z\) partition \(X\). Each such moving part has size \(g\), so \(z\) lies in exactly
\[
\frac{|X|}{g}=q
\]
augmented blocks. Therefore the total number of incidences between new points and old cross-blocks is
\[
rq\le q^2.
\tag{21}
\]

Let \(a_L\) be the number of new points added to an old cross-block \(L\). Then
\[
\sum_L a_L=rq\le q^2.
\]
Hence at most \(q^2/2\) old blocks have \(a_L\ge2\). At least \(q^2/2\) have \(a_L\in\{0,1\}\), so one of these two values occurs for at least \(q^2/4\) blocks. Thus at least \(q^2/4\) final blocks have size \(g\), or at least \(q^2/4\) have size \(g+1\).

When \(q\asymp g\), the number of points is \(\Theta(q^2)\), while the multiplicity is \(\Omega(q^2)\). Therefore adding cleanup points to an otherwise uniform transversal design cannot solve the problem, even if the augmentation breaks the original symmetry.

---

### 6. An exact cleanup lemma for arbitrary \(n\)

Although cleanup cannot repair a uniform family, it can extend an already-flat partial difference family to arbitrary orders.

Let \(X=H\times I\) and let \(\mathcal B\) satisfy the difference criterion. Let
\[
Z=\{z_1,\dots,z_r\}
\]
be new points.

Suppose that for each \(z\in Z\), there is a subfamily
\[
\mathcal P_z\subseteq\mathcal B
\]
such that:

1. the domain sets \(\{S_B:B\in\mathcal P_z\}\) partition \(I\);
2. the subfamilies \(\mathcal P_z\) are pairwise disjoint.

For \(B\in\mathcal P_z\), replace every developed block \(aB\) by
\[
aB\cup\{z\}.
\]
Leave unselected developed blocks unchanged. Retain the group blocks \(G_i\), and add \(Z\) as one block if \(r\ge2\).

#### Lemma 6.1: The resulting family is a PBD on \(hg+r\) points

#### Proof

Pairs of moving points are covered exactly as before, because adding fixed points does not change their coverage.

Fix \(z\in Z\) and a moving point \((u,i)\). Since the domains in \(\mathcal P_z\) partition \(I\), there is exactly one \(B\in\mathcal P_z\) with \(i\in S_B\). Write the point of \(B\) in group \(i\) as \((x,i)\). There is exactly one \(a=ux^{-1}\) such that \(aB\) contains \((u,i)\). Hence \(\{z,(u,i)\}\) is covered exactly once.

No developed block contains two points of \(Z\), because the \(\mathcal P_z\) are disjoint. Thus pairs within \(Z\) are covered exactly once by the block \(Z\), when \(r\ge2\). ∎

Let \(c_t\) be the total number of base blocks of size \(t\), and let \(a_t\) be the number of selected base blocks of size \(t\). Then the developed contribution to size \(t\) is
\[
h\bigl(c_t-a_t+a_{t-1}\bigr).
\tag{22}
\]
Consequently, if \(c_t\le D\) for every \(t\), then every developed multiplicity is at most
\[
2Dh.
\tag{23}
\]

This gives a precise sufficient object for all orders.

#### Conditional reduction for all large \(n\)

Define a resolvable partial difference family \(\operatorname{RPDF}(q,g,r;D)\) to be a family of partial maps
\[
f_B:S_B\to\mathbb Z_q
\]
such that:

1. for every \(i\ne j\) and every \(d\in\mathbb Z_q\), exactly one \(B\) has \(i,j\in S_B\) and
   \[
   f_B(j)-f_B(i)=d;
   \]
2. at most \(D\) domains have any prescribed cardinality;
3. there are \(r\) pairwise disjoint subfamilies whose domains each partition the \(g\) coordinates.

If there were a universal \(D\) such that \(\operatorname{RPDF}(q,g,r;D)\) existed for every sufficiently large prime \(q\), every
\[
q/12\le g\le q,
\]
and every \(0\le r<q\), then Erdős Problem #734 would follow.

Indeed, given large \(n\), let \(x=\lceil\sqrt n\rceil\). By Bertrand’s postulate choose a prime
\[
x<q<2x.
\]
Set
\[
g=\left\lfloor\frac nq\right\rfloor,\qquad r=n-qg.
\]
Then \(0\le r<q\), \(g\le q\), and for sufficiently large \(n\),
\[
\frac q{12}\le g\le q.
\]
Apply the RPDF construction and Lemma 6.1. Equations (22)–(23), together with the \(g\) group blocks and at most one fixed-point block, give
\[
\max_t b_t\le 2Dq+g+1=O(\sqrt n),
\]
with an absolute constant.

This implication is rigorous. The existence of the required RPDFs is not proved.

---

### 7. Precise obstruction remaining

For \(q=g\), the missing object can be described as an incomplete generalized Hadamard matrix:

- columns are coordinate labels;
- rows are partial functions \(f:S\to\mathbb Z_q\);
- for each pair of columns, the differences over rows containing both columns must be exactly \(\mathbb Z_q\);
- at most \(O(1)\) rows may have any one support size.

The elementary pair count only forces
\[
\max_t c_t\ge3,
\]
so there is no numerical contradiction. The character identity (18) also allows \(O(q)\) rows with widely varying supports. The obstruction is therefore genuinely geometric/algebraic: assigning compatible differences around all triangles of each support.

Constructing these direction-mixing rows for every large \(q\), let alone with the resolution subfamilies needed for arbitrary \(n\), is an unproved exact decomposition statement at the same \(\sqrt n\) scale as the original problem.

### Ledger

**Proved lemmas**

1. Full translation invariance on \(\mathbb Z_p\) forces a block-size multiplicity at least \(p\).
2. Lemma 2.1: exact semiregular development criterion.
3. Equations (11), (13), (14), and the lower bounds (15)–(19).
4. Theorem 4.1: every slope-pure affine-line refinement has multiplicity at least \(q^2/2\).
5. Uniform transversal blocks cannot be flattened by merely adding at most \(q\) cleanup points.
6. Lemma 6.1: exact fixed-point cleanup using disjoint domain partitions.
7. The stated RPDF existence hypothesis would imply the full Erdős problem for every sufficiently large \(n\).

**Plausible but unproved**

- Bounded-frequency direction-mixing partial difference families may exist when \(q\) and \(g\) are comparable.
- It is much less clear that they can also contain \(r\) disjoint domain partitions for every \(r<q\).

**Dead ends**

- Full cyclic development: fatal at prime order.
- Splitting affine slopes independently: fatal by Theorem 4.1.
- Restricting or refining affine lines while preserving a single slope per block: same obstruction.
- Starting from a uniform transversal design and using extra points merely to shift block sizes: still leaves \(\Omega(q^2)\) blocks of one of two adjacent sizes.
- Counting and Fourier constraints alone: compatible with bounded base multiplicity, so they do not resolve existence.

## Self-Audit

1. **The semiregular formulation covers only designs containing the point-orbits \(H\times\{i\}\) as blocks.** It is not a classification of all partially symmetric PBDs. The claims made within this subclass are nevertheless exact, because every pair type is checked directly in Lemma 2.1.

2. **The slope-pure no-go theorem relies on assigning every two-point block a unique affine slope.** Over a field this is valid: two points with distinct coordinate labels determine exactly one slope. For each fixed slope, the domain blocks really do form a PBD, so de Bruijn–Erdős applies without hidden assumptions.

3. **The all-\(n\) reduction depends on an unproved RPDF existence statement.** I do not assert that this hypothesis holds. Only the conditional implication is claimed, and its pair coverage and multiplicity estimates are completely checked. This unresolved hypothesis is precisely why the status is BLOCKED.

## Computations To Verify

The following CP-SAT search tests the central partial-difference-family problem for prime \(q\). Each candidate is normalized by setting its first value to \(0\), thereby selecting one representative from each vertical-translation orbit.

```python
from itertools import combinations, product
from ortools.sat.python import cp_model

def generate_candidates(q, g):
    """
    Candidate = (support_tuple, value_tuple, covered_cells).
    A covered cell is (i, j, d), i < j, where d=f(j)-f(i) mod q.
    """
    candidates = []

    for k in range(2, g + 1):
        for S in combinations(range(g), k):
            # Normalize f(S[0]) = 0.
            for tail in product(range(q), repeat=k - 1):
                vals = (0,) + tail
                f = dict(zip(S, vals))
                cover = []
                for i, j in combinations(S, 2):
                    d = (f[j] - f[i]) % q
                    cover.append((i, j, d))
                candidates.append((S, vals, tuple(cover)))

    return candidates

def solve_partial_difference_family(q, g, cap=None):
    C = generate_candidates(q, g)
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{j}") for j in range(len(C))]

    coverers = {
        (i, j, d): []
        for i in range(g)
        for j in range(i + 1, g)
        for d in range(q)
    }

    for idx, (_, _, cov) in enumerate(C):
        for cell in cov:
            coverers[cell].append(idx)

    # Every coordinate pair realizes every group difference exactly once.
    for cell, ids in coverers.items():
        model.Add(sum(x[j] for j in ids) == 1)

    M = model.NewIntVar(0, len(C), "M")
    for t in range(2, g + 1):
        count_t = sum(x[j] for j, (S, _, _) in enumerate(C) if len(S) == t)
        model.Add(count_t <= M)
        if cap is not None:
            model.Add(count_t <= cap)

    model.Minimize(M)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 3600
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    chosen = [j for j in range(len(C)) if solver.Value(x[j])]
    histogram = {}
    for j in chosen:
        t = len(C[j][0])
        histogram[t] = histogram.get(t, 0) + 1

    return {
        "M": solver.Value(M),
        "chosen_indices": chosen,
        "histogram": histogram,
        "candidates": C,
    }
```

To test the cleanup lemma, add variables \(y_{z,B}\) selecting the base blocks in the partition assigned to fixed point \(z\):

```python
def add_cleanup_constraints(model, x, candidates, q, g, r):
    y = {}
    for z in range(r):
        for j in range(len(candidates)):
            y[z, j] = model.NewBoolVar(f"y_{z}_{j}")
            model.Add(y[z, j] <= x[j])

    # No base-block orbit is assigned to two fixed points.
    for j in range(len(candidates)):
        model.Add(sum(y[z, j] for z in range(r)) <= x[j])

    # For each fixed point, selected domains partition the coordinate set.
    for z in range(r):
        for i in range(g):
            model.Add(
                sum(
                    y[z, j]
                    for j, (S, _, _) in enumerate(candidates)
                    if i in S
                ) == 1
            )

    return y
```

The final developed histogram can be optimized directly:

```python
def add_final_histogram_bound(
    model, x, y, candidates, q, g, r, L
):
    selected = []
    for j in range(len(candidates)):
        selected.append(sum(y[z, j] for z in range(r)))

    max_size = max(q, g + 1, r)

    for t in range(2, max_size + 1):
        unaugmented_t = sum(
            x[j] - selected[j]
            for j, (S, _, _) in enumerate(candidates)
            if len(S) == t
        )
        augmented_from_t_minus_1 = sum(
            selected[j]
            for j, (S, _, _) in enumerate(candidates)
            if len(S) + 1 == t
        )

        extra = 0
        if t == q:
            extra += g                  # The vertical group blocks.
        if r >= 2 and t == r:
            extra += 1                  # The fixed-point block.

        model.Add(
            q * (unaugmented_t + augmented_from_t_minus_1) + extra <= L
        )
```

A direct verifier for a chosen family is:

```python
from collections import Counter

def develop_and_check(q, g, chosen_candidates, owner=None, r=0):
    """
    owner[j] = z means candidate j is augmented by fixed point z.
    Candidate format: (support, values, covered_cells).
    """
    if owner is None:
        owner = {}

    blocks = []

    # Developed cross-blocks.
    for j, (S, vals, _) in enumerate(chosen_candidates):
        f = dict(zip(S, vals))
        for a in range(q):
            B = {i * q + ((a + f[i]) % q) for i in S}
            if j in owner:
                B.add(q * g + owner[j])
            blocks.append(B)

    # Vertical groups.
    for i in range(g):
        blocks.append({i * q + a for a in range(q)})

    # Fixed-point block.
    if r >= 2:
        blocks.append({q * g + z for z in range(r)})

    n = q * g + r
    pair_count = Counter()

    for B in blocks:
        assert 2 <= len(B) <= n - 1
        for u, v in combinations(sorted(B), 2):
            pair_count[u, v] += 1

    assert len(pair_count) == n * (n - 1) // 2
    assert all(pair_count[u, v] == 1 for u in range(n)
                                      for v in range(u + 1, n))

    hist = Counter(map(len, blocks))
    return blocks, hist
```

Concrete searches to run:

1. Compute the minimum base cap for
   \[
   (q,g)=(3,3),(5,5),(5,4),(7,7),(7,6).
   \]
2. For each feasible solution, test whether it admits \(r=1,\dots,q-1\) disjoint domain partitions.
3. Add the cap \(M=3,4,5,\dots\) successively. Persistent growth of the minimum \(M\) with \(q\) would refute the central Route 4 conjecture.
4. Classify solutions by the number of affine directions determined inside each row. This tests whether every low-cap solution must genuinely mix directions.
5. Verify the proved \(q=3\) construction:
   - full maps \(f(x)=0\) and \(f(x)=x\);
   - for every two-element support \(S\), the restriction \(f(x)=2x\).

## Route Diagnosis

Partial group symmetry is not intrinsically hopeless: after quotienting by an orbit group of order \(\Theta(\sqrt n)\), the desired global multiplicity becomes bounded base-row multiplicity, and the elementary lower bound is only \(3\). The route fails for every natural affine implementation, however. Treating slopes independently invokes a full PBD on the coordinate set for each slope and forces linear repetition; adding cleanup points to a uniform transversal design likewise cannot disperse enough blocks.

The only viable Route 4 subroute is therefore to construct partial difference matrices whose rows mix many secant directions and whose support sizes are globally flat. For all \(n\), these families additionally need many disjoint support partitions, or a different exact cleanup mechanism. No current argument constructs those objects, and the Fourier and counting conditions do not force them.

A fresh attempt should first run the stated CP-SAT search for \(q=5,7\). If bounded-cap examples appear, the next target is an algebraic composition theorem for these incomplete generalized Hadamard matrices. If the minimum cap grows already at small \(q\), Route 4 should be abandoned in favor of a nonsymmetric prescribed-clique decomposition with absorption.