STATUS: BLOCKED
## Result

Route 4 reduces rigorously to a bounded-predecessor compactness theorem: the problem has an affirmative solution if and only if there is a function \(b:\mathbb N\to\mathbb N_0\) such that every finite initial segment has a valid two-color ordering in which \(n\) has at most \(b(n)\) same-color predecessors. I prove this equivalence, but I could not establish such bounds. I also prove a quantitative “rank escape” obstruction showing why ordinary compactness cannot supply them, prove that \(\mathbb N\) and every cofinite subset admit no single avoiding enumeration, and show that the canonical parity-recursive compactness order cannot be split into finitely many induced \(\omega\)-orders. A separate dyadic-shell coloring reduces the original problem to an explicit family of finite extension lemmas; this appears computationally testable but remains unproved.

## Complete Argument

### 1. A dyadic-ray obstruction for every sequenceable set

Call \(A\subseteq\mathbb N\) sequenceable if it has an enumeration avoiding monotone three-term arithmetic progressions.

#### Lemma 1

Let \(A\subseteq\mathbb N\) be sequenceable, with position function \(p:A\to\mathbb N\). Fix \(u\in A\). Then there are only finitely many \(v>u\) for which

\[
u+2^k(v-u)\in A\qquad\text{for every }k\ge 0.
\]

#### Proof

Let

\[
P_u=\{a\in A:p(a)\le p(u)\}.
\]

This is finite, so let

\[
M_u=\max P_u.
\]

Suppose that \(v>M_u\) and that

\[
v_k=u+2^k(v-u)\in A
\]

for every \(k\ge0\). Since \(v_k\ge v>M_u\), none of the \(v_k\) belongs to \(P_u\). Hence

\[
p(u)<p(v_k)\qquad(k\ge0).
\]

For every \(k\),

\[
u+v_{k+1}=2v_k,
\]

so \(u,v_k,v_{k+1}\) is an arithmetic progression whose numerical middle term is \(v_k\). If \(p(v_{k+1})>p(v_k)\), then

\[
p(u)<p(v_k)<p(v_{k+1}),
\]

which is forbidden. Therefore

\[
p(v_{k+1})<p(v_k)
\]

for every \(k\). This gives an infinite strictly descending sequence of positive integer positions,

\[
p(v_0)>p(v_1)>p(v_2)>\cdots,
\]

which is impossible.

Thus every such \(v\) is at most \(M_u\), and there are only finitely many. ∎

#### Corollary 2

Neither \(\mathbb N\) nor any cofinite subset of \(\mathbb N\) is sequenceable.

#### Proof

Let \(A\) be cofinite and suppose it is sequenceable. Fix \(u\in A\), and let \(M_u\) be as in Lemma 1. Choose

\[
v>\max\bigl(M_u,\max(\mathbb N\setminus A)\bigr).
\]

Then every number \(u+2^k(v-u)\) is at least \(v\), hence belongs to \(A\). This contradicts Lemma 1. Taking \(A=\mathbb N\) gives the first assertion. ∎

Consequently, if the original two-color problem has a solution, both color classes are automatically infinite: if one were finite, the other would be cofinite and therefore not sequenceable.

This also demonstrates concretely that finite satisfiability with one color does not admit an automatic order-type upgrade.

---

### 2. Exact bounded-rank compactness criterion

For a finite colored set, say that an element \(n\) has predecessor count

\[
\operatorname{pred}(n)
 =
\left|\{m:\chi(m)=\chi(n),\ m\prec_{\chi(n)} n\}\right|.
\]

Here \(\prec_c\) denotes the proposed order on color \(c\).

#### Theorem 3: bounded-predecessor criterion

The original problem has an affirmative solution if and only if there exists a function

\[
b:\mathbb N\to\mathbb N_0
\]

with the following property:

> For every \(N\), there is a coloring of \([N]\) by two colors and an avoiding total order on each color class such that
> \[
> \operatorname{pred}(n)\le b(n)
> \qquad(1\le n\le N).
> \]

#### Proof

**Forward implication.** Suppose the original problem has a solution, with position functions \(p_c\). Define

\[
b(n)=p_{\chi(n)}(n)-1.
\]

Restrict the coloring and the two orders to \([N]\). Avoidance is hereditary, and restriction can only decrease predecessor counts. Hence the restricted structure satisfies the stated bounds.

**Reverse implication.** Fix such a function \(b\).

For each \(N\), let \(\mathcal T_N\) be the finite set of all valid colored ordered structures on \([N]\) satisfying the bounds \(b(1),\dots,b(N)\). Connect a structure in \(\mathcal T_{N+1}\) to its restriction in \(\mathcal T_N\).

Restriction preserves coloring, avoidance, totality on each color class, and the predecessor bounds. Thus these sets form a finitely branching rooted tree. By hypothesis, every level is nonempty. Kőnig’s infinity lemma therefore supplies a coherent infinite branch.

The coherent branch defines:

- a color \(\chi(n)\) for every \(n\);
- a total order \(\prec_c\) on each infinite color class;
- all required non-betweenness constraints.

For every \(n\), the global number of same-color predecessors is at most \(b(n)\). Indeed, if \(n\) had \(b(n)+1\) distinct predecessors, all of them would occur in some sufficiently large \([N]\), contradicting the bound at that level.

It remains to show that a countably infinite total order in which every element has finitely many predecessors has order type \(\omega\). For an element \(x\), define

\[
r(x)=|\{y:y\prec x\}|.
\]

If \(x\prec y\), then every predecessor of \(x\), together with \(x\), is a predecessor of \(y\), so

\[
r(y)\ge r(x)+1.
\]

Thus \(r\) is injective. The predecessor set of any element is a finite linear order, so if an element has rank \(r\), its predecessors have ranks exactly \(0,\dots,r-1\). Since the whole order is infinite, the ranks are unbounded. Hence every nonnegative integer occurs as a rank exactly once, and increasing rank gives an \(\mathbb N\)-enumeration.

Thus each infinite color class has an avoiding enumeration. By Corollary 2, neither class can be finite, since the other would then be cofinite. ∎

This is the precise compactness upgrade needed by Route 4. Unfortunately, producing \(b\) is essentially the unresolved quantitative core of the problem.

---

### 3. Quantitative rank escape in the one-color case

The next lemma shows that failure of bounded ranks is not merely a formal concern.

Let

\[
T(n)=2n-1.
\]

For an odd positive integer \(q\), the corresponding \(T\)-orbit is

\[
1+q,\quad 1+2q,\quad 1+2^2q,\quad\ldots.
\]

Distinct odd \(q\)'s give disjoint orbits.

#### Lemma 4: finite rank escape

Let \(q_1,\dots,q_r\) be distinct positive odd integers, and let

\[
v_{i,k}=1+2^kq_i
\qquad(1\le i\le r,\ 0\le k\le L).
\]

Suppose a finite set containing \(1\) and all \(v_{i,k}\) has a one-color avoiding order \(p\), and suppose

\[
p(1)\le r.
\]

Then for some \(i\),

\[
p(v_{i,0})\ge L+1.
\]

More precisely, \(v_{i,0}\) has at least \(L\) predecessors among its own orbit.

#### Proof

At most \(r-1\) elements precede \(1\). Since the \(r\) finite orbit segments are pairwise disjoint, at least one orbit segment contains no element preceding \(1\). Fix such an \(i\). Then

\[
p(1)<p(v_{i,k})
\qquad(0\le k\le L).
\]

For \(k<L\),

\[
1+v_{i,k+1}=2v_{i,k}.
\]

Avoidance therefore forces

\[
p(v_{i,k+1})<p(v_{i,k}).
\]

Consequently,

\[
p(v_{i,L})<p(v_{i,L-1})<\cdots<p(v_{i,0}).
\]

Thus \(v_{i,0}\) has at least the \(L\) elements

\[
v_{i,1},\dots,v_{i,L}
\]

before it. ∎

#### Corollary 5

For every proposed one-color predecessor budget \(b:\mathbb N\to\mathbb N_0\), some finite initial segment has no one-color avoiding order satisfying all the bounds \(b(n)\).

#### Proof

Set

\[
r=b(1)+1,\qquad q_i=2i-1,\qquad v_i=1+q_i=2i.
\]

For each \(i\), take an orbit segment of length

\[
L_i=b(v_i)+1.
\]

Choose \(N\) large enough to contain all these orbit segments. If \([N]\) had a \(b\)-bounded one-color avoiding order, then \(p(1)\le r\). The proof of Lemma 4, with the individual lengths \(L_i\), gives an orbit not meeting the predecessors of \(1\), and hence

\[
\operatorname{pred}(v_i)\ge L_i=b(v_i)+1,
\]

contrary to the budget. ∎

Thus any successful Route 4 argument must use the second color in an essential quantitative way, namely to interrupt these affine doubling rays. Finite satisfiability alone is categorically insufficient.

---

### 4. Failure of the canonical parity-recursive compactness order

The finite parity recursion has a natural infinite compactness limit. Write nonnegative integers as eventually-zero binary strings, with the least significant bit first. At every finite binary prefix, choose an orientation of its two children. Compare two integers at their first differing bit, using the orientation at their common prefix.

Every residue class modulo \(2^k\) is then a convex interval.

#### Lemma 6

Every such oriented binary-trie order avoids all numerical three-term arithmetic progressions.

#### Proof

Let

\[
x<y<z,\qquad x+z=2y,
\]

and write \(d=y-x=z-y\). Let \(t=v_2(d)\).

Then \(x\) and \(z=x+2d\) are congruent modulo \(2^{t+1}\), while \(y=x+d\) agrees with them in bits \(0,\dots,t-1\) and has the opposite bit at position \(t\).

Therefore, at the node corresponding to their common first \(t\) bits, both endpoints \(x,z\) lie in one child cylinder and the midpoint \(y\) lies in the other child cylinder. Since child cylinders are convex and disjoint, \(y\) cannot lie order-theoretically between \(x\) and \(z\). ∎

Despite perfect local avoidance, this order cannot be upgraded by coloring its elements and taking induced suborders.

#### Lemma 7

Every oriented binary-trie order on the eventually-zero binary strings contains an infinite descending sequence.

#### Proof

If the order has no least element, choose recursively

\[
x_0>x_1>x_2>\cdots.
\]

Suppose instead that it has a least element \(x\). At every prefix along the binary path of \(x\), the child followed by \(x\) must be the first child; otherwise the other child cylinder would contain elements before \(x\).

Since \(x\) is eventually zero, choose \(K\) so that all bits of \(x\) at positions at least \(K\) are zero. For \(k\ge K\), let \(y_k\) agree with \(x\) below bit \(k\), have bit \(1\) at \(k\), and have all higher bits zero.

The path of \(x\) takes the first child at level \(k\), so

\[
x<y_k.
\]

If \(K\le k<\ell\), then at bit \(k\), \(y_\ell\) follows \(x\) through the first child while \(y_k\) takes the second child. Hence

\[
y_\ell<y_k.
\]

Thus

\[
y_K>y_{K+1}>y_{K+2}>\cdots
\]

is an infinite descending sequence. ∎

#### Corollary 8

No finite coloring of such a trie order can make every induced color order have type \(\omega\).

#### Proof

An infinite descending sequence has an infinite monochromatic subsequence under every finite coloring. That subsequence is descending in the corresponding induced color order, whereas an order of type \(\omega\) has no infinite descending sequence. ∎

Therefore the particularly natural strategy

1. take the parity-recursive compactness order;
2. split it into two induced \(\omega\)-orders,

is impossible.

This does not rule out two separately constructed orders, nor does it rule out every possible compactness witness.

---

### 5. A separate dyadic-shell reduction

A potentially more structured way to obtain the uniform bounds required by Theorem 3 is the coloring

\[
\chi(n)=\lfloor\log_2 n\rfloor\pmod 2.
\]

Let

\[
B_k=[2^k,2^{k+1}-1].
\]

Thus \(B_k\) has color \(k\bmod 2\). Enumerate the blocks of each color in increasing \(k\), using some finite internal order \(\pi_k\) on \(B_k\).

This is automatically a genuine \(\omega\)-enumeration because every preceding block is finite.

#### Lemma 9: exact shell reduction

The resulting two enumerations avoid monotone three-term progressions if, for each \(k\), the internal order \(\pi_k\) satisfies:

1. every progression lying entirely in \(B_k\) is non-monotone in \(\pi_k\);
2. whenever
   \[
   x<y<z,\qquad x+z=2y,
   \]
   with \(y,z\in B_k\) and \(x\in B_j\) for some \(j<k\) of the same parity as \(k\), one has
   \[
   z\prec_{\pi_k} y.
   \]

These conditions are also necessary for this particular block-concatenation construction.

#### Proof

Consider a monochromatic progression \(x<y<z\), and put

\[
\ell(t)=\lfloor\log_2 t\rfloor.
\]

Since \(z=2y-x<2y\),

\[
\ell(z)\le \ell(y)+1.
\]

Monochromaticity says that \(\ell(y)\) and \(\ell(z)\) have the same parity. Since \(\ell(z)\ge\ell(y)\), it follows that

\[
\ell(z)=\ell(y).
\]

Thus \(y,z\) lie in the same dyadic block.

If \(x\) is also in that block, condition 1 is exactly what is required. Otherwise \(x\) lies in an earlier same-color block and therefore precedes both \(y\) and \(z\) in the concatenated enumeration. The numerical midpoint \(y\) avoids lying between the endpoint positions precisely when \(z\) precedes \(y\), giving condition 2. ∎

Hence the original problem would be solved by proving the following purely finite statement for every \(k\):

> The finite interval \(B_k\) has an AP-avoiding order satisfying all precedence constraints \(z\prec y\) generated by lower same-color shells.

I do not have a proof, and it may fail at some finite \(k\). Unlike unrestricted finite satisfiability, this is a nontrivial finite family and should be tested immediately.

---

### 6. Ledger

**Proved**

1. The dyadic-ray obstruction, Lemma 1.
2. No cofinite subset of \(\mathbb N\) is sequenceable.
3. Any affirmative solution necessarily has two infinite color classes.
4. The bounded-predecessor compactness criterion, Theorem 3.
5. Quantitative one-color rank escape, Lemma 4 and Corollary 5.
6. Every oriented least-significant-bit trie order avoids all progressions.
7. Every such trie order has an infinite descending sequence and cannot be split into finitely many induced \(\omega\)-orders.
8. The exact dyadic-shell reduction, Lemma 9.

**Plausible but unproved**

1. There may be a reasonably growing budget \(b(n)=O(n)\) satisfying Theorem 3.
2. The finite shell-extension systems in Lemma 9 may be satisfiable for every \(k\).
3. If shell satisfiability persists, there may be a substitution or recursion theorem proving all levels at once.

**Dead ends**

1. Bare compactness: one-color finite satisfiability plus Corollary 2 shows it cannot enforce order type \(\omega\).
2. Taking the canonical parity-recursive compactness order and splitting it into two induced sequences: Corollary 8 rules this out.
3. Tracking only the rank of one fixed small integer: rank can escape along one of many disjoint dyadic rays, so controlling finitely many selected ranks is inadequate.

## Self-Audit

1. **The bounded-predecessor criterion is exact but does not produce the needed bounds.**  
   This is the central limitation: Theorem 3 repackages the missing order-type upgrade into a quantitative finite theorem of comparable strength. I believe the equivalence itself is complete because the forward direction is restriction, while the reverse direction uses a finitely branching tree and explicitly proves finite predecessor sets yield order type \(\omega\).

2. **The ray obstruction uses a specially chosen affine family and is only necessary.**  
   A two-coloring can interrupt these rays, so Lemma 1 does not approach a disproof by itself. The lemma is nevertheless rigorous: every orbit element is placed after the center, and each progression then forces a strict rank descent.

3. **The dyadic-shell proposal remains entirely conditional on finite feasibility.**  
   I have proved only the reduction, not the shell-extension lemma. The reduction is reliable because \(z<2y\) forces the midpoint and upper endpoint of every monochromatic cross-shell progression into the same shell. No claim is made that the resulting finite constraints are always satisfiable.

## Computations To Verify

The following uses `z3-solver`.

```python
from z3 import *
from itertools import permutations

def check_avoiding(seq):
    pos = {x: i for i, x in enumerate(seq)}
    S = set(seq)
    vals = sorted(S)
    for i, x in enumerate(vals):
        for z in vals[i+1:]:
            if (x + z) % 2:
                continue
            y = (x + z) // 2
            if y in S:
                if min(pos[x], pos[z]) < pos[y] < max(pos[x], pos[z]):
                    return False
    return True
```

### A. Search for a uniform bounded-rank function

Here `b[n]` is a proposed predecessor budget. Numeric rank variables are equivalent to predecessor bounds because same-color ranks are distinct nonnegative integers.

```python
def bounded_two_color_instance(N, b, fixed_colors=None):
    s = Solver()
    C = {n: Int(f"C_{n}") for n in range(1, N+1)}
    R = {n: Int(f"R_{n}") for n in range(1, N+1)}

    for n in range(1, N+1):
        s.add(0 <= C[n], C[n] <= 1)
        s.add(0 <= R[n], R[n] <= b[n])
        if fixed_colors is not None and n in fixed_colors:
            s.add(C[n] == fixed_colors[n])

    # Same-color ranks must be distinct.
    for x in range(1, N+1):
        for y in range(x+1, N+1):
            s.add(Or(C[x] != C[y], R[x] != R[y]))

    # The numerical midpoint must be a rank extremum.
    for x in range(1, N+1):
        for z in range(x+2, N+1):
            if (x + z) % 2:
                continue
            y = (x + z) // 2
            same = And(C[x] == C[y], C[y] == C[z])
            extremum = Or(
                And(R[y] < R[x], R[y] < R[z]),
                And(R[y] > R[x], R[y] > R[z])
            )
            s.add(Implies(same, extremum))

    return s, C, R

# Candidate budgets to test:
for alpha in [0.5, 1.0, 2.0, 4.0]:
    for N in range(1, 101):
        b = {n: int(alpha*n) + 5 for n in range(1, N+1)}
        s, C, R = bounded_two_color_instance(N, b)
        if s.check() == unsat:
            print("Failed:", alpha, N)
            break
```

A persistent satisfiable budget such as \(b(n)=Cn+O(1)\) would be significant evidence, but not a proof for all \(N\).

### B. Verify finite rank escape

```python
def verify_escape(r, L):
    qs = [2*i - 1 for i in range(1, r+1)]
    bases = [1 + q for q in qs]
    S = {1}
    for q in qs:
        for k in range(L+1):
            S.add(1 + (2**k)*q)
    S = sorted(S)

    for seq in permutations(S):
        if not check_avoiding(seq):
            continue
        pos = {x: i+1 for i, x in enumerate(seq)}
        if pos[1] <= r:
            assert any(pos[v] >= L+1 for v in bases)

# Small feasible exhaustive checks:
verify_escape(r=2, L=2)
# r=2, L=3 is 9! permutations and may still be manageable.
```

### C. Test the dyadic-shell finite extension lemma

```python
def shell_instance(k):
    lo, hi = 2**k, 2**(k+1) - 1
    B = list(range(lo, hi+1))
    lower_same = [
        n for n in range(1, lo)
        if (n.bit_length() - 1) % 2 == k % 2
    ]

    s = Solver()
    R = {n: Int(f"R_{k}_{n}") for n in B}
    for n in B:
        s.add(0 <= R[n], R[n] < len(B))
    s.add(Distinct([R[n] for n in B]))

    # Internal AP constraints.
    Bset = set(B)
    for x in B:
        for z in B:
            if x >= z or (x + z) % 2:
                continue
            y = (x + z) // 2
            if y in Bset:
                s.add(Or(
                    And(R[y] < R[x], R[y] < R[z]),
                    And(R[y] > R[x], R[y] > R[z])
                ))

    # Cross-shell constraints: x is in an earlier same-color shell.
    for x in lower_same:
        for y in B:
            z = 2*y - x
            if z in Bset and y < z:
                s.add(R[z] < R[y])

    return s, R, B

def solve_shell(k):
    s, R, B = shell_instance(k)
    status = s.check()
    if status != sat:
        return None
    m = s.model()
    return sorted(B, key=lambda n: m[R[n]].as_long())

for k in range(0, 11):
    order = solve_shell(k)
    print(k, "SAT" if order is not None else "UNSAT", order)
    if order is None:
        break
```

An `UNSAT` result at any level disproves this shell construction. If levels remain satisfiable, the models should be analyzed for a recursive pattern.

### D. Verify complete shell candidates across all blocks tested

```python
def assemble_shells(K):
    orders = {}
    for k in range(K+1):
        orders[k] = solve_shell(k)
        if orders[k] is None:
            return None

    seq = {0: [], 1: []}
    for k in range(K+1):
        seq[k % 2].extend(orders[k])
    return seq

for K in range(1, 10):
    seq = assemble_shells(K)
    if seq is None:
        print("Shell failure by level", K)
        break
    assert check_avoiding(seq[0])
    assert check_avoiding(seq[1])
    print("Verified through", 2**(K+1)-1)
```

## Route Diagnosis

Route 4 is blocked exactly at the uniform bounded-predecessor theorem in Theorem 3. Ordinary compactness cannot provide it: the one-color case has all finite instances satisfiable, yet Corollary 2 rules out an \(\omega\)-enumeration, and Lemma 4 exhibits the mechanism by which ranks escape. The canonical parity-recursive compactness witness is especially unsuitable because it contains an unavoidable descending chain under every finite induced coloring.

A fresh Route 4 attempt should search directly for explicit budgets and normalization operations on finite two-color solutions, while monitoring all ranks simultaneously rather than a fixed finite collection. The most concrete alternative is the dyadic-shell reduction: first run the shell SAT computation until either a finite obstruction appears or a stable recursive pattern emerges. If all tested shells are satisfiable, the next target should be a finite substitution theorem proving shell feasibility uniformly; that would bypass abstract compactness and give an explicit affirmative construction.