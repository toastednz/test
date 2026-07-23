STATUS: BLOCKED

## Result

The direct weighted-antichain counting strategy required by Route 1 cannot settle any of the five unresolved density pairs. I prove the exact logarithmic growth rate
\[
A_{p,q}(X):=
\#\left\{A:\ A\text{ finite antichain},\ \sum_{(k,\ell)\in A}p^kq^\ell\le X\right\}
=X^{\gamma(p,q)+o(1)},
\]
where
\[
\gamma(p,q)
=
\frac{(\log p+\log q)\log(\log p+\log q)-(\log p)\log\log p-(\log q)\log\log q}
{\log p\,\log q}.
\]
For all five unresolved pairs, \(\gamma(p,q)>1\). Thus the key Route 1 lemma \(A_{p,q}(X)=o(X)\) is false, even by a fixed power of \(X\). The actual weight-sum constraint changes the count only by subpolynomial factors compared with requiring each summand to be at most \(X\). I also prove that for the three unresolved coprime pairs \((5,2),(9,2),(5,3)\), every residue class \(r\bmod M\) with \(\gcd(r,pq)=1\) contains arbitrarily large representable integers. Consequently, no fixed-modulus forbidden-residue argument can settle those coprime cases. The original density and coprime-infinitude questions remain open.

## Complete Argument

### 1. Exact weighted-antichain entropy

Put
\[
a=\log p,\qquad b=\log q.
\]
For \(T>0\), define the finite downset
\[
D_T:=\{(k,\ell)\in\mathbb N_0^2:ak+b\ell\le T\},
\]
and let \(B(T)\) be the number of antichains of \(D_T\), including the empty antichain.

Also let \(A_{p,q}(X)\) denote the number of nonempty antichains satisfying the actual sum constraint
\[
\sum_{(k,\ell)\in A}p^kq^\ell\le X.
\]

#### Lemma 1: Antichains and ideals

For every finite poset \(P\), its antichains are in bijection with its order ideals: an antichain is sent to the ideal it generates, and an ideal is sent to its set of maximal elements.

**Proof.**
If \(A\) is an antichain, let
\[
I(A)=\{x\in P:x\le a\text{ for some }a\in A\}.
\]
This is an order ideal, and its maximal elements are exactly \(A\). Conversely, if \(I\) is an ideal, its maximal elements form an antichain and generate \(I\). These operations are inverse. ∎

#### Lemma 2: Exponential growth of \(B(T)\)

As \(T\to\infty\),
\[
\log B(T)=\gamma(p,q)T+o(T),
\]
where
\[
\gamma(p,q)
=
\left(\frac1a+\frac1b\right)
 \log\left(\frac1a+\frac1b\right)
-\frac1a\log\frac1a-\frac1b\log\frac1b.
\]
Equivalently,
\[
\gamma(p,q)
=
\frac{(a+b)\log(a+b)-a\log a-b\log b}{ab}.
\]

**Proof: upper bound.**
The downset \(D_T\) is contained in the rectangle with
\[
M_T=\left\lfloor\frac{T}{a}\right\rfloor+1
\quad\text{rows},\qquad
N_T=\left\lfloor\frac{T}{b}\right\rfloor+1
\quad\text{columns}.
\]
An order ideal in an \(M_T\times N_T\) rectangle is determined by a monotone lattice path and hence there are
\[
\binom{M_T+N_T}{M_T}
\]
such ideals. By Lemma 1,
\[
B(T)\le \binom{M_T+N_T}{M_T}.
\]
Stirling's formula gives
\[
\log\binom{M_T+N_T}{M_T}
=\gamma(p,q)T+o(T).
\]

**Proof: lower bound.**
Set
\[
M=\left\lfloor\frac{T}{a}\right\rfloor,\qquad
N=\left\lfloor\frac{T}{b}\right\rfloor.
\]
Consider paths from \((0,N)\) to \((M,0)\), using east and south steps, that remain on or below the chord joining those endpoints:
\[
y\le N\left(1-\frac{x}{M}\right).
\]

Every such path bounds an order ideal inside \(D_T\). Indeed, for a point \((x,y)\) on or below the chord,
\[
ax+by
\le ax+bN\left(1-\frac{x}{M}\right).
\]
The right side is linear in \(x\), and its endpoint values are \(bN\le T\) and \(aM\le T\). Hence it is at most \(T\) throughout the interval \(0\le x\le M\).

There are at least
\[
\frac1{M+N}\binom{M+N}{M}
\]
such paths. To see this, reflect the path vertically to obtain a path from \((0,0)\) to \((M,N)\) which stays above its chord. Encode an upward step by the increment \(+M\) and an eastward step by \(-N\). Every word has total increment zero. Rotating the word immediately after a minimum partial sum makes every subsequent partial sum nonnegative, hence gives a path above the chord. Every cyclic orbit has at most \(M+N\) words, so at least a \(1/(M+N)\) fraction of all words can be selected in this way.

Thus
\[
B(T)\ge \frac1{M+N}\binom{M+N}{M}.
\]
Another application of Stirling's formula gives
\[
\log B(T)\ge\gamma(p,q)T+o(T).
\]
Together with the upper bound, this proves the lemma. ∎

#### Theorem 3: Exact exponent under the actual sum constraint

For every coprime \(p,q>1\),
\[
\boxed{\displaystyle
\lim_{X\to\infty}\frac{\log A_{p,q}(X)}{\log X}
=\gamma(p,q).}
\]

**Proof.**
Write \(X=e^T\).

If an antichain has sum at most \(e^T\), every individual term is at most \(e^T\), so it is contained in \(D_T\). Therefore
\[
A_{p,q}(e^T)\le B(T).
\]

For the reverse bound, put
\[
U=T-2\log T.
\]
Every term indexed by \(D_U\) is at most
\[
e^U=\frac{e^T}{T^2}.
\]
An antichain in \(D_U\) contains at most one point in each \(k\)-row, so its cardinality is at most
\[
\left\lfloor\frac{U}{a}\right\rfloor+1=O(T).
\]
Consequently, for all sufficiently large \(T\), every antichain in \(D_U\) has total weight at most
\[
O(T)e^U=O\left(\frac{e^T}{T}\right)\le e^T.
\]
Thus
\[
B(U)-1\le A_{p,q}(e^T).
\]

By Lemma 2,
\[
\log B(T)=\gamma T+o(T),
\qquad
\log B(U)=\gamma U+o(U)=\gamma T+o(T),
\]
because \(U=T-o(T)\). Hence
\[
\log A_{p,q}(e^T)=\gamma T+o(T).
\]
Dividing by \(T=\log X\) proves the theorem. ∎

### 2. Consequence for Route 1

For the five unresolved density pairs, the entropy exponent is:

\[
\begin{array}{c|c}
(p,q)&\gamma(p,q)\\ \hline
(5,2)&\text{approximately }1.263\\
(7,2)&\text{approximately }1.127\\
(9,2)&\text{approximately }1.045\\
(4,3)&\text{approximately }1.120\\
(5,3)&\text{approximately }1.034
\end{array}
\]

In particular, each value is strictly greater than \(1\). Theorem 3 therefore gives, for each unresolved pair,
\[
A_{p,q}(X)=X^{\gamma(p,q)+o(1)}
\]
with \(\gamma(p,q)>1\). Hence there is a \(\delta=\delta(p,q)>0\) such that
\[
A_{p,q}(X)\ge X^{1+\delta}
\]
for all sufficiently large \(X\).

Thus the central Route 1 statement
\[
\#\left\{A:\sum_Ap^kq^\ell\le X\right\}=o(X)
\]
is false for every unresolved pair.

This does not imply that represented integers have positive density: many antichains may have the same sum. It proves that a first-moment representation count cannot establish density zero. Any successful density-one proof must compress or classify collisions between at least \(X^{\gamma-1-o(1)}\) representations per represented value on average if \(R_{p,q}(X)=o(X)\).

For comparison, Theorem 3 immediately gives density one whenever \(\gamma(p,q)<1\), since then
\[
R_{p,q}(X)\le A_{p,q}(X)=X^{\gamma+o(1)}=o(X).
\]
The function \(\gamma\) decreases strictly when either \(a=\log p\) or \(b=\log q\) increases. For example,
\[
\frac{\partial\gamma}{\partial a}
=
-\frac{\log(1+a/b)}{a^2}<0,
\]
and symmetrically in \(b\). This entropy criterion recovers the already-known parameter thresholds but stops exactly before the five unresolved pairs.

### 3. A refinement by antichain length

Let \(A_r(X)\) count admissible antichains of cardinality \(r\) and sum at most \(X\). With \(T=\log X\), every such antichain lies in a rectangle having
\[
M=\frac{T}{a}+O(1),\qquad N=\frac{T}{b}+O(1)
\]
rows and columns. Choosing its \(r\) distinct \(k\)-coordinates and \(r\) distinct \(\ell\)-coordinates determines the antichain uniquely, since they must be paired in opposite order. Therefore
\[
A_r(X)\le \binom Mr\binom Nr.
\]

If \(r/T\to\rho\), Stirling's formula yields
\[
\limsup_{X\to\infty}\frac{\log A_r(X)}{\log X}
\le
f_{a,b}(\rho)
:=
\frac1a H(a\rho)+\frac1b H(b\rho),
\]
where
\[
H(t)=-t\log t-(1-t)\log(1-t).
\]
The function \(f_{a,b}\) is strictly concave and has its unique maximum at
\[
\rho_*=\frac1{a+b},
\]
because
\[
f'_{a,b}(\rho)
=
\log\frac{1-a\rho}{a\rho}
+
\log\frac{1-b\rho}{b\rho},
\]
which vanishes exactly when
\[
(1-a\rho)(1-b\rho)=ab\rho^2,
\]
equivalently \(\rho=1/(a+b)\). At this maximum,
\[
f_{a,b}(\rho_*)=\gamma(p,q).
\]

Thus the superlinear representation count is concentrated, at exponential scale, among antichains having approximately
\[
\frac{\log X}{\log p+\log q}
\]
summands. Merely discarding very short or very long representations cannot repair Route 1.

### 4. Fixed-modulus obstructions also fail for the three unresolved coprime pairs

The following theorem rules out the most direct alternative, Route 3, for \((5,2),(9,2),(5,3)\).

#### Theorem 4: Modular universality

Let
\[
(p,q)\in\{(5,2),(9,2),(5,3)\}.
\]
For every modulus \(M\ge1\) and every integer \(r\) satisfying
\[
\gcd(r,pq)=1,
\]
there are arbitrarily large \(n\in\mathcal R_{p,q}\) such that
\[
n\equiv r\pmod M.
\]

**Proof.**

Factor \(M\) as
\[
M=M_pM_qM_0,
\]
where every prime factor of \(M_p\) divides \(p\), every prime factor of \(M_q\) divides \(q\), and
\[
\gcd(M_0,pq)=1.
\]
These three factors are pairwise coprime. Choose \(A,B\ge0\) such that
\[
M_p\mid p^A,\qquad M_q\mid q^B.
\]

We first record two elementary facts.

**Fact 1: Powers of \(q\) cover all units modulo \(M_p\).**

- \(2\) is a primitive root modulo every \(5^c\);
- \(2\) is a primitive root modulo every \(3^c\);
- \(3\) is a primitive root modulo every \(5^c\).

For example,
\[
v_5(2^{4\cdot5^t}-1)=1+t,\qquad
v_3(2^{2\cdot3^t}-1)=1+t,
\]
and
\[
v_5(3^{4\cdot5^t}-1)=1+t
\]
by the lifting-the-exponent lemma. These identities show that the respective orders are
\[
4\cdot5^{c-1},\qquad
2\cdot3^{c-1},\qquad
4\cdot5^{c-1},
\]
which equal the corresponding Euler \(\varphi\)-values.

Since \(\gcd(r,p)=1\), we may therefore choose an arbitrarily large \(L\ge B\) such that
\[
q^L\equiv r\pmod{M_p}.
\]

**Fact 2: Every residue modulo \(M_q\) can be produced by a low-\(\ell\) antichain block with all \(k\)-exponents arbitrarily large.**

For \(q=2\), fix a large \(K_0\) and consider
\[
w_\ell=2^\ell p^{K_0+B-\ell},
\qquad 0\le\ell<B.
\]
The points
\[
(K_0+B-\ell,\ell)
\]
form an antichain. The \(2^B\) subset sums of the \(w_\ell\) are distinct modulo \(2^B\): if two subsets first differ at index \(\ell\), their difference has exact \(2\)-adic valuation \(\ell\). Thus these subset sums give every residue modulo \(2^B\), hence every residue modulo \(M_q\).

For \((p,q)=(5,3)\), process the ternary positions \(\ell=0,\dots,B-1\) in increasing order. At position \(\ell\), use either no term or one of
\[
3^\ell5^{K_0+2(B-\ell)},
\qquad
3^\ell5^{K_0+2(B-\ell)+1}.
\]
Modulo \(3\), the two coefficients \(5^k\) are \(1\) and \(2\), in some order. Hence, after positions below \(\ell\) have been fixed, one can choose no term, the even-exponent term, or the odd-exponent term to set the next ternary digit to \(0,1,\) or \(2\). The ranges for consecutive \(\ell\)'s are disjoint and descending, so every chosen set is an antichain. This realizes every residue modulo \(3^B\), hence modulo \(M_q\).

Choose such a low-\(\ell\) block \(D\) whose sum is congruent to \(r\pmod{M_q}\), and choose all of its \(k\)-coordinates larger than a threshold \(K_0>A\). Every term of \(D\) is then divisible by \(M_p\).

We next correct the residue modulo \(M_0\). Let
\[
u=\operatorname{ord}_{M_0}(p),\qquad
v=\operatorname{ord}_{M_0}(q),
\]
with the correction omitted if \(M_0=1\). Choose \(L\) and \(K_0\) so large that there are at least \(M_0\) multiples of \(v\) in \([B,L)\) and at least \(M_0\) multiples of \(u\) in \([A,K_0)\).

Let
\[
S_0=q^L+\sum_{x\in D}x.
\]
Choose \(h\in\{0,\dots,M_0-1\}\) satisfying
\[
h\equiv r-S_0\pmod{M_0}.
\]
If \(h>0\), choose
\[
A\le k_1<k_2<\cdots<k_h<K_0
\]
all divisible by \(u\), and
\[
L>\ell_1>\ell_2>\cdots>\ell_h\ge B
\]
all divisible by \(v\). Then each central term satisfies
\[
p^{k_i}q^{\ell_i}\equiv1\pmod{M_0},
\]
while it is divisible by both \(M_p\) and \(M_q\).

The complete exponent set consists of:

1. the point \((0,L)\);
2. the central points \((k_i,\ell_i)\);
3. the low-\(\ell\) block \(D\).

The first point has the smallest \(k\)-coordinate and the largest \(\ell\)-coordinate. All central \(\ell_i\) are at least \(B\), while every point of \(D\) has \(\ell<B\). All central \(k_i\) are below \(K_0\), while all \(k\)-coordinates in \(D\) are above \(K_0\). Within each block, increasing \(k\) corresponds to strictly decreasing \(\ell\). Hence the union is an antichain.

Its sum is congruent to \(r\):

- modulo \(M_p\), only \(q^L\) survives;
- modulo \(M_q\), only the block \(D\) survives;
- modulo \(M_0\), the central block contributes \(h\), correcting \(S_0\).

The Chinese remainder theorem gives
\[
n\equiv r\pmod M.
\]

Finally, increase \(L\) through a fixed arithmetic progression preserving \(q^L\) modulo \(M_pM_0\). The remaining blocks can be held fixed, and the antichain inequalities remain valid. Then \(n\to\infty\), proving that arbitrarily large such \(n\) exist. ∎

Theorem 4 does not show that all sufficiently large integers in a residue class are representable. It shows only that no residue class compatible with coprimality is completely excluded.

## Self-Audit

1. **The lower entropy bound depends on the path-to-ideal correspondence and a cyclic-shift argument.** Off-by-one errors at the axes are the main risk. They do not affect the exponent, and the proof deliberately uses only \(M=\lfloor T/a\rfloor\) columns and \(N=\lfloor T/b\rfloor\) rows. The endpoint inequalities \(aM,bN\le T\) make every cell below a good path lie in \(D_T\).

2. **The passage from an individual-weight bound to the actual sum bound could have failed if antichains had superlogarithmic size.** It does not: an antichain has at most one point in each \(k\)-row, hence \(O(T)\) points in \(D_T\). Replacing \(T\) by \(T-2\log T\) therefore supplies more than enough slack.

3. **The modular-universality construction has several interacting exponent-order constraints.** The construction separates the antichain into three disjoint layers: one high-\(\ell\) pure term, a central block with \(k\ge A,\ell\ge B\), and a low-\(\ell\), high-\(k\) block. The intervals for the exponents can be chosen arbitrarily large, so all strict inequalities and all congruence requirements can be imposed simultaneously. This theorem still gives no density information.

## Computations To Verify

```python
from math import log, gcd
from functools import lru_cache
from collections import Counter

pairs = [(5,2), (7,2), (9,2), (4,3), (5,3)]

def gamma(p, q):
    a, b = log(p), log(q)
    return ((a+b)*log(a+b) - a*log(a) - b*log(b))/(a*b)

for p, q in pairs:
    print((p,q), gamma(p,q))
    assert gamma(p,q) > 1
```

Exact representation and represented-value enumeration:

```python
def max_exp(base, X):
    e, z = 0, 1
    while z * base <= X:
        z *= base
        e += 1
    return e

def representation_counter(p, q, X):
    K = max_exp(p, X)
    L = max_exp(q, X)

    @lru_cache(None)
    def rec(k, lmax):
        # Counter of sums of antichains using rows k,...,K
        # with all selected ell < lmax.
        if k > K:
            return Counter({0: 1})

        out = Counter(rec(k + 1, lmax))  # skip row k

        pk = p ** k
        for ell in range(lmax):
            w = pk * (q ** ell)
            if w > X:
                break
            tail = rec(k + 1, ell)
            for s, multiplicity in tail.items():
                if s + w <= X:
                    out[s + w] += multiplicity
        return out

    c = rec(0, L + 1)
    c.pop(0, None)
    return c

for p, q in pairs:
    for X in [100, 300, 1000, 3000]:
        c = representation_counter(p, q, X)
        A = sum(c.values())
        R = len(c)
        print((p,q), X, "A=", A, "R=", R,
              "log(A)/log(X)=", log(A)/log(X))
```

Verify the binary low-boundary construction:

```python
def binary_low_block(p, B, K0, target):
    pts = []
    S = 0
    for ell in range(B):
        k = K0 + B - ell
        # Invariant: target-S is divisible by 2**ell.
        if ((target - S) // (2**ell)) % 2:
            pts.append((k, ell))
            S += (p**k) * (2**ell)
    assert (S-target) % (2**B) == 0
    pts.sort()
    assert all(pts[i][1] > pts[i+1][1]
               for i in range(len(pts)-1))
    return pts

for p in [5, 9]:
    for B in range(1, 9):
        for t in range(2**B):
            binary_low_block(p, B, 20, t)
```

Verify the ternary low-boundary construction:

```python
def ternary_low_block(B, K0, target):
    pts = []
    S = 0
    for ell in range(B):
        assert (target-S) % (3**ell) == 0
        digit = ((target-S)//(3**ell)) % 3
        if digit:
            candidates = [
                K0 + 2*(B-ell),
                K0 + 2*(B-ell) + 1
            ]
            k = next(k for k in candidates if pow(5, k, 3) == digit)
            pts.append((k, ell))
            S += (5**k) * (3**ell)
    assert (S-target) % (3**B) == 0
    pts.sort()
    assert all(pts[i][1] > pts[i+1][1]
               for i in range(len(pts)-1))
    return pts

for B in range(1, 7):
    for t in range(3**B):
        ternary_low_block(B, 20, t)
```

A finite residue-automaton check for modular universality:

```python
def antichain_residues(p, q, M, K, L):
    @lru_cache(None)
    def rec(k, lmax):
        # Pairs (residue, used_nonempty_term)
        if k > K:
            return frozenset({(0, False)})

        out = set(rec(k+1, lmax))
        for ell in range(lmax):
            w = (pow(p, k, M) * pow(q, ell, M)) % M
            for residue, used in rec(k+1, ell):
                out.add(((residue+w) % M, True))
        return frozenset(out)

    return {r for r, used in rec(0, L+1) if used}

for p, q in [(5,2), (9,2), (5,3)]:
    for M in range(2, 25):
        residues = antichain_residues(p, q, M, 4*M, 4*M)
        targets = {r for r in range(M) if gcd(r, p*q) == 1}
        assert targets <= residues, (p, q, M, targets-residues)
```

## Route Diagnosis

**Proved ledger.**

- The weighted antichain count has the exact exponent
  \[
  A_{p,q}(X)=X^{\gamma(p,q)+o(1)}.
  \]
- The actual sum constraint and the maximum-individual-term constraint have the same power-law exponent.
- For all five unresolved density pairs, \(\gamma(p,q)>1\); hence Route 1’s required first-moment lemma is false.
- Representations contributing the maximal entropy have about
  \[
  \frac{\log X}{\log p+\log q}
  \]
  summands.
- For \((5,2),(9,2),(5,3)\), every residue class compatible with \(\gcd(n,pq)=1\) contains arbitrarily large representable integers.

**Dead ends.**

- **Raw weighted-antichain counting:** decisively dead; it is superlinear for all unresolved pairs.
- **Restricting to the exponential weight triangle:** does not improve the exponent; a polynomial fraction of rectangle paths remain admissible.
- **Discarding very short or very long antichains:** insufficient; the entropy maximum lies at an interior linear-in-\(\log X\) length.
- **Fixed-modulus forbidden residues for the three unresolved coprime pairs:** impossible by Theorem 4.

**Precise block.**

To prove density one after the failure of Route 1, one must count distinct sums rather than antichains. For the unresolved pairs, any such argument must exploit collision/carry structure strong enough to compress
\[
X^{\gamma(p,q)+o(1)}
\]
representations into \(o(X)\) values. I have not constructed a canonical form or a collision theorem providing that compression. Conversely, the superlinear antichain count alone cannot imply positive density of represented integers because it gives no upper bound on collision multiplicities.

A fresh attempt should therefore focus on Route 2: establish a confluent mixed-base carry normalization, or at least a canonical encoding of distinct sums with sublinear complexity. For the coprime question, any modular approach must be size-sensitive or involve an infinite descent; no fixed congruence class can work for the three open pairs.