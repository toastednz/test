STATUS: BLOCKED

## Result

Route 1 yields sharp critical-scale estimates but not a contradiction. For every integer-valued \(f\in\mathbb Q[x]\) of degree \(d\ge2\), any hypothetical complement \(A\) satisfies the uniform bound \(|A\cap I|=O_f(|I|^{1-1/d})\), while covering an interval of length \(N\) requires at least \(\Omega_f(N^{1-1/d})\) distinct centers and \(\Omega_f(N^{1/d})\) distinct polynomial values. Thus the lower and upper exponents meet exactly. For \(f(x)=x^3\), this is genuinely sharp: along infinitely many scales there are cube-difference-free subsets of intervals of size \((4^{-1/3}+o(1))N^{2/3}\), exactly matching the leading constant in the elementary coverage lower bound. Such critical chunks can also be embedded at infinitely many separated scales in one infinite cube-difference-free set. Consequently, pure cardinality/extremal difference forcing cannot solve the problem; a successful Route 1 argument would need a new structural theorem about finite direct pairs whose sumset contains a long interval, together with a localization or multiscale rigidity result. No such theorem is proved here.

## Complete Argument

### 1. Uniform sparsity of polynomial values

Throughout, an interval of length \(L\) means an interval containing exactly \(L\) consecutive integers.

#### Lemma 1

Let \(f\in\mathbb Q[x]\) have degree \(d\ge1\) and leading coefficient \(\alpha\ne0\). There is a constant \(U_f\) such that every interval \(I\) of length \(L\ge1\) satisfies
\[
|f(\mathbb Z)\cap I|\le U_f(L^{1/d}+1).
\]

#### Proof

Write
\[
I=\{u,u+1,\dots,u+L-1\}
\]
and let \(t=u+(L-1)/2\). Factor over \(\mathbb C\):
\[
f(x)-t=\alpha\prod_{j=1}^d(x-z_j).
\]
If \(k\in\mathbb Z\) and \(f(k)\in I\), then
\[
|f(k)-t|\le L/2.
\]
Consequently,
\[
\prod_{j=1}^d |k-z_j|\le \frac{L}{2|\alpha|}.
\]
At least one factor therefore satisfies
\[
|k-z_j|\le \left(\frac{L}{2|\alpha|}\right)^{1/d}.
\]
Since \(|k-\operatorname{Re}z_j|\le |k-z_j|\), every such \(k\) lies in the union of \(d\) real intervals, each of length
\[
2\left(\frac{L}{2|\alpha|}\right)^{1/d}.
\]
The number of possible integer inputs is therefore at most
\[
d\left(2\left(\frac{L}{2|\alpha|}\right)^{1/d}+1\right).
\]
The number of distinct values is no larger. ∎

This proof applies to all rational-coefficient polynomials, independently of integer-valuedness.

---

### 2. The critical local upper bound for a complement

Let
\[
C=f(\mathbb Z)
\]
and suppose, provisionally, that
\[
\mathbb Z=A\oplus C.
\]

#### Lemma 2

There is a constant \(P_f\) such that every interval \(J\) of length \(L\ge1\) satisfies
\[
|A\cap J|\le P_f L^{1-1/d}.
\]

#### Proof

For \(K\ge1\), put
\[
E_K=f(\{-K,-K+1,\dots,K\})\subseteq C,
\]
with duplicate values discarded.

Every equation \(f(x)=v\) has at most \(d\) integer solutions. Hence
\[
|E_K|\ge \frac{2K+1}{d}.
\]
Also, for a constant \(V_f\),
\[
\operatorname{diam}(E_K)\le V_f(K+1)^d.
\]

Let \(B=A\cap J\). Since the global sum is direct, the map
\[
B\times E_K\longrightarrow\mathbb Z,\qquad (b,e)\mapsto b+e
\]
is injective. All these sums lie in an interval of length at most
\[
L+\operatorname{diam}(E_K).
\]
Therefore
\[
|B||E_K|
 \le L+\operatorname{diam}(E_K)
 \le L+V_f(K+1)^d.
\]
Choose \(K=\lfloor L^{1/d}\rfloor\). Since \(K\gg L^{1/d}\) and \((K+1)^d\ll L\), with constants depending only on \(d\),
\[
|B|\ll_f \frac{L}{L^{1/d}}=L^{1-1/d}.
\]
This proves the assertion. ∎

This is a quantitative difference-forcing statement: every finite subset of \(A\) is \(C-C\)-free, and packing it against a finite polynomial sample forces the critical exponent \(1-1/d\).

---

### 3. The exact coverage burden

For an interval \(I\), define the centers and polynomial values actually used to cover it:
\[
B_I:=\{a\in A:(a+C)\cap I\ne\varnothing\},
\]
\[
E_I:=\{c\in C:(A+c)\cap I\ne\varnothing\}.
\]
Both are finite because \(I\) has finitely many points and every point has one representation.

#### Lemma 3

There are constants \(c_f,c_f'>0\) such that every interval \(I\) of length \(L\) satisfies
\[
|B_I|\ge c_f L^{1-1/d}
\]
and
\[
|E_I|\ge c_f' L^{1/d}.
\]

Moreover,
\[
I\subseteq B_I+E_I,
\]
and the sum \(B_I+E_I\) is direct: all \(|B_I||E_I|\) cross-sums are distinct.

#### Proof

For a fixed \(a\in B_I\), the points of \(I\) represented using that center are
\[
(a+C)\cap I.
\]
Their number is
\[
|C\cap(I-a)|\le U_f(L^{1/d}+1)
\]
by Lemma 1. These sets partition \(I\), so
\[
L
 =\sum_{a\in B_I}|(a+C)\cap I|
 \le |B_I|\,U_f(L^{1/d}+1).
\]
Thus
\[
|B_I|\gg_f L^{1-1/d}.
\]

For a fixed \(c\in E_I\),
\[
(A+c)\cap I
\]
has cardinality
\[
|A\cap(I-c)|\le P_fL^{1-1/d}
\]
by Lemma 2. These sets also partition \(I\), giving
\[
L\le |E_I|P_fL^{1-1/d}.
\]
Hence
\[
|E_I|\gg_f L^{1/d}.
\]

Every \(n\in I\) has its representation in \(B_I\times E_I\), so
\[
I\subseteq B_I+E_I.
\]
Finally, global uniqueness implies that if
\[
b+e=b'+e',
\qquad b,b'\in B_I,\quad e,e'\in E_I,
\]
then \(b=b'\) and \(e=e'\). ∎

Thus Route 1 reduces naturally to the following finite structural problem:

> Can finite sets \(B\subseteq\mathbb Z\) and \(E\subseteq f(\mathbb Z)\), with \(B+E\) direct, contain arbitrarily long intervals inside \(B+E\)?

The preceding cardinal estimates alone do not answer this because they meet exactly at the critical exponents.

---

### 4. Sharpness for cubes

Now specialize to
\[
C_3=\{k^3:k\in\mathbb Z\},
\qquad
D_3=C_3-C_3.
\]

#### Lemma 4: Exact elementary coverage constant

Every interval \(I\) of length \(L\) contains at most
\[
(4(L-1))^{1/3}+1
\]
distinct cubes. Consequently, in any hypothetical tiling
\[
\mathbb Z=A\oplus C_3,
\]
covering an interval of length \(L\) requires at least
\[
\frac{L}{(4(L-1))^{1/3}+1}
  =(4^{-1/3}+o(1))L^{2/3}
\]
distinct centers.

#### Proof

Suppose \(r\) distinct cubes lie in \(I\), with corresponding indices
\[
k_1<k_2<\cdots<k_r.
\]
Put \(h=k_r-k_1\ge r-1\). For every real \(x\),
\[
(x+h)^3-x^3
 =h\left(3\left(x+\frac h2\right)^2+\frac{h^2}{4}\right)
 \ge \frac{h^3}{4}.
\]
Thus
\[
L-1\ge k_r^3-k_1^3\ge \frac{h^3}{4}.
\]
Hence
\[
r\le h+1\le (4(L-1))^{1/3}+1.
\]
The center bound follows by partitioning \(I\) among its used translates. ∎

#### Lemma 5: Critical upper bound for cube-difference-free sets

If \(B\) is contained in an interval of length \(L\) and
\[
(B-B)\cap D_3=\{0\},
\]
then
\[
|B|=O(L^{2/3}).
\]
More precisely,
\[
|B|\le
\left(\frac{3}{2^{4/3}}+o(1)\right)L^{2/3}.
\]

#### Proof

For \(K\ge1\), let
\[
E_K=\{-K^3,\dots,-1,0,1,\dots,K^3\}
\]
where only actual cubes are included, so \(|E_K|=2K+1\).

The map \(B\times E_K\to\mathbb Z\) by addition is injective. Indeed, a collision would give a nonzero element of
\[
(B-B)\cap(E_K-E_K)\subseteq(B-B)\cap D_3.
\]
All sums lie in an interval containing at most
\[
L+2K^3
\]
integers. Therefore
\[
|B|(2K+1)\le L+2K^3.
\]
Taking \(K=(L/4)^{1/3}+O(1)\) gives
\[
|B|\le
\left(\frac{3}{2^{4/3}}+o(1)\right)L^{2/3}.
\]
∎

The important point is that this \(L^{2/3}\) upper bound cannot be improved to \(o(L^{2/3})\).

#### Lemma 6: Critical cube-difference-free arithmetic progressions

Let \(p\) be a prime with
\[
p\equiv2\pmod3,
\]
and put
\[
M_p=\frac{p^2-1}{4},
\qquad
B_p=\{0,p,2p,\dots,M_pp\}.
\]
Then
\[
(B_p-B_p)\cap D_3=\{0\}.
\]

Moreover, writing \(X_p=\operatorname{diam}(B_p)=pM_p\),
\[
|B_p|
 =(4^{-1/3}+o(1))X_p^{2/3}.
\]

#### Proof

Because \(\gcd(3,p-1)=1\), the map \(x\mapsto x^3\) is injective modulo \(p\). Hence
\[
p\mid x^3-y^3
\quad\Longrightarrow\quad
x\equiv y\pmod p.
\]
Write \(h=x-y\). If \(x^3-y^3\ne0\) is divisible by \(p\), then \(|h|\ge p\). Also,
\[
|x^3-y^3|
 =|h|\left(3\left(y+\frac h2\right)^2+\frac{h^2}{4}\right)
 \ge \frac{|h|^3}{4}
 \ge \frac{p^3}{4}.
\]

Every nonzero difference of two elements of \(B_p\) is divisible by \(p\) and has absolute value at most
\[
pM_p=\frac{p(p^2-1)}4<\frac{p^3}{4}.
\]
It therefore cannot be a difference of two cubes.

Finally,
\[
X_p\sim\frac{p^3}{4},
\qquad
|B_p|=M_p+1\sim\frac{p^2}{4},
\]
so
\[
\frac{|B_p|}{X_p^{2/3}}\longrightarrow 4^{-1/3}.
\]
∎

There are infinitely many primes \(p\equiv2\pmod3\): if \(p_1,\dots,p_r\) were all of them, then a prime divisor congruent to \(2\pmod3\) of
\[
3p_1\cdots p_r-1
\]
would be new.

The constant \(4^{-1/3}\) is exactly the leading constant in Lemma 4. Thus even if one could localize all required centers to an interval comparable in length to the target interval, the elementary coverage bound would land exactly at a scale attained by genuine cube-difference-free sets.

---

### 5. Critical chunks can occur at infinitely many scales

The preceding construction is not merely a finite accident.

#### Lemma 7

There is an infinite set \(A_\infty\subseteq\mathbb Z\) such that
\[
(A_\infty-A_\infty)\cap D_3=\{0\}
\]
and such that \(A_\infty\) contains translates of \(B_p\) for infinitely many primes \(p\equiv2\pmod3\).

#### Proof

First observe that
\[
|D_3\cap[-X,X]|=O(X^{2/3}).
\]
Indeed, write
\[
x^3-y^3=h\left(3\left(y+\frac h2\right)^2+\frac{h^2}{4}\right),
\qquad h=x-y.
\]
If the absolute value is at most \(X\), then
\[
|h|\le (4X)^{1/3}.
\]
For a fixed nonzero \(h\),
\[
\left|y+\frac h2\right|
 \le \sqrt{\frac{X}{3|h|}},
\]
so there are
\[
O\left(\sqrt{\frac{X}{|h|}}+1\right)
\]
possible \(y\). Summing over \(1\le |h|\le(4X)^{1/3}\) gives
\[
O\left(
 \sqrt X\sum_{h\le(4X)^{1/3}}h^{-1/2}
 +X^{1/3}
\right)
=O(X^{2/3}).
\]

Now construct finite sets inductively. Suppose \(A_{j-1}\) is finite and cube-difference-free. Choose a new prime \(p_j\equiv2\pmod3\) and its block \(B_{p_j}\). A translate \(t+B_{p_j}\) conflicts with \(A_{j-1}\) only if
\[
t+b-a\in D_3
\]
for some \(b\in B_{p_j}\) and \(a\in A_{j-1}\). Thus the forbidden translations lie in the finite union
\[
\bigcup_{\substack{a\in A_{j-1}\\b\in B_{p_j}}}(D_3+a-b).
\]
Every finite union of translates of \(D_3\) has asymptotic density zero, by the bound just proved. It therefore cannot contain all sufficiently large integers. Choose a large permitted \(t_j\), and set
\[
A_j=A_{j-1}\cup(t_j+B_{p_j}).
\]
Internal differences in the new block are safe by Lemma 6, and all cross-differences are safe by the choice of \(t_j\).

Then
\[
A_\infty=\bigcup_{j\ge1}A_j
\]
has the required properties. ∎

Therefore, even strengthening Route 1 from a single interval to “infinitely many critical-scale intervals” is insufficient without exploiting coverage.

---

### 6. A digital exact tiling with the same critical exponents

The exponent balance itself is compatible with exact tiling.

Fix \(d\ge2\). Every integer has a unique finite balanced ternary expansion
\[
n=\sum_{j\ge0}\varepsilon_j3^j,
\qquad \varepsilon_j\in\{-1,0,1\}.
\]
Existence follows by repeatedly choosing the balanced residue modulo \(3\); uniqueness follows by considering the highest differing digit.

Define
\[
C^{\mathrm{dig}}_d
 =\left\{\sum_{j\ge0}\varepsilon_j3^{dj}:
   \varepsilon_j\in\{-1,0,1\},
   \text{ finitely supported}\right\}
\]
and
\[
A^{\mathrm{dig}}_d
 =\left\{\sum_{\substack{i\ge0\\d\nmid i}}\varepsilon_i3^i:
   \varepsilon_i\in\{-1,0,1\},
   \text{ finitely supported}\right\}.
\]
Splitting the balanced ternary digits according to whether \(d\mid i\) gives
\[
\mathbb Z=A^{\mathrm{dig}}_d\oplus C^{\mathrm{dig}}_d.
\]

Furthermore,
\[
|C^{\mathrm{dig}}_d\cap[-X,X]|=\Theta(X^{1/d}),
\qquad
|A^{\mathrm{dig}}_d\cap[-X,X]|=\Theta(X^{1-1/d}).
\]
The first set also has the uniform interval estimate
\[
\sup_u |C^{\mathrm{dig}}_d\cap[u,u+L-1]|=O_d(L^{1/d}).
\]

For the last assertion, write \(Q=3^d\) and choose \(J\) with
\[
Q^J\le L<Q^{J+1}.
\]
Every \(c\in C^{\mathrm{dig}}_d\) can be written
\[
c=u+Q^Jv,
\]
where \(u\) has only the first \(J\) base-\(Q\) digits and hence has at most \(3^J\) possibilities and satisfies
\[
|u|<\frac{Q^J}{Q-1}.
\]
An interval of length \(L<Q^{J+1}\) can intersect only \(O(Q)\) of the clusters indexed by \(v\). Hence it contains \(O(Q3^J)=O_d(L^{1/d})\) elements.

This is not a polynomial value set. It proves, however, that critical exponents, zero density, aperiodicity, and uniform sparse interval counts are all compatible with an exact tiling. Polynomial algebra must enter any successful proof.

---

### 7. A precise alternative finite-extension target

The analysis also produced a possible constructive route for cubes.

Let \(D_3=C_3-C_3\). Consider the statement:

> **Finite-extension claim.** For every finite set
> \[
> M\subseteq\mathbb Z\setminus C_3,
> \]
> there exists \(k\in\mathbb Z\) such that
> \[
> m-k^3\notin D_3
> \qquad\text{for every }m\in M.
> \]

If this claim were true, it would solve the problem affirmatively for \(f(x)=x^3\).

Indeed, enumerate the integers. Maintain a finite cube-difference-free set of centers \(A_s\). If the next integer \(n\) is uncovered, then
\[
M=\{n-a:a\in A_s\}
\]
contains no cube. Choose \(k\) as in the claim and add
\[
a_{\rm new}=n-k^3.
\]
For every old \(a\),
\[
a_{\rm new}-a=(n-a)-k^3\notin D_3,
\]
so disjointness is preserved, and \(n\) becomes covered. At the limit, every integer is covered and all representations are unique.

I could not prove the finite-extension claim. Its forbidden equation is
\[
m-k^3=x^3-y^3,
\]
or
\[
m=k^3+x^3+(-y)^3.
\]
For \(m=t^3\), every \(k\) is forbidden because
\[
t^3-k^3\in D_3;
\]
this explains why excluding cubes is necessary. For noncubes, proving that finitely many such equations cannot cover every \(k\) appears to require substantial information about integral points on cubic surfaces. Thus this alternative is also blocked.

---

### 8. Ledger

**Proved lemmas**

1. Uniform polynomial-value sparsity in every interval:
   \[
   |f(\mathbb Z)\cap I|=O_f(|I|^{1/d}+1).
   \]
2. Every hypothetical complement satisfies
   \[
   |A\cap I|=O_f(|I|^{1-1/d}).
   \]
3. Covering an interval of length \(L\) uses
   \[
   \Omega_f(L^{1-1/d})
   \]
   centers and
   \[
   \Omega_f(L^{1/d})
   \]
   polynomial values.
4. The used finite sets \(B_I,E_I\) form a finite direct pair with
   \[
   I\subseteq B_I+E_I.
   \]
5. Cube-difference-free subsets of length-\(L\) intervals have size \(O(L^{2/3})\).
6. Infinitely many critical cube-difference-free progressions have size
   \[
   (4^{-1/3}+o(1))L^{2/3}.
   \]
7. One infinite cube-difference-free set can contain such chunks at infinitely many scales.
8. Digital exact tilings exist with the same critical growth exponents.

**Plausible but unproved**

1. A structural theorem forbidding finite direct pairs \(B,E\), with \(E\subseteq C_3\), from containing arbitrarily long intervals.
2. A localization or multiscale rigidity theorem for the finite pairs \(B_I,E_I\).
3. The finite-extension claim for noncube shifts described above.

**Dead ends**

1. An \(o(L^{2/3})\) extremal bound for cube-difference-free sets is false.
2. A contradiction based only on the exponents \(1/3\) and \(2/3\) is impossible; the digital construction realizes them in an exact tiling.
3. Merely finding critical-scale dense chunks of \(A\) cannot suffice; an infinite cube-difference-free set can contain such chunks at infinitely many scales.
4. Greedy cube construction is not routine: its extension step reduces to avoiding projections of integral points on cubic surfaces.

## Self-Audit

1. **The strongest conclusion is only that basic cardinality forcing is blocked, not that every possible version of Route 1 is hopeless.** A stability theorem using the full condition \(I\subseteq B_I\oplus E_I\) could still succeed. I believe the narrower diagnosis is justified because the cube progressions exactly attain the critical center scale, and the digital model realizes all exponent-level estimates in a genuine exact tiling.

2. **The sharp lower construction is specific to \(f(x)=x^3\), not to every polynomial.** This is enough to block a universal Route 1 proof based on a stronger extremal estimate valid for all \(f\), since any complete negative solution must handle cubes. The modular injectivity and the lower bound \(p^3/4\) were proved explicitly.

3. **The digital example is not a polynomial value set and therefore is not evidence for an affirmative answer to the original problem.** It is used only as a counterexample to growth-only reasoning. Its exact factorization and critical growth estimates follow directly from unique balanced ternary expansions.

## Computations To Verify

The following code computes the complete cube-difference set in a bounded interval. The bounds on \(h\) and \(y\) are rigorous.

```python
from math import ceil, sqrt

def cube_differences(X):
    """Complete set D_3 intersect [-X,X]."""
    D = {0}
    H = ceil((4 * X) ** (1/3)) + 2

    for h in range(-H, H + 1):
        if h == 0:
            continue

        # If |h| * (3(y+h/2)^2 + h^2/4) <= X, then:
        # |y+h/2| <= sqrt(X/(3|h|)).
        R = sqrt(X / (3 * abs(h))) + 2
        Y = ceil(abs(h) / 2 + R)

        for y in range(-Y, Y + 1):
            x = y + h
            z = x**3 - y**3
            if abs(z) <= X:
                D.add(z)

    return D
```

An exact membership test using the factorization of a difference of cubes:

```python
from math import isqrt

def floor_cuberoot(n):
    h = int(round(n ** (1/3)))
    while (h + 1)**3 <= n:
        h += 1
    while h**3 > n:
        h -= 1
    return h

def is_cube_difference(z):
    if z == 0:
        return True

    N = abs(z)
    H = floor_cuberoot(4 * N)

    # N = h(3(y+h/2)^2 + h^2/4)
    # iff 4N/h - h^2 = 3(2y+h)^2.
    for h in range(1, H + 1):
        if N % h:
            continue
        T = 4 * (N // h) - h*h
        if T < 0 or T % 3:
            continue
        s2 = T // 3
        s = isqrt(s2)
        if s*s == s2 and (s - h) % 2 == 0:
            return True

    return False
```

Verification of the critical progressions:

```python
def verify_Bp(p):
    assert p % 3 == 2
    M = (p*p - 1) // 4
    B = [p*j for j in range(M + 1)]

    for i in range(len(B)):
        for j in range(i):
            if is_cube_difference(B[i] - B[j]):
                return False, (B[i], B[j])

    X = B[-1]
    ratio = len(B) / (X ** (2/3))
    return True, ratio

for p in [5, 11, 17, 23, 29, 41]:
    print(p, verify_Bp(p))
# Ratios should approach 4^(-1/3) ≈ 0.6299605.
```

Maximum independent sets in the truncated cube-difference graph can be computed with OR-Tools:

```python
from ortools.sat.python import cp_model

def cube_difference_independence_number(N):
    # Vertices 0,...,N-1
    positive_D = [
        d for d in range(1, N)
        if is_cube_difference(d)
    ]

    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x_{i}") for i in range(N)]

    for d in positive_D:
        for i in range(N - d):
            model.Add(x[i] + x[i + d] <= 1)

    model.Maximize(sum(x))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 600
    status = solver.Solve(model)

    chosen = [i for i in range(N) if solver.Value(x[i])]
    return solver.ObjectiveValue(), chosen

for N in [50, 100, 200, 400]:
    alpha, chosen = cube_difference_independence_number(N)
    print(N, alpha, alpha / (N ** (2/3)))
```

To inspect whether the modular extremizers can produce long consecutive runs when added to centered cube representatives:

```python
def longest_consecutive_run(S):
    S = sorted(set(S))
    best = cur = 1
    best_pair = (S[0], S[0])

    start = S[0]
    for i in range(1, len(S)):
        if S[i] == S[i-1] + 1:
            cur += 1
        else:
            if cur > best:
                best = cur
                best_pair = (start, S[i-1])
            cur = 1
            start = S[i]

    if cur > best:
        best = cur
        best_pair = (start, S[-1])

    return best, best_pair

def modular_block_probe(p):
    assert p % 3 == 2
    M = (p*p - 1) // 4
    B = [p*j for j in range(M + 1)]
    R = (p - 1) // 2
    E = [r**3 for r in range(-R, R + 1)]

    sums = [b + e for b in B for e in E]
    assert len(sums) == len(set(sums))  # directness

    run, endpoints = longest_consecutive_run(sums)
    return {
        "p": p,
        "|B|": len(B),
        "|E|": len(E),
        "sumset_size": len(sums),
        "longest_run": run,
        "run_endpoints": endpoints,
        "run_over_p3": run / p**3
    }

for p in [5, 11, 17, 23, 29]:
    print(modular_block_probe(p))
```

The finite-extension claim can be probed as follows:

```python
def safe_k_for_shifts(M, K):
    """
    Finds k in [-K,K] such that m-k^3 is not a cube difference
    for every m in M.
    """
    for k in range(-K, K + 1):
        if all(not is_cube_difference(m - k**3) for m in M):
            return k
    return None

# Single noncube shifts
for m in range(-30, 31):
    if not is_cube_difference(m):  # optional filter, not cube test
        k = safe_k_for_shifts([m], 100)
        print(m, k)

# More relevant random finite sets M containing no cubes:
tests = [
    [2, 3],
    [2, 9, 10],
    [-2, 2, 9],
    [3, 6, 9, 12],
]
for M in tests:
    print(M, safe_k_for_shifts(M, 500))
```

A modular obstruction search for the same claim:

```python
def cube_residues(q):
    return {pow(x, 3, q) for x in range(q)}

def cube_difference_residues(q):
    C = cube_residues(q)
    return {(x - y) % q for x in C for y in C}

def simultaneous_safe_residues(M, q):
    D = cube_difference_residues(q)
    return [
        k for k in range(q)
        if all((m - pow(k, 3, q)) % q not in D for m in M)
    ]

for q in range(2, 200):
    safe = simultaneous_safe_residues([2, 9], q)
    if safe:
        print("modulus", q, "safe residues", safe[:20])
```

## Route Diagnosis

The useful part of Route 1 is the finite reduction
\[
I\subseteq B_I\oplus E_I,
\qquad E_I\subseteq f(\mathbb Z),
\]
together with the sharp critical estimates
\[
|B_I|\gg L^{1-1/d},
\qquad
|E_I|\gg L^{1/d}.
\]
What fails is the hoped-for extremal gap: for cubes, \(L^{2/3}\)-sized difference-free sets really exist, with the same leading constant furnished by the simplest coverage estimate. Nonlocality remains completely uncontrolled, and even infinitely many localized critical chunks are compatible with avoiding all cube differences.

A fresh Route 1 attempt should not seek merely a stronger independence-number estimate. It should study the additional interval-containment condition \(I\subseteq B\oplus E\) and classify near-critical finite direct pairs with \(E\) contained in a polynomial image. For cubes, the progressions \(B_p\) and the fact that cubing permutes residues modulo \(p\equiv2\pmod3\) suggest a stability theorem with a modular or \(p\)-adic component. This naturally merges Route 1 with Route 4: determine whether the critical modular blocks can be coherently nested across scales. The alternative constructive finite-extension claim is also precise and potentially decisive, but it is presently blocked by nontrivial Diophantine questions about
\[
m=k^3+x^3-y^3.
\]