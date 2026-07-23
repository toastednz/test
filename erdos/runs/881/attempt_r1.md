STATUS: BLOCKED

## Result

Route 1 yields an exact hypergraph criterion for success and two rigorous sufficient conditions—one deterministic and one probabilistic—based on representation transversals. Every order-\(k\) basis automatically has polynomially many distinct \((k+1)\)-representation supports and hence polynomial-size sunflowers. However, the sunflower cores can move with \(n\), and even a nonessential element can lie in every \((k+1)\)-representation of infinitely many integers. The hypothesis is exactly equivalent to the absence of an infinite candidate deletion set whose relative \(k\)-representation transversal numbers tend to infinity, while the conclusion is exactly equivalent to the existence of such a set for \(k+1\). I could not prove the required passage from \(k\) to \(k+1\); this is a reformulation of comparable strength, so the route is blocked.

## Complete Argument

### 1. Representation hypergraphs and relative transversals

For \(h\ge1\) and \(n\ge0\), let \(\mathcal H_h(n)\) be the finite hypergraph whose vertices are \(A\cap[0,n]\) and whose edges are the supports of \(h\)-term representations of \(n\):
\[
\mathcal H_h(n)=
\left\{
\{a_1,\dots,a_h\}:a_i\in A,\ a_1+\cdots+a_h=n
\right\}.
\]
Repeated summands are allowed, so an edge can have fewer than \(h\) vertices.

For \(D\subseteq A\), define the relative transversal number
\[
\tau_{h,D}(n)=
\min\left\{|T|:T\subseteq D,\ T\cap E\ne\varnothing
\text{ for every }E\in\mathcal H_h(n)\right\}.
\]
If no such \(T\) exists, put \(\tau_{h,D}(n)=\infty\). For the large \(n\) under consideration, \(\mathcal H_h(n)\ne\varnothing\).

A set \(B\subseteq A\) destroys every \(h\)-term representation of \(n\) exactly when \(B\) is a transversal of \(\mathcal H_h(n)\). Since the hypergraph is finite, this happens if and only if the finite set \(B\cap[0,n]\) is a transversal.

### 2. A deterministic thinning lemma

**Lemma 1.**  
Suppose \(hA\) contains every integer \(n\ge N\). If there is an infinite \(D\subseteq A\) such that
\[
\tau_{h,D}(n)\longrightarrow\infty
\qquad(n\to\infty),
\]
then there is an infinite \(B\subseteq D\) such that
\[
n\in h(A\setminus B)\qquad\text{for every }n\ge N.
\]

**Proof.**

We construct
\[
B_j=\{b_1,\dots,b_j\}\subseteq D
\]
so that \(B_j\) is not a transversal of \(\mathcal H_h(n)\) for any \(n\ge N\).

The empty set \(B_0\) has this property because \(\mathcal H_h(n)\) is nonempty for \(n\ge N\).

Suppose \(B_j\) has been constructed. Let
\[
V_j=\{n\ge N:\tau_{h,D}(n)\le j+1\}.
\]
Because \(\tau_{h,D}(n)\to\infty\), the set \(V_j\) is finite. Choose
\[
b_{j+1}\in D
\]
larger than every element of \(V_j\), larger than \(b_j\), and distinct from the previous choices.

If \(n\in V_j\), then \(b_{j+1}>n\), so \(b_{j+1}\) belongs to no edge of \(\mathcal H_h(n)\). Consequently, adding \(b_{j+1}\) cannot turn \(B_j\) into a transversal of \(\mathcal H_h(n)\).

If \(n\notin V_j\), then
\[
\tau_{h,D}(n)>j+1=|B_{j+1}|,
\]
so \(B_{j+1}\) cannot be a transversal.

Thus the induction continues. Put
\[
B=\bigcup_{j\ge1}B_j.
\]
It is infinite.

Fix \(n\ge N\). Since \(b_j\to\infty\), there is \(J\) such that
\[
B\cap[0,n]=B_J\cap[0,n].
\]
If \(B\) hit every edge of \(\mathcal H_h(n)\), then \(B_J\) would also hit every edge, contradicting the construction. Hence some \(h\)-representation of \(n\) avoids \(B\), so \(n\in h(A\setminus B)\). ∎

There is no threshold-drift gap in this construction: every target \(n\ge N\) is protected at every finite stage and future deletions are eventually larger than \(n\).

### 3. Exact hypergraph reformulation of the problem

**Proposition 2.**  
Let \(hA\) be cofinite. The following are equivalent:

1. There is an infinite \(B\subseteq A\) such that \(h(A\setminus B)\) is cofinite.
2. There is an infinite \(D\subseteq A\) such that
   \[
   \tau_{h,D}(n)\to\infty.
   \]

**Proof.**

The implication \(2\Rightarrow1\) is Lemma 1.

For \(1\Rightarrow2\), take \(D=B\). For all sufficiently large \(n\), the set \(B\) is not a transversal of \(\mathcal H_h(n)\). No subset \(T\subseteq B\) can then be a transversal either. Thus
\[
\tau_{h,B}(n)=\infty
\]
for all sufficiently large \(n\). ∎

Consequently, the premise of Problem #881 is exactly
\[
\forall D\in[A]^\infty,\qquad
\tau_{k,D}(n)\not\longrightarrow\infty,
\]
while the desired conclusion is exactly
\[
\exists D\in[A]^\infty,\qquad
\tau_{k+1,D}(n)\longrightarrow\infty.
\]

Equivalently, under the premise, for every infinite \(D\subseteq A\) there is an integer \(r=r(D)\) and arbitrarily large \(n\) for which \(r\) elements of \(D\) hit every \(k\)-representation of \(n\).

This is a sharp Route 1 reformulation, but proving the required transition from the first statement to the second remains the original difficulty.

### 4. The probabilistic deletion criterion

Enumerate \(A=\{a_1,a_2,\dots\}\). Delete \(a\) independently with probability \(p_a\), and let \(B\) be the random deletion set. Define
\[
\Phi_h(n)=
\Pr\bigl(B\text{ is a transversal of }\mathcal H_h(n)\bigr).
\]

**Lemma 3.**  
If
\[
\sum_{a\in A}p_a=\infty
\]
and
\[
\sum_{n\ge N}\Phi_h(n)<\infty,
\]
then with probability one \(B\) is infinite and \(h(A\setminus B)\) is cofinite.

**Proof.**

The events \(\{a\in B\}\) are independent and have divergent sum of probabilities. The second Borel–Cantelli lemma therefore gives
\[
|B|=\infty
\]
almost surely.

The first Borel–Cantelli lemma, which does not require independence, gives that only finitely many events
\[
\{B\text{ transverses }\mathcal H_h(n)\}
\]
occur almost surely. Thus all sufficiently large \(n\) retain an \(h\)-term representation. ∎

A useful computable bound follows from suitably disjoint representations. Suppose \(E_1,\dots,E_m\in\mathcal H_h(n)\) and the sets
\[
E_j\cap\{a:p_a>0\}
\]
are pairwise disjoint. Then the events that these particular representations are hit are independent, and
\[
\Phi_h(n)
 \le
 \prod_{j=1}^m
 \left(1-\prod_{a\in E_j}(1-p_a)\right)
 \le
 \prod_{j=1}^m\sum_{a\in E_j}p_a.
\]
Thus a summable bound of this form would solve the problem.

### 5. A fixed-core sunflower criterion

A sunflower is a collection of distinct sets
\[
E_j=P\cup Q_j
\]
such that the petals \(Q_j\) are pairwise disjoint.

**Corollary 4.**  
Suppose there is a finite protected set \(P\subseteq A\), constants \(c,\delta>0\), and, for every sufficiently large \(n\), a sunflower of \((k+1)\)-representation supports
\[
E_{n,j}=P_n\cup Q_{n,j},
\qquad 1\le j\le m_n,
\]
such that

- \(P_n\subseteq P\);
- the \(Q_{n,j}\) are pairwise disjoint;
- \(m_n\ge c n^\delta\).

Then there is an infinite \(B\subseteq A\setminus P\) such that
\[
(k+1)(A\setminus B)
\]
is cofinite.

**Proof.**

Retain every element of \(P\), and independently delete each element of \(A\setminus P\) with a fixed probability \(q\) satisfying
\[
0<q<\frac1{k+1}.
\]
For all sufficiently large \(n\), no representation of \(n\) can be supported entirely inside finite \(P\). Thus each petal has at least one unprotected vertex.

The probability that a given sunflower representation is hit is at most
\[
(k+1)q.
\]
The random parts of different petals are disjoint, so
\[
\Phi_{k+1}(n)
 \le ((k+1)q)^{m_n}
 \le \exp(-c' n^\delta)
\]
for some \(c'>0\). This is summable in \(n\). Also
\[
\sum_{a\in A\setminus P}q=\infty.
\]
Lemma 3 applies. ∎

This proves Route 1 under a concrete fixed-core redundancy hypothesis. The obstruction is that the core supplied by a generic sunflower need not lie in any fixed finite protected set.

### 6. Automatic representation abundance

Despite the obstruction, every basis has many distinct \((k+1)\)-representation supports.

Write
\[
A(x)=|A\cap[0,x]|.
\]

**Lemma 5.**  
If every \(n\ge N\) belongs to \(kA\), then for every \(x\ge N\),
\[
A(x)^k\ge x-N+1.
\]

**Proof.**

Every integer in \([N,x]\) is the sum of a \(k\)-tuple from \(A\cap[0,x]\), since the summands are nonnegative and cannot exceed their sum. There are at most \(A(x)^k\) ordered tuples, and these must produce at least \(x-N+1\) distinct sums. ∎

**Lemma 6.**  
For \(n\ge N\),
\[
|\mathcal H_{k+1}(n)|
\ge \frac{A(n-N)}{k+1}.
\]

**Proof.**

For each \(a\in A\cap[0,n-N]\), one has \(n-a\ge N\), hence \(n-a\in kA\). Choose one \(k\)-term representation of \(n-a\) and adjoin \(a\). This produces a \((k+1)\)-representation of \(n\).

A fixed support has at most \(k+1\) distinct elements, so it can arise from at most \(k+1\) choices of the distinguished element \(a\). The stated bound follows. ∎

Combining Lemmas 5 and 6, for \(n\ge2N\),
\[
|\mathcal H_{k+1}(n)|
\ge
\frac{(n-2N+1)^{1/k}}{k+1}.
\]

By the Erdős–Rado sunflower lemma, a family of \(L\) distinct sets of size at most \(r\) contains a sunflower with at least
\[
c_r L^{1/r}
\]
petals, for a constant \(c_r>0\). Indeed, if no \(m\)-sunflower exists, then the subfamily of \(s\)-element sets has size at most
\[
s!(m-1)^s,
\]
and summing over \(0\le s\le r\) gives at most
\[
(r+1)r!(m-1)^r
\]
sets.

Taking \(r=k+1\), every sufficiently large \(n\) therefore has a sunflower of \((k+1)\)-representation supports with
\[
m_n\gg_k n^{1/(k(k+1))}
\]
petals.

This would be far more than enough for Borel–Cantelli if the cores could be protected uniformly. The theorem supplies no such control.

### 7. How the extra summand constrains a small transversal

There is one direct relation between the \(k\)- and \((k+1)\)-hypergraphs.

**Lemma 7.**  
Suppose \(T\subseteq A\) transverses \(\mathcal H_{k+1}(n)\). If
\[
c\in A\setminus T,\qquad c\le n-N,
\]
then
\[
n-c\notin k(A\setminus T).
\]

**Proof.**

If \(n-c\in k(A\setminus T)\), choose a \(k\)-term representation of \(n-c\) avoiding \(T\). Adjoining \(c\notin T\) gives a \((k+1)\)-term representation of \(n\) avoiding \(T\), contrary to the transversal assumption. ∎

Thus a small \((k+1)\)-transversal \(T\) at \(n\) forces at least
\[
A(n-N)-|T|
\]
distinct gaps in \(k(A\setminus T)\), namely the integers
\[
n-c,\qquad c\in A\cap[0,n-N]\setminus T.
\]
By Lemma 5 this is at least polynomially many gaps in \(n\). Unfortunately, a finite deletion is allowed to destroy the \(k\)-basis property, so this does not contradict the premise.

### 8. Counterexample to naive matching growth

Let
\[
A=\{0\}\cup\{1,3,5,\dots\}.
\]
Then \(A\) has exact order \(2\):

- every sufficiently large even integer is a sum of two odds;
- every odd integer is \(0\) plus an odd;
- \(A\) itself is not cofinite.

It also satisfies the infinite-deletion premise for \(k=2\). If an infinite \(B\subseteq A\) contains \(0\), then \(A\setminus B\) consists only of odd numbers, so its two-fold sumset misses every odd number. If \(0\notin B\), then \(B\) contains infinitely many odd numbers. For each odd \(b\in B\), the only possible parity pattern for a two-term representation of \(b\) is
\[
b=0+b,
\]
so \(b\notin2(A\setminus B)\).

For every positive even \(n\), however, every three-term representation of \(n\) uses \(0\): the number of odd summands must be even, and it cannot be zero. Therefore all edges of \(\mathcal H_3(n)\) contain \(0\), and the maximum number of vertex-disjoint representations is exactly \(1\). Thus ordinary pairwise-disjoint representation growth is false even for a basis satisfying the premise.

Nevertheless the desired deletion exists here. Take
\[
B=\{2^j+1:j\ge1\},
\qquad C=A\setminus B.
\]
For every sufficiently large even \(m\), there is an odd
\[
x\in[m/3,2m/3]
\]
such that neither \(x\) nor \(m-x\) lies in \(B\). Indeed, the interval contains \(\gg m\) odd candidates, while at most \(O(\log m)\) are forbidden by either condition. Hence
\[
m=x+(m-x)
\]
with both summands in \(C\).

It follows that every sufficiently large even \(n\) belongs to \(3C\) as
\[
n=0+x+(n-x),
\]
and every sufficiently large odd \(n\) belongs to \(3C\) as
\[
n=1+x+(n-1-x).
\]
On the other hand, every \(b\in B\) is absent from \(2C\). Thus \(C\) has exact order \(3\).

This example illustrates that protected-core sunflowers, not ordinary disjoint representations, are the appropriate Route 1 object.

### 9. Classical essential elements do not control the cores

Let
\[
C=\{n\ge0:n\bmod 5\in\{0,1\}\},
\qquad A=C\cup\{3\}.
\]

Then \(A\) has exact order \(2\). Modulo \(5\),
\[
2\{0,1\}=\{0,1,2\},
\qquad
3+\{0,1\}=\{3,4\},
\]
so \(2A\) is cofinite, while \(A\) is not cofinite.

Removing \(3\) leaves \(C\), which has exact order \(4\):
\[
3\{0,1\}=\{0,1,2,3\}
\]
misses residue \(4\), whereas
\[
4\{0,1\}=\mathbb Z/5\mathbb Z.
\]
Thus \(3\) is nonessential in the classical sense, but
\[
3C
\]
is not cofinite. In particular, every sufficiently large \(n\equiv4\pmod5\) has all of its three-term \(A\)-representations passing through the element \(3\).

No element of \(A\) is classically essential. Removing \(3\) leaves a basis of order \(4\). Removing any fixed \(c\in C\) leaves a basis of order \(2\): for residues \(0,1,2\), there are arbitrarily many \(C+C\) representations from which one can avoid \(c\); residues \(3,4\) are represented as
\[
3+(n-3),
\]
apart from at most the single exceptional value \(n=c+3\).

Therefore, protecting only the finitely many classical essential elements does not control recurring \((k+1)\)-representation cores. This example is diagnostic only; it is not claimed to satisfy the infinite-deletion premise.

## Self-Audit

1. **The main missing implication is substantial.**  
   I did not prove that the premise forces an infinite \(D\) with \(\tau_{k+1,D}(n)\to\infty\). Proposition 2 shows that this is essentially equivalent to the original problem, so it cannot be presented as a solution. The equivalence itself is sound because fixed-\(n\) representation hypergraphs are finite and the greedy construction explicitly prevents threshold drift.

2. **The automatic sunflower argument gives no control over its core.**  
   Polynomially many petals are rigorously guaranteed, but Corollary 4 requires the cores to lie in a fixed protected set. The modular example proves that even classical nonessential elements can recur as unavoidable cores. Thus the conditional probabilistic theorem is correct, but its key hypothesis has not been derived from the problem premise.

3. **The examples test only specific failure modes.**  
   The parity example genuinely satisfies the premise and conclusion, while the mod-\(5\) example only refutes a proposed universal redundancy lemma. Neither settles the general case. Their stated properties nevertheless follow directly from parity and residue-class calculations, including repeated summands.

## Computations To Verify

The following Python computes exact representation-support hypergraphs for each target \(n\), because nonnegative representations of \(n\) use only elements at most \(n\).

```python
from itertools import combinations, combinations_with_replacement
from math import inf

def rep_supports(A, n, h):
    """Exact support hypergraph of h-term representations of n."""
    vals = sorted(a for a in A if 0 <= a <= n)
    H = set()
    for tup in combinations_with_replacement(vals, h):
        if sum(tup) == n:
            H.add(frozenset(tup))
    return H

def relative_tau(H, D):
    """
    Minimum size of T subset D hitting every edge of H.
    Returns inf if an edge is disjoint from D.
    """
    if not H:
        return 0
    parts = [set(E) & set(D) for E in H]
    if any(len(P) == 0 for P in parts):
        return inf
    vertices = sorted(set().union(*parts))
    for r in range(len(vertices) + 1):
        for T in combinations(vertices, r):
            T = set(T)
            if all(T & P for P in parts):
                return r
    return inf

def matching_number(H):
    """Brute-force maximum number of pairwise vertex-disjoint edges."""
    H = list(H)

    def rec(edges):
        if not edges:
            return 0
        E = edges[0]
        without = rec(edges[1:])
        compatible = [F for F in edges[1:] if E.isdisjoint(F)]
        with_E = 1 + rec(compatible)
        return max(without, with_E)

    return rec(H)

def exact_h_sumset(A, h, U):
    S = {0}
    for _ in range(h):
        S = {x + a for x in S for a in A if x + a <= U}
    return S

# ------------------------------------------------------------
# Example 1: A = {0} union the odd numbers.
# ------------------------------------------------------------

U = 250
Aodd = {0} | {n for n in range(1, U + 1, 2)}

for n in range(2, 80, 2):
    H = rep_supports(Aodd, n, 3)
    assert H
    assert all(0 in E for E in H)
    assert matching_number(H) == 1

B = {2**j + 1 for j in range(1, 20) if 2**j + 1 <= U}
Codd = Aodd - B

# Every deleted odd b is a genuine 2-sum gap.
for b in B:
    assert not rep_supports(Codd, b, 2)

S3 = exact_h_sumset(Codd, 3, U)
miss3 = [n for n in range(U + 1) if n not in S3]
print("Parity example: largest observed 3-sum gap =", max(miss3, default=None))

# Relative transversal numbers after protecting 0.
for n in range(20, 51):
    H = rep_supports(Aodd, n, 3)
    D = Aodd - {0}
    print("n =", n, "tau relative to A\\{0} =", relative_tau(H, D))

# ------------------------------------------------------------
# Example 2: residues 0,1 mod 5 plus the exceptional element 3.
# ------------------------------------------------------------

Cmod = {n for n in range(U + 1) if n % 5 in (0, 1)}
Amod = Cmod | {3}

# 2A is observed to cover a full tail.
S2A = exact_h_sumset(Amod, 2, U)
assert all(n in S2A for n in range(30, U + 1))

# 3C misses every residue 4 mod 5.
for n in range(4, U + 1, 5):
    assert not rep_supports(Cmod, n, 3)

# Every large 3-representation of residue 4 uses the exceptional 3.
for n in range(34, U + 1, 5):
    H = rep_supports(Amod, n, 3)
    assert H
    assert all(3 in E for E in H)
    assert relative_tau(H, Amod) == 1

# 4C covers a tail.
S4C = exact_h_sumset(Cmod, 4, U)
assert all(n in S4C for n in range(30, U + 1))

# ------------------------------------------------------------
# Generic diagnostics for a candidate basis.
# ------------------------------------------------------------

def diagnose(A, h, L, U):
    rows = []
    for n in range(L, U + 1):
        Hh = rep_supports(A, n, h)
        Hhp1 = rep_supports(A, n, h + 1)
        rows.append({
            "n": n,
            "num_h_supports": len(Hh),
            "tau_h": relative_tau(Hh, A),
            "nu_h": matching_number(Hh) if len(Hh) <= 30 else None,
            "num_h1_supports": len(Hhp1),
            "tau_h1": relative_tau(Hhp1, A),
            "nu_h1": matching_number(Hhp1) if len(Hhp1) <= 30 else None,
            "common_h1_core": (
                set.intersection(*(set(E) for E in Hhp1))
                if Hhp1 else set()
            ),
        })
    return rows
```

For larger instances, `relative_tau` should be replaced by a \(0\)-\(1\) integer program:
\[
\min\sum_{a\in D}x_a
\quad\text{subject to}\quad
\sum_{a\in E\cap D}x_a\ge1
\quad(E\in\mathcal H_h(n)).
\]
The most relevant computational experiment is to track whether small optimal transversals of \(\mathcal H_{k+1}(n)\) repeatedly use the same vertices, move to new vertices, or admit a fixed finite protected core.

## Route Diagnosis

Route 1 works completely under either of the following additional conditions:

- there is an infinite deletion-candidate set \(D\) with
  \[
  \tau_{k+1,D}(n)\to\infty;
  \]
- or there are polynomially large representation sunflowers whose cores lie in a fixed finite protected set.

The first condition is an exact criterion rather than an independently proved consequence; the second is not automatic. Raw representation abundance is not enough: all representations can share a moving or recurring core. Classical essential-element theory does not remove this obstruction, since a nonessential element can still be indispensable for all \((k+1)\)-representations on an infinite progression.

A fresh attempt should focus on one of two sharply defined tasks:

1. **Affirmative direction:** prove a selection theorem showing that the simultaneous-transversal relation in Lemma 7 forces some infinite \(D\) with \(\tau_{k+1,D}(n)\to\infty\).
2. **Disproof direction:** construct a basis satisfying the premise for which every infinite \(D\subseteq A\) contains bounded-size recurring \((k+1)\)-transversals—equivalently, a system of private or moving witness integers defeating every infinite deletion.

Without control of these recurring cores, probabilistic sparsity alone cannot close the argument.