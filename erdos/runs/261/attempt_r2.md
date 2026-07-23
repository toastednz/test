STATUS: BLOCKED

## Result

Route 2 yields a sharp exact parametrization of every possible finite rewrite of \(w(n)\), strong localization of the first omitted offset, and rigorous obstructions to the most natural inductive template schemes. In particular, every representation is equivalent to finding an odd integer \(K<2^m\) satisfying a nonlinear binary-digit equation
\[
(n+m)K=2^{m+1}-2+B(K),
\qquad
B(K):=\sum_{k:\,\operatorname{bit}_k(K)=1}k2^k.
\]
Fixed rewrite shapes work for at most one \(n\); no nontrivial finite identity can be translated to infinitely many locations; and even the natural operation of adjoining a consecutive prefix to a known identity produces only \(O(\log X)\) values up to \(X\) from each seed. I did not obtain an adaptive family of identities solving the binary-digit equation for every \(n\), so Q2 remains unresolved.

## Complete Argument

### 1. Exact offset-pattern characterization

It suffices to consider \(n\ge2\), because \(w(1)=w(2)\), and any representation for \(n=2\) also represents \(w(1)\).

For \(n\ge2\), every nontrivial representation uses indices larger than \(n\). Write them as
\[
n+d,\qquad d\in D,
\]
where \(D\subset\mathbb N\) is finite and nonempty. The identity becomes
\[
n=\sum_{d\in D}\frac{n+d}{2^d}.
\]
Define
\[
S_0(D)=\sum_{d\in D}2^{-d},
\qquad
S_1(D)=\sum_{d\in D}d2^{-d}.
\]
Since \(D\) is finite and \(\sum_{d\ge1}2^{-d}=1\), one has \(S_0(D)<1\). Hence the identity is equivalent to
\[
n(1-S_0(D))=S_1(D),
\]
or
\[
\boxed{\quad n=\frac{S_1(D)}{1-S_0(D)}.\quad}
\]

Consequently, a fixed finite offset pattern \(D\) can represent at most one value of \(n\). This already rules out any covering argument based on translating one fixed singleton-replacement pattern.

For \(n\ge2\), \(D\) cannot be a singleton. Indeed, if \(D=\{d\}\), then
\[
n=\frac{n+d}{2^d},
\qquad
n=\frac d{2^d-1}\le1.
\]

---

### 2. Binary-hole normal form

Let
\[
m=\max D,\qquad H=\{1,\ldots,m\}\setminus D.
\]
Since \(m\in D\), one has \(m\notin H\). Multiplying the offset identity by \(2^m\) gives
\[
n2^m
=
n\sum_{d\in D}2^{m-d}
+
\sum_{d\in D}d2^{m-d}.
\]
Therefore
\[
nK=\sum_{d\in D}d2^{m-d},
\]
where
\[
K:=2^m-\sum_{d\in D}2^{m-d}
  =1+\sum_{h\in H}2^{m-h}.
\]
In particular, \(K\) is odd and
\[
1\le K<2^m.
\]

The full weighted sum satisfies
\[
\sum_{d=1}^m d2^{m-d}=2^{m+1}-m-2.
\]
Thus
\[
nK
=
2^{m+1}-m-2-\sum_{h\in H}h2^{m-h}.
\]

Put \(c=m-h\) for \(h\in H\). The nonzero binary digits of \(K\), apart from the compulsory units digit, occur exactly at these positions \(c\). Define
\[
B(K):=\sum_{\substack{c\ge1\\\operatorname{bit}_c(K)=1}}c2^c.
\]
Then
\[
\sum_{h\in H}h2^{m-h}
=
\sum_c(m-c)2^c
=
m(K-1)-B(K).
\]
Substitution yields
\[
nK
=
2^{m+1}-m-2-m(K-1)+B(K),
\]
and hence
\[
\boxed{\quad (n+m)K=2^{m+1}-2+B(K).\quad} \tag{1}
\]

Conversely, suppose \(m\ge1\) and \(K\) is odd with \(1\le K<2^m\). Use the nonzero bits of \(K\) in positions \(1,\dots,m-1\) to define
\[
H=\{m-c:\operatorname{bit}_c(K)=1,\ c\ge1\},
\qquad
D=\{1,\dots,m\}\setminus H.
\]
Then \(m\in D\), and reversing the preceding algebra shows that if (1) holds, the corresponding \(D\) represents \(w(n)\).

We therefore have the following exact equivalence.

> **Binary-hole criterion.** For \(n\ge2\), \(\mathcal F(n)\) holds if and only if there are \(m\ge1\) and an odd \(K<2^m\) such that
> \[
> (n+m)K=2^{m+1}-2+B(K).
> \]

The criterion automatically contains the parity restriction on the largest exponent. Indeed, \(K\) is odd, while the right side of (1) is even, so \(n+m\) is even. The largest actual exponent is \(n+m\).

This is an exact rewrite classification, but proving that such \(m,K\) always exist is essentially as difficult as the original reachability problem.

---

### 3. Localization of the first omitted offset

Let \(D\) be a representing offset pattern, and let
\[
h=\min(\mathbb N\setminus D).
\]
Then
\[
1,2,\dots,h-1\in D.
\]

The full infinite relative sum is
\[
\sum_{d=1}^{\infty}\frac{n+d}{2^d}=n+2.
\]
Since the selected set has sum \(n\), the omitted offsets have total exactly \(2\):
\[
\sum_{d\notin D}\frac{n+d}{2^d}=2. \tag{2}
\]
Because \(h\notin D\) and infinitely many larger offsets are omitted, (2) gives the strict inequality
\[
\frac{n+h}{2^h}<2.
\]
Thus
\[
\boxed{\quad n\le2^{h+1}-h-1.\quad} \tag{3}
\]

On the other hand, the selected prefix cannot exceed the target:
\[
\sum_{d=1}^{h-1}\frac{n+d}{2^d}\le n.
\]
Using
\[
\sum_{d=1}^{h-1}\frac{n+d}{2^d}
=
n+2-\frac{n+h+1}{2^{h-1}},
\]
we obtain
\[
n+h+1-2^h\ge0.
\]
Therefore
\[
n\ge2^h-h-1. \tag{4}
\]

If equality holds in (4), the selected prefix already has sum \(n\), so positivity forbids every later selected term. Hence
\[
D=\{1,\dots,h-1\},
\qquad
n=2^h-h-1,
\]
which is precisely the Borwein–Loring consecutive-block identity.

Otherwise the prefix sum is strictly less than \(n\), and integrality strengthens (4) to
\[
\boxed{\quad 2^h-h\le n\le2^{h+1}-h-1.\quad} \tag{5}
\]

Thus every non-consecutive-block representation has a first hole at a logarithmically localized offset.

Write
\[
n=2^h-h+s,\qquad 0\le s\le2^h-1.
\]
After selecting offsets \(1,\dots,h-1\), the scaled residual is
\[
n+h+1-2^h=s+1.
\]
Offset \(h\) is omitted, so after doubling once, the state is
\[
r=2s+2
\]
at absolute level
\[
j=n+h=2^h+s.
\]
Therefore every non-Borwein–Loring representation is forced through
\[
\boxed{\quad (j,r)=(2^h+s,\,2s+2).\quad} \tag{6}
\]
This is a potentially useful bridge from finite rewrite identities to the residual-state dynamics, but I found no uniform finite funnel from all states in (6) to zero.

---

### 4. No nontrivial identity has a translation-invariant finite shape

Suppose \(P,Q\) are finite subsets of the integers and that, for infinitely many shifts \(s\) for which all indices are positive,
\[
\sum_{p\in P}w(p+s)=\sum_{q\in Q}w(q+s).
\]
Multiplying by \(2^s\) gives
\[
\sum_{p\in P}\frac{p+s}{2^p}
=
\sum_{q\in Q}\frac{q+s}{2^q}.
\]
Equivalently,
\[
s\left(\sum_{p\in P}2^{-p}-\sum_{q\in Q}2^{-q}\right)
+
\left(\sum_{p\in P}p2^{-p}-\sum_{q\in Q}q2^{-q}\right)
=0.
\]
Since this affine function of \(s\) vanishes infinitely often, both coefficients vanish. In particular,
\[
\sum_{p\in P}2^{-p}=\sum_{q\in Q}2^{-q}.
\]
Finite subset sums of distinct powers of \(2^{-1}\) are unique: multiplying by a sufficiently large power of \(2\) reduces the assertion to uniqueness of a finite binary expansion. Hence \(P=Q\).

Thus:

> **No-shift lemma.** A nontrivial finite equal-sum identity among the weights \(w(k)\) cannot remain valid under infinitely many common translations of all its indices.

This rigorously explains why ordinary local rewrite rules, of the kind available for translation-invariant sequences, cannot work here.

---

### 5. The natural prefix-extension operation

There is nevertheless a limited way to turn one identity into a family.

Suppose \(D\subseteq\{1,\dots,m\}\) represents \(n\), and let
\[
K=2^m\bigl(1-S_0(D)\bigr).
\]
For \(\ell\ge0\), define
\[
D^{(\ell)}
=
\{1,\dots,\ell\}
\cup
\{\ell+d:d\in D\}.
\]
Thus one first selects a consecutive prefix of length \(\ell\), then inserts the old pattern shifted by \(\ell\).

For this new pattern,
\[
1-S_0(D^{(\ell)})
=
2^{-\ell}(1-S_0(D)).
\]
Also,
\[
\begin{aligned}
S_1(D^{(\ell)})
&=
\sum_{e=1}^{\ell}\frac e{2^e}
+
2^{-\ell}\sum_{d\in D}\frac{\ell+d}{2^d}\\
&=
2-\frac{\ell+2}{2^\ell}
+
2^{-\ell}\bigl(\ell S_0(D)+S_1(D)\bigr).
\end{aligned}
\]
Using \(S_1(D)=n(1-S_0(D))\), division gives the unique target represented by \(D^{(\ell)}\):
\[
\boxed{\quad
n_\ell
=
n-\ell+\frac{2^{m+1}(2^\ell-1)}K.
\quad} \tag{7}
\]

Because \(K\) is odd, \(n_\ell\) is an integer if and only if
\[
\boxed{\quad K\mid 2^\ell-1.\quad} \tag{8}
\]
Thus every seed does generate infinitely many new identities: take \(\ell\) to be a multiple of the multiplicative order of \(2\) modulo \(K\). The Borwein–Loring family is the special case \(K=1\).

However, this mechanism is far too sparse to cover all integers from finitely many seeds. Since \(D\ne\varnothing\),
\[
K\le2^m-1,
\]
so
\[
\frac{2^{m+1}}K>2.
\]
It follows from (7), for \(n\ge2\), that
\[
n_\ell
\ge n-\ell+2(2^\ell-1)
\ge2^\ell.
\]
Therefore \(n_\ell\le X\) implies \(\ell\le\log_2X\). Each seed produces only \(O(\log X)\) values up to \(X\), and a finite collection of seeds produces only \(O(\log X)\) values. It cannot cover all integers up to \(X\).

Repeated prefixing does not help: prefixing by \(\ell_1\) and then by \(\ell_2\) is the same as prefixing once by \(\ell_1+\ell_2\).

This disposes of the most direct finite-seed inductive closure of the Borwein–Loring construction.

---

### 6. Complete classification of one-hole templates

Suppose
\[
D=\{1,\dots,m\}\setminus\{m-c\},
\qquad 1\le c<m.
\]
Then
\[
K=1+2^c,\qquad B(K)=c2^c.
\]
The represented value is
\[
\boxed{\quad
n=
\frac{2^{m+1}-m-2-(m-c)2^c}{2^c+1}.
\quad} \tag{9}
\]
Since \(2^c\equiv-1\pmod{2^c+1}\), this is integral exactly when
\[
\boxed{\quad
2^{m+1}\equiv c+2\pmod{2^c+1}.
\quad} \tag{10}
\]

Examples:

- If \(c=2\), then \(2^c+1=5\), and (10) is equivalent to
  \[
  m\equiv1\pmod4.
  \]
  Thus
  \[
  n=\frac{2^{m+1}-5m+6}{5}.
  \]
  For \(m=5\), this gives \(n=9\) and
  \[
  \frac9{2^9}
  =
  \frac{10}{2^{10}}+\frac{11}{2^{11}}
  +\frac{13}{2^{13}}+\frac{14}{2^{14}}.
  \]

- If \(c=3\), then \(2^c+1=9\), and (10) is equivalent to
  \[
  m\equiv4\pmod6.
  \]
  The first case \(m=4\) gives \(n=2\) and
  \[
  \frac2{2^2}
  =
  \frac4{2^4}+\frac5{2^5}+\frac6{2^6}.
  \]
  The next case \(m=10\) gives \(n=220\).

These are genuine additional parametrized families, but each fixed \(c\) again produces only exponentially spaced values.

---

### 7. The unresolved binary carrying problem

For fixed
\[
N=n+m,
\]
define
\[
q_k=(N-k)2^k.
\]
Equation (1) can be rewritten as
\[
G_N(K):=NK-B(K)
       =\sum_{\operatorname{bit}_k(K)=1}(N-k)2^k
       =2^{m+1}-2. \tag{11}
\]
Thus Route 2 ultimately asks whether the specific target \(2^{m+1}-2\) can always be represented by binary digits with place values \(q_k\), for some \(m\).

The place values change from superincreasing to overlapping at a sharply defined scale:
\[
q_k-\sum_{i=0}^{k-1}q_i
=
N+2-2^{k+1}. \tag{12}
\]
Indeed,
\[
\sum_{i=0}^{k-1}(N-i)2^i
=
(N-k+2)2^k-N-2.
\]

There is also an exact carry formula. Enumerate odd \(K\) in increasing order. Suppose adding \(2\) clears bits \(1,\dots,t-1\) and sets bit \(t\). Then
\[
\begin{aligned}
G_N(K+2)-G_N(K)
&=
q_t-\sum_{i=1}^{t-1}q_i\\
&=
2N+2-2^{t+1}. \tag{13}
\end{aligned}
\]
Thus \(G_N\) is increasing across short carries and decreasing across sufficiently long carries. It is not monotone, so an intermediate-value argument does not apply.

I found no invariant forcing (11) to have a solution, no bounded collection of binary carry patterns covering every \(N=n+m\), and no descent that turns a solution for one \(n\) into solutions for a positive-density set of nearby \(n\). Establishing such a theorem is the precise unresolved block.

## Self-Audit

1. **The binary-hole normal form is only a reformulation, not a solution.**  
   Equation (1) is equivalent to the original finite representation problem and therefore does not by itself reduce the difficulty. I believe the equivalence is sound because both directions explicitly reconstruct \(D\) from the binary digits of \(K\), with all identities checked over the integers.

2. **The negative template results have deliberately limited scope.**  
   The no-shift lemma and the \(O(\log X)\) prefix-family bound do not exclude a more adaptive parametrized family whose shape changes with the binary expansion of \(n\). I have not claimed otherwise. They do rigorously eliminate the most natural fixed-shape and finite-seed versions of Route 2.

3. **The first-hole argument has an exceptional equality case.**  
   The lower bound is \(n\ge2^h-h-1\), not always \(n\ge2^h-h\). Equality means the initial consecutive block already terminates and gives exactly the Borwein–Loring family. This case was separated explicitly; positivity proves that no later selected indices can then occur.

## Computations To Verify

The following exact Python code checks the normal form, searches finite representations, tests the first-hole bounds, and verifies the prefix and one-hole constructions.

```python
def exact_offset_identity(n, D):
    """Check n = sum_{d in D} (n+d)/2^d exactly."""
    D = sorted(set(D))
    if not D:
        return False
    m = max(D)
    lhs = n * (1 << m)
    rhs = sum((n + d) * (1 << (m - d)) for d in D)
    return lhs == rhs


def K_from_pattern(m, D):
    D = set(D)
    return (1 << m) - sum(1 << (m - d) for d in D)


def B(K):
    ans = 0
    for k in range(1, K.bit_length()):
        if (K >> k) & 1:
            ans += k * (1 << k)
    return ans


def pattern_from_K(m, K):
    """Reconstruct D from odd K < 2^m."""
    assert 1 <= K < (1 << m) and K % 2 == 1
    holes = set()
    for c in range(1, m):
        if (K >> c) & 1:
            holes.add(m - c)
    return [d for d in range(1, m + 1) if d not in holes]


def enumerate_normal_form(n, max_m):
    out = []
    for m in range(1, max_m + 1):
        target = n + m
        for K in range(1, 1 << m, 2):
            if target * K == (1 << (m + 1)) - 2 + B(K):
                D = pattern_from_K(m, K)
                assert K_from_pattern(m, D) == K
                assert exact_offset_identity(n, D)
                if len(D) >= 2:
                    out.append((m, K, D))
    return out


def first_hole_checks(n, D):
    D = set(D)
    h = 1
    while h in D:
        h += 1

    assert n <= (1 << (h + 1)) - h - 1

    lower_exception = (1 << h) - h - 1
    if n == lower_exception:
        assert D == set(range(1, h))
    else:
        assert n >= (1 << h) - h

        s = n - ((1 << h) - h)
        assert 0 <= s <= (1 << h) - 1

        # State after selecting 1,...,h-1 and omitting h.
        j = n + h
        r = 2 * (s + 1)
        assert j == (1 << h) + s
        assert r == 2 * s + 2


def prefix_extension(n, D, ell):
    """Apply the prefix-extension construction."""
    D = sorted(set(D))
    m = max(D)
    K = K_from_pattern(m, D)
    numerator = (1 << (m + 1)) * ((1 << ell) - 1)

    if numerator % K != 0:
        return None

    n2 = n - ell + numerator // K
    D2 = list(range(1, ell + 1)) + [ell + d for d in D]
    D2 = sorted(set(D2))
    assert exact_offset_identity(n2, D2)
    return n2, D2


def one_hole_families(max_c=12, max_m=80):
    ans = []
    for c in range(1, max_c + 1):
        modulus = (1 << c) + 1
        for m in range(c + 1, max_m + 1):
            if ((1 << (m + 1)) - (c + 2)) % modulus:
                continue
            numerator = (
                (1 << (m + 1))
                - m - 2
                - (m - c) * (1 << c)
            )
            assert numerator % modulus == 0
            n = numerator // modulus
            if n >= 2:
                hole = m - c
                D = [d for d in range(1, m + 1) if d != hole]
                assert exact_offset_identity(n, D)
                ans.append((c, m, n, D))
    return ans


def finite_residual_search(n, max_m):
    """
    Find one representation with largest relative offset <= max_m.
    States are exact scaled residuals.
    """
    states = {n: 0}  # residual -> bit mask of selected offsets

    for d in range(1, max_m + 1):
        j = n + d
        new_states = {}

        for r, mask in states.items():
            doubled = 2 * r

            # Omit j.
            if 0 <= doubled <= j + 2:
                new_states.setdefault(doubled, mask)

            # Select j.
            selected = doubled - j
            if selected == 0:
                D = [
                    e for e in range(1, d)
                    if (mask >> (e - 1)) & 1
                ] + [d]
                assert exact_offset_identity(n, D)
                return D

            if 0 < selected <= j + 2:
                new_mask = mask | (1 << (d - 1))
                new_states.setdefault(selected, new_mask)

        states = new_states

    return None


def verify_range(N=500, max_m=100):
    for n in range(2, N + 1):
        D = finite_residual_search(n, max_m)
        if D is None:
            print("No representation found within cutoff:", n)
            continue
        assert exact_offset_identity(n, D)
        first_hole_checks(n, D)

        m = max(D)
        K = K_from_pattern(m, D)
        assert (n + m) * K == (1 << (m + 1)) - 2 + B(K)
```

For cataloguing arbitrary small equal-sum gadgets:

```python
def gadget_collisions(M):
    """
    Find pairs of distinct subsets of {1,...,M} with equal weight.
    All sums are scaled by 2^M.
    """
    first = {}
    gadgets = []

    for mask in range(1 << M):
        total = 0
        for k in range(1, M + 1):
            if (mask >> (k - 1)) & 1:
                total += k * (1 << (M - k))

        if total in first and first[total] != mask:
            other = first[total]

            # Cancel common coordinates.
            p_mask = mask & ~other
            q_mask = other & ~mask
            P = [k for k in range(1, M + 1)
                 if (p_mask >> (k - 1)) & 1]
            Q = [k for k in range(1, M + 1)
                 if (q_mask >> (k - 1)) & 1]

            if P and Q:
                gadgets.append((P, Q, total))
        else:
            first[total] = mask

    return gadgets
```

The most informative larger computation would enumerate solutions of
\[
(n+m)K=2^{m+1}-2+B(K)
\]
and record the binary forms of the successful \(K\). A reusable proof would likely require these successful \(K\)'s to fall into finitely describable carry families rather than isolated patterns.

## Route Diagnosis

**Proved lemmas**

- Every fixed offset pattern represents at most one \(n\).
- Every representation has the exact binary-hole normal form (1).
- The first omitted offset is logarithmically localized by (3)–(5).
- A nontrivial finite identity cannot be translated to infinitely many positions.
- Prefixing a known identity is governed exactly by (7)–(8).
- Finitely many prefix-generated seed families have zero density and cannot cover all integers.
- One-hole identities are completely classified by the congruence (10).
- The remaining binary carrying problem has exact local formulas (12)–(13).

**Plausible but unproved**

- For every \(n\), some pair \(m,K\) satisfies the binary-hole equation.
- Successful \(K\)'s may admit a recursive description through carries near the transition \(2^{k+1}\approx n+m+2\).
- The forced first-hole state (6) may enter a finite collection of terminating funnels. No such funnels were established.

**Dead ends**

- Fixed RHS shapes: each gives only one \(n\).
- Common translations of identities: rigorously impossible except for the trivial identity.
- Borwein–Loring identities plus consecutive-prefix induction: only exponentially sparse outputs.
- One-hole and other fixed small-hole templates: they produce useful congruence families but not a covering.
- Monotonic subset-sum interpolation in \(K\): fails because the carry increment (13) changes sign.

**Precise block**

Route 2 has reduced Q2 to proving that for every \(n\ge2\), there are \(m\) and odd \(K<2^m\) satisfying
\[
(n+m)K=2^{m+1}-2+B(K).
\]
No argument found forces this equation to be solvable, and it is an exact reformulation of comparable strength rather than a genuine descent. The finite rewrite route is therefore blocked unless one discovers an adaptive binary-carry construction with unboundedly changing templates.

A fresh attempt should probably switch to the residual-state formulation, using the forced first-hole state
\[
(2^h+s,\,2s+2),
\]
and search for certified return maps or terminating funnels. If Route 2 is retained, the most promising object is the carry function \(G_N(K)=NK-B(K)\): one needs a theorem exploiting the exact carry increment
\[
G_N(K+2)-G_N(K)=2N+2-2^{t+1}
\]
to hit \(2^{m+1}-2\), not merely to approximate it.