STATUS: BLOCKED

## Result

Route 2 does not currently yield a complete solution. I proved an exact compactness criterion showing that iterative deletion succeeds precisely when all finite-stage survivors share a uniform \((k+1)\)-basis threshold. The essential-element theorem supplies neither this uniformity nor the sharp order bound \(k+1\). A concrete basis of exact order \(2\), satisfying the full infinite-deletion premise, demonstrates all three phenomena: deleting one nonessential element can raise the order from \(2\) to \(4\); deleting nonessential elements indefinitely can leave every finite stage of order \(2\) while the limit has infinite order; yet a carefully chosen infinite deletion does leave exact order \(3\). Thus the unresolved issue is genuinely the global selection of deletions, not their finite-stage existence.

## Complete Argument

### 1. The exact limiting criterion for nested deletion

Let
\[
C_0\supseteq C_1\supseteq C_2\supseteq\cdots\subseteq\mathbb N_0,
\qquad
C_\infty=\bigcap_{j=0}^{\infty}C_j,
\]
and fix \(h\ge1\).

#### Lemma 1
For every \(n\in\mathbb N_0\),
\[
n\in hC_\infty
\quad\Longleftrightarrow\quad
n\in hC_j\ \text{for every }j.
\]
Consequently,
\[
hC_\infty=\bigcap_{j=0}^{\infty}hC_j.
\]

#### Proof
The forward implication follows from \(C_\infty\subseteq C_j\).

Conversely, suppose \(n\in hC_j\) for every \(j\). Since all summands are nonnegative, every \(h\)-term representation of \(n\) uses only elements of \([0,n]\). Hence there are only finitely many ordered \(h\)-tuples
\[
(a_1,\dots,a_h)\in\mathbb N_0^h,\qquad a_1+\cdots+a_h=n.
\]

Let \(R_j\) be the set of such tuples with all \(a_i\in C_j\). Then each \(R_j\) is a nonempty finite set and
\[
R_0\supseteq R_1\supseteq R_2\supseteq\cdots.
\]
A nested sequence of nonempty subsets of a fixed finite set has nonempty intersection. Choose
\[
(a_1,\dots,a_h)\in\bigcap_jR_j.
\]
Each \(a_i\) belongs to every \(C_j\), hence to \(C_\infty\). Therefore \(n\in hC_\infty\). ∎

Let
\[
G_j=\mathbb N_0\setminus hC_j.
\]
Because \(C_{j+1}\subseteq C_j\), the gap sets satisfy
\[
G_0\subseteq G_1\subseteq G_2\subseteq\cdots.
\]
Lemma 1 gives
\[
\mathbb N_0\setminus hC_\infty=\bigcup_{j=0}^{\infty}G_j.
\]

#### Corollary 2: Uniform-threshold criterion
The limit \(C_\infty\) is an asymptotic basis of order at most \(h\) if and only if there is a single \(N\) such that
\[
[N,\infty)\subseteq hC_j
\qquad\text{for every }j.
\]

#### Proof
The limit is an \(h\)-basis exactly when \(\bigcup_jG_j\) is finite. This is equivalent to all \(G_j\) being contained in one finite interval \([0,N)\). ∎

Thus Route 2 cannot be completed merely by arranging that every finite-stage survivor is an \((k+1)\)-basis. Their thresholds must be uniformly bounded.

In particular, if \(b_1,b_2,\dots\) are distinct, \(B_j=\{b_1,\dots,b_j\}\), and
\[
C_j=A\setminus B_j,
\]
then \(B=\{b_1,b_2,\dots\}\) solves the problem exactly when, for some fixed \(N\),
\[
[N,\infty)\subseteq (k+1)C_j
\quad\text{for every }j.
\]
This is the missing invariant in the naive essential-element iteration.

---

### 2. Safe-deletion families and why bare compactness is insufficient

For \(h,N\ge1\), define
\[
\mathcal X_{h,N}
=
\left\{
B\subseteq A:[N,\infty)\subseteq h(A\setminus B)
\right\}.
\]

#### Lemma 3
Each \(\mathcal X_{h,N}\) is a closed hereditary family in the Cantor space \(\{0,1\}^A\).

#### Proof
It is hereditary because deleting fewer elements cannot destroy a surviving representation.

For fixed \(n\), the condition
\[
n\in h(A\setminus B)
\]
depends only on the coordinates of \(B\) belonging to \(A\cap[0,n]\), which is finite. More explicitly, it is a finite union, over all \(h\)-term representations of \(n\), of the cylinder condition that none of the elements in that representation's support belongs to \(B\). It is therefore clopen.

Hence
\[
\mathcal X_{h,N}
=
\bigcap_{n\ge N}
\{B:n\in h(A\setminus B)\}
\]
is closed. ∎

The original premise says that every \(\mathcal X_{k,N}\) contains only finite deletion sets. The desired conclusion asks whether some \(\mathcal X_{k+1,N}\) contains an infinite set.

Compactness alone does not imply that a closed hereditary family with arbitrarily large finite members contains an infinite member. For example, the Schreier family
\[
\mathcal S
=
\{\varnothing\}\cup
\{F\subseteq\mathbb N:F\text{ finite and }|F|\le \min F+1\}
\]
is closed and hereditary, has members of arbitrarily large finite cardinality, but has no infinite member.

Therefore finite-window feasibility, even with arbitrarily many deletions, does not by itself produce the required infinite mask. One needs an additive property of the families \(\mathcal X_{h,N}\) that rules out Schreier-type behavior.

---

### 3. A rigorous reduction for deletions that preserve order \(k\)

Let
\[
\mathcal I_k(A)
=
\{F\subseteq A:F\text{ finite and }k(A\setminus F)\text{ is cofinite}\}.
\]
This family is hereditary.

Starting with \(F_0=\varnothing\), repeatedly add an element \(a\in A\setminus F_j\) whenever
\[
F_j\cup\{a\}\in\mathcal I_k(A).
\]

There are two possibilities.

1. The process continues indefinitely, producing
   \[
   F_0\subsetneq F_1\subsetneq\cdots,
   \]
   with every \(A\setminus F_j\) still an order-\(k\) basis.

2. It stops at a finite \(F\). Then \(C=A\setminus F\) is pointwise minimal as an order-\(k\) basis:
   \[
   k(C\setminus\{c\})\text{ is not cofinite for every }c\in C.
   \]

Indeed, if some finite strict extension \(F'\supsetneq F\) were in \(\mathcal I_k(A)\), then for any \(a\in F'\setminus F\),
\[
A\setminus(F\cup\{a\})\supseteq A\setminus F',
\]
so \(F\cup\{a\}\in\mathcal I_k(A)\), contradicting termination.

Moreover, if \(A\) satisfies the problem premise and \(F\in\mathcal I_k(A)\), then \(C=A\setminus F\) also satisfies it. For every infinite \(D\subseteq C\),
\[
k(C\setminus D)\subseteq k(A\setminus D),
\]
and the right side is not cofinite by the premise.

Thus Route 2 rigorously reduces the problem to two unresolved cases:

- an infinite chain of finite order-\(k\)-preserving deletions, where one must prevent \((k+1)\)-threshold drift; or
- a pointwise minimal order-\(k\) basis, where no further one-point deletion preserves order \(k\).

Neither reduction provides the required common \((k+1)\)-threshold.

---

### 4. A stress-test basis satisfying the full premise

Define
\[
P=\{5m+1:m\ge0\},\qquad
Q=\{5m+4:m\ge0\},
\]
and
\[
A=\{0\}\cup P\cup Q.
\]

This example satisfies the hypothesis for \(k=2\).

#### Proposition 4
The set \(A\) has exact order \(2\).

#### Proof
Every sufficiently large integer has a two-term representation according to its residue modulo \(5\):

\[
\begin{array}{c|c}
n\bmod5&\text{representation type}\\ \hline
0&P+Q\\
1&0+P\\
2&P+P\\
3&Q+Q\\
4&0+Q.
\end{array}
\]

More explicitly:

- \(5t=1+(5(t-1)+4)\) for \(t\ge1\);
- every element of \(P\) is \(0+p\);
- \(5t+2=1+(5t+1)\);
- \(5t+3=4+(5(t-1)+4)\) for \(t\ge1\);
- every element of \(Q\) is \(0+q\).

Thus \(2A\) is cofinite. But \(A\) itself misses every sufficiently large integer in residue classes \(0,2,3\pmod5\), so \(\operatorname{ord}(A)=2\). ∎

#### Proposition 5
For every infinite \(B\subseteq A\),
\[
2(A\setminus B)
\]
is not cofinite.

#### Proof
Since \(A\setminus(P\cup Q)=\{0\}\), the set \(B\cap(P\cup Q)\) is infinite and hence unbounded.

Let \(b\in B\cap P\). The available residues in \(A\) are \(0,1,4\pmod5\), and the only pair of these residues summing to \(1\pmod5\) is \(0+1\). Since the only element of \(A\) congruent to \(0\pmod5\) is \(0\), every two-term representation of \(b\) in \(A\) is
\[
b=0+b.
\]
After deleting \(b\), no representation survives.

Likewise, if \(b\in B\cap Q\), the only residue decomposition of \(4\) is \(0+4\), so again every representation is \(b=0+b\).

Therefore every \(b\in B\cap(P\cup Q)\) is absent from \(2(A\setminus B)\). There are arbitrarily large such \(b\), proving noncofiniteness. ∎

Hence \(A\) satisfies the full infinite-deletion minimality premise for \(k=2\).

---

### 5. Nonessential deletion can overshoot \(k+1\), even under the premise

Let
\[
C=A\setminus\{0\}=P\cup Q.
\]

#### Proposition 6
The set \(C\) has exact order \(4\).

#### Proof
Modulo \(5\), elements of \(C\) have residues \(1\) and \(-1\). The residues obtainable with \(h\) summands are therefore
\[
h-2t\pmod5,\qquad 0\le t\le h.
\]

For \(h=3\), these are
\[
3,1,4,2\pmod5,
\]
so residue \(0\) is missing. Thus \(3C\) is not cofinite.

For \(h=4\), the residues are
\[
4,2,0,3,1\pmod5,
\]
which are all residues modulo \(5\).

For each prescribed pattern of four residues, the least possible sum is fixed. Any larger integer in the same residue class is obtained by increasing one of the four summands by a multiple of \(5\). Therefore \(4C\) contains all sufficiently large integers in every residue class. Hence
\[
\operatorname{ord}(C)=4.
\]
∎

Thus \(0\) is nonessential in the classical sense—its removal leaves a finite-order basis—but its deletion raises the order from
\[
2\quad\text{to}\quad4>2+1.
\]

Consequently, the essential-element theorem alone cannot justify deleting an arbitrary nonessential element while keeping order at most \(k+1\), even when the original basis satisfies the full premise.

---

### 6. Every finite stage can retain order \(k\), while the limit loses every finite order

Enumerate \(P\cup Q\) as \(b_1,b_2,\dots\), and put
\[
C_j=A\setminus\{b_1,\dots,b_j\}.
\]

Every \(C_j\) still has exact order \(2\). Indeed, removing finitely many elements leaves tails of both residue classes \(P\) and \(Q\). The same residue table used in Proposition 4 then represents every sufficiently large integer.

However,
\[
\bigcap_jC_j=\{0\},
\]
which is not an asymptotic basis of any finite order.

Thus even an iteration in which:

- every deleted element is nonessential;
- every finite-stage survivor retains the original exact order \(k=2\);

can have a limit of infinite order. By Corollary 2, the thresholds of \(3C_j\) necessarily drift without a uniform bound.

This directly refutes the inference
\[
\text{“every finite stage is a \((k+1)\)-basis”}
\ \Longrightarrow\
\text{“the limiting survivor is a \((k+1)\)-basis.”}
\]

---

### 7. The same example also has a successful infinite deletion

The example is not a counterexample to the Erdős problem. Let
\[
B=P\setminus\{1,6\}
\]
and
\[
C^*=A\setminus B=\{0,1,6\}\cup Q.
\]
Then \(B\) is infinite.

#### Proposition 7
The set \(C^*\) has exact order \(3\).

#### Proof
Every sufficiently large integer has a three-term representation:

\[
\begin{array}{c|c}
n\bmod5&\text{representation}\\ \hline
0&n=1+(n-1)+0\\
1&n=1+6+(n-7)\\
2&n=4+4+(n-8)\\
3&n=4+(n-4)+0\\
4&n=n+0+0.
\end{array}
\]
In each row, the variable term belongs to \(Q\) once \(n\) is sufficiently large. For example, all \(n\ge12\) are covered by the relevant row.

Hence \(3C^*\) is cofinite. Since \(B\) is infinite, Proposition 5 shows that \(2C^*\) is not cofinite. Therefore
\[
\operatorname{ord}(C^*)=3.
\]
∎

This illustrates exactly what Route 2 must accomplish: protect a small fixed set of “repair elements” and delete infinitely many elements from a channel whose lost two-term representations can be replaced using the extra summand. The essential-element theorem itself does not identify such a channel.

## Self-Audit

1. **The limiting lemma relies critically on nonnegative summands.**  
   If negative integers were allowed, a fixed \(n\) could have infinitely many relevant tuples and the finite nested-set argument would fail. Under the stated convention \(A\subseteq\mathbb N_0\), every summand is at most \(n\), so the proof is valid.

2. **The residue-class example must control numerical values, not only residues.**  
   Residue coverage alone is not generally enough for cofiniteness. Here each successful residue pattern contains at least one full arithmetic progression \(P\) or \(Q\), and increasing that summand by multiples of \(5\) realizes every sufficiently large value in the residue class. The missing-residue arguments produce entire infinite arithmetic progressions of gaps.

3. **The greedy dichotomy does not advance through the pointwise-minimal case.**  
   It is a genuine reduction, not a solution: the stopped survivor still satisfies the original premise and may be just as difficult as \(A\). I believe the reduction itself is sound because safe finite deletions form a hereditary family, but no claim is made that the reduced case is easier.

## Computations To Verify

The following finite computations verify the residue example and search for similar modular gadgets. They cannot verify the universal quantifier over all infinite deletion sets; that part was proved above.

```python
from itertools import combinations

def hsum(S, h, U):
    """Exactly h summands, repetitions allowed, truncated to [0,U]."""
    reach = {0}
    for _ in range(h):
        reach = {
            x + a
            for x in reach
            for a in S
            if x + a <= U
        }
    return reach

U = 1000
P = {n for n in range(U + 1) if n % 5 == 1}
Q = {n for n in range(U + 1) if n % 5 == 4}
A = {0} | P | Q

# A has an empirical 2-basis tail.
S2A = hsum(A, 2, U)
assert all(n in S2A for n in range(20, U + 1))

# Removing 0 gives order 4, not 3.
C0 = A - {0}
S3C0 = hsum(C0, 3, U)
S4C0 = hsum(C0, 4, U)
assert all(5*t not in S3C0 for t in range(10, U // 5 + 1))
assert all(n in S4C0 for n in range(100, U + 1))

# Each b in P or Q is its own private 2-term witness.
for b in sorted((P | Q) & set(range(1, 300))):
    survivor = A - {b}
    assert b not in hsum(survivor, 2, b)

# Successful deletion: retain only 1 and 6 from P, all of Q, and 0.
Cstar = {0, 1, 6} | Q
S2star = hsum(Cstar, 2, U)
S3star = hsum(Cstar, 3, U)
assert all(n in S3star for n in range(20, U + 1))
assert any(n not in S2star for n in range(100, U + 1))

# Display empirical gaps.
print("2A gaps:", [n for n in range(100) if n not in S2A])
print("3(A-{0}) gaps up to 100:",
      [n for n in range(100) if n not in S3C0])
print("2Cstar gaps in [100,200]:",
      [n for n in range(100,201) if n not in S2star])
```

A modular search for the order jump \(2\to4\):

```python
from itertools import combinations

def add_mod(X, Y, q):
    return {(x + y) % q for x in X for y in Y}

def hfold_mod(D, h, q):
    R = {0}
    for _ in range(h):
        R = add_mod(R, D, q)
    return R

for q in range(2, 15):
    G = set(range(q))
    for r in range(1, q + 1):
        for tup in combinations(range(q), r):
            D = set(tup)
            for x in G - D:
                # x is a singleton exceptional element. For large 2-sums,
                # x+x contributes only one bounded integer, so omit it.
                tail_2A = add_mod(D, D, q) | {(x + d) % q for d in D}
                if (tail_2A == G
                    and hfold_mod(D, 3, q) != G
                    and hfold_mod(D, 4, q) == G):
                    print("gadget:", q, D, x)
                    # Expected example: q=5, D={1,4}, x=0
```

To observe threshold drift under finite deletions:

```python
U = 2000
A = {0} | {n for n in range(U + 1) if n % 5 in (1,4)}
deletion_order = sorted(A - {0})

for j in [0, 10, 50, 100, 200]:
    Cj = A - set(deletion_order[:j])
    S3 = hsum(Cj, 3, U)
    missing = [n for n in range(U + 1) if n not in S3]
    last_gap = max(missing) if missing else -1
    print(j, last_gap)
```

## Route Diagnosis

**Proved ledger**

- Nested finite-stage sumsets satisfy
  \[
  h\Bigl(\bigcap_jC_j\Bigr)=\bigcap_jhC_j.
  \]
- Iterative deletion preserves an \(h\)-basis in the limit exactly when the finite stages have a common tail threshold.
- Safe-deletion families \(\mathcal X_{h,N}\) are closed and hereditary.
- Greedy order-\(k\)-preserving deletion either gives an infinite safe chain or reduces to a pointwise minimal order-\(k\) basis.
- Under the full premise, a nonessential deletion can increase order by more than one.
- Even finite-stage preservation of exact order \(k\) at every stage does not prevent the limit from having infinite order.
- The explicit \(k=2\) stress-test basis satisfies the premise and admits a successful infinite deletion to exact order \(3\).

**Plausible but unproved**

- The additive safe-deletion families may possess a rank or barrier structure stronger than that of arbitrary closed hereditary families.
- In a pointwise minimal order-\(k\) basis, the extra summand may permit simultaneous deletion of infinitely many elements even though no one-point deletion preserves order \(k\).
- The premise may force “private representation channels” analogous to the residue classes in the example, but no such structural theorem has been established.

**Dead ends**

- “Delete any nonessential element; the order rises by at most one” is false.
- “Every finite stage remains a basis, so the intersection is a basis” is false.
- Protecting only finitely many initial representations at each stage does not control newly created gaps at larger scales.
- Bare compactness from arbitrarily large finite deletion masks is insufficient; closed hereditary Schreier families show the obstruction.

**Precise block**

Route 2 requires constructing distinct \(b_j\in A\) and a fixed \(N\) such that
\[
[N,\infty)\subseteq
(k+1)\left(A\setminus\{b_1,\dots,b_j\}\right)
\quad\text{for every }j.
\]
The essential-element theorem only guarantees that finite-stage survivors can be kept as bases of some finite orders, with neither the bound \(k+1\) nor a common threshold. Proving the displayed uniform invariant is essentially the original problem, so Route 2 is blocked rather than completed.

A fresh attempt should study the Cantor–Bendixson or Ramsey-theoretic ranks of the additive families \(\mathcal X_{h,N}\), seeking a theorem that passage from \(k\) to \(k+1\) forces an infinite member. The concrete residue example suggests a complementary structural attack: classify representation channels that make every infinite deletion create \(k\)-gaps, then show one channel can be thinned while the extra summand repairs it.