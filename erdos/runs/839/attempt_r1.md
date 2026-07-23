STATUS: BLOCKED

## Result

Route 1 yields several rigorous obstructions but not a proof of P1 or P2. I prove that every admissible sequence satisfies
\[
\limsup_{n\to\infty}\frac{a_n}{n}\ge \frac32
\quad\text{and}\quad
\limsup_{x\to\infty}\frac{H_A(x)}{\log x}\le\frac23.
\]
I also determine the exact eight-term finite threshold
\[
\min_{a_1<\cdots<a_8\ \mathrm{admissible}}
\max_{1\le i\le8}\frac{a_i}{i}=2,
\]
and derive a strong rigidity statement at the extremal asymptotic slope \(3/2\): the adjacent-pair sums must asymptotically exhaust the complement of \(A\), and almost every fixed-length block sum must also be an adjacent-pair sum. Exact exhaustion is impossible and uniquely forces \(A\) to be the positive integers not divisible by \(3\), which violates admissibility. The unresolved block is a quantitative stability theorem converting asymptotic exhaustion into exact or positive-density structural information. For larger linear bounds there is substantial unused complement, and elementary interval-sum counting collapses under high multiplicity.

## Complete Argument

### 1. The adjacent-pair obstruction

Define
\[
p_n=a_n+a_{n+1},\qquad P=\{p_n:n\ge1\}.
\]

#### Lemma 1.1: \(A\cap P=\varnothing\), and the \(p_n\) are strictly increasing

Indeed,
\[
p_{n+1}-p_n=a_{n+2}-a_n>0.
\]
If \(p_n=a_i\), then \(p_n>a_{n+1}\), so \(i>n+1\). But then
\[
a_i=a_n+a_{n+1}
\]
is a prohibited earlier consecutive sum. Thus \(A\cap P=\varnothing\).

#### Lemma 1.2: Every admissible sequence satisfies
\[
\limsup_{n\to\infty}\frac{a_n}{n}\ge\frac32.
\]

**Proof.** Let
\[
L=\limsup_{n\to\infty}\frac{a_n}{n}.
\]
There is nothing to prove if \(L=\infty\). Suppose \(L<\infty\).

For every \(\varepsilon>0\), all sufficiently large \(n\) satisfy
\[
a_n\le (L+\varepsilon)n.
\]
Consequently,
\[
p_n=a_n+a_{n+1}\le (2L+3\varepsilon)n
\]
for all sufficiently large \(n\), after harmlessly enlarging the error.

It follows that
\[
\liminf_{x\to\infty}\frac{|A\cap[1,x]|}{x}\ge\frac1L,
\qquad
\liminf_{x\to\infty}\frac{|P\cap[1,x]|}{x}\ge\frac1{2L}.
\]
More formally, first obtain \(1/(L+\varepsilon)\) and \(1/(2L+3\varepsilon)\), then let \(\varepsilon\downarrow0\).

Since \(A\) and \(P\) are disjoint subsets of the positive integers,
\[
|A\cap[1,x]|+|P\cap[1,x]|\le x.
\]
Hence
\[
\frac1L+\frac1{2L}\le1,
\]
which gives \(L\ge3/2\). ∎

This is the strongest asymptotic conclusion obtained here from a single fixed block length.

---

### 2. A reciprocal-sum consequence

The same adjacent-pair family gives a nontrivial, though far from sufficient, bound toward P2.

#### Lemma 2.1
Every admissible sequence satisfies
\[
\limsup_{x\to\infty}\frac{H_A(x)}{\log x}\le\frac23.
\]

**Proof.** Let
\[
H_P(x)=\sum_{\substack{n\ge1\\p_n<x}}\frac1{p_n}.
\]
If \(a_{n+1}<x/2\), then
\[
p_n=a_n+a_{n+1}<2a_{n+1}<x
\]
and
\[
\frac1{p_n}>\frac1{2a_{n+1}}.
\]
Therefore
\[
H_P(x)\ge \frac12H_A(x/2)-O_A(1).
\]
Since \(A\cap P=\varnothing\),
\[
H_A(x)+H_P(x)
\le \sum_{1\le m<x}\frac1m
=\log x+O(1).
\]
It follows that
\[
H_A(x)+\frac12H_A(x/2)\le\log x+O_A(1).
\]
Moreover,
\[
0\le H_A(x)-H_A(x/2)
\le\sum_{x/2\le m<x}\frac1m
=O(1).
\]
Thus
\[
\frac32H_A(x)\le\log x+O_A(1),
\]
and division by \(\log x\) proves the claim. ∎

This does not approach the required \(o(\log x)\); it only records what the pair obstruction alone can supply.

---

### 3. A finite pair-sum counting inequality

Let \(a_1<\cdots<a_N\) be admissible and suppose
\[
a_i\le Ci\qquad(1\le i\le N).
\]

#### Lemma 3.1
For every \(N\),
\[
N+\left\lfloor\frac{N-1}{2}\right\rfloor\le \lfloor CN\rfloor.
\tag{4}
\]

**Proof.** Put
\[
m=\left\lfloor\frac{N-1}{2}\right\rfloor.
\]
For \(1\le j\le m\),
\[
p_j=a_j+a_{j+1}\le C(2j+1)\le CN.
\]
The \(N\) values \(a_1,\dots,a_N\) and the \(m\) values \(p_1,\dots,p_m\) are all distinct, by Lemma 1.1, and are positive integers not exceeding \(\lfloor CN\rfloor\). This proves (4). ∎

As \(N\to\infty\), this reproduces the threshold \(C\ge3/2\).

#### Rigidity at \(C=3/2\)

There is no admissible five-term prefix satisfying \(a_i\le3i/2\).

For \(N=3\), the four distinct values
\[
a_1,a_2,a_3,p_1
\]
all lie in \([1,4]\), so they are exactly \(1,2,3,4\). Since \(a_1=1\), the only possibility is
\[
(a_1,a_2,a_3)=(1,2,4),\qquad p_1=3.
\]

For \(N=5\), the seven distinct values
\[
a_1,\dots,a_5,p_1,p_2
\]
all lie in \([1,7]\), so they partition that interval. Since
\[
p_2=a_2+a_3=6,
\]
the two remaining terms must be
\[
a_4=5,\qquad a_5=7.
\]
But then
\[
a_5=7=a_1+a_2+a_3,
\]
contradicting admissibility.

---

### 4. Exact eight-term finite threshold

Define
\[
c_N=\min_{a_1<\cdots<a_N\ \mathrm{admissible}}
\max_{1\le i\le N}\frac{a_i}{i}.
\]

#### Proposition 4.1
\[
c_8=2.
\]

**Proof: lower bound.** Suppose instead that
\[
a_i<2i\qquad(1\le i\le8).
\]
Since the terms are integers,
\[
a_i\le2i-1.
\tag{5}
\]

From \(a_1\le1\), we get \(a_1=1\), while \(a_2\le3\), so \(a_2=2\) or \(3\).

**Case 1: \(a_2=2\).**

The value \(3=1+2\) is forbidden, so \(a_3=4\) or \(5\).

- If \(a_3=4\), then:
  \[
  a_4=5,
  \]
  because \(6=2+4\) and \(7=1+2+4\);
  \[
  a_5=8,
  \]
  because \(6=2+4\), \(7=1+2+4\), and \(9=4+5\);
  \[
  a_6=10,
  \]
  because \(9=4+5\) and \(11=2+4+5\).
  But every possible \(a_7\le13\) is forbidden:
  \[
  11=2+4+5,\qquad
  12=1+2+4+5,\qquad
  13=5+8.
  \]

- If \(a_3=5\), then:
  \[
  a_4=6,
  \]
  because \(7=2+5\);
  \[
  a_5=9,
  \]
  because \(7=2+5\) and \(8=1+2+5\);
  \[
  a_6=10,
  \]
  because \(11=5+6\);
  \[
  a_7=12,
  \]
  because \(11=5+6\) and \(13=2+5+6\).
  But every possible \(a_8\le15\) is forbidden:
  \[
  13=2+5+6,\qquad
  14=1+2+5+6,\qquad
  15=6+9.
  \]

**Case 2: \(a_2=3\).**

Since \(4=1+3\), necessarily \(a_3=5\).

- If \(a_4=6\), then:
  \[
  a_5=7,
  \]
  because \(8=3+5\) and \(9=1+3+5\);
  \[
  a_6=10,
  \]
  because \(8=3+5\), \(9=1+3+5\), and \(11=5+6\);
  \[
  a_7=12,
  \]
  because \(11=5+6\) and \(13=6+7\).
  But
  \[
  13=6+7,\qquad
  14=3+5+6,\qquad
  15=1+3+5+6,
  \]
  so no \(a_8\le15\) is possible.

- If \(a_4=7\), then both possible fifth terms are forbidden:
  \[
  8=3+5,\qquad 9=1+3+5.
  \]

These cases exhaust all possibilities under (5), proving \(c_8\ge2\).

For the reverse inequality, consider
\[
(1,3,5,6,7,10,12,16).
\]
The non-singleton block sums available before appending each new term show successively that \(3,5,6,7,10,12,16\) are legal. In particular, for the final append, the earlier prefix sums are
\[
0,1,4,9,15,22,32,44,
\]
and \(16\) is not a positive difference of two of them. Thus the sequence is admissible, and
\[
\max_{1\le i\le8}\frac{a_i}{i}=2.
\]
Therefore \(c_8=2\). ∎

This is a genuine fixed-origin obstruction, but it does not imply
\(\limsup a_n/n\ge2\): the finite argument cannot be shifted to a tail because translation does not preserve the condition or the cap relative to the new local index.

---

### 5. Rigidity if the asymptotic slope equals \(3/2\)

The pair argument has a strong equality case.

#### Proposition 5.1
Suppose an admissible sequence satisfies
\[
\limsup_{n\to\infty}\frac{a_n}{n}\le\frac32.
\]
Then:

1. \(A\) has natural density \(2/3\);
2. \(P=\{a_n+a_{n+1}\}\) has natural density \(1/3\);
3. \(A\cup P\) has density \(1\);
4. \(a_n/n\to3/2\);
5. for each fixed \(k\ge2\), if
   \[
   B_k=\{a_n+\cdots+a_{n+k-1}:n\ge1\},
   \]
   then all but \(o(N)\) of the first \(N\) elements of \(B_k\) belong to \(P\).

**Proof.** Lemma 1.2 first forces
\[
\limsup a_n/n=3/2.
\]
The assumed upper bound gives
\[
\underline d(A)\ge\frac23.
\]
Also
\[
p_n/n\le3+o(1),
\]
so
\[
\underline d(P)\ge\frac13.
\]
Since \(A\cap P=\varnothing\),
\[
\overline d(A)\le1-\underline d(P)\le\frac23,
\]
and similarly
\[
\overline d(P)\le1-\underline d(A)\le\frac13.
\]
Thus the two natural densities exist and equal \(2/3\) and \(1/3\). Their union has density one.

A positive natural density \(2/3\) implies, by inversion of the counting function,
\[
\frac{a_n}{n}\longrightarrow\frac32.
\]

Fix \(k\ge2\), and write
\[
b_n^{(k)}=a_n+\cdots+a_{n+k-1}.
\]
The sequence \(b_n^{(k)}\) is strictly increasing because
\[
b_{n+1}^{(k)}-b_n^{(k)}=a_{n+k}-a_n>0.
\]
Moreover \(B_k\cap A=\varnothing\): a \(k\)-term block sum is larger than its final summand, so equality with an element of \(A\) would be a later forbidden equality.

Since \(a_{n+j}/n\to3/2\) for each fixed \(j\),
\[
\frac{b_n^{(k)}}n\longrightarrow\frac{3k}{2}.
\]
Hence \(B_k\) has natural density \(2/(3k)\).

Let
\[
D=\mathbb Z_{>0}\setminus(A\cup P).
\]
We have \(d(D)=0\). Since \(B_k\subseteq\mathbb Z_{>0}\setminus A\),
\[
B_k\setminus P\subseteq D.
\]
Also \(b_N^{(k)}=O_k(N)\), so
\[
\#\{n\le N:b_n^{(k)}\notin P\}
\le |D\cap[1,b_N^{(k)}]|=o(N).
\]
This proves the final assertion. ∎

Thus an extremal hypothetical sequence would have to satisfy, for every fixed \(k\), that almost every \(k\)-term block sum is also an adjacent-pair sum. This is an extremely rigid but presently insufficient conclusion.

---

### 6. Exact exhaustion is impossible

The exact analogue of the preceding equality structure can be completely classified.

#### Proposition 6.1
Suppose an increasing sequence \(A=\{a_n\}\) satisfies
\[
\mathbb Z_{>0}=A\mathbin{\dot\cup}\{a_n+a_{n+1}:n\ge1\}.
\tag{6}
\]
Then
\[
A=\{m\ge1:3\nmid m\},
\qquad
a_n=\left\lfloor\frac{3n-1}{2}\right\rfloor,
\qquad
a_n+a_{n+1}=3n.
\]
Consequently, no admissible sequence can satisfy (6).

**Proof.** We determine membership by strong induction on \(x\).

Assume membership has been determined below \(x\) and agrees with the set of positive integers not divisible by \(3\). If
\[
x=a_n+a_{n+1},
\]
then both summands are strictly less than \(x\), so by induction they are the \(n\)-th and \((n+1)\)-st positive integers not divisible by \(3\). Those terms satisfy
\[
a_n+a_{n+1}=3n.
\]
Thus \(x\) is an adjacent-pair sum exactly when \(3\mid x\). By the partition property (6), \(x\in A\) exactly when \(3\nmid x\). This closes the induction.

For this sequence,
\[
a_1+a_2+a_3=1+2+4=7=a_5,
\]
so it is not admissible. ∎

The missing step is that density-one exhaustion does not imply exact exhaustion. Sparse defects can change the enumeration and may propagate across scales.

---

### 7. Why the raw interval count does not close Route 1

Suppose again that \(a_i\le Ci\) for \(i\le N\). For a block of length \(\ell\) beginning at \(r\),
\[
a_r+\cdots+a_{r+\ell-1}
\le C\left(\ell r+\frac{\ell(\ell-1)}2\right).
\]
Thus every pair \((r,\ell)\) satisfying
\[
\ell r+\frac{\ell(\ell-1)}2\le N
\tag{7}
\]
produces a forbidden block sum at most \(CN\).

Let
\[
L=\max\left\{\ell:\frac{\ell(\ell+1)}2\le N\right\}.
\]
The number of blocks certified by (7), with \(\ell\ge2\), is
\[
M_N
=\sum_{\ell=2}^{L}
\left\lfloor\frac N\ell-\frac{\ell-1}{2}\right\rfloor
=\frac12N\log N+O(N).
\tag{8}
\]

However, these are not necessarily distinct values. A fixed integer \(x\) has at most one representation by a block of each fixed length, since the sums of \(\ell\) consecutive terms strictly increase with the starting index. Also any length-\(\ell\) block has sum at least
\[
1+2+\cdots+\ell=\frac{\ell(\ell+1)}2.
\]
Hence a value \(x\le CN\) has at most
\[
\sqrt{2CN}
\]
representations as a consecutive block sum. From (8) one obtains only
\[
\#\{\text{certified distinct block sums}\}
=\Omega_C(\sqrt N\log N),
\]
which is much smaller than the \(\Theta(N)\) complement available below \(CN\).

Thus the naive “\(N\log N\) blocks versus \(CN\) integers” count loses too much through multiplicity. The single pair-sum family avoids this multiplicity but yields only the \(3/2\) threshold.

A small additional structural fact does not repair the loss:

#### Lemma 7.1
Suppose two distinct intervals \([r,s]\) and \([u,v]\), with \(r<u\), have equal sums. Then \(s<v\), and the later interval is shorter. If the intervals overlap, then in an admissible sequence
\[
u-r\ge3,\qquad v-s\ge2.
\]

**Proof.** If \(v\le s\), the later interval is a proper subinterval of the first and has smaller positive sum, impossible. If its length were at least that of the first, termwise comparison would make its sum strictly larger.

In the overlapping case, cancellation gives
\[
\sum_{j=r}^{u-1}a_j=\sum_{j=s+1}^{v}a_j.
\]
If \(u-r=1\), the left side is \(a_r\), while every term on the right is larger than \(a_r\), impossible. If \(v-s=1\), then
\[
a_v=\sum_{j=r}^{u-1}a_j,
\]
and the left block has at least two terms, contradicting admissibility. Since the later interval is shorter,
\[
u-r>v-s,
\]
which gives \(u-r\ge3\). ∎

Even these endpoint separations permit \(\Theta(\sqrt N)\) representations of a value.

---

### 8. Counterexamples to overly optimistic collision lemmas

It is false that pair sums and triple sums are generally almost disjoint, even for admissible finite prefixes.

For any \(M\), the sequence
\[
M,M+1,\dots,2M-1
\]
is admissible: its smallest two-term block sum is \(2M+1\), larger than every term. Its pair and triple sums are
\[
p_j=2M+2j-1,\qquad q_k=3M+3k-3.
\]
They are equal whenever
\[
j=\frac{M+3k-2}{2},
\]
which occurs for \(\Theta(M)\) choices of \(k\).

Even consecutive triple sums can be pair sums. The admissible prefix
\[
(10,11,13,16,18,22,25,31)
\]
satisfies
\[
q_1=p_4=34,\quad
q_2=p_5=40,\quad
q_3=p_6=47,\quad
q_4=p_7=56.
\]
It is admissible because its only non-singleton block sums at most \(31\) are \(21,24,29\), none of which is a term.

These examples do not satisfy a fixed linear cap independent of their length, but they show that any successful Route 1 argument must use the global cap essentially, not merely monotonicity and admissibility.

---

### Ledger

**Proved lemmas and propositions**

1. \(A\) is disjoint from its adjacent-pair-sum set \(P\).
2. Every admissible sequence has \(\limsup a_n/n\ge3/2\).
3. Every admissible sequence has \(\limsup H_A(x)/\log x\le2/3\).
4. The finite pair-sum counting inequality (4).
5. No five-term prefix obeys \(a_i\le3i/2\).
6. The exact finite extremum \(c_8=2\).
7. At asymptotic slope \(3/2\), \(A\) and \(P\) have densities \(2/3\) and \(1/3\), and every fixed-length block-sum family is asymptotically contained in \(P\).
8. Exact partition \(A\dot\cup P=\mathbb Z_{>0}\) uniquely forces the nonmultiples of \(3\), which are not admissible.
9. The low-sum interval count (8) and the \(\sqrt{N}\)-scale multiplicity bound.
10. The equal-interval endpoint-separation lemma.

**Plausible but unproved claims**

1. A stability version of Proposition 6.1: if \(A\cup P\) misses only \(o(x)\) integers up to \(x\), then the triple-sum family cannot be contained in \(P\) up to \(o(x)\) exceptions.
2. More generally, under a fixed cap \(a_i\le Ci\), the union of several block-length families should occupy more than the available complement unless the sequence has a rigid multiscale structure.
3. Such rigid structure may force either a forbidden term or rapid growth, but no quantitative theorem of this kind was obtained.

**Dead ends**

1. Counting all \(O(N\log N)\) guaranteed small block sums loses too much to multiplicity.
2. Pair/triple disjointness is false; even consecutive triple sums may be pair sums.
3. The exact \(A\dot\cup P\) classification does not automatically extend to density-zero defects.
4. The finite result \(c_8=2\) cannot be shifted to a tail because translation is not an invariance and the cap is relative to the original indices.

## Self-Audit

1. **The eight-term case split is vulnerable to an omitted branch.**  
   The proof uses the exact integral bounds \(a_i\le2i-1\), and every possible value at each branch is explicitly either retained or represented by an earlier block. The code below independently performs the full backtracking check.

2. **The endpoint density argument uses several inverse-density passages.**  
   These are valid because all relevant sequences are strictly increasing and have positive limiting density. The proof first establishes matching lower and upper densities and only then inverts the counting function to obtain \(a_n/n\to3/2\).

3. **The exact partition theorem is much stronger than what the asymptotic endpoint supplies.**  
   I do not claim that density-one exhaustion implies exact exhaustion. The exact theorem itself is secure by strong induction, but extending it to sparse defects is precisely the unresolved and most consequential gap.

## Computations To Verify

```python
from fractions import Fraction

def is_admissible(seq):
    forbidden = set()
    prefix = []
    for v in seq:
        if prefix and v <= prefix[-1]:
            return False
        if v in forbidden:
            return False

        prefix.append(v)

        # Add all new blocks ending at v.
        total = 0
        for y in reversed(prefix):
            total += y
            forbidden.add(total)
    return True

def extend_states(caps):
    """
    Enumerate all admissible sequences with a_i <= caps[i-1].
    Each state carries the complete set of old consecutive block sums.
    """
    states = [(tuple(), frozenset())]

    for cap in caps:
        new_states = []
        for seq, forbidden in states:
            lo = seq[-1] + 1 if seq else 1
            for v in range(lo, cap + 1):
                if v in forbidden:
                    continue

                new_seq = seq + (v,)
                new_forbidden = set(forbidden)

                total = 0
                for y in reversed(new_seq):
                    total += y
                    new_forbidden.add(total)

                new_states.append((new_seq, frozenset(new_forbidden)))
        states = new_states

    return states

# Verify the exact lower bound c_8 >= 2:
# max_i a_i/i < 2 is equivalent to a_i <= 2i-1.
strict_two_caps = [2*i - 1 for i in range(1, 9)]
assert extend_states(strict_two_caps) == []

# Verify the witness for c_8 <= 2.
witness = (1, 3, 5, 6, 7, 10, 12, 16)
assert is_admissible(witness)
assert max(Fraction(a, i) for i, a in enumerate(witness, 1)) == 2

# Optional independent optimization under a_i <= 2i.
states = extend_states([2*i for i in range(1, 9)])
best = min(
    max(Fraction(a, i) for i, a in enumerate(seq, 1))
    for seq, _ in states
)
assert best == 2

def fixed_C_states(p, q, N):
    """Exact rational cap C=p/q."""
    caps = [(p*i)//q for i in range(1, N+1)]
    return extend_states(caps)

# Verify no five-term prefix for C=3/2.
assert fixed_C_states(3, 2, 5) == []

# Search maximum depth for selected rational C.
def maximum_depth(p, q, depth_limit):
    states = [(tuple(), frozenset())]
    for i in range(1, depth_limit + 1):
        cap = (p*i)//q
        new_states = []
        for seq, forbidden in states:
            lo = seq[-1] + 1 if seq else 1
            for v in range(lo, cap + 1):
                if v in forbidden:
                    continue
                new_seq = seq + (v,)
                new_forbidden = set(forbidden)
                total = 0
                for y in reversed(new_seq):
                    total += y
                    new_forbidden.add(total)
                new_states.append((new_seq, frozenset(new_forbidden)))
        if not new_states:
            return i - 1
        states = new_states
        print("depth", i, "survivors", len(states))
    return depth_limit

# Suggested runs:
# maximum_depth(2, 1, 100)
# maximum_depth(5, 2, 100)
# maximum_depth(3, 1, 100)
# maximum_depth(4, 1, 100)

# Verify the finite pair/triple collision example.
collision_example = (10, 11, 13, 16, 18, 22, 25, 31)
assert is_admissible(collision_example)

P = [
    collision_example[i] + collision_example[i+1]
    for i in range(len(collision_example)-1)
]
Q = [
    collision_example[i]
    + collision_example[i+1]
    + collision_example[i+2]
    for i in range(len(collision_example)-2)
]
assert Q[:4] == P[3:7]

# Diagnostics for a long survivor.
def block_sum_sets(seq, max_length=None):
    n = len(seq)
    if max_length is None:
        max_length = n
    result = {}
    for length in range(2, min(max_length, n) + 1):
        vals = []
        total = sum(seq[:length])
        vals.append(total)
        for r in range(1, n - length + 1):
            total += seq[r + length - 1] - seq[r - 1]
            vals.append(total)
        result[length] = set(vals)
    return result

def candidate_coverage(seq, cap):
    sums = set()
    total = 0
    pref = [0]
    for a in seq:
        total += a
        pref.append(total)
    for s in range(1, len(pref)):
        for t in range(s):
            sums.add(pref[s] - pref[t])

    lo = seq[-1] + 1
    candidates = set(range(lo, cap + 1))
    return {
        "candidate_count": len(candidates),
        "covered": len(candidates & sums),
        "uncovered_values": sorted(candidates - sums),
    }
```

For fixed \(C\), the most useful computational certificate would be a complete search tree showing that all states vanish by some depth. For structural discovery, record for each survivor:

- the holes in \(A\cup P\);
- the proportion of triple and longer block sums already represented as pair sums;
- the representation multiplicity of each forbidden value;
- the uncovered candidates in \((a_m,\lfloor C(m+1)\rfloor]\).

## Route Diagnosis

Route 1 works cleanly when a single fixed block length nearly fills the available complement. Adjacent pairs give the universal slope obstruction \(3/2\), exact finite rigidity at \(C=3/2\), and complete asymptotic saturation if equality holds. The route becomes blocked at the following precise statement:

> If \(A\) and its adjacent-pair sums \(P\) are disjoint, \(A\cup P\) has density one, and every triple sum avoids \(A\), prove that a positive proportion of triple sums lie outside \(P\).

That would contradict the density-zero exceptional set and rule out the endpoint \(3/2\). Exact exhaustion proves the corresponding zero-defect statement, but sparse defects may propagate through the enumeration, and no stability theorem was found.

For general \(C>3/2\), even this saturation disappears. One needs a quantitative lower bound for the union of many block-length sumsets, not merely their total number with multiplicity. The natural fresh attempt is therefore a hybrid of Routes 1 and 2: analyze the representation function of small prefix-sum differences under the additional condition that its support avoids the positive-density gap set \(A\). A cardinality-only estimate is insufficient; the required theorem must either force interval coverage or classify the high-multiplicity structures and show that those structures create a forbidden term.