STATUS: BLOCKED

## Result

Neither P1 nor P2 is resolved. I obtained several rigorous Route 2 consequences: (i) admissibility says every gap \(a_i\) is a uniquely represented positive difference of the prefix-sum set; (ii) every admissible sequence has lower density at most \(2/3\), hence \(\limsup a_n/n\ge 3/2\); (iii) universally,
\[
\limsup_{x\to\infty}\frac{H_A(x)}{\log x}\le \frac23;
\]
and (iv) any positive-density or positive-logarithmic-density counterexample must force the complement of \(A\) to absorb, on average, \(\gg\log K\) distinct consecutive-block lengths \(2\le k\le K\). I also construct finite admissible sequences in which a single missing integer has \(\asymp\sqrt N\) consecutive-block representations, showing that pointwise multiplicity bounds and cardinality-only additive-energy arguments cannot close the problem. Finally, no eventually periodic set can be admissible.

## Complete Argument

### 1. Global difference formulation and exact Fourier identity

For \(k\ge2\), define
\[
B_k=\left\{b_n^{(k)}:n\ge1\right\},
\qquad
b_n^{(k)}=a_n+a_{n+1}+\cdots+a_{n+k-1}.
\]

#### Lemma 1
For every \(k\ge2\),
\[
A\cap B_k=\varnothing.
\]

#### Proof
If \(b_n^{(k)}=a_i\), then
\[
b_n^{(k)}>a_{n+k-1},
\]
because \(k\ge2\) and all terms are positive. Hence \(i>n+k-1\), and \(a_i\) equals a consecutive block sum of earlier terms, contrary to admissibility. ∎

Let
\[
S_0=0,\qquad S_j=\sum_{m=1}^j a_m
\]
and, for a finite prefix of length \(N\), put
\[
R_N(x)=\#\{(t,s):0\le t<s\le N,\ S_s-S_t=x\}.
\]

#### Lemma 2
A prefix \(a_1,\ldots,a_N\) is admissible if and only if
\[
R_N(a_i)=1\qquad(1\le i\le N).
\]

#### Proof
The adjacent pair \((i-1,i)\) always represents \(a_i\), so \(R_N(a_i)\ge1\).

Suppose another interval represents \(a_i\). A length-one interval would be another term \(a_j=a_i\), impossible by strict increase. Thus its length is at least two.

If its endpoint is before \(i\), it is a forbidden earlier block representation of \(a_i\). If its endpoint is at least \(i\), then either the interval contains \(a_i\), in which case its sum is strictly greater than \(a_i\), or every term in it occurs after \(a_i\), in which case every term is already greater than \(a_i\). Thus no such representation exists. The converse is immediate. ∎

This makes the Route 2 problem precise: the adjacent differences of the convex prefix-sum sequence are “private differences”.

Define
\[
P_N(\theta)=\sum_{j=0}^N e^{2\pi i\theta S_j},
\qquad
G_N(\theta)=\sum_{i=1}^N e^{2\pi i\theta a_i}.
\]

Orthogonality gives the exact identity
\[
\int_0^1 |P_N(\theta)|^2\overline{G_N(\theta)}\,d\theta
=
\sum_{i=1}^N R_N(a_i).
\tag{4}
\]
Consequently, for an admissible prefix,
\[
\boxed{\int_0^1 |P_N(\theta)|^2\overline{G_N(\theta)}\,d\theta=N.}
\tag{5}
\]

Thus a Fourier proof would have to show that a linear-growth or logarithmic-mass hypothesis makes the left side strictly larger than \(N\). Standard energy estimates alone do not do this: the integrand has no fixed sign, and energy controls the distribution of all differences rather than forcing them to meet the particular private-difference set \(\{a_i\}\).

---

### 2. A universal lower-density bound

For fixed \(k\), the sequence \(b_n^{(k)}\) is strictly increasing because
\[
b_{n+1}^{(k)}-b_n^{(k)}
=a_{n+k}-a_n>0.
\]

#### Theorem 3
Every admissible set satisfies
\[
\underline d(A)\le\frac23.
\]
Equivalently,
\[
\limsup_{n\to\infty}\frac{a_n}{n}\ge\frac32.
\]

#### Proof
Let \(d=\underline d(A)\). There is nothing to prove if \(d=0\), so assume \(d>0\). By the density-enumeration identity,
\[
\limsup_{n\to\infty}\frac{a_n}{n}=\frac1d.
\]

For fixed \(k\ge2\),
\[
b_n^{(k)}\le k\,a_{n+k-1}.
\]
Therefore
\[
\limsup_{n\to\infty}\frac{b_n^{(k)}}n
\le
k\limsup_{n\to\infty}
\frac{a_{n+k-1}}{n+k-1}\frac{n+k-1}{n}
=\frac{k}{d}.
\]
Applying the same density-enumeration identity to \(B_k\) gives
\[
\underline d(B_k)\ge\frac{d}{k}.
\]

By Lemma 1, \(A\cap B_k=\varnothing\). Hence
\[
\underline d(A)+\underline d(B_k)\le1,
\]
and consequently
\[
d+\frac{d}{k}\le1.
\]
Taking \(k=2\) gives \(d\le2/3\). ∎

This proves finite obstruction for every cap \(C<3/2\), but not for arbitrary fixed \(C\).

---

### 3. A universal logarithmic-density bound

#### Theorem 4
Every admissible sequence satisfies
\[
\limsup_{X\to\infty}\frac{H_A(X)}{\log X}\le\frac23.
\]

#### Proof
For \(k\ge2\), if \(a_{n+k-1}<X/k\), then
\[
b_n^{(k)}\le k a_{n+k-1}<X
\]
and
\[
\frac1{b_n^{(k)}}\ge\frac1{k\,a_{n+k-1}}.
\]
It follows that
\[
H_{B_k}(X)
\ge
\frac1k H_A(X/k)-O_{A,k}(1),
\tag{6}
\]
where only the first \(k-1\) terms of \(A\) are omitted.

Since \(A\cap B_k=\varnothing\),
\[
H_A(X)+H_{B_k}(X)
\le
\sum_{n<X}\frac1n
=
\log X+O(1).
\]
Combining this with (6),
\[
H_A(X)+\frac1k H_A(X/k)
\le\log X+O_{A,k}(1).
\tag{7}
\]

Also,
\[
0\le H_A(X)-H_A(X/k)
\le
\sum_{X/k\le n<X}\frac1n
=
\log k+O_k(X^{-1}).
\]
Thus (7) yields
\[
\left(1+\frac1k\right)H_A(X)
\le
\log X+O_{A,k}(1).
\]
Taking \(k=2\) and dividing by \(\log X\) proves
\[
\limsup_{X\to\infty}\frac{H_A(X)}{\log X}\le\frac23.
\]
∎

This is only a constant-factor bound and does not establish P2.

---

### 4. What a positive-density counterexample would force energetically

For \(K\ge2\), define the restricted block-representation multiplicity
\[
r_K(x)=
\#\left\{
k\in\{2,\ldots,K\}:x\in B_k
\right\}.
\tag{8}
\]
For a fixed \(k\), there is at most one starting position representing \(x\), because \(b_n^{(k)}\) is strictly increasing.

#### Proposition 5
Suppose an admissible set has lower density \(d>0\). Write
\[
h_K=\sum_{k=2}^K\frac1k.
\]
Then
\[
\liminf_{X\to\infty}
\frac1X\sum_{\substack{x\le X\\x\notin A}}r_K(x)
\ge d h_K.
\tag{9}
\]
Consequently, the average of \(r_K\) over holes of \(A\) is asymptotically at least
\[
\frac{d h_K}{1-d},
\tag{10}
\]
and
\[
\liminf_{X\to\infty}
\frac1X\sum_{\substack{x\le X\\x\notin A}}r_K(x)^2
\ge
\frac{d^2 h_K^2}{1-d}.
\tag{11}
\]

#### Proof
The proof of Theorem 3 gives
\[
\underline d(B_k)\ge\frac dk.
\]
Since \(K\) is fixed,
\[
\begin{aligned}
\sum_{\substack{x\le X\\x\notin A}}r_K(x)
&=\sum_{k=2}^K |B_k\cap[1,X]|\\
&\ge \left(dh_K-o(1)\right)X.
\end{aligned}
\]
This proves (9).

The number of holes up to \(X\) is at most
\[
(1-d+o(1))X.
\]
Dividing gives (10). Finally, Cauchy–Schwarz yields
\[
\sum_{\substack{x\le X\\x\notin A}}r_K(x)^2
\ge
\frac{\left(\sum_{x\le X,\ x\notin A}r_K(x)\right)^2}
{\#\{x\le X:x\notin A\}},
\]
which gives (11). ∎

Because \(h_K=\log K+O(1)\), any positive-lower-density counterexample must make a typical missing integer absorb an unbounded number, of order \(\log K\), of different block lengths.

There is an analogous logarithmic statement.

#### Proposition 6
Suppose that along \(X_j\to\infty\),
\[
\frac{H_A(X_j)}{\log X_j}\longrightarrow\delta>0.
\]
Then for every fixed \(K\),
\[
\liminf_{j\to\infty}
\frac{1}{\log X_j}
\sum_{\substack{x<X_j\\x\notin A}}\frac{r_K(x)}x
\ge \delta h_K.
\tag{12}
\]
Moreover,
\[
\liminf_{j\to\infty}
\frac{1}{\log X_j}
\sum_{\substack{x<X_j\\x\notin A}}\frac{r_K(x)^2}{x}
\ge
\frac{\delta^2h_K^2}{1-\delta}.
\tag{13}
\]

#### Proof
Summing (6) over \(2\le k\le K\) gives
\[
\begin{aligned}
\sum_{\substack{x<X\\x\notin A}}\frac{r_K(x)}x
&=\sum_{k=2}^K H_{B_k}(X)\\
&\ge
\sum_{k=2}^K\frac1kH_A(X/k)-O_{A,K}(1).
\end{aligned}
\]
For fixed \(k\),
\[
H_A(X/k)=H_A(X)+O_k(1),
\]
so the right side is
\[
h_KH_A(X)-O_{A,K}(1).
\]
This proves (12).

The harmonic mass of the holes is
\[
\sum_{\substack{x<X_j\\x\notin A}}\frac1x
=(1-\delta+o(1))\log X_j.
\]
Weighted Cauchy–Schwarz now gives
\[
\left(\sum_{\substack{x<X_j\\x\notin A}}\frac{r_K(x)}x\right)^2
\le
\left(\sum_{\substack{x<X_j\\x\notin A}}\frac{r_K(x)^2}{x}\right)
\left(\sum_{\substack{x<X_j\\x\notin A}}\frac1x\right),
\]
which yields (13). ∎

This is the sharp Route 2 reduction I could establish: P1 or P2 would follow from an appropriate theorem preventing this \(\log K\)-scale concentration of representation multiplicity. No such theorem was proved.

---

### 5. Pointwise multiplicity can be very large even in admissible prefixes

The next construction rules out a tempting lemma such as
\[
R_N(x)=O(\log x)
\]
for all admissible prefixes.

#### Proposition 7
For every integer \(L\ge100\), there is a finite admissible sequence with \(\Theta(L^2)\) terms and an integer
\[
X=100L^3
\]
having at least \(L/10\) distinct consecutive-block representations.

#### Proof
Let
\[
q=\left\lfloor\frac L{10}\right\rfloor.
\]
For every length
\[
L\le \ell\le L+q,
\]
write
\[
X-\frac{\ell(\ell-1)}2=\ell Q_\ell+R_\ell,
\qquad 0\le R_\ell<\ell.
\]
Define an increasing \(\ell\)-tuple
\[
t_{\ell,j}
=
Q_\ell+j+\mathbf 1_{\{j\ge \ell-R_\ell\}},
\qquad 0\le j<\ell,
\tag{14}
\]
where the indicator is always zero if \(R_\ell=0\). Its sum is
\[
\ell Q_\ell+\frac{\ell(\ell-1)}2+R_\ell=X.
\tag{15}
\]

The tuple is strictly increasing: successive differences are \(1\), except possibly one difference equal to \(2\).

Its terms satisfy
\[
\min T_\ell>
\frac X\ell-\frac{\ell-1}{2}-1,
\qquad
\max T_\ell\le
\frac X\ell+\frac{\ell+1}{2}.
\tag{16}
\]

Concatenate the tuples in descending order of length:
\[
T_{L+q},T_{L+q-1},\ldots,T_L.
\]
For \(L<\ell\le L+q\), (16) gives
\[
\begin{aligned}
\min T_{\ell-1}-\max T_\ell
&>
\frac{X}{\ell-1}-\frac{\ell-2}{2}-1
-\frac X\ell-\frac{\ell+1}{2}\\
&=
\frac{X}{\ell(\ell-1)}-\ell-\frac12.
\end{aligned}
\]
Since \(\ell\le1.1L\) and \(X=100L^3\),
\[
\frac{X}{\ell(\ell-1)}
>
\frac{100}{1.21}L>82L,
\]
whereas \(\ell+1/2<2L\). Hence every term of \(T_\ell\) is smaller than every term of \(T_{\ell-1}\). The concatenation is therefore strictly increasing.

Again using (16), all its terms lie between
\[
90L^2
\quad\text{and}\quad
101L^2.
\]
Thus every sum of at least two terms exceeds \(180L^2\), while every term is below \(101L^2\). The finite sequence is consequently admissible.

Each tuple \(T_\ell\) is a consecutive block with sum \(X\). There are \(q+1\ge L/10\) such tuples. The number of terms is
\[
\sum_{\ell=L}^{L+q}\ell=\Theta(L^2).
\]
Thus one missing value has multiplicity \(\gg L\), which is \(\gg\sqrt N\) in terms of the number \(N\) of sequence elements. ∎

This construction does not satisfy a fixed cap \(a_i\le Ci\) from its first index: all terms begin around \(L^2\). It therefore is not a counterexample to P1. It does show that admissibility and convexity alone permit nearly maximal concentration of difference energy on missing values.

---

### 6. Eventually periodic sets are impossible

#### Proposition 8
No infinite eventually periodic subset of the positive integers is consecutive-sum-avoiding.

#### Proof
Suppose there are \(Q\ge1\), \(N_0\), and \(R\subseteq\mathbb Z/Q\mathbb Z\) such that, for all \(n\ge N_0\),
\[
n\in A\quad\Longleftrightarrow\quad n\bmod Q\in R.
\]

Choose \(Q+1\) consecutive terms of \(A\),
\[
x_0<x_1<\cdots<x_Q,
\]
all exceeding \(N_0\). Consider the \(Q+1\) residues
\[
0,\quad x_0,\quad x_0+x_1,\quad\ldots,\quad x_0+\cdots+x_{Q-1}
\pmod Q.
\]
Two coincide. Hence there exist \(0\le u<v\le Q\) such that
\[
x_u+x_{u+1}+\cdots+x_{v-1}\equiv0\pmod Q.
\]
Append the next term \(x_v\). Then
\[
y=x_u+x_{u+1}+\cdots+x_v
\equiv x_v\pmod Q.
\]
The block has length at least two, and \(y>x_v\ge N_0\). Since \(x_v\in A\), its residue lies in \(R\), so eventual periodicity implies \(y\in A\). As \(y>x_v\), it is a later term of \(A\), represented by the displayed earlier consecutive block. This contradicts admissibility. ∎

## Self-Audit

1. **The passage from \(A\) to the block-sum sequences \(B_k\).**  
   A hidden chronology error here would invalidate the density bounds. It is sound because every \(k\)-term block sum with \(k\ge2\) is strictly larger than its last summand, so if it belongs to \(A\), its index must occur after the entire block.

2. **The logarithmic inequality \(H_{B_k}(X)\ge k^{-1}H_A(X/k)-O(1)\).**  
   The cutoff and reciprocal directions are easy to reverse accidentally. They are correct: \(b_n^{(k)}\le k a_{n+k-1}\), so \(a_{n+k-1}<X/k\) implies both \(b_n^{(k)}<X\) and \(1/b_n^{(k)}\ge1/(k a_{n+k-1})\).

3. **The large-multiplicity construction.**  
   Its tuple ordering and admissibility depend on generous but explicit constants. Inequalities (16) and \(X=100L^3\) give large separation between successive tuples, while all terms lie in an interval of ratio below \(2\); the supplied computation can check every assertion exactly. Its limitation is important: it does not have a fixed global linear cap and therefore only refutes generic energy lemmas, not P1.

## Computations To Verify

```python
from collections import Counter
from fractions import Fraction
from math import floor, log

def prefix_sums(a):
    S = [0]
    for v in a:
        S.append(S[-1] + v)
    return S

def representation_histogram(a):
    """R[x] = number of consecutive blocks with sum x."""
    S = prefix_sums(a)
    R = Counter()
    N = len(a)
    for s in range(1, N + 1):
        for t in range(s):
            R[S[s] - S[t]] += 1
    return R

def admissible(a):
    if any(a[i] >= a[i+1] for i in range(len(a)-1)):
        return False
    forbidden = Counter()
    S = [0]
    for v in a:
        if forbidden[v] > 0:
            return False
        sn = S[-1] + v
        for old in S:
            forbidden[sn - old] += 1
        S.append(sn)
    return True

def verify_private_differences(a):
    """Checks Lemma 2 and the exact Fourier coefficient identity."""
    R = representation_histogram(a)
    return admissible(a), [R[v] for v in a], sum(R[v] for v in a)

def balanced_collision_construction(L):
    assert L >= 100
    X = 100 * L**3
    q = L // 10
    a = []
    blocks = []

    for ell in range(L + q, L - 1, -1):
        Y = X - ell * (ell - 1) // 2
        Q, rem = divmod(Y, ell)
        block = [
            Q + j + (1 if rem > 0 and j >= ell - rem else 0)
            for j in range(ell)
        ]
        assert len(block) == ell
        assert all(block[j] < block[j+1] for j in range(ell-1))
        assert sum(block) == X
        if a:
            assert a[-1] < block[0]
        blocks.append(block)
        a.extend(block)

    assert all(90 * L**2 < v < 101 * L**2 for v in a)
    assert 2 * min(a) > max(a)
    assert admissible(a)

    R = representation_histogram(a)
    assert R[X] >= q + 1
    return a, X, blocks, R[X]

# Example:
# a, X, blocks, multiplicity = balanced_collision_construction(100)
# print(len(a), X, multiplicity)


def find_prefix_under_cap(C_num, C_den, target_depth, stop_after_one=True):
    """
    Exact DFS for a_i <= floor(C*i), with C=C_num/C_den.
    Returns one surviving prefix of target_depth, or None.
    """
    a = []
    S = [0]
    forbidden = Counter()
    answer = None

    def cap(i):
        return (C_num * i) // C_den

    def dfs():
        nonlocal answer
        m = len(a)
        if m == target_depth:
            answer = a.copy()
            return True

        i = m + 1
        lo = a[-1] + 1 if a else 1
        hi = cap(i)

        for v in range(lo, hi + 1):
            if forbidden[v]:
                continue

            sn = S[-1] + v
            added = [sn - old for old in S]

            a.append(v)
            S.append(sn)
            for x in added:
                forbidden[x] += 1

            if dfs() and stop_after_one:
                return True

            for x in added:
                forbidden[x] -= 1
                if forbidden[x] == 0:
                    del forbidden[x]
            S.pop()
            a.pop()

        return False

    dfs()
    return answer

# Examples:
# for N in range(1, 30):
#     sol = find_prefix_under_cap(3, 2, N)
#     print(N, sol)


def block_length_multiplicities(a, K, X):
    """
    r_K(x): number of lengths 2 <= k <= K representing x.
    """
    N = len(a)
    rK = Counter()
    for k in range(2, min(K, N) + 1):
        value = sum(a[:k])
        if value < X:
            rK[value] += 1
        for n in range(1, N - k + 1):
            value += a[n+k-1] - a[n-1]
            if value < X:
                rK[value] += 1
    return rK

def route2_diagnostics(a, K, X):
    Aset = {v for v in a if v < X}
    rK = block_length_multiplicities(a, K, X)
    holes = [x for x in range(1, X) if x not in Aset]

    first_moment = sum(rK[x] for x in holes)
    second_moment = sum(rK[x]**2 for x in holes)
    harmonic_first = sum(rK[x] / x for x in holes)
    harmonic_second = sum(rK[x]**2 / x for x in holes)

    return {
        "admissible": admissible(a),
        "A_count": len(Aset),
        "hole_count": len(holes),
        "first_moment": first_moment,
        "second_moment": second_moment,
        "average_multiplicity_on_holes":
            first_moment / len(holes) if holes else 0.0,
        "harmonic_first": harmonic_first,
        "harmonic_second": harmonic_second,
        "max_multiplicity": max(rK.values(), default=0),
        "maximizers": [x for x, v in rK.items()
                       if v == max(rK.values(), default=0)]
    }


def verify_eventual_periodic_obstruction(Q, residues):
    """
    Finite modular check: every word of Q+1 term residues has a block
    of length >=2 whose sum has the residue of its last term.
    For an actual periodic set, use its Q+1 consecutive term residues.
    """
    residues = [r % Q for r in residues]
    assert len(residues) >= Q + 1

    pref = [0]
    for j in range(Q):
        pref.append((pref[-1] + residues[j]) % Q)

    seen = {}
    for v, residue in enumerate(pref):
        if residue in seen:
            u = seen[residue]
            # zero-sum block residues[u:v], append residues[v]
            block_sum = sum(residues[u:v+1]) % Q
            assert block_sum == residues[v] % Q
            assert v - u + 1 >= 2
            return (u, v, block_sum)
        seen[residue] = v

    raise AssertionError("Pigeonhole principle should force a collision.")
```

The most informative computational experiment is not merely interval coverage. For each fixed-cap survivor, record
\[
r_K(x),\qquad x\notin A,
\]
and test whether its average over holes grows like \(\log K\). A putative positive-density counterexample must exhibit exactly that concentration.

## Route Diagnosis

### Proved ledger

- Every gap \(a_i\) is a uniquely represented positive difference of the finite prefix-sum set.
- Exact Fourier identity:
  \[
  \int |P_N|^2\overline{G_N}=N
  \]
  for admissible prefixes.
- \(A\cap B_k=\varnothing\) for every \(k\ge2\).
- Universal bounds
  \[
  \underline d(A)\le\frac23,\qquad
  \limsup\frac{a_n}{n}\ge\frac32,
  \qquad
  \limsup\frac{H_A(x)}{\log x}\le\frac23.
  \]
- Positive density or positive logarithmic density forces average block-length multiplicity \(\gg\log K\) on the complement.
- Individual missing values can have \(\asymp\sqrt N\) representations in finite admissible prefixes.
- Eventually periodic sets cannot be admissible.

### Plausible but unproved claim needed to finish Route 2

One sufficient form would be:

> Under a fixed global linear bound \(a_n\le Cn\), the average number of distinct block lengths \(2\le k\le K\) representing a hole \(x\le X\) is \(o(\log K)\), uniformly as \(X\to\infty\).

Propositions 5–6 would then contradict positive lower or logarithmic density. I could not prove this. Without the global linear bound it is false in any pointwise form, as Proposition 7 shows.

### Dead ends

1. **Large difference-set cardinality.**  
   Even a very large support of \(S-S\) need not intersect the particular adjacent-difference set \(A\). Cardinality does not encode the required target or chronology.

2. **Pointwise representation bounds.**  
   Proposition 7 gives admissible finite prefixes with a hole having nearly maximal \(\sqrt N\)-scale multiplicity.

3. **Bare Fourier energy.**  
   Cauchy–Schwarz provides only an upper bound for (4). The complex Fourier integrand has no sign, and the unavoidable adjacent representations already account exactly for the value \(N\).

4. **Periodic approximation.**  
   Exact eventual periodicity is impossible, but positive density gives no exact residue-class closure, so the modular argument does not extend by a standard recurrence theorem.

### Sharp block

Route 2 reduces the problem to an inverse theorem for highly colliding interval sums of a strictly convex prefix sequence: if the holes absorb \(\Omega(\log K)\) block lengths on average at every large scale, one must extract a private-difference violation. Establishing that inverse theorem appears comparable in strength to P1/P2 themselves.

A fresh attempt should compute and classify high-\(r_K\) holes in fixed-\(C\) extremal prefixes. The likely useful statement is structural rather than purely energetic: large multiplicity should force many balanced equal-sum packets; one must then prove that a globally dense earlier history makes at least one term in such a packet an earlier block sum. Cross-scale information, absent from standard convex-set energy estimates, seems essential.