STATUS: BLOCKED

## Result

Cyclotomic and primitive-divisor methods give a strong classification of possible higher prime powers \(n-1=p^a\). In particular, I prove that \(2^a+1\) is a barrier exactly for \(1\le a\le7\); that the barriers with \(n-1=p^2\) are exactly \(5,10,26,50,290\); and that the only barriers whose canonical prime-power exponent is composite are \(17,65,82\). Consequently, every barrier \(n>290\) has either \(n-1\) prime, or
\[
n-1=p^\ell
\]
with \(p,\ell\) odd primes, \(p\) a Fermat prime, and \(\Phi_\ell(p)\) a power of a single odd prime. Further shifted factorization restricts the exponent; for example, when \(p=3\), necessarily \(\ell=3\) or \((\ell-1)/2\) is prime. This is a substantial reduction, but it does not address the likely dominant case \(n-1\) prime, and the surviving higher-power family involves unresolved prime-power values of cyclotomic polynomials. Thus Route 4 is blocked as a route to the full infinitude problem.

## Complete Argument

### 1. Primitive-divisor lower bounds

Write \(\tau(a)\) for the number of positive divisors of \(a\).

I use the following standard form of the Bang–Zsigmondy theorem.

> **Bang–Zsigmondy theorem.**  
> If \(x>y>0\), \(\gcd(x,y)=1\), and \(d>1\), then \(x^d-y^d\) has a prime divisor which divides none of
> \[
> x-y,x^2-y^2,\ldots,x^{d-1}-y^{d-1},
> \]
> except in the following cases:
> 1. \(d=2\) and \(x+y\) is a power of \(2\);
> 2. \((x,y,d)=(2,1,6)\).

Such a prime is called primitive for exponent \(d\). Primitive divisors belonging to different exponents are distinct, since their multiplicative orders are different.

#### Lemma 1

For a prime \(p\) and \(a\ge2\):

1. If \(p\) is odd, then
   \[
   \omega(p^a-1)\ge
   \omega(p-1)+\tau(a)-1-\delta,
   \]
   where
   \[
   \delta=
   \begin{cases}
   1,&2\mid a\text{ and }p+1\text{ is a power of }2,\\
   0,&\text{otherwise}.
   \end{cases}
   \]

2. If \(p=2\), then
   \[
   \omega(2^a-1)\ge \tau(a)-1-\mathbf 1_{6\mid a}.
   \]

#### Proof

For every divisor \(d>1\) of \(a\), a primitive prime divisor of \(p^d-1\), when it exists, also divides \(p^a-1\). Primitive divisors for distinct \(d\) are distinct, and none divides \(p-1\).

There are \(\tau(a)-1\) divisors \(d>1\) of \(a\). For odd \(p\), the only possible missing primitive divisor is at \(d=2\), when \(p+1\) is a power of \(2\). The primes dividing \(p-1\) supply a further \(\omega(p-1)\) distinct primes.

For \(p=2\), \(p-1=1\) contributes nothing, the \(d=2\) exception does not occur because \(2+1=3\) is not a power of \(2\), and the only possible missing exponent is \(d=6\). ∎

---

### 2. Classification under the second barrier condition

For a barrier \(n=p^a+1\), the offset \(j=2\) requires
\[
\omega(p^a-1)\le2.
\]
We now classify the implications of this condition.

### Proposition 2: odd bases

Let \(p\) be an odd prime, \(a\ge2\), and suppose
\[
\omega(p^a-1)\le2.
\]
Then precisely one of the following structural alternatives holds:

1. \(a=2\) and
   \[
   p\in\{3,5,7,17\};
   \]
2. \(a\) is an odd prime, \(p\) is a Fermat prime, and
   \[
   \Phi_a(p)=R^v
   \]
   for some odd prime \(R\) and \(v\ge1\);
3. \((p,a)=(3,4)\).

Conversely, all pairs in cases 1 and 3 satisfy \(\omega(p^a-1)\le2\), and the condition in case 2 is also sufficient.

#### Proof

By Lemma 1 and \(\omega(p-1)\ge1\), if the Zsigmondy exception at \(d=2\) does not occur, then
\[
2\ge \omega(p^a-1)\ge 1+\tau(a)-1=\tau(a).
\]
Thus \(\tau(a)\le2\), so \(a\) is prime.

If the exception does occur, then \(2\mid a\), \(p+1\) is a power of \(2\), and
\[
2\ge \omega(p^a-1)\ge 1+\tau(a)-2=\tau(a)-1.
\]
Thus \(\tau(a)\le3\). Since \(a\) is even, this leaves \(a=2\) or \(a=4\).

#### The case \(a=4\)

Suppose \(a=4\). Since this is only an additional possibility in the exceptional case, \(p+1\) is a power of \(2\).

A primitive divisor for exponent \(4\) exists and is an odd prime not dividing \(p-1\). If \(p-1\) had an odd prime divisor, then \(p^4-1\) would be divisible by \(2\), that odd prime, and the primitive divisor for exponent \(4\), contradicting \(\omega(p^4-1)\le2\). Hence \(p-1\) is also a power of \(2\).

Thus
\[
p-1=2^u,\qquad p+1=2^v.
\]
Their difference is \(2\), so
\[
2^u(2^{v-u}-1)=2.
\]
It follows that \(u=1\) and \(v=2\), hence \(p=3\). Indeed,
\[
3^4-1=80=2^4\cdot5.
\]

#### The case where \(a\) is an odd prime

Factor
\[
p^a-1=(p-1)\Phi_a(p).
\]
The Zsigmondy theorem supplies a prime divisor of \(\Phi_a(p)\) not dividing \(p-1\). Therefore \(\omega(p-1)\le1\). Since \(p-1\) is even,
\[
p-1=2^u.
\]
As \(p=2^u+1\) is prime, \(u\) must itself be a power of \(2\): if \(u=2^s t\) with odd \(t>1\), then
\[
2^u+1=(2^{2^s})^t+1
\]
is divisible by \(2^{2^s}+1\). Thus \(p\) is a Fermat prime.

Because \(a\) and \(p\) are odd,
\[
\Phi_a(p)=1+p+\cdots+p^{a-1}
\]
is odd. Since the only prime divisor of \(p-1\) is \(2\), the bound \(\omega(p^a-1)\le2\) is equivalent to \(\Phi_a(p)\) having only one distinct prime divisor:
\[
\Phi_a(p)=R^v
\]
for an odd prime \(R\).

#### The case \(a=2\)

Here
\[
p^2-1=(p-1)(p+1).
\]
For \(p=3\), this is \(8\), so \(p=3\) works.

Suppose \(p>3\). Exactly one of \(p-1,p+1\) is divisible by \(3\). Since the total number of distinct prime divisors is at most two and \(2\) divides both neighboring even numbers, the only possible odd prime divisor is \(3\). The neighbor not divisible by \(3\) must therefore be a power of \(2\). Since that neighbor exceeds \(2\), it is divisible by \(4\), so the other neighbor has \(2\)-adic valuation exactly one.

Thus one of the following equations holds:
\[
p-1=2^u,\qquad p+1=2\cdot3^v,
\]
or
\[
p-1=2\cdot3^v,\qquad p+1=2^u,
\]
with \(u\ge2\) and \(v\ge1\).

In the first case,
\[
2^{u-1}+1=3^v.
\]
Put \(k=u-1\). If \(k=1\), then \(v=1\), giving \(p=5\). If \(k=2\), there is no solution. If \(k\ge3\), reduction modulo \(8\) shows that \(v\) is even, say \(v=2t\). Then
\[
(3^t-1)(3^t+1)=2^k.
\]
Both factors are powers of \(2\) differing by \(2\), hence they are \(2\) and \(4\). Thus \(t=1\), \(v=2\), \(k=3\), and \(p=17\).

In the second case,
\[
3^v+1=2^{u-1}.
\]
If \(v\) is even, the left side is \(2\bmod 8\), impossible for a power of \(2\) at least \(4\). If \(v\) is odd, the left side is \(4\bmod8\), so \(u-1=2\). Hence \(v=1\) and \(p=7\).

Therefore
\[
p\in\{3,5,7,17\}.
\]
Directly,
\[
\begin{aligned}
3^2-1&=2^3,\\
5^2-1&=2^3\cdot3,\\
7^2-1&=2^4\cdot3,\\
17^2-1&=2^5\cdot3^2.
\end{aligned}
\]
This completes the proof. ∎

---

### Proposition 3: base \(2\)

Let \(a\ge2\). If
\[
\omega(2^a-1)\le2,
\]
then
\[
a\text{ is prime},\qquad a=\ell^2\text{ for a prime }\ell,\qquad\text{or}\qquad a=6.
\]

In the square case \(a=\ell^2\), the condition is equivalent to
\[
2^\ell-1\text{ being prime}
\]
and
\[
\Phi_{\ell^2}(2)\text{ being a prime power}.
\]

#### Proof

If \(6\nmid a\), Lemma 1 gives
\[
2\ge\tau(a)-1,
\]
so \(\tau(a)\le3\). Hence \(a\) is prime or the square of a prime.

If \(6\mid a\), then
\[
2\ge\tau(a)-2,
\]
so \(\tau(a)\le4\). But an integer divisible by \(6\) has at least four divisors. An integer with exactly four divisors is either a prime cube or a product of two distinct primes. Divisibility by both \(2\) and \(3\) therefore forces \(a=6\). Indeed,
\[
2^6-1=63=3^2\cdot7.
\]

Now suppose \(a=\ell^2\), with \(\ell\) prime. Then
\[
2^{\ell^2}-1=(2^\ell-1)\Phi_{\ell^2}(2).
\]
These two factors are coprime. Indeed, if a prime \(R\) divided both, then \(2^\ell\equiv1\pmod R\), and hence
\[
\Phi_{\ell^2}(2)
=1+2^\ell+\cdots+2^{(\ell-1)\ell}
\equiv \ell\pmod R.
\]
Thus \(R=\ell\). But Fermat's congruence gives
\[
2^\ell-1\equiv1\pmod\ell,
\]
also for \(\ell=2\), so this is impossible.

Both factors exceed \(1\), and their product has at most two distinct prime divisors. Hence each is a prime power.

It remains to show that if \(2^\ell-1\) is a prime power, then it is prime. Write
\[
2^\ell-1=R^c
\]
with \(R\) an odd prime. If \(c\) is even and \(\ell\ge3\), then
\[
2^\ell=R^c+1\equiv2\pmod8,
\]
a contradiction. The case \(\ell=2\) is immediate. If \(c>1\) is odd, then
\[
2^\ell=R^c+1
=(R+1)(R^{c-1}-R^{c-2}+\cdots-R+1),
\]
where the second factor is an odd integer greater than \(1\), again impossible. Thus \(c=1\).

The converse follows from the coprimality of the two factors. ∎

---

### 3. Complete treatment of predecessors that are powers of \(2\)

### Theorem 4

For \(a\ge1\),
\[
2^a+1\in\mathcal B_1
\quad\Longleftrightarrow\quad
1\le a\le7.
\]

#### Proof

The case \(a=1\), giving \(n=3\), is immediate.

Let \(a\ge2\) and suppose \(n=2^a+1\) is a barrier. At offsets \(j=2\) and \(j=3\), respectively,
\[
\omega(2^a-1)\le2
\]
and
\[
\omega(2^a-2)\le3.
\]
Since
\[
2^a-2=2(2^{a-1}-1)
\]
and the second factor is odd,
\[
\omega(2^{a-1}-1)\le2.
\]

By Proposition 3,
\[
a\in S:=\{\text{primes}\}\cup\{\text{prime squares}\}\cup\{6\},
\]
while
\[
a-1\in S\cup\{1\}.
\]

We determine the intersection.

- If \(a\) is prime, then \(a=2\), or \(a\) is odd and \(a-1\) is even. An even member of \(S\cup\{1\}\) which is one less than an odd prime can only be \(2,4,\) or \(6\). This gives
  \[
  a\in\{2,3,5,7\}.
  \]

- If \(a=\ell^2\), then \(\ell=2\) gives \(a=4\). If \(\ell\) is odd, then \(a-1\) is even, and the same alternatives \(2,4,6\) would give \(a=3,5,7\), none a square. Thus only \(a=4\).

- The final possibility is \(a=6\), and then \(a-1=5\) is prime.

Therefore
\[
a\in\{2,3,4,5,6,7\}.
\]

Conversely, for \(2\le a\le7\), one has
\[
2^a+1\le129<210=2\cdot3\cdot5\cdot7.
\]
Thus every positive \(m<2^a+1\) has at most three distinct prime divisors. Consequently all offsets \(j\ge3\) are automatic. It remains to check \(j=1,2\). The \(j=1\) predecessor is \(2^a\), with one distinct prime divisor, while
\[
\begin{array}{c|c}
a&2^a-1\\ \hline
2&3\\
3&7\\
4&3\cdot5\\
5&31\\
6&3^2\cdot7\\
7&127
\end{array}
\]
has at most two distinct prime divisors in every case. Here \(127\) is prime. ∎

---

### 4. Square and composite exponents

### Theorem 5

If \(p\) is prime, then
\[
p^2+1\in\mathcal B_1
\quad\Longleftrightarrow\quad
p\in\{2,3,5,7,17\}.
\]
Thus the square-predecessor barriers are exactly
\[
5,10,26,50,290.
\]

#### Proof

Necessity follows from Proposition 2 for odd \(p\), and Theorem 4 for \(p=2\).

For sufficiency, all five proposed \(n\) are at most \(290<2310\), the product of the first five primes. Thus every \(m<n\) has \(\omega(m)\le4\), so only \(j=1,2,3\) need checking.

The \(j=1\) predecessor \(p^2\) has one distinct prime divisor. The \(j=2\) factorizations were given in Proposition 2. At \(j=3\),
\[
\begin{array}{c|c}
p&p^2-2\\ \hline
2&2\\
3&7\\
5&23\\
7&47\\
17&287=7\cdot41.
\end{array}
\]
All have at most three distinct prime divisors. ∎

### Theorem 6

Suppose \(n>2\) is a barrier and write its canonical prime-power predecessor as
\[
n-1=p^a,
\]
where \(p\) is prime. If \(a\) is composite, then
\[
n\in\{17,65,82\}.
\]
All three numbers are barriers.

#### Proof

If \(p=2\), Theorem 4 gives \(1\le a\le7\). The composite possibilities are \(a=4,6\), giving
\[
n=2^4+1=17,\qquad n=2^6+1=65.
\]

If \(p\) is odd, Proposition 2 shows that the only composite exponent is \(a=4\), and then \(p=3\), giving
\[
n=3^4+1=82.
\]

Conversely, all three numbers are below \(210\), so every predecessor has at most three distinct prime factors and offsets \(j\ge3\) are automatic. At \(j=1,2\), the relevant pairs are
\[
(16,15),\qquad(64,63),\qquad(81,80),
\]
whose \(\omega\)-values are respectively \((1,2),(1,2),(1,2)\). ∎

---

### 5. Reduction for all barriers beyond \(290\)

### Corollary 7

If \(n>290\) is a barrier, then exactly one of the following holds:

1. \(n-1\) is prime;
2. there are odd primes \(p,\ell\) such that
   \[
   n-1=p^\ell,
   \]
   \(p\) is a Fermat prime, and
   \[
   \Phi_\ell(p)=R^v
   \]
   for some odd prime \(R\).

#### Proof

The offset \(j=1\) forces \(n-1\) to be a prime power. If the exponent is composite, Theorem 6 gives \(n\le82\). If the base is \(2\), Theorem 4 gives \(n\le129\). If the exponent is \(2\), Theorem 5 gives \(n\le290\).

Therefore, beyond \(290\), either the exponent is \(1\), so \(n-1\) is prime, or both the base and exponent are odd primes. Proposition 2 gives the Fermat-prime and cyclotomic prime-power conditions. ∎

---

### 6. A second cyclotomic restriction from the shift \(q-p\)

There is one further factorable predecessor.

### Lemma 8

Let \(n=p^a+1\) be a barrier, where \(a\ge2\). Then
\[
\omega(p^{a-1}-1)\le p.
\]

More generally, for \(1\le b<a\),
\[
\omega(p^{a-b}-1)\le p^b.
\]

#### Proof

At offset
\[
j=p^b+1
\]
the predecessor is
\[
n-j=p^a-p^b=p^b(p^{a-b}-1).
\]
The two displayed factors have disjoint prime divisors because
\[
p\nmid p^{a-b}-1.
\]
Hence
\[
\omega(n-j)=1+\omega(p^{a-b}-1).
\]
The barrier inequality gives
\[
1+\omega(p^{a-b}-1)\le p^b+1.
\]
∎

For the surviving family \(p^\ell\) from Corollary 7, take \(b=1\). Since \(\ell\) is an odd prime,
\[
\omega(p^{\ell-1}-1)\le p.
\]

If \(p=3\), then \(3+1\) is a power of \(2\), so Lemma 1 gives
\[
\omega(3^{\ell-1}-1)\ge\tau(\ell-1)-1.
\]
Therefore
\[
\tau(\ell-1)\le4.
\]
Classifying even integers with at most four divisors gives:

### Corollary 9

If \(3^\ell+1\) is a barrier and \(\ell\) is an odd prime, then
\[
\ell=3
\quad\text{or}\quad
\frac{\ell-1}{2}\text{ is prime}.
\]

#### Proof

Put \(b=\ell-1\). An integer with at most four divisors is one of
\[
r,\quad r^2,\quad r^3,\quad rs
\]
for primes \(r,s\), with \(r\ne s\) in the last case.

Since \(b\) is even:

- \(b=r\) gives \(b=2\), hence \(\ell=3\);
- \(b=r^2\) gives \(b=4\), hence \(\ell=5\), for which \((\ell-1)/2=2\);
- \(b=r^3\) gives \(b=8\), hence \(\ell=9\), not prime;
- \(b=rs\) forces \(b=2s\) with \(s\) an odd prime, hence \((\ell-1)/2=s\).

∎

Similarly, for \(p=5\), the \(d=2\) Zsigmondy exception does not occur, and Lemma 1 gives
\[
\omega(5^{\ell-1}-1)\ge\tau(\ell-1).
\]
Thus \(\tau(\ell-1)\le5\), which yields
\[
\ell=3,\qquad \ell=17,\qquad\text{or}\qquad \frac{\ell-1}{2}\text{ is prime}.
\]

These restrictions are necessary, not sufficient.

---

### 7. The higher-power branch is nonempty

The preceding reductions do not eliminate all odd higher powers. For example,
\[
28,\quad126,\quad244,\quad2188
\]
are barriers, with predecessors
\[
27=3^3,\quad125=5^3,\quad243=3^5,\quad2187=3^7.
\]

Indeed:

- \(28<30\), so only \(j=1\) needs nonautomatic checking beyond the equality case \(j=2\):
  \[
  \omega(27)=1,\qquad \omega(26)=2.
  \]

- \(126<210\), so only \(j=1,2\) need checking:
  \[
  \omega(125)=1,\qquad124=2^2\cdot31.
  \]

- \(244<2310\), so only \(j=1,2,3\) need checking:
  \[
  243=3^5,\qquad242=2\cdot11^2,\qquad241\text{ is prime}.
  \]

- \(2188<2310\), and
  \[
  2187=3^7,\qquad
  2186=2\cdot1093,\qquad
  2185=5\cdot19\cdot23,
  \]
  where \(1093\) is prime.

Thus cyclotomic restrictions are a reduction mechanism, not a proof that all large barriers have prime predecessor.

---

### 8. Ledger

#### Proved

1. Primitive-divisor lower bounds in Lemma 1.
2. Complete structural classification for odd \(p\) under
   \(\omega(p^a-1)\le2\).
3. Necessary exponent classification for \(2^a-1\) with at most two distinct prime factors.
4. Exact classification
   \[
   2^a+1\in\mathcal B_1\iff1\le a\le7.
   \]
5. Exact classification of square-predecessor barriers.
6. Exact classification of barriers with composite canonical exponent.
7. Reduction of every barrier \(n>290\) to either a prime predecessor or an odd prime exponent over a Fermat-prime base.
8. Divisor-count restrictions obtained from the factorable shift \(p^\ell-p\).

#### Plausible but unproved

1. Higher-prime-power barriers are probably very sparse, but no finiteness theorem is proved.
2. It is plausible that most sufficiently large barriers, if infinite, have \(n-1\) prime.
3. No infinitude is known here for pairs satisfying
   \[
   p\text{ Fermat prime},\quad \ell\text{ prime},\quad
   \Phi_\ell(p)\text{ a prime power},
   \]
   much less the remaining shifted \(\omega\)-conditions.

#### Dead ends

1. Cyclotomic factorization says nothing useful about general shifts
   \[
   p^\ell-2,\ p^\ell-3,\ldots.
   \]
2. The factorable shifts
   \[
   p^\ell-p^b=p^b(p^{\ell-b}-1)
   \]
   yield only
   \[
   \omega(p^{\ell-b}-1)\le p^b.
   \]
   This is decisive for \(p=2,b=1\), moderately restrictive for \(p=3,5\), and rapidly becomes too weak.
3. The exponent \(a=1\) is completely invisible to cyclotomic exponent classification. This is the central block.

## Self-Audit

1. **Reliance on the exact Bang–Zsigmondy exception list.**  
   A missing exception would invalidate the divisor-count bounds. The form used here is the standard theorem for \(x^d-y^d\): only \(d=2\) with \(x+y\) a power of \(2\), and \((x,y,d)=(2,1,6)\). Every later use explicitly accounts for the applicable exception.

2. **The finite classifications require careful distinction between necessary and sufficient conditions.**  
   In particular, “\(a\) is prime” is only necessary for \(\omega(2^a-1)\le2\), not sufficient. I never use it as sufficient. Sufficiency is asserted only where explicit factorizations are supplied or where the cyclotomic factor is explicitly assumed to be a prime power.

3. **The argument does not approach a proof of infinitude in the prime-predecessor case.**  
   This is a genuine limitation, not a suppressed gap. When \(n-1=q\) is prime, Route 4 has no exponent structure to exploit; already \(\omega(q-1)\le2\) is a difficult shifted-prime condition. The final status is therefore BLOCKED rather than SOLVED or PARTIAL-as-solution.

## Computations To Verify

The following exact Python code enumerates barriers and checks the finite classifications.

```python
from math import isqrt
from sympy import factorint

def omega_sieve(X):
    om = [0] * (X + 1)
    for p in range(2, X + 1):
        if om[p] == 0:                 # p is prime
            for k in range(p, X + 1, p):
                om[k] += 1
    return om

def barrier_list(X):
    om = omega_sieve(X)
    ans = []
    prefix_max = -10**30
    for n in range(1, X + 1):
        if prefix_max <= n:
            ans.append(n)
        prefix_max = max(prefix_max, n + om[n])
    return ans, om

X = 300_000
B, om = barrier_list(X)
Bset = set(B)

# Checksum from the brief
assert B[:12] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 17]

# Theorem 4: powers of 2 in the tested range
base2_exponents = []
for n in B:
    if n <= 2:
        continue
    f = factorint(n - 1)
    if len(f) == 1 and 2 in f:
        base2_exponents.append(f[2])
assert base2_exponents == list(range(1, 8))

# Theorem 5: square predecessors
square_predecessor_barriers = []
for n in B:
    if n <= 2:
        continue
    f = factorint(n - 1)
    if len(f) == 1:
        p, a = next(iter(f.items()))
        if a == 2:
            square_predecessor_barriers.append(n)
assert square_predecessor_barriers == [5, 10, 26, 50, 290]

# Theorem 6: composite canonical exponents
composite_exponent_barriers = []
for n in B:
    if n <= 2:
        continue
    f = factorint(n - 1)
    if len(f) == 1:
        p, a = next(iter(f.items()))
        if a > 1 and not all(a % d for d in range(2, isqrt(a) + 1)):
            composite_exponent_barriers.append(n)
assert composite_exponent_barriers == [17, 65, 82]

# Explicit higher-power examples
assert {28, 126, 244, 2188}.issubset(Bset)
```

The following checks the Zsigmondy-derived inequalities and the odd-base classification over a finite range.

```python
from math import isqrt
from sympy import factorint, primerange, isprime, divisor_count

def omega_factor(n):
    return len(factorint(n))

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def prime_square(n):
    r = isqrt(n)
    return r * r == n and isprime(r)

# Lemma 1 over a moderate exact range
for p in list(primerange(2, 30)):
    for a in range(2, 13):
        actual = omega_factor(p**a - 1)
        if p == 2:
            lower = int(divisor_count(a)) - 1 - int(a % 6 == 0)
        else:
            delta = int(a % 2 == 0 and is_power_of_two(p + 1))
            lower = omega_factor(p - 1) + int(divisor_count(a)) - 1 - delta
        assert actual >= lower, (p, a, actual, lower)

# Proposition 2 over a finite range
for p in primerange(3, 500):
    for a in range(2, 13):
        if omega_factor(p**a - 1) <= 2:
            if a == 2:
                assert p in {3, 5, 7, 17}
            elif a == 4:
                assert p == 3
            else:
                assert isprime(a) and a % 2 == 1
                assert is_power_of_two(p - 1)
                Phi = (p**a - 1) // (p - 1)
                assert omega_factor(Phi) == 1

# Proposition 3 over a finite exponent range
for a in range(2, 50):
    if omega_factor(2**a - 1) <= 2:
        assert isprime(a) or prime_square(a) or a == 6
```

A useful empirical continuation would separate barriers by predecessor type:

```python
def predecessor_type(n):
    if n <= 2:
        return ("small",)
    f = factorint(n - 1)
    if len(f) != 1:
        return ("impossible_for_barrier",)
    p, a = next(iter(f.items()))
    if a == 1:
        return ("prime", p)
    return ("higher_prime_power", p, a)

prime_case = []
higher_power_case = []

for n in B:
    t = predecessor_type(n)
    if t[0] == "prime":
        prime_case.append(n)
    elif t[0] == "higher_prime_power":
        higher_power_case.append((n, t[1], t[2]))

print("largest tested barrier:", B[-1])
print("higher-prime-power barriers:", higher_power_case)
```

These computations can refute a finite classification if an omitted example appears, but cannot prove infinitude.

## Route Diagnosis

Route 4 works very well as an exponent-reduction tool. Zsigmondy theory almost completely destroys complicated exponents, and combining it with the factorable shift \(p^a-p\) completely settles the base-\(2\) branch. It also proves that every sufficiently large nonprime predecessor must be an odd-prime power \(p^\ell\) with both \(p\) and \(\ell\) prime, \(p\) Fermat, and \(\Phi_\ell(p)\) a prime power.

The route is nevertheless blocked for two independent reasons:

1. It gives no information when \(n-1\) itself is prime. This case survives unchanged and is likely the main source of large barriers.
2. In the higher-power branch, even the second offset leads to unresolved questions about prime-power values of \(\Phi_\ell(p)\), while general shifts \(p^\ell-r\) have no cyclotomic factorization.

A fresh attempt should therefore use this classification only as a preprocessing theorem. The main work must come from a method acting on prime predecessors—most plausibly a genuine strengthening of Lau’s construction that can impose \(n-1\) prime or prime-power and patch the remaining terminal offsets. A direct sieve must first overcome the lower-bound/parity obstruction already visible in finding infinitely many primes \(q\) with \(\omega(q-1)\le2\).