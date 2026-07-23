STATUS: BLOCKED

## Result

Route 4 produces abundant modular and \(p\)-adic “near-misses,” but I could not convert them into exact forbidden equalities with adequate size control. I prove: (i) every residue sequence of length \(>2M^2\) contains the required chronological congruence modulo \(M\); (ii) consequently, a linearly bounded admissible sequence has nonzero near-misses divisible by every prescribed modulus, with explicit bounds; (iii) nested \(p\)-adic recurrence still does not yield a fixed exact equality; (iv) no eventually periodic set is admissible; and, via a stronger alternative packing argument, (v) every admissible sequence satisfies \(\limsup a_n/n\ge 3/2\), equivalently \(\underline d(A)\le 2/3\). Neither P1 nor P2 is resolved.

## Complete Argument

### 1. A universal chronological congruence lemma

Let \(G\) be a finite abelian group and let \(x_1,\dots,x_N\in G\). Define
\[
P_0=0,\qquad P_i=x_1+\cdots+x_i.
\]

#### Lemma 1
If \(N>2|G|^2\), then there are indices
\[
1\le r\le s<i\le N,\qquad s-r+1\ge 2,
\]
such that
\[
x_r+\cdots+x_s=x_i
\quad\text{in }G.
\]

#### Proof
Associate to index \(i\) the directed edge
\[
e_i=(P_{i-1},P_i)\in G^2.
\]
There are only \(|G|^2\) possible directed edges. Since \(N>2|G|^2\), some edge occurs at least three times, say at indices
\[
n_1<n_2<n_3.
\]
Write this repeated edge as \((u,v)\). Thus
\[
P_{n_1-1}=P_{n_2-1}=P_{n_3-1}=u,
\qquad
P_{n_1}=P_{n_2}=P_{n_3}=v.
\]
Taking
\[
r=n_1,\qquad s=n_2,\qquad i=n_3,
\]
we obtain
\[
x_r+\cdots+x_s
=P_{n_2}-P_{n_1-1}
=v-u
=P_{n_3}-P_{n_3-1}
=x_{n_3}.
\]
Because \(n_2>n_1\), the block has length at least two, and \(s=n_2<n_3=i\). ∎

Taking \(G=\mathbb Z/M\mathbb Z\) and \(x_j\equiv a_j\pmod M\) gives the following.

#### Corollary 2
For every integer sequence \(a_1,\dots,a_N\), if \(N>2M^2\), then some indices
\[
1\le r\le s<i\le N,\qquad s-r+1\ge2,
\]
satisfy
\[
a_r+\cdots+a_s\equiv a_i\pmod M.
\]

This is a genuinely chronological statement: the congruent block lies entirely before the target.

The order of magnitude cannot be made sublinear for arbitrary residue words. Indeed, for the constant word \(x_i=1\in\mathbb Z/M\mathbb Z\), a block of length \(\ell\ge2\) has sum congruent to \(1\) only if
\[
\ell\equiv1\pmod M.
\]
The first possible length is \(M+1\), so no violation occurs before target index \(M+2\). This example does not respect a fixed linear bound \(a_i\le Ci\) when realized by distinct integers for arbitrarily large \(M\), but it shows that a purely finite-group argument cannot give recurrence in \(o(M)\) steps.

---

### 2. Quantitative modular near-misses under a linear bound

#### Proposition 3
Suppose
\[
a_j\le Cj\qquad(1\le j\le 2M^2+1).
\]
Then there are \(r\le s<i\le2M^2+1\), with \(s-r+1\ge2\), such that
\[
M\mid \left(\sum_{j=r}^s a_j-a_i\right).
\]
If the prefix is admissible, then the difference is nonzero and
\[
M
\le
\left|\sum_{j=r}^s a_j-a_i\right|
\le
\frac C2(2M^2+1)(2M^2+2).
\tag{4}
\]

#### Proof
The divisibility follows from Corollary 2. Put
\[
D=\sum_{j=r}^s a_j-a_i.
\]
If \(D=0\), the admissibility condition is violated, since the block has length at least two and ends before \(i\). Hence an admissible prefix has \(D\ne0\). Since \(M\mid D\), this gives \(|D|\ge M\).

Also,
\[
\sum_{j=r}^s a_j
\le \sum_{j=1}^{i-1}a_j
\le C\sum_{j=1}^{i-1}j
=\frac C2(i-1)i,
\]
while \(a_i\le Ci\). Consequently
\[
|D|\le \max\left(\sum_{j=r}^s a_j,a_i\right)
\le \frac C2i(i+1).
\]
Using \(i\le2M^2+1\) proves (4). ∎

For \(M=p^k\), this yields a nonzero integer \(D\) with
\[
v_p(D)\ge k,
\qquad
|D|=O_C(p^{4k}).
\]
Thus the forced valuation is only about one quarter of the trivial logarithmic size bound. There is no contradiction.

This quantifies the central size failure of Route 4. Congruence would force equality if \(|D|<M\), but the automatic recurrence gives only
\[
|D|=O_C(M^4).
\]
Even a hypothetical improvement of Lemma 1 from \(O(M^2)\) indices to \(O(M)\) indices would, using only the global prefix-sum bound, give \(|D|=O_C(M^2)\), still insufficient.

---

### 3. Infinite \(p\)-adic recurrence does not fix the witness

There is also a natural infinite \(p\)-adic version.

#### Lemma 4
For every infinite integer sequence \(a_1,a_2,\dots\) and every prime \(p\), there are nested infinite sets of indices
\[
I_1\supseteq I_2\supseteq\cdots
\]
such that, for each \(k\), the pair
\[
(S_{i-1},S_i)\pmod{p^k}
\]
is constant as \(i\) ranges over \(I_k\).

Consequently, for every \(k\), there are indices \(r\le s<i\), with block length at least two, such that
\[
p^k\mid \left(\sum_{j=r}^s a_j-a_i\right).
\]

#### Proof
Modulo \(p\), only \(p^2\) pairs \((S_{i-1},S_i)\) are possible, so one pair occurs infinitely often; let its index set be \(I_1\).

Inductively, suppose \(I_k\) has been chosen. The common pair modulo \(p^k\) has only \(p^2\) possible refinements modulo \(p^{k+1}\). One refinement occurs infinitely often among \(I_k\); take those indices as \(I_{k+1}\).

For fixed \(k\), choose three indices \(n_1<n_2<n_3\) in \(I_k\). The repeated-edge argument from Lemma 1 gives
\[
S_{n_2}-S_{n_1-1}
\equiv
S_{n_3}-S_{n_3-1}\pmod{p^k},
\]
which is the asserted congruence with \(r=n_1,s=n_2,i=n_3\). ∎

The obstruction is that the three indices depend on \(k\). If one fixed triple worked for every \(k\), its difference would be divisible by all powers of \(p\), hence would be zero. Lemma 4 does not provide this: nested infinite sets can have empty intersection, and the selected indices can escape to infinity arbitrarily rapidly.

Likewise, applying Corollary 2 separately modulo several relatively prime moduli gives potentially different triples. The Chinese remainder theorem cannot combine congruences having different witnesses. Applying the lemma directly modulo their product \(Q\) returns to the poor bounds
\[
i=O(Q^2),\qquad |D|=O_C(Q^4).
\]

Thus basic \(p\)-adic compactness and CRT do not supply the missing equality.

---

### 4. A modular consequence: eventually periodic sets are impossible

Although fixed-modulus recurrence does not settle the density questions, it completely excludes periodic constructions.

#### Proposition 5
No infinite eventually periodic subset \(A\subseteq\mathbb Z_{>0}\) is consecutive-sum-avoiding.

#### Proof
Suppose that membership in \(A\) is eventually periodic modulo \(M\). Thus there are \(X_0\) and a nonempty residue set
\[
R\subseteq\mathbb Z/M\mathbb Z
\]
such that, for every \(n\ge X_0\),
\[
n\in A\quad\Longleftrightarrow\quad n\bmod M\in R.
\]
Let \(q=|R|\). Once the terms \(a_j\) exceed \(X_0\), their residues cycle periodically through the \(q\) elements of \(R\), in increasing order within each interval of length \(M\).

Choose \(r\) so large that every term from \(a_r\) onward is at least \(X_0\), and set
\[
L=Mq+1,\qquad s=r+Mq.
\]
The first \(Mq\) terms
\[
a_r,\dots,a_{r+Mq-1}
\]
split into \(M\) consecutive groups of \(q\) terms. Each group contains every residue in \(R\) once. Therefore their total sum is divisible by \(M\):
\[
a_r+\cdots+a_{r+Mq-1}\equiv
M\sum_{c\in R}c\equiv0\pmod M.
\]
Moreover, shifting by \(Mq\) terms preserves the residue, so
\[
a_{r+Mq}\equiv a_r\pmod M.
\]
Hence the full block sum
\[
B=a_r+\cdots+a_{r+Mq}
\]
satisfies
\[
B\equiv a_r\pmod M.
\]
This residue belongs to \(R\), and \(B\ge X_0\); therefore \(B\in A\).

Since \(L\ge2\) and all terms are positive,
\[
B>a_s.
\]
Thus \(B=a_i\) for some \(i>s\), contradicting admissibility. ∎

For the odd integers, this recovers the elementary violation
\[
1+3+5=9.
\]
For a complete arithmetic progression modulo \(M\), the argument uses a block of length \(M+1\).

This proposition only rules out an important special class and does not control aperiodic positive-density sets.

---

### 5. A stronger alternative route: packing fixed-length block sums

The following does not arise from \(p\)-adic descent, but it is stronger quantitative progress toward P1 than the modular near-miss alone.

For fixed \(k\ge2\), define
\[
B_{r,k}=a_r+a_{r+1}+\cdots+a_{r+k-1}.
\]

#### Lemma 6
For fixed \(k\ge2\), the numbers \(B_{r,k}\) are strictly increasing in \(r\), and none belongs to \(A\).

#### Proof
We have
\[
B_{r+1,k}-B_{r,k}=a_{r+k}-a_r>0,
\]
so they are strictly increasing.

Also
\[
B_{r,k}>a_{r+k-1}.
\]
If \(B_{r,k}=a_i\) for some \(i\), then necessarily \(i>r+k-1\), and \(a_i\) equals a consecutive block of earlier terms. This contradicts admissibility. ∎

#### Theorem 7
Every infinite consecutive-sum-avoiding sequence satisfies
\[
\limsup_{n\to\infty}\frac{a_n}{n}\ge\frac32.
\tag{5}
\]
Equivalently,
\[
\underline d(A)\le\frac23.
\]

More generally, if
\[
L=\limsup_{n\to\infty}\frac{a_n}{n}<\infty,
\]
then
\[
\liminf_{n\to\infty}\frac{a_n}{n}
\ge
\frac{2L}{2L-1}.
\tag{6}
\]

#### Proof
Fix \(C>L\). There is \(n_0\) such that
\[
a_n\le Cn\qquad(n\ge n_0).
\]

For large \(N\), consider all \(r\ge n_0\) satisfying
\[
C(2r+1)\le a_N.
\tag{7}
\]
For every such \(r\),
\[
a_r+a_{r+1}
\le Cr+C(r+1)
=C(2r+1)
\le a_N.
\]
By Lemma 6, these pair sums are distinct integers in \([1,a_N]\) not belonging to \(A\).

The number of such \(r\) is
\[
\frac{a_N}{2C}+O_{C,n_0}(1).
\]
There are exactly \(N\) elements of \(A\) in \([1,a_N]\), so that interval contains \(a_N-N\) holes. Therefore
\[
a_N-N
\ge
\frac{a_N}{2C}-O_{C,n_0}(1).
\]
Dividing by \(N\) and writing \(x_N=a_N/N\), we obtain
\[
x_N\left(1-\frac1{2C}\right)\ge1-o(1).
\]
Hence
\[
\liminf_{N\to\infty}x_N
\ge
\frac{1}{1-\frac1{2C}}
=
\frac{2C}{2C-1}.
\]
Letting \(C\downarrow L\) proves (6).

Since the liminf cannot exceed the limsup,
\[
L\ge \frac{2L}{2L-1}.
\]
As \(L\ge1\), this is equivalent to
\[
2L-1\ge2,
\]
and hence \(L\ge3/2\). If \(L=\infty\), (5) is automatic. ∎

The same argument with blocks of a fixed length \(k\ge2\) gives only
\[
L\ge1+\frac1k;
\]
the case \(k=2\) is strongest among these one-length packing arguments.

There is also a residuewise form. For a modulus \(m\), a cutoff \(X\), and residue \(c\), let
\[
A_c(X)=\#\{a_i\le X:a_i\equiv c\pmod m\},
\]
and let
\[
B_{k,c}(X)
=
\#\{r:B_{r,k}\le X,\ B_{r,k}\equiv c\pmod m\}.
\]
Then Lemma 6 gives the exact packing inequality
\[
A_c(X)+B_{k,c}(X)
\le
\#\{1\le n\le X:n\equiv c\pmod m\}.
\tag{8}
\]
Summing (8) over residues recovers the ordinary packing bound. To improve it using modular information, one needs nontrivial lower bounds on the distribution of block sums among residue classes. No such universal bound was obtained.

---

### 6. Ledger

**Proved**

1. Every residue word of length \(>2M^2\) has a chronological modular violation.
2. Under \(a_i\le Ci\), this forces a nonzero divisible near-miss of size between \(M\) and \(O_C(M^4)\).
3. Infinite \(p\)-adic edge recurrence is automatic, but its witnesses may vary with the precision.
4. No eventually periodic set is admissible.
5. Every admissible sequence has
   \[
   \limsup a_n/n\ge3/2,
   \qquad
   \underline d(A)\le2/3.
   \]
6. The residuewise packing inequalities (8) hold for every fixed block length.

**Plausible but unproved**

1. The additional structure
   \[
   a_n=n+b_n,\qquad b_{n+1}\ge b_n,
   \]
   may force much faster or more size-controlled modular recurrence than is possible for arbitrary residue words.
2. Several block lengths together may produce substantially more distinct forbidden values than the fixed-length argument detects.
3. A useful theorem would bound collisions between the increasing sequences
   \[
   \{B_{r,k}\}_r
   \]
   for many different \(k\), perhaps after decomposition into residue or valuation classes.

**Dead ends**

1. **Single-modulus pigeonhole:** the forced modulus is far smaller than the possible error.
2. **Naive CRT:** different moduli generally produce different triples.
3. **Nested \(p\)-adic compactness:** the witness indices escape; no fixed difference is divisible by all powers.
4. **Residue thinning from recurrence:** false without a quantitative upper bound on nonzero high-valuation near-misses. Modular near-misses occur even in admissible sparse examples.
5. **Fixed block length packing:** gives at best the \(3/2\) bound, not divergence of \(a_n/n\).

## Self-Audit

1. **The indexing in Lemma 1 is the most delicate point.**  
   A repeated edge at \(n_1<n_2<n_3\) produces the block \(n_1,\dots,n_2\), not merely a singleton. Its length is \(n_2-n_1+1\ge2\), and it ends before \(n_3\). Thus it has exactly the required chronology.

2. **The passage from eventual \(a_n\le Cn\) to the \(3/2\) bound uses initial exceptions.**  
   I discarded all pair sums beginning before a fixed \(n_0\). This loses only \(O(1)\) terms. The eligible pair-sum count remains \(a_N/(2C)+O(1)\), so the asymptotic inequality is unaffected.

3. **The periodicity proposition assumes eventual periodicity of membership, not merely periodic term residues along a subsequence.**  
   This stronger hypothesis is essential when concluding that the constructed block sum belongs to \(A\). Under that stated hypothesis, every sufficiently large integer in an allowed residue class is indeed in \(A\), so the proof is complete. It does not extend automatically to automatic or substitutional sets.

The decisive weakness is not a hidden gap but the stated block: none of the modular lemmas converts congruence into equality under a fixed linear bound.

## Computations To Verify

```python
# 1. Direct admissibility checker

def admissible(a):
    assert all(a[i] < a[i+1] for i in range(len(a)-1))
    S = [0]
    forbidden = set()
    for v in a:
        if v in forbidden:
            return False
        newS = S[-1] + v
        for oldS in S:
            forbidden.add(newS - oldS)
        S.append(newS)
    return True
```

```python
# 2. Find the repeated-edge modular witness from Lemma 1.
# Returns 1-based indices (r,s,i).

def edge_witness(a, M):
    S = [0]
    positions = {}
    for idx, v in enumerate(a, start=1):
        S.append(S[-1] + v)
        edge = (S[idx-1] % M, S[idx] % M)
        positions.setdefault(edge, []).append(idx)
        if len(positions[edge]) == 3:
            n1, n2, n3 = positions[edge]
            B = sum(a[n1-1:n2])
            assert n2 - n1 + 1 >= 2
            assert n2 < n3
            assert (B - a[n3-1]) % M == 0
            return n1, n2, n3, B - a[n3-1]
    return None

# For random words of length 2*M*M+1, this must never return None.
```

```python
# 3. Exhaustive search for the longest residue word avoiding
# all chronological modular violations. Feasible only for small M.

def modular_bad(prior, x, M):
    # Is x equal mod M to a block of length >= 2 entirely in prior?
    P = [0]
    for y in prior:
        P.append((P[-1] + y) % M)

    n = len(prior)
    for r in range(n):
        for s in range(r + 1, n):  # block length >= 2
            if (P[s+1] - P[r] - x) % M == 0:
                return True
    return False

def longest_modular_word(M):
    best = []

    def dfs(word):
        nonlocal best
        if len(word) > len(best):
            best = word[:]

        # Lemma 1 says no legal word has length > 2*M^2.
        if len(word) == 2 * M * M:
            assert all(modular_bad(word, x, M) for x in range(M))
            return

        for x in range(M):
            if not modular_bad(word, x, M):
                dfs(word + [x])

    dfs([])
    return best

# Suggested experiment:
# for M in range(1, 9):
#     w = longest_modular_word(M)
#     print(M, len(w), w)
#
# This tests whether the true extremal length may be O(M), although
# even such an improvement would not by itself fix the size problem.
```

```python
# 4. Enumerate every modular near-miss in a finite prefix and record
# its block length and quotient D/M.

def congruent_witnesses(a, M):
    N = len(a)
    S = [0]
    for v in a:
        S.append(S[-1] + v)

    out = []
    for i in range(2, N):           # 0-based target
        for r in range(i):
            for s in range(r + 1, i):  # length at least two
                B = S[s+1] - S[r]
                D = B - a[i]
                if D % M == 0:
                    out.append({
                        "r": r + 1,
                        "s": s + 1,
                        "i": i + 1,
                        "length": s - r + 1,
                        "D": D,
                        "quotient": D // M
                    })
    return out

# For fixed-C extremal prefixes, record:
#   min(abs(D)) for each M,
#   min block length,
#   frequency of D == 0,
#   distribution of D/M.
```

```python
# 5. Fixed-C exact backtracking search.
# C is represented as numerator/denominator to avoid floating error.

def fixed_C_prefixes(C_num, C_den, target_depth):
    best = []
    survivors = [0] * (target_depth + 1)

    def cap(i):  # i is 1-based
        return (C_num * i) // C_den

    def dfs(a, S, forbidden):
        nonlocal best
        m = len(a)
        survivors[m] += 1
        if m > len(best):
            best = a[:]
        if m == target_depth:
            return

        lo = 1 if m == 0 else a[-1] + 1
        hi = cap(m + 1)

        for v in range(lo, hi + 1):
            if v in forbidden:
                continue

            newS = S[-1] + v
            new_forbidden = forbidden.copy()
            for oldS in S:
                new_forbidden.add(newS - oldS)

            dfs(a + [v], S + [newS], new_forbidden)

    dfs([], [0], set())
    return best, survivors
```

```python
# 6. Verify the pair-sum packing used for Theorem 7.

def pair_holes(a, N=None):
    if N is None:
        N = len(a)
    prefix = a[:N]
    assert admissible(prefix)

    X = prefix[-1]
    Aset = set(prefix)
    pairs = []

    for r in range(N - 1):
        p = prefix[r] + prefix[r+1]
        if p <= X:
            assert p not in Aset
            pairs.append(p)

    assert len(pairs) == len(set(pairs))
    assert N + len(pairs) <= X
    return X, N, pairs
```

```python
# 7. Verify the eventual-periodic obstruction for a residue set R.

def periodic_violation(M, residues, X0):
    residues = set(r % M for r in residues)
    assert residues
    q = len(residues)
    L = M * q + 1

    terms = []
    x = X0
    while len(terms) < L:
        if x % M in residues:
            terms.append(x)
        x += 1

    B = sum(terms)
    assert B % M == terms[0] % M
    assert B % M in residues
    assert B > terms[-1]
    return terms, B
```

## Route Diagnosis

The successful part of Route 4 is a clean finite-state recurrence theorem: chronological congruences are unavoidable modulo every fixed modulus, and repeated-edge arguments preserve the required ordering. The route fails precisely at the transition from congruence to equality. With \(N\) terms under a linear bound, prefix differences can have size \(O(N^2)\). Modular recurrence obtained from \(M^2\) edge states only becomes automatic around \(N\asymp M^2\), where the possible error is \(O(M^4)\), not \(<M\). CRT and \(p\)-adic nesting do not improve this because they either enlarge the state space or change the witness.

The best alternative found was fixed-length packing, yielding the rigorous bound \(\limsup a_n/n\ge3/2\). To go further, a fresh attempt should combine several block lengths and prove that their values have low cross-length collision multiplicity under
\[
a_n=n+b_n,\qquad b_n\ \text{nondecreasing}.
\]
Equivalently, one needs a structural theorem showing that many of the block sums below \(a_N\) are distinct. A modular version would need residuewise lower bounds in (8), or a dichotomy saying that concentration of block sums in a few residue classes forces a genuine \(p\)-adic descent. Establishing such a theorem appears comparable in difficulty to the original problem; without it, Route 4 is blocked.