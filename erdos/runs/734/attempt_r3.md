STATUS: BLOCKED

## Result

Route 3 does not presently yield a solution. I proved three rigorous obstructions: independent recursive refinement cannot reduce a repeated parent block size by more than a factor asymptotically \(2\); every uniform-weight Wilson fundamental construction has multiplicity \(\gg\max\{v,g^2\}\) on \(N=vg\) points and therefore cannot satisfy \(O(\sqrt N)\) for unbounded \(N\); and dense truncations of transversal designs retain the same \(q^2/\sqrt{k}\) concentration obstruction as finite-plane restrictions. Unequal weights remain viable, and I reduce that surviving case to a precise GDD problem with pairwise distinct group sizes. That GDD problem would solve Erdős #734 immediately, but it is an exact growing-clique decomposition problem of comparable strength, so the route is blocked rather than solved.

## Complete Argument

### 1. Independent block refinement cannot disperse frequencies

Suppose a clique \(K_B\), \(|B|=k\), is recursively refined into smaller cliques. At the end, the leaf blocks contained in \(B\) form a clique decomposition of \(K_B\), hence a PBD on \(B\). It is either:

1. the trivial one-block decomposition \(\{B\}\); or
2. a nontrivial PBD on \(k\) points, containing at least \(k\) blocks by de Bruijn–Erdős, all of sizes \(2,\dots,k-1\).

This observation gives a quantitative obstruction.

#### Lemma 1: refinement obstruction

Let a parent PBD contain \(R\) blocks of some fixed size \(k\). Replace each parent block, through any number of recursive refinement levels, by a clique decomposition of that parent clique. Let \(M\) be the maximum final block-size multiplicity.

If \(k=2\), then
\[
M\ge R.
\]
If \(k\ge3\), then
\[
M\ge \frac{k}{2(k-1)}R\ge\frac R2.
\tag{9}
\]

#### Proof

A \(2\)-clique cannot be nontrivially decomposed, proving the first assertion.

Now let \(k\ge3\). Among the \(R\) parent \(k\)-blocks, suppose \(u\) remain as single final \(k\)-blocks and \(R-u\) are nontrivially decomposed.

The retained blocks give
\[
M\ge u.
\tag{10}
\]

Each of the other \(R-u\) parent blocks gives at least \(k\) final blocks, all with sizes in the \(k-2\) element set
\[
\{2,\dots,k-1\}.
\]
Thus some such size occurs at least
\[
\frac{k(R-u)}{k-2}
\]
times, and hence
\[
M\ge \max\left\{u,\frac{k(R-u)}{k-2}\right\}.
\tag{11}
\]

The minimum over real \(u\in[0,R]\) occurs when the two terms are equal:
\[
u=\frac{k(R-u)}{k-2},
\]
which gives
\[
u=\frac{kR}{2(k-1)}.
\]
This proves (9). ∎

#### Consequences

If \(\mathcal A'\) is obtained solely by recursively refining blocks of a master PBD \(\mathcal A\), then
\[
\max_t b_t(\mathcal A')
\ge \frac12\max_t b_t(\mathcal A).
\tag{12}
\]

Thus:

- refining all affine-plane lines still leaves multiplicity \(\Omega(n)\);
- refining all projective-plane lines still leaves multiplicity \(\Omega(n)\);
- choosing different ingredients for different repeated parent blocks does not evade the obstruction.

For example, for \(R\) triangles, retaining \(u\) triangles and refining the rest gives \(u\) blocks of size \(3\) and \(3(R-u)\) edges. The optimum balance is \(u\approx3R/4\), agreeing with (9).

This rules out the simplest interpretation of Route 3 completely.

---

### 2. A rank lower bound for GDD ingredients

A group-divisible design, or GDD, has groups \(G_1,\dots,G_k\), blocks meeting each group in at most one point, and every pair from different groups in exactly one block.

#### Lemma 2: number of blocks in a GDD

Let the group sizes be
\[
w_i=|G_i|,\qquad W=\sum_{i=1}^k w_i,
\]
where \(k\ge2\) and every \(w_i\ge1\). If the GDD has \(L\) blocks, then
\[
L\ge W-k=\sum_{i=1}^k(w_i-1).
\tag{13}
\]
Moreover,
\[
L\ge \max_{i<j}w_iw_j.
\tag{14}
\]

#### Proof

For (14), fix two groups \(G_i,G_j\). There are \(w_iw_j\) pairs with one endpoint in each group. Every block contains at most one such pair, so at least \(w_iw_j\) blocks are required.

For (13), let \(A\) be the \(W\times L\) incidence matrix. If \(r_p\) is the number of blocks through point \(p\), then
\[
AA^{\mathsf T}
=
D+J_W-\bigoplus_{i=1}^kJ_{w_i},
\tag{15}
\]
where \(D=\operatorname{diag}(r_p)\).

Let
\[
U=\left\{z\in\mathbb R^W:
\sum_{p\in G_i}z_p=0\text{ for every }i\right\}.
\]
Then \(\dim U=W-k\). For \(z\in U\),
\[
z^{\mathsf T}
\left(J_W-\bigoplus_iJ_{w_i}\right)z
=
\left(\sum_pz_p\right)^2
-\sum_i\left(\sum_{p\in G_i}z_p\right)^2
=0.
\]
Every point has positive replication because there is at least one other group, so
\[
z^{\mathsf T}AA^{\mathsf T}z
=\sum_pr_pz_p^2>0
\]
for every nonzero \(z\in U\). Hence the kernel of \(AA^{\mathsf T}\) intersects \(U\) trivially. Therefore
\[
\operatorname{rank}(AA^{\mathsf T})\ge W-k.
\]
Since
\[
\operatorname{rank}(AA^{\mathsf T})\le\operatorname{rank}(A)\le L,
\]
equation (13) follows. ∎

---

### 3. Uniform Wilson inflation is quantitatively impossible

Consider the standard uniform Wilson construction:

1. take a nontrivial master PBD \(\mathcal B\) on \(v\) points;
2. replace every master point by a group of size \(g\ge2\);
3. for every master block \(B\), insert a GDD of type \(g^{|B|}\);
4. fill each of the \(v\) groups by an arbitrary clique decomposition.

The final order is
\[
N=vg.
\]

#### Theorem 3: uniform-inflation obstruction

Let \(M\) be the maximum final block-size multiplicity. Then
\[
M\ge\max\left\{\frac v2,\;g^2\right\}.
\tag{16}
\]
Consequently, if
\[
M\le C\sqrt N
\]
for a fixed \(C\), then
\[
N\le16C^6.
\tag{17}
\]
In particular, uniform Wilson inflation cannot solve the problem for an unbounded sequence of orders.

#### Proof

First consider the blocks covering pairs inside the \(v\) groups. These form \(v\) independent clique decompositions of \(K_g\). Applying Lemma 1 with \(R=v\) and \(k=g\) gives
\[
M\ge\frac{gv}{2(g-1)}\ge\frac v2
\]
when \(g\ge3\). For \(g=2\), every group contributes its unique edge, so \(M\ge v\), which is stronger.

Now consider the cross-group ingredients. Every ingredient of type \(g^{|B|}\) contains at least \(g^2\) blocks by (14). The master PBD has at least \(v\) blocks. Hence the total number of cross-group blocks is at least
\[
vg^2.
\]
Because the master is nontrivial, every master block has size at most \(v-1\), so every cross-group block has size in
\[
\{2,\dots,v-1\}.
\]
There are \(v-2\) possible sizes, and therefore
\[
M\ge\frac{vg^2}{v-2}\ge g^2.
\]
This proves (16).

If \(M\le C\sqrt{vg}\), the internal-group lower bound gives
\[
\frac v2\le C\sqrt{vg},
\]
and hence
\[
v\le4C^2g.
\tag{18}
\]
The cross-group lower bound gives
\[
g^2\le C\sqrt{vg},
\]
so
\[
g^3\le C^2v.
\tag{19}
\]
Combining (18) and (19),
\[
g^3\le4C^4g,
\]
whence
\[
g\le2C^2.
\]
Equation (18) then yields
\[
v\le8C^4.
\]
Thus
\[
N=vg\le16C^6.
\]
∎

This obstruction persists through arbitrary recursive fillings of the top-level groups: Lemma 1 already allowed arbitrary final clique decompositions inside each group.

---

### 4. What unequal weights must satisfy

Uniform weights are therefore unusable. Let the master points \(x\) instead have positive weights \(w_x\), and write
\[
N=\sum_xw_x.
\]

For an integer \(g\ge2\), let
\[
R_g=\#\{x:w_x=g\}.
\]
The blocks covering pairs internal to these \(R_g\) groups satisfy Lemma 1. Consequently,
\[
M\ge
\begin{cases}
R_2,&g=2,\\[2mm]
\dfrac{gR_g}{2(g-1)},&g\ge3.
\end{cases}
\tag{20}
\]
Thus equal group sizes themselves cannot occur much more than \(O(\sqrt N)\) times. Pairwise distinct weights avoid this particular obstruction.

There is also a cumulative obstruction for the cross-group ingredients. For a master block \(B\), put
\[
k_B=|B|,\qquad W_B=\sum_{x\in B}w_x.
\]
Let \(L_B\) be the number of blocks in its GDD ingredient. Lemma 2 gives
\[
L_B\ge
\max\left\{
W_B-k_B,\;
\max_{\substack{x,y\in B\\x\ne y}}w_xw_y
\right\}.
\tag{21}
\]

Every block in this ingredient has size at most \(k_B\). Therefore, for every \(s\ge2\), all ingredients with \(k_B\le s\) collectively use only the sizes \(2,\dots,s\). It follows that
\[
M\ge
\frac1{s-1}
\sum_{\substack{B\in\mathcal B\\k_B\le s}}L_B.
\tag{22}
\]
Combining (21) and (22),
\[
M\ge
\frac1{s-1}
\sum_{\substack{B\in\mathcal B\\k_B\le s}}
\max\left\{
W_B-k_B,\;
\max_{x\ne y\in B}w_xw_y
\right\}.
\tag{23}
\]

Equation (23) is a necessary cumulative condition for any proposed unequal-weight Wilson construction. In particular, merely choosing all group sizes differently is insufficient: the master blocks must also distribute large weight products among ingredients with sufficiently broad size spectra.

---

### 5. Dense truncated transversal designs remain too concentrated

The most natural unequal-weight GDD ingredient is obtained by truncating a transversal design.

Let \(\operatorname{TD}(k,q)\) have \(k\) groups of size \(q\) and \(q^2\) transversal blocks. Retain an arbitrary set of \(w_i\) points from group \(i\), and intersect every transversal block with the retained points.

For an original transversal block \(L\), let
\[
T_L=|L\cap S|,
\]
where \(S\) is the retained point set. Put
\[
p_i=\frac{w_i}{q},\qquad \mu=\sum_{i=1}^kp_i.
\]

#### Lemma 4: exact variance identity

For uniformly random \(L\),
\[
\mathbb E T_L=\mu
\]
and
\[
\operatorname{Var}(T_L)
=\sum_{i=1}^kp_i(1-p_i)
\le\frac k4.
\tag{24}
\]

#### Proof

Let \(I_i\) indicate that the point where \(L\) meets group \(i\) was retained. Every point of a group occurs in exactly \(q\) transversal blocks, so
\[
\mathbb P(I_i=1)=p_i.
\]
For \(i\ne j\), every ordered pair of points from groups \(i,j\) lies in exactly one transversal block. Thus
\[
\mathbb P(I_i=I_j=1)=p_ip_j.
\]
The indicators \(I_i,I_j\) are therefore pairwise independent. Since
\[
T_L=\sum_iI_i,
\]
the variance is the sum of the individual variances, proving (24). ∎

Let
\[
h_t=\#\{L:T_L=t\}.
\]

#### Corollary 5: concentration in the dense regime

If
\[
\mu\ge2+\sqrt{k},
\tag{25}
\]
then
\[
\max_{t\ge2}h_t
\ge
\frac{3q^2}{4(2\sqrt{k}+1)}.
\tag{26}
\]

#### Proof

Write \(\sigma^2=\operatorname{Var}(T_L)\). If \(\sigma=0\), all \(q^2\) blocks have the same intersection size and the conclusion is immediate.

Otherwise, Chebyshev's inequality gives
\[
\mathbb P(|T_L-\mu|<2\sigma)\ge\frac34.
\]
By (24),
\[
2\sigma\le\sqrt{k}.
\]
Under (25), every integer in this central interval is at least \(2\). The interval contains at most
\[
4\sigma+1\le2\sqrt{k}+1
\]
integer values. At least \(3q^2/4\) blocks are distributed among these values, giving (26). ∎

At the natural Wilson scale
\[
q=\Theta(k),\qquad \mu=\Theta(k),
\]
the retained order is
\[
W=\sum_iw_i=q\mu=\Theta(q^2),
\]
while (26) gives a repeated size at least
\[
\Omega\!\left(\frac{q^2}{\sqrt{k}}\right)
=\Omega(q^{3/2})
=\Omega(W^{3/4}).
\]
This is much larger than the desired \(O(\sqrt W)=O(q)\).

The hypothesis (25) is essential. Very sparse truncations may have most intersections of size \(0\) or \(1\), so this lemma alone does not rule them out. Such sparse truncations, however, offer only small block sizes and do not by themselves provide the \(\Theta(\sqrt N)\) useful size range.

---

### 6. The exact surviving GDD problem

There is a clean way to eliminate the group-filling frequency problem entirely.

For a given \(n\), let \(k\) be maximal such that
\[
\frac{k(k+1)}2\le n,
\]
and write
\[
r=n-\frac{k(k+1)}2,\qquad 0\le r\le k.
\]
Partition the point set into \(k\) groups of sizes
\[
1,2,\dots,k-1,k+r.
\tag{27}
\]
These sizes are pairwise distinct, and
\[
k=\Theta(\sqrt n).
\]

Suppose one could decompose all edges between distinct groups into cliques, each meeting a group in at most one point, such that
\[
\max_t b_t^{\mathrm{cross}}\le C\sqrt n.
\tag{28}
\]
Adding each group of size at least \(2\) as a single block would then give a PBD on \(n\) points. Because the group sizes are distinct, this adds at most one block of any given size. Thus
\[
\max_t b_t\le C\sqrt n+1.
\]
All pairs are covered exactly once: cross-group pairs by the GDD, and within-group pairs by the group blocks.

This proves the following exact reduction.

#### Proposition 6

Erdős Problem #734 would follow from the assertion that, for every sufficiently large \(n\), the complete multipartite graph with part sizes (27) admits a clique decomposition satisfying (28).

The numerical scale is feasible. Here
\[
\sum_iw_i^2=O(k^3)=O(n^{3/2}),
\]
so the number of cross edges is
\[
\binom n2-\sum_i\binom{w_i}{2}
=\frac{n^2}{2}+O(n^{3/2}).
\]
The rank bound gives at least
\[
n-k=\Theta(n)
\]
cross blocks. There are \(k-1=\Theta(\sqrt n)\) available cross-block sizes, so a cap of order \(\sqrt n\) has total capacity \(\Theta(n)\), exactly the necessary scale.

No known Wilson ingredient theorem supplies Proposition 6: its block orders grow like \(k=\Theta(\sqrt n)\), and its required histogram cap is sharp. Adding the distinct groups as blocks also shows why this is a problem of comparable strength, not a routine recursive subproblem.

---

### 7. Ledger

**Proved lemmas**

1. Recursive independent refinement preserves at least half of every repeated parent-size frequency.
2. A GDD with group sizes \(w_1,\dots,w_k\) has at least \(W-k\) blocks and at least \(\max_{i<j}w_iw_j\) blocks.
3. Uniform-weight Wilson inflation cannot satisfy a fixed \(C\sqrt N\) cap for \(N>16C^6\).
4. Unequal-weight Wilson constructions satisfy the cumulative lower bound (23).
5. Dense truncated transversal-design ingredients have multiplicity \(\Omega(q^2/\sqrt{k})\).
6. A flat GDD for the distinct group sizes (27) would solve the original problem for every sufficiently large \(n\).

**Plausible but unproved**

- The multipartite graph in Proposition 6 may admit a prescribed variable-clique decomposition with \(O(\sqrt n)\) copies of every size.
- A sufficiently rich family of trades might couple many transversal decompositions and defeat the variance obstruction of any one transversal design.
- A growing-parameter absorption theorem may apply to the multipartite formulation.

**Dead ends**

- Refining affine or projective lines independently: killed by Lemma 1.
- Reusing a fixed ingredient library: repeated count vectors align linearly.
- Uniform Wilson inflation: killed by Theorem 3.
- Dense truncation of a single transversal design: killed by Corollary 5.
- Making all group sizes distinct without a new cross-group GDD theorem: removes only the group-filling concentration, not the principal exact-decomposition problem.

## Self-Audit

1. **The obstructions do not cover arbitrary unequal-weight Wilson constructions.** This is the main limitation and the reason for the `BLOCKED` status. The surviving case is isolated explicitly in Proposition 6 rather than silently assumed impossible.

2. **Lemma 1 relies on de Bruijn–Erdős for each nontrivial child decomposition.** This application is valid because the final leaves inside a parent block cover every parent pair exactly once and are therefore a nontrivial PBD on exactly \(k\) points.

3. **The transversal-design concentration result applies only when \(\mu\ge2+\sqrt{k}\).** Sparse truncations are not ruled out. The stated dense-regime conclusion nevertheless follows from exact pairwise independence and Chebyshev's inequality, with no heuristic probabilistic step.

## Computations To Verify

The following CP-SAT search computes the smallest possible histogram maximum for a GDD with prescribed group sizes. It directly tests the unresolved multipartite ingredients.

```python
from itertools import product
from collections import Counter
from ortools.sat.python import cp_model

def optimize_gdd(weights, time_limit=300):
    """
    Groups are indexed 0,...,k-1.
    A candidate block chooses either no point (-1) or one local point
    from each group, with support at least 2.
    Group blocks are then added to the objective as in Proposition 6.
    """
    k = len(weights)

    candidates = []
    for choice in product(*[[-1] + list(range(w)) for w in weights]):
        support = tuple(i for i, a in enumerate(choice) if a >= 0)
        if len(support) >= 2:
            candidates.append(choice)

    pair_to_candidates = {}
    for i in range(k):
        for j in range(i + 1, k):
            for a in range(weights[i]):
                for b in range(weights[j]):
                    pair_to_candidates[(i, a, j, b)] = []

    for idx, block in enumerate(candidates):
        supp = [i for i, a in enumerate(block) if a >= 0]
        for pos, i in enumerate(supp):
            for j in supp[pos + 1:]:
                pair_to_candidates[(i, block[i], j, block[j])].append(idx)

    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{i}") for i in range(len(candidates))]

    for pair, idxs in pair_to_candidates.items():
        model.Add(sum(x[j] for j in idxs) == 1)

    max_size = max(k, max(weights))
    group_hist = Counter(w for w in weights if w >= 2)

    M = model.NewIntVar(0, len(candidates) + len(weights), "M")
    for t in range(2, max_size + 1):
        cross = sum(
            x[i] for i, B in enumerate(candidates)
            if sum(a >= 0 for a in B) == t
        )
        model.Add(cross + group_hist[t] <= M)

    model.Minimize(M)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None

    selected = [
        candidates[i] for i in range(len(candidates))
        if solver.Value(x[i])
    ]
    hist = Counter(sum(a >= 0 for a in B) for B in selected)
    final_hist = hist + group_hist

    return {
        "M": solver.Value(M),
        "cross_histogram": dict(sorted(hist.items())),
        "final_histogram": dict(sorted(final_hist.items())),
        "blocks": selected,
        "optimal": status == cp_model.OPTIMAL,
    }

# Small triangular instances:
for weights in ([1, 2, 3], [1, 2, 4], [1, 2, 3, 4]):
    print(weights, optimize_gdd(weights, time_limit=60))
```

The exact moment calculation for truncated affine transversal designs can be checked as follows. This constructs \(\operatorname{TD}(k,q)\) for prime \(q\).

```python
from collections import Counter

def td_truncation_histogram(q, k, kept):
    """
    q must be prime, k <= q.
    Group i consists of points (i,y), y in F_q.
    Block (a,b) contains (i, a*i+b) for every i.
    kept[i] is a set of retained y-values in group i.
    """
    assert k <= q
    assert len(kept) == k

    values = []
    for a in range(q):
        for b in range(q):
            t = sum(((a * i + b) % q) in kept[i] for i in range(k))
            values.append(t)

    hist = Counter(t for t in values if t >= 2)
    empirical_mean = sum(values) / (q * q)
    empirical_var = sum(
        (t - empirical_mean) ** 2 for t in values
    ) / (q * q)

    p = [len(S) / q for S in kept]
    theoretical_mean = sum(p)
    theoretical_var = sum(x * (1 - x) for x in p)

    assert abs(empirical_mean - theoretical_mean) < 1e-9
    assert abs(empirical_var - theoretical_var) < 1e-9

    return {
        "histogram": dict(sorted(hist.items())),
        "max_multiplicity": max(hist.values(), default=0),
        "mean": empirical_mean,
        "variance": empirical_var,
        "chebyshev_lower_bound":
            3 * q * q / (4 * (2 * (k ** 0.5) + 1))
    }

# Dense example:
q = 11
k = 11
kept = [set(range(8)) for _ in range(k)]
print(td_truncation_histogram(q, k, kept))

# Sparse example showing why the density hypothesis is needed:
kept_sparse = [{0} for _ in range(k)]
print(td_truncation_histogram(q, k, kept_sparse))
```

The elementary Wilson lower bounds can be evaluated before attempting any ingredient search.

```python
from collections import Counter
from fractions import Fraction
from math import ceil

def wilson_necessary_bounds(master_blocks, weights):
    """
    master_blocks: list of lists/tuples of master-point indices.
    weights[x]: positive group size.
    """
    group_counts = Counter(weights)

    internal = Fraction(0, 1)
    for g, R in group_counts.items():
        if g == 2:
            internal = max(internal, Fraction(R, 1))
        elif g >= 3:
            internal = max(internal, Fraction(g * R, 2 * (g - 1)))

    data = []
    for B in master_blocks:
        k = len(B)
        W = sum(weights[x] for x in B)
        max_product = max(
            weights[B[i]] * weights[B[j]]
            for i in range(k) for j in range(i + 1, k)
        )
        L = max(W - k, max_product)
        data.append((k, L))

    cumulative = Fraction(0, 1)
    K = max(k for k, _ in data)
    for s in range(2, K + 1):
        total = sum(L for k, L in data if k <= s)
        cumulative = max(cumulative, Fraction(total, s - 1))

    return {
        "internal_lower_bound": ceil(internal),
        "cross_cumulative_lower_bound": ceil(cumulative),
        "combined_lower_bound": ceil(max(internal, cumulative)),
    }
```

## Route Diagnosis

Block refinement, the most direct form of Route 3, is definitively ineffective: it cannot flatten a bad master histogram by more than a constant factor. Uniform Wilson inflation is even more strongly excluded. Unequal weights are the only surviving Wilson mechanism, but after choosing distinct group sizes to eliminate internal concentration, the unresolved task is Proposition 6—a sharp exact decomposition of a dense complete multipartite graph into growing cliques. That is essentially Route 1 with prescribed holes and is of comparable strength to the original problem. A fresh attempt should therefore focus on a new growing-parameter multipartite clique-decomposition theorem, probably using random greedy packing plus absorption and trades that couple many transversal classes. Further work with standard fixed-size GDD libraries or independent refinements is unlikely to help.