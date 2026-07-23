STATUS: BLOCKED

## Result

For the required **universal** interpretation, Route 4 does not presently yield a solution of \((2,3)\). I prove that ordinary independent mixed-radix block constructions cannot work: pair-erasure tolerance in independent blocks always permits a harmless triple spread across different blocks. I also derive necessary “gap-shift” and modular conditions for any genuine universal construction. On the positive side, Route 4 completely solves the **existential** interpretation: for every \(0\le m<n\), an explicit repeated mixed-radix sequence survives every \(m\)-deletion and has some fatal \(n\)-deletion. Thus the quantifier distinction is decisive.

## Complete Argument

### 1. A complete solution under the existential interpretation

#### Theorem 1

For every pair \(0\le m<n\), there is an infinite nondecreasing sequence which remains strongly complete after every deletion of \(m\) terms, but becomes weakly incomplete after some deletion of \(n\) terms.

#### Proof

The case \(m=0\) is supplied by the powers of two.

Now let \(m\ge1\), put
\[
q=m+1,
\]
and define \(A_m\) to contain exactly \(2m\) indexed copies of each power
\[
1,q,q^2,q^3,\ldots.
\]
Thus
\[
A_m=(\underbrace{1,\ldots,1}_{2m},
\underbrace{q,\ldots,q}_{2m},
\underbrace{q^2,\ldots,q^2}_{2m},\ldots).
\]

##### Robustness after every \(m\)-deletion

Delete any \(m\) indexed terms. At each level \(q^k\), at least
\[
2m-m=m=q-1
\]
copies remain. Select \(q-1\) surviving copies from every level. Every nonnegative integer has a base-\(q\) expansion
\[
x=\sum_{k\ge0}d_kq^k,\qquad 0\le d_k\le q-1,
\]
with only finitely many nonzero digits. Selecting \(d_k\) of the chosen copies of \(q^k\) represents \(x\).

Hence every \(m\)-deletion leaves a strongly complete sequence.

##### A fatal \((m+1)\)-deletion

Fix a level \(k\), and delete \(m+1\) of the \(2m\) copies of \(q^k\). There remain \(m-1\) copies at that level.

Let
\[
Q=q^{k+1}.
\]
All terms above level \(k\) are divisible by \(Q\). The largest possible contribution from levels below \(k\) is
\[
2m\sum_{r=0}^{k-1}q^r
=
2m\frac{q^k-1}{q-1}
=
2(q^k-1),
\]
because \(q-1=m\). The remaining copies at level \(k\) contribute at most
\[
(m-1)q^k.
\]
Consequently the total contribution from levels at most \(k\) is at most
\[
2(q^k-1)+(m-1)q^k
=(m+1)q^k-2
=q^{k+1}-2
=Q-2.
\]

Therefore no subset sum is congruent to \(Q-1\pmod Q\): terms above level \(k\) contribute \(0\pmod Q\), while terms at or below level \(k\) contribute an integer between \(0\) and \(Q-2\). Thus all integers
\[
Q-1,\ 2Q-1,\ 3Q-1,\ldots
\]
are missing. The resulting sequence is weakly incomplete.

For \(n>m+1\), enlarge this fatal deletion set arbitrarily to one of size \(n\). Further deletion cannot restore any representation. This proves the theorem. ∎

#### Consequence

If Erdős Problem #348 intended the existential quantifier
\[
\exists J,\quad |J|=n,\quad A\setminus J\text{ incomplete},
\]
then every admissible pair \(0\le m<n\) is possible, and the classification is complete.

---

### 2. Why this construction fails the universal requirement

For every finite \(n\), choose \(n\) distinct levels and delete one occurrence from each. At every level at least
\[
2m-1\ge m=q-1
\]
copies remain. The remaining sequence therefore still contains \(q-1\) copies of every \(q^k\), so it is strongly complete by the base-\(q\) argument.

Thus \(A_m\) is not universally \(n\)-fragile for any finite \(n\). In particular, for \(m=2\), four copies of every ternary power survive every two-deletion, and deletion of three copies from one level is fatal, but a triple spread over three levels is harmless.

This is the fundamental “spread erasure” obstruction for independent blocks.

---

### 3. No-go theorem for carry-free mixed-radix blocks

The preceding obstruction does not depend only on using repeated powers.

#### Definition

Let
\[
q_0=1,\qquad q_{k+1}=r_kq_k,\qquad r_k\ge2.
\]
Suppose the indices are partitioned into finite nonempty blocks \(B_k\). Call the system **independent-digit** if, after every finite deletion \(D\), there are local sets
\[
L_k(D\cap B_k)\subseteq\{0,1,\ldots,r_k-1\}
\]
such that
\[
\Sigma(A\setminus D)
=
\left\{
\sum_{k\ge0}d_kq_k:
d_k\in L_k(D\cap B_k),\ 
d_k=0\text{ for all but finitely many }k
\right\}.
\]
Thus choices in different blocks factor completely and no carry state couples different levels.

#### Theorem 2

No independent-digit system can be both two-deletion robust and universally \(n\)-deletion fragile for any finite \(n\ge3\).

#### Proof

Mixed-radix expansion with digits \(0\le d_k<r_k\) is unique.

If, for some \(s\), the local digit set \(L_s(E)\) omits a digit \(d\), then infinitely many integers having mixed-radix digit \(d\) at position \(s\) are absent from the global subset-sum set. Conversely, if every local digit set is full, every nonnegative integer is represented. Therefore
\[
A\setminus D\text{ is complete}
\iff
L_k(D\cap B_k)=\{0,\ldots,r_k-1\}
\quad\text{for every }k.
\tag{1}
\]

Assume every two-deletion leaves a complete sequence. Fix a block \(B_k\) and a subset \(E\subseteq B_k\) with \(|E|\le2\).

- If \(|E|=2\), take \(D=E\).
- If \(|E|=1\), add one index from another block to make a two-set \(D\).
- If \(E=\varnothing\), choose two deleted indices outside \(B_k\).

In each case \(A\setminus D\) is complete, so by (1)
\[
L_k(E)=\{0,\ldots,r_k-1\}.
\tag{2}
\]

Now choose \(n\) indices lying in \(n\) distinct blocks, one from each block. Every affected block has suffered only one local deletion, and every unaffected block has suffered none. By (2), all its digit sets remain full. Hence the resulting sequence is strongly complete.

This supplies an \(n\)-deletion which is harmless, contradicting universal \(n\)-fragility. ∎

#### Interpretation

Any successful Route 4 construction must therefore have genuine, unbounded carry coupling. A deletion at one level must leave a latent state which remains relevant arbitrarily far into the future. Local erasure correction followed by a reset cannot suffice.

---

### 4. Necessary gap structure for a hypothetical universal \((2,3)\) example

The next lemma applies to every possible construction, not just block systems.

#### Lemma 3: gap-shift condition

Suppose \(A\) is two-deletion robust and universally three-deletion fragile. Fix
\[
J=\{i,j,k\}
\]
and put
\[
C_J=\Sigma(A\setminus J),\qquad
G_J=\mathbb N_0\setminus C_J.
\]
Then \(G_J\) is infinite, and for each \(t\in J\), every sufficiently large \(x\in G_J\) satisfies
\[
x-a_t\in C_J.
\tag{3}
\]
Equivalently,
\[
G_J\cap(G_J+a_t)
\]
is finite for every \(t\in J\).

#### Proof

Universal three-fragility makes \(G_J\) infinite.

For \(t\in J\), deleting the other two elements of \(J\) leaves
\[
(A\setminus J)\cup\{a_t\},
\]
which is complete by two-deletion robustness. Its subset-sum support is exactly
\[
C_J\cup(a_t+C_J),
\]
because a representation either does not use the indexed occurrence \(t\), or uses it exactly once.

Hence there is \(N_t\) such that every \(x\ge N_t\) lies in this union. If \(x\in G_J\) and \(x\ge\max(N_t,a_t)\), then \(x\notin C_J\), so necessarily
\[
x\in a_t+C_J,
\]
which is precisely (3).

If both \(y\) and \(y+a_t\) were sufficiently large gaps, applying (3) to \(y+a_t\) would imply \(y\in C_J\), a contradiction. ∎

This shows that the gaps caused by a triple cannot be a thick or elementary periodic defect. They must be sparse enough that adding any one of the deleted terms repairs all sufficiently large gaps.

#### Corollary 4: restriction on modular obstructions

If \(A\setminus J\) omits an entire residue class modulo \(q\), then
\[
q\nmid a_t\qquad(t\in J).
\]

More generally, if its eventual gap residues form a nonempty set \(R\subseteq\mathbb Z/q\mathbb Z\), then
\[
R\cap(R+a_t)=\varnothing
\qquad(t\in J).
\]

#### Proof

If \(q\mid a_t\) and all sufficiently large integers in a residue \(r\pmod q\) are gaps, then for arbitrarily large \(x\equiv r\pmod q\), both \(x\) and \(x-a_t\) are gaps. This contradicts Lemma 3.

The same argument gives the statement for an arbitrary periodic residue set \(R\). ∎

Thus a successful carry automaton cannot simply enter a state omitting a residue class modulo a divisor of one of the erased terms.

---

### 5. Tail-divisibility constraints on mixed-radix attempts

#### Lemma 5

Suppose \(q\ge2\) divides every \(a_i\) with \(i>K\). For a finite deletion set \(D\), let
\[
P_{K,D}=\{a_i:1\le i\le K,\ i\notin D\}.
\]
Then:

1. If \(A\setminus D\) is complete, the subset sums of \(P_{K,D}\) cover every residue modulo \(q\).
2. If those prefix subset sums omit a residue modulo \(q\), then \(A\setminus D\) is weakly incomplete.
3. Deleting terms whose indices are all greater than \(K\) does not change the set of attainable residues modulo \(q\).

#### Proof

Every surviving tail term is \(0\pmod q\). Hence all subset-sum residues modulo \(q\) come solely from the surviving prefix.

If \(A\setminus D\) is complete, every residue class contains sufficiently large represented integers, proving part 1. If a residue is absent, every integer in that residue class is unrepresentable, proving part 2. Part 3 follows because the deleted tail terms all have residue zero. ∎

#### Consequences for Route 4

If \(A\) were two-deletion robust and \(q\) divided a tail, then for every pair \(D\) in the corresponding prefix,
\[
\Sigma(P_{K,D})\pmod q=\mathbb Z/q\mathbb Z.
\]
Thus every cut must carry a finite two-erasure subset-sum code.

A fixed modulus cannot certify fragility of triples lying entirely beyond the point where the tail becomes divisible by that modulus. One therefore needs an unbounded hierarchy of moduli and compatible erasure codes.

There is also a basic obstruction to a tempting diagonal construction. Suppose
\[
q_s\to\infty
\]
and \(q_s\) divides the tail after a cut \(K_s\). For every fixed old term \(a_i>0\), once \(q_s>a_i\),
\[
a_i\not\equiv0\pmod{q_s}.
\]
Hence old terms cannot be made inactive in all later modular checks. In particular, the local four-coordinate ternary code cannot simply be reassigned at later and later scales to target arbitrary triples while making all other old coordinates zero.

---

### 6. A boundedness reduction

#### Lemma 6

Any universally finitely deletion-fragile complete sequence has \(a_i\to\infty\).

#### Proof

Suppose some value \(v\) occurs infinitely often. Choose a deletion set \(J\) consisting only of finitely many occurrences of \(v\). Removing these copies does not change the subset-sum set: every representation uses only finitely many occurrences of \(v\), and any deleted occurrences can be replaced by surviving occurrences of the same value.

Thus
\[
\Sigma(A\setminus J)=\Sigma(A).
\]
If \(A\) is complete, so is \(A\setminus J\), contradicting universal finite-deletion fragility.

A nondecreasing bounded integer sequence has some value occurring infinitely often, so it is excluded. ∎

---

### 7. Ledger

#### Proved

1. The existential interpretation is possible for every \(0\le m<n\), using \(2m\) copies of every \((m+1)\)-st radix power.
2. The construction is strongly \(m\)-deletion robust and has an explicit modularly fatal \((m+1)\)-deletion.
3. The same construction is never universally finitely fragile, because deletions can be spread across distinct levels.
4. No carry-free independent-digit block system can realize universal \((2,3)\), or universal finite fragility at any later deletion count.
5. Every hypothetical universal \((2,3)\) example satisfies the gap-shift condition of Lemma 3.
6. Simple modular obstructions must avoid divisors of all three deleted values.
7. Tail-divisibility cuts impose finite two-erasure residue-code conditions.
8. A hypothetical example must have \(a_i\to\infty\).

#### Plausible but unproved

1. Any successful construction must retain a permanent erasure syndrome recording up to three deletions; no bounded-reset carry system can work.
2. A sufficiently strong finite-state arithmetic realization theorem might rule out such permanent syndromes and prove nonexistence.
3. Alternatively, a non-reset convolutional numeration system might realize states
   \[
   G_0\to G_1\to G_2\to B,
   \]
   where the first three states have cofinite support and \(B\) has sparse gaps satisfying Lemma 3. No arithmetic realization is known.

#### Dead ends

1. **Independent redundant radix blocks:** concentrated triples are fatal, but spread triples are harmless.
2. **Repeating a local \((2,3)\) erasure code at every digit:** the code corrects each separated erasure independently, so it cannot detect the total number of erasures.
3. **Assigning a new modular check to each triple:** old positive terms cannot be made zero modulo an unbounded sequence of later tail moduli.
4. **Assuming pair robustness causes the carry state to reset:** this is false as a general principle; Fibonacci’s one-deletion behavior already demonstrates persistent but nonfatal defect states.

## Self-Audit

1. **The universal problem remains unsolved.**  
   The principal limitation is substantive, not cosmetic: the no-go theorem covers only systems whose digit states factor by block. I have not proved that every mixed-radix carry construction eventually factorizes or resets.

2. **The existential construction relies on a residue bound rather than a complete description of all subset sums.**  
   This is nevertheless sufficient and rigorous: after the concentrated deletion, every lower-level contribution lies in \([0,Q-2]\), while every higher term is divisible by \(Q\), so residue \(Q-1\) is impossible.

3. **The modular and gap-shift lemmas are necessary conditions, not close to a contradiction.**  
   Their proofs are exact, but sparse nonperiodic gap sets can satisfy all of them. Additional arithmetic structure of restricted subset sums is needed to turn them into a nonexistence theorem.

## Computations To Verify

```python
from itertools import combinations

def repeated_radix_terms(m, levels):
    """Indexed terms (value, level, copy)."""
    q = m + 1
    return [
        (q**k, k, c)
        for k in range(levels)
        for c in range(2*m)
    ]

def subset_sum_bits(indexed_terms, deleted, limit):
    bits = 1
    mask = (1 << (limit + 1)) - 1
    for idx, (value, level, copy) in enumerate(indexed_terms):
        if idx not in deleted:
            bits |= bits << value
            bits &= mask
    return bits

def contains_interval(bits, lo, hi):
    mask = ((1 << (hi - lo + 1)) - 1) << lo
    return (bits & mask) == mask

def verify_all_m_deletions(m, levels):
    """
    Finite verification of the canonical interval
    [0, (m+1)^levels - 1] after every m-deletion
    among the tested levels.
    """
    terms = repeated_radix_terms(m, levels)
    q = m + 1
    limit = q**levels - 1
    for D in combinations(range(len(terms)), m):
        bits = subset_sum_bits(terms, set(D), limit)
        if not contains_interval(bits, 0, limit):
            return False, D
    return True, None

def residue_support(indexed_terms, deleted, modulus):
    R = {0}
    for idx, (value, level, copy) in enumerate(indexed_terms):
        if idx in deleted:
            continue
        v = value % modulus
        R |= {(r + v) % modulus for r in list(R)}
    return R

def verify_concentrated_fatal_deletion(m, level, extra_levels=3):
    """
    Delete m+1 copies at one level and verify that
    Q-1 mod Q is absent.
    """
    levels = level + 1 + extra_levels
    terms = repeated_radix_terms(m, levels)
    q = m + 1
    Q = q**(level + 1)

    at_level = [
        idx for idx, (_, k, _) in enumerate(terms) if k == level
    ]
    deleted = set(at_level[:m+1])

    R = residue_support(terms, deleted, Q)
    return (Q - 1) not in R, sorted(set(range(Q)) - R)

def verify_spread_deletion_is_harmless(m, n, levels=None):
    """
    Delete one term at each of n distinct levels.
    Check the canonical interval through the tested levels.
    """
    if levels is None:
        levels = n + 2
    terms = repeated_radix_terms(m, levels)
    q = m + 1

    deleted = set()
    for k in range(n):
        idx = next(
            i for i, (_, level, _) in enumerate(terms)
            if level == k and i not in deleted
        )
        deleted.add(idx)

    limit = q**levels - 1
    bits = subset_sum_bits(terms, deleted, limit)
    return contains_interval(bits, 0, limit)

# Suggested checks:
print(verify_all_m_deletions(m=2, levels=5))
print(verify_concentrated_fatal_deletion(m=2, level=3))
print(verify_spread_deletion_is_harmless(m=2, n=3))
print(verify_spread_deletion_is_harmless(m=2, n=20, levels=22))
```

For a recurrence-based controlled-carry candidate, the following diagnostic tests the necessary gap-shift condition on finite prefixes:

```python
def finite_support(values, deleted, limit):
    bits = 1
    mask = (1 << (limit + 1)) - 1
    for i, value in enumerate(values):
        if i not in deleted:
            bits |= bits << value
            bits &= mask
    return bits

def gap_shift_violations(values, triple, limit, lower_cutoff=0):
    """
    For J=triple, list finite-prefix gaps x for which x-a_j
    is also a gap. In a genuine candidate these violations must
    disappear, for each fixed J, as the prefix and cutoff grow.
    """
    bits = finite_support(values, set(triple), limit)
    gaps = {
        x for x in range(lower_cutoff, limit + 1)
        if ((bits >> x) & 1) == 0
    }

    out = {}
    for j in triple:
        a = values[j]
        out[j] = [
            x for x in gaps
            if x >= a and (x - a) in gaps
        ]
    return out
```

Finite-prefix violations are not by themselves disproofs, because later terms can represent targets above their values. To obtain a rigorous disproof from this computation, one should find a symbolic recurrent state producing such violations at unbounded scales.

## Route Diagnosis

The local coding problem is easy: four unit coordinates modulo \(3\) tolerate two erasures and fail after three. The obstruction is global quantification. Independent blocks detect only how many deletions occurred in each block, so a triple distributed among three blocks is corrected. Any successful universal construction must make every deletion leave a permanent carry syndrome visible at all later scales, while one or two such syndromes still allow eventual representation of every integer.

Route 4 is therefore blocked at the following precise coding theorem:

> Construct, or rule out, a restricted integer numeration system with non-reset carry states in which every state reachable after at most two arbitrary term erasures has cofinite support, while every state reachable after three arbitrary erasures has infinitely many sparse gaps satisfying the gap-shift condition.

Proving that all arithmetic carry systems eventually reset would essentially be a nonexistence proof and is currently unsupported. Conversely, an abstract four-state erasure automaton is easy to write, but realizing it by subset sums of fixed positive integers is the unresolved arithmetic step.

A fresh constructive attempt should search directly for a non-reset convolutional numeration system rather than independent digit blocks. A fresh nonexistence attempt should exploit Lemma 3 in representation-hypergraph form: for every triple \(J\), infinitely many targets have \(J\) as a transversal, yet deleting any one member of \(J\) must expose a representation whose remainder lies in the same three-deleted support. This appears more promising than further purely local mixed-radix coding.