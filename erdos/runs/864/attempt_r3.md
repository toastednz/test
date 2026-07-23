STATUS: BLOCKED

## Result

Route 3 yields exact Fourier identities but does not presently recover the conjectured constant. I prove the nontrivial global bound
\[
F(N)\le S(N)+S(\lfloor N/2\rfloor)
=\left(1+\frac1{\sqrt2}\right)\sqrt N+O(N^{1/4}),
\]
improving the elementary constant \(2\). I also derive the exact fourth moment in terms of the exceptional core and reduce the completely reflected, center-free case to a sharply localized polynomial-coefficient problem: for a Sidon set \(X\subseteq[0,D]\) and \(\sigma>2D\), the reflected set \(X\cup(\sigma-X)\) is admissible exactly when
\[
[z^\sigma]\,D_X(z)H_X(z)=0,
\]
where \(D_X\) and \(H_X\) encode positive differences and unordered sums of \(X\). Equivalently, \(\sigma\notin 3X-X\). The desired constant in this special case requires proving that such a missing coefficient forces
\[
\sigma\ge(3-o(1))|X|^2.
\]
Fourier inversion represents this coefficient, but the integrand is not nonnegative, and standard fourth-moment or positive-kernel estimates control only averages of nearby coefficients. This is the precise block.

## Complete Argument

### 1. Ordered convolution and the exact fourth moment

Let \(A\subseteq[N]\) be admissible, with \(k=|A|\). If there is no exceptional sum, then \(A\) is a genuine Sidon set and \(k\le S(N)\), so suppose there is an exceptional sum \(s\).

Write
\[
t=r_A(s),\qquad
\delta=
\begin{cases}
1,&s\text{ even and }s/2\in A,\\
0,&\text{otherwise}.
\end{cases}
\]
Let
\[
C=A\cap(s-A).
\]
The \(t-\delta\) off-diagonal representations of \(s\) contribute two elements each, while the possible diagonal contributes one, so
\[
c:=|C|=2t-\delta.
\]

Define
\[
P(z)=\sum_{a\in A}z^a,
\qquad
R(n)=[z^n]P(z)^2.
\]
Thus \(R(n)\) is the ordered representation count. In particular,
\[
R(s)=c.
\]

For \(n\ne s\), admissibility implies that either:

* \(n\) has no representation, so \(R(n)=0\);
* \(n=2a\) has only its diagonal representation, so \(R(n)=1\);
* \(n=a+b\) with \(a<b\), so \(R(n)=2\).

A diagonal and an off-diagonal representation cannot coexist when \(n\ne s\), because that would give two unordered representations.

There are \(k-\delta\) diagonal ordered representations outside \(s\). If \(o\) denotes the number of nonexceptional off-diagonal unordered representations, then
\[
k^2-c=2o+(k-\delta).
\]
Consequently,
\[
\begin{aligned}
\sum_n R(n)^2
&=c^2+4o+(k-\delta)\\
&=c^2+2(k^2-c)-(k-\delta)\\
&=2k^2-k+c^2-2c+\delta.
\end{aligned}
\]
Parseval therefore gives the exact identity
\[
\boxed{
\int_0^1 |P(e^{2\pi i\theta})|^4\,d\theta
=
2k^2-k+c^2-2c+\delta.
}
\tag{1}
\]

More generally, for any real weights \(w_n\),
\[
\boxed{
\sum_n w_nR(n)^2
=
2\sum_n w_nR(n)
-\sum_{\substack{a\in A\\2a\ne s}}w_{2a}
+(c^2-2c)w_s.
}
\tag{2}
\]
Indeed, outside \(s\), an off-diagonal coefficient satisfies \(R^2=2R\), while a diagonal coefficient satisfies \(R^2=2R-1\); at \(s\), the required correction is \(c^2-2c\).

Identity (2) is the exact weighted fourth-moment information supplied by admissibility. In particular, a weight satisfying \(w_s=0\) removes the exceptional spike completely, but one still needs a sufficiently strong lower bound for the left side that uses the spatial position of the convolution coefficients.

---

### 2. Difference multiplicities and the exact number of doubled differences

For \(1\le d<N\), write
\[
m_A(d)=|\{x:x,x+d\in A\}|.
\]

First, \(m_A(d)\le2\). If \(x<y\) are two distinct bases for the same difference \(d\), then
\[
(x+d)+y=(y+d)+x.
\]
These are distinct unordered representations, so their common sum must be \(s\). If there were a third base \(z\), applying the same argument to \(x,z\) would give
\[
x+y+d=s=x+z+d,
\]
hence \(y=z\), a contradiction.

Let
\[
h=|\{d:m_A(d)=2\}|.
\]
Since
\[
\sum_{d=1}^{N-1}m_A(d)=\binom{k}{2},
\]
we have
\[
\sum_{d=1}^{N-1}m_A(d)^2
=\binom{k}{2}+2h.
\]
Parseval applied to \(P(z)P(z^{-1})\) gives
\[
\sum_n R(n)^2
=k^2+2\sum_{d=1}^{N-1}m_A(d)^2
=2k^2-k+4h.
\]
Comparing with (1),
\[
4h=c^2-2c+\delta.
\]
Thus
\[
\boxed{
h=
\begin{cases}
q(q-1),&c=2q,\\
q^2,&c=2q+1.
\end{cases}
}
\tag{3}
\]
Equivalently,
\[
h=\left\lfloor\frac{(c-1)^2}{4}\right\rfloor.
\]

Hence the exceptional core determines exactly, not merely approximately, the number of doubled positive differences.

---

### 3. The unordered generating polynomial

Define
\[
H_A(z)=\frac{P(z)^2+P(z^2)}2.
\]
The coefficient of \(z^n\) in \(H_A\) is exactly \(r_A(n)\).

If \(s\) is exceptional, set
\[
Q_A(z)=H_A(z)-(t-1)z^s.
\]
Every coefficient of \(Q_A\) is either \(0\) or \(1\), and
\[
Q_A(1)=\binom{k+1}{2}-t+1.
\]
Therefore
\[
\int_0^1|Q_A(e^{2\pi i\theta})|^2\,d\theta
=
Q_A(1)
=
\binom{k+1}{2}-t+1.
\tag{4}
\]

Since \(Q_A\) is supported on \(2,\dots,2N\), (4) immediately gives
\[
\binom{k+1}{2}-t+1\le2N-1.
\]
Using \(t\le\lceil k/2\rceil\) recovers only
\[
k\le2\sqrt N+O(1).
\]
Thus merely collapsing the spike and applying Parseval is exactly equivalent to the elementary pair-sum count.

Similarly, Cauchy–Schwarz and (1) give
\[
\frac{k^4}{2N-1}
\le \sum_nR(n)^2
\le 3k^2+O(k),
\]
which is weaker still. Hence an unweighted fourth moment cannot provide the conjectured constant.

---

### 4. A global upper bound from the core geometry

I now prove
\[
\boxed{F(N)\le S(N)+S(\lfloor N/2\rfloor).}
\tag{5}
\]

As before, let \(p=t-\delta\) be the number of off-diagonal representations of \(s\), and put
\[
u=|A\setminus C|.
\]
Then
\[
k=u+2p+\delta.
\]

Choose from each off-diagonal representation \(x+(s-x)=s\) its smaller endpoint. The set \(X\) of these smaller endpoints has size \(p\) and is contained in
\[
I_s=
\left[
\max(1,s-N),\,
\left\lfloor\frac{s-1}{2}\right\rfloor
\right].
\tag{6}
\]

The interval \(I_s\) has at most \(\lfloor N/2\rfloor\) elements. Indeed:

* If \(s\le N+1\), its size is
  \[
  \left\lfloor\frac{s-1}{2}\right\rfloor
  \le\left\lfloor\frac N2\right\rfloor.
  \]
* If \(s\ge N+1\), its size is
  \[
  \left\lfloor\frac{s-1}{2}\right\rfloor-(s-N)+1,
  \]
  which is maximal at \(s=N+1\) and is then \(\lfloor N/2\rfloor\).

Moreover, \(X\) is a genuine Sidon set. Every sum of two elements of \(X\) is strictly smaller than \(s\). Hence two distinct unordered representations inside \(X\) would give a repeated sum different from \(s\), contradicting admissibility. Translation preserves the Sidon property, so
\[
p\le S(\lfloor N/2\rfloor).
\tag{7}
\]

Next construct a genuine Sidon subset \(B\subseteq A\).

* If \(\delta=0\), retain both endpoints of one exceptional pair and one endpoint from each of the other \(p-1\) exceptional pairs, as well as all \(u\) unpaired elements. Then
  \[
  |B|=u+p+1.
  \]
  Exactly one representation of \(s\) remains.
* If \(\delta=1\), retain the central point \(s/2\), one endpoint from each of the \(p\) off-diagonal pairs, and all \(u\) unpaired elements. Again
  \[
  |B|=u+p+1,
  \]
  and the only remaining representation of \(s\) is the diagonal one.

All other sums were already unique in \(A\). Thus \(B\) is genuine Sidon and
\[
u+p+1\le S(N).
\tag{8}
\]

If \(\delta=0\), then
\[
k=u+2p=(u+p+1)+p-1
\le S(N)+S(\lfloor N/2\rfloor)-1.
\]
If \(\delta=1\), then
\[
k=u+2p+1=(u+p+1)+p
\le S(N)+S(\lfloor N/2\rfloor).
\]
This proves (5). The no-exception case is immediate from \(k\le S(N)\).

Using the classical bound
\[
S(M)\le\sqrt M+O(M^{1/4}),
\]
we obtain
\[
\boxed{
F(N)\le
\left(1+\frac1{\sqrt2}\right)\sqrt N+O(N^{1/4}).
}
\tag{9}
\]
This remains larger than \(2/\sqrt3\), so it does not solve the problem.

---

### 5. Exact polynomial reduction for a completely reflected core

The Fourier obstruction can already be isolated in the case where every element belongs to the exceptional core and there is no central point.

Let
\[
X\subseteq\{0,1,\dots,D\},
\qquad \sigma>2D,
\]
and define
\[
C=X\cup(\sigma-X).
\]
The two parts are disjoint. Define
\[
D_X(z)=\sum_{\substack{x,y\in X\\x<y}}z^{y-x},
\qquad
H_X(z)=\sum_{\substack{x,y\in X\\x\le y}}z^{x+y}.
\]

#### Proposition

The set \(C\) is admissible with all repeated sums equal to \(\sigma\) if and only if:

1. \(X\) is a genuine Sidon set;
2. \([z^\sigma]D_X(z)H_X(z)=0\).

Equivalently,
\[
\sigma\notin 3X-X.
\tag{10}
\]

#### Proof: necessity

If \(X\) were not Sidon, two distinct unordered pairs from \(X\) would have a common sum. That sum is at most \(2D<\sigma\), contradicting admissibility of \(C\).

Suppose now that
\[
\sigma=a+b+c-d
\]
for some \(a,b,c,d\in X\). Since \(a+b\le2D<\sigma\),
\[
c-d=\sigma-(a+b)>0,
\]
so \(c>d\). Let
\[
e=c-d=\sigma-a-b.
\]
The difference \(e\) occurs in the two reflected intervals
\[
[d,c],
\qquad
[\sigma-c,\sigma-d].
\]
It also occurs as a cross difference:

* if \(a=b\), in \([a,\sigma-a]\);
* if \(a\ne b\), in both \([a,\sigma-b]\) and \([b,\sigma-a]\).

The cross interval is distinct from either within-side interval because it has one endpoint in \(X\) and one in \(\sigma-X\). Thus \(m_C(e)\ge3\), impossible for an admissible set. Hence \(\sigma\notin3X-X\).

The coefficient of \(z^\sigma\) in \(D_XH_X\) counts precisely equations
\[
\sigma=(c-d)+(a+b)
\]
with \(c>d\). Because \(\sigma>2D\), every equation \(\sigma=a+b+c-d\) automatically has \(c>d\). Thus (10) is equivalent to the asserted coefficient vanishing.

#### Proof: sufficiency

Assume \(X\) is Sidon and \(\sigma\notin3X-X\).

The positive differences inside \(C\) have two types.

1. Differences within \(X\), together with their reflected copies within \(\sigma-X\):
   \[
   y-x,\qquad x<y.
   \]
   Since \(X\) is Sidon, its positive differences are distinct. Each such value occurs exactly twice in the two reflected intervals.

2. Cross differences:
   \[
   (\sigma-y)-x=\sigma-(x+y).
   \]
   Since \(X\) is Sidon, its unordered sums \(x+y\) are distinct. If \(x\ne y\), the cross difference occurs in the two reflected intervals
   \[
   [x,\sigma-y],
   \qquad
   [y,\sigma-x].
   \]
   If \(x=y\), it occurs once.

The two types cannot overlap. An equality
\[
y-x=\sigma-(a+b)
\]
would give
\[
\sigma=a+b+y-x\in3X-X,
\]
contrary to assumption. Therefore every positive difference in \(C\) has multiplicity at most two, and whenever it has multiplicity two, its two intervals are reflections of one another under \(v\mapsto\sigma-v\).

Suppose two distinct unordered pairs satisfy
\[
u+v=w+x.
\]
Write \(u\le v\), \(w\le x\). The smaller endpoints cannot agree, so after exchanging the pairs assume \(u<w\). Then
\[
v-x=w-u>0.
\]
Thus \([u,w]\) and \([x,v]\) are two distinct intervals with the same positive difference. They must be reflections:
\[
x=\sigma-w,\qquad v=\sigma-u.
\]
It follows that
\[
u+v=\sigma.
\]
Thus every repeated sum is \(\sigma\), proving admissibility. ∎

Fourier inversion now writes the obstruction as
\[
[z^\sigma]D_XH_X
=
\int_0^1
D_X(e^{2\pi i\theta})
H_X(e^{2\pi i\theta})
e^{-2\pi i\sigma\theta}\,d\theta.
\tag{11}
\]
The product in (11) is not pointwise nonnegative, despite both polynomials having nonnegative coefficients.

---

### 6. The precise localized statement that remains unproved

Let \(p=|X|\). The classical Sidon bound only gives
\[
D\ge(1-o(1))p^2.
\]
Together with \(\sigma>2D\), this yields only
\[
\sigma\ge(2-o(1))p^2.
\]
For the reflected set \(C\), whose size is \(2p\) and whose ambient interval has length approximately \(\sigma\), the conjectured bound instead requires
\[
\sigma\ge(3-o(1))p^2.
\]

Thus Route 3 already encounters the following special-case problem:

> **Localized coefficient problem.** Prove that if \(X\subseteq[0,D]\) is genuine Sidon, \(|X|=p\), \(\sigma>2D\), and
> \[
> [z^\sigma]D_X(z)H_X(z)=0,
> \]
> then
> \[
> \sigma\ge(3-o(1))p^2.
> \]

Equivalently, one must prove that for every near-extremal Sidon set \(X\), every integer
\[
2D<\sigma<(3-o(1))p^2
\]
belongs to \(3X-X\).

The value at the principal Fourier frequency is large:
\[
D_X(1)H_X(1)
=
\binom p2\binom{p+1}2
\asymp p^4.
\]
This can make suitable averages of nearby convolution coefficients large. It does not force the specified coefficient at \(\sigma\) to be positive, because the nonprincipal frequencies in (11) can cancel the principal contribution. Establishing pointwise coverage of the relevant interval is substantially stronger than an additive-energy or averaged supersaturation statement.

Since this obstruction occurs in the completely reflected special case, and the full problem must additionally handle unpaired elements, Route 3 is blocked at a statement of comparable sharpness to the original problem.

## Self-Audit

1. **The most delicate proved step is the converse in the reflected-core proposition.**  
   Equal sums are converted into two equal positive differences, including cases involving diagonal representations. The ordering \(u<w\) gives the two intervals \([u,w]\) and \([x,v]\); if the doubled difference is reflected, their endpoints force the common sum to be \(\sigma\). This explicitly includes shared-endpoint and diagonal cases.

2. **The global bound uses that the lower endpoints occupy at most \(\lfloor N/2\rfloor\) consecutive positions.**  
   This is sensitive to \(s>N+1\), where the lower endpoint must also satisfy \(x\ge s-N\). Formula (6) includes that boundary, and the interval-size calculation treats both sides of \(N+1\).

3. **The asymptotic form of (9) invokes the classical genuine-Sidon estimate rather than reproving it.**  
   The exact inequality (5) is proved independently. The supplied problem brief explicitly includes
   \[
   S(M)\le\sqrt M+O(M^{1/4}),
   \]
   with the same diagonal convention, so its application here is legitimate.

No proof is claimed for the localized coefficient problem. In particular, positivity of an average of coefficients would not justify positivity of the individual coefficient at \(\sigma\).

## Computations To Verify

```python
from itertools import combinations
from collections import Counter
from math import floor

def representations(A):
    """Unordered representation counts."""
    A = sorted(A)
    r = Counter()
    for i, a in enumerate(A):
        for b in A[i:]:
            r[a + b] += 1
    return r

def admissible(A):
    r = representations(A)
    exceptional = [n for n, v in r.items() if v >= 2]
    return len(exceptional) <= 1

def invariants(A):
    """
    Verify:
      - exact fourth-moment formula;
      - m_A(d) <= 2;
      - exact number of doubled differences.
    """
    A = sorted(A)
    k = len(A)
    r = representations(A)
    exceptional = [n for n, v in r.items() if v >= 2]

    if not exceptional:
        s = None
        t = 0
        delta = 0
        core = set()
    else:
        assert len(exceptional) == 1
        s = exceptional[0]
        t = r[s]
        delta = int(s % 2 == 0 and s // 2 in A)
        core = {a for a in A if s - a in A}

    # Ordered convolution.
    R = Counter()
    for a in A:
        for b in A:
            R[a + b] += 1
    energy = sum(v * v for v in R.values())

    # Positive differences.
    m = Counter()
    for i, a in enumerate(A):
        for b in A[i+1:]:
            m[b - a] += 1

    if s is not None:
        c = len(core)
        predicted_energy = 2*k*k - k + c*c - 2*c + delta
        predicted_h = (c*c - 2*c + delta) // 4
        actual_h = sum(v == 2 for v in m.values())

        assert c == 2*t - delta
        assert energy == predicted_energy
        assert actual_h == predicted_h

    assert max(m.values(), default=0) <= 2

    return {
        "k": k,
        "exceptional": s,
        "t": t,
        "delta": delta,
        "core": sorted(core),
        "ordered_energy": energy,
        "differences": dict(m),
    }

def is_genuine_sidon(X):
    sums = set()
    X = sorted(X)
    for i, a in enumerate(X):
        for b in X[i:]:
            if a + b in sums:
                return False
            sums.add(a + b)
    return True

def pure_core_data(X):
    """
    For normalized X containing 0, find the least sigma > 2D
    with sigma not in 3X-X, construct C=X union (sigma-X),
    and verify admissibility after shifting into positive integers.
    """
    X = tuple(sorted(X))
    assert X[0] == 0
    assert is_genuine_sidon(X)

    D = X[-1]
    positive_differences = {
        X[j] - X[i]
        for i in range(len(X))
        for j in range(i+1, len(X))
    }
    unordered_sums = {
        X[i] + X[j]
        for i in range(len(X))
        for j in range(i, len(X))
    }

    # Exponents appearing in D_X(z) H_X(z).
    forbidden_sigma = {
        d + q
        for d in positive_differences
        for q in unordered_sums
    }

    sigma = 2*D + 1
    while sigma in forbidden_sigma:
        sigma += 1

    C0 = set(X) | {sigma - x for x in X}
    C = {x + 1 for x in C0}  # Now C subset [sigma+1].
    assert admissible(C)

    r = representations(C)
    repeated = [n for n, v in r.items() if v >= 2]
    if len(X) >= 2:
        assert repeated == [sigma + 2]

    return {
        "X": X,
        "p": len(X),
        "D": D,
        "sigma": sigma,
        "sigma_over_p2": sigma / (len(X)**2),
        "N": sigma + 1,
        "C": sorted(C),
    }

def search_pure_cores(p, Dmax):
    """
    Enumerate normalized Sidon rulers X with |X|=p, min X=0,
    max X <= Dmax. Return the least sigma found.
    Intended for small p (roughly p <= 7 or 8).
    """
    best = None

    if p == 1:
        return pure_core_data((0,))

    for D in range(p - 1, Dmax + 1):
        if p == 2:
            candidates = [(0, D)]
        else:
            candidates = [
                (0,) + middle + (D,)
                for middle in combinations(range(1, D), p - 2)
            ]

        for X in candidates:
            if not is_genuine_sidon(X):
                continue
            data = pure_core_data(X)
            if best is None or data["sigma"] < best["sigma"]:
                best = data

    return best

def exact_F(N):
    """
    Exact depth-first search for modest N.
    Builds subsets in increasing order and maintains unordered sum counts.
    """
    best = []
    counts = Counter()

    def dfs(next_x, A):
        nonlocal best

        if len(A) + (N - next_x + 1) <= len(best):
            return

        if next_x == N + 1:
            if len(A) > len(best):
                best = A[:]
            return

        # Exclude next_x.
        dfs(next_x + 1, A)

        # Include next_x.
        new_sums = [next_x + a for a in A] + [2 * next_x]
        for n in new_sums:
            counts[n] += 1

        repeated = sum(v >= 2 for v in counts.values())
        if repeated <= 1:
            A.append(next_x)
            dfs(next_x + 1, A)
            A.pop()

        for n in new_sums:
            counts[n] -= 1
            if counts[n] == 0:
                del counts[n]

    dfs(1, [])
    assert admissible(best)
    return len(best), best, invariants(best)

# Suggested checks:
#
# 1. Exact extremizers and core statistics:
# for N in range(1, 31):
#     print(N, exact_F(N))
#
# 2. Reduced pure-core obstruction:
# for p in range(2, 8):
#     print(search_pure_cores(p, Dmax=40))
#
# 3. Verify the small examples:
# print(pure_core_data((0, 1)))
# print(pure_core_data((0, 1, 3)))
# print(pure_core_data((0, 1, 4, 6)))
#
# 4. For every exact extremizer, verify the fourth-moment and doubled-
#    difference identities using invariants().
```

The most informative finite experiment is to compute
\[
g(p):=\min_X\min\{\sigma>2\max X:\sigma\notin3X-X\},
\]
where \(X\) ranges over normalized \(p\)-element genuine Sidon sets. The key ratio is \(g(p)/p^2\). Values persistently bounded below \(3-\varepsilon\) for growing \(p\) would undermine the proposed localized theorem and could point toward a disproof construction.

## Route Diagnosis

### Proved ledger

* Exact ordered fourth moment:
  \[
  \int|P|^4=2k^2-k+c^2-2c+\delta.
  \]
* Exact weighted coefficient identity (2).
* Exact number of doubled positive differences:
  \[
  h=\lfloor(c-1)^2/4\rfloor.
  \]
* Exact \(0\)-\(1\) collapsed unordered-sum polynomial \(Q_A\).
* Exact global bound:
  \[
  F(N)\le S(N)+S(\lfloor N/2\rfloor)
  =\left(1+\frac1{\sqrt2}\right)\sqrt N+O(N^{1/4}).
  \]
* In the completely reflected, center-free case,
  \[
  X\cup(\sigma-X)\text{ admissible}
  \iff X\text{ Sidon and }\sigma\notin3X-X.
  \]
* Equivalent polynomial obstruction:
  \[
  [z^\sigma]D_XH_X=0.
  \]

### Plausible but unproved

* The localized covering statement
  \[
  \sigma>2D,\quad \sigma\notin3X-X
  \quad\Longrightarrow\quad
  \sigma\ge(3-o(1))|X|^2
  \]
  for genuine Sidon \(X\subseteq[0,D]\).
* A stability version would likely need quantitative Fourier control of near-extremal Sidon sets strong enough to prove pointwise, rather than average, coverage by \(3X-X\).

### Dead ends

* **Raw fourth moment:** the exceptional coefficient contributes \(c^2\), and the resulting energy estimate is too weak.
* **Collapsed unordered convolution:** Parseval reduces exactly to counting the available sum positions and gives only constant \(2\).
* **Weights annihilating the exceptional coefficient:** identity (2) removes the spike but leaves the need for a new spatial lower bound; standard Cauchy or large-sieve estimates do not supply the missing factor.
* **Positive-kernel averaging:** it can show that many coefficients of \(D_XH_X\) are occupied, but admissibility depends on one prescribed coefficient being zero. Average positivity does not rule out a localized hole.
* **Classical Sidon diameter alone:** it gives \(D\ge(1-o(1))p^2\), and \(\sigma>2D\) then gives only \(\sigma\ge(2-o(1))p^2\), short of the required \(3p^2\).

A fresh Route 3 attempt should target a pointwise Fourier theorem for \(3X-X\) when \(X\) is a near-extremal interval Sidon set, possibly via a strong discrepancy/stability theorem for its difference and sum polynomials. Without such a theorem, the Fourier route is blocked before even addressing the unpaired part \(A\setminus C\).