STATUS: BLOCKED

## Result

Route 4 does not yield a counterexample. I obtained an exact \(2\)-adic carry parametrization of every finite representation, proved additional necessary congruence conditions such as \(M\equiv0\) or \(6\pmod 8\) when \(M-n\ge3\), and proved that every bounded-depth congruence obstruction can be evaded by taking \(M\equiv-2\pmod{2^h}\). The global problem becomes an exact digit-derivative equation
\[
(n+L)Y-D(Y)=2^{L+1}-2
\]
in an unbounded length \(L\) and an odd integer \(Y<2^L\). Excluding all such pairs for one explicit \(n\), or proving one exists for every \(n\), is of comparable strength to Q2. Thus no proof or disproof of Q2 is obtained.

## Complete Argument

### 1. Exact backward carry descent

It suffices to treat \(n\ge2\). For such \(n\), any nontrivial representation uses only indices greater than \(n\). The case \(n=1\) has the same target as \(n=2\).

Suppose
\[
\frac n{2^n}=\sum_{a\in A}\frac a{2^a},
\qquad
A\subset\{n+1,n+2,\dots\}
\]
is finite, and let
\[
M=\max A,\qquad L=M-n.
\]
For \(0\le d<L\), put
\[
b_d=\mathbf 1_{\{M-d\in A\}}.
\]
Because \(M\in A\), we have \(b_0=1\). Multiplying the identity by \(2^M\) gives
\[
n2^L=\sum_{d=0}^{L-1}(M-d)b_d2^d. \tag{1}
\]

Define \(c_0=0\). Whenever the indicated quotient is integral, define
\[
c_{d+1}=\frac{c_d+(M-d)b_d}{2}. \tag{2}
\]
Inductively,
\[
c_d
=
\frac1{2^d}\sum_{e=0}^{d-1}(M-e)b_e2^e. \tag{3}
\]
Indeed, substituting (3) into (2) gives the same formula with \(d+1\).

Consequently, (1) is equivalent to requiring that all the carries \(c_d\) be integral and that
\[
c_L=n. \tag{4}
\]

These carries are exactly the reverse residual states. If \(j=M-d\), then, using the full identity,
\[
c_d
=
2^j\sum_{\substack{a\in A\\a>j}}\frac a{2^a}
=
2^j\left(
\frac n{2^n}
-\sum_{\substack{a\in A\\n<a\le j}}\frac a{2^a}
\right)
=r_j.
\]
Thus
\[
0\le c_d\le M-d+2, \tag{5}
\]
because the scaled full tail after \(j=M-d\) has mass \(j+2\).

This proves the exact carry criterion:

> A finite representation with maximum \(M=n+L\) is equivalent to a binary word
> \[
> b_0b_1\dots b_{L-1},\qquad b_0=1,
> \]
> whose carries under (2) are integral and terminate at \(c_L=n\).

### 2. Initial congruence restrictions

Reducing (1) modulo \(2\), only the \(d=0\) term survives. Since \(b_0=1\),
\[
M\equiv0\pmod2.
\]
Thus the maximum selected exponent is even.

There is a slightly stronger restriction.

> **Lemma.** If \(L=M-n\ge3\), then
> \[
> M\equiv0\quad\text{or}\quad6\pmod8.
> \]

**Proof.**

The first carry is
\[
c_1=\frac M2.
\]
At \(d=1\), the number \(M-1\) is odd, so integrality of
\[
c_2=\frac{c_1+(M-1)b_1}{2}
\]
forces
\[
b_1\equiv c_1\pmod2.
\]

If \(M\equiv0\pmod4\), then \(b_1=0\) and
\[
c_2=\frac M4.
\]
Since \(L\ge3\), the next carry must exist:
\[
c_3=\frac{c_2+(M-2)b_2}{2}.
\]
The coefficient \(M-2\) is even, so this is integral only if \(c_2\) is even. Hence
\[
M\equiv0\pmod8.
\]

If \(M\equiv2\pmod4\), then \(b_1=1\) and
\[
c_2
=
\frac{M/2+M-1}{2}
=
\frac{3M-2}{4}.
\]
Again \(c_2\) must be even. For \(M\equiv2\pmod8\), this number is odd; for \(M\equiv6\pmod8\), it is even. Therefore
\[
M\equiv6\pmod8.
\]
These are the only cases. ∎

Higher descent gives further nested restrictions, but branching occurs whenever both the carry and current exponent are even. For example, the admissible maximum residues obtained by checking only divisibility through depth \(h\) begin as follows:
\[
\begin{array}{c|c}
h&\text{possible }M\bmod 2^h\\ \hline
1&\{0\}\\
2&\{0,2\}\\
3&\{0,6\}\\
4&\{0,6,8,14\}\\
5&\{0,6,8,14,22,24,30\}.
\end{array}
\]
The code below verifies this table exactly.

### 3. Every bounded-depth top congruence can be evaded

The preceding residue restrictions cannot by themselves produce a counterexample, because one residue always survives to every depth.

> **Lemma.** Let \(h\ge1\). If
> \[
> 2^h\mid M+2,
> \]
> then selecting all of the top \(h\) indices
> \[
> M,M-1,\dots,M-h+1
> \]
> makes their scaled contribution divisible by \(2^h\).

**Proof.**

The contribution is
\[
S_h=\sum_{d=0}^{h-1}(M-d)2^d.
\]
Using
\[
\sum_{d=0}^{h-1}2^d=2^h-1,
\qquad
\sum_{d=0}^{h-1}d2^d=(h-2)2^h+2,
\]
we get
\[
\begin{aligned}
S_h
&=M(2^h-1)-\bigl((h-2)2^h+2\bigr)\\
&=(M-h+2)2^h-(M+2).
\end{aligned}
\]
Hence \(2^h\mid S_h\) whenever \(2^h\mid M+2\). ∎

The resulting reverse carries are admissible, not merely integral. If \(M=t2^h-2\) and the top \(d\) digits are all \(1\), then
\[
c_d=M-d+2-\frac{M+2}{2^d}
=t\bigl(2^h-2^{h-d}\bigr)-d. \tag{6}
\]
For \(d=0\), this is zero. For \(1\le d\le h\),
\[
2^h-2^{h-d}
=2^{h-d}(2^d-1)\ge d,
\]
so \(c_d\ge0\). Equation (6) also gives
\[
c_d\le M-d+2.
\]
Thus this is a valid reverse suffix of arbitrary prescribed length \(h\).

For any fixed target \(n\) and fixed congruence depth \(h\), choose \(t\) large enough that
\[
M=t2^h-2>n+h.
\]
Then \(L=M-n\ge h\), the left side \(n2^L\) of (1) is zero modulo \(2^h\), and the selected top block also contributes zero modulo \(2^h\).

Therefore:

> No obstruction examining only a fixed number \(h\) of top binary congruences can exclude any particular \(n\).

The surviving residues are coherently
\[
M\equiv-2\pmod{2^h}.
\]
Their inverse-limit value is the \(2\)-adic integer \(M=-2\). This is not a permissible positive maximum; it is precisely an “escape to infinity” that defeats bounded-depth congruence arguments.

### 4. A global digit-derivative parametrization

For a nonnegative integer \(z\) with binary expansion
\[
z=\sum_{d\ge0}z_d2^d,\qquad z_d\in\{0,1\},
\]
define its binary digit derivative
\[
D(z):=\sum_{d\ge0}d\,z_d2^d. \tag{7}
\]

For the word \(b_0,\dots,b_{L-1}\) above, let
\[
X=\sum_{d=0}^{L-1}b_d2^d.
\]
Then \(X\) is odd and \(1\le X<2^L\), and (1) becomes
\[
MX-D(X)=n2^L. \tag{8}
\]
Since \(M=n+L\),
\[
n(2^L-X)=LX-D(X). \tag{9}
\]

Now put
\[
Y=2^L-X.
\]
Then \(Y\) is odd and
\[
1\le Y<2^L.
\]

Because \(Y\) is odd, subtracting \(1\) changes only its least significant bit, whose contribution to \(D\) is zero. Hence
\[
D(Y-1)=D(Y).
\]
Furthermore,
\[
X=2^L-Y=(2^L-1)-(Y-1),
\]
so the \(L\) binary digits of \(X\) are the complements of those of \(Y-1\). Therefore
\[
D(X)=D(2^L-1)-D(Y-1).
\]
The full digit sum is
\[
D(2^L-1)=\sum_{d=0}^{L-1}d2^d=(L-2)2^L+2.
\]
It follows that
\[
D(X)=(L-2)2^L+2-D(Y). \tag{10}
\]

Substituting \(X=2^L-Y\), (10), and \(M=n+L\) into (8) gives
\[
(n+L)Y-D(Y)=2^{L+1}-2. \tag{11}
\]

Conversely, suppose \(L\ge1\) and \(Y\) is odd with \(1\le Y<2^L\), and suppose (11) holds. Set
\[
X=2^L-Y
\]
and select \(M-d\) exactly when the \(d\)-th binary digit of \(X\) is \(1\). Reversing the preceding algebra gives (8), hence the desired finite identity.

We have thus proved:

> **Exact parametrization.** For \(n\ge2\), \(\mathcal F(n)\) holds if and only if there are \(L\ge1\) and an odd \(Y\), \(1\le Y<2^L\), such that
> \[
> \boxed{(n+L)Y-D(Y)=2^{L+1}-2.} \tag{12}
> \]
> The representing set is recovered from the binary digits of
> \[
> X=2^L-Y
> \]
> by
> \[
> A=\{\,n+L-d:0\le d<L,\ \text{the \(d\)-th bit of \(X\) is \(1\)}\,\}.
> \]

For \(n\ge2\), this set cannot have only one member: that would give \(w(n)=w(M)\) with \(M>n\), contradicting strict decrease of \(w(r)\) for \(r\ge2\).

There are useful necessary bounds. Since \(Y<2^L\),
\[
0\le D(Y)\le(L-1)Y.
\]
Writing \(R_L=2^{L+1}-2\), equation (12) gives
\[
\frac{R_L}{n+L}\le Y\le\frac{R_L}{n+1}. \tag{13}
\]
Also, the full finite block from \(n+1\) through \(M=n+L\) has scaled sum
\[
(n+2)2^L-(M+2).
\]
It must be at least the target \(n2^L\), so necessarily
\[
M+2\le2^{L+1}. \tag{14}
\]
This only gives a lower bound on the required gap \(L\); it gives no upper bound.

### 5. The parametrization produces many nontrivial infinite families

Fix an odd integer \(Y\). If
\[
2^e\equiv 2-D(Y)\pmod Y \tag{15}
\]
for some \(e\), then every sufficiently large \(L\) satisfying
\[
L+1\equiv e\pmod{\operatorname{ord}_Y(2)}
\]
makes
\[
M=\frac{2^{L+1}-2+D(Y)}Y
\]
an integer. Defining \(n=M-L\), equation (12) holds. For sufficiently large \(L\), the exponential term dominates \(L\), so \(n\ge2\). Thus every such \(Y\) gives an infinite family of finite representations.

This includes but is not limited to the Borwein–Loring family:

- \(Y=1\) gives
  \[
  n=2^{L+1}-L-2.
  \]

- \(Y=9\) has \(D(9)=24\). Taking \(L=4\) gives
  \[
  n=\frac{2^5-2+24}{9}-4=2.
  \]
  Here \(X=16-9=7\), yielding
  \[
  \frac2{2^2}
  =\frac4{2^4}+\frac5{2^5}+\frac6{2^6}.
  \]

- \(Y=11\) has \(D(11)=26\). Taking \(L=5\) gives \(n=3\), \(M=8\), and \(X=21\), yielding
  \[
  \frac3{2^3}
  =\frac4{2^4}+\frac6{2^6}+\frac8{2^8}.
  \]

- \(Y=5\) has \(D(5)=8\). Taking \(L=5\) gives \(n=9\), \(M=14\), and \(X=27\), yielding
  \[
  \frac9{2^9}
  =
  \frac{10}{2^{10}}+\frac{11}{2^{11}}
  +\frac{13}{2^{13}}+\frac{14}{2^{14}}.
  \]

These examples show that the carry restrictions do not collapse to the consecutive-block family.

### 6. Precise obstruction to completing Route 4

To disprove Q2 by this route, one must exhibit an explicit \(n_0\) and prove that
\[
(n_0+L)Y-D(Y)\ne2^{L+1}-2
\]
for every \(L\ge1\) and every odd \(Y<2^L\).

For each fixed \(L\), this is a finite exact calculation, and (13) narrows the search interval. However:

1. There is no proved upper bound on \(L\).
2. Every fixed amount of top congruence information is compatible with arbitrarily large potential maxima, by the lemma in Section 3.
3. The function \(D(Y)\) depends on the entire binary word for \(Y\); reducing modulo a fixed power of \(2\) discards exactly the global information needed to couple the bottom of the descent to \(c_L=n\).

Thus equation (12) is an exact reformulation but not a resolution. Ruling out all its solutions for one \(n\) is presently of comparable strength to the original counterexample problem.

## Self-Audit

1. **The “bounded congruences cannot work” conclusion has deliberately limited scope.**  
   It excludes only arguments based on a fixed number of top suffix congruences. It does not exclude a global \(2\)-adic/Archimedean invariant using the whole gap \(L=M-n\). The stated limited conclusion follows exactly from the explicit suffix construction \(M\equiv-2\pmod{2^h}\).

2. **The digit-derivative parametrization does not reduce the logical difficulty of Q2 by itself.**  
   Equation (12) still has two unbounded variables and is equivalent to the original problem. I nevertheless believe the equivalence is correct because both directions explicitly reconstruct the binary selection word, and the identities \(D(Y-1)=D(Y)\) and \(D(2^L-1)=(L-2)2^L+2\) were used exactly.

3. **The fixed-\(Y\) families do not approach a covering theorem for all \(n\).**  
   They only show that the congruence structure is flexible and generate additional infinite families. Their validity follows from direct substitution into (12), but no claim is made that their union covers all positive integers.

## Computations To Verify

```python
from math import gcd

def digit_derivative(z):
    """D(z) = sum d * bit_d(z) * 2^d."""
    ans = 0
    d = 0
    while z:
        if z & 1:
            ans += d * (1 << d)
        z >>= 1
        d += 1
    return ans

def check_representation(n, A):
    """Exact integer checker."""
    A = sorted(set(A))
    if n < 1 or len(A) < 2 or any(a < 1 for a in A):
        return False
    M = max([n] + A)
    lhs = n << (M - n)
    rhs = sum(a << (M - a) for a in A)
    return lhs == rhs

# Explicit identities from the argument.
assert check_representation(2, [4, 5, 6])
assert check_representation(3, [4, 6, 8])
assert check_representation(9, [10, 11, 13, 14])

def representation_from_Y(n, L, Y):
    """
    Recover A from a solution of
        (n+L)Y - D(Y) = 2^(L+1)-2.
    """
    assert 1 <= Y < (1 << L) and Y % 2 == 1
    M = n + L
    assert M * Y - digit_derivative(Y) == (1 << (L + 1)) - 2

    X = (1 << L) - Y
    A = [M - d for d in range(L) if (X >> d) & 1]
    assert check_representation(n, A)
    return A

assert representation_from_Y(2, 4, 9) == [6, 5, 4]
assert representation_from_Y(3, 5, 11) == [8, 6, 4]
assert representation_from_Y(9, 5, 5) == [14, 13, 11, 10]

def search_by_Y(n, Lmax):
    """
    Search exactly for representations with gap L <= Lmax.
    Absence from this search is not a disproof.
    """
    answers = []
    for L in range(1, Lmax + 1):
        M = n + L
        R = (1 << (L + 1)) - 2

        # Necessary bounds R/M <= Y <= R/(n+1).
        lo = (R + M - 1) // M
        hi = min((1 << L) - 1, R // (n + 1))

        if lo % 2 == 0:
            lo += 1
        for Y in range(lo, hi + 1, 2):
            if M * Y - digit_derivative(Y) == R:
                answers.append((L, Y, representation_from_Y(n, L, Y)))
    return answers

def backward_representation(n, M):
    """
    Exact reverse residual search for a representation with maximum exactly M.
    Returns one representation or None.
    """
    if M <= n:
        return None

    # At level M, residual is zero. Map residual to selected indices.
    states = {0: ()}

    for j in range(M, n, -1):
        new_states = {}
        for rj, selected in states.items():
            choices = (1,) if j == M else (0, 1)  # force M to be selected
            for eps in choices:
                numerator = rj + j * eps
                if numerator % 2:
                    continue
                prev = numerator // 2

                # State is now at level j-1, whose tail capacity is j+1.
                if not (0 <= prev <= j + 1):
                    continue

                new_selected = selected + ((j,) if eps else ())
                new_states.setdefault(prev, new_selected)
        states = new_states
        if not states:
            return None

    if n not in states:
        return None

    A = sorted(states[n])
    assert max(A) == M
    assert check_representation(n, A)
    return A

def first_backward_representation(n, Mmax):
    for M in range(n + 1, Mmax + 1):
        if M % 2 == 0:
            A = backward_representation(n, M)
            if A is not None:
                return M, A
    return None

def admissible_max_residues(h):
    """
    Residues M mod 2^h for which some top h-bit word, with the
    maximum selected, has total divisible by 2^h.
    """
    modulus = 1 << h
    out = set()
    for M in range(modulus):
        for X in range(1, modulus, 2):  # low bit 1 means maximum selected
            if (M * X - digit_derivative(X)) % modulus == 0:
                out.add(M)
                break
    return out

assert admissible_max_residues(1) == {0}
assert admissible_max_residues(2) == {0, 2}
assert admissible_max_residues(3) == {0, 6}
assert admissible_max_residues(4) == {0, 6, 8, 14}
assert admissible_max_residues(5) == {0, 6, 8, 14, 22, 24, 30}

def verify_top_block_evasion(h, t):
    """
    Verify the all-ones top block when M+2=t*2^h.
    """
    M = t * (1 << h) - 2
    X = (1 << h) - 1
    assert (M * X - digit_derivative(X)) % (1 << h) == 0

    # Check all reverse carries explicitly.
    c = 0
    for d in range(h):
        numerator = c + (M - d)
        assert numerator % 2 == 0
        c = numerator // 2
        assert 0 <= c <= M - d + 1

for h in range(1, 15):
    for t in range(2, 8):
        verify_top_block_evasion(h, t)

# Suggested finite experimental search:
# for n in range(10001, 20001):
#     ans = first_backward_representation(n, n + 500)
#     if ans is None:
#         print("No representation found within this horizon:", n)
#
# Such output would identify search candidates only, not counterexamples.
```

## Route Diagnosis

**Proved lemmas**

- Exact equivalence between finite representations and integral reverse carries terminating at \(c_L=n\).
- If \(M-n\ge3\), then \(M\equiv0\) or \(6\pmod8\).
- For every fixed depth \(h\), the residue \(M\equiv-2\pmod{2^h}\) supports an admissible top suffix of length \(h\).
- Exact parametrization by odd \(Y<2^L\):
  \[
  (n+L)Y-D(Y)=2^{L+1}-2.
  \]
- Fixed odd \(Y\) satisfying a power-of-two congruence produces an infinite family of represented \(n\).

**Plausible but unproved**

- Every \(n\ge2\) admits some pair \((L,Y)\) satisfying the parametrization. This is exactly Q2 in new coordinates.
- A useful global invariant may have to combine the Archimedean size of \(Y\), the full digit statistic \(D(Y)\), and the congruence class of \(2^{L+1}\) modulo \(Y\).

**Dead ends**

- Parity of \(M\) is far too weak.
- Increasing a fixed modulus \(2^h\) does produce nested restrictions, but \(M\equiv-2\pmod{2^h}\) survives every finite depth.
- A bounded search over \(M\) or \(L\) cannot disprove Q2 because no upper bound on either is known.
- The digit-derivative parametrization is exact but currently only repackages the unbounded global obstruction.

**Recommended next attempt**

A fresh counterexample attempt should not pursue further fixed-depth suffix congruences. It would need either:

1. an a priori upper bound on \(L\) for a proposed \(n_0\); or
2. a genuinely global theorem showing that
   \[
   \frac{2^{L+1}-2+D(Y)}Y-L
   \]
   omits a specific positive integer for all odd \(Y<2^L\).

For an affirmative approach, the same parametrization suggests studying the range of this expression as \(Y\) varies, possibly through recursive formulas for \(D(2Y\pm1)\). No such covering theorem has been established here.