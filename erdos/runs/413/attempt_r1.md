STATUS: BLOCKED

## Result

Lau’s constant-\(C\) theorem can be translated exactly into infinitely many bounded visits of a one-dimensional envelope process \(D(x)\), while a genuine barrier is exactly a visit to the minimal state \(D(x)=1\). Patching Lau’s result requires a prescribed \(C-1\)-step descent with no arithmetic “jumps”; its last step forces a prime power, and the preceding step forces that prime power minus one to have at most two distinct prime factors. I prove this reduction rigorously and classify sharply the possible exponents of higher prime powers satisfying the latter condition using Bang–Zsigmondy and Catalan–Mihăilescu. However, the supplied form of Lau’s theorem gives no distributional information that would force even the first two terminal conditions. The remaining patching assertion is in fact exactly equivalent to the original barrier problem, so Route 1 is blocked without a new lower-bound sieve or additional structural information from Lau’s construction.

## Complete Argument

### 1. An exact envelope recurrence

For \(x\ge 0\), define
\[
R(x)=\max_{1\le m\le x}\bigl(m+\omega(m)\bigr),
\]
with \(R(0)=0\), and put
\[
D(x)=R(x)-x.
\]

For \(x\ge1\),
\[
\begin{aligned}
D(x)
&=\max\left(R(x-1),x+\omega(x)\right)-x\\
&=\max\left(D(x-1)-1,\omega(x)\right).
\end{aligned}
\tag{1}
\]

Equivalently,
\[
D(x)=\max_{0\le j\le x-1}\bigl(\omega(x-j)-j\bigr).
\tag{2}
\]

Indeed, write \(m=x-j\) in the definition of \(R(x)-x\).

An integer \(n\) is a barrier precisely when
\[
R(n-1)\le n,
\]
or equivalently
\[
D(n-1)\le1.
\tag{3}
\]

For \(x\ge2\), the term \(m=x\) in \(R(x)\) shows
\[
D(x)\ge\omega(x)\ge1.
\]
Consequently, for \(n\ge3\),
\[
n\text{ is a barrier}\iff D(n-1)=1.
\tag{4}
\]

This gives a compressed version of the prime-power obstruction.

**Lemma 1.** For \(q\ge2\),
\[
q+1\text{ is a barrier}
\iff
\omega(q)=1\ \text{and}\ D(q-1)\le2.
\tag{5}
\]

**Proof.** By (4), \(q+1\) is a barrier exactly when \(D(q)=1\). By (1),
\[
D(q)=\max\bigl(D(q-1)-1,\omega(q)\bigr).
\]
As \(q\ge2\), one has \(\omega(q)\ge1\). Thus the maximum equals \(1\) exactly when
\[
D(q-1)-1\le1
\quad\text{and}\quad
\omega(q)=1.
\]
These are precisely \(D(q-1)\le2\) and \(\omega(q)=1\). By unique factorization, \(\omega(q)=1\) is equivalent to \(q\) being a prime power. ∎

Thus, apart from the barrier \(2\), the original problem is exactly the problem of proving infinitely many prime powers \(q\) for which
\[
D(q-1)\le2.
\tag{6}
\]

In particular, since \(D(q-1)\ge\omega(q-1)\), every such \(q\) must satisfy
\[
\omega(q-1)\le2.
\tag{7}
\]

---

### 2. Exact formulation of the Lau patch

We may assume Lau’s constant \(C\) is a positive integer: if the theorem initially gives a real \(C_0\), replace it by \(\lceil C_0\rceil\), which only weakens the range of controlled \(m\).

Suppose \(n=x+C\). Lau’s inequality
\[
m+\omega(m)\le n\qquad(1\le m\le n-C=x)
\]
is exactly
\[
R(x)\le x+C,
\]
or
\[
D(x)\le C.
\tag{8}
\]

The missing terminal patch has an exact description.

**Lemma 2 (exact patching criterion).** Let \(C\ge1\), \(x\ge1\), and \(n=x+C\). Then \(n\) is a barrier if and only if
\[
D(x)\le C
\tag{9}
\]
and
\[
\omega(x+s)\le C-s
\qquad(1\le s\le C-1).
\tag{10}
\]

**Proof.** Partition the integers \(m<n\) into
\[
1\le m\le x
\]
and
\[
m=x+s,\qquad 1\le s\le C-1.
\]

For the first range, the barrier inequalities are equivalent to
\[
R(x)\le x+C,
\]
which is (9). For \(m=x+s\), the barrier inequality is
\[
x+s+\omega(x+s)\le x+C,
\]
equivalent to
\[
\omega(x+s)\le C-s.
\]
This proves both directions. ∎

The recurrence (1) shows what this patch means dynamically. If (9) and (10) hold, then induction gives
\[
D(x+s)\le C-s
\qquad(0\le s\le C-1).
\tag{11}
\]
Indeed, if \(D(x+s-1)\le C-s+1\), then
\[
D(x+s)
=\max\bigl(D(x+s-1)-1,\omega(x+s)\bigr)
\le C-s.
\]
At the final step,
\[
D(x+C-1)\le1,
\]
which is exactly the barrier condition for \(x+C\).

Consequently, if
\[
G_C=\{x\ge1:D(x)\le C\},
\]
then Lau’s stated theorem gives
\[
G_C\ \text{is infinite},
\tag{12}
\]
whereas the desired result is
\[
\left\{
x\in G_C:
\omega(x+s)\le C-s\text{ for }1\le s<C
\right\}
\ \text{is infinite}.
\tag{13}
\]

By Lemma 2, assertion (13) is itself equivalent, up to a fixed translation and finitely many small cases, to the original barrier conjecture. Thus it cannot simply be treated as a routine finite deletion from (12).

The failure of such an inference is visible even numerically. For example,
\[
R(14)=16,
\qquad D(14)=2,
\]
so \(14\in G_2\). Nevertheless,
\[
\omega(15)=2>1,
\]
and \(16=14+2\) is not a barrier. Its explicit witness is \(m=15\):
\[
15+\omega(15)=15+2=17>16.
\]

More abstractly, the recurrence alone cannot bridge the gap. If an artificial arithmetic function \(g\) were defined by \(g(1)=0\) and \(g(m)=2\) for \(m\ge2\), its corresponding envelope would satisfy \(D_g(x)=2\) for every \(x\ge2\). It would therefore have infinitely many bounded visits \(D_g(x)\le2\), but no later visits to \(D_g(x)=1\). Special arithmetic information about \(\omega\), not the recurrence itself, is indispensable.

---

### 3. The first two terminal conditions

Set
\[
q=x+C-1=n-1.
\]
The last inequality in (10) is
\[
\omega(q)\le1.
\]
For all sufficiently large candidates \(q\ge2\), this says exactly that \(q\) is a prime power.

The preceding condition is
\[
\omega(q-1)\le2.
\]
If \(C=2\), it is already contained in \(D(x)\le2\), since then \(x=q-1\) and \(D(x)\ge\omega(x)\). Thus every successful patch, for every relevant \(C\ge2\), must at least produce infinitely many prime powers \(q\) satisfying
\[
\omega(q-1)\le2.
\tag{14}
\]

This is not a congruence condition. For instance, finite congruence restrictions alone cannot force an integer in a reduced residue class to be a prime power: if \((a,M)=1\), choose a prime \(r\equiv1\pmod M\), and by Dirichlet’s theorem choose infinitely many distinct primes \(s\equiv a\pmod M\). Then
\[
rs\equiv a\pmod M
\]
and \(rs\) has two distinct prime divisors. A genuine lower-bound sieve or a special algebraic parametrization is therefore required.

---

### 4. Restrictions on higher prime-power candidates

The following analysis executes the brief’s proposed quick blocking test for the prime-power condition.

I use the standard Bang–Zsigmondy theorem in this form:

> If \(A>1\) and \(d>1\), then \(A^d-1\) has a prime divisor that divides no \(A^e-1\) with \(1\le e<d\), except when  
> 1. \(d=2\) and \(A+1\) is a power of \(2\), or  
> 2. \((A,d)=(2,6)\).

Such a prime is called primitive. A primitive divisor attached to \(d\) has multiplicative order \(d\) modulo that prime, so primitive divisors attached to distinct exponents are distinct.

#### Proposition 3

Let \(q=p^a\), where \(p\) is prime and \(a\ge1\), and suppose
\[
\omega(p^a-1)\le2.
\tag{15}
\]

1. If \(p\) is odd, exactly the following possibilities remain:
   - \(a=1\), with \(\omega(p-1)\le2\);
   - \(a=2\) and
     \[
     p\in\{3,5,7,17\};
     \]
   - \(a=4\) and \(p=3\);
   - \(a=\ell\) is an odd prime,
     \[
     p-1=2^u,
     \]
     and
     \[
     \Phi_\ell(p)=r^v
     \]
     for some odd prime \(r\) and \(v\ge1\).

2. If \(p=2\), then necessarily
   \[
   a=1,\qquad
   a=\ell,\qquad
   a=\ell^2
   \quad(\ell\text{ prime}),
   \qquad\text{or}\qquad
   a=6.
   \tag{16}
   \]

These restrictions are necessary; the exponent alternatives in the \(p=2\) case are not asserted to be sufficient.

**Proof.**

##### Odd \(p\)

The prime \(2\) divides \(p-1\), hence divides \(p^a-1\).

For every divisor \(d\mid a\) with \(d>2\), Bang–Zsigmondy supplies a primitive prime divisor \(r_d\) of \(p^d-1\). It divides \(p^a-1\), is different from \(2\), and the primes \(r_d\) are distinct for distinct \(d\).

Therefore, if \(a\) has two distinct divisors greater than \(2\), then \(p^a-1\) has at least the three distinct prime divisors
\[
2,\quad r_{d_1},\quad r_{d_2},
\]
contrary to (15).

Hence \(a\) has at most one divisor greater than \(2\). The possibilities are
\[
a=1,\quad a=2,\quad a=4,\quad\text{or}\quad a=\ell
\]
with \(\ell\) an odd prime. Indeed, an odd composite \(a\) has a proper divisor \(d>2\) in addition to \(a\), while an even \(a>4\) has the two distinct divisors \(a/2>2\) and \(a>2\).

For \(a=2\), suppose first that \(p>3\). Since \(p\not\equiv0\pmod3\), one has \(3\mid p^2-1\). Thus (15) forces all prime divisors of \(p^2-1\) to lie in \(\{2,3\}\).

Put
\[
u=\frac{p-1}{2},
\qquad
v=\frac{p+1}{2}.
\]
Then \(u,v>1\), \((u,v)=1\), and \(v-u=1\). Their prime divisors lie in \(\{2,3\}\). Since they are coprime and both exceed \(1\), one is a power of \(2\) and the other a power of \(3\). Hence
\[
|2^\alpha-3^\beta|=1.
\]

The Catalan–Mihăilescu theorem shows that the only solution with \(\alpha,\beta>1\) is
\[
3^2-2^3=1.
\]
Checking cases where one exponent is \(0\) or \(1\) gives the consecutive pairs
\[
(1,2),\quad(2,3),\quad(3,4),\quad(8,9).
\]
They correspond respectively to
\[
p=3,5,7,17.
\]
All four satisfy \(\omega(p^2-1)\le2\).

Now let \(a=4\). Bang–Zsigmondy supplies a primitive divisor \(r_4\) of \(p^4-1\). If \(p+1\) is not a power of \(2\), it also supplies a primitive divisor \(r_2\) of \(p^2-1\). Then \(2,r_2,r_4\) are distinct, contradicting (15). Therefore \(p+1\) is a power of \(2\).

Furthermore, if \(p-1\) had an odd prime divisor \(s\), then \(2,s,r_4\) would be three distinct prime divisors of \(p^4-1\). Hence \(p-1\) is also a power of \(2\). The only two powers of \(2\) differing by \(2\) are \(2\) and \(4\), so \(p=3\). Conversely,
\[
3^4-1=80=2^4\cdot5
\]
has two distinct prime divisors.

Finally, let \(a=\ell\) be an odd prime. A primitive divisor \(r\) belonging to exponent \(\ell\) is distinct from every divisor of \(p-1\). Since \(2\mid p-1\), condition (15) forces
\[
p-1=2^u.
\]
Also
\[
p^\ell-1=(p-1)\Phi_\ell(p),
\]
and \(\Phi_\ell(p)\) is odd. All its prime divisors must therefore equal the single odd prime \(r\), so
\[
\Phi_\ell(p)=r^v.
\]
Conversely, these displayed conditions make \(p^\ell-1=2^u r^v\), which has exactly two distinct prime divisors. This proves the odd-\(p\) classification.

##### The case \(p=2\)

For each divisor \(d>1\) of \(a\), Bang–Zsigmondy gives a distinct primitive prime divisor of \(2^d-1\), except possibly for \(d=6\).

If \(6\nmid a\), all divisors \(d>1\) of \(a\) are nonexceptional. Thus
\[
\tau(a)-1\le\omega(2^a-1)\le2,
\]
so \(\tau(a)\le3\). Hence \(a=1\), \(a\) is prime, or \(a\) is the square of a prime.

If \(6\mid a\), only \(d=6\) can be exceptional, so
\[
\tau(a)-2\le2.
\]
Thus \(\tau(a)\le4\). An integer divisible by \(6\) has at least four divisors, and equality occurs only for \(a=6\). Therefore \(a=6\).

This proves (16). ∎

This classification eliminates most composite exponents, but it does not construct infinitely many candidates. In particular:

- the unrestricted exponent \(a=1\) is exactly the difficult prime case;
- for odd \(p\) and odd prime exponent, \(p\) must be a Fermat-type prime and a cyclotomic value must be a prime power;
- for \(p=2\), one is left with Mersenne and related cyclotomic factorization questions.

Thus switching to a purely cyclotomic route does not bypass the main analytic obstruction.

---

### 5. Precise point of blockage

From Lau’s theorem as stated, one obtains only
\[
D(x)\le C
\]
for infinitely many \(x\).

To complete Route 1 one must prove that infinitely many of those \(x\) also satisfy
\[
\omega(x+1)\le C-1,\quad
\omega(x+2)\le C-2,\quad\ldots,\quad
\omega(x+C-1)\le1.
\tag{17}
\]

The final two constraints require
\[
q=x+C-1\ \text{to be a prime power}
\]
and
\[
\omega(q-1)\le2.
\]
No distribution of Lau’s candidate set in shifted prime or prime-power sequences is supplied. Infinitude of the set \(G_C\) gives no lower bound for its intersection with these sparse terminal conditions.

Moreover, by Lemma 2, proving that this intersection is infinite is not a weaker cleanup statement: it is exactly the original barrier conjecture expressed relative to \(G_C\). Therefore Route 1, using only the stated Lau theorem, has reduced the problem to an unproved assertion of equal strength and is BLOCKED.

## Self-Audit

1. **The exponent classification invokes Bang–Zsigmondy and Catalan–Mihăilescu rather than reproving them.** These are established theorems, and I stated the precise forms used. The divisor counts and all exceptional cases were checked explicitly.

2. **I did not have the detailed parameterization or quantitative estimates from Lau’s paper.** A stronger unpublished feature—such as a lower-bound sieve retaining distribution after terminal restrictions—could reopen Route 1. Nevertheless, the exact consequence of the theorem as stated in the brief is only \(D(x)\le C\) infinitely often, and Lemma 2 rigorously shows why that alone is insufficient.

3. **I have not proved that the weaker problem “infinitely many prime powers \(q\) with \(\omega(q-1)\le2\)” is open.** I use it only as a necessary blocking test, not as a formal impossibility theorem. The actual rigorous block is sharper: the required intersection (13) is exactly equivalent to the original conjecture, and no theorem in the supplied material establishes it.

## Computations To Verify

The following Python performs exact barrier enumeration, verifies the envelope recurrence and patching criterion, measures successive terminal losses, and checks the exponent restrictions in Proposition 3 over a finite range.

```python
from math import isqrt

def omega_sieve(N):
    w = [0] * (N + 1)
    for p in range(2, N + 1):
        if w[p] == 0:                 # p is prime
            for k in range(p, N + 1, p):
                w[k] += 1
    return w

def prime_sieve(N):
    isp = bytearray(b"\x01") * (N + 1)
    if N >= 0:
        isp[0] = 0
    if N >= 1:
        isp[1] = 0
    for p in range(2, isqrt(N) + 1):
        if isp[p]:
            isp[p*p:N+1:p] = b"\x00" * (((N - p*p) // p) + 1)
    return isp

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def compute_data(N):
    w = omega_sieve(N)

    # R[x] and D[x]
    R = [0] * (N + 1)
    D = [0] * (N + 1)
    running = 0
    for x in range(1, N + 1):
        running = max(running, x + w[x])
        R[x] = running
        D[x] = running - x

        # Verify D(x) = max(D(x-1)-1, omega(x))
        assert D[x] == max(D[x-1] - 1, w[x])

    # Barrier enumeration; test before inserting n + omega(n)
    barriers = []
    prefix_max = 0
    for n in range(1, N + 1):
        if prefix_max <= n:
            barriers.append(n)
        prefix_max = max(prefix_max, n + w[n])

    return w, R, D, barriers

N = 1_000_000
w, R, D, barriers = compute_data(N)
B = set(barriers)

assert barriers[:12] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 17]

# Lemma 1:
# q+1 is a barrier iff q is a prime power and D(q-1) <= 2.
for q in range(2, N):
    rhs = (w[q] == 1 and D[q-1] <= 2)
    assert ((q + 1) in B) == rhs

# Concrete failure of "D(x) <= C implies patch".
assert D[14] == 2
assert w[15] == 2
assert 16 not in B

# Verify Lemma 2 for several C and measure successive terminal attrition.
for C in range(2, 16):
    pool = [x for x in range(1, N - C + 1) if D[x] <= C]
    print("C =", C, "near candidates =", len(pool))

    for s in range(1, C):
        pool = [x for x in pool if w[x+s] <= C-s]
        print("   after s =", s, "survivors =", len(pool))

    # Exact patch equivalence
    for x in range(1, N - C + 1):
        patched = (
            D[x] <= C and
            all(w[x+s] <= C-s for s in range(1, C))
        )
        assert patched == ((x + C) in B)

# Verify the exponent restrictions in Proposition 3.
Q = 2_000_000
wq = omega_sieve(Q)
isp = prime_sieve(Q)

def is_prime_square(a):
    r = isqrt(a)
    return r * r == a and bool(isp[r])

examples = []

for p in range(2, Q + 1):
    if not isp[p]:
        continue

    a = 1
    q = p
    while q <= Q:
        if wq[q - 1] <= 2:
            examples.append((p, a, q, wq[q - 1]))

            if p == 2:
                valid = (
                    a == 1 or
                    bool(isp[a]) or
                    is_prime_square(a) or
                    a == 6
                )
                assert valid, ("p=2 exponent violation", p, a, q)

            else:
                if a == 1:
                    valid = True
                elif a == 2:
                    valid = p in {3, 5, 7, 17}
                elif a == 4:
                    valid = (p == 3)
                elif a % 2 == 1 and isp[a]:
                    cyclotomic = (q - 1) // (p - 1)
                    valid = (
                        is_power_of_two(p - 1) and
                        wq[cyclotomic] == 1
                    )
                else:
                    valid = False

                assert valid, ("odd-p exponent violation", p, a, q)

        if q > Q // p:
            break
        q *= p
        a += 1

print("Prime powers q <= Q with omega(q-1) <= 2:", len(examples))
print("First examples:", examples[:50])
```

The most informative computation for Route 1, once Lau’s actual candidates can be generated, is:

```python
# lau_candidates should yield n satisfying all offsets j >= C.
for n in lau_candidates:
    terminal = [w[n-j] for j in range(1, C)]
    ok = all(terminal[j-1] <= j for j in range(1, C))
    print(n, terminal, ok)
```

One should record sequential survivor counts after imposing \(j=1\), then \(j=2\), and so on, rather than only the final count.

## Route Diagnosis

**Proved ledger**

- The exact recurrence
  \[
  D(x)=\max(D(x-1)-1,\omega(x)).
  \]
- For \(q\ge2\),
  \[
  q+1\text{ is a barrier}
  \iff q\text{ is a prime power and }D(q-1)\le2.
  \]
- Lau’s stated theorem is exactly the assertion that \(D(x)\le C\) infinitely often.
- The terminal patch is exactly the prescribed descent
  \[
  D(x+s)\le C-s,\qquad 0\le s<C.
  \]
- Every patch must produce a prime power \(q\) with \(\omega(q-1)\le2\).
- Bang–Zsigmondy sharply restricts the possible exponents of higher prime powers satisfying this second condition.

**Plausible but unproved**

- Lau’s parameter set may possess enough quantitative distribution to survive restriction to \(x+C-1\) prime and then to the remaining low-\(\omega\) shifts.
- A Chen-type switching argument with a variable power of \(2\) might help with
  \[
  q\text{ prime},\qquad \omega(q-1)\le2,
  \]
  but ordinary “\(P_2\)” output for \((q-1)/2\) is insufficient: two distinct odd factors would give \(\omega(q-1)=3\).
- The prime branch \(q=p\) likely dominates, but no rigorous argument here establishes that it contains infinitely many successful patches.

**Dead ends**

- Bounded recurrence states do not force state \(1\); arithmetic distribution is essential.
- A finite congruence patch cannot force the last shifted value to be a prime power.
- Cyclotomic methods eliminate many higher exponents but leave the prime case \(a=1\) untouched.
- Merely asserting that finitely many offsets remain is misleading: the last two are lower-bound sieve conditions, not finite verification conditions.

**Best next move**

Obtain the full quantitative form and parameterization of Lau’s construction. The first decisive test is whether one can prove a nonzero lower bound, within that family, for
\[
x+C-1\ \text{prime}
\quad\text{and}\quad
\omega(x+C-2)\le2.
\]
If Lau’s sieve weights or parameter sequence cannot survive this restriction, direct Route 1 is genuinely exhausted. A fresh attempt should then target the envelope formulation
\[
\text{infinitely many prime powers }q\text{ with }D(q-1)\le2,
\]
using a joint shifted almost-prime sieve or a nested-gap/second-moment method conditioned on \(q\) being prime.