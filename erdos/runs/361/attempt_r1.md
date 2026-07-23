STATUS: BLOCKED
## Result

Route 1 does not presently yield a global inverse theorem, so the problem remains unsolved for \(0<c<1\). I proved several rigorous structural results that clarify the obstruction. First, there is a substantially stronger geometric construction than the single-window construction: a union of weighted cardinality windows, certified by an integer-valued separating function. Second, if an admissible set contains a full divisibility core \(d\mathbb Z\cap[N]\), the remaining optimization reduces exactly to a bounded-residue subset-sum condition; for \(d=3\) this reduction can be solved completely. This produces mixed periodic/high-interval constructions that beat both the least-nondivisor construction and every single-window construction—for example, when \(c=3/4\) and \(n\equiv1\pmod 3\), it gives \(M_c(n)\ge n/3+O(1)\). Finally, a full cardinality window is locally rigid against adding elements well below it. The unresolved step is a global theorem forcing an arbitrary dense extremizer to contain, or be close to, one of these structured cores; proving that appears comparable in strength to the original problem.

## Complete Argument

Throughout this section assume \(N<n\), since the range \(N\ge n\) is already settled in the brief.

### 1. A weighted multi-window construction

The one-window construction is only the first member of a larger family.

#### Theorem 1

For every integer \(K\ge1\), define
\[
W_K(N,n):=
\bigcup_{j=1}^{K}
\left\{
a\in[N]:
\frac{jn}{K+1}<a<\frac{jn}{K}
\right\}.
\]
Then \(W_K(N,n)\) is admissible: no subset of it sums to \(n\).

Moreover,
\[
|W_K(N,n)|
=
\sum_{j=1}^{K}
\max\left(
0,\,
\min\left(N,\left\lceil\frac{jn}{K}\right\rceil-1\right)
-\left\lfloor\frac{jn}{K+1}\right\rfloor
\right).
\]

For fixed \(c\in(0,1)\) and \(N=\lfloor cn\rfloor\),
\[
|W_K(N,n)|=g_K(c)n+O_K(1),
\]
where
\[
g_K(c):=
\sum_{j=1}^{K}
\left(
\min\left(c,\frac jK\right)-\frac{j}{K+1}
\right)_+.
\]

#### Proof

For \(1\le j<K\),
\[
\frac jK\le \frac{j+1}{K+1}
\]
because \(j\le K\). Thus the open intervals
\[
\left(\frac{jn}{K+1},\frac{jn}{K}\right)
\]
are pairwise disjoint. Consequently, every \(a\in W_K(N,n)\) has a unique associated integer \(j(a)\in\{1,\dots,K\}\) satisfying
\[
\frac{j(a)n}{K+1}<a<\frac{j(a)n}{K}.
\]
Equivalently,
\[
K\frac an<j(a)<(K+1)\frac an.
\]

Suppose, for contradiction, that \(S\subseteq W_K(N,n)\) and
\[
\sum_{a\in S}a=n.
\]
Summing the preceding strict inequalities over \(a\in S\) gives
\[
K
=
K\sum_{a\in S}\frac an
<
\sum_{a\in S}j(a)
<
(K+1)\sum_{a\in S}\frac an
=
K+1.
\]
But \(\sum_{a\in S}j(a)\) is an integer, and there is no integer strictly between \(K\) and \(K+1\). This contradiction proves admissibility.

For a fixed \(j\), the integers in the \(j\)-th interval range from
\[
\left\lfloor\frac{jn}{K+1}\right\rfloor+1
\]
to
\[
\min\left(N,\left\lceil\frac{jn}{K}\right\rceil-1\right).
\]
This gives the exact cardinality formula. Dividing the interval lengths by \(n\) gives the asymptotic formula, with \(O_K(1)\) total endpoint error. ∎

#### Example: \(c=3/4\)

Taking \(K=4\) gives the three relevant intervals
\[
\left(\frac n5,\frac n4\right),\qquad
\left(\frac{2n}5,\frac n2\right),\qquad
\left(\frac{3n}5,\frac{3n}4\right).
\]
Their total asymptotic length inside \([3n/4]\) is
\[
\left(\frac14-\frac15\right)
+
\left(\frac12-\frac25\right)
+
\left(\frac34-\frac35\right)
=
\frac{3}{10}.
\]
Hence
\[
M(\lfloor3n/4\rfloor,n)\ge \frac{3n}{10}+O(1)
\]
for every \(n\).

This is stronger than every single-window construction at \(c=3/4\), whose best density is \(1/4\).

A simpler instance is
\[
\left(\frac n4,\frac n3\right)
\cup
\left(\frac n2,\frac{2n}3\right).
\]
Assign weight \(1\) to the first interval and weight \(2\) to the second. Any subset of total weight at most \(3\) has sum less than \(n\), while one of total weight at least \(4\) has sum greater than \(n\).

---

### 2. Exact reduction around a full divisibility core

Let
\[
D_d(N):=d\mathbb Z\cap[N],
\qquad
m:=\left\lfloor\frac Nd\right\rfloor.
\]

The subset sums of \(D_d(N)\) contain every multiple
\[
0,d,2d,\dots,d\frac{m(m+1)}2,
\]
because after division by \(d\) this is the complete sequence \([m]\).

#### Theorem 2

Let \(d\ge2\) with \(d\nmid n\), and suppose
\[
\frac{m(m+1)}2\ge \left\lfloor\frac nd\right\rfloor.
\]
For any
\[
B\subseteq[N]\setminus D_d(N),
\]
the set
\[
A=D_d(N)\cup B
\]
is admissible if and only if there is no subset \(X\subseteq B\) satisfying
\[
\sigma(X)\le n
\qquad\text{and}\qquad
\sigma(X)\equiv n\pmod d.
\]

For fixed \(c>0\), \(N=\lfloor cn\rfloor\), and fixed \(d\), the displayed capacity condition holds for all sufficiently large \(n\).

#### Proof

Suppose first that \(A\) contains a subset \(S\) with \(\sigma(S)=n\). Put
\[
X:=S\cap B.
\]
The sum of the elements of \(S\cap D_d(N)\) is divisible by \(d\), so
\[
\sigma(X)\equiv n\pmod d.
\]
Also \(\sigma(X)\le n\). Thus \(X\) has the prohibited property.

Conversely, suppose \(X\subseteq B\) satisfies the two displayed conditions. If \(\sigma(X)=n\), then \(X\) itself is a forbidden subset.

Otherwise \(\sigma(X)<n\), and
\[
q:=\frac{n-\sigma(X)}d
\]
is a positive integer. Moreover,
\[
q\le \left\lfloor\frac nd\right\rfloor
\le \frac{m(m+1)}2.
\]
Every integer from \(0\) to \(m(m+1)/2\) is a subset sum of \([m]\). Hence some subset of \(D_d(N)\) sums to \(dq=n-\sigma(X)\). Combining it with \(X\) gives a subset of \(A\) summing to \(n\).

Finally, when \(N=\lfloor cn\rfloor\),
\[
m=\frac{cn}{d}+O(1),
\]
so \(m(m+1)/2\gg_{c,d}n^2\), which eventually exceeds \(n/d\). ∎

This theorem is an exact local inverse statement: once the full periodic core is present, all remaining structure is governed by a residue condition together with the inequality \(\sigma(X)\le n\).

---

### 3. A mixed periodic/high-interval construction

Theorem 2 immediately suggests constructions that are neither a pure sublattice nor a pure cardinality window.

#### Theorem 3

Let \(d\ge2\), \(d\nmid n\), and write
\[
t\equiv n\pmod d,\qquad 1\le t\le d-1.
\]
Define
\[
A_d(N,n)
=
D_d(N)
\cup
\left\{
a\in[N]:
a>\frac n2,\ a\not\equiv t\pmod d
\right\}.
\]
Then \(A_d(N,n)\) is admissible.

For fixed \(d\) and \(N=\lfloor cn\rfloor\),
\[
|A_d(N,n)|
=
\frac{c}{d}n
+
\frac{d-2}{d}\left(c-\frac12\right)_+n
+
O_d(1).
\]

Equivalently, when \(c>1/2\),
\[
|A_d(N,n)|
=
\left(
c-\frac12+\frac{1-c}{d}
\right)n+O_d(1).
\]

#### Proof

Suppose \(S\subseteq A_d(N,n)\) sums to \(n\). Since every element in the added high part is greater than \(n/2\), \(S\) contains at most one element outside \(D_d(N)\).

If it contains none, then \(\sigma(S)\equiv0\pmod d\), contrary to \(d\nmid n\).

If it contains exactly one element \(a\notin D_d(N)\), then
\[
\sigma(S)\equiv a\not\equiv t\equiv n\pmod d,
\]
again a contradiction.

For the count, \(D_d(N)\) contributes \(N/d+O(1)\). In the interval \((n/2,N]\), the nonzero residues other than \(t\) comprise \(d-2\) of the \(d\) residue classes, contributing
\[
\frac{d-2}{d}\left(N-\frac n2\right)_++O_d(1).
\]
This proves the formula. ∎

#### Consequence at \(c=3/4\)

Take \(n\equiv1\pmod3\) and \(N=\lfloor3n/4\rfloor\). Then
\[
A=
\{a\le N:3\mid a\}
\cup
\left\{
a:\frac n2<a\le N,\ a\equiv2\pmod3
\right\}
\]
is admissible and has
\[
|A|=\frac N3+\frac{N-n/2}{3}+O(1)
=\frac n3+O(1).
\]

For example, along \(n=6m+4\),
\[
M(\lfloor3n/4\rfloor,n)\ge \frac n3+O(1).
\]

This beats, on this sequence:

- the least-nondivisor construction, which gives \(N/3=n/4+O(1)\);
- every single cardinality window, whose best density at \(c=3/4\) is \(1/4\);
- the weighted \(K=4\) construction above, which gives \(3n/10+O(1)\).

It does not establish that \(n/3\) is globally optimal.

---

### 4. Complete classification when the full \(3\)-divisibility core is fixed

For modulus \(3\), Theorem 2 can be completely resolved.

#### Theorem 4

Suppose \(3\nmid n\), let \(t\equiv n\pmod3\), and let \(r\) be the other nonzero residue modulo \(3\). Thus
\[
\{t,r\}=\{1,2\}.
\]
Assume
\[
m=\left\lfloor\frac N3\right\rfloor,
\qquad
\frac{m(m+1)}2\ge\left\lfloor\frac n3\right\rfloor.
\]

An admissible set \(A\subseteq[N]\) containing every multiple of \(3\) has the form
\[
A=D_3(N)\cup B,
\]
where:

1. every element of \(B\) is congruent to \(r\pmod3\);
2. every two distinct \(x,y\in B\) satisfy
   \[
   x+y>n.
   \]

Conversely, every such \(B\) gives an admissible \(A\).

Consequently, if
\[
C_r:=\{x\in[N]:x\equiv r\pmod3\},
\]
the exact largest possible number of extra elements is
\[
T_r(N,n)
=
\max\left(
0,\,
\max_{x\in C_r}
\left[
1+
\#\{y\in C_r:y>\max(x,n-x)\}
\right]
\right).
\]

In particular,
\[
T_r(N,n)=
\begin{cases}
O(1),&N\le n/2,\\[1mm]
\dfrac{N-n/2}{3}+O(1),&N>n/2.
\end{cases}
\]

Thus among sets containing \(D_3(N)\),
\[
|A|
\le
\frac N3+\frac{(N-n/2)_+}{3}+O(1),
\]
and this bound is attained up to \(O(1)\).

#### Proof

By Theorem 2, \(B\) cannot contain an element congruent to \(t\pmod3\), since its singleton sum is at most \(N<n\) and is congruent to \(n\pmod3\). Hence all elements of \(B\) lie in residue class \(r\).

In both cases \(t=1,r=2\) and \(t=2,r=1\), one has
\[
2r\equiv t\pmod3.
\]
Therefore, if distinct \(x,y\in B\) satisfy \(x+y\le n\), the subset \(\{x,y\}\) has sum congruent to \(n\pmod3\), contradicting Theorem 2. This proves the necessity of the pairwise inequality.

Conversely, suppose every two distinct elements of \(B\) have sum greater than \(n\). If \(X\subseteq B\) satisfies
\[
\sigma(X)\equiv n\pmod3,
\]
then \(|X|\equiv2\pmod3\), hence \(|X|\ge2\). Any two elements of \(X\) already have sum greater than \(n\), so \(\sigma(X)>n\). Theorem 2 now shows that \(D_3(N)\cup B\) is admissible.

For the exact optimization, let \(x\) be the smallest element of a nonempty valid \(B\). Every other member \(y\) must satisfy both \(y>x\) and \(y>n-x\). Thus
\[
|B|
\le
1+\#\{y\in C_r:y>\max(x,n-x)\}.
\]
Conversely, taking \(x\) together with every such \(y\) gives a valid set, proving the formula.

Finally, a valid \(B\) has at most one element at most \(n/2\), while all its remaining elements lie in \(C_r\cap(n/2,N]\). This gives
\[
|B|\le1+\#(C_r\cap(n/2,N])
=\frac{(N-n/2)_+}{3}+O(1).
\]
Taking all members of \(C_r\cap(n/2,N]\) gives the matching lower bound. ∎

The restriction \(A\supseteq D_3(N)\) is essential: this theorem does not give a global upper bound for \(M(N,n)\).

---

### 5. Local rigidity of a full cardinality window

The geometric obstruction also has a genuine local stability property.

#### Lemma 5: restricted sums of an integer interval

Let \(L\le U\) and \(1\le h\le U-L+1\). The sums of \(h\) distinct elements of \([L,U]\) are precisely all integers in
\[
\left[
hL+\frac{h(h-1)}2,\,
hU-\frac{h(h-1)}2
\right].
\]

#### Proof

Put \(m=U-L\). Choosing \(h\) distinct elements of \([L,U]\) is equivalent to choosing
\[
0\le x_1<\cdots<x_h\le m.
\]
Write
\[
y_i=x_i-(i-1).
\]
Then
\[
0\le y_1\le\cdots\le y_h\le m-h+1
\]
and
\[
\sum_{i=1}^h x_i
=
\frac{h(h-1)}2+\sum_{i=1}^h y_i.
\]

Every integer \(q\in[0,h(m-h+1)]\) can be written as the sum of \(h\) integers
\[
0\le y_1\le\cdots\le y_h\le m-h+1.
\]
Indeed, write \(q=ah+b\) with \(0\le b<h\); take \(h-b\) entries equal to \(a\) and \(b\) entries equal to \(a+1\). The case \(a=m-h+1\) necessarily has \(b=0\). This proves the stated interval of sums after restoring the contribution \(hL+h(h-1)/2\). ∎

#### Proposition 6

Fix \(K\ge1\) and put
\[
H_K(n)=
\left\{
a\in\mathbb Z:
\frac n{K+1}<a<\frac nK
\right\}.
\]
Let
\[
C_K:=\frac{K(K+1)}2.
\]
For all sufficiently large \(n\), every integer \(x\) satisfying
\[
C_K\le x\le \frac n{K+1}-C_K
\]
can be completed to \(n\) by \(K\) distinct elements of \(H_K(n)\).

Consequently, an admissible set containing all of \(H_K(n)\) cannot contain any such \(x\).

#### Proof

Write
\[
L=\left\lfloor\frac n{K+1}\right\rfloor+1,
\qquad
U=\left\lceil\frac nK\right\rceil-1.
\]
For large \(n\), \([L,U]\) contains at least \(K\) integers.

By Lemma 5, the \(K\)-element sums from this interval fill
\[
\left[
KL+\frac{K(K-1)}2,\,
KU-\frac{K(K-1)}2
\right].
\]

Since
\[
L\le \frac n{K+1}+1,
\]
the lower endpoint is at most
\[
\frac{Kn}{K+1}+K+\frac{K(K-1)}2
=
\frac{Kn}{K+1}+C_K.
\]
The assumed upper bound on \(x\) gives
\[
n-x\ge \frac{Kn}{K+1}+C_K.
\]

Similarly,
\[
U\ge\frac nK-1,
\]
so the upper endpoint is at least
\[
n-K-\frac{K(K-1)}2=n-C_K.
\]
The assumed lower bound on \(x\) gives \(n-x\le n-C_K\). Hence \(n-x\) lies in the complete interval of \(K\)-term sums, proving the result. ∎

Thus a full window \((n/(K+1),n/K)\) excludes, up to \(O_K(1)\) boundary points, the entire interval below it. It is not globally saturated: the weighted-window construction shows that additional safe intervals can exist much higher up.

## Self-Audit

1. **There is no global upper bound matching the new constructions.**  
   This is the decisive weakness and the reason for the status `BLOCKED`. The proved results classify only sets containing a full periodic core or a full interval window. An arbitrary extremizer need contain neither.

2. **The exact periodic-core reduction uses the full set \(d\mathbb Z\cap[N]\).**  
   Omitting even a few multiples can destroy the direct completion argument for selected remainders. Within the stated hypothesis, however, Theorem 2 is exact: it follows solely from the complete subset sums of \([m]\), with the finite capacity condition written explicitly.

3. **The geometric rigidity result is one-sided.**  
   Proposition 6 controls additions below a full window but says nothing about upper gaps or mixed periodic additions. Its claimed range is nevertheless justified by the exact interval-of-restricted-sums lemma and explicit floor-safe inequalities.

## Computations To Verify

The following code verifies admissibility, computes small exact optima, and tests the constructions.

```python
def admissible(A, n):
    """Exact distinct-subset-sum test."""
    mask = (1 << (n + 1)) - 1
    R = 1  # bit 0
    for a in A:
        R |= (R << a) & mask
    return ((R >> n) & 1) == 0


def weighted_windows(N, n, K):
    A = []
    for a in range(1, N + 1):
        for j in range(1, K + 1):
            # j*n/(K+1) < a < j*n/K
            if j * n < (K + 1) * a and K * a < j * n:
                A.append(a)
                break
    return A


def modular_high(N, n, d):
    assert n % d != 0
    t = n % d
    return [
        a for a in range(1, N + 1)
        if (a % d == 0) or (2 * a > n and a % d != t)
    ]


def exact_M(N, n):
    """
    Exhaustive branch-and-bound. Practical only for small N,
    roughly N <= 30 depending on the instance.
    """
    items = list(range(N, 0, -1))
    capmask = (1 << (n + 1)) - 1
    best_size = 0
    best_set = []

    def dfs(i, R, chosen):
        nonlocal best_size, best_set

        if len(chosen) + (len(items) - i) <= best_size:
            return

        if i == len(items):
            if len(chosen) > best_size:
                best_size = len(chosen)
                best_set = chosen[:]
            return

        a = items[i]
        R2 = R | ((R << a) & capmask)

        if ((R2 >> n) & 1) == 0:
            chosen.append(a)
            dfs(i + 1, R2, chosen)
            chosen.pop()

        dfs(i + 1, R, chosen)

    dfs(0, 1, [])
    return best_size, sorted(best_set)


def d3_local_formula(N, n):
    """
    Exact optimum among sets containing every multiple of 3,
    assuming the capacity condition in Theorem 4.
    """
    assert n % 3 != 0
    t = n % 3
    r = 3 - t  # swaps 1 and 2

    D = [a for a in range(1, N + 1) if a % 3 == 0]
    C = [a for a in range(1, N + 1) if a % 3 == r]

    best_B = []
    for x in C:
        B = [x] + [y for y in C if y > max(x, n - x)]
        if len(B) > len(best_B):
            best_B = B

    A = sorted(D + best_B)
    return len(A), A


# Verification grid for the weighted construction
for n in range(20, 201):
    for N in range(1, n):
        for K in range(1, 12):
            A = weighted_windows(N, n, K)
            assert admissible(A, n)

# Verification grid for modular-high constructions
for n in range(20, 201):
    for N in range(1, n):
        for d in range(2, 15):
            if n % d:
                A = modular_high(N, n, d)
                assert admissible(A, n)

# Check the c=3/4, d=3 family
for m in range(10, 101):
    n = 6 * m + 4
    N = (3 * n) // 4
    A = modular_high(N, n, 3)
    assert admissible(A, n)
    print(n, N, len(A), len(A) / n)

# Compare exact small optima against all templates
for n in range(10, 41):
    for N in range(1, min(n, 26)):
        opt, extremizer = exact_M(N, n)

        candidates = []
        for K in range(1, 15):
            candidates.append(("weight", K, weighted_windows(N, n, K)))

        for d in range(2, 12):
            if n % d:
                candidates.append(("mod-high", d, modular_high(N, n, d)))

        best_template = max(candidates, key=lambda z: len(z[2]))
        if opt > len(best_template[2]):
            print("UNEXPLAINED:",
                  n, N, opt, extremizer,
                  "best template", best_template[0:2],
                  len(best_template[2]))

# Verify Theorem 4 against brute force over the nonmultiple elements
for n in range(10, 60):
    if n % 3 == 0:
        continue
    for N in range(1, min(n, 25)):
        m = N // 3
        if m * (m + 1) // 2 < n // 3:
            continue

        formula_size, formula_A = d3_local_formula(N, n)
        assert admissible(formula_A, n)

        D = {a for a in range(1, N + 1) if a % 3 == 0}
        outsiders = [a for a in range(1, N + 1) if a % 3]

        best = len(D)
        for mask in range(1 << len(outsiders)):
            A = set(D)
            for i, a in enumerate(outsiders):
                if (mask >> i) & 1:
                    A.add(a)
            if admissible(A, n):
                best = max(best, len(A))

        assert best == formula_size, (n, N, best, formula_size)
```

For larger \(n\), the most useful computation would be exact ILP optimization followed by classification of extremizers according to:

1. distance from \(W_K(N,n)\) for \(K\le50\);
2. distance from \(d\mathbb Z\cap[N]\) and the modular-high extensions for \(d\le20\);
3. whether extremizers combine several weighted intervals with residue restrictions;
4. whether any extremizer is \(\Omega(n)\)-far from every bounded-complexity periodic/weighted template.

## Route Diagnosis

### What worked

- A genuine geometric certificate emerged: assigning each selected integer \(a\) an integer weight \(j(a)\) with
  \[
  K\frac an<j(a)<(K+1)\frac an
  \]
  rules out a target sum. This yields bounded unions of intervals rather than a single cardinality window.
- A full periodic core admits an exact quotient-remainder reduction.
- For modulus \(3\), that reduced problem is completely classifiable.
- The resulting mixed construction shows that pure “sublattice versus one interval” classifications are false even at the level of the best presently available lower bounds.

### Precise block

To finish Route 1, one would need to prove something like:

> Every dense admissible \(A\subseteq[cn]\), after deleting \(o(n)\) elements, either contains an almost-complete residue-class core whose missing remainders can be classified, or admits a bounded-complexity integer-weight certificate of the type used in Theorem 1.

No such implication has been proved. If the full divisibility core is replaced by an arbitrary dense subset of that core, deciding which remainders its subset sums cover becomes another dense missing-target subset-sum problem. Thus the attempted reduction returns to a problem of essentially comparable strength.

Ordinary continuum compactness is insufficient: for example, the even numbers become equidistributed across \([0,c]\) after scaling, so their decisive parity obstruction disappears in the real limit.

### Ledger

**Proved**

1. Weighted multi-window construction and exact count.
2. Exact full-divisibility-core reduction.
3. Mixed periodic/high-interval construction.
4. Complete modulus-\(3\) classification conditional on containing the full \(3\)-core.
5. Restricted-sum interval lemma and low-side saturation of a full cardinality window.

**Plausible but unproved**

1. Extremizers may be describable by recursive combinations of residue obstructions and integer-weight windows.
2. A universal asymptotic upper bound \(M(N,n)\le N/2+o(n)\) may hold for fixed \(N/n\), but no proof was obtained.
3. Bounded-complexity periodic/weighted templates may capture all leading-order extremizers.

**Dead ends**

1. **“Pure sublattice or one interval” classification:** disproved as an adequate list by Theorems 1 and 3.
2. **A purely real/continuum inverse theorem:** loses modular obstructions such as parity.
3. **Extending the full-core theorem by simply deleting \(o(n)\) core elements:** even sparse deletions can target particular remainders, and proving robustness leads back to the original subset-sum problem.
4. **Using modular zero-sums alone:** a zero-sum modulo \(n\) may lift to \(2n\) or more; the divisibility constructions exploit exactly this failure.

A fresh attempt should computationally classify exact extremizers against the combined periodic/weighted templates, then seek an inverse theorem formulated in a mixed ordered-profinite space rather than solely in \(\mathbb R\) or solely modulo \(n\).