STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #477. For every integer-valued polynomial of even degree, I proved that after normalization its distinct values form a subset \(C\subseteq\mathbb N_0\) whose consecutive gaps tend to infinity. I also proved a precise “mass escape” theorem showing that any hypothetical tiling by such a \(C\) must cover arbitrarily long intervals using distinct, arbitrarily remote polynomial values and correspondingly nonlocal centers. However, the hoped-for order-theoretic conclusion is false in considerable generality: I construct exact tilings \(\mathbb Z=A\oplus C\) where \(C\subseteq\mathbb N_0\) has gaps tending to infinity, \(A\) is nonperiodic and bounded above, and even where the \(m\)-th element of \(C\) is asymptotic to \(100m^4\). Thus one-sidedness, growing gaps, and polynomial-scale growth do not by themselves force periodicity or impossibility. I also isolate a finite-extension criterion which would give an affirmative polynomial example, but for \(C=f(\mathbb Z)\) it reduces to unresolved uniform avoidance questions for equations \(f(k)+f(u)-f(v)=t\).

## Complete Argument

### 1. Normalization of an even-degree polynomial value set

Let \(f\in\mathbb Q[x]\) be integer-valued and have even degree \(d\ge 2\).

After replacing \(f\) by \(-f\), if necessary, assume its leading coefficient is positive. Then
\[
f(n)\longrightarrow +\infty\qquad (|n|\to\infty).
\]
Consequently \(f\) attains a minimum \(m\in\mathbb Z\) on \(\mathbb Z\). Replacing \(f\) by \(f-m\), we may therefore normalize its value set to
\[
C=f(\mathbb Z)\subseteq\mathbb N_0,\qquad 0\in C.
\]

These operations preserve the tiling question up to reflection and translation of the complementary set.

### 2. Distinct values of an even-degree polynomial have growing gaps

#### Lemma 2.1

For every \(H>0\), there are only finitely many pairs of distinct values \(c,c'\in f(\mathbb Z)\) satisfying
\[
0<|c-c'|\le H.
\]

#### Proof

Suppose otherwise. Then there are integer sequences \(x_r,y_r\) such that
\[
f(x_r)\ne f(y_r),\qquad |f(x_r)-f(y_r)|\le H,
\]
and \(\max(|x_r|,|y_r|)\to\infty\).

Write the leading term as \(\alpha x^d\), where \(\alpha>0\) and \(d\) is even. Since
\[
f(x)=\alpha |x|^d+O(|x|^{d-1}),
\]
boundedness of \(f(x_r)-f(y_r)\) implies
\[
\frac{|x_r|}{|y_r|}\longrightarrow 1.
\]
In particular, both absolute values tend to infinity.

Pass to a subsequence on which the signs of \(x_r,y_r\) are fixed.

If they have the same sign, both lie eventually on the same monotone tail of \(f\). On either tail,
\[
|f'(t)|\asymp |t|^{d-1}.
\]
By the mean value theorem, if \(x_r\ne y_r\),
\[
|f(x_r)-f(y_r)|
  =|x_r-y_r|\,|f'(\xi_r)|
  \gg \min(|x_r|,|y_r|)^{d-1},
\]
which tends to infinity. This contradicts the bound by \(H\).

It remains to consider opposite signs. After interchanging the sequences if necessary, write
\[
x_r=m_r+s_r,\qquad y_r=-m_r,
\]
where \(m_r\to\infty\). The ratio conclusion gives \(s_r=o(m_r)\).

If \(|s_r|\to\infty\), then
\[
\begin{aligned}
f(m_r+s_r)-f(-m_r)
 &=\alpha\bigl((m_r+s_r)^d-m_r^d\bigr)+O(m_r^{d-1})\\
 &=\alpha d m_r^{d-1}s_r
   +O(m_r^{d-2}s_r^2)+O(m_r^{d-1}).
\end{aligned}
\]
Because \(s_r=o(m_r)\), division by \(m_r^{d-1}|s_r|\) shows that the first term dominates. Thus the difference is unbounded, again a contradiction.

Hence \(s_r\) is bounded. Passing to another subsequence, assume \(s_r=s\) is constant. Then the polynomial
\[
P_s(X)=f(X+s)-f(-X)
\]
is bounded at infinitely many positive integers and therefore is constant, say \(P_s(X)=K\).

Equivalently,
\[
f(x)-f(s-x)=K
\]
identically in \(x\). Replacing \(x\) by \(s-x\) gives
\[
f(s-x)-f(x)=K.
\]
Thus \(K=-K\), so \(K=0\). It follows that
\[
f(m_r+s)=f(-m_r)
\]
for every \(r\), contrary to the assumption that the two values are distinct. ∎

#### Corollary 2.2

If the distinct normalized values are enumerated as
\[
0=c_0<c_1<c_2<\cdots,
\]
then
\[
c_{j+1}-c_j\longrightarrow\infty.
\]

Indeed, otherwise some fixed \(H\) would bound infinitely many consecutive gaps, contradicting Lemma 2.1.

This proof applies to all integer-valued \(f\in\mathbb Q[x]\), not merely to polynomials in \(\mathbb Z[x]\).

---

### 3. What a hypothetical one-sided tiling must look like

Let \(C\subseteq\mathbb N_0\) be infinite and suppose
\[
\mathbb Z=A\oplus C.
\]

For each \(n\in\mathbb Z\), write its unique representation as
\[
n=a(n)+c(n),\qquad a(n)\in A,\quad c(n)\in C.
\]

#### Lemma 3.1: Exact finite-window identity

For every finite interval \(I\subseteq\mathbb Z\),
\[
\sum_{c\in C}|A\cap(I-c)|=|I|.
\]

#### Proof

The term \(|A\cap(I-c)|\) counts the integers \(n\in I\) whose representation uses the value \(c\). Every \(n\in I\) has exactly one such value. ∎

In particular, for fixed \(I\), only finitely many \(c\in C\) satisfy
\[
A\cap(I-c)\ne\varnothing.
\]
Thus, as \(c\) runs to infinity through \(C\), the regions \(I-c\) are eventually completely free of \(A\). This is an exact form of escape toward \(-\infty\).

#### Lemma 3.2: Upper Banach density of \(A\)

One has
\[
d^*(A)=0.
\]

#### Proof

Choose distinct \(c_1,\dots,c_m\in C\), and let
\[
R=\max_i c_i-\min_i c_i.
\]
For an interval \(J\) of \(N\) consecutive integers, the sets
\[
(A\cap J)+c_i
\]
are pairwise disjoint, by uniqueness, and all lie in an interval of length at most \(N+R\). Hence
\[
m|A\cap J|\le N+R.
\]
Taking the supremum over \(J\), then the limit superior as \(N\to\infty\), gives
\[
d^*(A)\le \frac1m.
\]
As \(m\) is arbitrary, \(d^*(A)=0\). ∎

Consequently, for every finite \(F\subseteq C\),
\[
U_F:=A+F
\]
also has upper Banach density zero.

#### Lemma 3.3: Forced nonlocal coverage

Assume in addition that the consecutive gaps of \(C\) tend to infinity. For every \(L\ge1\), there is an interval \(I\) of \(L\) consecutive integers such that:

1. every \(n\in I\) is represented using a value outside any prescribed finite initial segment of \(C\);
2. the \(L\) centers \(a(n)\), \(n\in I\), are all distinct.

#### Proof

Choose a finite initial segment \(F\subset C\) such that
\[
|c-c'|>L
\]
whenever \(c,c'\in C\setminus F\) are distinct.

Since \(A+F\) has upper Banach density zero, it cannot meet every interval of length \(L\): otherwise every sufficiently long interval, partitioned into blocks of length \(L\), would have density at least approximately \(1/L\). Thus there is an interval \(I\) of length \(L\) disjoint from \(A+F\).

Therefore \(c(n)\notin F\) for every \(n\in I\).

Suppose distinct \(n,m\in I\) had the same center \(a(n)=a(m)\). Then
\[
n-m=c(n)-c(m).
\]
The left side has absolute value at most \(L-1\), while the right side is either zero or has absolute value greater than \(L\). It cannot be zero because \(n\ne m\). This is impossible. ∎

For a normalized even-degree polynomial, Corollary 2.2 makes Lemma 3.3 applicable. It shows why the apparent recurrence
\[
1_A(n)+\sum_{\substack{c\in C\\c>0}}1_A(n-c)=1
\]
is not well-founded: arbitrarily long intervals may be covered entirely by values and centers escaping to enormous opposite magnitudes.

---

### 4. A finite-extension theorem

The preceding nonlocality is not merely a technical possibility. It can sustain genuine one-sided, aperiodic tilings.

For \(C\subseteq\mathbb Z\), put
\[
D=C-C.
\]
For \(t\in\mathbb Z\), define
\[
E_C(t):=\{c\in C:t-c\in D\}.
\]

#### Theorem 4.1

Let \(C\subseteq\mathbb N_0\) be infinite with \(0\in C\). Suppose
\[
t\notin C\implies E_C(t)\text{ is finite}.
\tag{4.1}
\]
Then there exists \(A\subseteq\mathbb Z\) such that
\[
\mathbb Z=A\oplus C.
\]
Moreover, \(A\) can be chosen with
\[
A\subseteq\mathbb Z_{\le0},\qquad 0\in A.
\]

#### Proof

Begin with
\[
A_0=\{0\}.
\]
Enumerate \(\mathbb Z\), for example as
\[
0,1,-1,2,-2,\dots.
\]

Suppose a finite set \(A_r\subseteq\mathbb Z_{\le0}\) has been constructed so that
\[
(A_r-A_r)\cap D=\{0\}.
\tag{4.2}
\]
Let \(n\) be the next integer in the enumeration.

If \(n\in A_r+C\), set \(A_{r+1}=A_r\).

Otherwise, for every \(a\in A_r\),
\[
t_a:=n-a\notin C.
\]
By (4.1), each \(E_C(t_a)\) is finite. Hence
\[
\bigcup_{a\in A_r}E_C(t_a)
\]
is finite. Since \(C\) is infinite and unbounded, choose \(c\in C\) such that
\[
c>n
\]
and
\[
c\notin E_C(t_a)\qquad\text{for every }a\in A_r.
\]
Set
\[
a_{\mathrm{new}}=n-c<0
\]
and
\[
A_{r+1}=A_r\cup\{a_{\mathrm{new}}\}.
\]

For every \(a\in A_r\),
\[
a_{\mathrm{new}}-a=n-c-a=t_a-c\notin D.
\]
Since \(D=-D\), the reverse difference also does not belong to \(D\). Thus (4.2) remains valid. Also,
\[
n=a_{\mathrm{new}}+c
\]
is now covered.

Let
\[
A=\bigcup_{r\ge0}A_r.
\]
Every integer is eventually processed and hence covered. If
\[
a+c=a'+c'
\]
with \(a,a'\in A\) and \(c,c'\in C\), then
\[
a-a'=c'-c\in D.
\]
Both \(a,a'\) occur together at some finite stage, so (4.2) implies \(a=a'\), and then \(c=c'\). Thus the representation is unique. ∎

A weaker condition sufficient for the same recursive construction is:

\[
\forall\text{ finite }T\subseteq\mathbb Z\setminus C,\quad
C\not\subseteq \bigcup_{t\in T}\bigl(t-(C-C)\bigr).
\tag{4.3}
\]

To force \(A\subseteq\mathbb Z_{\le0}\), the surviving values \(c\) in (4.3) should be arbitrarily large.

---

### 5. A fixed one-sided tile with growing gaps

Let
\[
C_4=\{0,1,4,16,64,\dots\}
    =\{0\}\cup\{4^j:j\ge0\}.
\]

Its consecutive gaps tend to infinity.

#### Lemma 5.1

For every \(t\notin C_4\), the set \(E_{C_4}(t)\) is finite.

#### Proof

Fix \(t\notin C_4\), and let \(c=4^j\) be sufficiently large that
\[
c>2|t|.
\]
Suppose
\[
t-c=u-v,\qquad u,v\in C_4.
\]
Then
\[
v-u=c-t>0,
\]
so \(v>u\). Write \(v=4^s\).

If \(s<j\), then
\[
v-u\le 4^{j-1}=\frac c4,
\]
whereas
\[
c-t\ge c-|t|>\frac c2,
\]
a contradiction.

If \(s=j\), then
\[
c-u=c-t,
\]
so \(u=t\), contrary to \(t\notin C_4\).

If \(s>j\), then the largest element of \(C_4\) below \(v\) is \(v/4\), so
\[
v-u\ge \frac{3v}{4}\ge 3c.
\]
But
\[
c-t\le c+|t|<\frac{3c}{2},
\]
again a contradiction.

Thus no sufficiently large \(4^j\) belongs to \(E_{C_4}(t)\). ∎

Theorem 4.1 now gives:

#### Corollary 5.2

There is an explicitly recursively defined set
\[
A\subseteq\mathbb Z_{\le0}
\]
such that
\[
\mathbb Z=A\oplus C_4.
\]

The set \(A\) is nonperiodic: it contains \(0\) and is bounded above, whereas any nonempty set with a nonzero period is unbounded in both directions.

Therefore the central generic hope of Route 2 is false:

> An infinite set \(C\subseteq\mathbb N_0\) can have gaps tending to infinity and nevertheless tile all of \(\mathbb Z\) uniquely with a bounded-above, nonperiodic complement.

This \(C_4\) is not a polynomial value set, so it does not settle the original problem.

---

### 6. Even polynomial-scale growth does not restore order rigidity

The preceding example is exponentially lacunary. One might hope that a structural theorem survives under the additional condition \(c_{m+1}/c_m\to1\), as holds for polynomial value sets. Even this is false without using the exact algebraic form of the values.

#### Proposition 6.1

There are sets \(B,C\subseteq\mathbb N_0\) such that

\[
\mathbb Z=C-B
\]
uniquely, and, writing their positive elements in increasing order as \(b_m,c_m\),
\[
b_m\sim100m^4,\qquad c_m\sim100m^4.
\]
In particular,
\[
b_{m+1}-b_m\to\infty,\qquad
c_{m+1}-c_m\to\infty,
\]
and
\[
\frac{b_{m+1}}{b_m}\to1,\qquad
\frac{c_{m+1}}{c_m}\to1.
\]

Consequently \(A=-B\) gives
\[
\mathbb Z=A\oplus C
\]
with \(C\) having quartic-scale growth and \(A\) bounded above and nonperiodic.

#### Proof

Start with
\[
B=C=\{0\}.
\]
Maintain the invariant that all differences
\[
c-b,\qquad c\in C,\ b\in B,
\]
are distinct.

Suppose currently \(|B|=|C|=m\). The existing difference set has exactly \(m^2\) elements. Hence some integer
\[
n\in[-m^2,m^2]
\]
is not represented as \(c-b\), since the interval has \(2m^2+1\) elements. Choose an unrepresented \(n\) of least absolute value.

We seek to adjoin
\[
b_*=N,\qquad c_*=N+n.
\]
The new differences are

\[
P_N=\{N+n-b:b\in B\},
\]
\[
Q_N=\{c-N:c\in C\},
\]
and
\[
c_*-b_*=n.
\]

The sets \(P_N\) and \(Q_N\) have no internal repetitions. To preserve uniqueness, it is enough to avoid:

1. \(P_N\) meeting the old \(m^2\) differences: at most \(m^3\) forbidden values of \(N\);
2. \(Q_N\) meeting the old differences: at most \(m^3\) forbidden values;
3. \(P_N\cap Q_N\ne\varnothing\): at most \(m^2\) forbidden values, from equations
   \[
   2N=c+b-n;
   \]
4. \(P_N\) or \(Q_N\) containing \(n\), or \(b_*,c_*\) duplicating old elements: at most \(2m\) additional forbidden values.

Thus fewer than
\[
2m^3+m^2+2m<10m^3+10
\]
integers \(N\) are forbidden.

Choose an allowed integer in
\[
100m^4\le N\le100m^4+10m^3+10.
\]
Adjoin \(b_*,c_*\). The invariant is preserved, and \(n\) is now represented.

Repeat indefinitely. Every fixed integer is eventually represented: if an integer \(z\) remained missing forever, then at every later stage the chosen least-absolute-value missing integer would have absolute value at most \(|z|\). But there are only finitely many such integers, and each chosen one becomes permanently represented.

All differences remain unique because any two pairs occur together at a finite stage where the invariant holds. Hence
\[
\mathbb Z=C-B
\]
uniquely.

At the stage indexed by \(m\),
\[
b_m=N=100m^4+O(m^3),
\]
and, because \(|n|\le m^2\),
\[
c_m=N+n=100m^4+O(m^3).
\]
The prescribed intervals for \(N\) are disjoint and increasingly separated, so these are the increasing enumerations. The asserted gap and ratio conclusions follow. ∎

Thus any successful Route 2 theorem must use much more than one-sidedness, growing gaps, zero density, or polynomial-order counting growth. It must exploit exact polynomial identities or congruence structure.

---

### 7. The polynomial finite-extension block

For a normalized polynomial value set \(C=f(\mathbb Z)\), Theorem 4.1 would give an affirmative answer if one could prove condition (4.1), or even the weaker finite-union condition (4.3).

Membership
\[
c\in E_C(t)
\]
means that there exist polynomial values \(u,v\in C\) satisfying
\[
t-c=u-v,
\]
or equivalently
\[
c+u-v=t.
\]
In parameters, after accounting for the normalization constant, this becomes
\[
f(k)+f(r)-f(s)=t'
\tag{7.1}
\]
for a fixed integer \(t'\).

For example, for \(f(x)=x^4\), the needed avoidance statement concerns
\[
k^4+r^4-s^4=t.
\tag{7.2}
\]
To run the recursive construction, one must show that for every finite collection of forbidden \(t\)'s, there is a fourth power \(k^4\) for which none of the corresponding equations has a solution in \(r,s\).

I do not know how to prove this. Conversely, I also do not know how to use failure of this avoidance property to derive a negative tiling theorem. The required assertion is a uniform integral-point avoidance statement on a family of diagonal surfaces, not a consequence of the elementary gap lemma.

This is the precise block reached by the constructive alternative.

## Self-Audit

1. **The delicate part of Lemma 2.1 is the opposite-tail analysis.**  
   The risk is that lower-degree terms could cancel the leading difference when \(x\) and \(-y\) are close. The proof handles this by first obtaining \(s=o(m)\), then showing that unbounded \(s\) makes the term \(dm^{d-1}s\) dominate all \(O(m^{d-1})\) lower-degree terms. Bounded \(s\) reduces to a polynomial reflection identity, whose constant must be zero.

2. **The recursive complement in Theorem 4.1 adds an entire translate, not merely one target point.**  
   This is exactly where many greedy arguments fail. Here every possible collision with an old translate is equivalent to
   \[
   (n-c)-a\in C-C,
   \]
   and the choice \(c\notin E_C(n-a)\) excludes it globally. Any two final centers coexist at some finite stage, so no collision can appear only “at infinity.”

3. **Proposition 6.1 is not a polynomial construction.**  
   Its asymptotically quartic growth could be mistaken for progress on \(f(x)=x^4\), but the exact algebraic structure is entirely different. The proposition is used only to disprove order-and-growth structural lemmas, not as evidence that a polynomial tile exists.

## Computations To Verify

The following Python verifies the fixed lacunary construction and probes the unresolved quartic extension condition.

```python
from itertools import count

# C4 = {0, 1, 4, 16, ...}

def in_C4(x):
    if x == 0:
        return True
    if x < 0:
        return False
    while x % 4 == 0:
        x //= 4
    return x == 1

def C4_upto(B):
    vals = [0]
    q = 1
    while q <= B:
        vals.append(q)
        q *= 4
    return vals

def in_D4(x):
    """Exact test for x in C4-C4."""
    if x == 0:
        return True

    M = abs(x)

    # If q is the larger of two distinct powers of 4,
    # their difference is at least 3q/4.
    # Hence q <= 4M/3.
    B = (4 * M) // 3 + 4
    vals = C4_upto(B)
    return any(u - v == x for u in vals for v in vals)

def integer_enumeration():
    yield 0
    for r in count(1):
        yield r
        yield -r

def greedy_C4(stages=100):
    A = [0]
    processed = []

    for n in integer_enumeration():
        if len(processed) >= stages:
            break
        processed.append(n)

        if any(in_C4(n - a) for a in A):
            continue

        # Search for c in C4, c > n, avoiding every old translate.
        candidates = [0]
        q = 1
        while True:
            if len(candidates) == 1:
                c = 0
            else:
                c = q
                q *= 4

            if c > n and all(not in_D4((n - a) - c) for a in A):
                A.append(n - c)
                break

            if c == 0:
                candidates.append(1)

        # Exact finite-stage collision check.
        for i in range(len(A)):
            for j in range(i):
                assert not in_D4(A[i] - A[j])

        # Every processed target is now covered.
        for z in processed:
            assert any(in_C4(z - a) for a in A)

    assert max(A) == 0
    return A

A = greedy_C4(100)
print("First centers:", A[:20])
```

A direct implementation of Proposition 6.1:

```python
def least_missing(D):
    r = 0
    while True:
        if r == 0:
            if 0 not in D:
                return 0
        else:
            if r not in D:
                return r
            if -r not in D:
                return -r
        r += 1

def quartic_scale_difference_pair(steps=20):
    B = [0]
    C = [0]
    D = {0}

    for _ in range(steps):
        m = len(B)
        n = least_missing(D)
        assert abs(n) <= m * m

        lo = 100 * m**4
        hi = lo + 10 * m**3 + 10

        chosen = None
        for N in range(lo, hi + 1):
            bnew = N
            cnew = N + n

            P = [cnew - b for b in B]
            Q = [c - bnew for c in C]
            new_diffs = P + Q + [n]

            if len(set(new_diffs)) != len(new_diffs):
                continue
            if set(new_diffs) & D:
                continue
            if bnew in B or cnew in C:
                continue

            chosen = (bnew, cnew, new_diffs)
            break

        assert chosen is not None
        bnew, cnew, new_diffs = chosen
        B.append(bnew)
        C.append(cnew)
        D.update(new_diffs)

        # Recompute all differences and verify uniqueness.
        all_diffs = [c - b for c in C for b in B]
        assert len(all_diffs) == len(set(all_diffs))
        assert set(all_diffs) == D

    return B, C

B, C = quartic_scale_difference_pair(20)
print("B:", B)
print("C:", C)
print("C gaps:", [C[i+1] - C[i] for i in range(len(C)-1)])
```

An exact test for whether an integer is a difference of fourth powers:

```python
def is_fourth_power(x):
    if x < 0:
        return False
    r = int(round(x ** 0.25))
    return any(k >= 0 and k**4 == x for k in range(max(0, r-2), r+3))

def is_fourth_difference(x):
    """Exact test for x = u^4-v^4 with u,v >= 0."""
    if x == 0:
        return True

    M = abs(x)
    vals = [0]
    u = 1

    # If u^4-(u-1)^4 > M, no pair with larger index u or above
    # can have difference of magnitude M.
    while u**4 - (u-1)**4 <= M:
        vals.append(u**4)
        u += 1

    return any(a - b == x for a in vals for b in vals)

def quartic_extension_probe(T, K):
    """
    Search for k <= K such that, for every t in T,
    t-k^4 is not a difference of fourth powers.
    Such k is a valid extension candidate for this finite T.
    """
    assert all(not is_fourth_power(t) for t in T)

    good = []
    bad_by_t = {t: [] for t in T}

    for k in range(K + 1):
        c = k**4
        ok = True
        for t in T:
            if is_fourth_difference(t - c):
                bad_by_t[t].append(k)
                ok = False
        if ok:
            good.append(k)

    return good, bad_by_t

for T in [
    [2],
    [2, 3],
    [2, 3, 5],
    [-1, 2, 3, 5],
]:
    good, bad = quartic_extension_probe(T, 100)
    print("T =", T)
    print("good k up to 100:", good)
    print("bad counts:", {t: len(v) for t, v in bad.items()})
```

These quartic checks can find extension candidates or finite obstructions, but no bounded computation proves condition (4.3).

## Route Diagnosis

**Proved lemmas**

- Every even-degree integer-valued polynomial can be normalized to a value set \(C\subseteq\mathbb N_0\) containing \(0\).
- The gaps between its distinct values tend to infinity.
- A hypothetical complement has exact mass escape: arbitrarily long intervals are covered by distinct centers using polynomial values outside any prescribed finite initial segment.
- The finite-extension criterion, Theorem 4.1, rigorously constructs exact complements when the bad sets \(E_C(t)\) are finite.
- One-sided growing-gap tiles can exist with nonperiodic bounded-above complements.
- Even quartic-scale growth and ratio \(c_{m+1}/c_m\to1\) do not yield an order-theoretic obstruction.

**Dead ends**

- **Forward recurrence:** blocked because \(A\) is unbounded below and the recurrence depends on the entire negative half-line.
- **Formal power series:** no standard well-ordered Laurent product is available, and the explicit \(C_4\) tiling shows that one-sided coefficient identities alone cannot force periodicity.
- **Periodicity from growing gaps:** false, even with \(A\) bounded above.
- **Periodicity from polynomial-order growth:** false for arbitrary sets with \(c_m\asymp m^4\).
- **Local interval counting:** it produces many centers but gives no control on where those centers lie; Lemma 3.3 shows that complete nonlocal escape is forced rather than exceptional.

**Plausible but unproved target**

For some polynomial value set \(C=f(\mathbb Z)\), prove the finite-union avoidance property
\[
\forall\text{ finite }T\subseteq\mathbb Z\setminus C,\qquad
C\not\subseteq\bigcup_{t\in T}\bigl(t-(C-C)\bigr).
\]
This would produce an affirmative solution by the recursive construction. For \(f(x)=x^4\), it requires uniform avoidance of finitely many equations
\[
k^4+r^4-s^4=t.
\]
I found no rigorous way to establish this.

A fresh Route 2 attempt must therefore exploit exact polynomial algebra—likely congruences, valuation patterns, or a theorem about integral points on the difference surfaces—not merely order, sparsity, gap growth, or generating-function formalism.