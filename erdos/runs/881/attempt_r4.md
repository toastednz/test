STATUS: BLOCKED

## Result

Route 4 gives a complete affirmative result for every eventually periodic basis and a useful replacement criterion based on recurring translations. It also exposes the decisive obstruction to a general Kneser argument: even for bases satisfying the infinite-deletion minimality premise, a deletion can make the \((k+1)\)-fold sumset noncofinite while its reduction modulo every finite modulus is complete. Thus failure of cofiniteness need not have any fixed modular explanation. I also give a modular example showing that deleting one nonessential element can raise the order from \(3\) to \(5\), refuting the natural “one deletion costs at most one order” lemma. These results do not settle the general problem.

## Complete Argument

### 1. A necessary modular profile for an asymptotic basis

For a set \(X\subseteq\mathbb Z\) bounded below and an integer \(q\ge1\), define
\[
E_q(X)=\{x\bmod q:x\in X\},
\]
and
\[
R_q(X)=\{r\bmod q:X\cap(r+q\mathbb Z)\text{ is infinite}\}.
\]

#### Lemma 1
If \(hX\) contains all sufficiently large integers, then
\[
R_q(X)+(h-1)E_q(X)=\mathbb Z/q\mathbb Z
\]
for every \(q\ge1\).

#### Proof
Fix \(r\in\mathbb Z/q\mathbb Z\), and choose a sequence \(n_j\to\infty\) with \(n_j\equiv r\pmod q\). For all sufficiently large \(j\),
\[
n_j=x_{j,1}+\cdots+x_{j,h},\qquad x_{j,i}\in X.
\]
Because \(X\) is bounded below, at least one summand tends to infinity as \(j\to\infty\). Passing to a subsequence, we may assume that the same index, say \(i=1\), tends to infinity, and that every \(x_{j,i}\bmod q\) is constant in \(j\). Hence \(x_{j,1}\bmod q\in R_q(X)\), while the other residues lie in \(E_q(X)\). Reducing the representation modulo \(q\) proves that \(r\) lies in the stated sumset. ∎

This is more precise than the elementary condition \(hE_q(X)=\mathbb Z/q\mathbb Z\): at least one residue in each large representation must occur infinitely often in \(X\).

---

### 2. Infinite deletions can preserve all infinitely occupied residue classes

#### Lemma 2
Let \(A\) be countably infinite and let \(\mathcal S=\{S_1,S_2,\dots\}\) be a countable family of infinite subsets of \(A\). Given a finite set \(P\subseteq A\), there is a partition
\[
A=B\sqcup C
\]
such that \(P\subseteq C\) and, for every \(i\),
\[
|B\cap S_i|=|C\cap S_i|=\infty.
\]

#### Proof
List every \(S_i\) infinitely often as
\[
T_1,T_2,\dots.
\]
At stage \(j\), choose two elements \(b_j,c_j\in T_j\setminus P\) not chosen at any earlier stage. This is possible because only finitely many elements have previously been chosen and \(T_j\) is infinite. Assign \(b_j\) to \(B\) and \(c_j\) to \(C\). After completing all stages, assign every unassigned element to \(C\).

Every \(S_i\) occurs infinitely often in the schedule, so it contains infinitely many selected \(b_j\)'s and infinitely many selected \(c_j\)'s. ∎

Applying this to all infinite congruence slices
\[
A\cap(r+q\mathbb Z)
\]
shows that an infinite deletion can be chosen with
\[
R_q(A\setminus B)=R_q(A)
\]
for every \(q\). Under the premise of Problem #881, \(k(A\setminus B)\) must nevertheless be noncofinite. Thus the premise itself allows destruction of order \(k\) without losing any infinitely occupied residue class. Finite exceptional residues may still change, so this observation alone does not eliminate every modular obstruction.

---

### 3. A translation-replacement criterion

The following gives a genuine affirmative result whenever \(A\) contains a suitable recurring additive pattern.

#### Lemma 3
Let \(A\subseteq\mathbb Z\) be bounded below, suppose \(0\in A\), and suppose \(kA\) is cofinite. Assume there is an integer \(\delta>0\) such that

1. \(\delta,2\delta,\dots,k\delta\in A\);
2. there are infinitely many \(x\) such that \(x,x+\delta\in A\).

Then there is an infinite \(B\subseteq A\) such that
\[
(k+1)(A\setminus B)
\]
is cofinite.

#### Proof
Consider all pairs \(\{x,x+\delta\}\subseteq A\). Each integer belongs to at most two such pairs, so from infinitely many pairs one can greedily select infinitely many pairwise disjoint pairs
\[
\{x_j,x_j+\delta\},\qquad j\ge1.
\]
Discard finitely many pairs so that none meets
\[
\{0,\delta,2\delta,\dots,k\delta\}.
\]
Set
\[
B=\{x_j+\delta:j\ge1\},\qquad C=A\setminus B.
\]
Then \(B\) is infinite, every \(x_j\) belongs to \(C\), and
\[
0,\delta,2\delta,\dots,k\delta\in C.
\]

Let \(n\in kA\), say
\[
n=a_1+\cdots+a_k.
\]
Count with multiplicity the number \(t\) of summands \(a_i\) belonging to \(B\).

If \(t=0\), all \(a_i\in C\), and
\[
n=a_1+\cdots+a_k+0\in(k+1)C.
\]

If \(t\ge1\), replace each occurrence \(x_j+\delta\in B\) by its retained predecessor \(x_j\in C\). This decreases the sum by \(t\delta\). Adding the single retained element \(t\delta\in C\) restores the sum. The resulting representation uses
\[
(k-t)+t+1=k+1
\]
elements of \(C\). Hence \(kA\subseteq(k+1)C\). Since \(kA\) is cofinite, so is \((k+1)C\). ∎

This criterion is not universal: thin bases such as polynomial sequences may have only finitely many pairs at every fixed nonzero difference.

---

### 4. Complete solution for eventually periodic bases

Call \(A\subseteq\mathbb N_0\) eventually periodic if there are \(q,N\) and \(D\subseteq\mathbb Z/q\mathbb Z\) such that, for \(n\ge N\),
\[
n\in A\quad\Longleftrightarrow\quad n\bmod q\in D.
\]

#### Theorem 4
Let \(A\) be an eventually periodic asymptotic basis of order at most \(k\). Then there exists an infinite \(B\subseteq A\) for which
\[
(k+1)(A\setminus B)
\]
is cofinite.

Consequently, if \(A\) also satisfies the premise of Problem #881 and has exact order \(k\), then
\[
\operatorname{ord}(A\setminus B)=k+1.
\]

#### Proof
Choose a sufficiently large \(a_*\in A\) lying in one of the eventual residue classes, and translate
\[
A'=A-a_*.
\]
This is a subset of \(\mathbb Z\) bounded below. Translation preserves asymptotic order because
\[
hA'=hA-ha_*.
\]
Moreover, \(0\in A'\), and the eventual residue set \(D'\) of \(A'\) modulo \(q\) contains \(0\).

Let
\[
E=E_q(A').
\]
By Lemma 1, for every \(r\in\mathbb Z/q\mathbb Z\) there are residues
\[
d_r\in D',\qquad e_{r,1},\dots,e_{r,k-1}\in E
\]
such that
\[
r=d_r+e_{r,1}+\cdots+e_{r,k-1}\pmod q.
\]
For each \(r\), choose fixed elements
\[
z_{r,i}\in A',\qquad z_{r,i}\equiv e_{r,i}\pmod q.
\]
Let \(P\) be the finite set consisting of \(0\) and all these \(z_{r,i}\).

Choose any \(\rho\in D'\). Since every sufficiently large integer congruent to \(\rho\pmod q\) lies in \(A'\), we can choose an infinite exponentially sparse set
\[
B'=\{b_j:j\ge1\}\subseteq A'\cap(\rho+q\mathbb Z)
\]
disjoint from \(P\), with
\[
|B'\cap[-X,X]|=O(\log X).
\]
For example, after adjusting finitely many terms, one can take \(b_j=\rho+q2^j\).

Set
\[
C'=A'\setminus B'.
\]
We prove that \((k+1)C'\) is cofinite.

Fix a large \(n\), and let \(r=n\bmod q\). Put
\[
S_r=z_{r,1}+\cdots+z_{r,k-1},\qquad M=n-S_r.
\]
Then
\[
M\equiv d_r\pmod q.
\]
We seek
\[
M=x+y
\]
with
\[
x\equiv d_r\pmod q,\qquad y\equiv0\pmod q,
\]
where both \(x,y\) are sufficiently large and avoid \(B'\).

Among \(x\) in an interval such as
\[
[M/3,2M/3]
\]
with \(x\equiv d_r\pmod q\), there are \(M/(3q)+O(1)\) candidates. For each such \(x\), \(y=M-x\) automatically satisfies \(y\equiv0\pmod q\). The forbidden candidates are those with \(x\in B'\) or \(M-x\in B'\), of which there are only \(O(\log M)\). Thus, for sufficiently large \(M\), a permissible \(x\) exists.

Because \(d_r,0\in D'\), sufficiently large such \(x,y\) both belong to \(A'\), and by construction they do not belong to \(B'\). Also, all \(z_{r,i}\) were protected from deletion. Therefore
\[
n=x+y+z_{r,1}+\cdots+z_{r,k-1}\in(k+1)C'.
\]
This holds for every sufficiently large \(n\).

Translate \(B'\) and \(C'\) back by \(a_*\). The resulting infinite \(B\subseteq A\) satisfies that \((k+1)(A\setminus B)\) is cofinite.

If \(\operatorname{ord}(A)=k\), inclusion prevents \(A\setminus B\) from having order below \(k\). Under the premise of Problem #881, the infinite deletion prevents it from having order \(k\). Hence its exact order is \(k+1\). ∎

---

### 5. A finite deletion can raise the order by more than one

The following modular example kills a tempting iterative Kneser lemma.

#### Proposition 5
Let
\[
A=\{0\}\cup\{n\ge1:n\bmod6\in\{1,2\}\}.
\]
Then
\[
\operatorname{ord}(A)=3,
\]
but
\[
\operatorname{ord}(A\setminus\{0\})=5.
\]

#### Proof
Modulo \(6\), all residues have a three-term representation using \(0,1,2\), with at least one summand in \(\{1,2\}\):
\[
\begin{array}{c|c}
r&\text{residue representation}\\ \hline
0&2+2+2\\
1&1+0+0\\
2&2+0+0\\
3&1+1+1\\
4&2+2+0\\
5&1+2+2.
\end{array}
\]
These residue representations lift to representations of every sufficiently large integer, so \(3A\) is cofinite.

With two summands, every sufficiently large sum has residue in
\[
\{1,2\}+\{0,1,2\}=\{1,2,3,4\}\pmod6.
\]
Thus infinitely many integers congruent to \(0\) or \(5\pmod6\) are absent from \(2A\), proving \(\operatorname{ord}(A)=3\).

Now put
\[
C=A\setminus\{0\}.
\]
A four-term sum of elements whose residues lie in \(\{1,2\}\) has residue represented by an integer between \(4\) and \(8\), so it can have only residues
\[
\{4,5,0,1,2\}\pmod6.
\]
Hence \(4C\) misses every integer congruent to \(3\pmod6\).

Five residues chosen from \(\{1,2\}\) have integer sums \(5,6,7,8,9,10\), covering every residue modulo \(6\). These residue representations again lift to all sufficiently large integers. Therefore \(5C\) is cofinite, and \(\operatorname{ord}(C)=5\). ∎

Thus the claim

> deleting a nonessential element from an order-\(k\) basis leaves a basis of order at most \(k+1\)

is already false for \(k=3\).

---

### 6. A family satisfying the premise: both good and purely nonperiodic bad deletions

For every \(k\ge2\), define
\[
A_k=k\mathbb N_0\cup\{1\}.
\]

#### Proposition 6
For every \(k\ge2\):

1. \(\operatorname{ord}(A_k)=k\);
2. every infinite deletion destroys order \(k\);
3. there is an explicit infinite deletion raising the exact order to \(k+1\);
4. there is also an infinite deletion for which the \((k+1)\)-fold sumset is noncofinite although its reduction modulo every modulus is complete.

#### Proof

##### Exact order \(k\)

Let \(n\equiv r\pmod k\), where \(0\le r\le k-1\). Then
\[
n=\underbrace{1+\cdots+1}_{r\text{ times}}
 +(n-r)+\underbrace{0+\cdots+0}_{k-r-1\text{ times}},
\]
so every sufficiently large \(n\) lies in \(kA_k\).

If \(h<k\), consider large \(n\equiv h\pmod k\). In an \(h\)-term representation, if \(t\) summands are equal to \(1\), then
\[
t\equiv h\pmod k,\qquad 0\le t\le h<k.
\]
Thus \(t=h\), forcing the represented number to be exactly \(h\). Hence all larger \(n\equiv h\pmod k\) are absent from \(hA_k\).

##### Infinite-deletion minimality

Let \(B\subseteq A_k\) be infinite. Since \(A_k\setminus k\mathbb N_0\subseteq\{1\}\), the set \(B\) contains infinitely many multiples \(km\).

For every deleted \(km\), consider
\[
n_m=km+k-1.
\]
In a \(k\)-term representation of \(n_m\), if \(t\) summands equal \(1\), then
\[
t\equiv k-1\pmod k,\qquad 0\le t\le k.
\]
Hence \(t=k-1\), and the remaining summand must be \(km\). Therefore deleting \(km\) destroys every \(k\)-term representation of \(n_m\). These witnesses are unbounded, proving that \(k(A_k\setminus B)\) is not cofinite.

##### A good deletion

Take
\[
B_{\mathrm{good}}=\{k2^j:j\ge0\},
\]
and let \(C_{\mathrm{good}}=A_k\setminus B_{\mathrm{good}}\).

For every sufficiently large \(N\), there are integers \(x,y\) such that
\[
N=x+y
\]
and neither \(x\) nor \(y\) is a power of \(2\). Indeed, choose \(x\in[N/3,2N/3]\). At most \(O(\log N)\) choices are forbidden by \(x\) or \(N-x\) being a power of \(2\), while the interval contains \(\asymp N\) integers.

Given large \(n\equiv r\pmod k\), put
\[
N=\frac{n-r}{k}.
\]
Write \(N=x+y\) as above. Then
\[
n=\underbrace{1+\cdots+1}_{r}
 +kx+ky+\underbrace{0+\cdots+0}_{k-r-1}.
\]
This is a representation by exactly \(k+1\) elements of \(C_{\mathrm{good}}\). Hence \((k+1)C_{\mathrm{good}}\) is cofinite. By the already proved premise, its exact order is \(k+1\).

##### A bad deletion with no finite modular obstruction

Choose integers \(N_j\) with
\[
N_{j+1}>4N_j+1
\]
and define
\[
D=\{0\}\cup\bigcup_{j\ge1}[N_j,2N_j]\cap\mathbb N_0.
\]
Then \(D\) contains arbitrarily long intervals, but \(2D\) has infinitely many gaps. Indeed,
\[
(4N_j,N_{j+1})\cap2D=\varnothing:
\]
two elements from blocks up to \(j\) sum to at most \(4N_j\), while any summand from a later block is at least \(N_{j+1}\).

Delete
\[
B_{\mathrm{bad}}=\{km:m\notin D\}.
\]
The survivor is
\[
C_{\mathrm{bad}}=kD\cup\{1\}.
\]
Let \(N\notin2D\) be large and set
\[
n=kN+k-1.
\]
In a \((k+1)\)-term representation of \(n\), let \(t\) be the number of summands equal to \(1\). Then
\[
t\equiv k-1\pmod k,\qquad 0\le t\le k+1.
\]
For \(k\ge3\), this forces \(t=k-1\). For \(k=2\), the additional possibility \(t=3\) represents only the fixed integer \(3\), so it is irrelevant for large \(n\). Thus a large \(n\) would require exactly two multiples \(kd_1,kd_2\), giving
\[
N=d_1+d_2,
\]
contrary to \(N\notin2D\). Hence \((k+1)C_{\mathrm{bad}}\) is not cofinite.

Nevertheless, for every modulus \(m\),
\[
(k+1)(C_{\mathrm{bad}}\bmod m)=\mathbb Z/m\mathbb Z.
\]
To see this, put \(g=\gcd(k,m)\). Since \(D\) contains arbitrarily long intervals,
\[
\{kd\bmod m:d\in D\}=g\mathbb Z/m\mathbb Z=:H.
\]
Given \(r\bmod m\), choose
\[
0\le t\le g-1\le k-1,\qquad t\equiv r\pmod g.
\]
Then \(r-t\in H\), so choose \(d\in D\) with
\[
kd\equiv r-t\pmod m.
\]
Using \(t\) copies of \(1\), one copy of \(kd\), and \(k-t\) copies of \(0\) gives exactly \(k+1\) summands and total residue \(r\).

In fact, the stronger modular profile from Lemma 1 is also complete: every residue of \(H\) occurs infinitely often among \(kD\), because \(D\) contains arbitrarily long intervals at arbitrarily large scales. Thus the gaps are genuinely scale-dependent, not caused by a missing residue class modulo any fixed modulus. ∎

This is the principal obstruction to Route 4.

## Self-Audit

1. **The eventually periodic theorem is only a restricted result.**  
   Nothing proved here implies that a general basis satisfying the premise has an eventual periodic component. The proof itself is rigorous, but its structural hypothesis is much stronger than the problem’s assumptions.

2. **“No modular obstruction” is used in the fixed finite-quotient sense.**  
   Proposition 6 proves completeness modulo every fixed \(m\), including the robust profile involving infinitely occupied classes. It does not rule out scale-dependent approximate periodicity, which is precisely how the constructed gaps arise.

3. **The replacement criterion requires patterns not forced by basis status.**  
   Lemma 3 is exact once its hypotheses hold, including repeated deleted summands. I found no argument deriving a recurring difference \(\delta\) and the elements \(\delta,\dots,k\delta\) from the minimality premise; thin bases can plausibly avoid every such fixed pattern.

## Computations To Verify

```python
from itertools import product, combinations
from math import gcd

def exact_h_sumset(S, h, U):
    """Exact h-fold sumset, truncated to [0,U]."""
    bits = 1  # {0}
    mask = (1 << (U + 1)) - 1
    for _ in range(h):
        nxt = 0
        for a in S:
            if 0 <= a <= U:
                nxt |= bits << a
        bits = nxt & mask
    return {n for n in range(U + 1) if (bits >> n) & 1}

# Proposition 5: order 3, then order 5 after deleting 0.
U = 1000
A3 = {0} | {n for n in range(1, U + 1) if n % 6 in (1, 2)}
C3 = A3 - {0}

for h in range(1, 6):
    HA = exact_h_sumset(A3, h, U)
    HC = exact_h_sumset(C3, h, U)
    print("h =", h)
    print("A missing after 500:",
          [n for n in range(500, U + 1) if n not in HA][:20])
    print("C missing after 500:",
          [n for n in range(500, U + 1) if n not in HC][:20])

# A_k and the good deletion.
def A_k(k, U):
    return {1} | set(range(0, U + 1, k))

def good_survivor(k, U):
    B = set()
    p = 1
    while k * p <= U:
        B.add(k * p)
        p *= 2
    return A_k(k, U) - B

for k in range(2, 8):
    C = good_survivor(k, U)
    HC = exact_h_sumset(C, k + 1, U)
    print(k, [n for n in range(U // 2, U + 1) if n not in HC][:20])

# Bad block deletion.
def block_D(limit, N1=10, ratio=10):
    D = {0}
    N = N1
    while N <= limit:
        D.update(range(N, min(2 * N, limit) + 1))
        N *= ratio
    return D

for k in range(2, 7):
    D = block_D(U // k)
    Cbad = {1} | {k * d for d in D if k * d <= U}
    H = exact_h_sumset(Cbad, k + 1, U)
    gaps = [n for n in range(U // 4, U + 1)
            if n % k == k - 1 and n not in H]
    print("bad k =", k, "sample gaps:", gaps[:20])

# Exact modular sumsets.
def mod_sumset(S, h, m):
    R = {0}
    for _ in range(h):
        R = {(x + y) % m for x in R for y in S}
    return R

for k in range(2, 8):
    D = block_D(10000)
    for m in range(2, 50):
        residues = {1 % m} | {(k * d) % m for d in D}
        assert mod_sumset(residues, k + 1, m) == set(range(m))

# Search for one-element modular jumps, recovering q=6, k=3,
# D={1,2}, exceptional residue e=0.
def robust_with_exception(D, e, k, q):
    E = set(D) | {e}
    out = set()
    for tup in product(E, repeat=k):
        # At least one summand comes from an infinite residue class D.
        if any(x in D for x in tup):
            out.add(sum(tup) % q)
    return out

for q in range(2, 15):
    universe = list(range(q))
    for size in range(1, q):
        for Dtuple in combinations(universe, size):
            D = set(Dtuple)
            for e in set(universe) - D:
                if robust_with_exception(D, e, 3, q) != set(universe):
                    continue
                if mod_sumset(D, 4, q) == set(universe):
                    continue
                if any(mod_sumset(D, h, q) == set(universe)
                       for h in range(5, 2*q + 1)):
                    print("jump gadget:", q, D, e)
```

## Route Diagnosis

### Proved ledger

- A cofinite \(h\)-fold sumset forces the modular profile
  \[
  R_q(A)+(h-1)E_q(A)=\mathbb Z/q\mathbb Z.
  \]
- One can make an infinite deletion while splitting every infinitely occupied congruence class.
- A recurring translation pattern with retained corrections \(\delta,\dots,k\delta\) yields an infinite deletion preserving order at most \(k+1\).
- Problem #881 is affirmative for every eventually periodic basis.
- A single nonessential deletion can raise order from \(3\) to \(5\), so controlled iterative deletion cannot rely on a one-level jump bound.
- Even for bases satisfying the premise, failure of \((k+1)\)-cofiniteness can occur with complete modular images modulo every fixed modulus.

### Plausible but unproved

- A useful general dichotomy would say that every basis satisfying the premise either contains a replacement pattern as in Lemma 3 or has sufficiently many two-variable representations to permit a sparse deletion. No proof is known here.
- A stronger “scale-sensitive Kneser theorem” might classify nonperiodic gaps of \(k(A\setminus B)\), but such a theorem would need substantially more than finite residue information and appears comparable in strength to the original problem.

### Dead ends

1. **Classify every noncofinite sumset by a fixed modulus:** false.  
   Proposition 6 gives \((k+1)C\) noncofinite with full reduction modulo every modulus.

2. **Delete nonessential elements one at a time, losing at most one order:** false.  
   Proposition 5 gives a jump \(3\to5\).

3. **Preserve all infinitely occupied residue classes and invoke Kneser:** insufficient.  
   Lemma 2 preserves those classes, but the premise still forces \(k\)-gaps; finite and scale-dependent effects remain.

### Precise block

Classical Kneser theory detects fixed periodic stabilizers or density deficits. The desired conclusion can fail for a particular deletion through arbitrarily sparse, scale-dependent gaps invisible in every finite quotient. To finish by Route 4 one would need a new theorem showing that some specially selected infinite deletion cannot create such gaps. Establishing that requires direct control of representations across infinitely many scales—essentially the sparse-deletion or gap-correlation problem from Routes 1, 3, or 5. No such control follows from the given minimality premise by the arguments developed here.