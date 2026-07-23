STATUS: BLOCKED

## Result

For \(0<c<1\), I did not obtain a sharp formula for \(M_c(n)\). I proved a rigorous interval-core closure theorem: once a subset of \(A\) has subset sums containing an integer interval of sufficient length, all remaining elements can be absorbed according to an explicit maximum-gap parameter, forcing \(n\) to be represented whenever it lies in the resulting interval. I also proved two concrete mechanisms for constructing such cores—restricted sums of an integer interval and sums from two dense disjoint blocks—and their lattice analogues. However, converting these criteria into a universal cardinality bound requires a new inverse theorem classifying dense sets which fail to produce a correctly located core. Divisibility constructions and cardinality-window constructions show that both the arithmetic step size and the location of the core are genuine obstructions.

## Complete Argument

Write
\[
\Sigma(A):=\left\{\sum_{a\in S}a:S\subseteq A\right\}.
\]

### 1. A maximum-gap bound for arbitrary subset sums

For a finite set
\[
X=\{x_1<\cdots <x_t\}
\]
of positive integers, put
\[
S_i:=\sum_{j=1}^i x_j,\qquad S_0:=0,
\]
and define
\[
D(X):=\max_{1\le i\le t}(x_i-S_{i-1}).
\]
For \(X=\varnothing\), set \(D(X)=0\).

For a finite set \(R=\{r_0<\cdots<r_s\}\) of integers, define its maximum gap by
\[
G(R):=
\begin{cases}
0,&s=0,\\
\max_{0\le j<s}(r_{j+1}-r_j),&s\ge1.
\end{cases}
\]

#### Lemma 1: Maximum-gap lemma

For every finite set \(X\) of positive integers,
\[
G(\Sigma(X))\le D(X).
\]

#### Proof

Let
\[
R_i:=\Sigma(\{x_1,\dots,x_i\}).
\]
Thus
\[
R_i=R_{i-1}\cup(x_i+R_{i-1}),
\]
and \(R_{i-1}\subseteq[0,S_{i-1}]\) contains both endpoints.

Suppose first that \(x_i>S_{i-1}\). Then the convex hulls
\[
[0,S_{i-1}],\qquad [x_i,x_i+S_{i-1}]
\]
are disjoint. Internal gaps in either copy are at most \(G(R_{i-1})\), and the gap between the copies is
\[
x_i-S_{i-1}.
\]
Consequently,
\[
G(R_i)\le\max\bigl(G(R_{i-1}),x_i-S_{i-1}\bigr).
\]

Suppose instead that \(x_i\le S_{i-1}\), so the two convex hulls overlap. Let \(g=G(R_{i-1})\). Every \(y\in[0,S_{i-1})\) has some point of \(R_{i-1}\) in \((y,y+g]\), because consecutive points of \(R_{i-1}\) differ by at most \(g\). Every \(y\in(S_{i-1},x_i+S_{i-1})\) lies in the convex hull of \(x_i+R_{i-1}\) and has a point of that translate in \((y,y+g]\). Thus no gap in the union exceeds \(g\), and
\[
G(R_i)\le G(R_{i-1}).
\]

Starting from \(R_0=\{0\}\) and iterating gives
\[
G(R_t)\le
\max_{1\le i\le t}(x_i-S_{i-1})=D(X).
\]
This proves the lemma. \(\square\)

The case \(D(X)=1\) recovers the usual complete-sequence criterion: since \(\Sigma(X)\) contains \(0\) and \(\sigma(X)\), and all successive represented sums differ by at most one,
\[
\Sigma(X)=[0,\sigma(X)].
\]

---

### 2. The interval-core closure theorem

#### Theorem 2: Smoothing an arbitrary remainder

Let \(B,X\) be disjoint finite sets of positive integers. Suppose
\[
[L,L+W]\subseteq \Sigma(B),
\]
where \(L,W\) are nonnegative integers. If
\[
D(X)\le W+1,
\]
then
\[
[L,L+W+\sigma(X)]\subseteq\Sigma(B\cup X).
\]

In particular, if
\[
L\le n\le L+W+\sigma(X),
\]
then \(n\in\Sigma(B\cup X)\).

#### Proof

List the subset sums of \(X\) as
\[
0=r_0<r_1<\cdots<r_s=\sigma(X).
\]
By Lemma 1,
\[
r_{j+1}-r_j\le D(X)\le W+1.
\]

For every \(j\),
\[
[L+r_j,L+W+r_j]\subseteq\Sigma(B\cup X):
\]
take a subset of \(B\) giving any number in \([L,L+W]\), together with a subset of \(X\) summing to \(r_j\).

Because
\[
r_{j+1}\le r_j+W+1,
\]
the consecutive integer intervals
\[
[L+r_j,L+W+r_j]
\quad\text{and}\quad
[L+r_{j+1},L+W+r_{j+1}]
\]
overlap or are adjacent. Their union over all \(j\) is therefore the full interval
\[
[L,L+W+\sigma(X)].
\]
\(\square\)

This is the precise form of the Route 3 mechanism: a core interval of width \(W\) smooths every gap in the remaining subset sums provided those gaps are at most \(W+1\).

---

### 3. Cores coming from consecutive elements

#### Lemma 3: Restricted sums of an interval

Let
\[
Q=\{u,u+1,\dots,u+\ell-1\},
\]
and let \(1\le h\le\ell\). Then the sums of exactly \(h\) distinct elements of \(Q\) form the complete interval
\[
\left[
hu+\frac{h(h-1)}2,\,
hu+\frac{h(2\ell-h-1)}2
\right].
\]
Its width is
\[
h(\ell-h).
\]

#### Proof

It suffices to prove that sums of \(h\) distinct indices from
\[
\{0,1,\dots,\ell-1\}
\]
give every integer between
\[
\frac{h(h-1)}2
\quad\text{and}\quad
\frac{h(2\ell-h-1)}2.
\]

Proceed by induction on \(\ell\). For \(\ell=h\), there is only one \(h\)-element subset, so the assertion is immediate.

For \(\ell>h\), divide the \(h\)-subsets according to whether they contain \(\ell-1\). By induction, subsets not containing \(\ell-1\) give an interval, and subsets containing \(\ell-1\) give \(\ell-1\) plus the interval of \((h-1)\)-subset sums of \(\{0,\dots,\ell-2\}\). The two intervals overlap or are adjacent; the relevant endpoint inequality reduces to
\[
(h-1)\ell-h^2+1\ge0,
\]
which holds for \(\ell\ge h+1\), with equality when \(\ell=h+1\). Thus their union is the claimed interval. Translating all \(h\) selected indices by \(u\) proves the result. \(\square\)

Combining Lemma 3 with Theorem 2 gives the following explicit target-hitting criterion.

#### Corollary 4: Consecutive-run certificate

Suppose \(A\) contains
\[
Q=\{u,u+1,\dots,u+\ell-1\}.
\]
Let \(X=A\setminus Q\), and choose \(1\le h\le\ell\). Put
\[
L=hu+\frac{h(h-1)}2,\qquad W=h(\ell-h).
\]
If
\[
D(X)\le W+1
\]
and
\[
L\le n\le L+W+\sigma(X),
\]
then \(n\in\Sigma(A)\).

Every condition here is finite and directly checkable.

---

### 4. Arithmetic-progression cores

The previous argument also has a lattice version.

Let
\[
Q=\{u,u+d,\dots,u+(\ell-1)d\}.
\]
The sums of exactly \(h\) elements of \(Q\) are
\[
L+d\{0,1,\dots,h(\ell-h)\},
\]
where
\[
L=hu+d\frac{h(h-1)}2.
\]

#### Corollary 5: Lattice smoothing

Suppose \(X\cap Q=\varnothing\) and every element of \(X\) is divisible by \(d\). Put
\[
Y=\{x/d:x\in X\},\qquad W=h(\ell-h).
\]
If
\[
D(Y)\le W+1,
\]
then every integer congruent to \(L\pmod d\) in
\[
[L,L+dW+\sigma(X)]
\]
belongs to \(\Sigma(Q\cup X)\).

#### Proof

Divide all increments coming from \(X\) and the progression step in the core by \(d\), and apply Theorem 2. \(\square\)

This makes the arithmetic obstruction explicit: the same interval-closure argument may produce only one residue class. If that residue class does not contain \(n\), no amount of closure within the lattice can hit \(n\).

---

### 5. Cores extracted from two dense blocks

A complete run is stronger than necessary. Two intervals with sufficiently few missing elements already produce an interval of pair sums.

#### Lemma 6: Dense two-block lemma

Let
\[
J=[r,r+\ell]\cap\mathbb Z,\qquad
K=[s,s+m]\cap\mathbb Z
\]
be disjoint integer intervals. Let
\[
A_J\subseteq J,\qquad A_K\subseteq K,
\]
and define the total number of holes
\[
H=(|J|-|A_J|)+(|K|-|A_K|).
\]
If
\[
H\le\min(\ell,m),
\]
then
\[
[r+s+H,\ r+s+\ell+m-H]
\subseteq A_J+A_K.
\]

Because \(J\) and \(K\) are disjoint, every represented sum uses two distinct elements.

#### Proof

Fix
\[
z=r+s+q
\]
with
\[
H\le q\le\ell+m-H.
\]
In the full intervals \(J,K\), the number of representations
\[
z=(r+i)+(s+j),\qquad 0\le i\le\ell,\quad 0\le j\le m,
\]
equals
\[
C(q)=
\min(\ell,q)-\max(0,q-m)+1.
\]
As \(q\) is at distance at least \(H\) from both endpoints \(0\) and \(\ell+m\), and \(H\le\min(\ell,m)\), one has
\[
C(q)\ge H+1.
\]

For this fixed \(z\), each missing element of \(J\) destroys at most one candidate pair, and each missing element of \(K\) destroys at most one candidate pair. Since there are only \(H\) missing elements altogether, at most \(H\) of the at least \(H+1\) candidate pairs are destroyed. Thus one pair remains in \(A_J\times A_K\), proving \(z\in A_J+A_K\). \(\square\)

Applying Theorem 2 gives:

#### Corollary 7: Dense-block closure certificate

Under the hypotheses of Lemma 6, let
\[
X=A\setminus(J\cup K),
\]
and put
\[
L=r+s+H,\qquad W=\ell+m-2H.
\]
If
\[
D(X)\le W+1
\]
and
\[
L\le n\le L+W+\sigma(X),
\]
then \(n\in\Sigma(A)\).

Thus Route 3 can work even when \(A\) contains no long consecutive run, provided it has two appropriately located dense blocks.

---

### 6. Sharp counterexamples to overly optimistic completeness claims

The preceding criteria cannot be inferred from positive density alone.

#### 6.1 Lattice obstruction

If \(n\) is odd, then
\[
A=2\mathbb Z\cap[N]
\]
is admissible and has size \(\lfloor N/2\rfloor\). Every subset sum is even, so \(\Sigma(A)\) contains no interval of two consecutive integers.

Thus any completeness theorem must allow a genuine lattice exception.

Even \(\gcd(A)=1\) is not by itself sufficient to remove this issue. For example, if \(n\equiv1\pmod3\), then
\[
A=(3\mathbb Z\cap[N])\cup\{2\}
\]
is admissible: its subset sums are congruent only to \(0\) or \(2\pmod3\). Yet \(\gcd(A)=1\). If \(n\equiv2\pmod3\), the analogous example is
\[
(3\mathbb Z\cap[N])\cup\{1\}.
\]
Consequently, a structural theorem must allow bounded exceptional elements outside a lattice.

#### 6.2 A high-window obstruction persists after adding a small element

Fix \(k\ge2\), and assume \(n\ge k(k+1)\). Let
\[
Q=\left\{q\in[N]:\frac{n}{k+1}<q<\frac nk\right\}.
\]
Then
\[
A=Q\cup\{1\}
\]
is still admissible.

Indeed, let \(S\subseteq A\), and let \(r=|S\cap Q|\).

If \(r\ge k+1\), then
\[
\sigma(S)>\frac{(k+1)n}{k+1}=n.
\]

Suppose \(r\le k\). Let
\[
t=\left\lceil\frac nk\right\rceil-1,
\]
the largest integer strictly below \(n/k\). Since \(n\ge k(k+1)\), one has \(t\ge k\). The sum of any at most \(k\) distinct positive integers bounded by \(t\) is at most the sum of the \(k\) largest such integers:
\[
kt-\frac{k(k-1)}2.
\]
Write \(n=kq+r_0\), with \(0\le r_0<k\).

If \(r_0=0\), then \(t=q-1\), and
\[
kt-\frac{k(k-1)}2
=n-\frac{k(k+1)}2\le n-3.
\]

If \(1\le r_0<k\), then \(t=q\), and
\[
kt-\frac{k(k-1)}2
=n-r_0-\frac{k(k-1)}2\le n-2.
\]

After possibly adding the element \(1\), the sum is therefore at most \(n-1\). Hence no subset sums to \(n\).

This example has gcd \(1\) and contains a very small element. Thus neither “gcd \(1\)” nor “contains a small element” is enough. It is, however, only a bounded perturbation of a cardinality-window construction.

#### 6.3 A long core can be in the wrong location

When \(Q\) is the full interval
\[
\left(\frac n{k+1},\frac nk\right)\cap\mathbb Z,
\]
Lemma 3 shows that its \(k\)-element subset sums contain an interval of length
\[
k(|Q|-k)=\Theta_k(n).
\]
Nevertheless, all such sums are strictly below \(n\), while every sum of at least \(k+1\) elements is strictly above \(n\).

Therefore, merely extracting an interval of length \(\gg n\) is insufficient. Its location, and the ability of the remainder to move it across \(n\), are essential.

---

### 7. Ledger

#### Proved lemmas

1. **Maximum-gap lemma:**  
   \[
   G(\Sigma(X))\le D(X).
   \]

2. **Interval-core closure theorem:** an interval core of width \(W\) absorbs an arbitrary disjoint remainder \(X\) when \(D(X)\le W+1\).

3. **Restricted interval-sum lemma:** exactly \(h\) elements of a consecutive run give a complete interval of width \(h(\ell-h)\).

4. **Lattice analogue:** an arithmetic-progression core gives a complete progression of represented sums, and can absorb increments in the same lattice.

5. **Dense two-block lemma:** two disjoint blocks with \(H\) total holes produce a pair-sum interval after trimming \(H\) from each end.

6. **Counterexamples:** lattice sets, bounded perturbations of lattices, and bounded perturbations of cardinality windows defeat several natural but false completeness statements.

#### Plausible but unproved claims

1. A sharp result likely requires a stability statement saying that every dense admissible set is close, after deleting \(o(n)\) or perhaps \(O_c(1)\) elements, to a bounded-state lattice or layered cardinality obstruction.

2. Outside such structured exceptions, one expects a correctly located interval or arithmetic-progression core satisfying a closure criterion like Theorem 2.

Neither statement is proved here. In their present breadth they are comparable in difficulty to the original problem.

#### Dead ends

1. **“Positive density implies a long interval starting near zero.”** False for multiples of \(d\).

2. **“Positive density plus gcd \(1\) implies completeness.”** False uniformly, as shown by the mod-\(3\) construction with one exceptional element and by \(I_k\cup\{1\}\).

3. **“A long interval somewhere in \(\Sigma(A)\) is enough.”** False because cardinality-window constructions have long intervals entirely below \(n\).

4. **Greedy complete-prefix extraction alone.** It only identifies the first superincreasing gap and does not distinguish lattices from high windows or layered constructions.

5. **Adjacent-pair extraction from a globally dense set.** Choosing one element from each of linearly many adjacent pairs places the resulting interval at total size \(\Theta(n^2)\), far above the target \(n\). Restricting to only \(O(1)\) pairs gives too short an interval.

## Self-Audit

1. **Maximum-gap induction when the two translated subset-sum sets overlap.**  
   This is the most delicate proof step. The argument is valid because every point before the right endpoint of either convex hull has a represented point within the old maximum gap to its right; overlap cannot create a larger empty interval.

2. **The hole count in the dense two-block lemma.**  
   A missing element could in principle destroy many pair sums, but for one fixed target \(z\), it destroys at most one candidate representation because the complementary summand is uniquely determined. Hence the union bound by \(H\) is exact for each \(z\).

3. **Endpoint arithmetic in the construction \(I_k\cup\{1\}\).**  
   The argument needs \(t\ge k\), which is why the explicit hypothesis \(n\ge k(k+1)\) was imposed. Under that hypothesis, padding to the \(k\) largest eligible distinct integers is legitimate, and the displayed deficit is at least two.

The principal weakness is not a doubtful lemma but applicability: none of the proved criteria converts \(|A|\) alone into a sharp upper bound. I have not claimed otherwise.

## Computations To Verify

The following Python checks the maximum-gap lemma exhaustively.

```python
from itertools import product

def subset_sum_bits(A):
    R = 1
    for a in A:
        R |= R << a
    return R

def represented_values(A):
    R = subset_sum_bits(A)
    return [s for s in range(sum(A) + 1) if (R >> s) & 1]

def max_actual_gap(A):
    vals = represented_values(A)
    return max((b - a for a, b in zip(vals, vals[1:])), default=0)

def D_gap(A):
    s = 0
    d = 0
    for x in sorted(A):
        d = max(d, x - s)
        s += x
    return d

for N in range(1, 18):
    for mask in range(1 << N):
        A = [i + 1 for i in range(N) if (mask >> i) & 1]
        assert max_actual_gap(A) <= D_gap(A)

print("Maximum-gap lemma verified for all A subset [17].")
```

Exhaustive verification of the interval-core closure theorem:

```python
def bit_has(R, x):
    return (R >> x) & 1

def maximal_runs(R, total):
    runs = []
    x = 0
    while x <= total:
        if not bit_has(R, x):
            x += 1
            continue
        y = x
        while y + 1 <= total and bit_has(R, y + 1):
            y += 1
        runs.append((x, y))
        x = y + 1
    return runs

for N in range(1, 11):
    # State 0: unused, 1: B, 2: X
    for state in product(range(3), repeat=N):
        B = [i + 1 for i, z in enumerate(state) if z == 1]
        X = [i + 1 for i, z in enumerate(state) if z == 2]

        RB = subset_sum_bits(B)
        Rall = subset_sum_bits(B + X)

        for L, U in maximal_runs(RB, sum(B)):
            W = U - L
            if D_gap(X) <= W + 1:
                for z in range(L, U + sum(X) + 1):
                    assert bit_has(Rall, z)

print("Core-closure theorem verified for all disjoint B,X subset [10].")
```

Verification of the dense two-block lemma:

```python
for ell in range(1, 7):
    for m in range(1, 7):
        r = 1
        s = r + ell + 2  # makes the intervals disjoint
        J = list(range(r, r + ell + 1))
        K = list(range(s, s + m + 1))

        for maskJ in range(1 << len(J)):
            AJ = {J[i] for i in range(len(J)) if (maskJ >> i) & 1}
            for maskK in range(1 << len(K)):
                AK = {K[i] for i in range(len(K)) if (maskK >> i) & 1}

                H = (len(J) - len(AJ)) + (len(K) - len(AK))
                if H > min(ell, m):
                    continue

                pair_sums = {x + y for x in AJ for y in AK}
                lo = r + s + H
                hi = r + s + ell + m - H
                assert all(z in pair_sums for z in range(lo, hi + 1))

print("Dense two-block lemma verified in the tested range.")
```

Verification of \(I_k\cup\{1\}\):

```python
def avoids_target(A, n):
    mask = (1 << (n + 1)) - 1
    R = 1
    for a in A:
        R |= (R << a) & mask
    return ((R >> n) & 1) == 0

for k in range(2, 9):
    for n in range(k * (k + 1), 501):
        for N in range(1, n):
            Q = [
                q for q in range(1, N + 1)
                if (k + 1) * q > n and k * q < n
            ]
            A = sorted(set(Q + [1]))
            assert avoids_target(A, n)

print("I_k union {1} verified for k <= 8 and n <= 500.")
```

An exact branch-and-bound computation of \(M(N,n)\) for small instances:

```python
def exact_M(N, n):
    target_mask = 1 << n
    trunc = (1 << (n + 1)) - 1

    best_size = 0
    best_set = []

    def dfs(a, R, chosen):
        nonlocal best_size, best_set

        if len(chosen) + (N - a + 1) <= best_size:
            return

        if a > N:
            if len(chosen) > best_size:
                best_size = len(chosen)
                best_set = chosen[:]
            return

        # Include a first.
        R2 = R | ((R << a) & trunc)
        if not (R2 & target_mask):
            chosen.append(a)
            dfs(a + 1, R2, chosen)
            chosen.pop()

        # Exclude a.
        dfs(a + 1, R, chosen)

    dfs(1, 1, [])
    return best_size, best_set

for n in range(20, 60):
    for N in range(1, n):
        m, A = exact_M(N, n)
        assert len(A) == m and avoids_target(A, n)
        print(n, N, m, A)
```

A direct test of whether an extremizer is certified by a consecutive-run core:

```python
def run_core_certificate(A, n):
    Aset = set(A)
    for u in A:
        for v in range(u, max(A) + 1):
            if any(x not in Aset for x in range(u, v + 1)):
                break
            ell = v - u + 1
            Q = set(range(u, v + 1))
            X = sorted(Aset - Q)

            for h in range(1, ell + 1):
                L = h * u + h * (h - 1) // 2
                W = h * (ell - h)
                if D_gap(X) <= W + 1:
                    if L <= n <= L + W + sum(X):
                        return (u, v, h, L, W, D_gap(X))
    return None
```

The most useful next experiment is to compute all extremizers for \(20\le n\le 200\), record which are certified by Corollary 4 or Corollary 7, and inspect the uncertified examples for lattice, bounded-exception, and layered-window structure.

## Route Diagnosis

Route 3 successfully yields an exact and flexible target-hitting mechanism once a correctly located interval or arithmetic-progression core has been found. The obstruction is the extraction step. Global density does not force a unit-step interval because of lattices; gcd \(1\) does not remove bounded periodic exceptions; and even a core of linear length may lie wholly below or above \(n\) because of cardinality windows. A theorem strong enough to infer a suitable core from cardinality would have to classify these exceptions and likely bounded unions or layered versions of them. That is an inverse-additive theorem of comparable strength to the original problem, so the route is blocked rather than complete.

A fresh attempt should combine the present closure theorem with either:

1. a composite-modulus restricted-sumset theorem that first identifies the relevant lattice and its stabilizer, followed by interval lifting inside the quotient; or
2. exact ILP data to formulate a finite list of periodic/layered extremal templates, followed by a stability theorem proving that every large admissible set is close to one of them.

The second option should begin by testing whether all computational extremizers not certified by the interval-core criteria are \(O(1)\)- or \(o(n)\)-close to a bounded-modulus periodic set or a union of cardinality windows.