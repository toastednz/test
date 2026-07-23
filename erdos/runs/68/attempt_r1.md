STATUS: BLOCKED

## Result

I obtained an exact Route 1 reformulation. From the rational partial sums alone, define \(B_m=\lceil m!S_m\rceil\) and \(\varepsilon_m=B_m-m!S_m\). Then
\[
\alpha\in\mathbb Q
\iff
\frac1{m+1}<\varepsilon_m<\frac1m
\quad\text{for every sufficiently large }m,
\]
equivalently \(m\varepsilon_m\to1\), equivalently an explicit signed factorial-digit sequence is eventually zero. This gives a sharp, entirely finite residue problem and rigorous finite certificates excluding rational denominators. However, proving that the residues escape the shrinking interval infinitely often is exactly equivalent to the original irrationality problem. Standard denominator clearing is provably ineffective: the least common denominator of the first \(N\) summands already enlarges the omitted tail beyond \(1\) for every \(N\ge5\). Thus Route 1 is blocked at a precise modular anti-concentration statement.

## Complete Argument

Write
\[
d_n=n!-1,\qquad
S_m=\sum_{n=2}^m\frac1{d_n},\qquad
R_m=\alpha-S_m,
\]
and set
\[
\delta_m:=m!R_m.
\]

### 1. Sharp localization of the scaled tail

**Lemma 1.** For every \(m\ge3\),
\[
\boxed{\frac1{m+1}<\delta_m<\frac1m.}
\]

**Proof.** The first omitted term gives
\[
\delta_m
>
\frac{m!}{(m+1)!-1}
>
\frac1{m+1}.
\]

For the upper bound, apply the stated tail estimate with \(N=m\):
\[
R_m\le
\frac1{1-1/(m+1)!}\,
\frac{m+2}{(m+1)(m+1)!}.
\]
Multiplying by \(m!\) gives
\[
\delta_m
\le
\frac{m+2}{(m+1)^2}\,
\frac1{1-1/(m+1)!}.
\]
Let \(F=(m+1)!\). This upper bound is less than \(1/m\) precisely when
\[
m(m+2)F<(m+1)^2(F-1).
\]
The difference between the right and left sides is
\[
\bigl((m+1)^2-m(m+2)\bigr)F-(m+1)^2
=F-(m+1)^2>0
\]
for \(m\ge3\). Hence \(\delta_m<1/m\). ∎

The restriction \(m\ge3\) is necessary for this particular bound: numerically \(\delta_2=2(\alpha-1)>1/2\).

---

### 2. A signed factorial expansion determined by finite partial sums

Define
\[
x_m:=m!S_m,\qquad
B_m:=\lceil x_m\rceil,\qquad
\varepsilon_m:=B_m-x_m.
\]
Thus
\[
0\le\varepsilon_m<1.
\]
All these quantities are exactly computable rational numbers and do not involve \(\alpha\).

For \(m\ge3\), put
\[
c_m:=\frac{m!}{m!-1}=1+\frac1{m!-1}.
\]
Since
\[
x_m=m x_{m-1}+c_m,
\]
define the integer
\[
a_m:=B_m-mB_{m-1}.
\]

**Lemma 2.** For \(m\ge3\),
\[
\boxed{a_m=\left\lceil c_m-m\varepsilon_{m-1}\right\rceil}
\]
and
\[
\boxed{\varepsilon_m=a_m-c_m+m\varepsilon_{m-1}.}
\]
Moreover,
\[
2-m\le a_m\le2.
\]

**Proof.** Since \(x_{m-1}=B_{m-1}-\varepsilon_{m-1}\),
\[
x_m
=mB_{m-1}+c_m-m\varepsilon_{m-1}.
\]
Taking ceilings and using that \(mB_{m-1}\) is integral gives
\[
B_m=mB_{m-1}
+\left\lceil c_m-m\varepsilon_{m-1}\right\rceil.
\]
This proves the first identity, and subtracting \(x_m\) proves the second.

Because \(0\le\varepsilon_{m-1}<1\) and \(1<c_m<2\),
\[
1-m<c_m-m\varepsilon_{m-1}<2.
\]
Taking ceilings gives \(2-m\le a_m\le2\). ∎

Dividing \(B_m=mB_{m-1}+a_m\) by \(m!\) gives
\[
\frac{B_m}{m!}
=
\frac{B_{m-1}}{(m-1)!}+\frac{a_m}{m!}.
\]
Now \(S_2=1\), \(B_2=2\), and hence \(B_2/2!=1\). Also,
\[
0\le\frac{B_m}{m!}-S_m<\frac1{m!},
\]
so \(B_m/m!\to\alpha\). Therefore
\[
\boxed{\alpha=1+\sum_{m=3}^\infty\frac{a_m}{m!}.}
\]
The series is absolutely convergent because \(|a_m|\le m\).

This is not the usual nonnegative factorial expansion; its advantage is that its digits are obtained from finite partial sums and have no endpoint ambiguity.

---

### 3. Exact rationality criteria

**Theorem 3.** The following statements are equivalent:

1. \(\alpha\in\mathbb Q\).
2. \(a_m=0\) for every sufficiently large \(m\).
3. \(B_m/m!\) is eventually constant.
4. For every sufficiently large \(m\),
   \[
   \boxed{\frac1{m+1}<\varepsilon_m<\frac1m.}
   \]
5. One has
   \[
   \boxed{\lim_{m\to\infty}m\varepsilon_m=1.}
   \]

**Proof.**

#### \(1\Rightarrow2,4,5\)

Suppose \(\alpha=p/q\), with \(q>0\). For every \(m\ge q\), \(q\mid m!\), so \(m!\alpha\) is an integer. Since
\[
x_m=m!S_m=m!\alpha-\delta_m
\]
and \(0<\delta_m<1\), it follows that
\[
B_m=\lceil x_m\rceil=m!\alpha
\]
for every sufficiently large \(m\). Consequently,
\[
\varepsilon_m=B_m-x_m=\delta_m.
\]
Lemma 1 therefore gives
\[
\frac1{m+1}<\varepsilon_m<\frac1m.
\]
It also gives
\[
\frac{m}{m+1}<m\varepsilon_m<1,
\]
so \(m\varepsilon_m\to1\).

Finally, for all sufficiently large \(m\),
\[
B_m=m!\alpha=m(m-1)!\alpha=mB_{m-1},
\]
hence \(a_m=0\).

#### \(2\Leftrightarrow3\)

This follows immediately from
\[
\frac{B_m}{m!}-\frac{B_{m-1}}{(m-1)!}
=\frac{a_m}{m!}.
\]

#### \(3\Rightarrow1\)

If \(B_m/m!\) is eventually equal to a rational constant \(C\), then its limit is \(C\). But \(B_m/m!\to\alpha\), so \(\alpha=C\in\mathbb Q\).

#### \(4\Rightarrow2\)

Assume the displayed interval contains \(\varepsilon_m\) for every sufficiently large \(m\). For such \(m\), both \(\varepsilon_{m-1}\) and \(\varepsilon_m\) satisfy their corresponding bounds. From Lemma 2,
\[
a_m=\varepsilon_m+c_m-m\varepsilon_{m-1}.
\]
Using
\[
\varepsilon_m>\frac1{m+1},\quad
c_m>1,\quad
\varepsilon_{m-1}<\frac1{m-1},
\]
we obtain
\[
a_m>
\frac1{m+1}+1-\frac{m}{m-1}
=-\frac{2}{m^2-1}>-1.
\]
On the other hand,
\[
\varepsilon_m<\frac1m,\quad
c_m=1+\frac1{m!-1},\quad
m\varepsilon_{m-1}>1,
\]
give
\[
a_m<
\frac1m+\frac1{m!-1}<1
\]
for \(m\ge3\). Since \(a_m\) is an integer, \(a_m=0\).

#### \(5\Rightarrow2\)

The hypothesis implies \(\varepsilon_m\to0\). It also implies
\[
m\varepsilon_{m-1}
=
\frac{m}{m-1}\bigl((m-1)\varepsilon_{m-1}\bigr)
\longrightarrow1.
\]
Since \(c_m\to1\),
\[
a_m=\varepsilon_m+c_m-m\varepsilon_{m-1}\longrightarrow0.
\]
The \(a_m\) are integers, so they are eventually zero. ∎

Thus Route 1 has been reduced to the following exact finite statement:
\[
\boxed{
\alpha\notin\mathbb Q
\iff
\varepsilon_m\notin
\left(\frac1{m+1},\frac1m\right)
\text{ for infinitely many }m.
}
\]

This is much narrower than merely proving \(\varepsilon_m\ne0\): the interval has length \(1/(m(m+1))\).

---

### 4. Finite denominator-exclusion certificates

Since
\[
m!\alpha=x_m+\delta_m=B_m-\varepsilon_m+\delta_m,
\]
Lemma 1 immediately gives:

**Corollary 4.** If \(m\ge3\) and
\[
\varepsilon_m\le\frac1{m+1}
\quad\text{or}\quad
\varepsilon_m\ge\frac1m,
\]
then \(m!\alpha\notin\mathbb Z\). Consequently, \(\alpha\) cannot have any reduced denominator dividing \(m!\); in particular, it cannot have denominator at most \(m\).

**Proof.** If \(\varepsilon_m\le1/(m+1)\), then
\[
0<\delta_m-\varepsilon_m<1,
\]
so \(m!\alpha\) lies strictly between \(B_m\) and \(B_m+1\). If \(\varepsilon_m\ge1/m\), then
\[
0<\varepsilon_m-\delta_m<1,
\]
so \(m!\alpha\) lies strictly between \(B_m-1\) and \(B_m\). ∎

As a small exact example,
\[
B_5=151,\qquad
\varepsilon_5=\frac{2119}{2737}>\frac15.
\]
Thus \(120\alpha\notin\mathbb Z\), excluding every reduced denominator dividing \(120\). This is only a finite check, not an irrationality proof.

The initial signed digits are
\[
(a_3,\ldots,a_{12})
=
(2,-2,1,-3,-3,-3,1,-3,-7,-10).
\]
They already refute tempting monotonicity, positivity, or fixed-sign conjectures.

---

### 5. Exact modular form of the obstruction

Let
\[
D_m:=\operatorname{lcm}(d_2,\ldots,d_m),\qquad
U_m:=\sum_{n=2}^m\frac{D_m}{d_n}\in\mathbb Z.
\]
Then
\[
x_m=\frac{m!U_m}{D_m}.
\]
Let \(r_m\) be the least nonnegative residue of \(m!U_m\) modulo \(D_m\). Therefore
\[
\varepsilon_m=
\begin{cases}
0,&r_m=0,\\[4pt]
\dfrac{D_m-r_m}{D_m},&r_m>0.
\end{cases}
\]

For \(r_m>0\), the rationality window becomes
\[
\frac1{m+1}<\frac{D_m-r_m}{D_m}<\frac1m,
\]
or equivalently
\[
\boxed{
D_m-\frac{D_m}{m}
<
r_m
<
D_m-\frac{D_m}{m+1}.
}
\]

Hence the exact missing lemma is:

> Prove that the explicitly defined residue \(r_m\) fails to lie in this short interval immediately below \(D_m\) for infinitely many \(m\).

By Theorem 3, this statement is not merely sufficient; it is equivalent to the desired irrationality.

---

### 6. Why ordinary denominator clearing fails

First, consecutive factorial-minus-one numbers are coprime.

**Lemma 5.** For \(n\ge3\),
\[
\gcd(n!-1,(n-1)!-1)=1.
\]

**Proof.** A common divisor divides
\[
(n!-1)-n\bigl((n-1)!-1\bigr)=n-1.
\]
But every prime divisor of \((n-1)!-1\) exceeds \(n-1\), since every prime at most \(n-1\) divides \((n-1)!\). Thus no prime can divide both quantities. ∎

It follows that
\[
D_N\ge (N!-1)((N-1)!-1).
\]

**Lemma 6.** For every \(N\ge5\),
\[
\boxed{D_NR_N>1.}
\]

**Proof.** Since \(R_N>1/((N+1)!-1)\),
\[
D_NR_N>
\frac{(N!-1)((N-1)!-1)}{(N+1)!-1}.
\]
Let \(A=(N-1)!\). The numerator minus the denominator in the last ratio is
\[
(NA-1)(A-1)-\bigl(N(N+1)A-1\bigr)
=
A\bigl(NA-(N+1)^2\bigr)+2.
\]
For \(N\ge5\), \(NA=N!>(N+1)^2\), so this is positive. ∎

Thus multiplying by the least common denominator \(D_N\) clears the first \(N\) terms but makes the omitted positive tail larger than \(1\). The usual “nonzero integer of absolute value below \(1\)” mechanism cannot work with this multiplier.

There is one limited prime-isolation fact.

**Lemma 7.** Suppose a prime \(p\mid d_m\) divides none of \(d_2,\ldots,d_{m-1}\). Then \(p\) remains in the reduced denominator of \(m!S_m\).

**Proof.** Write \(p^a\Vert d_m\). Since \(p\nmid D_{m-1}\), one has \(p^a\Vert D_m\). In
\[
U_m=\sum_{n=2}^m\frac{D_m}{d_n},
\]
every term with \(n<m\) is divisible by \(p\), while \(D_m/d_m\) is not. Hence \(p\nmid U_m\). Also \(p>m\), so \(p\nmid m!\). Therefore \(p\nmid m!U_m\), while \(p\mid D_m\). ∎

This proves denominator survival but gives no control over where \(r_m\) lies modulo \(D_m\). Even infinitely many private primes would therefore not, by itself, complete Route 1.

Finally, if \(a_j=0\) throughout a run \(M<j\le K\), then Lemma 2 gives
\[
\frac{\varepsilon_j}{j!}
=
\frac{\varepsilon_{j-1}}{(j-1)!}
-\frac1{j!-1}.
\]
Consequently,
\[
\frac{\varepsilon_M}{M!}
=
\sum_{j=M+1}^K\frac1{j!-1}
+\frac{\varepsilon_K}{K!}.
\]
An infinite zero run would force
\[
\frac{\varepsilon_M}{M!}=R_M.
\]
The left side is rational. Proving this impossible is precisely proving irrationality of the tail \(R_M\), hence of \(\alpha\). The expanding recurrence does not supply an independent contradiction.

## Self-Audit

1. **The tail bound is the most delicate inequality.** The upper estimate fails in the claimed form at \(m=2\), so the threshold \(m\ge3\) matters. For \(m\ge3\), however, the reduction to \((m+1)!>(m+1)^2\) is exact.

2. **The eventual-window equivalence could hide an endpoint issue.** It does not: rationality gives strict inequalities because the tail bounds are strict, while equality at either endpoint in Corollary 4 still certifies nonintegrality. The ceiling convention also handles the case \(m!S_m\in\mathbb Z\).

3. **The common-denominator obstruction does not rule out all sophisticated multipliers.** Lemma 6 only kills the direct multiplier \(D_N\) and larger multiples of it; a selective multiplier or modular isolation argument might still work. I believe the lemma itself is sound, but its diagnostic scope is intentionally limited.

## Computations To Verify

```python
from fractions import Fraction
from math import factorial, lcm

def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)

def route1_data(M):
    S = Fraction(0)
    previous_B = None
    D = 1
    denominators = []

    for m in range(2, M + 1):
        F = factorial(m)
        d = F - 1
        S += Fraction(1, d)

        x = F * S
        B = ceil_fraction(x)
        eps = Fraction(B) - x
        assert 0 <= eps < 1

        if previous_B is None:
            signed_digit = None
        else:
            signed_digit = B - m * previous_B
            c = Fraction(F, F - 1)
            assert signed_digit == ceil_fraction(c - m * previous_eps)
            assert eps == signed_digit - c + m * previous_eps

        denominators.append(d)
        D = lcm(D, d)
        U = sum(D // q for q in denominators)
        residue = (F * U) % D
        eps_from_residue = (
            Fraction(0) if residue == 0
            else Fraction(D - residue, D)
        )
        assert eps == eps_from_residue

        outside = None
        if m >= 3:
            outside = (
                eps <= Fraction(1, m + 1)
                or eps >= Fraction(1, m)
            )

        print({
            "m": m,
            "B_m": B,
            "a_m": signed_digit,
            "epsilon_exact": eps,
            "epsilon_decimal": float(eps),
            "m_times_epsilon": float(m * eps),
            "outside_rationality_window": outside,
            "residue": residue,
            "D_digits": len(str(D)),
        })

        previous_B = B
        previous_eps = eps

# Exact initial search
route1_data(30)
```

Certified intervals for arbitrary \(m!\alpha\):

```python
def certified_orbit_interval(m, N):
    """
    Returns lo, hi such that lo < m!*alpha <= hi.
    Requires N >= max(m, 2).
    """
    assert N >= max(m, 2)

    S = sum(
        (Fraction(1, factorial(n) - 1) for n in range(2, N + 1)),
        Fraction(0)
    )

    t = N + 1
    Ft = factorial(t)

    lower_alpha = S + Fraction(1, Ft - 1)
    upper_alpha = S + Fraction(t + 1, t * (Ft - 1))

    Fm = factorial(m)
    return Fm * lower_alpha, Fm * upper_alpha

def interval_contains_integer(lo, hi):
    # The interval is (lo, hi].
    first_possible = lo.numerator // lo.denominator + 1
    last_possible = hi.numerator // hi.denominator
    return first_possible <= last_possible

for m in range(3, 31):
    lo, hi = certified_orbit_interval(m, m + 8)
    print(m, interval_contains_integer(lo, hi), lo, hi)
```

Checks of the denominator obstruction:

```python
for N in range(3, 20):
    dNm1 = factorial(N - 1) - 1
    dN = factorial(N) - 1
    dNp1 = factorial(N + 1) - 1

    from math import gcd
    assert gcd(dNm1, dN) == 1

    ratio = Fraction(dNm1 * dN, dNp1)
    if N >= 5:
        assert ratio > 1

    print(N, ratio, float(ratio))
```

Primitive-prime incidence search:

```python
# Requires sympy
from sympy import factorint

seen_primes = set()
for n in range(2, 40):
    d = factorial(n) - 1
    factors = factorint(d)
    private = [p for p in factors if p not in seen_primes]

    print({
        "n": n,
        "factorization": factors,
        "private_primes": private,
    })

    seen_primes.update(factors)
```

The most relevant large computation is to search for:

- indices with \(a_m=0\);
- lengths of consecutive zero runs;
- indices where \(\varepsilon_m\) lies inside the rationality window;
- the behavior of \(m\varepsilon_m-1\);
- residues \(r_m\) in the short interval
  \[
  D_m-D_m/m<r_m<D_m-D_m/(m+1).
  \]

No finite search can prove irrationality, but it can refute proposed monotonicity or periodicity lemmas immediately.

## Route Diagnosis

**Proved ledger**

- The scaled tail satisfies
  \[
  1/(m+1)<m!R_m<1/m
  \]
  for every \(m\ge3\).
- The finite quantities \(B_m,\varepsilon_m,a_m\) give an exact signed factorial expansion of \(\alpha\).
- Rationality is equivalent to eventual vanishing of \(a_m\), eventual trapping of \(\varepsilon_m\) in \((1/(m+1),1/m)\), and \(m\varepsilon_m\to1\).
- The trapping condition is an explicit modular condition on \(r_m\bmod D_m\).
- Consecutive numbers \(n!-1\) and \((n-1)!-1\) are coprime.
- Clearing the full head with \(D_N\) makes the scaled tail exceed \(1\) for \(N\ge5\).
- A genuinely private prime divisor of \(m!-1\) survives in the denominator of \(m!S_m\).

**Plausible but unproved**

- The residues \(r_m\) should escape their shrinking terminal interval infinitely often.
- Long zero runs of the signed digits should be rare.
- Primitive prime divisors may occur often enough to help, but denominator survival alone is insufficient.

**Dead ends**

- Multiplication by \(m!\) does not clear the finite head.
- Multiplication by the least common denominator clears the head but destroys tail smallness.
- Positivity and the expanding recurrence do not prove nonvanishing: an infinite zero branch is exactly the equality \(\varepsilon_M/M!=R_M\), which is the original irrationality question for a tail.
- Private divisors control denominator support but not the required residue location.

**Precise block**

Route 1 now requires a theorem showing that
\[
r_m\notin
\left(D_m-\frac{D_m}{m},\,
      D_m-\frac{D_m}{m+1}\right)
\]
for infinitely many \(m\). This is exactly equivalent to irrationality, and no available congruence or monotonicity controls these residues. A fresh attempt should combine the residue formulation with genuinely new prime-factor incidence information—stronger than mere existence of private primes—or find selective multipliers that isolate a short block without paying the full \(D_N\) tail cost.