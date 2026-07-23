STATUS: BLOCKED

## Result

I did not resolve the five open density cases or the three open coprime-infinitude cases. Route 2 yields several rigorous structural reductions: representability factors exactly through a unique \(p,q\)-primitive core; primitive representable numbers satisfy an exact affine recursion; ordinary base-\(p\) carrying has a precise state description; and collisions can occur only between different top \(q\)-levels and obey strong lifting-the-exponent constraints. However, these facts do not furnish an \(o(X)\)-sized canonical code. In fact, for each unresolved coprime pair \((5,2),(9,2),(5,3)\), every reduced residue class modulo every modulus \(p^a q^b\) contains a representable integer, so no finite mixed \(p,q\)-adic digit obstruction can work. The unresolved core is to control antichains whose first and last exponent gaps are both \(O(\log\log X)\); the present canonicalization does not compress that family.

## Complete Argument

### 1. Exact reduction to primitive cores

For an integer base \(b\ge2\), write
\[
\nu_b(n):=\max\{a\ge0:b^a\mid n\}.
\]
For composite \(b\), this is not an ordinary prime valuation.

#### Lemma 1: Endpoint exponents are intrinsic

Let
\[
n=\sum_{i=0}^r p^{k_i}q^{\ell_i},
\qquad
k_0<k_1<\cdots<k_r,\quad
\ell_0>\ell_1>\cdots>\ell_r.
\]
Then
\[
\nu_p(n)=k_0,\qquad \nu_q(n)=\ell_r.
\]

**Proof.**
Factor out \(p^{k_0}\):
\[
n=p^{k_0}\left(q^{\ell_0}+
 \sum_{i=1}^r p^{k_i-k_0}q^{\ell_i}\right).
\]
Modulo \(p\), the expression in parentheses is congruent to \(q^{\ell_0}\), which is a unit modulo \(p\) because \(\gcd(p,q)=1\). Thus it is not divisible by \(p\), proving \(\nu_p(n)=k_0\).

Similarly,
\[
n=q^{\ell_r}\left(p^{k_r}+
 \sum_{i=0}^{r-1}p^{k_i}q^{\ell_i-\ell_r}\right),
\]
and the parenthetical expression is congruent to \(p^{k_r}\not\equiv0\pmod q\). Hence \(\nu_q(n)=\ell_r\). ∎

Define the primitive core
\[
\operatorname{core}_{p,q}(n)
 :=
 \frac{n}{p^{\nu_p(n)}q^{\nu_q(n)}}.
\]
It is not divisible by \(p\) or by \(q\), though for composite bases it need not be coprime to \(pq\).

#### Lemma 2: Primitive-core equivalence

For every \(n\ge1\),
\[
n\in\mathcal R_{p,q}
\quad\Longleftrightarrow\quad
\operatorname{core}_{p,q}(n)\in\mathcal R_{p,q}.
\]

**Proof.**
If \(n\) is represented as above, Lemma 1 shows that every exponent pair can be shifted by
\[
(-\nu_p(n),-\nu_q(n)).
\]
All shifted exponents remain nonnegative, incomparability is preserved, and the resulting sum is the primitive core.

Conversely, multiplying every term in a representation of the core by
\[
p^{\nu_p(n)}q^{\nu_q(n)}
\]
shifts every exponent pair by the same vector and preserves incomparability. ∎

Let
\[
P_{p,q}(X)
 =
 \#\{m\le X:m\in\mathcal R_{p,q},\ p\nmid m,\ q\nmid m\}.
\]

#### Corollary 3: Exact counting decomposition

For every \(X\ge1\),
\[
R_{p,q}(X)
 =
 \sum_{a,b\ge0}
 P_{p,q}\!\left(\frac{X}{p^a q^b}\right).
\]

Only finitely many terms are nonzero.

**Proof.**
Every integer has a unique expression
\[
n=p^a q^b m,\qquad p\nmid m,\quad q\nmid m,
\]
because \(\gcd(p,q)=1\). Lemma 2 says \(n\) is representable exactly when \(m\) is. ∎

Consequently,
\[
R_{p,q}(X)=o(X)
\quad\Longleftrightarrow\quad
P_{p,q}(X)=o(X).
\]
The forward implication is immediate from \(P_{p,q}(X)\le R_{p,q}(X)\). For the reverse implication, divide the exact formula by \(X\) and use the summable majorant \(p^{-a}q^{-b}\).

More generally, if
\[
\frac{P_{p,q}(X)}X\longrightarrow \delta,
\]
then dominated convergence gives
\[
\frac{R_{p,q}(X)}X
 \longrightarrow
 \frac{\delta}{(1-1/p)(1-1/q)}.
\]

For prime \(p,q\), the primitive cores are exactly the integers coprime to \(pq\). Thus if only finitely many coprime integers were non-representable, representable integers would have density \(1\), not merely positive density. This illustrates how strong a possible disproof via eventual coprime representability would be.

---

### 2. Exact affine recursion for primitive represented numbers

Let \(\mathcal U_L\) be the set of integers having a normalized antichain representation with
\[
\min k=0,\qquad \min\ell=0,\qquad \max\ell\le L.
\]
Every element of \(\mathcal U_L\) is indivisible by both \(p\) and \(q\).

#### Lemma 4: Affine recursion

One has
\[
\mathcal U_0=\{1\},
\]
and for \(L\ge1\),
\[
\boxed{
\mathcal U_L
 =
 \mathcal U_{L-1}
 \,\cup\,
 \bigcup_{d\ge1}
 \left(q^L+p^d\mathcal U_{L-1}\right).
}
\]

For a fixed \(L\), the sets
\[
q^L+p^d\mathcal U_{L-1},\qquad d\ge1,
\]
are pairwise disjoint.

**Proof.**
A normalized representation whose largest \(q\)-exponent is exactly \(L\) has a unique top term \(q^L\) at \(k=0\). If \(d\ge1\) is the least \(k\)-exponent among the remaining terms, removing \(q^L\) and dividing all remaining terms by \(p^d\) leaves a normalized antichain with all \(\ell\le L-1\). Thus its sum belongs to \(\mathcal U_{L-1}\).

Conversely, shift a normalized antichain for \(m\in\mathcal U_{L-1}\) by \((d,0)\) and adjoin \((0,L)\). Every shifted point has \(k\ge d>0\) and \(\ell\le L-1\), so it is incomparable with \((0,L)\).

For disjointness, suppose
\[
q^L+p^d m=q^L+p^{d'}m',
\]
where \(m,m'\in\mathcal U_{L-1}\). Since \(p\nmid m,m'\),
\[
\nu_p(p^dm)=d,\qquad \nu_p(p^{d'}m')=d'.
\]
Therefore \(d=d'\), and then \(m=m'\). ∎

This recursion is a clean Route 2 formulation: all collisions occur between branches with different top levels \(L\), never between different first gaps \(d\) at one fixed level.

---

### 3. Exact carry normalization

Consider a normalized representation
\[
n=\sum_{i=0}^r p^{k_i}q^{\ell_i},
\qquad
0=k_0<k_1<\cdots<k_r,
\quad
\ell_0>\cdots>\ell_r=0.
\]
Put
\[
P_i=\sum_{j=0}^i p^{k_j}q^{\ell_j},
\qquad
c_i=\left\lfloor\frac{P_i}{p^{k_i}}\right\rfloor,
\]
and
\[
d_i=k_{i+1}-k_i\quad(0\le i<r).
\]

#### Lemma 5: Carry-state recurrence

The carry states satisfy
\[
c_0=q^{\ell_0},
\qquad
c_{i+1}
 =
 q^{\ell_{i+1}}
 +
 \left\lfloor\frac{c_i}{p^{d_i}}\right\rfloor.
\]
Moreover, the ordinary base-\(p\) digit block in positions
\[
k_i,k_i+1,\dots,k_{i+1}-1
\]
is the base-\(p\) expansion of
\[
c_i\bmod p^{d_i}.
\]
In particular,
\[
n
 =
 \sum_{i=0}^{r-1}
 p^{k_i}(c_i\bmod p^{d_i})
 +p^{k_r}c_r.
\]

**Proof.**
Write
\[
P_i=\rho_i+p^{k_i}c_i,\qquad 0\le\rho_i<p^{k_i}.
\]
Then
\[
\left\lfloor\frac{P_i}{p^{k_{i+1}}}\right\rfloor
 =
 \left\lfloor
 \frac{c_i+\rho_i/p^{k_i}}{p^{d_i}}
 \right\rfloor
 =
 \left\lfloor\frac{c_i}{p^{d_i}}\right\rfloor.
\]
Adding the next term \(p^{k_{i+1}}q^{\ell_{i+1}}\) proves the recurrence.

All terms after \(P_i\) are divisible by \(p^{k_{i+1}}\), so modulo the block \(p^{k_{i+1}}/p^{k_i}=p^{d_i}\), the quotient \(\lfloor n/p^{k_i}\rfloor\) is congruent to \(c_i\). This gives the block formula and hence the displayed reconstruction of \(n\). ∎

Thus carrying can be made completely deterministic once the antichain is given. The problem is that different antichains can induce different segmentations of the same standard digit string.

For example, for \((p,q)=(5,2)\),
\[
133=2^7+5=2^3+5^3.
\]
Both are valid two-term antichain representations:
\[
\{(0,7),(1,0)\},
\qquad
\{(0,3),(3,0)\}.
\]
For the first, the carry decomposition is
\[
c_0=128,\quad d_0=1,\quad
c_0\bmod5=3,\quad
c_1=1+\lfloor128/5\rfloor=26,
\]
so
\[
133=3+5\cdot26.
\]
For the second,
\[
c_0=8,\quad d_0=3,\quad
c_0\bmod125=8,\quad c_1=1,
\]
so
\[
133=8+125.
\]
This explicitly defeats uniqueness based on the top exponent, first gap, or base-\(p\) block segmentation.

---

### 4. Arithmetic restriction on cross-level collisions

Define
\[
\omega_{p,q}(t)
 :=
 \max\{a\ge0:p^a\mid q^t-1\}.
\]

#### Lemma 6: Collision constraint

Suppose
\[
n=q^L+p^d m=q^{L'}+p^{d'}m',
\]
where \(L>L'\), \(d,d'\ge1\), and \(p\nmid mm'\). Then
\[
\boxed{
\min(d,d')\le \omega_{p,q}(L-L').
}
\]

**Proof.**
Subtracting gives
\[
q^{L'}(q^{L-L'}-1)
 =
 p^{d'}m'-p^dm.
\]
The right side is divisible by \(p^{\min(d,d')}\). Since \(p\) is coprime to \(q^{L'}\), the same power divides \(q^{L-L'}-1\). ∎

For the five unresolved density pairs, LTE gives explicit formulas.

- For \((5,2)\),
  \[
  \omega_{5,2}(t)=
  \begin{cases}
  0,&4\nmid t,\\
  1+v_5(t/4),&4\mid t.
  \end{cases}
  \]

- For \((7,2)\),
  \[
  \omega_{7,2}(t)=
  \begin{cases}
  0,&3\nmid t,\\
  1+v_7(t/3),&3\mid t.
  \end{cases}
  \]

- For \((5,3)\),
  \[
  \omega_{5,3}(t)=
  \begin{cases}
  0,&4\nmid t,\\
  1+v_5(t/4),&4\mid t.
  \end{cases}
  \]

- For \((9,2)\),
  \[
  \omega_{9,2}(t)=
  \begin{cases}
  0,&t\ \text{odd},\\
  \left\lfloor\frac{1+v_3(t/2)}2\right\rfloor,
       &t\ \text{even}.
  \end{cases}
  \]

- For \((4,3)\),
  \[
  \omega_{4,3}(t)=
  \begin{cases}
  0,&t\ \text{odd},\\
  1+\left\lfloor\frac{v_2(t)}2\right\rfloor,
       &t\ \text{even}.
  \end{cases}
  \]

For instance, in the first case, if \(t=4u\), LTE gives
\[
v_5(2^t-1)
 =
 v_5(2^{4u}-1)
 =
 v_5(2^4-1)+v_5(u)
 =
 1+v_5(u).
\]
The other formulas follow identically, remembering that \(9^a=3^{2a}\) and \(4^a=2^{2a}\).

Since \(L-L'\le\log_q X\), every such collision satisfies
\[
\min(d,d')=O(\log\log X).
\]
Thus two representations with different top levels cannot both have very large first gaps.

This is useful collision rigidity, but it works in the wrong direction for a straightforward compression proof: large-gap branches are essentially disjoint and therefore provide little collision compression.

---

### 5. Large boundary gaps are sparse

#### Lemma 7: First-gap pruning

Let \(\mathcal H_D(X)\) be the primitive represented integers \(n\le X\) which admit a representation
\[
n=q^L+p^d m
\]
with \(d\ge D\). Then
\[
\#\mathcal H_D(X)
 \ll_p X(1+\log_qX)p^{-D}.
\]

**Proof.**
For each \(L\le\log_qX\) and \(d\ge D\), even if \(m\) is allowed to be an arbitrary positive integer, there are at most \(X/p^d\) possible values of \(m\). Hence
\[
\#\mathcal H_D(X)
 \le
 (1+\lfloor\log_qX\rfloor)
 \sum_{d\ge D}\frac X{p^d}
 \ll_p X(1+\log_qX)p^{-D}.
\]
∎

Taking
\[
D=\left\lceil2\log_p\log X\right\rceil
\]
gives
\[
\#\mathcal H_D(X)=O(X/\log X)=o(X).
\]

There is a symmetric statement for the last \(q\)-gap. Removing the bottom term gives a decomposition
\[
n=p^K+q^e m.
\]
Thus the integers admitting a representation with \(e\ge E\) are
\[
\ll_q X(1+\log_pX)q^{-E}.
\]

Therefore any positive-density family of represented integers must overwhelmingly consist of representations whose first and last boundary gaps are both \(O(\log\log X)\). The unresolved difficulty is controlling internal chains made entirely from such short gaps.

---

### 6. Small endpoint ranges are sparse

A normalized antichain inside
\[
\{0,\dots,T\}\times\{0,\dots,L\}
\]
with both coordinate minima zero is determined by choosing the same number \(r\) of positive \(k\)-coordinates and positive \(\ell\)-coordinates; the unique antichain pairing puts them in opposite order. Hence the number of such antichains is
\[
\sum_r\binom Tr\binom Lr
 =
 \binom{T+L}{T}.
\]

#### Lemma 8

The number of primitive represented \(n\le X\) which admit a representation with maximal \(q\)-exponent at most \(L\) is at most
\[
\binom{\lfloor\log_pX\rfloor+L}{L}.
\]

In particular, if
\[
L=o\!\left(\frac{\log X}{\log\log X}\right),
\]
then this number is \(X^{o(1)}\), and hence \(o(X)\).

**Proof.**
Every term is at most \(X\), so every \(k\le\lfloor\log_pX\rfloor\). The antichain count above is therefore an upper bound on the number of representations and hence on the number of represented integers.

Finally,
\[
\log\binom{T+L}{L}
 \le
 L\log\frac{e(T+L)}L
 =
 o(\log X)
\]
under the stated hypothesis. ∎

Thus any substantial represented population must simultaneously use large endpoint exponents but short boundary gaps. This is the exact “long shallow path” regime in which neither raw entropy nor the current carry normalization is effective.

---

### 7. Complete saturation of all finite \(p^a q^b\)-adic unit conditions

The most promising alternative after the carry obstruction is higher boundary congruences. For the three unresolved coprime pairs, however, those congruences are maximally saturated.

#### Lemma 9: Primitive-root facts

For every \(a,b\ge1\):

1. \(2\) generates \((\mathbb Z/5^a\mathbb Z)^\times\);
2. \(2\) generates \((\mathbb Z/3^{2a}\mathbb Z)^\times\);
3. \(3\) generates \((\mathbb Z/5^a\mathbb Z)^\times\);
4. \(5\) generates \((\mathbb Z/3^b\mathbb Z)^\times\).

**Proof.**
For example, every exponent giving \(2^e\equiv1\pmod5\) is divisible by \(4\), and
\[
v_5(2^{4u}-1)=1+v_5(u).
\]
Thus the least exponent producing divisibility by \(5^a\) is
\[
4\cdot5^{a-1}=\varphi(5^a).
\]
The other cases use
\[
v_3(2^{2u}-1)=1+v_3(u),
\]
\[
v_5(3^{4u}-1)=1+v_5(u),
\]
and
\[
v_3(5^{2u}-1)=1+v_3(u),
\]
respectively. In each case the resulting order equals the Euler totient of the modulus. ∎

#### Theorem 10: Mixed-modulus saturation

Let
\[
(p,q)\in\{(5,2),(9,2),(5,3)\}.
\]
For every \(a,b\ge1\) and every residue \(r\) satisfying
\[
\gcd(r,pq)=1,
\]
there is an antichain \(A\) whose sum \(n\) satisfies
\[
n\equiv r\pmod{p^a q^b}.
\]
The resulting \(n\) is itself coprime to \(pq\).

**Proof for \((5,3)\).**
By Lemma 9 choose \(L\ge b\) and \(K\ge a\) such that
\[
3^L\equiv r\pmod{5^a},
\qquad
5^K\equiv r\pmod{3^b}.
\]
Then
\[
n=3^L+5^K
\]
is an antichain sum from \((0,L)\) and \((K,0)\). Modulo \(5^a\), the second term vanishes; modulo \(3^b\), the first term vanishes. Hence CRT gives
\[
n\equiv r\pmod{5^a3^b}.
\]

**Proof for \((5,2)\) and \((9,2)\).**
Write \(p=5\) or \(9\). Choose \(L\ge b\) such that
\[
2^L\equiv r\pmod{p^a};
\]
this is possible by Lemma 9.

Write the binary expansion of \(r\bmod2^b\) as
\[
r\equiv\sum_{j=0}^{s-1}2^{\lambda_j}\pmod{2^b},
\qquad
0=\lambda_0<\lambda_1<\cdots<\lambda_{s-1}<b.
\]
Choose a positive integer \(B\ge a\) divisible by the multiplicative order of \(p\) modulo \(2^b\). Define
\[
k_j=(s-j)B.
\]
Then
\[
k_0>k_1>\cdots>k_{s-1}\ge B\ge a
\]
and
\[
p^{k_j}\equiv1\pmod{2^b}.
\]

Take the exponent pairs
\[
(0,L),\quad
(k_j,\lambda_j)\quad(0\le j<s).
\]
As the \(\lambda_j\)'s increase, the \(k_j\)'s strictly decrease. Since \(L\ge b>\lambda_{s-1}\), these points form an antichain.

Modulo \(p^a\), every low-\(\lambda\) term vanishes because \(k_j\ge a\), leaving \(2^L\equiv r\). Modulo \(2^b\), the top term vanishes and
\[
\sum_j p^{k_j}2^{\lambda_j}
 \equiv
 \sum_j2^{\lambda_j}
 \equiv r.
\]
CRT proves the claim. ∎

Therefore no reduced residue class modulo any modulus \(p^a q^b\) can be forbidden in any of the three unresolved coprime cases. Equivalently, the representable coprime integers are dense in the profinite topology generated by these natural boundary moduli.

This does not rule out an obstruction using other prime factors or a non-periodic sequence of moduli, but it blocks the most direct higher-layer congruence strategy.

---

### 8. Ledger

#### Proved lemmas

1. Endpoint exponents equal \(\nu_p(n)\) and \(\nu_q(n)\).
2. Representability is equivalent to representability of the unique primitive core.
3. Exact convolution formula for \(R_{p,q}(X)\).
4. Exact affine recursion
   \[
   \mathcal U_L
   =
   \mathcal U_{L-1}\cup
   \bigcup_{d\ge1}(q^L+p^d\mathcal U_{L-1}).
   \]
5. Same-level affine branches are disjoint.
6. Exact base-\(p\) carry-state recurrence.
7. Cross-level collisions obey
   \[
   \min(d,d')\le\omega_{p,q}(|L-L'|).
   \]
8. Large first or last gaps contribute \(o(X)\) after a \(2\log\log X\) cutoff.
9. Bounded endpoint ranges contain only \(X^{o(1)}\) represented numbers.
10. Every reduced residue modulo every \(p^a q^b\) contains a representable integer for \((5,2),(9,2),(5,3)\).

#### Plausible but unproved claims

1. The long-shallow-path family, in which all relevant exponent gaps are \(O(\log\log X)\), may still have only \(o(X)\) distinct sums.
2. Cross-level carry collisions may provide enough compression in that family, but no lower bound on collision multiplicity has been established.
3. A two-sided carry normalization, simultaneously exposing base-\(p\) and base-\(q\) blocks, may constrain the internal path more strongly than either one-sided normalization.

#### Dead ends

1. **Ordinary base-\(p\) normalization.** It is exact but not compressive: all unit digit prefixes occur, and \(133=2^7+5=2^3+5^3\) shows nonunique block segmentation.
2. **Rewriting \(p=q^s+1\).** Identities such as \(5=1+2^2\) replace one grid term by comparable terms in the same row, leaving the antichain class. No confluent antichain-preserving rewrite system emerged.
3. **Fixed \(p^a q^b\) congruences.** Theorem 10 shows complete saturation of all reduced residue classes in the three unresolved coprime cases.
4. **Pruning only large gaps.** Large gaps are sparse, but the remaining \(O(\log\log X)\)-gap family is still large enough that a direct first-moment count does not yield \(o(X)\).

## Self-Audit

1. **Composite-base divisibility is easy to mishandle.** Lemmas 1–3 use divisibility by the integers \(p^a\) and \(q^b\), not prime valuations. I believe the statements hold because the unique minimum row contributes a unit modulo the whole integer base, so no cancellation modulo \(p\) or \(q\) is possible.

2. **The mixed-modulus saturation theorem depends on full power orbits.** I supplied the LTE calculations showing the relevant orders equal the Euler totients. The antichain ordering and both CRT components are checked explicitly.

3. **None of the pruning or collision lemmas proves density zero.** Their weakest aspect is scope, not an identified logical gap. In particular, the long-shallow-path family remains uncontrolled, and I have deliberately not inferred \(o(X)\) from these partial bounds.

## Computations To Verify

```python
from collections import Counter, defaultdict
from math import gcd

def exponent_pairs(p, q, X):
    out = []
    pk = 1
    k = 0
    while pk <= X:
        ql = 1
        l = 0
        while pk * ql <= X:
            out.append((k, l, pk * ql))
            ql *= q
            l += 1
        pk *= p
        k += 1
    return out

def exact_representations(p, q, X):
    """Counter[n] = exact number of antichain representations of n."""
    pairs = exponent_pairs(p, q, X)
    K = max(k for k, l, w in pairs)
    L = max(l for k, l, w in pairs)

    weight = {}
    for k, l, w in pairs:
        weight[k, l] = w

    counts = Counter()

    def dfs(k, lmax, total):
        if k > K:
            if total > 0:
                counts[total] += 1
            return

        # Skip row k.
        dfs(k + 1, lmax, total)

        # Choose at most one point from row k; future l must be smaller.
        for l in range(min(L, lmax - 1), -1, -1):
            w = weight.get((k, l))
            if w is not None and total + w <= X:
                dfs(k + 1, l, total + w)

    dfs(0, L + 1, 0)
    return counts

def primitive_U_recurrence(p, q, X):
    """
    Exact numerical sets U_L from:
      U_0={1},
      U_L=U_{L-1} union {q^L+p^d*m}.
    """
    U = {1}
    by_level = [set(U)]
    top_decompositions = defaultdict(list)

    L = 1
    qL = q
    while qL <= X:
        old = set(U)
        new = set(old)
        pd = p
        d = 1
        while qL + pd <= X:
            for m in old:
                n = qL + pd * m
                if n <= X:
                    new.add(n)
                    top_decompositions[n].append((L, d, m))
            pd *= p
            d += 1
        U = new
        by_level.append(set(U))
        L += 1
        qL *= q

    return U, by_level, top_decompositions

def base_power_valuation(base, n):
    a = 0
    while n % base == 0:
        n //= base
        a += 1
    return a

def primitive_core(p, q, n):
    while n % p == 0:
        n //= p
    while n % q == 0:
        n //= q
    return n

def verify_core_equivalence(p, q, X):
    counts = exact_representations(p, q, X)
    represented = set(counts)
    for n in range(1, X + 1):
        c = primitive_core(p, q, n)
        assert ((n in represented) == (c in represented))

def omega(p, q, t):
    return base_power_valuation(p, pow(q, t) - 1)

def verify_collision_constraint(p, q, X):
    U, levels, dec = primitive_U_recurrence(p, q, X)
    for n, reps in dec.items():
        for i in range(len(reps)):
            L, d, m = reps[i]
            for j in range(i):
                L2, d2, m2 = reps[j]
                if L != L2:
                    assert min(d, d2) <= omega(p, q, abs(L - L2))

def multiplicative_order(a, mod):
    assert gcd(a, mod) == 1
    x = 1
    for t in range(1, 10 * mod + 1):
        x = (x * a) % mod
        if x == 1:
            return t
    raise RuntimeError("order search failed")

def discrete_log_with_lower_bound(base, target, mod, lower):
    order = multiplicative_order(base, mod)
    x = 1
    found = None
    for e in range(order):
        if x == target % mod:
            found = e
            break
        x = (x * base) % mod
    if found is None:
        raise ValueError("target not in power orbit")
    while found < lower:
        found += order
    return found

def construct_saturated_antichain(p, q, a, b, r):
    """
    Constructs Theorem 10 antichains for:
      (5,2), (9,2), (5,3).
    Returns list of exponent pairs.
    """
    assert (p, q) in {(5, 2), (9, 2), (5, 3)}
    assert gcd(r, p * q) == 1

    if (p, q) == (5, 3):
        L = discrete_log_with_lower_bound(3, r, 5**a, b)
        K = discrete_log_with_lower_bound(5, r, 3**b, a)
        return [(0, L), (K, 0)]

    # q=2 cases.
    L = discrete_log_with_lower_bound(2, r, p**a, b)

    bits = [l for l in range(b) if ((r % (2**b)) >> l) & 1]
    assert bits and bits[0] == 0

    order = multiplicative_order(p, 2**b)
    B = order
    while B < a:
        B += order

    s = len(bits)
    low_terms = [((s - j) * B, l) for j, l in enumerate(bits)]
    return [(0, L)] + low_terms

def verify_antichain_and_residue(p, q, a, b, r, A):
    B = sorted(A)
    assert all(B[i][0] < B[i+1][0] for i in range(len(B)-1))
    assert all(B[i][1] > B[i+1][1] for i in range(len(B)-1))
    n = sum((p**k) * (q**l) for k, l in B)
    assert n % (p**a * q**b) == r % (p**a * q**b)
    assert gcd(n, p*q) == 1
    return n

def collision_statistics(p, q, X):
    counts = exact_representations(p, q, X)
    R = len(counts)
    A = sum(counts.values())
    E = sum(v*v for v in counts.values())
    max_mult = max(counts.values(), default=0)
    cs_lower = A*A/E if E else 0
    return {
        "R": R,
        "A_antichains": A,
        "A_over_R": A/R if R else 0,
        "energy": E,
        "CS_lower_bound": cs_lower,
        "max_multiplicity": max_mult,
    }

# Suggested runs:
#
# for pair in [(5,2),(7,2),(9,2),(4,3),(5,3)]:
#     for X in [10**3, 3*10**3, 10**4, 3*10**4]:
#         print(pair, X, collision_statistics(*pair, X))
#
# for pair in [(5,2),(9,2),(5,3)]:
#     p,q = pair
#     for a in range(1,5):
#         for b in range(1,7):
#             M = p**a * q**b
#             for r in range(M):
#                 if gcd(r,p*q)==1:
#                     A = construct_saturated_antichain(p,q,a,b,r)
#                     verify_antichain_and_residue(p,q,a,b,r,A)
#
# verify_collision_constraint(5,2,10**6)
# verify_core_equivalence(5,2,10**4)
```

The most informative numerical quantities for Route 2 are:

1. the ratio
   \[
   \frac{\#\{\text{antichain representations of weight}\le X\}}
        {R_{p,q}(X)};
   \]
2. multiplicity distributions conditioned on all first and last gaps being at most \(2\log\log X\);
3. the number of distinct top decompositions \((L,d,m)\) per represented integer;
4. whether cross-level collisions such as \(133=2^7+5=2^3+5^3\) proliferate exponentially or remain rare.

## Route Diagnosis

The exact affine recursion and carry-state normalization are the successful parts of Route 2. They isolate the only possible compression mechanism: overlaps between different top \(q\)-levels. Same-level branches are disjoint, and large-gap cross-level collisions are prohibited by LTE. This leaves a long-shallow-path regime with endpoint exponents of order \(\log X\) but exponent gaps only \(O(\log\log X)\). Proving that this regime has \(o(X)\) distinct sums is essentially the unresolved problem, and I found no canonical code with fewer than \(\log X-o(\log X)\) bits.

The natural alternative, higher \(p^a q^b\) congruences, is also blocked for \((5,2),(9,2),(5,3)\): every reduced residue class is attained by an explicit antichain. A fresh attempt should therefore focus on global, non-finite-state compatibility—most plausibly a two-sided carry process that simultaneously normalizes from the top in base \(p\) and from the bottom in base \(q\), or a weighted entropy estimate specialized to paths whose boundary gaps are \(O(\log\log X)\). Computationally, the decisive preliminary test is whether collision multiplicities in that shallow-gap family grow fast enough to justify further canonical-compression work.