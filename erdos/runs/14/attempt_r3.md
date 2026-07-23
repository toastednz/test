STATUS: BLOCKED

## Result

Route 3 yields a rigorous Fourier obstruction for **balanced cyclic sum systems**. If \(S\subseteq \mathbb Z/q\mathbb Z\), \(q\) is odd, \(|S|=k\), and the total number \(\binom{k+1}{2}\) of unordered pairs is within \(o(k)\) of \(\lambda q\), then at least \((1/(2\lambda)-o(1))k\) residues fail to have exactly \(\lambda\) unordered representations. In particular, when \(\binom{k+1}{2}=q+o(k)\), at least \((1/2-o(1))k=\Omega(\sqrt q)\) residues fail to have exactly one representation. I also prove an exact interval-to-cyclic transference lemma. However, applying it to \(X=A\cap[1,N]\) introduces an uncontrolled set of upper-half sums whose unique representation uses an element exceeding \(N\). Naive projection instead produces modular representation counts \(1\) or \(2\), and such cyclic systems can exist perfectly even in small examples. Thus neither Q1 nor Q2 is resolved; the precise block is a missing multiscale “representation-capture” theorem.

## Complete Argument

### 1. Cyclic representation functions

Let \(G=\mathbb Z/q\mathbb Z\), with \(q\) odd, and let \(S\subseteq G\), \(|S|=k\). Define the cyclic unordered representation function
\[
R_S(x)=\#\{\{s,t\}\subseteq S:s+t=x\},
\]
where a diagonal pair \(\{s,s\}\) is permitted.

The total number of unordered pairs is
\[
P:=\sum_{x\in G}R_S(x)=\frac{k(k+1)}2.
\]

For a fixed positive integer \(\lambda\), put
\[
u(x)=R_S(x)-\lambda,
\qquad
e_\lambda(S)=\#\{x\in G:u(x)\ne0\}.
\]

We first derive a support-sensitive cyclic inequality.

---

### 2. Fourier identity

Let \(f=1_S\), and use the unnormalized Fourier transform
\[
\widehat g(t)=\sum_{x\in G}g(x)e^{-2\pi itx/q}.
\]
Parseval is
\[
\sum_{t\in G}|\widehat g(t)|^2
=
q\sum_{x\in G}|g(x)|^2.
\]

Let
\[
C(x)=(f*f)(x)=\#\{(s,t)\in S^2:s+t=x\}
\]
be the ordered convolution, and define
\[
D(x)=1_S(x/2),
\]
where \(x/2\) is well-defined because \(q\) is odd.

Every off-diagonal unordered representation contributes two ordered representations, while every diagonal contributes one ordered representation and one unit to \(D\). Hence
\[
2R_S(x)=C(x)+D(x).
\]
Moreover,
\[
\widehat C(t)=\widehat f(t)^2,
\qquad
\widehat D(t)=\widehat f(2t).
\]
Therefore, for every nonzero \(t\in G\),
\[
2\widehat u(t)
=
\widehat f(t)^2+\widehat f(2t).
\tag{2.1}
\]

This identity retains the diagonal term exactly.

---

### 3. A Fourier lower bound for the coefficient defect

Put
\[
V=qk-k^2.
\]
Since \(\widehat f(0)=k\), Parseval gives
\[
\sum_{t\ne0}|\widehat f(t)|^2=V.
\tag{3.1}
\]

By Cauchy–Schwarz,
\[
\sum_{t\ne0}|\widehat f(t)|^4
\ge
\frac{V^2}{q-1}.
\tag{3.2}
\]
Thus
\[
\left\|(\widehat f(t)^2)_{t\ne0}\right\|_2
\ge
\frac{V}{\sqrt{q-1}}.
\tag{3.3}
\]

Because multiplication by \(2\) permutes the nonzero residues modulo odd \(q\),
\[
\left\|(\widehat f(2t))_{t\ne0}\right\|_2
=
\sqrt V.
\tag{3.4}
\]

Applying the reverse triangle inequality to (2.1),
\[
2\left(\sum_{t\ne0}|\widehat u(t)|^2\right)^{1/2}
\ge
\left(
\frac{V}{\sqrt{q-1}}-\sqrt V
\right)_+.
\]
Using Parseval for \(u\), we obtain the exact inequality
\[
\boxed{
\sum_{x\in G}u(x)^2
\ge
\Lambda(q,k):=
\frac1{4q}
\left(
\frac{V}{\sqrt{q-1}}-\sqrt V
\right)_+^2.
}
\tag{3.5}
\]

This is the main Fourier input.

---

### 4. Conversion from \(L^2\)-defect to support in the balanced case

For fixed \(x\), the map \(s\mapsto x-s\) is an involution on \(G\), with exactly one fixed point. Its orbits contributing representations use either one or two elements of \(S\). Consequently,
\[
R_S(x)\le \left\lceil\frac{k}{2}\right\rceil.
\tag{4.1}
\]

Let
\[
d=P-\lambda q=\sum_x u(x).
\]
Write
\[
T_+=\sum_{u(x)>0}u(x),
\qquad
T_-=\sum_{u(x)<0}(-u(x)).
\]
Then
\[
T_+-T_-=d.
\tag{4.2}
\]

At a negative site, \(-u(x)\le\lambda\), so
\[
T_-\le \lambda e_\lambda(S).
\tag{4.3}
\]
Thus
\[
T_+\le |d|+\lambda e_\lambda(S).
\tag{4.4}
\]

The negative values satisfy
\[
\sum_{u<0}u(x)^2\le \lambda T_-\le \lambda^2 e_\lambda(S),
\]
while, by (4.1),
\[
\sum_{u>0}u(x)^2
\le
\left\lceil\frac k2\right\rceil T_+
\le
\left\lceil\frac k2\right\rceil
\bigl(|d|+\lambda e_\lambda(S)\bigr).
\]
Therefore
\[
\sum_xu(x)^2
\le
\left(
\lambda^2+\lambda\left\lceil\frac k2\right\rceil
\right)e_\lambda(S)
+
\left\lceil\frac k2\right\rceil |d|.
\tag{4.5}
\]

Combining (3.5) and (4.5) proves the following explicit bound.

#### Theorem 4.1: balanced cyclic defect theorem

For odd \(q\), \(S\subseteq\mathbb Z/q\mathbb Z\), \(|S|=k\), and fixed \(\lambda\ge1\),
\[
\boxed{
e_\lambda(S)
\ge
\frac{
\Lambda(q,k)
-
\lceil k/2\rceil\,|P-\lambda q|
}{
\lambda^2+\lambda\lceil k/2\rceil
},
}
\tag{4.6}
\]
whenever the right side is positive.

In particular, suppose \(k\to\infty\), \(\lambda\) is fixed, and
\[
P-\lambda q=o(k).
\tag{4.7}
\]
Since \(P=k(k+1)/2\), this implies
\[
q=\left(\frac1{2\lambda}+o(1)\right)k^2.
\]
Then
\[
V=qk-k^2
=
\left(\frac1{2\lambda}+o(1)\right)k^3.
\]
Hence
\[
\frac{V}{\sqrt{q-1}}
=
\left(\frac1{\sqrt{2\lambda}}+o(1)\right)k^2,
\qquad
\sqrt V=O(k^{3/2}),
\]
and consequently
\[
\Lambda(q,k)=\left(\frac14-o(1)\right)k^2.
\]
Substitution in (4.6) gives
\[
\boxed{
e_\lambda(S)
\ge
\left(\frac1{2\lambda}-o(1)\right)k.
}
\tag{4.8}
\]

For \(\lambda=1\):

#### Corollary 4.2

If
\[
\frac{k(k+1)}2=q+o(k)
\]
and \(q\) is odd, then
\[
\#\{x\in\mathbb Z/q\mathbb Z:R_S(x)\ne1\}
\ge
\left(\frac12-o(1)\right)k
=
\Omega(\sqrt q).
\tag{4.9}
\]

Thus a balanced near-perfect cyclic unordered sum system cannot have \(o(\sqrt q)\) exceptional residues.

The balance hypothesis is essential to this proof. Without it, the term
\[
\left\lceil\frac k2\right\rceil |P-\lambda q|
\]
can absorb the entire Fourier lower bound.

---

### 5. Exact interval-to-cyclic transference

Let \(X\) be a finite set of \(k\) integers. Write
\[
a=\min X,\qquad a+L=\max X,
\]
so that \(L\) is the diameter of \(X\). Its possible integer pair sums lie in the consecutive interval
\[
I=[2a,2a+2L],
\qquad |I|=H:=2L+1.
\]
Let
\[
\rho_X(n)=\#\{x\le y:x,y\in X,\ x+y=n\}.
\]
Define the full-hull defect
\[
B_X(I)=\#\{n\in I:\rho_X(n)\ne1\}.
\]

Let \(q\) be odd and suppose
\[
q>L.
\tag{5.1}
\]
Then reduction modulo \(q\) is injective on \(X\). Let \(S=X\bmod q\). Every unordered pair of elements of \(X\) corresponds bijectively to an unordered pair of elements of \(S\), and hence
\[
R_S(r)
=
\sum_{\substack{n\in I\\n\equiv r\pmod q}}\rho_X(n).
\tag{5.2}
\]

Fix \(\lambda\ge1\), and suppose
\[
|H-\lambda q|<q.
\tag{5.3}
\]
Since \(I\) consists of consecutive integers, exactly
\[
|H-\lambda q|
\]
residue classes have a number of representatives in \(I\) different from \(\lambda\). Every other residue class contains exactly \(\lambda\) integers from \(I\).

If such a regular residue class contains no integer \(n\) with \(\rho_X(n)\ne1\), equation (5.2) gives \(R_S(r)=\lambda\). Therefore
\[
e_\lambda(S)
\le
B_X(I)+|H-\lambda q|.
\tag{5.4}
\]

Combining this with Theorem 4.1 gives:

#### Theorem 5.1: interval transference theorem

Under (5.1), (5.3), and
\[
P-\lambda q=o(k),
\]
one has
\[
\boxed{
B_X(I)+|2L+1-\lambda q|
\ge
\left(\frac1{2\lambda}-o(1)\right)k.
}
\tag{5.5}
\]

For example, take \(\lambda=1\) and let \(q\) be the odd integer equal to \(P\) or \(P-1\). If \(q>L\), then
\[
B_X(I)+|2L+1-q|
\ge
\left(\frac12-o(1)\right)k.
\tag{5.6}
\]

Thus if the number of available pair sums \(P\) is balanced with the length \(2L+1\) of the sum hull, the hull must contain \(\Omega(k)\) failures of exact uniqueness.

---

### 6. What this says for prefixes of an infinite set

Let \(A\subseteq\mathbb N\) and
\[
X=A\cap[1,N].
\]
Let \(I=[2\min X,2\max X]\), assuming \(X\ne\varnothing\), and define the escaped-good-sum count
\[
W_A(N;I)
=
\#\left\{
n\in I:
\begin{array}{l}
r_A(n)=1,\ \text{and the unique representing pair}\\
\text{is not wholly contained in }X
\end{array}
\right\}.
\]
Because \(X\subseteq A\),
\[
\rho_X(n)\le r_A(n).
\]
If \(\rho_X(n)\ne1\), then either:

1. \(r_A(n)\ne1\), which is charged to \(E_A(2N)\); or
2. \(r_A(n)=1\) but its unique pair is not contained in \(X\), which is charged to \(W_A(N;I)\).

Since \(I\subseteq[2,2N]\),
\[
B_X(I)\le E_A(2N)+W_A(N;I).
\tag{6.1}
\]

Therefore Theorem 5.1 gives the rigorous conditional inequality
\[
\boxed{
E_A(2N)+W_A(N;I)+|2L+1-\lambda q|
\ge
\left(\frac1{2\lambda}-o(1)\right)|A\cap[1,N]|
}
\tag{6.2}
\]
whenever the cyclic balance and injectivity hypotheses hold.

This is the strongest direct consequence I obtained for the original problem. It exhibits the exact obstruction: even if \(E_A(2N)\) is tiny, the term \(W_A(N;I)\) can be large. For \(n>N\), the unique representation may use an element of \(A\cap(N,2N]\), so it is invisible in \(A\cap[1,N]\).

No estimate of the required strength for \(W_A(N;I)\) follows from small \(E_A(2N)\) alone.

---

### 7. Why naive modular projection fails

Take \(X=A\cap[1,q]\) and reduce it modulo \(q\). For a residue \(x\), cyclic representations can arise from integer pair sums \(x\) and \(x+q\). If both integer sums are uniquely represented inside \(X\), then the cyclic residue has two representations, not one.

This is not merely a technical annoyance. For example, in \(\mathbb Z/7\mathbb Z\), let
\[
S=\{0,1,2,4\}.
\]
Its unordered pair sums are
\[
0,1,2,4,2,3,5,4,6,1,
\]
so
\[
(R_S(0),\ldots,R_S(6))=(1,2,2,1,2,1,1).
\]
Every residue has either one or two representations. Hence no Fourier theorem forbidding systems that are pointwise in \(\{1,2\}\) can be true in general.

The cyclic Fourier theorem above applies to representations near a **fixed** value \(\lambda\), not to an uncontrolled residue-dependent mixture of one and two. In the interval problem, this mixture records whether the upper folded sum is represented internally or by a later block of \(A\).

## Self-Audit

1. **The Fourier theorem requires pair-count balance \(P-\lambda q=o(k)\).**  
   This is a substantial restriction, not a harmless normalization. Without it, the support bound (4.6) can be vacuous because a few residues can carry a large net excess. I believe the theorem itself is correct because both the Fourier lower bound (3.5) and the support upper bound (4.5) are exact inequalities; the restriction enters transparently in the final comparison.

2. **The interval transference controls the full sum hull, not the original exceptional set alone.**  
   For \(X=A\cap[1,N]\), the upper part of the hull may have unique global representations involving elements greater than \(N\), while \(\rho_X\) vanishes there. This is why the escaped term \(W_A(N;I)\) appears. The inequality is nevertheless valid: equation (5.2) is a direct bijective count, and (6.1) classifies every possible reason that \(\rho_X(n)\ne1\).

3. **The diagnosis that a multiscale capture theorem is needed is not itself a proof that Route 3 cannot work.**  
   A more sophisticated averaging over windows, moduli, or adjacent blocks could conceivably control the escaped representations. I have not ruled this out. I believe the stated block is genuine for the present argument because the explicit \(\mathbb Z/7\mathbb Z\) example disproves the simplest “one-or-two modular representations are impossible” replacement, while \(W_A(N;I)\) is not bounded by any quantity established here.

## Computations To Verify

The following exact brute-force code checks cyclic representation profiles and exhaustively tests the finite inequality underlying Theorem 4.1 for small odd moduli.

```python
from itertools import combinations
from math import sqrt, ceil

def cyclic_profile(q, S):
    S = sorted(S)
    r = [0] * q
    for i, a in enumerate(S):
        for b in S[i:]:
            r[(a + b) % q] += 1
    return r

def fourier_support_lower_bound(q, k, lam=1):
    """
    Returns the RHS of the explicit support bound (4.6).
    A negative value means that this particular estimate is vacuous.
    """
    P = k * (k + 1) // 2
    V = q * k - k * k
    if q <= 1 or V < 0:
        return float("-inf")

    Lambda = (
        max(0.0, V / sqrt(q - 1) - sqrt(V)) ** 2
        / (4.0 * q)
    )
    d = abs(P - lam * q)
    denom = lam * lam + lam * ceil(k / 2)
    return (Lambda - ceil(k / 2) * d) / denom

def verify_cyclic_bound(max_q=25, max_lambda=3):
    for q in range(3, max_q + 1, 2):
        for k in range(1, q + 1):
            # Translation preserves the representation histogram,
            # so it is enough to inspect sets containing 0.
            for rest in combinations(range(1, q), k - 1):
                S = (0,) + rest
                r = cyclic_profile(q, S)
                for lam in range(1, max_lambda + 1):
                    e = sum(v != lam for v in r)
                    lb = fourier_support_lower_bound(q, k, lam)
                    assert e + 1e-9 >= lb, (q, S, lam, e, lb)
    print("All cyclic checks passed.")

print(cyclic_profile(7, {0, 1, 2, 4}))
# Expected: [1, 2, 2, 1, 2, 1, 1]

verify_cyclic_bound()
```

The interval projection lemma can be checked exhaustively as follows.

```python
def integer_profile(X):
    X = sorted(X)
    lo = 2 * min(X)
    hi = 2 * max(X)
    rho = {n: 0 for n in range(lo, hi + 1)}
    for i, a in enumerate(X):
        for b in X[i:]:
            rho[a + b] += 1
    return lo, hi, rho

def verify_projection(max_L=10):
    for L in range(1, max_L + 1):
        interior = list(range(1, L))
        # Require both endpoints so the diameter is exactly L.
        for mask in range(1 << len(interior)):
            X = {0, L}
            for j, x in enumerate(interior):
                if (mask >> j) & 1:
                    X.add(x)

            lo, hi, rho = integer_profile(X)
            H = hi - lo + 1

            for q in range(L + 1, 3 * L + 6):
                if q % 2 == 0:
                    continue

                S = {x % q for x in X}
                assert len(S) == len(X)
                cyc = cyclic_profile(q, S)

                for lam in range(1, 4):
                    if abs(H - lam * q) >= q:
                        continue

                    B = sum(rho[n] != 1 for n in range(lo, hi + 1))
                    e_lam = sum(v != lam for v in cyc)

                    assert e_lam <= B + abs(H - lam * q), (
                        X, q, lam, B, e_lam
                    )
    print("All projection checks passed.")

verify_projection()
```

A useful exhaustive experiment is to compute
\[
\min_{|S|=k}e_1(S)
\]
for odd \(q\), grouped by the imbalance
\[
d=\binom{k+1}{2}-q.
\]
This tests whether a stronger cyclic theorem might hold without \(d=o(k)\).

```python
def cyclic_minima(max_q=25):
    output = []
    for q in range(3, max_q + 1, 2):
        for k in range(1, q + 1):
            best = q + 1
            best_S = None
            for rest in combinations(range(1, q), k - 1):
                S = (0,) + rest
                r = cyclic_profile(q, S)
                e = sum(v != 1 for v in r)
                if e < best:
                    best = e
                    best_S = S
            P = k * (k + 1) // 2
            output.append((q, k, P - q, best, best_S))
    return output

for row in cyclic_minima(17):
    q, k, d, best, S = row
    if abs(d) <= 2 * k:
        print(row)
```

The decisive data to record are:

- whether \(e_1(S)/k\) stays bounded below when \(P-q\) is intermediate between \(k\) and \(k^2\);
- the maximum exceptional multiplicity;
- whether near-minimizers concentrate almost all excess pairs on one or a few residues;
- whether the bad residues form reflection centers with strong additive structure.

## Route Diagnosis

**Proved ledger.**

1. The exact cyclic Fourier identity
   \[
   2\widehat{(R_S-\lambda)}(t)
   =
   \widehat{1_S}(t)^2+\widehat{1_S}(2t),
   \qquad t\ne0.
   \]
2. The quantitative \(L^2\)-defect lower bound (3.5).
3. The balanced cyclic theorem
   \[
   e_\lambda(S)\ge\left(\frac1{2\lambda}-o(1)\right)|S|
   \]
   when \(\binom{|S|+1}{2}-\lambda q=o(|S|)\).
4. The exact interval-to-cyclic transference inequality
   \[
   e_\lambda(S)\le B_X(I)+||I|-\lambda q|.
   \]
5. The conditional prefix inequality (6.2), isolating the escaped-representation term.

**Plausible but unproved.**

- A multiscale theorem may force the escaped upper-half representations at one scale to create modular or interval collisions at a later scale.
- A stronger cyclic theorem might hold without pair-count balance, but the present Fourier-to-support conversion cannot prove it.
- The masks identifying whether a folded upper sum is represented internally are not arbitrary; exploiting their cross-block convolution structure may restore a Fourier obstruction.

**Dead ends.**

1. **Naive projection modulo \(q\).** It folds sums \(n\) and \(n+q\), producing representation counts \(1\) or \(2\), not near-constant \(1\).
2. **Forbidding pointwise \(\{1,2\}\)-valued cyclic profiles.** This is false, as shown by \(S=\{0,1,2,4\}\subseteq\mathbb Z/7\mathbb Z\).
3. **Parseval without pair-count balance.** A small exceptional support can carry a net excess as large as \(O(k)\) per residue, and the resulting \(|P-\lambda q|\) term destroys the support lower bound.
4. **Full-hull transference from a prefix.** Later elements do not affect earlier sums, but they can supply essentially all unique representations in the upper half of the prefix’s sum hull. This creates the uncontrolled term \(W_A(N;I)\).

A fresh attempt should combine the cyclic theorem with a dyadic decomposition. For each scale, classify good sums according to which pair of dyadic blocks supplies their unique representation. One would then need to prove that the escaped mass \(W_A(N;I)\) cannot migrate indefinitely to higher block pairs without either producing \(\Omega(\sqrt N)\) collisions or leaving \(\Omega(\sqrt N)\) gaps. That is a Route 3/Route 4 hybrid; the missing multiscale inequality is presently of comparable difficulty to the original problem, so the route is blocked.