STATUS: BLOCKED

## Result

Under the universal interpretation, I did not resolve \((m,n)=(2,3)\). I obtained several rigorous structural consequences of a hypothetical example. Most importantly, every fixed triple must recur infinitely often as an inclusion-minimal transversal of the representation hypergraphs; deleting any pair produces a minimal complete sequence; and for every four indexed terms, the remaining core is incomplete after restoring any one of them but complete after restoring any two. I also proved strong restrictions on gcd-based obstructions and constructed counterexamples showing that neither abstract hypergraph compactness nor any purely local “four repair terms” argument can yield the desired contradiction. The route is therefore blocked precisely at the need for a global arithmetic-coherence theorem linking representation hypergraphs at different target sums and for overlapping deletion sets.

## Complete Argument

Assume throughout this section, for the purpose of deriving necessary conditions, that \(A=(a_i)_{i\ge1}\) is \(2\)-deletion robust and universally \(3\)-deletion fragile.

### 1. The sequence must tend to infinity

**Lemma 1.** The sequence \(A\) is unbounded, and hence \(a_i\to\infty\).

**Proof.** If \(A\) were bounded, then, being nondecreasing and integer-valued, it would eventually be constant, say \(a_i=c\) for all \(i\ge i_0\).

Choose three distinct indices \(p,q,r\ge i_0\). Since infinitely many copies of \(c\) remain after any finite deletion,
\[
\Sigma(A\setminus\{p,q\})
=
\Sigma(A\setminus\{p,q,r\}).
\]
Indeed, any finite use of the deleted copies can be replaced by surviving indexed copies of the same value \(c\).

The left-hand sequence is complete by \(2\)-deletion robustness, while the right-hand sequence is incomplete by universal \(3\)-deletion fragility, a contradiction. Thus \(A\) is unbounded. Since it is nondecreasing, \(a_i\to\infty\). ∎

Consequently, for each fixed \(x\), only finitely many terms of \(A\) can occur in a representation of \(x\).

---

### 2. Exact hypergraph formulation

For \(x\ge0\), define the finite representation hypergraph
\[
\mathcal R_x
=
\left\{
F\subseteq\mathbb N:
F\text{ finite and }\sum_{i\in F}a_i=x
\right\}.
\]
Its vertices may be restricted to the finite set \(\{i:a_i\le x\}\).

For a finite index set \(D\), let
\[
T(D)=\{x\ge0:D\cap F\ne\varnothing\text{ for every }F\in\mathcal R_x\}.
\]

**Lemma 2.** For every finite \(D\),
\[
T(D)=\mathbb N_0\setminus\Sigma(A\setminus D).
\]

**Proof.** The number \(x\) belongs to \(\Sigma(A\setminus D)\) precisely when it has a representation \(F\in\mathcal R_x\) disjoint from \(D\). Negating this statement gives the assertion. This also covers \(\mathcal R_x=\varnothing\), since then every \(D\) is vacuously a transversal. ∎

Therefore the assumed properties are exactly:

1. \(T(P)\) is finite for every pair \(P\);
2. \(T(J)\) is infinite for every triple \(J\).

Because \(T(P)\subseteq T(J)\) whenever \(P\subseteq J\), the second statement is much stronger than merely saying that some targets have transversal number three.

**Lemma 3.** For every triple \(J=\{p,q,r\}\), there are infinitely many \(x\) for which \(J\) is an inclusion-minimal transversal of \(\mathcal R_x\).

For every such \(x\), there are representations \(F_p,F_q,F_r\in\mathcal R_x\) satisfying
\[
F_p\cap J=\{p\},\qquad
F_q\cap J=\{q\},\qquad
F_r\cap J=\{r\}.
\]

**Proof.** The union
\[
T(\{p,q\})\cup T(\{p,r\})\cup T(\{q,r\})
\]
is finite. Removing it from the infinite set \(T(J)\) leaves infinitely many \(x\).

For such an \(x\), \(J\) is a transversal but none of its two-element subsets is. Since \(\{q,r\}\) is not a transversal, there is a representation \(F_p\) disjoint from \(\{q,r\}\). As \(J\) is a transversal, this representation must contain \(p\). Thus \(F_p\cap J=\{p\}\). The other two representations are obtained symmetrically. ∎

Writing
\[
F_j=\{j\}\cup E_j,\qquad E_j\subseteq\mathbb N\setminus J,
\]
one obtains
\[
\sum_{i\in E_j}a_i=x-a_j,\qquad j\in J.
\]
Thus every triple must support infinitely many three-way equal-sum exchanges
\[
a_p+\sum_{i\in E_p}a_i
=
a_q+\sum_{i\in E_q}a_i
=
a_r+\sum_{i\in E_r}a_i.
\]

After cancelling common indices between two \(E_j\)'s, this gives disjoint signed subset-sum relations outside \(J\), for example
\[
a_p+\sum_{i\in E_p\setminus E_q}a_i
=
a_q+\sum_{i\in E_q\setminus E_p}a_i.
\]

The missing ingredient is control of how these relations for different targets and overlapping triples interact.

---

### 3. Hole-neighbour structure after a triple deletion

Fix a triple \(J=\{p,q,r\}\), and put
\[
B=A\setminus J,\qquad S=\Sigma(B),\qquad H=\mathbb N_0\setminus S.
\]
The set \(H\) is infinite.

For each \(j\in J\), the sequence
\[
B\cup\{a_j\}=A\setminus(J\setminus\{j\})
\]
is complete, because only two terms have been deleted. Its support is exactly
\[
S\cup(a_j+S).
\]

**Lemma 4.** For every \(j\in J\), all sufficiently large \(h\in H\) satisfy
\[
h-a_j\in S
\quad\text{and}\quad
h+a_j\in S.
\]

**Proof.** Choose \(N_j\) such that
\[
[N_j,\infty)\subseteq S\cup(a_j+S).
\]

Let \(h\in H\) be sufficiently large. Since \(h\notin S\) but \(h\ge N_j\), it must lie in \(a_j+S\), so
\[
h-a_j\in S.
\]

Now consider \(h+a_j\). If \(h+a_j\notin S\), completeness of \(S\cup(a_j+S)\) would force
\[
h+a_j=a_j+s
\]
for some \(s\in S\). This gives \(h=s\in S\), contradicting \(h\in H\). Hence \(h+a_j\in S\). ∎

Thus the infinite hole set \(H\) is eventually independent with respect to all three distances:
\[
H\cap(H+a_j)\text{ is finite},\qquad j\in J.
\]
This is a necessary but far from sufficient condition; arbitrary infinite subsets of the integers can easily avoid finitely many prescribed distances.

---

### 4. Every pair deletion is a minimal complete sequence

**Lemma 5.** For every pair \(P\), the sequence \(A\setminus P\) is complete, but deletion of any further remaining indexed term makes it incomplete.

**Proof.** Completeness is exactly \(2\)-deletion robustness. If \(r\notin P\), then
\[
(A\setminus P)\setminus\{r\}=A\setminus(P\cup\{r\})
\]
is incomplete by universal \(3\)-deletion fragility. ∎

Equivalently, every pair-deleted sequence is a minimal weakly complete restricted basis.

There is also a useful recursive formulation.

**Corollary 6.** For every index \(p\), the sequence \(A\setminus\{p\}\) is \(1\)-deletion robust and universally \(2\)-deletion fragile.

**Proof.** Deleting any one further term from \(A\setminus\{p\}\) amounts to deleting two terms from \(A\), hence leaves a complete sequence. Deleting any two further terms amounts to deleting three terms from \(A\), hence leaves an incomplete sequence. ∎

Thus every one-term deletion of a hypothetical \((2,3)\) example would itself be a full universal \((1,2)\) example.

---

### 5. Four-term cores have an exact two-out-of-four repair property

Let \(K=\{i_1,i_2,i_3,i_4\}\) be any four distinct indexed occurrences, and let
\[
C=A\setminus K,\qquad S_C=\Sigma(C).
\]

**Lemma 7.** For every \(i\in K\), the sequence \(C\cup\{a_i\}\) is incomplete, while for every distinct \(i,j\in K\), the sequence \(C\cup\{a_i,a_j\}\) is complete.

**Proof.** Restoring one element of \(K\) leaves three elements deleted from \(A\), so universal \(3\)-fragility gives incompleteness. Restoring two elements leaves only two elements deleted, so \(2\)-robustness gives completeness. ∎

In translate language,
\[
\Sigma(C\cup\{a_i\})=S_C\cup(a_i+S_C)
\]
is incomplete, while
\[
S_C\cup(a_i+S_C)\cup(a_j+S_C)\cup(a_i+a_j+S_C)
\]
is cofinite for every pair \(i\ne j\).

This looks restrictive, but the following exact arithmetic construction shows that it is locally consistent.

**Proposition 8: local binary gadget.** There is an unbounded sequence \(C\) and four indexed terms \(u_1,u_2,u_3,u_4\), all of the same value \(u\), such that:

- \(C\cup\{u_i\}\) is weakly incomplete for every \(i\);
- \(C\cup\{u_i,u_j\}\) is strongly complete for every \(i\ne j\).

**Proof.** Fix \(k\ge1\) and put \(u=2^k\). Let \(C\) consist of one copy of every power of two except \(2u=2^{k+1}\):
\[
C=(1,2,4,\ldots,u,4u,8u,16u,\ldots).
\]
The lower powers \(1,\ldots,u/2\) have subset sums exactly \([0,u-1]\). The tail \(4u,8u,\ldots\) has subset sums exactly the nonnegative multiples of \(4u\).

The core \(C\) already contains one copy of \(u\). After adding one further indexed copy, there are two copies of \(u\), so the available multiples of \(u\) below \(4u\) are
\[
0,u,2u.
\]
Consequently all integers congruent to an element of
\[
[3u,4u-1]\pmod{4u}
\]
are missing. Hence \(C\cup\{u_i\}\) is weakly incomplete.

After adding two further indexed copies, there are three copies of \(u\), whose subset sums are
\[
0,u,2u,3u.
\]
Together with the lower powers and the \(4u\)-scaled binary tail, every nonnegative integer
\[
x=4ut+qu+r,\qquad
t\ge0,\quad 0\le q\le3,\quad 0\le r<u,
\]
is represented. Thus \(C\cup\{u_i,u_j\}\) is strongly complete. ∎

Therefore Lemma 7 alone, even together with the fact that all supports are genuine restricted subset-sum sets, cannot produce a contradiction. The global requirement that this property hold for every four-set \(K\) must be used.

---

### 6. Growth restrictions forced by pair robustness

For a nondecreasing sequence \(B=(b_i)\), put \(S_k(B)=\sum_{i\le k}b_i\).

**Lemma 9.** If \(B\) is weakly complete and unbounded, then
\[
b_{k+1}\le 1+S_k(B)
\]
for all sufficiently large \(k\).

**Proof.** If
\[
b_{k+1}>1+S_k(B),
\]
then \(S_k(B)+1\) cannot be represented: it is larger than the sum of all first \(k\) terms, while every later term is at least \(b_{k+1}>S_k(B)+1\).

If this happened for infinitely many \(k\), the missing integers \(S_k(B)+1\) would be unbounded, contradicting weak completeness. ∎

For the original sequence, define
\[
S_{k-1}=\sum_{i<k}a_i,\qquad
\delta_k=1+S_{k-1}-a_k.
\]

**Corollary 10.** A hypothetical example must satisfy
\[
\delta_k\longrightarrow\infty.
\]

More precisely, for every fixed pair \(P=\{p,q\}\),
\[
\delta_k\ge a_p+a_q
\]
for all sufficiently large \(k\).

**Proof.** Apply Lemma 9 to \(A\setminus P\). For sufficiently large \(k>\max P\),
\[
a_k
\le
1+\sum_{\substack{i<k\\i\notin P}}a_i
=
1+S_{k-1}-a_p-a_q.
\]
Hence \(\delta_k\ge a_p+a_q\).

Given \(M\), choose distinct \(p,q\) with \(a_p+a_q\ge M\), possible because \(A\) is unbounded. The preceding inequality then holds for all sufficiently large \(k\), proving \(\delta_k\to\infty\). ∎

This condition is only necessary. Eventual Brown inequalities do not imply weak completeness; persistent numeration-system gaps can remain despite large eventual slack.

---

### 7. Restrictions on gcd-based obstructions

Fix a triple \(J=\{p,q,r\}\), let \(B=A\setminus J\), and put
\[
g_J=\gcd\{a_i:i\notin J\}.
\]

**Lemma 11.** For every triple \(J\),
\[
g_J\in\{1,2\}.
\]
If \(g_J=2\), then:

1. \(a_p,a_q,a_r\) are all odd;
2. every term outside \(J\) is even;
3. \(B\) represents every sufficiently large even integer;
4. the scaled sequence \(B/2\) is weakly complete.

**Proof.** Fix \(j\in J\). The sequence \(B\cup\{a_j\}\) is complete. Modulo \(g_J\), every subset sum of \(B\) is congruent to \(0\), while every subset sum using \(a_j\) is congruent to \(a_j\). Hence
\[
\Sigma(B\cup\{a_j\})\pmod{g_J}
\subseteq\{0,a_j\}.
\]
A complete sequence represents all sufficiently large integers and therefore all residue classes modulo \(g_J\). Thus \(g_J\) has at most two residue classes, so \(g_J\le2\).

If \(g_J=2\), the two residue classes must be distinct, so \(a_j\) is odd. This holds for all \(j\in J\). Every term of \(B\) is even by definition of \(g_J\).

For every sufficiently large even integer \(x\), completeness of \(B\cup\{a_j\}\) represents \(x\). It cannot use \(a_j\), since \(a_j\) is odd and all terms of \(B\) are even. Thus \(x\in\Sigma(B)\). Dividing all such representations by two proves that \(B/2\) is weakly complete. ∎

**Corollary 12.** There is at most one triple \(J\) for which \(g_J=2\).

**Proof.** If \(g_J=2\), Lemma 11 says that the indexed occurrences in \(J\) are precisely all odd-valued terms of \(A\): every member of \(J\) is odd and every term outside \(J\) is even. Thus \(J\) is uniquely determined. ∎

Consequently, for all but at most one triple \(J\),
\[
\gcd(A\setminus J)=1.
\]
This rules out a common-divisor explanation for universal triple fragility. It does not rule out more subtle periodic obstructions with gcd one, such as missing binary digit classes.

There is also a simpler finite-witness observation.

**Lemma 13.** There are infinitely many triples \(J\) with
\[
\gcd(A\setminus J)=1.
\]

**Proof.** Fix any pair \(P\). Since \(A\setminus P\) is complete, the gcd of its terms is one. Therefore some finite subset \(K\subseteq\mathbb N\setminus P\) already has
\[
\gcd\{a_i:i\in K\}=1.
\]
Every triple \(J\) disjoint from \(K\) leaves all terms indexed by \(K\), so
\[
\gcd(A\setminus J)=1.
\]
There are infinitely many such triples. ∎

---

### 8. Why abstract hypergraph compactness cannot finish the proof

The natural Route 2 compactness statement is false for arbitrary hypergraphs, even finite ones.

**Proposition 14.** There is a sequence \((\mathcal H_x)_{x\ge1}\) of finite hypergraphs on vertex set \(\mathbb N\) such that:

- no pair is ever a transversal of any \(\mathcal H_x\);
- every triple is a transversal of infinitely many \(\mathcal H_x\).

**Proof.** Choose a sequence \(J_1,J_2,\ldots\) in which every three-element subset of \(\mathbb N\) occurs infinitely often. If
\[
J_x=\{p_x,q_x,r_x\},
\]
define
\[
\mathcal H_x=\big\{\{p_x\},\{q_x\},\{r_x\}\big\}.
\]

A pair cannot intersect all three singleton edges, so no pair is a transversal. A triple \(J\) is a transversal precisely when \(J=J_x\). Since every triple occurs infinitely often in the schedule, every triple is a transversal infinitely often. ∎

Thus the quantifier pattern alone contains no contradiction. Any successful hypergraph theorem must exploit that the edges of \(\mathcal R_x\) are precisely fibers of one fixed positive weight map
\[
F\longmapsto\sum_{i\in F}a_i,
\]
and that these fibers for different \(x\) arise from the same sequence.

The local binary gadget in Proposition 8 further shows that even some substantial arithmetic structure at one fixed four-set is insufficient.

---

### 9. Ledger

#### Proved

1. A hypothetical \((2,3)\) example is unbounded and has finite representation hypergraphs at every target.
2. Every pair is a transversal for only finitely many targets; every triple is an inclusion-minimal transversal for infinitely many targets.
3. For a triple-deleted support \(S\), every sufficiently large hole \(h\) has all six neighbours
   \[
   h\pm a_p,\quad h\pm a_q,\quad h\pm a_r
   \]
   in \(S\).
4. Every pair deletion is a minimal weakly complete sequence.
5. Every one-deletion subsequence is itself universally \((1,2)\).
6. Every four-term core is incomplete after one repair and complete after any two repairs.
7. The Brown slack \(1+\sum_{i<k}a_i-a_k\) tends to infinity.
8. For every triple \(J\), \(\gcd(A\setminus J)\in\{1,2\}\), and gcd \(2\) can occur for at most one triple.
9. Pure abstract hypergraph compactness is insufficient.
10. The fixed-four-set repair property is arithmetically realizable and hence cannot alone yield a contradiction.

#### Plausible but unproved

1. No universal weak \((2,3)\) example exists.
2. The overlapping four-core conditions may be globally incompatible, even though each one is locally realizable.
3. A classification of minimal complete restricted bases and their one-term extensions may force this incompatibility.
4. The signed equal-sum exchanges supplied by Lemma 3 may obey a global rigidity theorem, but no such theorem has been established here.

#### Dead ends

1. **Abstract compactness/sunflower argument:** refuted by Proposition 14.
2. **“Three one-term repairs force the core complete”:** false. For example, delete one binary digit \(u\) from the powers of two and add three indexed copies of \(u\); any one copy repairs the core.
3. **“Four repair terms with every pair sufficient force one term sufficient”:** refuted in the restricted subset-sum setting by Proposition 8.
4. **Common-gcd obstruction:** can explain at most one triple.
5. **Eventual Brown inequalities:** only control local growth and do not rule out persistent numeration-system gaps.

## Self-Audit

1. **The \(h+a_j\in S\) conclusion in Lemma 4 is the most delicate local step.**  
   It uses the exact identity \(\Sigma(B\cup\{a_j\})=S\cup(a_j+S)\). If \(h+a_j\notin S\), eventual completeness forces it into \(a_j+S\), whose predecessor is exactly \(h\), contradicting \(h\notin S\). Thus no closure assumption on \(S\) is being smuggled in.

2. **The gcd restriction addresses only the gcd of all remaining terms, not every modular obstruction.**  
   The proof that \(g_J\le2\) is sound because one repair term creates at most two residue classes modulo \(g_J\). However, gcd one does not imply absence of periodic gaps. I have not used the stronger and false conclusion that all other triple gaps are nonmodular.

3. **The growth conclusion \(\delta_k\to\infty\) is necessary but has very limited force.**  
   The indexing after deletion must be handled carefully, but for fixed \(P=\{p,q\}\) and sufficiently large original \(k\), the preceding sum in \(A\setminus P\) is exactly \(S_{k-1}-a_p-a_q\). The argument proves only a necessary inequality and is not presented as a completeness criterion.

## Computations To Verify

The following code exactly computes finite-prefix subset sums and representation transversals. For targets \(x\), the prefix must contain every term \(a_i\le x\).

```python
from itertools import combinations
from math import gcd
from functools import reduce

def subset_sum_mask(values, deleted=()):
    """Bit x is set iff x is a subset sum of undeleted indexed terms."""
    deleted = set(deleted)
    mask = 1
    for i, a in enumerate(values):
        if i not in deleted:
            mask |= mask << a
    return mask

def reachable(mask, x):
    return ((mask >> x) & 1) == 1

def missing_up_to(values, deleted, X):
    mask = subset_sum_mask(values, deleted)
    return [x for x in range(X + 1) if not reachable(mask, x)]

def representation_masks(values, x):
    """
    All indexed representations of x as bitmasks.
    Use only for small examples.
    """
    dp = {0: [0]}
    for i, a in enumerate(values):
        old = list(dp.items())
        for s, masks in old:
            if s + a <= x:
                dp.setdefault(s + a, []).extend(
                    m | (1 << i) for m in masks
                )
    return dp.get(x, [])

def is_transversal(D, reps):
    Dmask = sum(1 << i for i in D)
    return all((Dmask & R) != 0 for R in reps)

def transversal_number(values, x):
    reps = representation_masks(values, x)
    n = len(values)
    for r in range(n + 1):
        for D in combinations(range(n), r):
            if is_transversal(D, reps):
                return r, D
    raise RuntimeError("unreachable")
```

Verification of the local binary gadget in Proposition 8:

```python
def local_binary_gadget(k, max_power):
    """
    Core contains powers 2^r except 2^(k+1).
    It already contains one copy u=2^k.
    """
    u = 2 ** k
    core = [2 ** r for r in range(max_power + 1) if r != k + 1]

    # One restored indexed u: total of two copies of u.
    one_repair = sorted(core + [u])
    mask1 = subset_sum_mask(one_repair)
    total1 = sum(one_repair)

    # Exactly the fourth u-block modulo 4u should be missing.
    for x in range(total1 + 1):
        q = (x % (4 * u)) // u
        assert reachable(mask1, x) == (q != 3)

    # Two restored indexed u's: total of three copies of u.
    two_repairs = sorted(core + [u, u])
    mask2 = subset_sum_mask(two_repairs)
    total2 = sum(two_repairs)
    assert all(reachable(mask2, x) for x in range(total2 + 1))

for k in range(1, 6):
    local_binary_gadget(k, max_power=k + 8)

print("Local binary gadget verified.")
```

Finite search for recurring minimal triple transversals in a candidate recurrence:

```python
def minimal_triple_transversals(values, X):
    """
    Returns triples J that are inclusion-minimal transversals
    for at least one target x <= X.
    Intended only for small values/prefixes.
    """
    out = {}
    n = len(values)
    for x in range(X + 1):
        reps = representation_masks(values, x)
        if not reps:
            continue
        for J in combinations(range(n), 3):
            if not is_transversal(J, reps):
                continue
            if all(not is_transversal(P, reps)
                   for P in combinations(J, 2)):
                out.setdefault(J, []).append(x)
    return out

def kbonacci(initial, order, X):
    """
    Generates terms until the next term exceeds X.
    'initial' must have length at least order.
    """
    a = list(initial)
    while a[-1] <= X:
        a.append(sum(a[-order:]))
    return [v for v in a if v <= X]

# Example exploratory run:
vals = kbonacci([1, 1, 1], 3, 200)
data = minimal_triple_transversals(vals, 200)
for J, targets in sorted(data.items(), key=lambda kv: -len(kv[1]))[:20]:
    print(J, [vals[i] for i in J], targets[:20])
```

Finite deletion-gap scan:

```python
def deletion_gap_report(values, deletion_size, X, deletion_window=None):
    """
    Exact up to X provided values contains every sequence term <= X.
    deletion_window limits which indexed terms are tested.
    """
    if deletion_window is None:
        deletion_window = len(values)
    report = {}
    for D in combinations(range(deletion_window), deletion_size):
        gaps = missing_up_to(values, D, X)
        report[D] = {
            "number_of_gaps": len(gaps),
            "largest_gap": max(gaps) if gaps else None,
            "last_20_gaps": gaps[-20:]
        }
    return report
```

A more targeted computation should, for each candidate recurrence:

1. Generate every term at most \(X\).
2. Enumerate all pairs and triples among the first \(L\) indices.
3. For each \(x\le X\), compute the minimal transversals of \(\mathcal R_x\).
4. Record signed exchanges obtained from minimal triple transversals.
5. Test whether exchanges for overlapping triples reuse a finite collection of local carry states.

## Route Diagnosis

Route 2 successfully isolates the exact combinatorial object: a hypothetical example requires every pair to be an eventual non-transversal while every triple is recurrently an inclusion-minimal transversal. It also yields useful arithmetic consequences—three-way equal-sum exchanges, six represented neighbours around every large triple-deletion hole, minimality of every pair-deleted basis, and severe restrictions on gcd obstructions.

The route is blocked because the natural abstract compactness theorem is false, as Proposition 14 shows. Moreover, arithmetic information attached to one fixed triple or quadruple is insufficient: binary missing-digit gadgets realize the same local repair patterns. What is not understood is the **global compatibility across all overlapping triples and quadruples** for one fixed sequence of weights.

A fresh attempt should therefore avoid another pointwise transversal argument. The most promising next targets are:

1. classify, or substantially constrain, minimal weakly complete restricted bases;
2. compare the minimal bases \(A\setminus P\) for overlapping pairs \(P\);
3. encode the signed exchanges from Lemma 3 as carry states and prove that the local binary gadgets cannot coexist at infinitely many scales;
4. computationally search for finite-state recurrence candidates, tracking minimal transversals rather than merely missing sums.

Without such a global arithmetic-coherence theorem, Route 2 reduces to essentially the original open difficulty and is presently blocked.