STATUS: BLOCKED

## Result

I proved the full lower-bound half of the \(r=7\) conjecture, for every \(k\):
\[
f(k,7)\ge \left\lceil\frac{3k}{4}\right\rceil.
\]
The construction is the complete \(k\)-uniform hypergraph on \(k+\lfloor(3k-1)/4\rfloor\) vertices. A sharp seven-block incidence lemma explains the constant \(3/4\), with equality witnessed by the Fano plane. On the upper-bound side, the dual formulation yields a rigorous fractional theorem
\[
\tau^*(\mathcal H)\le (35k)^{1/3},
\]
and consequently an integral bound \(O(k^{1/3}\log |E|)\) for finite families. I also give an exact reduction of the non-intersecting case to a bipartite five-local “cross-transversal” theorem. However, neither the fractional estimate nor that reduction controls the large integrality gap required for a \((3/4+o(1))k\) integral upper bound. Thus the main problem remains blocked.

## Complete Argument

### 1. A sharp incidence lemma for seven covering blocks

We first isolate the mechanism producing the constant \(3/4\).

**Lemma 1.**  
Let \(C_1,\dots,C_s\subseteq[n]\), where \(1\le s\le7\) and \(|C_i|\le q\). Suppose every two-element subset of \([n]\) is contained in at least one \(C_i\). Then
\[
q\ge \frac{3n}{7}.
\]

**Proof.**  
For each \(x\in[n]\), define its incidence mask
\[
I(x)=\{i\in[s]:x\in C_i\}\subseteq[s].
\]
The hypothesis says that for distinct \(x,y\in[n]\),
\[
I(x)\cap I(y)\ne\varnothing.
\tag{1}
\]

If some \(x\) satisfies \(|I(x)|\le2\), then every \(y\ne x\) belongs to at least one \(C_i\) with \(i\in I(x)\), by (1). Therefore
\[
\sum_{i\in I(x)}|C_i|\ge n.
\]
If \(|I(x)|=1\), this gives \(q\ge n\). If \(|I(x)|=2\), it gives \(2q\ge n\). In either case,
\[
q\ge \frac n2\ge \frac{3n}{7}.
\]
The case \(I(x)=\varnothing\) is impossible when \(n\ge2\).

It remains to consider the case \(|I(x)|\ge3\) for every \(x\). Double-counting incidences gives
\[
sq\ge \sum_{i=1}^s|C_i|
 =\sum_{x\in[n]}|I(x)|
 \ge3n.
\]
Since \(s\le7\), it follows that
\[
q\ge \frac{3n}{s}\ge\frac{3n}{7}.
\]
This proves the lemma. \(\square\)

The lemma is asymptotically sharp. When \(n=7m\) and \(q=3m\), partition \([n]\) into seven equal classes indexed by the points of the Fano plane. For each of the seven Fano lines, take the union of its three classes. Every pair of vertices lies together in at least one of these seven sets, and each set has size \(3m\).

---

### 2. The complete-hypergraph construction

For a given \(k\), put
\[
q=\left\lfloor\frac{3k-1}{4}\right\rfloor,
\qquad
n=k+q,
\]
and let
\[
\mathcal H_k=\binom{[n]}{k}
\]
be the family of all \(k\)-subsets of \([n]\).

Because \(4q<3k\), we have
\[
7q<3(k+q)=3n,
\qquad\text{so}\qquad
q<\frac{3n}{7}.
\tag{2}
\]

**Lemma 2.**  
The hypergraph \(\mathcal H_k\) satisfies \((P_7)\).

**Proof.**  
Choose \(s\le7\) edges \(A_1,\dots,A_s\in\mathcal H_k\), and set
\[
C_i=[n]\setminus A_i.
\]
Then \(|C_i|=q\).

Suppose no two distinct vertices \(x,y\in[n]\) meet all the \(A_i\). Then for every pair \(\{x,y\}\), there is some \(i\) for which
\[
\{x,y\}\cap A_i=\varnothing,
\]
equivalently,
\[
\{x,y\}\subseteq C_i.
\]
Thus the sets \(C_1,\dots,C_s\) cover every pair of vertices. By Lemma 1,
\[
q\ge\frac{3n}{7},
\]
contradicting (2). Hence some pair meets all selected edges. \(\square\)

**Lemma 3.**  
The transversal number of \(\mathcal H_k\) is
\[
\tau(\mathcal H_k)=q+1=\left\lceil\frac{3k}{4}\right\rceil.
\]

**Proof.**  
If \(|T|\le q=n-k\), then
\[
|[n]\setminus T|\ge k,
\]
so there is a \(k\)-set disjoint from \(T\). Thus \(T\) is not a transversal.

Conversely, if \(|T|=q+1=n-k+1\), then its complement has size \(k-1\), so no \(k\)-set can be disjoint from \(T\). Hence \(T\) is a transversal. Therefore
\[
\tau(\mathcal H_k)=q+1.
\]
The identity with \(\lceil3k/4\rceil\) follows directly from the definition of \(q\). \(\square\)

Consequently,
\[
\boxed{f(k,7)\ge \left\lceil\frac{3k}{4}\right\rceil}
\]
for every \(k\). In particular,
\[
\liminf_{k\to\infty}\frac{f(k,7)}k\ge\frac34.
\]

The strict inequality \(4q<3k\) is essential for this complete-family construction. If \(k=4m\), \(n=7m\), and \(q=3m\), the Fano blow-up described after Lemma 1 gives seven complements covering every pair, so the corresponding seven \(4m\)-sets have no two-point transversal.

---

### 3. A dual fractional local-cover theorem

Let \(\Omega\) be a finite point set and let \(\mathcal D\) be a family of blocks such that:

1. every point of \(\Omega\) belongs to exactly \(k\) blocks;
2. every set of at most seven points is contained in the union of two blocks.

This is exactly the dual of a finite \(k\)-uniform hypergraph satisfying \((P_7)\).

**Theorem 4.**  
For every probability distribution \(\mu\) on \(\Omega\), some block \(D\in\mathcal D\) satisfies
\[
\mu(D)\ge (35k)^{-1/3}.
\tag{3}
\]

**Proof.**  
Draw seven independent samples \(X_1,\dots,X_7\) from \(\mu\). Repetitions cause no difficulty: the local property applied to the set of distinct sampled points gives two blocks covering all seven sample positions.

For a block \(D\), let
\[
N_D=\bigl|\{j:X_j\in D\}\bigr|.
\]
Since two blocks cover all seven positions, one of them contains at least four positions. Therefore, for every outcome,
\[
\sum_{D\in\mathcal D}\binom{N_D}{4}\ge1.
\tag{4}
\]
Taking expectations,
\[
1\le
\sum_{D\in\mathcal D}\mathbb E\binom{N_D}{4}
=
\binom74\sum_{D\in\mathcal D}\mu(D)^4
=
35\sum_{D\in\mathcal D}\mu(D)^4.
\tag{5}
\]
Let
\[
M=\max_{D\in\mathcal D}\mu(D).
\]
Exact point-regularity gives
\[
\sum_{D\in\mathcal D}\mu(D)
 =\sum_{x\in\Omega}\mu(x)
   \bigl|\{D:x\in D\}\bigr|
 =k.
\tag{6}
\]
Hence
\[
\sum_D\mu(D)^4
\le M^3\sum_D\mu(D)
=kM^3.
\]
Combining this with (5) gives
\[
1\le35kM^3,
\]
which is exactly (3). \(\square\)

Let \(\tau^*(\Omega,\mathcal D)\) denote the fractional number of blocks required to cover \(\Omega\).

**Corollary 5.**
\[
\boxed{\tau^*(\Omega,\mathcal D)\le(35k)^{1/3}.}
\]

**Proof.**  
The dual LP is
\[
\max \sum_{x\in\Omega}y_x
\]
subject to
\[
y_x\ge0,\qquad
\sum_{x\in D}y_x\le1\quad(D\in\mathcal D).
\]
Let \(Y=\sum_x y_x\). If \(Y>0\), normalize by \(\mu(x)=y_x/Y\). Every block then has
\[
\mu(D)=\frac1Y\sum_{x\in D}y_x\le\frac1Y.
\]
Theorem 4 gives \(1/Y\ge(35k)^{-1/3}\), so
\[
Y\le(35k)^{1/3}.
\]
Finite-dimensional LP duality proves the claim. \(\square\)

This theorem is genuinely fractional; it does not imply a linear integral upper bound with the desired constant.

---

### 4. A ground-size-dependent integral consequence

The same argument can be iterated.

**Corollary 6.**  
If \(|\Omega|=N<\infty\), then
\[
\tau(\Omega,\mathcal D)
\le
1+(35k)^{1/3}\log N.
\tag{7}
\]

**Proof.**  
Apply Theorem 4 to the uniform distribution on the currently uncovered points. A block covers at least the fraction
\[
\delta=(35k)^{-1/3}
\]
of those points. After selecting \(m\) blocks, the number left uncovered is at most
\[
N(1-\delta)^m.
\]
This is less than \(1\) once
\[
m>\frac{\log N}{-\log(1-\delta)}
\le \delta^{-1}\log N,
\]
using \(-\log(1-\delta)\ge\delta\). Taking an extra block handles rounding. \(\square\)

Thus any finite example with \(\tau\ge c k\) must have
\[
\log |E|\ge (ck-1)(35k)^{-1/3}
 =\Omega(k^{2/3}).
\tag{8}
\]
In particular, linearly extremal examples must have exponentially many edges in \(k^{2/3}\), unless additional structure defeats this estimate.

The exponent \(1/3\) in Theorem 4 cannot be improved in general.

**Example 7.**  
Let \(\Omega=[n]\) and let the dual blocks be all four-element subsets of \([n]\). Every point belongs to
\[
k=\binom{n-1}{3}
\]
blocks. Every seven points are covered by two four-sets, and
\[
\tau=\tau^*=\left\lceil\frac n4\right\rceil
 =\Theta(k^{1/3}).
\]
For the fractional equality, summing all point-covering constraints gives a lower bound \(n/4\), while uniform weights on the four-sets attain \(n/4\).

---

### 5. Exact reduction when two disjoint primal edges exist

Let \(B,C\) be two disjoint edges of the original hypergraph. Set
\[
U=B\cup C.
\]
No third edge can be disjoint from both \(B\) and \(C\), since that would give three pairwise disjoint edges and violate \((P_3)\). Hence every edge has a nonempty trace on \(U\).

For an edge \(E\), write
\[
S_E=E\cap B,\qquad T_E=E\cap C.
\]

**Lemma 8.**  
For every five edges \(E_1,\dots,E_5\), there are \(b\in B\) and \(c\in C\) such that
\[
E_i\cap\{b,c\}\ne\varnothing
\qquad(1\le i\le5).
\tag{9}
\]

**Proof.**  
Apply \((P_7)\) to
\[
B,C,E_1,\dots,E_5.
\]
Any pair hitting the disjoint edges \(B\) and \(C\) must contain one vertex of \(B\) and one vertex of \(C\). That same pair hits the remaining five edges. \(\square\)

Thus the non-intersecting case reduces to the following purely dual/trace problem.

> **Unproved cross-transversal statement.**  
> Let \(B,C\) be disjoint \(k\)-sets, and let \(\mathcal G\) be a hypergraph on \(B\cup C\) of rank at most \(k\), containing \(B\) and \(C\). Suppose every five members of \(\mathcal G\) have a transversal \(\{b,c\}\) with \(b\in B,c\in C\). Must
> \[
> \tau(\mathcal G)\le\left(\frac34+o(1)\right)k?
> \tag{10}
> \]

A proof would establish the desired upper bound whenever the original hypergraph contains two disjoint edges.

There is a useful rectangle formulation. For
\[
E=S_E\cup T_E,
\]
define
\[
R_E=(B\setminus S_E)\times(C\setminus T_E).
\]
Five trace edges have a common cross-transversal exactly when their five rectangles do not cover \(B\times C\). A transversal \(X\cup Y\), where \(X\subseteq B\) and \(Y\subseteq C\), hits every trace edge exactly when no rectangle \(R_E\) contains \(X\times Y\). Thus (10) asks for an “anti-contained” biclique with
\[
|X|+|Y|\le\left(\frac34+o(1)\right)k.
\]
I do not have a proof of this rectangle theorem.

The intersecting case is a separate obstacle. If every two primal edges intersect, any one edge gives a transversal of size \(k\), but Route 4 currently supplies no mechanism for deleting \(k/4\) of its vertices while preserving global coverage.

---

### 6. Why a naive finite-kernel argument does not close the gap

One can bound the number of edges in a transversal-critical subfamily, but the resulting bound is too large to combine effectively with Corollary 6.

**Lemma 9.**  
If a finite \(k\)-uniform hypergraph \(\mathcal F\) is edge-minimal subject to \(\tau(\mathcal F)=t\), then
\[
|\mathcal F|\le\binom{k+t-1}{k}.
\tag{11}
\]

**Proof.**  
Write \(\mathcal F=\{A_1,\dots,A_m\}\). By edge-minimality,
\[
\tau(\mathcal F\setminus\{A_i\})=t-1.
\]
Choose a transversal \(T_i\) of \(\mathcal F\setminus\{A_i\}\) of size \(t-1\). Necessarily
\[
A_i\cap T_i=\varnothing,
\]
or else \(T_i\) would hit all of \(\mathcal F\). For \(i\ne j\),
\[
A_i\cap T_j\ne\varnothing.
\]

The Bollobás set-pairs inequality now applies to the pairs \((A_i,T_i)\), with sizes \(k\) and \(t-1\), and gives
\[
m\le\binom{k+t-1}{k}.
\]

For completeness, the relevant set-pairs inequality follows by considering a random ordering of the underlying elements. The event that all elements of \(A_i\) precede all elements of \(T_i\) has probability \(\binom{k+t-1}{k}^{-1}\). These events are pairwise disjoint: if both the \(i\)- and \(j\)-events occurred, elements from \(A_i\cap T_j\) and \(A_j\cap T_i\) would be forced into contradictory relative orders. Summing their probabilities proves (11). \(\square\)

Combining (7) and (11) only yields
\[
t\le
1+(35k)^{1/3}
 \log\binom{k+t-1}{k},
\]
which is \(O(k^{4/3})\) when \(t=\Theta(k)\), weaker than the known bound \(t\le k\). Therefore this kernel estimate does not approach the coefficient \(3/4\).

## Self-Audit

1. **The decisive integral upper bound is missing.**  
   The fractional estimate is rigorous but cannot be rounded with additive \(o(k)\) loss by any argument given here. I therefore make no claim that the problem is solved; this is the exact reason for the `BLOCKED` status.

2. **The lower construction uses the strict inequality \(4q<3k\).**  
   This is essential, not a rounding artifact. The proof explicitly converts failure of two-point coverability into seven \(q\)-sets covering every pair, and Lemma 1 then contradicts \(q<3n/7\). The Fano blow-up verifies that equality can genuinely fail.

3. **The cross-transversal reduction covers only the case of two disjoint edges.**  
   Lemma 8 is exact, but statement (10) is unproved and the intersecting case remains separate. I believe the reduction itself is sound because the two witnesses are forced into the two disjoint core edges; I do not assert that the proposed cross theorem is true.

## Computations To Verify

```python
from itertools import combinations, combinations_with_replacement

def two_coverable(subfamily):
    U = sorted(set().union(*subfamily))
    for x, y in combinations_with_replacement(U, 2):
        if all((x in A) or (y in A) for A in subfamily):
            return True, (x, y)
    return False, None

def satisfies_Pr(edges, r=7):
    m = len(edges)
    for s in range(1, min(r, m) + 1):
        for inds in combinations(range(m), s):
            fam = [edges[i] for i in inds]
            ok, witness = two_coverable(fam)
            if not ok:
                return False, inds
    return True, None

def transversal_number(edges):
    U = sorted(set().union(*edges))
    for t in range(len(U) + 1):
        for T in combinations(U, t):
            T = set(T)
            if all(T & A for A in edges):
                return t, T
    raise RuntimeError("Impossible")

def complete_construction(k):
    q = (3*k - 1) // 4
    n = k + q
    edges = [set(A) for A in combinations(range(n), k)]
    return n, q, edges

# Directly feasible for small k, e.g. k <= 4.
for k in range(1, 5):
    n, q, edges = complete_construction(k)
    ok, bad = satisfies_Pr(edges, 7)
    tau, T = transversal_number(edges)
    print(k, n, q, ok, tau, (3*k + 3)//4)
```

Check the Fano equality obstruction:

```python
FANO_LINES = [
    {0,1,2}, {0,3,4}, {0,5,6},
    {1,3,5}, {1,4,6},
    {2,3,6}, {2,4,5}
]

def fano_blowup(m):
    # Ground set consists of pairs (Fano point, clone index).
    V = {(i, a) for i in range(7) for a in range(m)}
    complements = []
    edges = []
    for L in FANO_LINES:
        C = {(i, a) for i in L for a in range(m)}
        complements.append(C)
        edges.append(V - C)
    return V, complements, edges

for m in range(1, 4):
    V, complements, edges = fano_blowup(m)
    ok, witness = two_coverable(edges)
    print("m =", m, "edge size =", len(edges[0]),
          "two-coverable =", ok)
    # Expected: False
```

Generic dual incidence-matrix checker. Each column is represented by the bitmask of rows containing it.

```python
def dual_local_ok(columns, num_rows, r=7):
    # Exact k-regularity can be checked separately by bit_count.
    row_pairs = [
        (1 << i) | (1 << j)
        for i in range(num_rows)
        for j in range(i, num_rows)
    ]
    m = len(columns)
    for s in range(1, min(r, m) + 1):
        for inds in combinations(range(m), s):
            if not any(
                all(columns[c] & pairmask for c in inds)
                for pairmask in row_pairs
            ):
                return False, inds
    return True, None

def dual_cover_number(columns, num_rows):
    for t in range(num_rows + 1):
        for rows in combinations(range(num_rows), t):
            mask = sum(1 << i for i in rows)
            if all(c & mask for c in columns):
                return t, rows
    raise RuntimeError("Impossible")

def check_dual(columns, num_rows, k):
    assert all(c.bit_count() == k for c in columns)
    return dual_local_ok(columns, num_rows, 7), \
           dual_cover_number(columns, num_rows)
```

Verify the four-set example showing the \(k^{1/3}\) fractional exponent is sharp:

```python
from math import comb, ceil

for n in range(7, 15):
    blocks = [set(B) for B in combinations(range(n), 4)]
    k = comb(n - 1, 3)
    # Every <=7 points can be partitioned into sets of size <=4.
    integral_cover = ceil(n / 4)
    fractional_cover = n / 4
    print(n, k, integral_cover, fractional_cover)
```

A CP-SAT search over fixed row ground set \(R\) can search directly for counterexamples:

```python
# Pseudocode using OR-Tools cp_model.
#
# candidates = all k-subsets of range(R), represented as masks
# z[c] = 1 iff candidate column c is selected
#
# For every tuple Q of 3,...,7 candidate columns:
#     if no pair of rows meets every column in Q:
#         Add(sum(z[c] for c in Q) <= len(Q)-1)
#
# To force covering number at least t+1:
# for every t-subset T of rows:
#     disjoint = [c for c in candidates if (c & Tmask) == 0]
#     Add(sum(z[c] for c in disjoint) >= 1)
#
# Solve feasibility.
```

The same model should be run for the reduced cross problem by taking two \(k\)-element row classes \(B,C\), candidate trace edges of size at most \(k\), and declaring a tuple bad when no pair \((b,c)\in B\times C\) hits every trace edge.

## Route Diagnosis

### Proved ledger

- The complete \(k\)-uniform hypergraph on
  \[
  k+\left\lfloor\frac{3k-1}{4}\right\rfloor
  \]
  vertices is \(7\)-locally 2-coverable.
- Its transversal number is exactly
  \[
  \left\lceil\frac{3k}{4}\right\rceil.
  \]
- Hence the conjectured \(3/4\) lower bound holds for every \(k\), not merely along a subsequence.
- The Fano plane gives the sharp equality obstruction for this construction.
- Every dual \(k\)-regular seven-local system satisfies
  \[
  \tau^*\le(35k)^{1/3}.
  \]
- A finite system on \(N\) dual points satisfies
  \[
  \tau\le1+(35k)^{1/3}\log N.
  \]
- The exponent \(1/3\) is sharp for the fractional theorem.
- In the presence of two disjoint primal edges, the problem reduces exactly to a bipartite five-local cross-transversal problem.
- A transversal-critical finite witness has at most
  \[
  \binom{k+t-1}{k}
  \]
  edges.

### Plausible but unproved

- The bipartite cross-transversal statement (10).
- An integral rounding theorem exploiting seven-local coverability strongly enough to turn the \(O(k^{1/3})\) fractional cover into a \((3/4+o(1))k\) integral cover.
- A stability refinement of the known \(f(k,6)=k\) theorem showing that exclusion of seven-edge obstructions saves \(k/4-o(k)\) vertices.

### Dead ends

- **Naive projection to a matching core.** Traces need not remain locally two-coverable. For example, with
  \[
  B=\{b_1,b_2,b_3\},\qquad
  E_i=\{b_i,z,u_i\},
  \]
  the four-edge family \(\{B,E_1,E_2,E_3\}\) is globally covered by \(\{z,b_1\}\), but the traces \(E_i\cap B=\{b_i\}\) require three points.
- **Fractional rounding alone.** The moment argument is strong fractionally but supplies no bounded integrality gap. The conjectured linear examples, if they exist, must exhibit an integrality gap of order at least \(k^{2/3}\).
- **Critical-family kernelization.** Bollobás gives only an exponential-in-\(k\) bound on the number of edges, too large for the \(O(k^{1/3}\log N)\) estimate to improve the known linear upper bound.
- **Majority-block charging on private points.** It yields a block covering \(\Omega(k^{-1/3})\) of any weighted private-point set, but replacement by that block can uncover unrelated points. Minimum-cover exchange witnesses do not presently give the required coefficient.

A fresh attempt should reconstruct the \(f(k,6)=k\) proof and derive a stability theorem under the extra seventh-edge condition. In parallel, the cross-rectangle statement should be tested exhaustively for small \(k\); either a counterexample will kill the most promising disjoint-core reduction, or its extremizers may reveal the missing \(3/4\) charging inequality.