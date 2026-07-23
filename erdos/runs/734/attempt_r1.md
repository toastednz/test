STATUS: BLOCKED

## Result

Route 1 is arithmetically viable but remains blocked at the integral-decomposition step. For every \(n\ge 36\), I construct an explicit multiset of clique orders \(2\le k_i\le \lfloor\sqrt n\rfloor\) such that every order occurs between \(3\lfloor\sqrt n\rfloor\) and \(3\lfloor\sqrt n\rfloor+18\) times and
\[
\sum_i\binom{k_i}{2}=\binom n2.
\]
Thus any edge-disjoint realization of this list would solve the problem with constant \(6\). The list also passes a strong per-block crossing-partition condition forced by every PBD, admits an exactly symmetric fractional decomposition, has fractional codegrees tending to zero, and admits an abstract incidence assignment whose pointwise weighted degrees are within \(O(\sqrt n)\) of the required value. However, I cannot round the fractional decomposition to an integral one. This is not a routine nibble issue: the auxiliary hyperedges have rank \(\Theta(n)\), and a sequential random-greedy process would leave a random-like residual graph containing no further \(\Theta(\sqrt n)\)-cliques. The required integral matching theorem is essentially the unresolved core of the original problem.

## Complete Argument

### 1. A bounded-denomination lemma

We first isolate the elementary arithmetic tool.

**Lemma 1.**  
Let
\[
1=a_1<a_2<\cdots<a_r
\]
be positive integers, and let \(M\ge1\). Suppose
\[
a_j\le 1+M\sum_{\ell<j}a_\ell
\qquad (2\le j\le r).
\tag{9}
\]
Then every integer
\[
0\le z\le M\sum_{j=1}^r a_j
\]
has a representation
\[
z=\sum_{j=1}^r c_j a_j,
\qquad 0\le c_j\le M,\quad c_j\in\mathbb Z.
\]

**Proof.** Induct on \(r\). For \(r=1\), the assertion is immediate because \(a_1=1\).

Let
\[
P=M\sum_{j<r}a_j.
\]
By induction, the smaller denominations represent every integer in \([0,P]\). For each \(q\in\{0,\ldots,M\}\), using \(q\) copies of \(a_r\) therefore represents the interval
\[
[qa_r,qa_r+P].
\]
Condition (9) says \(a_r\le P+1\), so consecutive such intervals meet or are adjacent. Their union is the full integer interval
\[
[0,Ma_r+P].
\]
This proves the induction step. \(\square\)

For the triangular denominations
\[
a_t=\binom t2,\qquad 2\le t\le L,
\]
we have
\[
\sum_{u=2}^{t-1}\binom u2=\binom t3.
\tag{10}
\]
Consequently, with \(M=18\),
\[
\binom t2\le 1+18\binom t3
\]
for every \(t\ge3\). Lemma 1 therefore applies.

---

### 2. An explicit flat prescribed size profile for every \(n\)

**Theorem 2.**  
Let \(n\ge9\), and put
\[
L=\lfloor\sqrt n\rfloor.
\]
There are integers \(b_t\), \(2\le t\le L\), such that
\[
3L\le b_t\le 3L+18
\tag{11}
\]
and
\[
\sum_{t=2}^L b_t\binom t2=\binom n2.
\tag{12}
\]
In particular, for \(n\ge36\),
\[
\max_t b_t\le6\sqrt n.
\tag{13}
\]

**Proof.** Write
\[
n=L^2+s,\qquad 0\le s\le2L.
\]
The hockey-stick identity gives
\[
\sum_{t=2}^L\binom t2=\binom{L+1}{3}
=\frac{L(L^2-1)}6.
\]
Therefore
\[
3L\sum_{t=2}^L\binom t2
=\frac{L^2(L^2-1)}2
=\binom{L^2}{2}.
\tag{14}
\]

It remains to represent the nonnegative difference
\[
R=\binom n2-\binom{L^2}{2}.
\]
Since \(n=L^2+s\),
\[
R=\frac{s(2L^2+s-1)}2.
\tag{15}
\]
Using \(s\le2L\),
\[
R\le 2L^3+2L^2-L.
\tag{16}
\]
On the other hand,
\[
18\binom{L+1}{3}=3L(L^2-1)=3L^3-3L.
\]
For \(L\ge3\),
\[
3L^3-3L-(2L^3+2L^2-L)
=L(L^2-2L-2)\ge0.
\]
Hence
\[
0\le R\le18\sum_{t=2}^L\binom t2.
\]
By Lemma 1, there are integers \(c_t\in[0,18]\) such that
\[
R=\sum_{t=2}^L c_t\binom t2.
\]
Set
\[
b_t=3L+c_t.
\]
Equations (12) and (11) follow from (14).

Finally, if \(n\ge36\), then \(L\ge6\), so
\[
b_t\le3L+18\le6L\le6\sqrt n.
\]
\(\square\)

This profile also has enough blocks to pass the de Bruijn–Erdős lower bound. Indeed,
\[
m=\sum_{t=2}^L b_t\ge3L(L-1).
\]
Because \(n\le L^2+2L\),
\[
3L(L-1)-n\ge2L^2-5L\ge0
\]
for \(L\ge3\). Thus \(m\ge n\).

For square orders the profile is especially simple:

\[
n=L^2
\quad\Longrightarrow\quad
b_2=b_3=\cdots=b_L=3L.
\tag{17}
\]

For example, when \(n=16\), the desired list is
\[
12K_2,\quad12K_3,\quad12K_4,
\]
whose total edge count is
\[
12(1+3+6)=120=\binom{16}{2}.
\]

If Theorem 2’s list could be decomposed edge-disjointly in \(K_n\), it would immediately solve the original problem with \(C=6\).

---

### 3. A necessary crossing-partition condition

Global pair counts and pointwise degree equations are not the only numerical constraints.

**Lemma 3.**  
Let \((A_i)\) be a PBD on \(n\) points, and fix a block \(B=A_i\) of size \(k\). The other block indices that meet \(B\) can be partitioned into \(k\) classes
\[
\mathcal C_y=\{j\ne i:y\in A_j\},
\qquad y\in B,
\]
such that
\[
\sum_{j\in\mathcal C_y}(|A_j|-1)=n-k
\qquad\text{for every }y\in B.
\tag{18}
\]
In particular,
\[
\sum_{j\ne i}(|A_j|-1)\ge k(n-k).
\tag{19}
\]

**Proof.** Fix \(y\in B\). For every \(z\notin B\), the pair \(\{y,z\}\) lies in a unique block \(A_j\ne B\). Distinct such blocks through \(y\) have disjoint sets \(A_j\setminus\{y\}\), since otherwise a pair \(\{y,z\}\) would be repeated. Moreover, none of these blocks contains another point of \(B\), because distinct blocks intersect in at most one point. Hence the sets
\[
A_j\setminus\{y\},\qquad j\in\mathcal C_y,
\]
partition the \(n-k\) points outside \(B\), proving (18).

If \(y,y'\in B\) are distinct, no block other than \(B\) can belong to both \(\mathcal C_y\) and \(\mathcal C_{y'}\). Thus these classes are pairwise disjoint. Summing (18) gives (19). \(\square\)

The profile from Theorem 2 passes even the full numerical partition condition in Lemma 3.

**Proposition 4.**  
Assume \(L=\lfloor\sqrt n\rfloor\ge7\), and let the list be the one from Theorem 2. Fix any one slot of size \(k\), \(2\le k\le L\). Using distinct other slots, one can form \(k\) disjoint classes, each having
\[
\sum_{\text{slot in class}}(\text{slot size}-1)=n-k.
\tag{20}
\]

**Proof.** Write \(n=L^2+s\), \(0\le s\le2L\), and use weights
\[
w=t-1,\qquad 1\le w\le L-1.
\]
There are at least \(3L\) slots of every weight.

Set
\[
d=s+L-k.
\]
Then
\[
n-k=L^2+s-k
=L(L-1)+d
=2\sum_{w=1}^{L-1}w+d.
\tag{21}
\]
Furthermore,
\[
0\le d\le3L-2.
\]
For \(L\ge7\),
\[
3L-2\le\sum_{w=1}^{L-1}w.
\]
Since \(1,2,\ldots,L-1\) is a complete sequence, \(d\) is the sum of a subset \(D\subseteq[L-1]\).

For each of the \(k\) desired classes, take two slots of every weight \(1,\ldots,L-1\), and one additional slot of each weight in \(D\). By (21), every class has weight \(n-k\).

Across all \(k\) classes, a weight is used at most \(3k\) times. If \(k<L\), then
\[
3k\le3L-3,
\]
so there remain enough of the \(3L\) baseline slots even after excluding the distinguished slot when its weight is considered.

If \(k=L\), then \(d=s\le2L\). For \(L\ge7\),
\[
2L\le\sum_{w=1}^{L-2}w,
\]
so \(D\) may be chosen to avoid weight \(L-1\). The distinguished size-\(L\) slot has weight \(L-1\); that weight is then used only \(2L\) times, at most \(3L-1\). Every other weight is used at most \(3L\) times.

Thus all slots can be chosen distinctly. \(\square\)

This is still only a test performed separately around each proposed block. It does not make the choices globally consistent.

---

### 4. Global and pointwise numerical feasibility are not sufficient

A small example demonstrates why a prescribed-list theorem cannot use only the pair equation, \(m\ge n\), and the pointwise equations.

Take \(n=7\) and the list
\[
2K_4,\quad 2K_3,\quad 3K_2.
\tag{22}
\]
It has \(m=7=n\) and
\[
2\binom42+2\binom32+3\binom22
=12+6+3=21=\binom72.
\]

There is also an abstract incidence assignment satisfying every pointwise equation. Put the two size-\(4\) slots on points \(1,2,3,4\). Put the two size-\(3\) slots on points \(5,6,7\), and put the three size-\(2\) slots on the three pairs among \(5,6,7\). Then points \(1,\ldots,4\) have weighted degree
\[
2(4-1)=6,
\]
and points \(5,6,7\) have weighted degree
\[
2(3-1)+2(2-1)=6=n-1.
\]

Nevertheless, no PBD with this list exists. Indeed,
\[
W=\sum_i(k_i-1)=2\cdot3+2\cdot2+3\cdot1=13.
\]
For a size-\(4\) block, Lemma 3 would require
\[
W-(4-1)\ge4(7-4)=12,
\]
but the left side is \(10\).

Thus even exact local degree data do not encode the geometric intersection constraints.

---

### 5. A near-balanced integral incidence assignment

Although I cannot enforce pairwise intersections, the pointwise degree condition can be met within \(O(\sqrt n)\) by a simple deterministic procedure.

**Lemma 5.**  
Let \(k_1,\ldots,k_m\le L<n\) satisfy
\[
\sum_{i=1}^m k_i(k_i-1)=n(n-1).
\tag{23}
\]
Then there are subsets \(S_i\subseteq[n]\), \(|S_i|=k_i\), such that, for
\[
d_x=\sum_{i:x\in S_i}(k_i-1),
\]
one has
\[
|d_x-(n-1)|\le L-1
\qquad\text{for every }x.
\tag{24}
\]

**Proof.** Begin with all loads zero. Process the slots in any order. For a slot of size \(k\) and weight \(w=k-1\), choose the \(k\) currently least-loaded points and add \(w\) to their loads.

We claim that after every step the difference between the largest and smallest load is at most \(L-1\). Suppose the current loads are
\[
a_1\le\cdots\le a_n
\]
and the first \(k\) receive weight \(w\le L-1\). The new maximum is
\[
\max(a_n,a_k+w),
\]
and the new minimum is
\[
\min(a_1+w,a_{k+1}).
\]
If the new maximum is \(a_n\), the range is at most the old range. If it is \(a_k+w\), then according as the new minimum is \(a_1+w\) or \(a_{k+1}\), the new range is at most the old range or at most \(w\). The claim follows by induction.

At the end,
\[
\sum_xd_x=\sum_i k_i(k_i-1)=n(n-1),
\]
so the average load is \(n-1\). Since all loads lie in an interval of length at most \(L-1\), (24) follows. \(\square\)

For Theorem 2’s list this gives pointwise errors at most \(\sqrt n\). Eliminating those errors exactly while simultaneously enforcing pairwise intersections remains nontrivial.

---

### 6. An exact fractional decomposition and its codegrees

Let \(k_1,\ldots,k_m\) be any list satisfying
\[
\sum_i\binom{k_i}{2}=\binom n2.
\tag{25}
\]
Construct an auxiliary hypergraph \(H\) whose vertices are:

- one slot vertex \(i\) for each prescribed clique;
- one pair vertex for each \(e\in E(K_n)\).

For each \(i\) and each \(k_i\)-set \(S\subseteq[n]\), put in \(H\) the hyperedge
\[
\{i\}\cup E(K_n[S]).
\]
An integral matching using every slot is exactly an edge-disjoint realization of the prescribed cliques.

There is always a perfectly symmetric fractional matching.

**Lemma 6.**  
Assign to every auxiliary hyperedge belonging to slot \(i\) the weight
\[
x_{i,S}=\binom n{k_i}^{-1}.
\tag{26}
\]
Then the total weight incident with every auxiliary vertex is exactly \(1\).

**Proof.** For a slot vertex \(i\),
\[
\sum_{|S|=k_i}x_{i,S}=1.
\]
For a graph pair \(e\),
\[
\begin{aligned}
\sum_i\sum_{\substack{|S|=k_i\\e\subseteq S}}x_{i,S}
&=\sum_i\frac{\binom{n-2}{k_i-2}}{\binom n{k_i}}\\
&=\sum_i\frac{k_i(k_i-1)}{n(n-1)}\\
&=1
\end{aligned}
\]
by (25). \(\square\)

For the profile of Theorem 2, all \(k_i\le L\le\sqrt n\). The fractional co-loads are small:

- If two graph-pair vertices share one endpoint, their union has three points, and their co-load is at most
  \[
  \sum_i\frac{(k_i)_3}{(n)_3}
  \le \frac{L}{n-2}.
  \tag{27}
  \]
- If the two pairs are disjoint, their co-load is at most
  \[
  \sum_i\frac{(k_i)_4}{(n)_4}
  \le \frac{L^2}{(n-2)(n-3)}.
  \tag{28}
  \]
- The co-load of a slot \(i\) and a graph pair is
  \[
  \frac{(k_i)_2}{(n)_2}=O(n^{-1}).
  \tag{29}
  \]

For example, (27) follows from
\[
(k_i)_3\le L(k_i)_2
\]
and
\[
\sum_i(k_i)_2=(n)_2.
\]

Thus the fractional solution is highly spread: its largest co-load is \(O(n^{-1/2})\). The missing theorem would have to round this fractional perfect matching despite the fact that the auxiliary hyperedges have size
\[
1+\binom{k_i}{2}=\Theta(n)
\]
for the important slots. Standard fixed-rank matching and design theorems do not directly apply uniformly in this regime.

Moreover, selecting one auxiliary hyperedge for every slot is already enough: disjointness gives edge-disjoint cliques, and (25) says their total number of graph edges is exactly \(\binom n2\), so all graph-pair vertices are covered.

---

### 7. Why a naive random-greedy residual is unsuitable

The following rigorous observation explains one difficulty with an ordinary sequential nibble.

**Lemma 7.**  
Fix constants \(p,c>0\) with \(p<1\). Then
\[
G(n,p)
\]
contains no clique of order \(c\sqrt n\) with probability tending to \(1\).

**Proof.** Put \(k=\lceil c\sqrt n\rceil\). The expected number of \(K_k\)'s is at most
\[
\binom nk p^{\binom k2}
\le
\left(\frac{en}{k}\right)^k p^{k(k-1)/2}.
\]
Its logarithm is
\[
O(\sqrt n\log n)-\Omega(n)\longrightarrow-\infty.
\]
Hence the expectation tends to zero, and Markov's inequality completes the proof. \(\square\)

For the square profile \(n=L^2\), the blocks of orders up to \(\varepsilon L\) account for asymptotically an \(\varepsilon^3\) fraction of all graph edges:
\[
\frac{3L\sum_{t\le\varepsilon L}\binom t2}{\binom{L^2}{2}}
=\varepsilon^3+o(1).
\]
Thus if the larger blocks were packed first and the residual became random-like with constant edge density, it would contain no remaining clique of order \(\Theta(\sqrt n)\). A successful construction must keep the residual highly structured or choose all blocks simultaneously. This does not rule out a sophisticated nibble-plus-absorber, but it rules out treating graph-level pseudorandomness of the residual as the desired invariant.

---

### 8. One finite realization of the square profile

The square profile is realizable for \(L=3\), \(n=9\). Let the points be
\[
\mathbb F_3\times\mathbb F_3.
\]
For each \(a,b\in\mathbb F_3\), take the triple
\[
B_{a,b}=\{(g,ag+b):g\in\mathbb F_3\}.
\]
These nine triples cover every pair whose first coordinates are distinct exactly once. Add all three pairs inside each of the three groups
\[
\{g\}\times\mathbb F_3.
\]
These nine edges cover the remaining pairs. Hence
\[
b_2=b_3=9=3L,
\]
as prescribed by (17).

This is only a finite consistency check; the same transversal construction at larger orders has a concentrated block-size histogram.

---

## Self-Audit

1. **The fixed correction bound \(18\) is vulnerable to off-by-one errors.**  
   The critical facts are \(s\le2L\), formula (15), and
   \[
   R\le2L^3+2L^2-L\le3L^3-3L
   =18\binom{L+1}{3}
   \]
   for \(L\ge3\). These are explicit inequalities, and the reconstruction code below verifies them exactly.

2. **Proposition 4 is only a separate feasibility check around each block.**  
   Its choices cannot presently be made simultaneously for all blocks, so it gives no PBD. I believe the proposition itself because each class has the explicit weight representation (21), and the slot-capacity check separately handles the distinguished block’s missing slot.

3. **The route diagnosis depends partly on the absence of an applicable integral-rounding theorem.**  
   I have not proved that no theorem in the literature can handle this auxiliary hypergraph. What is rigorous is the exact fractional formulation, the codegree bounds, the growing rank, and the equivalence between the required integral matching and the desired prescribed decomposition. I therefore do not infer nonexistence; I mark the route blocked precisely at this rounding step.

## Computations To Verify

The following constructs the profile using the descending reconstruction implicit in Lemma 1.

```python
from math import isqrt, comb

def profile(n):
    assert n >= 9
    L = isqrt(n)
    R = comb(n, 2) - comb(L * L, 2)

    # Represent R using at most 18 copies of each triangular number.
    c = {t: 0 for t in range(2, L + 1)}
    rem = R

    for t in range(L, 1, -1):
        a = comb(t, 2)
        q = min(18, rem // a)
        c[t] = q
        rem -= q * a

    assert rem == 0
    b = {t: 3 * L + c[t] for t in range(2, L + 1)}

    assert all(3 * L <= b[t] <= 3 * L + 18 for t in b)
    assert sum(b[t] * comb(t, 2) for t in b) == comb(n, 2)
    assert sum(b.values()) >= n

    if n >= 36:
        assert max(b.values()) <= 6 * (n ** 0.5)

    return L, b

for n in range(9, 10000):
    profile(n)

print("All profiles verified.")
```

The per-block crossing-partition test can be checked as follows.

```python
def distinct_subset_sum(d, r):
    """Represent 0 <= d <= 1+...+r using distinct elements of [1,r]."""
    chosen = []
    for w in range(r, 0, -1):
        if w <= d:
            chosen.append(w)
            d -= w
    assert d == 0
    return set(chosen)

def verify_crossing_test(n):
    L, b = profile(n)
    assert L >= 7
    s = n - L * L

    for k in range(2, L + 1):
        d = s + L - k

        if k == L:
            D = distinct_subset_sum(d, L - 2)  # Avoid own weight L-1.
        else:
            D = distinct_subset_sum(d, L - 1)

        target = n - k
        one_class = 2 * sum(range(1, L)) + sum(D)
        assert one_class == target

        for w in range(1, L):
            used = k * (2 + (1 if w in D else 0))
            available = b[w + 1] - (1 if w == k - 1 else 0)
            assert used <= available

for n in range(49, 10000):
    verify_crossing_test(n)

print("Crossing tests verified.")
```

An exact CP-SAT search for the prescribed profile can test \(n=16\), and possibly \(n=25\).

```python
from itertools import combinations
from ortools.sat.python import cp_model

def solve_exact_profile(n, seconds=300):
    L, b = profile(n)
    points = range(n)
    pairs = list(combinations(points, 2))
    pair_id = {e: j for j, e in enumerate(pairs)}

    candidates = []
    candidate_pair_ids = []

    for t in range(2, L + 1):
        for S in combinations(points, t):
            candidates.append((t, S))
            candidate_pair_ids.append(
                [pair_id[e] for e in combinations(S, 2)]
            )

    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{j}") for j in range(len(candidates))]

    containing = [[] for _ in pairs]
    by_size = {t: [] for t in range(2, L + 1)}

    for j, ((t, S), edge_ids) in enumerate(zip(candidates,
                                               candidate_pair_ids)):
        by_size[t].append(x[j])
        for e_id in edge_ids:
            containing[e_id].append(x[j])

    for vars_for_pair in containing:
        model.Add(sum(vars_for_pair) == 1)

    for t in range(2, L + 1):
        model.Add(sum(by_size[t]) == b[t])

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8

    status = solver.Solve(model)
    print("n =", n, "status =", solver.StatusName(status))

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        blocks = [
            candidates[j][1]
            for j in range(len(candidates))
            if solver.Value(x[j])
        ]
        return blocks
    return None

# Recommended first tests:
# blocks9  = solve_exact_profile(9)
# blocks16 = solve_exact_profile(16)
# blocks25 = solve_exact_profile(25, seconds=3600)
```

The exact pointwise-incidence relaxation, without pair-intersection constraints, is:

```python
def solve_local_incidence(n, seconds=60):
    L, b = profile(n)
    slots = []
    for t in range(2, L + 1):
        slots += [t] * b[t]

    model = cp_model.CpModel()
    z = [
        [model.NewBoolVar(f"z_{i}_{x}") for x in range(n)]
        for i in range(len(slots))
    ]

    for i, t in enumerate(slots):
        model.Add(sum(z[i][x] for x in range(n)) == t)

    for x in range(n):
        model.Add(
            sum((slots[i] - 1) * z[i][x] for i in range(len(slots)))
            == n - 1
        )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8
    status = solver.Solve(model)
    print("Local incidence:", n, solver.StatusName(status))
    return status
```

An infeasible result for the exact-profile solver would refute only that particular profile, not the Erdős problem. An infeasible local-incidence result would identify an additional arithmetic obstruction and should be investigated before further decomposition searches.

## Route Diagnosis

**Proved ledger.**

- A uniform bounded-coin lemma.
- For every \(n\ge9\), an exact prescribed histogram with
  \[
  3\lfloor\sqrt n\rfloor\le b_t
  \le3\lfloor\sqrt n\rfloor+18
  \]
  for every \(2\le t\le\lfloor\sqrt n\rfloor\).
- This histogram has the exact pair count, \(m\ge n\), and cap \(6\sqrt n\) for \(n\ge36\).
- The histogram passes the strong per-block crossing-partition condition of Lemma 3.
- Every globally feasible prescribed list has an exact symmetric fractional decomposition.
- For the constructed profile, fractional codegrees are \(O(n^{-1/2})\).
- An integral abstract incidence assignment can make all pointwise weighted degrees accurate within \(\sqrt n\).
- The square profile is genuinely realizable at \(n=9\).

**Plausible but unproved.**

- The profile \(b_t=3L\) for \(n=L^2\), or a nearby profile, may admit exact decompositions for all sufficiently large \(L\).
- A simultaneous randomized matching method guided by an algebraic or pre-existing linear-space template may round the fractional solution.
- A suitable absorber might correct both uncovered graph pairs and prescribed slot sizes, but no absorber with these growing clique orders has been constructed here.

**Dead ends.**

- Pair count, \(m\ge n\), and pointwise degree equations are insufficient; example (22) demonstrates this.
- A sequential random-greedy process that tries to leave a graph-level pseudorandom residual is incompatible with having \(\Theta(\sqrt n)\)-cliques still to place.
- Fixed-rank nibble or design-existence theorems cannot simply be quoted, because the relevant auxiliary rank is \(\Theta(n)\).
- Refining each line of a uniform finite geometry separately creates at least \(\Theta(n^{3/2})\) child blocks and forces some size to repeat \(\Theta(n)\) times.

**Precise block.**  
The remaining step is to prove that the auxiliary hypergraph in Section 6 has a perfect matching for the explicit profile of Theorem 2. This is an exact clique-decomposition theorem with clique orders up to \(\sqrt n\). At present that statement is of essentially the same strength as the original problem, so Route 1 is blocked rather than completed.

A fresh Route 1 attempt should focus on a **structured simultaneous rounding theorem**, not an ordinary residual nibble. The immediate computational priorities are the square profiles
\[
n=16:\quad b_2=b_3=b_4=12,
\]
and
\[
n=25:\quad b_2=b_3=b_4=b_5=15.
\]
If these are feasible, extracted solutions should be mined for repeatable clique trades or an algebraic template. If they are infeasible, one should optimize over the \(18\)-copy correction freedom and identify which stronger intersection constraints exclude them.