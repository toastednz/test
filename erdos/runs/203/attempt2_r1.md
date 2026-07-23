STATUS: PARTIAL

## Result

No complete \(m\) or finite covering certificate was obtained. I proved several exact reductions and obstructions specific to Route 1. Most importantly: (i) the exponent \(M\) may be normalized to either a squarefree odd integer or four times one; (ii) the total density covered by all odd-power and Sophie Germain identities is always \(<1/4\), regardless of how many odd prime divisors \(M\) has; hence the listed \(31\)-prime \(2\)-\(3\)-smooth-index pool, whose exact mass is \(559335/746496<3/4\), cannot work with this algebraic core for any \(M\); (iii) I determined exactly which prime targets are compatible with \(m=x^M\); and (iv) when \(q\mid M\), compatible prime cosets with full \(q\)-primary character necessarily have central line shadows modulo \(q\), yielding sharp per-direction conditional-mass inequalities. These results substantially narrow a future exact search, but the decisive target-compatible mixed-prime cover remains unfound.

## Complete Argument

### 1. The exact hybrid construction criterion

Fix \(M\ge1\), and put
\[
m=x^M,\qquad x>1,\qquad \gcd(x,6)=1.
\]

Let \(Q(M)\) denote the set of odd prime divisors of \(M\). Define
\[
E_q=\{(k,\ell)\in\mathbb Z^2:q\mid k,\ q\mid \ell\}
\qquad(q\in Q(M)).
\]
If \(4\mid M\), also define
\[
S=\{(k,\ell): k\equiv2\pmod4,\ \ell\equiv0\pmod4\}.
\]
Let
\[
\mathcal A_M=\bigcup_{q\in Q(M)}E_q
\]
when \(4\nmid M\), and
\[
\mathcal A_M=S\cup\bigcup_{q\in Q(M)}E_q
\]
when \(4\mid M\).

#### Lemma 1: Every exponent pair in \(\mathcal A_M\) gives a composite term.

If \((k,\ell)\in E_q\), write
\[
Y=2^{k/q}3^{\ell/q}x^{M/q}.
\]
For \(k,\ell\ge0\), this is an integer and \(Y>1\). Therefore
\[
2^k3^\ell x^M+1=Y^q+1
=(Y+1)(Y^{q-1}-Y^{q-2}+\cdots-Y+1).
\]
Both factors exceed \(1\): the first because \(Y>1\), and the second because
\[
Y^q+1>Y+1.
\]

If \((k,\ell)\in S\), put
\[
b=2^{(k-2)/4}3^{\ell/4}x^{M/4}.
\]
Then \(b\ge x>1\), and
\[
2^k3^\ell x^M+1=4b^4+1
=(2b^2-2b+1)(2b^2+2b+1).
\]
For \(b\ge2\), both factors are greater than \(1\). Thus the number is composite. ∎

For a prime \(p\ge5\), let
\[
H_p=\langle2,3\rangle\le\mathbb F_p^\times.
\]
A target \(t\in H_p\) can be used with \(m=x^M\) precisely when
\[
-t^{-1}\in(\mathbb F_p^\times)^M.
\]
If this holds, choose a root \(r_p\) satisfying
\[
r_p^M\equiv-t^{-1}\pmod p.
\]

#### Lemma 2: Hybrid covering sufficiency.

Suppose distinct primes \(p_1,\dots,p_s\ge5\) and compatible targets \(t_i\in H_{p_i}\) satisfy
\[
\mathbb Z^2=
\mathcal A_M\cup
\bigcup_{i=1}^s
\{(k,\ell):2^k3^\ell\equiv t_i\pmod{p_i}\}.
\]
Then there is an \(x\), and hence \(m=x^M\), solving the original problem.

**Proof.**
Choose compatible roots \(r_i\) with
\[
r_i^M\equiv-t_i^{-1}\pmod{p_i}.
\]
By CRT, choose \(x\) such that
\[
x\equiv r_i\pmod{p_i}\quad(1\le i\le s),
\qquad x\equiv1\pmod6.
\]
Add a sufficiently large multiple of \(6\prod_i p_i\) so that
\[
x>1,\qquad x^M>\max_i p_i.
\]
Then \(\gcd(x^M,6)=1\).

For any \(k,\ell\ge0\), if \((k,\ell)\in\mathcal A_M\), Lemma 1 applies. Otherwise some \(i\) has
\[
2^k3^\ell\equiv t_i\pmod{p_i},
\]
and hence
\[
2^k3^\ell x^M
\equiv t_i(-t_i^{-1})
\equiv-1\pmod{p_i}.
\]
Thus \(p_i\mid 2^k3^\ell x^M+1\). Since
\[
2^k3^\ell x^M+1>x^M>p_i,
\]
this is a proper divisor. ∎

Thus the remaining problem in Route 1 is an exact finite cover using only compatible targets.

---

### 2. Exact density of the algebraic core

All sets in \(\mathcal A_M\) are periodic. For distinct odd primes \(q\), the conditions defining \(E_q\) are independent by CRT, and the Sophie Germain condition modulo \(4\) is independent of all odd moduli.

Consequently,
\[
\delta(\mathcal A_M)=
1-\prod_{q\mid M,\ q\text{ odd}}\left(1-\frac1{q^2}\right)
\]
if \(4\nmid M\), and
\[
\delta(\mathcal A_M)=
1-\frac{15}{16}
\prod_{q\mid M,\ q\text{ odd}}\left(1-\frac1{q^2}\right)
\]
if \(4\mid M\).

In particular:
\[
\delta(\mathcal A_3)=\frac19,\qquad
\delta(\mathcal A_{15})=\frac{11}{75},
\]
and
\[
\delta(\mathcal A_{12})=\frac16,\qquad
\delta(\mathcal A_{20})=\frac1{10},\qquad
\delta(\mathcal A_{60})=\frac15.
\]

Since
\[
\prod_{\substack{q\ \mathrm{prime}\\q\text{ odd}}}
\left(1-\frac1{q^2}\right)=\frac8{\pi^2},
\]
every finite choice of odd prime factors satisfies
\[
\prod_{q\mid M,\ q\text{ odd}}
\left(1-\frac1{q^2}\right)>\frac8{\pi^2}.
\]
Therefore
\[
\delta(\mathcal A_M)<1-\frac8{\pi^2}
\]
when \(4\nmid M\), and
\[
\delta(\mathcal A_M)<1-\frac{15}{2\pi^2}
\]
when \(4\mid M\).

In particular,
\[
\delta(\mathcal A_M)<\frac14
\]
for every \(M\). Indeed, \(\pi^2<10\) gives
\[
\frac{15}{2\pi^2}>\frac34.
\]

Thus these algebraic identities alone can never cover even one quarter of the exponent plane. Any prime pool in a Route 1 certificate must have nominal mass at least
\[
\sum_p\frac1{h_p}>
\begin{cases}
\dfrac8{\pi^2},&4\nmid M,\\[2mm]
\dfrac{15}{2\pi^2},&4\mid M.
\end{cases}
\]
For \(M=60\), the sharper fixed-\(M\) bound is
\[
\sum_p\frac1{h_p}\ge\frac45.
\]

---

### 3. Normalization of the exponent \(M\)

Let
\[
R=\prod_{\substack{q\mid M\\q\text{ odd prime}}}q,
\]
and define
\[
M^\flat=
\begin{cases}
R,&4\nmid M,\\
4R,&4\mid M.
\end{cases}
\]

#### Lemma 3: It suffices to search \(M=R\) or \(M=4R\), with \(R\) odd and squarefree.

More precisely, any Route 1 certificate for \(M\) yields one with exactly the same prime cosets and algebraic mask for \(M^\flat\).

**Proof.**
We have \(M^\flat\mid M\). The sets \(E_q\) depend only on whether \(q\mid M\), and the Sophie Germain set depends only on whether \(4\mid M\). Hence
\[
\mathcal A_{M^\flat}=\mathcal A_M.
\]

If \(t\) is compatible with \(M\), then
\[
-t^{-1}=y^M
=\left(y^{M/M^\flat}\right)^{M^\flat}.
\]
Thus every \(M\)-compatible target is also \(M^\flat\)-compatible. Lemma 2 can then be applied with fresh CRT roots for exponent \(M^\flat\). ∎

Consequently:

- odd prime powers in \(M\) do not add algebraic classes and can only remove targets;
- a factor \(2\) without a factor \(4\) adds no Sophie Germain class and can only remove targets;
- factors \(2^a\) with \(a>2\) add nothing beyond the \(4\)-factor and can only remove targets.

This is a rigorous search-space reduction.

---

### 4. Exact characterization of compatible targets

Fix \(p\ge5\), and write
\[
G=\mathbb F_p^\times,\qquad n=p-1,\qquad H=H_p,\qquad |H|=h.
\]
Let
\[
P=G^M=\{z^M:z\in G\}.
\]
Set
\[
d=\gcd(M,n).
\]
Since \(G\) is cyclic,
\[
|P|=\frac nd.
\]

Define the allowable target set
\[
T_M(p)=\{t\in H:-t^{-1}\in P\}.
\]

#### Lemma 4: Target count and nonemptiness.

One has
\[
T_M(p)=H\cap(-P).
\]
Choose a generator \(g\) of \(G\). Then
\[
H=\langle g^{n/h}\rangle,\qquad P=\langle g^d\rangle.
\]
Put
\[
e=\gcd(n/h,d).
\]
Then
\[
T_M(p)\ne\varnothing
\iff e\mid\frac n2.
\]
When nonempty,
\[
|T_M(p)|=\gcd\left(h,\frac nd\right).
\]

**Proof.**
Because \(P\) is closed under inversion,
\[
-t^{-1}\in P\iff t\in-P.
\]
Thus \(T_M(p)=H\cap(-P)\).

The intersection \(H\cap(-P)\) is nonempty exactly when \(-1\in HP\). Now
\[
HP=\langle g^{\gcd(n/h,d)}\rangle=\langle g^e\rangle.
\]
Since \(-1=g^{n/2}\), this gives the nonemptiness condition
\[
e\mid n/2.
\]

If nonempty, \(H\cap(-P)\) is a coset of \(H\cap P\), so its cardinality is
\[
|H\cap P|=\gcd(|H|,|P|)
=\gcd\left(h,\frac nd\right).
\]
∎

If \(M\) is odd, then \((-1)^M=-1\), so \(-1\in P\). Therefore every prime has at least one compatible target for odd \(M\). This does not mean every target is compatible.

For the two principal trial exponents, the first target counts are:

\[
\begin{array}{c|c|c|c}
p&h_p&|T_{15}(p)|&|T_{60}(p)|\\ \hline
5&4&4&1\\
7&6&2&1\\
11&10&2&1\\
13&12&4&1\\
17&16&16&4\\
19&18&6&3\\
23&11&11&0\\
47&23&23&0\\
71&35&7&0\\
167&83&83&0\\
431&43&43&0
\end{array}
\]

Thus \(M=60\) forces the targets for \(p=5,7,11,13\) and completely excludes several important exact-line primes.

A useful general exclusion is the following.

#### Corollary 5: Even powers exclude odd-order subgroups at primes \(p\equiv3\pmod4\).

If \(M\) is even, \(p\equiv3\pmod4\), and \(h_p\) is odd, then
\[
T_M(p)=\varnothing.
\]

**Proof.**
Every \(M\)-th power is a square. Since \(p\equiv3\pmod4\), \(-1\) is a nonsquare, so the negative of an \(M\)-th power is a nonsquare. On the other hand, the odd-order subgroup \(H_p\) lies in the subgroup of squares. Hence \(H_p\cap(-P)=\varnothing\). ∎

This removes \(p=23,47,71,167,191,431\), among others, from every Sophie Germain search \(M=4R\).

---

### 5. Rigidity of the \(q\)-shadows forced by the power condition

Let \(q\) be an odd prime with \(q\mid M\). Suppose \(q\mid h_p\), and write
\[
\alpha=v_q(p-1),\qquad \beta=v_q(h_p).
\]

Choose a generator \(u\) of \(H_p\), and write
\[
2=u^a,\qquad 3=u^b,\qquad t=u^c.
\]
The corresponding prime coset is
\[
ak+b\ell\equiv c\pmod{h_p}.
\]

#### Lemma 6: Full \(q\)-primary characters have central shadows.

If
\[
v_q(h_p)=v_q(p-1),
\]
then every \(M\)-compatible target satisfies
\[
c\equiv0\pmod q.
\]
Thus the reduction of the prime coset modulo \(q\) is the central line
\[
ak+b\ell\equiv0\pmod q.
\]

**Proof.**
Since \(q\mid M\),
\[
G^M\subseteq G^q.
\]
Also \(-1=(-1)^q\in G^q\), so
\[
-G^M\subseteq G^q.
\]
Therefore every compatible \(t\) belongs to
\[
H_p\cap G^q.
\]

If \(H_p\) has the full \(q\)-primary order of \(G\), cyclic-group arithmetic gives
\[
H_p\cap G^q=H_p^q.
\]
Thus \(t\in H_p^q\). Relative to the generator \(u\), this means \(t=u^c\) with \(q\mid c\). ∎

Hence the \(q\)-th power identity does not merely add the algebraic point \((0,0)\pmod q\): it also tends to force the compatible \(q\)-divisible prime cosets to pass through that same point. This is a significant loss of affine flexibility.

---

### 6. Conditional-density inequalities modulo \(q\)

Let \(C_p\) be a selected prime coset of index \(h_p\). Fix an odd prime \(q\), and let
\[
R_v=\{(k,\ell)\in\mathbb Z^2:(k,\ell)\equiv v\pmod q\}
\]
for \(v\in\mathbb F_q^2\).

If \(q\nmid h_p\), then \(C_p\) has conditional density
\[
\frac1{h_p}
\]
inside every \(R_v\).

If \(q\mid h_p\), its shadow modulo \(q\) is an affine line \(L_p\). It is empty in \(R_v\) when \(v\notin L_p\), while for \(v\in L_p\) it has conditional density
\[
\frac q{h_p}.
\]

These assertions follow from the joint homomorphism
\[
(k,\ell)\longmapsto
\bigl(k\bmod q,\ell\bmod q,ak+b\ell\bmod h_p\bigr).
\]
When \(q\mid h_p\), the image has the single compatibility condition
\[
ak+b\ell\equiv c\pmod q,
\]
so the prime coset is distributed equally among the \(q\) residue cells on its shadow line.

Now assume \(q\mid M\). The mask \(E_q\) covers \(R_0\) completely and covers no other \(R_v\). Let \(D_q\) be the conditional density in any \(R_v\) of all the other algebraic masks. CRT gives
\[
D_q=
1-\eta\prod_{\substack{r\mid M,\ r\text{ odd prime}\\r\ne q}}
\left(1-\frac1{r^2}\right),
\]
where
\[
\eta=
\begin{cases}
1,&4\nmid M,\\
15/16,&4\mid M.
\end{cases}
\]

For example,
\[
D_3(M=15)=\frac1{25},\qquad D_5(M=15)=\frac19,
\]
and
\[
D_3(M=60)=\frac1{10},\qquad D_5(M=60)=\frac16.
\]

Let
\[
W_0(q)=\sum_{\substack{p\text{ selected}\\q\nmid h_p}}\frac1{h_p}.
\]

#### Lemma 7: Exact shadow-capacity necessity.

For every nonzero \(v\in\mathbb F_q^2\), a hybrid cover must satisfy
\[
1\le
D_q+W_0(q)+
q\sum_{\substack{p\text{ selected}\\q\mid h_p\\v\in L_p}}
\frac1{h_p}.
\]

**Proof.**
Inside \(R_v\), \(v\ne0\), the set \(E_q\) is absent. The other algebraic masks have union density \(D_q\). Prime cosets with \(q\nmid h_p\) contribute conditional density at most \(1/h_p\), while those with \(q\mid h_p\) contribute either \(0\) or \(q/h_p\), according as \(v\notin L_p\) or \(v\in L_p\). The union bound within \(R_v\) gives the displayed inequality. ∎

Suppose additionally that every selected prime with \(q\mid h_p\) has
\[
v_q(h_p)=v_q(p-1).
\]
By Lemma 6, all its shadows are central lines. For a projective direction \(L\subset\mathbb F_q^2\), set
\[
W_L=\sum_{\substack{p:q\mid h_p\\L_p=L}}\frac1{h_p}.
\]
Every nonzero vector lies on exactly one of the \(q+1\) central projective lines. Therefore
\[
D_q+W_0(q)+qW_L\ge1
\]
for every one of the \(q+1\) directions. Summing gives the necessary inequality
\[
\boxed{\;
\sum_{\substack{p:q\mid h_p}}\frac1{h_p}
\ge
\frac{q+1}{q}\bigl(1-D_q-W_0(q)\bigr)
\;}
\]
whenever the right side is positive.

This is substantially stronger than a total-mass test because the \(q\)-divisible mass must be distributed among all \(q+1\) central directions.

More generally, if some \(q\)-divisible shadows are noncentral, write \(W_{\rm cen}\) and \(W_{\rm non}\) for their total masses. Summing Lemma 7 over all \(q^2-1\) nonzero cells gives
\[
(q^2-1)(1-D_q-W_0(q))
\le q(q-1)W_{\rm cen}+q^2W_{\rm non}.
\]
A central line meets \(q-1\) nonzero cells, while a noncentral affine line meets \(q\) of them.

---

### 7. The bounded smooth-index pool is impossible for every \(M\)

The \(31\) indices listed in the brief are
\[
\begin{gathered}
4,6,12,16,18,36,36,48,96,108,144,162,216,256,384,486,576,\\
648,648,648,1458,1728,2916,4608,5184,5184,5832,23328,31104,
46656,746496.
\end{gathered}
\]

Their exact reciprocal mass is
\[
S=
\frac14+\frac16+\frac1{12}+\cdots+\frac1{746496}.
\]
All denominators divide
\[
746496=2^{10}3^6.
\]
Direct exact summation gives
\[
S=\frac{559335}{746496}.
\]
Since
\[
\frac34=\frac{559872}{746496},
\]
we have
\[
S=\frac34-\frac{537}{746496}<\frac34.
\]

By Section 2, the full algebraic mask produced by all Route 1 identities has density \(<1/4\) for every \(M\). Thus
\[
\delta(\mathcal A_M)+S<1.
\]

Therefore:

> **Proposition 8.** No choice of \(M\), no choice of compatible targets, and no use of all the odd-power and Sophie Germain identities can produce a hybrid cover using only the listed \(31\)-prime smooth-index pool.

This conclusion is independent of overlaps and remains true even if every target were allowed.

For the main trial exponents one gets stronger fixed-\(M\) gaps:
\[
S+\delta(\mathcal A_{15})
=
\frac{559335}{746496}+\frac{11}{75}
<\frac{269}{300}<1,
\]
and
\[
S+\delta(\mathcal A_{60})
=
\frac{559335}{746496}+\frac15
<\frac{19}{20}<1.
\]
For \(M=60\), at least about \(0.0507\) additional nominal prime mass is required even before accounting for target restrictions or overlaps.

This eliminates the most immediate implementation of Route 1: the algebraic core cannot merely be appended to the known bounded smooth pool.

## Self-Audit

1. **The exact \(31\)-prime obstruction depends on the pool enumeration supplied in the brief.**  
   I did not independently prove that the list contains every qualifying prime below \(2\cdot10^6\). The mathematical conclusion is unconditional for the displayed \(31\) primes themselves; the claim that they are the complete bounded pool should be rechecked computationally. The exact reciprocal sum is independently reproducible from the displayed indices.

2. **The projective-direction inequality has an explicit hypothesis in its strongest form.**  
   The bound using \(q+1\) central directions assumes \(v_q(h_p)=v_q(p-1)\) for every selected \(q\)-divisible index. Primes with deficient \(q\)-primary order can have noncentral compatible shadows and must instead be handled by the general cellwise inequality in Lemma 7. I believe the statement is sound because the full-primary hypothesis is exactly what implies \(H_p\cap G^q=H_p^q\).

3. **These are only necessary conditions, not a construction.**  
   Passing all mass, target-count, and shadow-capacity tests would not prove coverage. Exact overlap and lifting constraints remain. I have not inferred existence from any of these inequalities; a finite torus or intersection-lattice certificate is still required.

## Computations To Verify

The following Python checks the exact smooth-pool mass, target formula, target table, and character shadows.

```python
from math import gcd, lcm
from fractions import Fraction
from sympy import n_order

SMOOTH_H = [
    4, 6, 12, 16, 18, 36, 36, 48, 96, 108, 144, 162, 216,
    256, 384, 486, 576, 648, 648, 648, 1458, 1728, 2916,
    4608, 5184, 5184, 5832, 23328, 31104, 46656, 746496
]

S = sum((Fraction(1, h) for h in SMOOTH_H), Fraction(0))
print(S, float(S))
assert S == Fraction(559335, 746496)
assert S < Fraction(3, 4)

def subgroup_23(p):
    o2 = n_order(2, p)
    o3 = n_order(3, p)
    H = {
        (pow(2, k, p) * pow(3, ell, p)) % p
        for k in range(o2)
        for ell in range(o3)
    }
    h = lcm(o2, o3)
    assert len(H) == h
    return H, o2, o3, h

def allowed_targets_bruteforce(p, M):
    H, o2, o3, h = subgroup_23(p)
    powers = {pow(x, M, p) for x in range(1, p)}
    T = {
        t for t in H
        if (-pow(t, -1, p)) % p in powers
    }
    return T, h

def target_count_formula(p, M):
    H, o2, o3, h = subgroup_23(p)
    n = p - 1
    d = gcd(M, n)
    e = gcd(n // h, d)
    if (n // 2) % e != 0:
        return 0
    return gcd(h, n // d)

test_primes = [5, 7, 11, 13, 17, 19, 23, 47, 71, 167, 431]

for p in test_primes:
    for M in [3, 15, 60]:
        T, h = allowed_targets_bruteforce(p, M)
        assert len(T) == target_count_formula(p, M)
    print(
        p,
        subgroup_23(p)[3],
        len(allowed_targets_bruteforce(p, 15)[0]),
        len(allowed_targets_bruteforce(p, 60)[0])
    )
```

To compute character data and modulo-\(q\) shadows:

```python
def character_data(p):
    H, o2, o3, h = subgroup_23(p)

    generator = None
    for g in H:
        if n_order(g, p) == h:
            generator = g
            break
    assert generator is not None

    log = {}
    z = 1
    for c in range(h):
        log[z] = c
        z = (z * generator) % p
    assert len(log) == h

    a = log[2 % p]
    b = log[3 % p]
    assert gcd(gcd(a, b), h) == 1
    return h, generator, a, b, log

def allowed_shadow_lines(p, M, q):
    T, h = allowed_targets_bruteforce(p, M)
    assert h % q == 0
    h, g, a, b, log = character_data(p)

    # Each tuple represents a*k + b*l = c modulo q.
    lines = {(a % q, b % q, log[t] % q) for t in T}
    return lines

for p in test_primes:
    h = subgroup_23(p)[3]
    for q in [3, 5]:
        if 15 % q == 0 and h % q == 0:
            print("p, q, lines =", p, q, allowed_shadow_lines(p, 15, q))
```

A proof-producing exact SAT search for a manageable pool can be organized as follows. The mask periods must be included in both coordinate periods.

```python
# Requires: pip install ortools sympy

from ortools.sat.python import cp_model

def algebraic_mask(k, ell, M):
    # Odd-power masks
    n = M
    q = 3
    odd_primes = []
    d = 3
    temp = M
    f = 3
    while f * f <= temp:
        if temp % f == 0:
            odd_primes.append(f)
            while temp % f == 0:
                temp //= f
        f += 2
    if temp > 1 and temp % 2 == 1:
        odd_primes.append(temp)

    if any(k % q == 0 and ell % q == 0 for q in odd_primes):
        return True

    if M % 4 == 0 and k % 4 == 2 and ell % 4 == 0:
        return True

    return False

def exact_cover_sat(primes, M):
    data = {}
    A = B = 1

    # Include algebraic periods.
    temp = M
    odd_primes = []
    f = 3
    while f * f <= temp:
        if temp % f == 0:
            odd_primes.append(f)
            while temp % f == 0:
                temp //= f
        f += 2
    if temp > 1 and temp % 2 == 1:
        odd_primes.append(temp)

    for q in odd_primes:
        A = lcm(A, q)
        B = lcm(B, q)
    if M % 4 == 0:
        A = lcm(A, 4)
        B = lcm(B, 4)

    for p in primes:
        T, h = allowed_targets_bruteforce(p, M)
        o2 = n_order(2, p)
        o3 = n_order(3, p)
        A = lcm(A, o2)
        B = lcm(B, o3)
        data[p] = (sorted(T), o2, o3)

    print("Rectangle size:", A, "x", B, "=", A * B)

    model = cp_model.CpModel()
    choose = {}
    for p, (targets, _, _) in data.items():
        for t in targets:
            choose[p, t] = model.NewBoolVar(f"x_{p}_{t}")
        model.Add(sum(choose[p, t] for t in targets) <= 1)

    for k in range(A):
        for ell in range(B):
            if algebraic_mask(k, ell, M):
                continue
            covering = []
            for p, (targets, o2, o3) in data.items():
                value = (
                    pow(2, k % o2, p) *
                    pow(3, ell % o3, p)
                ) % p
                if value in targets:
                    covering.append(choose[p, value])
            if not covering:
                return None, ("uncoverable cell", k, ell)
            model.Add(sum(covering) >= 1)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 8
    result = solver.Solve(model)

    if result not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return None, "UNSAT"

    selected = {
        p: t for (p, t), var in choose.items()
        if solver.Value(var)
    }
    return selected, "SAT"
```

For large rectangular periods, the same constraints should be generated on
\[
\mathbb Z^2/\bigcap_pL_p
\]
using Smith normal form, or represented by a BDD/ZDD. Any returned target assignment must be independently checked over the exact finite quotient.

## Route Diagnosis

### Proved ledger

1. The precise hybrid-cover sufficiency theorem for \(m=x^M\).
2. Exact algebraic-mask density for arbitrary \(M\).
3. Universal algebraic-density ceiling \(<1/4\).
4. Normalization to \(M=R\) or \(M=4R\), with \(R\) odd and squarefree.
5. Exact formula for compatible target existence and count.
6. Exclusion of odd-order \(H_p\) at \(p\equiv3\pmod4\) for every even \(M\).
7. Central \(q\)-shadow rigidity when \(q\mid M\) and \(H_p\) has the full \(q\)-primary order.
8. Exact cellwise and projective-direction conditional-mass inequalities.
9. Impossibility of using the displayed \(31\)-prime smooth-index pool with this algebraic core for any \(M\).

### Plausible but unproved

1. Odd \(M\), especially \(M=3\) or \(15\), may be preferable to \(M=60\), because all primes remain available and the exact odd-order line primes are retained.
2. A successful cover may exist in a substantially larger mixed-index, cohort-closed pool below \(10^5\), whose total nominal mass is known to be ample.
3. The central-shadow inequalities may eliminate many candidate \(M\) and pools before any full torus search, but this has not yet been run on the complete enumerated pool.

### Dead ends established here

1. The algebraic identities alone cannot approach full coverage: their density is always \(<1/4\).
2. The bounded \(31\)-prime smooth pool cannot be repaired by choosing a larger perfect-power exponent \(M\).
3. \(M=60\) cannot use important odd-order exact-line primes such as \(23,47,167,431\), and its smallest targets are heavily forced.

### Precise block

The route is not blocked by an unproved theorem; it is blocked at a concrete finite design problem. One must find a mixed prime pool, choose one \(M\)-compatible target per prime, pass the modulo-\(q\) conditional-capacity tests for every \(q\mid M\), satisfy cohort constraints at all other index primes, and then prove exact coverage of the resulting finite quotient. No such assignment is currently available.

A fresh attempt should first search normalized exponents
\[
M\in\{3,5,15,12,20,60\},
\]
but should not begin with a full torus SAT instance. It should:

1. enumerate all compatible targets;
2. apply the cellwise inequalities of Lemma 7 as an LP relaxation;
3. perform cohort pruning;
4. retain only pools with substantial mass slack;
5. then run a proof-producing exact quotient search.

The strongest immediate priority is comparing \(M=3,15,12,60\) on the same large mixed pool using the exact target and shadow constraints above.