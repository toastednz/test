STATUS: BLOCKED

## Result

I did not resolve Erdős Problem #196. For Route 2, I established an exact arrival-band counting identity, isolated precisely what the order-type-\(\omega\) condition contributes, and proved a quantitative \(U^3\)-uniformity criterion: sufficiently arithmetically uniform arrival quartiles force an ordered rainbow four-term progression. Conversely, every finite avoiding order has a uniformly positive \(U^3\)-bias in at least one arrival quartile. I also constructed a genuine permutation whose nested quartile colorings avoid the desired rainbow pattern at every \(4\)-adic scale, showing that balance, nesting, and fairness alone do not suffice. Finally, I proved that a broad class of natural digitwise/hierarchical constructions always fails because of an explicit carry-generated increasing four-AP. The unresolved structured case—large \(U^3\)-bias persisting coherently through all scales—is essentially as hard as the original problem.

## Complete Argument

### 1. Exact arrival-band formulation

Let \(\prec\) be a total order on \([N]\), and let
\[
r(v)=1+\#\{u\in[N]:u\prec v\}
\]
be its rank. For thresholds
\[
1\le t_1<t_2<t_3\le N-1,
\]
define four consecutive arrival bands
\[
\begin{aligned}
C_0&=\{v:r(v)\le t_1\},\\
C_1&=\{v:t_1<r(v)\le t_2\},\\
C_2&=\{v:t_2<r(v)\le t_3\},\\
C_3&=\{v:t_3<r(v)\}.
\end{aligned}
\]

Let \(Q_+(t_1,t_2,t_3)\) count pairs \((a,d)\) with \(a+3d\le N\) such that
\[
a\in C_0,\quad a+d\in C_1,\quad a+2d\in C_2,\quad a+3d\in C_3.
\]
Define \(Q_-\) analogously with the bands in reverse order.

Then
\[
\begin{aligned}
\sum_{t_1<t_2<t_3}Q_+(t_1,t_2,t_3)
={}&\sum_{\substack{a+3d\le N\\
r(a)<r(a+d)<r(a+2d)<r(a+3d)}}
\prod_{j=0}^{2}\bigl(r(a+(j+1)d)-r(a+jd)\bigr),
\end{aligned}
\tag{1}
\]
and similarly
\[
\begin{aligned}
\sum_{t_1<t_2<t_3}Q_-(t_1,t_2,t_3)
={}&\sum_{\substack{a+3d\le N\\
r(a)>r(a+d)>r(a+2d)>r(a+3d)}}
\prod_{j=0}^{2}\bigl(r(a+jd)-r(a+(j+1)d)\bigr).
\end{aligned}
\tag{2}
\]

#### Proof

Fix a four-AP with ranks
\[
r_0<r_1<r_2<r_3.
\]
It lies in \(C_0,C_1,C_2,C_3\), respectively, exactly when
\[
r_0\le t_1<r_1,\qquad
r_1\le t_2<r_2,\qquad
r_2\le t_3<r_3.
\]
There are
\[
(r_1-r_0)(r_2-r_1)(r_3-r_2)
\]
such threshold triples, and their required ordering is automatic. This proves (1). Reversing the ranks proves (2). ∎

Consequently, a finite order avoids monotone four-APs if and only if every one of these ordered transversal counts is zero. Thus Route 2 is exact if all thresholds are retained. Restricting attention to four equal quantiles loses information: monotone ranks may lie in bands with repetitions such as \(1,1,3,3\).

---

### 2. What order type \(\omega\) says in quantile language

Let \(p:\mathbb N\to\mathbb N\) be a permutation and, for \(n\le N\), let
\[
r_N(n)=\#\{m\le N:p(m)\le p(n)\}.
\]
Then
\[
r_N(n)\le p(n).
\tag{3}
\]

Indeed, globally there are exactly \(p(n)\) values whose positions are at most \(p(n)\), and the set counted by \(r_N(n)\) is a subset of them.

It follows that for every fixed finite set \(F\subset\mathbb N\) and every fixed number \(q\) of quantiles, all elements of \(F\) eventually lie in the first relative \(q\)-quantile of \([N]\). It is enough to take \(N\) so large that
\[
\left\lfloor\frac Nq\right\rfloor\ge \max_{n\in F}p(n).
\]

More exactly, for an arbitrary total order \(\prec\) on \(\mathbb N\),
\[
\sup_N r_N(n)<\infty\quad\text{for every }n
\tag{4}
\]
is equivalent to \(\prec\) having order type \(\omega\).

#### Proof

The supremum in (4) equals one plus the total number of predecessors of \(n\). Hence (4) says every element has finitely many predecessors. The rank map
\[
n\longmapsto \#\{m:m\prec n\}
\]
is then an order-preserving injection into \(\mathbb N_0\). Its image is an infinite initial segment of \(\mathbb N_0\), hence all of \(\mathbb N_0\). Therefore the order has type \(\omega\). The converse is immediate. ∎

The weaker normalized condition
\[
\frac{r_N(n)}N\longrightarrow0
\tag{5}
\]
does not characterize order type \(\omega\). To see this, identify \(\mathbb N_0\) with pairs \((k,j)\in\mathbb N_0^2\) using the Cantor pairing function, and order pairs lexicographically:
\[
(k,j)\prec(k',j')\iff k<k'\ \text{or}\ (k=k'\text{ and }j<j').
\]
This order has type \(\omega^2\). For fixed \(k\), only \(O_k(\sqrt N)\) elements of the first \(k\) rows have natural label at most \(N\), so every fixed element satisfies (5), even though every element in a row \(k\ge1\) has infinitely many predecessors.

Thus fixed-density quantile data sees only zero-density predecessor sets, not the essential finite-predecessor condition.

---

### 3. Balanced ordered-rainbow statements are false even under strong nesting

On \([4m]\), split the numerical interval into four consecutive blocks \(I_0,I_1,I_2,I_3\), each of size \(m\), and give them arrival colors
\[
1,3,2,4
\tag{6}
\]
in numerical order.

This is a balanced coloring, but no increasing four-tuple—hence no increasing four-AP—has colors \(1,2,3,4\): color \(2\) lies numerically after color \(3\). Nor can an increasing tuple have colors \(4,3,2,1\), since color \(4\) occupies the last numerical block.

These colorings can be made consistent across infinitely many scales by one genuine permutation. Work first on \(\mathbb N_0\). Let
\[
\phi(0)=0,\qquad \phi(1)=2,\qquad \phi(2)=1,\qquad \phi(3)=3.
\]
For the base-four expansion
\[
n=\sum_{j\ge0}\varepsilon_j4^j,
\]
define
\[
P(n)=\sum_{j\ge0}\phi(\varepsilon_j)4^j.
\tag{7}
\]
Since \(\phi\) is a permutation fixing zero, \(P\) is a bijection of \(\mathbb N_0\). Hence
\[
p(n)=P(n-1)+1
\tag{8}
\]
is a permutation of \(\mathbb N\).

For every \(k\),
\[
P\bigl([0,4^k-1]\bigr)=[0,4^k-1].
\]
Therefore the first \(4^k\) positions contain exactly the values \(1,\dots,4^k\). In the four numerical quarters of this interval, the leading base-four digit is \(0,1,2,3\), while its transformed digit is \(0,2,1,3\). Thus the relative arrival quartile colors are exactly
\[
1,3,2,4.
\]
Moreover,
\[
P(h4^k+r)=P(h)4^k+P(r)\qquad(0\le r<4^k),
\]
so the same pattern occurs inside every aligned \(4\)-adic interval at every depth.

Nevertheless, this is not a counterexample to the original problem. Indeed,
\[
P(2)=1,\quad P(3)=3,\quad P(4)=8,\quad P(5)=10,
\]
and therefore
\[
p(3)=2<p(4)=4<p(5)=9<p(6)=11.
\]
Thus \(3,4,5,6\) is a monotone four-AP. At the \(N=16\) quartile scale its color pattern is \(1,1,3,3\), not an ordered rainbow. This demonstrates rigorously that recursively excluding only strict four-color rainbows cannot suffice.

---

### 4. A carry obstruction to digitwise and simple substitution constructions

The previous construction fails for a general reason.

#### Proposition

Let \(B\ge2\). For each digit position \(j\), let
\[
\phi_j:\{0,\dots,B-1\}\to\{0,\dots,B-1\}
\]
be a permutation satisfying \(\phi_j(0)=0\). Define
\[
P\left(\sum_{j\ge0}\varepsilon_jB^j\right)
 =\sum_{j\ge0}\phi_j(\varepsilon_j)B^j.
\tag{9}
\]
Then the permutation \(p(n)=P(n-1)+1\) contains an increasing four-term arithmetic progression.

#### Proof

For \(B=2\), every \(\phi_j\) is the identity, so \(P\) is the identity.

Assume \(B\ge3\), and put
\[
A=B^2-B,\qquad D=B-1.
\]
The four terms have base-\(B\) expansions
\[
\begin{aligned}
A&=(0,B-1,0)_B,\\
A+D&=(0,B-1,B-1)_B,\\
A+2D&=(1,0,B-2)_B,\\
A+3D&=(1,1,B-3)_B.
\end{aligned}
\]
First,
\[
P(A+D)-P(A)=\phi_0(B-1)>0.
\]
Also,
\[
P(A+D)\le B(B-1)+(B-1)=B^2-1,
\]
while
\[
P(A+2D)\ge B^2\phi_2(1)\ge B^2.
\]
Finally,
\[
\begin{aligned}
P(A+3D)-P(A+2D)
 &=B\phi_1(1)+\phi_0(B-3)-\phi_0(B-2)\\
 &\ge B-(B-1)=1.
\end{aligned}
\]
Hence
\[
P(A)<P(A+D)<P(A+2D)<P(A+3D).
\]
After translating from \(\mathbb N_0\) to \(\mathbb N\), the progression starts at \(A+1\) and has difference \(D\). ∎

This rules out not only a fixed digit permutation but position-dependent coordinatewise digit permutations. The obstruction is a two-level carry. It also rules out homogeneous recursive block orders in which the numerical zero-child is always listed first.

---

### 5. The arithmetically uniform quantile case is solvable

The next result gives a rigorous positive theorem for Route 2’s pseudorandom regime.

Let \(G=\mathbb Z/q\mathbb Z\), where \(q>3\) is prime. For \(f:G\to\mathbb C\), define
\[
\|f\|_{U^3(G)}^8
 =
 \mathbb E_{x,h_1,h_2,h_3}
 \prod_{\omega\in\{0,1\}^3}
 \mathcal C^{|\omega|}
 f(x+\omega_1h_1+\omega_2h_2+\omega_3h_3).
\]

For bounded functions \(f_0,\dots,f_3\), put
\[
\Lambda(f_0,f_1,f_2,f_3)
 =
 \mathbb E_{x,d\in G}\prod_{j=0}^3 f_j(x+jd).
\]

#### Generalized von Neumann inequality

If \(|f_j|\le1\), then
\[
|\Lambda(f_0,f_1,f_2,f_3)|
 \le \min_{0\le i\le3}\|f_i\|_{U^3(G)}.
\tag{10}
\]

#### Proof

Write \(L_j(x,d)=x+jd\). Fix \(i\). For each \(j\ne i\), choose
\[
v_j=(j,-1)\in G^2.
\]
Then
\[
L_j(v_j)=0,\qquad L_i(v_j)=j-i\ne0.
\]
Apply Cauchy–Schwarz successively along the three one-dimensional directions \(v_j\). At the step corresponding to \(j\), every copy of \(f_j(L_j(x,d))\) is invariant under translation in direction \(v_j\); it becomes a modulus square and is bounded by \(1\). After the three applications, only the eight cube copies of \(f_i\) remain. Since each scalar \(L_i(v_j)=j-i\) is nonzero, rescaling the three increment variables is bijective in \(G\). The resulting eighth power is exactly \(\|f_i\|_{U^3}^8\). This proves (10). ∎

Now embed
\[
I=\{0,\dots,N-1\}
\]
in \(G\), with \(q>2N\). Let \(C_0,C_1,C_2,C_3\) partition \(I\), and put
\[
\alpha_i=\frac{|C_i|}{N},\qquad
h_i=1_{C_i}-\alpha_i1_I.
\]
A telescoping replacement of \(1_{C_i}\) by \(\alpha_i1_I\), together with (10), gives
\[
\left|
\Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})
-\left(\prod_{i=0}^3\alpha_i\right)
 \Lambda(1_I,1_I,1_I,1_I)
\right|
\le\sum_{i=0}^3\|h_i\|_{U^3}.
\tag{11}
\]

Let
\[
H_N=N+2\sum_{d=1}^{\lfloor(N-1)/3\rfloor}(N-3d).
\tag{12}
\]
This is exactly the number of integer pairs \((a,d)\), allowing positive, zero, and negative \(d\), for which
\[
a,a+d,a+2d,a+3d\in I.
\]
Because \(q>2N\), any modular progression supported in \(I\) lifts uniquely to such an integer progression. Hence
\[
\Lambda(1_I,1_I,1_I,1_I)=\frac{H_N}{q^2}.
\tag{13}
\]

Suppose \(C_0,C_1,C_2,C_3\) are consecutive arrival bands. If
\[
\sum_{i=0}^3\|h_i\|_{U^3}
<
\left(\prod_{i=0}^3\alpha_i\right)\frac{H_N}{q^2},
\tag{14}
\]
then (11) implies
\[
\Lambda(1_{C_0},1_{C_1},1_{C_2},1_{C_3})>0.
\]
The contributing common difference cannot be zero because the \(C_i\) are disjoint. A positive integer difference gives an increasing-arrival four-AP. A negative difference, after reversing the numerical progression, gives a decreasing-arrival four-AP. Thus (14) forces the desired configuration.

For equal quartiles, \(\alpha_i=1/4\). Therefore every avoiding order on \([N]\), with \(4\mid N\), must satisfy
\[
\max_i\left\|1_{C_i}-\frac14 1_I\right\|_{U^3}
\ge \frac{H_N}{1024q^2}.
\tag{15}
\]

For completeness, writing \(N=3m,3m+1,3m+2\) in (12) gives respectively
\[
H_N=
3m^2,\qquad
3m^2+2m+1,\qquad
3m^2+4m+2,
\]
so
\[
H_N\ge \frac{N^2}{3}.
\tag{16}
\]
By Bertrand’s postulate, one may choose a prime
\[
2N<q<4N.
\]
Then (15) implies the absolute lower bound
\[
\max_i\left\|1_{C_i}-\frac14 1_I\right\|_{U^3}
>\frac1{49152}.
\tag{17}
\]

Thus every avoiding finite order has a quantitatively nonuniform arrival quartile at every balanced scale.

This is the strongest positive conclusion obtained from Route 2: the quasirandom case is completely handled, but the structured case remains.

## Self-Audit

1. **The \(U^3\) criterion does not apply automatically to arbitrary permutations.**  
   Nothing proved here shows that some arrival scale must have small \(U^3\)-discrepancy. In fact, block-structured permutations can have large discrepancy on infinitely many scales. The finite inequality itself is rigorous; its limitation is applicability, not validity.

2. **The nested base-four construction only defeats coarse rainbow arguments, not every conceivable multiscale theorem.**  
   It contains an actual monotone four-AP, so a sufficiently refined argument could detect it. What it proves is precisely that equal quartiles, nesting, one-point arrival consistency, and order type \(\omega\) do not by themselves force a strict \(1234\) or \(4321\) color pattern at the selected scales.

3. **The digitwise obstruction covers a broad but restricted construction class.**  
   Prefix-dependent substitutions whose local block orders vary with the entire prefix are not covered. The explicit carry calculation is valid for all coordinatewise digit permutations fixing zero, but extrapolating it to arbitrary hierarchical constructions would be unjustified.

## Computations To Verify

```python
from itertools import permutations
from random import shuffle

def aps(N):
    for d in range(1, (N - 1) // 3 + 1):
        for a in range(1, N - 3*d + 1):
            yield a, d

# ------------------------------------------------------------
# 1. Verify the threshold identity.
# order is a list containing 1,...,N in arrival order.
# ------------------------------------------------------------

def threshold_identity(order):
    N = len(order)
    rank = {v: i+1 for i, v in enumerate(order)}

    rhs_plus = rhs_minus = 0
    for a, d in aps(N):
        rr = [rank[a+j*d] for j in range(4)]
        if rr[0] < rr[1] < rr[2] < rr[3]:
            rhs_plus += ((rr[1]-rr[0]) *
                         (rr[2]-rr[1]) *
                         (rr[3]-rr[2]))
        if rr[0] > rr[1] > rr[2] > rr[3]:
            rhs_minus += ((rr[0]-rr[1]) *
                          (rr[1]-rr[2]) *
                          (rr[2]-rr[3]))

    lhs_plus = lhs_minus = 0
    for t1 in range(1, N):
        for t2 in range(t1+1, N):
            for t3 in range(t2+1, N):
                def color(v):
                    r = rank[v]
                    if r <= t1:
                        return 0
                    if r <= t2:
                        return 1
                    if r <= t3:
                        return 2
                    return 3

                for a, d in aps(N):
                    cc = [color(a+j*d) for j in range(4)]
                    lhs_plus += (cc == [0, 1, 2, 3])
                    lhs_minus += (cc == [3, 2, 1, 0])

    return (lhs_plus, rhs_plus, lhs_minus, rhs_minus)

for N in range(4, 10):
    order = list(range(1, N+1))
    shuffle(order)
    assert threshold_identity(order)[0] == threshold_identity(order)[1]
    assert threshold_identity(order)[2] == threshold_identity(order)[3]

# ------------------------------------------------------------
# 2. Base-four nested permutation and its first violation.
# ------------------------------------------------------------

phi4 = (0, 2, 1, 3)

def digit_permutation(n, B, phi):
    ans = 0
    place = 1
    while n:
        digit = n % B
        ans += phi[digit] * place
        n //= B
        place *= B
    return ans

def p4(n):  # positive-integer rank permutation
    return digit_permutation(n-1, 4, phi4) + 1

def first_violation(p, N):
    for a, d in aps(N):
        rr = [p(a+j*d) for j in range(4)]
        if rr == sorted(rr) or rr == sorted(rr, reverse=True):
            return a, d, rr
    return None

assert first_violation(p4, 20) == (3, 1, [2, 4, 9, 11])

for k in range(1, 6):
    N = 4**k
    block = N // 4
    colors = [
        digit_permutation(z, 4, phi4) // block + 1
        for z in range(N)
    ]
    expected = [1, 3, 2, 4]
    for j in range(4):
        assert all(c == expected[j]
                   for c in colors[j*block:(j+1)*block])

    for a, d in aps(N):
        cc = [colors[a-1+j*d] for j in range(4)]
        assert cc != [1, 2, 3, 4]
        assert cc != [4, 3, 2, 1]

# ------------------------------------------------------------
# 3. Verify the universal digit-carry witness for constant
#    digit permutations in small bases.
# ------------------------------------------------------------

for B in range(3, 9):
    for tail in permutations(range(1, B)):
        phi = (0,) + tail
        A = B*B - B
        D = B - 1
        vals = [digit_permutation(A+j*D, B, phi) for j in range(4)]
        assert vals[0] < vals[1] < vals[2] < vals[3]

# ------------------------------------------------------------
# 4. Numerically check the U^3 telescoping inequality.
# ------------------------------------------------------------

def u3_norm(f, q):
    total = 0j
    for x in range(q):
        for h1 in range(q):
            for h2 in range(q):
                for h3 in range(q):
                    prod = 1+0j
                    hs = (h1, h2, h3)
                    for mask in range(8):
                        y = x
                        parity = 0
                        for j in range(3):
                            if (mask >> j) & 1:
                                y += hs[j]
                                parity ^= 1
                        val = f[y % q]
                        if parity:
                            val = val.conjugate()
                        prod *= val
                    total += prod
    value = total.real / (q**4)
    return max(value, 0.0)**(1/8)

def lambda4(fs, q):
    total = 0j
    for x in range(q):
        for d in range(q):
            prod = 1+0j
            for j in range(4):
                prod *= fs[j][(x+j*d) % q]
            total += prod
    return total / (q*q)

N, q = 8, 17
block = N // 4
numeric_block_color = [0, 2, 1, 3]

classes = [set() for _ in range(4)]
for x in range(N):
    classes[numeric_block_color[x // block]].add(x)

indicators = []
errors = []
for i in range(4):
    ind = [1.0 if x in classes[i] else 0.0 for x in range(q)]
    base = [0.25 if x < N else 0.0 for x in range(q)]
    indicators.append(ind)
    errors.append([ind[x] - base[x] for x in range(q)])

I = [1.0 if x < N else 0.0 for x in range(q)]
lhs = abs(lambda4(indicators, q) -
          (0.25**4) * lambda4([I, I, I, I], q))
rhs = sum(u3_norm(h, q) for h in errors)
assert lhs <= rhs + 1e-10
```

## Route Diagnosis

### Proved ledger

1. All monotone four-APs are counted exactly by ordered transversals through all triples of nested arrival thresholds.
2. Order type \(\omega\) is equivalent to uniformly bounded finite-restriction rank for each fixed value; fixed-quantile migration alone is strictly weaker.
3. Balanced four-color ordered-rainbow statements fail even for colorings arising coherently from a genuine permutation at every \(4\)-adic scale.
4. Coordinatewise digit permutations, even with position-dependent digit maps, always contain an explicit increasing four-AP generated by carries.
5. \(U^3\)-quasirandom arrival layers force the desired progression. Hence every avoiding finite order has an absolute amount of \(U^3\)-structure in at least one quartile.

### Plausible but unproved

A completion of Route 2 would require a structured-case theorem roughly of the following form:

> If every balanced arrival partition of a single order has a large \(U^3\)-structured component, and these partitions are nested through all scales with every element having finitely many predecessors, then some four-AP has monotone ranks.

No compatible inverse theorem or density-increment mechanism was obtained. Standard \(U^3\) inverse theory only gives correlation with scale-dependent quadratic structure; it does not make the structures at different arrival scales compatible, preserve the ordered layer labels under restriction, or exploit finite predecessor counts.

### Dead ends

- An arbitrary balanced ordered-rainbow theorem is false by the block coloring \(1,3,2,4\).
- Requiring such colorings to arise at infinitely many nested scales from one permutation is still insufficient, as shown by the base-four construction.
- Normalized quantile migration does not encode order type \(\omega\).
- Straight digit substitutions are killed by the explicit carry progression.
- A naive density increment has no monotone energy: after restricting to a structured region, the four arrival layers need not remain balanced or consecutive.

A fresh attempt should either:

1. develop an arithmetic regularity/inverse theorem simultaneously for the entire nested family of arrival bands, while retaining the absolute bounded-predecessor information; or
2. move to prefix-dependent finite-state substitutions and classify all carry states, with the carry obstruction above used as a mandatory regression test.

At present, handling the persistent structured case is a problem of comparable strength to Erdős Problem #196 itself, so Route 2 is blocked rather than completed.