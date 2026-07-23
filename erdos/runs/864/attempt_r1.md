STATUS: BLOCKED

## Result

The conjectured \(2/\sqrt3\) upper bound remains unproved. I established three rigorous partial results along Route 1: (i) the uniform improvement
\[
F(N)\le \sqrt{2N}+O(N^{1/4});
\]
(ii) an exact exceptional-core difference decomposition, including a finite packing inequality in the parameters “number of complementary pairs” and “number of unpaired elements”; and (iii) an exact reduction of the fully reflected case to a Sidon seed \(X\subseteq[0,w]\) satisfying
\[
D(X)\cap\bigl(S-\Sigma(X)\bigr)=\varnothing,
\]
where \(D(X)\) is the positive difference set and \(\Sigma(X)\) the unordered sum set. The missing theorem is already substantial in the fully reflected case: one would need to prove that this disjointness forces \(S\ge(3-o(1))|X|^2\). Elementary packing gives only \(S\ge(2-o(1))|X|^2\), and the tempting stronger assertion \(S\ge3w\) is false even for small seeds. With unpaired elements, a second unresolved mixed-packing problem remains.

## Complete Argument

### 1. A uniform \(\sqrt2\)-upper bound

Let \(A\subseteq[N]\) be admissible and \(k=|A|\).

If no sum has two representations, then \(A\) is a genuine Sidon set, so the classical bound gives
\[
k\le \sqrt N+O(N^{1/4}).
\]

Suppose now that \(s\) is the unique exceptional sum. Partition
\[
A_-= \{a\in A:2a<s\},\qquad
A_0=\{a\in A:2a=s\},\qquad
A_+=\{a\in A:2a>s\}.
\]
Write
\[
\ell=|A_-|,\qquad h=|A_+|,\qquad \delta=|A_0|\in\{0,1\}.
\]

Every pair sum from \(A_-\) is strictly smaller than \(s\). Therefore a repeated sum inside \(A_-\) would be a second exceptional value, which is impossible. Hence \(A_-\) is a genuine Sidon set. Similarly, every pair sum from \(A_+\) is strictly larger than \(s\), so \(A_+\) is also genuine Sidon.

The set \(A_-\) is contained in an interval of
\[
n_-=\left\lfloor\frac{s-1}{2}\right\rfloor
\]
integer positions, while \(A_+\) is contained in an interval of
\[
n_+=N-\left\lfloor\frac s2\right\rfloor
\]
positions. Notice that
\[
n_-+n_+\le N.
\]
By the classical Sidon bound,
\[
\ell\le \sqrt{n_-}+O(N^{1/4}),\qquad
h\le \sqrt{n_+}+O(N^{1/4}).
\]
Consequently,
\[
\begin{aligned}
k
&=\ell+h+\delta\\
&\le \sqrt{n_-}+\sqrt{n_+}+O(N^{1/4})\\
&\le \sqrt{2(n_-+n_+)}+O(N^{1/4})\\
&\le \sqrt{2N}+O(N^{1/4}).
\end{aligned}
\]
Thus
\[
\boxed{F(N)\le \sqrt{2N}+O(N^{1/4}).}
\]

More precisely,
\[
|A|
\le
\sqrt{\left\lfloor\frac{s-1}{2}\right\rfloor}
+
\sqrt{N-\left\lfloor\frac s2\right\rfloor}
+O(N^{1/4}).
\]
In particular, sets approaching the constant \(\sqrt2\) under this argument must have \(s=N+o(N)\).

---

### 2. Exact structure of duplicated differences

Let
\[
m_A(d)=|\{x:x,x+d\in A\}|,
\qquad 1\le d\le N-1.
\]

#### Lemma 2.1

If \(m_A(d)\ge2\), then \(m_A(d)=2\), and every element occurring in the two representations of \(d\) lies in the exceptional core
\[
C_s=A\cap(s-A).
\]

#### Proof

Suppose
\[
x,x+d,y,y+d\in A,\qquad x<y.
\]
Then
\[
(x+d)+y=x+(y+d)=x+y+d.
\]
The unordered pairs \(\{x+d,y\}\) and \(\{x,y+d\}\) are distinct, including when \(x+d=y\), in which case the first pair is diagonal. Hence their common sum must be \(s\):
\[
x+y+d=s.
\]
It follows that
\[
s-x=y+d,\qquad s-y=x+d.
\]
Thus all four elements are paired under reflection about \(s/2\), and hence lie in \(C_s\).

If a third base \(z\) existed, comparison of the representations based at \(x,y\) and \(x,z\) would give
\[
x+y+d=s=x+z+d,
\]
so \(y=z\). Thus \(m_A(d)\le2\). ∎

Now let

- \(p\) be the number of non-diagonal representations of \(s\);
- \(\delta=1\) if \(s\) is even and \(s/2\in A\), and \(\delta=0\) otherwise;
- \(u=|A\setminus C_s|\).

Then
\[
r_A(s)=p+\delta,\qquad |C_s|=2p+\delta,
\]
and
\[
|A|=2p+\delta+u.
\]

Reflection \(R(a)=s-a\) acts on the unordered pairs of distinct elements of \(C_s\). A pair is fixed by this action precisely when its two elements sum to \(s\). There are exactly \(p\) such fixed pairs. Every other reflection orbit has size two and gives two occurrences of one positive difference.

Different nonfixed reflection orbits give different difference values, since otherwise the corresponding difference would occur at least four times, contradicting Lemma 2.1. A fixed core difference cannot coincide with a nonfixed one, and no difference involving an element of \(A\setminus C_s\) can be repeated at all, again by Lemma 2.1.

Therefore the number of distinct positive differences occurring in \(A\) is exactly
\[
\frac{\binom{2p+\delta}{2}+p}{2}
 +(2p+\delta)u+\binom u2.
\]
Since these differences belong to \(\{1,\dots,N-1\}\), we obtain:

#### Proposition 2.2

Every admissible \(A\subseteq[N]\) with exceptional sum \(s\) satisfies
\[
\boxed{
\frac{\binom{2p+\delta}{2}+p}{2}
 +(2p+\delta)u+\binom u2
 \le N-1.
}
\]

Equivalently, if there is no midpoint,
\[
\boxed{
p^2+2pu+\binom u2\le N-1,
}
\]
while in the midpoint case,
\[
\boxed{
p(p+1)+(2p+1)u+\binom u2\le N-1.
}
\]

Asymptotically, with the midpoint ignored as a lower-order term,
\[
N\ge p^2+2pu+\frac{u^2}{2}-O(p+u).
\]
This is exact at the level of the number of occupied positive-difference labels, but its coefficients are much too small for the conjecture, which would require
\[
N\ge \frac34(2p+u)^2-o(N)
=3p^2+3pu+\frac34u^2-o(N).
\]

---

### 3. Sidon transversals of the exceptional matching

Every choice of at most one endpoint from each noncentral complementary pair, together with all of \(A\setminus C_s\), has no non-diagonal representation of \(s\). Since all other sums were already unique in \(A\), such a set is genuine Sidon, with the possible single diagonal representation at \(s/2\).

One may do slightly better and retain exactly one representation of \(s\):

- if \(\delta=0\), retain both endpoints of one complementary pair and one endpoint from every other pair;
- if \(\delta=1\), retain the midpoint and one endpoint from every noncentral pair.

In either case this gives a genuine Sidon subset of size
\[
u+p+1=|A|-r_A(s)+1.
\]
Thus
\[
\boxed{u+p+1\le S(N).}
\]
In particular,
\[
u+p\le \sqrt N+O(N^{1/4}).
\]

This proves the standard Sidon-extraction estimate in the core parameters, but it does not force \(u=o(|A|)\). Hence it does not justify reducing the general problem to the fully reflected case.

---

### 4. Exact reduction of the fully reflected case

Consider first a set with no midpoint and with every element paired at the exceptional sum. After translation it has the form
\[
C=X\cup(S-X),
\]
where
\[
X\subseteq[0,w],\qquad 0,w\in X,\qquad 2w<S.
\]
Write \(p=|X|\), and define
\[
\Sigma(X)=\{x+x':x,x'\in X,\ x\le x'\}
\]
and
\[
D(X)=\{x'-x:x,x'\in X,\ x<x'\}.
\]

#### Proposition 4.1: fully reflected characterization

The set \(C=X\cup(S-X)\) has no repeated sum other than \(S\) if and only if

1. \(X\) is a genuine Sidon set; and
2.
   \[
   \boxed{
   D(X)\cap\bigl(S-\Sigma(X)\bigr)=\varnothing.
   }
   \]

Equivalently,
\[
\boxed{
\Sigma(X)\cap\bigl(S-D(X)\bigr)=\varnothing.
}
\]

#### Proof

The low-low sums are precisely \(\Sigma(X)\), and all are less than \(S\). The high-high sums are
\[
2S-\Sigma(X),
\]
and all are greater than \(S\). Thus low-low and high-high sums are individually unique exactly when \(X\) is Sidon.

A cross pair \(x\in X\), \(S-y\in S-X\) has sum
\[
S+x-y.
\]
When \(x=y\), this is \(S\), giving the \(p\) allowed representations. When \(x\ne y\), uniqueness of positive differences in a genuine Sidon set implies that the cross sums are individually unique.

The cross sums below \(S\) are exactly
\[
S-D(X).
\]
Thus the only possible collision below \(S\) between different sum types is a collision between \(\Sigma(X)\) and \(S-D(X)\). By reflection, the corresponding condition above \(S\) is identical. This proves the characterization. ∎

The positive difference labels of \(C\) are correspondingly
\[
D(X)\ \sqcup\ \bigl(S-\Sigma(X)\bigr).
\]
Since
\[
|D(X)|=\binom p2,\qquad
|\Sigma(X)|=\binom{p+1}{2},
\]
the core occupies exactly
\[
p^2
\]
distinct positive-difference values. Pure cardinality therefore gives only
\[
S\ge p^2.
\]

The Sidon bound for \(X\subseteq[0,w]\) gives
\[
w\ge p^2-o(p^2),
\]
and \(S>2w\), so one obtains only
\[
S\ge (2-o(1))p^2.
\]
This recovers at best
\[
|C|=2p\le(\sqrt2+o(1))\sqrt S,
\]
not the desired \(2/\sqrt3\).

On the other hand, for any Sidon \(X\subseteq[0,w]\), choosing
\[
S=3w+1
\]
makes the disjointness automatic:
\[
\max\Sigma(X)=2w
<
S-w
\le \min(S-D(X)).
\]
This is precisely the three-span mechanism behind the Erdős–Freud construction.

Thus the sharp missing statement in the fully reflected case is:

> **Unproved symmetric packing statement.**  
> If \(p\to\infty\), \(X\subseteq[0,w]\) is Sidon, \(2w<S\), and
> \[
> D(X)\cap(S-\Sigma(X))=\varnothing,
> \]
> then
> \[
> S\ge(3-o(1))p^2.
> \]

This statement is already strong enough to settle the fully reflected case and is not obtained from the standard Sidon bound.

---

### 5. A finite overlap inequality

The disjointness condition does give a more localized necessary inequality.

Set
\[
h=3w-S.
\]
When \(h\ge0\), define the reflected seed
\[
Z=w-X
\]
and let
\[
P_Z(h)=
\left|\{z+z':z,z'\in Z,\ z\le z',\ z+z'\le h\}\right|.
\]
Because \(Z\) is Sidon, this is also the number of corresponding unordered pair instances.

#### Proposition 5.1

Under the hypotheses of Proposition 4.1,
\[
\boxed{
\binom p2+P_Z(h)\le w.
}
\]

#### Proof

The set \(D(X)\) consists of \(\binom p2\) distinct integers in \([1,w]\).

A sum \(\sigma\in\Sigma(X)\) can have \(S-\sigma\in[1,w]\) only when
\[
\sigma\ge S-w.
\]
Write \(\sigma=2w-(z+z')\), where \(z,z'\in Z\). Then
\[
\sigma\ge S-w
\iff
2w-(z+z')\ge S-w
\iff
z+z'\le3w-S=h.
\]
Therefore the values \(S-\sigma\) lying in \([1,w]\) are counted by \(P_Z(h)\). They are distinct and, by Proposition 4.1, disjoint from \(D(X)\). Since \([1,w]\) has only \(w\) integer positions,
\[
\binom p2+P_Z(h)\le w.
\]
∎

For example, if
\[
q=|Z\cap[0,h/2]|,
\]
then all unordered sums of those \(q\) elements are at most \(h\), so
\[
P_Z(h)\ge\binom{q+1}{2}.
\]
Hence
\[
w\ge\binom p2+\binom{q+1}{2}.
\]
A local Sidon bound also gives
\[
q\ge
p-\sqrt{w-h/2}-O(w^{1/4}).
\]
These inequalities are rigorous but do not force the required factor \(3\).

---

### 6. A failed stronger span lemma

It is false that admissibility forces \(S\ge3w\).

Take
\[
X=\{0,2,5\},\qquad w=5,\qquad S=11.
\]
Then
\[
\Sigma(X)=\{0,2,4,5,7,10\},
\]
and
\[
D(X)=\{2,3,5\}.
\]
Moreover,
\[
S-D(X)=\{9,8,6\},
\]
which is disjoint from \(\Sigma(X)\). Therefore
\[
C=X\cup(S-X)=\{0,2,5,6,9,11\}
\]
has \(S=11<3w=15\) and is admissible with exceptional sum \(11\).

After shifting into the positive integers,
\[
A=\{1,3,6,7,10,12\}\subseteq[12]
\]
has exceptional sum \(13\), represented by
\[
1+12=3+10=6+7,
\]
and no other repeated sum.

Thus any successful asymptotic argument must use the size \(p\) and the near-optimal geometry of large Sidon seeds; it cannot prove a pointwise inequality \(S\ge3w\).

---

### 7. Ledger

**Proved**

1. Uniform upper bound
   \[
   F(N)\le\sqrt{2N}+O(N^{1/4}).
   \]
2. Every duplicated difference is generated entirely inside the exceptional core and has multiplicity exactly two.
3. Exact difference-label count
   \[
   \frac{\binom{2p+\delta}{2}+p}{2}
   +(2p+\delta)u+\binom u2\le N-1.
   \]
4. Existence of a genuine Sidon subset of size \(u+p+1\).
5. Exact fully reflected characterization
   \[
   D(X)\cap(S-\Sigma(X))=\varnothing.
   \]
6. Local overlap inequality
   \[
   \binom p2+P_Z(3w-S)\le w.
   \]

**Plausible but unproved**

1. The symmetric packing statement
   \[
   S\ge(3-o(1))p^2.
   \]
2. A mixed core–unpaired packing inequality strong enough to imply
   \[
   N\ge\frac34(2p+u)^2-o(N).
   \]

**Dead ends**

1. The assertion \(S\ge3w\) is false, as shown by \(X=\{0,2,5\}\), \(S=11\).
2. Counting distinct difference labels gives only
   \[
   N\ge p^2+2pu+\frac12u^2-O(p+u),
   \]
   far below the required coefficients.
3. Sidon extraction alone gives only \(p+u\le(1+o(1))\sqrt N\), which permits a large unpaired part.
4. Splitting at \(s/2\) yields the constant \(\sqrt2\), but no iteration of that argument directly sees the three-span structure needed for \(2/\sqrt3\).

## Self-Audit

1. **Fatal missing step: the symmetric packing statement is unproved.**  
   The reduction to \(D(X)\cap(S-\Sigma(X))=\varnothing\) is exact, but none of the established inequalities upgrades the factor \(2\) in \(S\ge(2-o(1))p^2\) to \(3\). I do not claim otherwise; this is why the route is marked BLOCKED.

2. **The \(\sqrt2\)-bound relies on the classical sharp Sidon estimate.**  
   This is an external theorem rather than reproved here. It is explicitly included in the problem brief, and it applies because both sides of \(s/2\) are genuine Sidon sets, including their diagonal sums.

3. **The fully reflected characterization omits the midpoint.**  
   A midpoint can be deleted without creating any collision, leaving the \(p\) noncentral complementary pairs to which the characterization applies. All midpoint terms are only \(O(1)\), but a future sharp finite theorem would have to restore them explicitly.

## Computations To Verify

The following code exhaustively checks the structural lemmas for small \(N\), computes exact small values of \(F(N)\), and searches the fully reflected seed problem.

```python
from itertools import combinations

def pair_sum_counts(A):
    A = sorted(A)
    c = {}
    for i, a in enumerate(A):
        for b in A[i:]:
            c[a + b] = c.get(a + b, 0) + 1
    return c

def is_admissible(A):
    c = pair_sum_counts(A)
    E = [s for s, v in c.items() if v >= 2]
    return len(E) <= 1

def is_sidon(A):
    c = pair_sum_counts(A)
    return all(v <= 1 for v in c.values())

def difference_counts(A):
    A = sorted(A)
    c = {}
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            d = A[j] - A[i]
            c[d] = c.get(d, 0) + 1
    return c

def exhaustive_check(Nmax=16):
    F = [0] * (Nmax + 1)

    for N in range(1, Nmax + 1):
        for mask in range(1 << N):
            A = {i + 1 for i in range(N) if (mask >> i) & 1}
            sums = pair_sum_counts(A)
            E = [s for s, v in sums.items() if v >= 2]

            if len(E) > 1:
                continue

            F[N] = max(F[N], len(A))

            if not E:
                assert is_sidon(A)
                continue

            s = E[0]
            delta = int(s % 2 == 0 and s // 2 in A)
            C = {a for a in A if s - a in A}
            U = A - C

            p = sum(1 for a in C if 2 * a < s)
            assert sums[s] == p + delta
            assert len(C) == 2 * p + delta

            dc = difference_counts(A)
            assert max(dc.values(), default=0) <= 2

            u = len(U)
            expected = (
                ((2 * p + delta) * (2 * p + delta - 1) // 2 + p) // 2
                + (2 * p + delta) * u
                + u * (u - 1) // 2
            )
            assert len(dc) == expected
            assert expected <= N - 1

            # Both sides of s/2 are genuine Sidon.
            lower = {a for a in A if 2 * a < s}
            upper = {a for a in A if 2 * a > s}
            assert is_sidon(lower)
            assert is_sidon(upper)

            # Verify the normalized core obstruction.
            if p > 0:
                lows = sorted(a for a in C if 2 * a < s)
                x0 = lows[0]
                X = {a - x0 for a in lows}
                S = s - 2 * x0
                w = max(X)

                assert 2 * w < S
                assert is_sidon(X)

                Sigma = {
                    x + y
                    for x in X
                    for y in X
                    if x <= y
                }
                D = {
                    y - x
                    for x in X
                    for y in X
                    if x < y
                }
                assert Sigma.isdisjoint({S - d for d in D})
                assert D.isdisjoint({S - z for z in Sigma})

    return F

print(exhaustive_check(16))
```

Search for the minimum reflected span \(S\) for each Sidon seed:

```python
from itertools import combinations

def unordered_sum_set(X):
    X = sorted(X)
    return {
        X[i] + X[j]
        for i in range(len(X))
        for j in range(i, len(X))
    }

def positive_difference_set(X):
    X = sorted(X)
    return {
        X[j] - X[i]
        for i in range(len(X))
        for j in range(i + 1, len(X))
    }

def minimum_S_for_seed(X):
    X = set(X)
    assert min(X) == 0
    w = max(X)
    assert is_sidon(X)

    Sigma = unordered_sum_set(X)
    D = positive_difference_set(X)

    # S = 3w+1 always works.
    for S in range(2 * w + 1, 3 * w + 2):
        if Sigma.isdisjoint({S - d for d in D}):
            return S
    raise AssertionError("3w+1 should always work")

def search_reflected_seeds(Wmax=30):
    best_by_p = {}

    for w in range(1, Wmax + 1):
        for p in range(2, w + 2):
            for middle in combinations(range(1, w), p - 2):
                X = (0,) + middle + (w,)
                if not is_sidon(X):
                    continue

                S = minimum_S_for_seed(X)
                record = (S / (p * p), S / w, S, w, X)

                if p not in best_by_p or record < best_by_p[p]:
                    best_by_p[p] = record

                # Directly verify the reflected construction.
                C = set(X) | {S - x for x in X}
                A = {c + 1 for c in C}  # shift to positive integers
                assert is_admissible(A)

    return best_by_p

for p, rec in sorted(search_reflected_seeds(30).items()):
    print("p =", p,
          "S/p^2 =", rec[0],
          "S/w =", rec[1],
          "S =", rec[2],
          "w =", rec[3],
          "X =", rec[4])
```

The most important experimental questions are:

1. Does the minimum \(S/p^2\) trend toward \(3\), or can it stay below \(3-\varepsilon\)?
2. For exact maximizers of \(F(N)\), does \(u/|A|\) tend to zero?
3. Are there large seeds for which \(S<3w\) by a positive proportion while \(w=(1+o(1))p^2\)?
4. Can a small seed such as \(\{0,2,5\}\) be amplified by a product or finite-field construction without introducing new repeated sums?

## Route Diagnosis

Route 1 successfully isolates the exceptional matching and shows exactly where the missing factor must come from. In the fully reflected case, the problem becomes a sharp packing question for the two structured sets
\[
D(X)\quad\text{and}\quad S-\Sigma(X).
\]
Their cardinalities total \(p^2\), but their spatial interaction must somehow force an ambient span near \(3p^2\). Neither ordinary Sidon bounds nor unweighted difference counting capture that interaction. Moreover, \(S\ge3w\) is false, so the needed theorem must be asymptotic and sensitive to the distribution of near-extremal Sidon sets.

The general case has an additional obstruction: unpaired elements contribute completely new difference labels, but the exact label count is far too weak. A fresh attempt should combine Route 1 with Route 2, seeking a weighted, location-sensitive inequality for
\[
D(X)\sqcup(S-\Sigma(X))
\]
and then showing that differences involving \(U\) must occupy the remaining weighted capacity. On the disproof side, the highest-priority search is for a scalable family of Sidon seeds satisfying the disjointness condition with \(S\le(3-\varepsilon)|X|^2\); isolated finite examples do not suffice.