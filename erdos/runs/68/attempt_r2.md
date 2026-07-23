STATUS: BLOCKED

## Result

Route 2 yields substantial but insufficient structure. Every prime \(p\ge5\) occurs as a divisor of some \(n!-1\), and infinitely many indices \(n\) have a prime divisor that occurs in no earlier \(m!-1\). Such a primitive prime gives an exact modular lower bound on the tail under the assumption that \(\alpha\) is rational. However, the usual termwise denominator-clearing multiplier is provably already too large: consecutive numbers \((N-1)!-1\) and \(N!-1\) are coprime, and their product exceeds \((N+1)!-1\) for \(N\ge5\). An optimized version depends on unexpectedly strong cancellation in the reduced denominator of the preceding partial sum; no argument controlling that cancellation was found. Thus the route is blocked at a precise finite-denominator problem, not at the existence of primitive primes.

## Complete Argument

Write
\[
d_n:=n!-1,\qquad
S_N:=\sum_{n=2}^N\frac1{d_n},\qquad
R_N:=\alpha-S_N,
\]
and
\[
L_N:=\operatorname{lcm}(d_2,\dots,d_N).
\]

### 1. Exact prime-incidence structure

#### Lemma 1

If a prime \(p\) divides \(d_n=n!-1\), then:

1. \(p\ge n+2\);
2. \(p\mid d_{p-2}\);
3. \(p\nmid d_m\) for every \(m\ge p-1\).

Consequently, \(p-2\) is the last index at which \(p\) divides \(d_m\).

#### Proof

Since \(p\mid n!-1\), no integer \(1,\dots,n\) is divisible by \(p\), so \(p>n\).

The possibility \(p=n+1\) is impossible. Indeed, then \(n=p-1\), and Wilson’s theorem gives
\[
n!=(p-1)!\equiv-1\pmod p,
\]
whereas \(p\mid n!-1\) would require \(n!\equiv1\pmod p\). Since \(n\ge2\), this cannot be the exceptional prime \(p=2\). Hence \(p\ge n+2\), and in particular \(p\ge5\).

Wilson’s theorem also gives
\[
(p-1)!=(p-1)(p-2)!\equiv-1\pmod p.
\]
As \(p-1\equiv-1\pmod p\), it follows that
\[
(p-2)!\equiv1\pmod p,
\]
so \(p\mid d_{p-2}\).

At \(m=p-1\),
\[
d_{p-1}=(p-1)!-1\equiv-2\not\equiv0\pmod p.
\]
For \(m\ge p\), one has \(m!\equiv0\pmod p\), hence
\[
d_m\equiv-1\not\equiv0\pmod p.
\]
Thus \(p-2\) is the final occurrence. ∎

Wilson’s theorem used above follows by pairing every nonzero residue modulo \(p\) with its inverse; only \(1\) and \(-1\) are self-inverse, so the product of all nonzero residues is \(-1\).

#### Lemma 2

If \(p^a\mid d_n\) and \(p^a\mid d_m\), where \(n<m\), then
\[
\frac{m!}{n!}\equiv1\pmod{p^a}.
\]
In particular,
\[
\frac{m!}{n!}\ge p^a+1.
\]

#### Proof

Put \(P=m!/n!\). Since
\[
n!\equiv m!\equiv1\pmod{p^a},
\]
we have
\[
P\equiv m!(n!)^{-1}\equiv1\pmod{p^a}.
\]
Also \(P>1\), so the least possible value is \(p^a+1\). ∎

Thus a large primitive prime power remains isolated for a quantitatively long interval. This does not yet overcome denominator growth.

### 2. Infinitely many primitive prime divisors

Call \(p\) primitive at index \(n\) if
\[
p\mid d_n
\quad\text{and}\quad
p\nmid d_m\quad(2\le m<n).
\]

#### Proposition 3

There are infinitely many indices \(n\) for which \(d_n\) has a primitive prime divisor.

#### Proof

For each prime \(p\ge5\), Lemma 1 shows that \(p\mid d_{p-2}\). Therefore the set
\[
\{m\ge2:p\mid d_m\}
\]
is nonempty, and we may define
\[
f(p):=\min\{m\ge2:p\mid d_m\}.
\]
Then \(p\) is primitive at \(f(p)\).

The values \(f(p)\) are unbounded. Otherwise, if \(f(p)\le M\) for every prime \(p\ge5\), every such prime would divide the fixed nonzero integer
\[
\prod_{m=2}^M d_m,
\]
which has only finitely many prime divisors. This contradicts the infinitude of primes.

Since each fixed \(d_n\) has only finitely many prime divisors, unboundedness of \(f(p)\) implies that infinitely many distinct indices support a primitive prime. ∎

Thus the basic “private divisor” requirement from Route 2 is available unconditionally, at least relative to the preceding terms.

### 3. Denominator effect of a primitive prime

Let \(v_p\) denote the usual \(p\)-adic valuation on nonzero rational numbers.

#### Lemma 4

Suppose \(p\) is primitive at \(n\), and
\[
p^a\parallel d_n.
\]
Then
\[
v_p(S_n)=-a.
\]
If, in addition, \(\alpha=A/q\in\mathbb Q\) and \(p\nmid q\), then
\[
v_p(R_n)=-a.
\]

#### Proof

No denominator in \(S_{n-1}\) is divisible by \(p\), so
\[
v_p(S_{n-1})\ge0.
\]
On the other hand,
\[
v_p(1/d_n)=-a.
\]
The two valuations are unequal, hence
\[
v_p(S_n)
=v_p\left(S_{n-1}+\frac1{d_n}\right)
=\min\{v_p(S_{n-1}),-a\}
=-a.
\]

If \(\alpha=A/q\) and \(p\nmid q\), then \(v_p(\alpha)\ge0\). Therefore
\[
v_p(R_n)
=v_p(\alpha-S_n)
=\min\{v_p(\alpha),v_p(S_n)\}
=-a.
\]
∎

So rationality would force the real tail \(R_n\), in lowest terms, to retain the primitive prime power \(p^a\) in its denominator.

### 4. The sharp one-prime isolation criterion

Let
\[
S_{n-1}=\frac uv
\]
in lowest terms. Suppose \(p\) is primitive at \(n\), with
\[
p^a\parallel d_n,\qquad d_n=p^a c,\qquad p\nmid c.
\]
Define
\[
H:=\operatorname{lcm}(q,v,c).
\]

#### Proposition 5

If \(\alpha=A/q\in\mathbb Q\) and \(p\nmid q\), then
\[
\boxed{p^a H R_n\ge1.}
\]

#### Proof

Because \(p\) is primitive at \(n\), we have \(p\nmid v\), and by hypothesis \(p\nmid q c\). Hence \(p\nmid H\).

The numbers
\[
H\alpha=\frac{HA}{q}
\quad\text{and}\quad
HS_{n-1}=\frac{Hu}{v}
\]
are integers. Since \(c\mid H\),
\[
\frac{H}{d_n}
=\frac{H/c}{p^a}.
\]
Moreover \(p\nmid H/c\), so this rational has a nonzero fractional part whose denominator is \(p^a\).

From
\[
\alpha=S_{n-1}+\frac1{d_n}+R_n
\]
we obtain
\[
H\alpha-HS_{n-1}
=\frac{H/c}{p^a}+HR_n.
\]
The left side is an integer. Since \(HR_n>0\), it must carry the nonintegral number \((H/c)/p^a\) upward to an integer. The distance to the next integer is at least \(1/p^a\). Hence
\[
HR_n\ge\frac1{p^a},
\]
as claimed. ∎

This is the exact modular contradiction mechanism. It also isolates the required denominator estimate.

Since
\[
H\le q\,\operatorname{lcm}(v,c),
\]
a sufficient condition for irrationality would be the existence of infinitely many primitive pairs \((n,p)\) for which
\[
p^a\operatorname{lcm}(v,c)\,R_n\longrightarrow0.
\]
Using the explicit upper bound
\[
R_n\le
U_n:=
\frac{n+2}{(n+1)((n+1)!-1)}
=\frac{n+2}{(n+1)d_{n+1}},
\]
it would suffice to prove
\[
p^a\operatorname{lcm}(v,c)\,U_n\longrightarrow0.
\]

Now
\[
p^a\operatorname{lcm}(v,c)
=p^a c\,\frac{v}{\gcd(v,c)}
=d_n\,\frac{v}{\gcd(v,c)}.
\]
Thus the precise finite-denominator target is
\[
\boxed{
\frac{v}{\gcd(v,c)}=o(n)
}
\]
along infinitely many primitive indices. No such estimate was obtained. Computations suggest the opposite behavior.

### 5. Why termwise denominator clearing cannot work

#### Lemma 6

For \(2\le m<n\),
\[
\gcd(d_m,d_n)
=
\gcd\left(d_m,\frac{n!}{m!}-1\right).
\]
In particular,
\[
\gcd(d_m,d_{m+1})=1.
\]

#### Proof

Put \(P=n!/m!\). Modulo \(d_m=m!-1\), one has \(m!\equiv1\), and therefore
\[
n!-1=m!P-1\equiv P-1\pmod{d_m}.
\]
This proves the first identity.

For \(n=m+1\), we have \(P=m+1\), so
\[
\gcd(d_m,d_{m+1})
=\gcd(m!-1,m).
\]
But \(m!\equiv0\pmod m\), hence \(m!-1\equiv-1\pmod m\), and this gcd is \(1\). ∎

Consequently,
\[
L_N\ge d_{N-1}d_N.
\]

#### Lemma 7

For every \(N\ge5\),
\[
d_{N-1}d_N>d_{N+1}.
\]

#### Proof

Let \(x=(N-1)!\). Then
\[
d_{N-1}=x-1,\qquad d_N=Nx-1,\qquad d_{N+1}=N(N+1)x-1.
\]
Thus
\[
d_{N-1}d_N-d_{N+1}
=x\bigl(Nx-(N+1)^2\bigr)+2.
\]
For \(N\ge5\),
\[
Nx=N!>(N+1)^2;
\]
this holds at \(N=5\), since \(120>36\), and is preserved thereafter. Hence the displayed difference is positive. ∎

Since
\[
R_N>\frac1{d_{N+1}},
\]
Lemmas 6 and 7 give
\[
\boxed{L_NR_N>1\qquad(N\ge5).}
\]

Therefore clearing all preceding denominators term by term can never produce the inequality needed for a contradiction.

More explicitly, in Proposition 5 replace the reduced denominator \(v\) by the crude clearing denominator \(L_{n-1}\). Since
\[
\gcd(d_{n-1},d_n)=1
\]
and \(c\mid d_n\), one has
\[
d_{n-1}\mid
\frac{L_{n-1}}{\gcd(L_{n-1},c)}.
\]
Hence
\[
p^a\operatorname{lcm}(L_{n-1},c)
=d_n\frac{L_{n-1}}{\gcd(L_{n-1},c)}
\ge d_nd_{n-1}.
\]
For \(n\ge5\),
\[
p^a\operatorname{lcm}(L_{n-1},c)R_n
>
\frac{d_nd_{n-1}}{d_{n+1}}
>1.
\]
Thus even an arbitrarily large private prime power does not rescue the naive multiplier: its size appears both in the denominator spacing and in the multiplier and consequently cancels out.

### 6. Even the optimized method is blocked at many primitive indices

The reduced denominator \(v\) can only be smaller than \(L_{n-1}\) through cancellations. Those cancellations must be very substantial for Proposition 5 to help.

#### Lemma 8

Suppose \(d_{n-1}\) has a primitive prime divisor \(\ell\), with
\[
\ell^b\parallel d_{n-1}.
\]
Then \(\ell^b\) divides the reduced denominator \(v\) of \(S_{n-1}\).

#### Proof

No denominator in \(S_{n-2}\) is divisible by \(\ell\), so
\[
v_\ell(S_{n-2})\ge0.
\]
But
\[
v_\ell(1/d_{n-1})=-b.
\]
Therefore
\[
v_\ell(S_{n-1})=-b,
\]
which means precisely that \(\ell^b\mid v\). ∎

Because \(\gcd(d_{n-1},d_n)=1\), this \(\ell\) does not divide \(c\). Moreover Lemma 1 gives
\[
\ell\ge n+1.
\]
Consequently,
\[
\frac{v}{\gcd(v,c)}\ge\ell^b\ge n+1.
\]

For completeness, the resulting modular lower bound is already automatically satisfied.

#### Lemma 9

For every \(n\ge3\),
\[
(n+1)d_nR_n>1.
\]

#### Proof

It suffices to use the first two tail terms:
\[
R_n>\frac1{d_{n+1}}+\frac1{d_{n+2}}.
\]
The first contribution satisfies
\[
\frac{(n+1)d_n}{d_{n+1}}
=1-\frac{n}{d_{n+1}}.
\]
It remains to show
\[
\frac{(n+1)d_n}{d_{n+2}}>\frac{n}{d_{n+1}},
\]
or
\[
(n+1)d_nd_{n+1}>n d_{n+2}.
\]
For \(n\ge4\), put \(x=n!\). Then
\[
d_{n+1}=(n+1)x-1>nx,
\qquad
d_{n+2}<(n+2)(n+1)x.
\]
Since \(x-1>n+2\) for \(n\ge4\),
\[
(n+1)(x-1)d_{n+1}
>n(n+1)x(x-1)
>n(n+2)(n+1)x
>n d_{n+2}.
\]
The case \(n=3\) is checked directly:
\[
4\cdot5\cdot23>3\cdot119.
\]
This proves the claim. ∎

Thus, if both \(n-1\) and \(n\) support primitive primes, the optimized one-prime isolation at \(n\) cannot succeed:
\[
p^a\operatorname{lcm}(v,c)R_n
=d_n\frac{v}{\gcd(v,c)}R_n
\ge(n+1)d_nR_n>1.
\]

Potential successful indices must therefore exhibit unusually complete cancellation of all large denominator factors inherited from \(S_{n-1}\).

### 7. Why pure \(p\)-adic reasoning about the real tail is invalid

For \(m\ge p\),
\[
d_m=m!-1\equiv-1\pmod p.
\]
It is tempting to claim that a rational real sum of such \(p\)-integral terms must itself be \(p\)-integral. This is false even for positive unit fractions with much faster than factorial convergence.

#### Proposition 10

For every prime \(p\), there is a positive, superexponentially convergent series of unit fractions
\[
\frac1p=\sum_{j=1}^\infty\frac1{b_j}
\]
such that
\[
b_j\equiv-1\pmod p
\]
for every \(j\).

#### Proof

Define
\[
a_0=p,\qquad a_{k+1}=a_k(a_k+1).
\]
Then
\[
\frac1{a_k}
=
\frac1{a_k+1}+\frac1{a_{k+1}},
\]
so telescoping gives
\[
\frac1p
=\sum_{k=0}^{K}\frac1{a_k+1}+\frac1{a_{K+1}},
\]
and hence
\[
\frac1p=\sum_{k=0}^{\infty}\frac1{a_k+1}.
\]

Because \(p\mid a_k\), we have \(a_k+1\equiv1\pmod p\). Replace each term \(1/(a_k+1)\) by \(p-1\) identical terms
\[
\frac1{(p-1)(a_k+1)}.
\]
Their sum is \(1/(a_k+1)\), while each new denominator satisfies
\[
(p-1)(a_k+1)\equiv-1\pmod p.
\]

Finally, \(a_{k+1}>a_k^2\), so
\[
a_k>p^{2^k},
\]
and the remainder \(1/a_{K+1}\) decays superexponentially. ∎

Thus positivity, unit-fraction form, congruence \(b_j\equiv-1\pmod p\), and extremely rapid real convergence do not prevent the real sum from having \(p\) in its denominator. Any successful use of \(p\)-adic information must exploit more than these local facts; it must use the exact factorial-minus-one structure.

### Ledger

**Proved**

- Every prime divisor \(p\mid n!-1\) satisfies \(p\ge n+2\), recurs at \(p-2\), and never occurs later.
- Infinitely many \(n!-1\) possess a prime divisor absent from all preceding terms.
- A primitive \(p^a\) survives exactly in the reduced denominator of \(S_n\), and under rationality also in that of \(R_n\).
- The exact modular lower bound \(p^aHR_n\ge1\).
- Consecutive \(d_n\) are coprime.
- Full termwise denominator clearing is quantitatively incapable of proving irrationality for \(n\ge5\).
- If \(n-1\) also has a primitive prime, even optimized one-prime isolation at \(n\) is too expensive.
- Pure real-to-\(p\)-adic limit transfer is invalid in this setting without additional structure.

**Plausible but unproved**

- There may be infinitely many primes \(p\) whose first factorial residue \(1\) occurs only at \(p-2\), i.e. \(f(p)=p-2\).
- The principal \(p\)-adic parts of the finitely many terms \(1/(m!-1)\) with \(p\mid m!-1\) may often fail to cancel.
- Reduced denominators of \(S_N\) appear computationally close to the full lcm, but no useful lower bound of this strength is proved.

**Dead ends**

- A primitive prime by itself does not give a contradiction; its size cancels from the basic modular inequality.
- Clearing all earlier summands separately is defeated by the coprime consecutive denominators.
- Reducing the infinite real tail modulo \(p\) is invalid.
- Treating the real tail as a \(p\)-adic sum is invalid; its terms do not even tend to zero \(p\)-adically.

## Self-Audit

1. **The lcm obstruction applies only to termwise clearing, not every modular construction.**  
   This is the main limitation. I have not claimed otherwise: an optimized construction may clear only the reduced denominator of the aggregate \(S_{n-1}\), or use weighted combinations of several cutoffs. The obstruction is nevertheless rigorous for the most direct Route 2 implementation.

2. **The countermodel does not use the exact denominators \(m!-1\).**  
   It therefore does not disprove a theorem exploiting their full multiplicative structure. It does rigorously show that positivity, rapid convergence, unit fractions, and the congruence \(-1\bmod p\) alone cannot justify a \(p\)-integrality conclusion.

3. **The unresolved denominator condition may conceivably hold on a sparse subsequence.**  
   The condition
   \[
   \frac{\operatorname{den}(S_{n-1})}
   {\gcd(\operatorname{den}(S_{n-1}),\,d_n/p^a)}=o(n)
   \]
   looks very unlikely numerically, and Lemma 8 rules it out whenever \(n-1\) has a primitive prime. But there is no proof that all primitive indices are covered by such obstructions. This is the precise remaining gap, not a hidden assumption in the proved lemmas.

## Computations To Verify

The following Python code checks the incidence, primitive-prime, denominator-growth, and isolation quantities exactly.

```python
from math import factorial, gcd, lcm
from fractions import Fraction
from sympy import factorint, primerange

def vp_int(x, p):
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e

def vp_fraction(x, p):
    return vp_int(abs(x.numerator), p) - vp_int(x.denominator, p)

# 1. Exact partial sums, primitive primes, and denominator scores.
NMAX = 14
S = Fraction(0, 1)
L = 1
seen_primes = set()

for n in range(2, NMAX + 1):
    d = factorial(n) - 1
    fac = factorint(d)
    primitive = [p for p in fac if p not in seen_primes]

    Qprev = S.denominator
    Lprev = L

    print(f"\nn={n}, d_n={d}")
    print("factorization:", fac)
    print("primitive primes:", primitive)
    print("den(S_{n-1}) =", Qprev)

    # Tail bounds for R_n.
    dnext = factorial(n + 1) - 1
    Rlo = Fraction(1, dnext)
    Rup = Fraction(n + 2, (n + 1) * dnext)

    for p in primitive:
        a = fac[p]
        pa = p ** a
        c = d // pa

        # Optimized aggregate multiplier, excluding the unknown q.
        H0 = lcm(Qprev, c)
        A0 = pa * H0

        # Equivalent formula A0 = d_n * Qprev/gcd(Qprev,c).
        assert A0 == d * (Qprev // gcd(Qprev, c))

        print(
            f"  p={p}, exponent={a}, c={c}, "
            f"A0*Rlo={A0 * Rlo}, A0*Rup={A0 * Rup}"
        )

        # Crude termwise-clearing multiplier.
        Hterm = lcm(Lprev, c)
        Aterm = pa * Hterm
        print(
            f"    termwise: Aterm*Rlo={Aterm * Rlo}, "
            f"Aterm*Rup={Aterm * Rup}"
        )

    S += Fraction(1, d)
    L = lcm(L, d)
    seen_primes.update(fac)

    print("den(S_n) =", S.denominator)
    print("L_n * lower tail bound =", L * Rlo)
    print("L_n * upper tail bound =", L * Rup)

# 2. Verify the exact gcd identity and consecutive coprimality.
for m in range(2, 12):
    for n in range(m + 1, 13):
        dm = factorial(m) - 1
        dn = factorial(n) - 1
        P = factorial(n) // factorial(m)
        assert gcd(dm, dn) == gcd(dm, P - 1)

for n in range(3, 20):
    assert gcd(factorial(n - 1) - 1, factorial(n) - 1) == 1

# 3. Verify d_{N-1} d_N > d_{N+1}.
for N in range(5, 30):
    assert (
        (factorial(N - 1) - 1) * (factorial(N) - 1)
        > factorial(N + 1) - 1
    )

# 4. Factorial-residue incidence for each prime.
for p in primerange(5, 200):
    r = 1
    occurrences = []
    for m in range(1, p):
        r = (r * m) % p
        if m >= 2 and r == 1:
            occurrences.append(m)

    assert occurrences
    assert occurrences[-1] == p - 2
    print(
        f"p={p}, first={occurrences[0]}, "
        f"occurrences={occurrences}"
    )

# 5. Check principal p-adic cancellation among all p-pole terms.
# C_p = sum_{m: p | m!-1} 1/(m!-1).
for p in primerange(5, 100):
    facts = [1] * p
    f = 1
    for m in range(1, p):
        f *= m
        facts[m] = f

    occ = [m for m in range(2, p - 1) if (facts[m] - 1) % p == 0]
    assert occ[-1] == p - 2

    exponents = {m: vp_int(facts[m] - 1, p) for m in occ}
    A = max(exponents.values())

    # Coefficient of p^{-A} modulo p.
    lead = 0
    for m in occ:
        if exponents[m] == A:
            unit = (facts[m] - 1) // (p ** A)
            lead += pow(unit % p, -1, p)
    lead %= p

    print(
        f"p={p}, first={occ[0]}, occ={occ}, "
        f"max exponent={A}, leading residue={lead}"
    )

    # Exact check for modest p.
    if p < 45:
        C = sum((Fraction(1, facts[m] - 1) for m in occ), Fraction(0, 1))
        print("   exact v_p(C_p) =", vp_fraction(C, p))

# 6. Verify the explicit p-adic countermodel.
for p in [5, 7, 11]:
    a = p
    partial = Fraction(0, 1)

    for k in range(8):
        b = (p - 1) * (a + 1)
        assert b % p == p - 1

        # p-1 repeated copies of 1/b.
        partial += Fraction(p - 1, b)

        anew = a * (a + 1)
        assert Fraction(1, p) - partial == Fraction(1, anew)
        a = anew

    print(f"p={p}, remainder after 8 blocks =", Fraction(1, p) - partial)
```

The most informative experimental quantities are:

- the first-occurrence function \(f(p)\);
- the frequency of consecutive primitive indices;
- the exact ratio
  \[
  \frac{\operatorname{den}(S_{n-1})}
       {\gcd(\operatorname{den}(S_{n-1}),\,d_n/p^a)};
  \]
- the leading \(p\)-adic residue of the sum over all occurrences of \(p\);
- whether any primitive indices make
  \[
  p^a\operatorname{lcm}\!\left(
  \operatorname{den}(S_{n-1}),d_n/p^a
  \right)U_n
  \]
  unusually small.

## Route Diagnosis

The prime-divisor part worked better than expected: infinitely many primitive primes exist by an elementary Wilson-theorem argument, and their incidence has a rigid final occurrence at \(p-2\). The route fails not because private primes are unavailable, but because converting their nonzero residue into an archimedean contradiction requires a multiplier. Clearing terms individually is provably too expensive, already because \(d_{N-1}d_N>d_{N+1}\). Clearing only the reduced preceding partial sum could be cheaper, but success requires exceptionally strong and presently uncontrolled cancellation in \(\operatorname{den}(S_{n-1})\). Replacing that missing estimate by a claim that rational real tails are \(p\)-integral is invalid and is refuted by Proposition 10.

A fresh Route 2 attempt should therefore avoid a single-cutoff common denominator. The most plausible possibilities are:

1. construct a weighted combination of several cutoffs in which the costly consecutive denominators cancel exactly;
2. use several primitive primes simultaneously and obtain quantitative CRT information about the least positive residue, not merely its nonvanishing;
3. analyze the complete finite occurrence set
   \[
   \{m: p\mid m!-1\}
   \]
   and prove a structured noncancellation theorem strong enough to interact with a specially chosen real tail;
4. hybridize the modular information with Padé or moment weights so that denominator clearing occurs only after analytic annihilation of most head terms.

Absent such a new mechanism, Route 2 reduces to a denominator-cancellation statement of comparable difficulty to the original irrationality problem.