STATUS: BLOCKED

## Result

Route 3 yields a sharp polynomial reduction but not a complete solution. The direct Combinatorial Nullstellensatz coefficient for \(Q=\Delta P\) vanishes identically whenever \(t\equiv0,3\pmod4\), so the most obvious one-coefficient argument is impossible. Exploiting the exceptional first position gives a better reduction: for \(n=t-1\), define a universal integer coefficient vector \(c_{n,1},\dots,c_{n,n}\). If, for every prime \(p\ge n+2\), at least one \(c_{n,k}\not\equiv0\pmod p\), then the Erdős problem has an affirmative solution. Equivalently, a fixed product of interval linear forms must be nonzero in the type-\(A\) coinvariant algebra over \(\mathbb F_p\). I prove this reduction, its antisymmetrization and differential formulations, and compute
\[
\begin{aligned}
(c_{2,k})&=(1,-1),\\
(c_{3,k})&=(-1,0,1),\\
(c_{4,k})&=(1,-1,-1,1),\\
(c_{5,k})&=(4,-2,-4,-2,4).
\end{aligned}
\]
However, I cannot prove the required nonvanishing for all \(n\), nor rule out a prime \(p\ge n+2\) dividing every \(c_{n,k}\). That coefficient assertion would itself settle the original problem and is the precise block.

## Complete Argument

### 1. The original polynomial is a product of two Vandermondes

Put
\[
Y_j=x_1+\cdots+x_j,\qquad 1\le j\le t.
\]
Then
\[
Y_j-Y_i=x_{i+1}+\cdots+x_j,
\]
and therefore
\[
P(x_1,\dots,x_t)
=\prod_{1\le i<j\le t}(Y_j-Y_i)
=\Delta(Y_1,\dots,Y_t).
\]
Consequently,
\[
Q(x)=\Delta(x_1,\dots,x_t)\Delta(Y_1,\dots,Y_t).
\]

For \(x\in A^t\), \(Q(x)\ne0\) exactly when:

1. the \(x_i\) are pairwise distinct, hence form a permutation of \(A\);
2. the nonempty intervals beginning at position \(2\) have nonzero sum.

Thus this polynomial encodes the problem exactly.

Its total degree is
\[
\deg Q=2\binom t2=t(t-1).
\]
On the grid \(A^t\), where every coordinate set has size \(t\), the only monomial that can meet the standard Combinatorial Nullstellensatz degree condition is
\[
M_t=\prod_{i=1}^t x_i^{t-1}.
\]
Indeed, if all exponents are at most \(t-1\) and their sum is \(t(t-1)\), all of them must equal \(t-1\).

Hence a direct application of the usual Nullstellensatz can only use
\[
C_t=[M_t]Q.
\]

### 2. The direct coefficient vanishes in half the congruence classes

Let \(\tau\) fix \(x_1\) and reverse \(x_2,\dots,x_t\). The factors of \(P\) are all intervals in the word \(x_2,\dots,x_t\), so reversal merely permutes those factors:
\[
P(x_\tau)=P(x).
\]
On the other hand,
\[
\Delta(x_\tau)=\operatorname{sgn}(\tau)\Delta(x),
\qquad
\operatorname{sgn}(\tau)
=(-1)^{(t-1)(t-2)/2}.
\]
Since \(M_t\) is invariant under coordinate permutations,
\[
C_t=\operatorname{sgn}(\tau)C_t.
\]
Over the integers this implies
\[
C_t=0
\quad\text{if}\quad
\frac{(t-1)(t-2)}2\ \text{is odd}.
\]
Equivalently,
\[
\boxed{C_t=0\quad\text{for }t\equiv0,3\pmod4.}
\]

Therefore the most direct one-coefficient proof using \(Q\) is genuinely blocked, not merely computationally inconvenient.

---

### 3. Removing the exceptional first element creates a better polynomial

Let \(A\subseteq\mathbb F_p^\times\) have size \(t\ge2\), and put
\[
T=\sum_{a\in A}a.
\]
There exists \(a\in A\) with \(a\ne T\): at most one member of the set \(A\) can equal \(T\), while \(A\) has at least two members.

Set
\[
B=A\setminus\{a\},\qquad n=|B|=t-1.
\]
Then
\[
\sum_{b\in B}b=T-a\ne0.
\]

Suppose \(b_1,\dots,b_n\) is an ordering of \(B\) such that every nonempty consecutive block of the word \(b_1,\dots,b_n\) has nonzero sum. Then
\[
(a,b_1,\dots,b_n)
\]
is valid for \(A\): every interval relevant to the original validity condition begins at position \(2\), hence is precisely a consecutive block of the \(b\)-word.

Thus it suffices to prove the following stronger statement for every nonzero-sum set \(B\):

> \(B\) has an ordering for which every nonempty consecutive block has nonzero sum.

Singleton blocks are automatically nonzero because \(B\subseteq\mathbb F_p^\times\), and the full block is nonzero because \(\sum B\ne0\). We only need to encode the remaining proper blocks of length at least two.

For \(n\ge2\), define
\[
R_n(z_1,\dots,z_n)
=
\prod_{\substack{1\le r<s\le n\\(r,s)\ne(1,n)}}
(z_r+\cdots+z_s)
\]
and
\[
H_n(z)=\Delta(z_1,\dots,z_n)R_n(z).
\]
The product \(R_n\) ranges over all intervals of length at least two except the full interval.

There are
\[
\binom n2-1
\]
such factors, so
\[
\deg H_n
=
\binom n2+\binom n2-1
=n(n-1)-1.
\]

For \(1\le k\le n\), define
\[
c_{n,k}
=
\left[
z_k^{n-2}\prod_{i\ne k}z_i^{n-1}
\right]H_n.
\]
The displayed monomial has total degree
\[
(n-2)+(n-1)^2=n(n-1)-1,
\]
as required.

### 4. Conditional Nullstellensatz theorem

**Lemma.** Let \(B\subseteq\mathbb F_p^\times\) have size \(n\ge2\) and nonzero total sum. If
\[
c_{n,k}\not\equiv0\pmod p
\]
for some \(k\), then \(B\) has an ordering in which every nonempty consecutive block has nonzero sum.

**Proof.** Apply the Combinatorial Nullstellensatz to \(H_n\) on the grid
\[
B^n.
\]
Use degree bounds
\[
d_k=n-2,\qquad d_i=n-1\quad(i\ne k).
\]
Every coordinate grid has size \(n>d_i\), and
\[
\sum_i d_i=\deg H_n.
\]
Since the coefficient of \(\prod_i z_i^{d_i}\) is nonzero, there is a tuple
\[
(z_1,\dots,z_n)\in B^n
\]
with \(H_n(z)\ne0\).

The Vandermonde factor is nonzero, so the \(z_i\) are distinct. As there are \(n\) of them and \(|B|=n\), they form a permutation of \(B\).

Every proper interval of length at least two has nonzero sum because \(R_n(z)\ne0\). Singleton sums are nonzero because \(B\subseteq\mathbb F_p^\times\), and the full sum is \(\sum B\ne0\). Thus every nonempty consecutive block has nonzero sum. ∎

It follows immediately that the original Erdős assertion would be proved by the following universal coefficient statement:

\[
\boxed{
\forall n\ge2,\ \forall p\ge n+2\text{ prime},\
(c_{n,1},\dots,c_{n,n})\not\equiv(0,\dots,0)\pmod p.
}
\]

Equivalently, if
\[
g_n=\gcd(c_{n,1},\dots,c_{n,n}),
\]
it would suffice to prove that \(g_n\) has no prime divisor greater than \(n+1\).

The condition \(p\ge n+2\) is automatic in the application: \(t=n+1\le p-1\).

---

### 5. Antisymmetrization formula for the coefficient vector

Let
\[
N=\binom n2
\]
and, for a polynomial \(F\), define
\[
\operatorname{Alt}(F)
=
\sum_{\pi\in S_n}\operatorname{sgn}(\pi)
F(z_{\pi(1)},\dots,z_{\pi(n)}).
\]

The polynomial \(z_kR_n\) has degree
\[
1+(N-1)=N.
\]
Every alternating polynomial of degree \(N\) is an integer multiple of the Vandermonde, so there is an integer \(K_{n,k}\) such that
\[
\operatorname{Alt}(z_kR_n)=K_{n,k}\Delta(z).
\]

**Lemma.**
\[
\boxed{c_{n,k}=(-1)^N K_{n,k}.}
\]

**Proof.** Let
\[
M=\prod_{i=1}^n z_i^{n-1}.
\]
By definition,
\[
c_{n,k}=[M]\Delta(z)\,z_kR_n(z).
\]
For a permutation \(\pi\), invariance of \(M\) and alternation of \(\Delta\) give
\[
[M]\Delta(z)(z_kR_n)(z_\pi)
=
\operatorname{sgn}(\pi)c_{n,k}.
\]
Therefore
\[
[M]\Delta\,\operatorname{Alt}(z_kR_n)
=n!c_{n,k}.
\]
On the other hand,
\[
[M]\Delta\,\operatorname{Alt}(z_kR_n)
=
K_{n,k}[M]\Delta^2.
\]

Expand
\[
\Delta
=
\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_i z_i^{\sigma(i)-1}.
\]
A pair of monomials from the two copies of \(\Delta\) contributes to \(M\) exactly when their exponent assignments are complementary under
\[
j\longmapsto n-1-j.
\]
The complementary permutation differs by the reversal permutation, whose sign is \((-1)^N\). There are \(n!\) possible first assignments. Hence
\[
[M]\Delta^2=(-1)^Nn!.
\]
Thus
\[
n!c_{n,k}=(-1)^Nn!K_{n,k},
\]
and cancellation over the integers proves the claim. ∎

Two useful identities follow immediately.

#### Sum identity

Because
\[
\sum_{k=1}^n z_kR_n
=
(z_1+\cdots+z_n)R_n
\]
and \(z_1+\cdots+z_n\) is symmetric,
\[
\operatorname{Alt}\bigl((z_1+\cdots+z_n)R_n\bigr)
=
(z_1+\cdots+z_n)\operatorname{Alt}(R_n).
\]
But \(\deg R_n=N-1<N\), so \(\operatorname{Alt}(R_n)=0\). Therefore
\[
\boxed{\sum_{k=1}^n c_{n,k}=0.}
\]

#### Reversal identity

The polynomial \(R_n\) is invariant under reversal
\[
(z_1,\dots,z_n)\longmapsto(z_n,\dots,z_1).
\]
That reversal has sign \((-1)^N\). Consequently,
\[
\boxed{c_{n,n+1-k}=(-1)^N c_{n,k}.}
\]

These relations are useful computational checks but do not by themselves imply that the vector is nonzero.

---

### 6. Differential formulation

Let
\[
J_n=\prod_{j=0}^{n-1}j!.
\]
Writing \(R_n(\partial)\) for the constant-coefficient differential operator obtained by replacing \(z_i\) by \(\partial/\partial z_i\), direct expansion of the determinant formula for \(\Delta\) gives
\[
\boxed{
R_n(\partial)\Delta(z)
=
J_n\sum_{k=1}^n K_{n,k}z_k.
}
\]

Indeed, every monomial in \(\Delta\) has exponent vector a permutation of
\[
(0,1,\dots,n-1).
\]
To leave the monomial \(z_k\) after applying a degree-\(N-1\) differential operator, the exponent selected from \(R_n\) must be that staircase exponent vector with one subtracted in coordinate \(k\). The derivative multiplier is always
\[
0!1!\cdots(n-1)!=J_n.
\]

Thus the desired coefficient condition is equivalent, for \(p>n\), to
\[
R_n(\partial)\Delta\not\equiv0\pmod p.
\]

This is a compact way to compute the entire vector.

---

### 7. Coinvariant-algebra formulation

Let \(K\) be a field of characteristic \(0\) or characteristic \(p>n\), and let
\[
\mathcal C_n
=
K[z_1,\dots,z_n]/(e_1,\dots,e_n),
\]
where \(e_i\) are the elementary symmetric polynomials.

This is the type-\(A\) coinvariant algebra. It is an Artinian complete intersection with top degree \(N=\binom n2\), and multiplication gives a perfect pairing
\[
(\mathcal C_n)_1\times(\mathcal C_n)_{N-1}
\longrightarrow(\mathcal C_n)_N.
\]
The top component is one-dimensional and affords the sign representation, with \([\Delta]\) as a nonzero generator.

For \(F\) of degree \(N\), if
\[
\operatorname{Alt}(F)=K_F\Delta,
\]
then in the coinvariant algebra
\[
[\operatorname{Alt}(F)]=n![F],
\]
because the top component transforms by sign. Since \(n!\) is invertible when \(\operatorname{char}K>n\),
\[
K_F=0
\quad\Longleftrightarrow\quad
[F]=0\text{ in }(\mathcal C_n)_N.
\]

Applying this to \(F=z_kR_n\), and using perfect pairing, gives

\[
\boxed{
K_{n,1}=\cdots=K_{n,n}=0\text{ in }K
\iff
[R_n]=0\text{ in }\mathcal C_n.
}
\]

Therefore the universal polynomial lemma needed to settle the Erdős problem is exactly
\[
\boxed{
R_n\notin(e_1,\dots,e_n)
\quad\text{over }\mathbb F_p
\quad\text{for every prime }p\ge n+2.
}
\]

This is the cleanest diagnosis I found for Route 3.

---

### 8. Exact coefficients for \(2\le n\le5\)

For \(n=2\),
\[
R_2=1,\qquad H_2=z_2-z_1,
\]
so
\[
(c_{2,1},c_{2,2})=(1,-1).
\]

For \(n=3\),
\[
R_3=(z_1+z_2)(z_2+z_3).
\]
Extracting the three degree-five coefficients gives
\[
(c_{3,1},c_{3,2},c_{3,3})=(-1,0,1).
\]

For \(n=4\),
\[
\begin{aligned}
R_4={}&(z_1+z_2)(z_2+z_3)(z_3+z_4)\\
&\cdot(z_1+z_2+z_3)(z_2+z_3+z_4).
\end{aligned}
\]
For \(c_{4,1}\), the target exponent vector is \((2,3,3,3)\). Expanding the Vandermonde by its exponent assigned to \(z_1\), the contributions for that exponent \(0,1,2,3\) are respectively
\[
0,\quad 2,\quad -1,\quad 0.
\]
Thus \(c_{4,1}=1\). Reversal gives \(c_{4,4}=1\), while the sum identity and reversal give
\[
c_{4,2}=c_{4,3}=-1.
\]
Hence
\[
(c_{4,k})=(1,-1,-1,1).
\]

For \(n=5\), it is convenient to compute the antisymmetrization constants. Evaluate at
\[
x=(-2,-1,0,1,2),
\qquad
\Delta(x)=1!\,2!\,3!\,4!=288.
\]
A term in \(\operatorname{Alt}(z_kR_5)(x)\) can be nonzero only if:

1. the zero occurs in position \(2\), \(3\), or \(4\), because a zero at an endpoint makes a length-four interval vanish;
2. neither opposite pair \(\{1,-1\}\), \(\{2,-2\}\) is cyclically adjacent.

For each possible position of zero, the remaining four entries must alternate between the two opposite pairs around the path obtained by deleting the zero. This leaves exactly \(24\) contributing permutations.

Direct signed summation gives:

\[
\begin{array}{c|rr}
\text{position of }0
&\operatorname{Alt}(z_1R_5)\text{ contribution}
&\operatorname{Alt}(z_2R_5)\text{ contribution}\\ \hline
2&0&0\\
3&576&-576\\
4&576&0
\end{array}
\]

Thus
\[
K_{5,1}=\frac{1152}{288}=4,\qquad
K_{5,2}=\frac{-576}{288}=-2.
\]
Since \(N=10\) is even, \(c_{5,k}=K_{5,k}\). Reversal and the sum identity then give
\[
(c_{5,k})=(4,-2,-4,-2,4).
\]

This calculation also kills two tempting conjectures:

- the endpoint coefficient is not always \(\pm1\);
- the coefficient vector need not be primitive over \(\mathbb Z\), since its gcd for \(n=5\) is \(2\).

Nevertheless, all prime divisors seen here are at most \(n+1\), which is exactly the range harmless for the application.

## Self-Audit

1. **The \(n=5\) coefficient enumeration is the most error-prone finite step.**  
   It involves a signed sum over 24 surviving permutations. I believe it is correct because the contributing permutations are classified completely, the result satisfies both mandatory identities—reversal symmetry and zero coordinate sum—and the supplied code independently recomputes it directly over the integers.

2. **The deletion argument proves a stronger sequencing statement for \(B\), so the first-position asymmetry had to be handled exactly.**  
   The potential error would be accidentally requiring a zero-sum prefix of the full ordering to be forbidden. The proof avoids that: after prepending \(a\), every relevant collision \(S_i=S_j\) has \(i\ge1\), and hence corresponds exactly to an interval lying wholly in the \(B\)-word.

3. **The coinvariant-algebra equivalence uses characteristic \(p>n\).**  
   This is essential because the antisymmetrizer contributes \(n!\). In the actual application \(p\ge n+2\), so \(n!\) is invertible. The main Nullstellensatz reduction does not depend on the coinvariant formulation, so even a presentation issue there would not invalidate the central conditional theorem.

## Computations To Verify

The following exact Python computes \(R_n\), the antisymmetrization constants \(K_{n,k}\), and hence \(c_{n,k}\). It uses only integer arithmetic.

```python
from itertools import permutations
from math import gcd
from functools import reduce

def mul_linear(poly, variables, n):
    """
    poly: dict exponent_tuple -> integer coefficient
    multiply by sum(z_j for j in variables)
    Exponents > n-1 are discarded because no staircase-minus-one
    coefficient can use them.
    """
    out = {}
    for exp, coeff in poly.items():
        for j in variables:
            ee = list(exp)
            ee[j] += 1
            if ee[j] > n - 1:
                continue
            ee = tuple(ee)
            out[ee] = out.get(ee, 0) + coeff
    return out

def R_coefficients(n):
    """
    R_n = product over intervals [r,s], r<s,
    except the full interval [0,n-1].
    """
    zero = (0,) * n
    poly = {zero: 1}

    for r in range(n):
        for s in range(r + 1, n):
            if r == 0 and s == n - 1:
                continue
            poly = mul_linear(poly, range(r, s + 1), n)

    return poly

def permutation_sign(values):
    inv = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                inv += 1
    return -1 if inv % 2 else 1

def K_and_c_vectors(n):
    """
    K_k is defined by Alt(z_k R_n) = K_k Delta.
    c_k = (-1)^(n choose 2) K_k.
    """
    R = R_coefficients(n)
    K = [0] * n

    for alpha in permutations(range(n)):
        sgn = permutation_sign(alpha)

        for k in range(n):
            if alpha[k] == 0:
                continue
            beta = list(alpha)
            beta[k] -= 1
            K[k] += sgn * R.get(tuple(beta), 0)

    N = n * (n - 1) // 2
    c = [((-1) ** N) * x for x in K]
    return K, c

def coefficient_gcd(c):
    return reduce(gcd, (abs(x) for x in c), 0)

for n in range(2, 6):
    K, c = K_and_c_vectors(n)
    print("n =", n)
    print("K =", K)
    print("c =", c)
    print("gcd =", coefficient_gcd(c))
    print("sum =", sum(c))
    print()
```

Expected output:

```text
n = 2
K = [-1, 1]
c = [1, -1]
gcd = 1
sum = 0

n = 3
K = [1, 0, -1]
c = [-1, 0, 1]
gcd = 1
sum = 0

n = 4
K = [1, -1, -1, 1]
c = [1, -1, -1, 1]
gcd = 1
sum = 0

n = 5
K = [4, -2, -4, -2, 4]
c = [4, -2, -4, -2, 4]
gcd = 2
sum = 0
```

The highest-priority experiment is to compute \(g_n\) for as many \(n\) as feasible and factor it:

```python
from sympy import factorint

for n in range(2, 13):
    K, c = K_and_c_vectors(n)
    g = coefficient_gcd(c)
    dangerous = {
        q: e for q, e in factorint(g).items()
        if q >= n + 2
    }
    print(n, c, g, factorint(g), "DANGEROUS:", dangerous)
```

Any prime divisor \(q\ge n+2\) of \(g_n\) would refute this particular universal Nullstellensatz criterion at \((n,p)=(n,q)\), though it would not refute the original ordering conjecture.

For regression testing against direct expansion of \(H_n\):

```python
def mul_factor(poly, terms, cap):
    """
    terms is [(coefficient, variable_index), ...].
    """
    out = {}
    for exp, coeff in poly.items():
        for a, j in terms:
            ee = list(exp)
            ee[j] += 1
            if ee[j] > cap[j]:
                continue
            ee = tuple(ee)
            out[ee] = out.get(ee, 0) + coeff * a
    return out

def direct_c_vector(n):
    c = []
    for missing in range(n):
        target = tuple(n - 2 if i == missing else n - 1
                       for i in range(n))
        poly = {(0,) * n: 1}

        # Vandermonde factors z_j - z_i
        for i in range(n):
            for j in range(i + 1, n):
                poly = mul_factor(poly, [(-1, i), (1, j)], target)

        # Proper nonsingleton interval factors
        for r in range(n):
            for s in range(r + 1, n):
                if r == 0 and s == n - 1:
                    continue
                poly = mul_factor(
                    poly,
                    [(1, j) for j in range(r, s + 1)],
                    target
                )

        c.append(poly.get(target, 0))
    return c

for n in range(2, 7):
    K, c = K_and_c_vectors(n)
    assert c == direct_c_vector(n)
```

Finally, this brute-force test verifies the stronger ordering conclusion for small fields:

```python
from itertools import combinations

def strong_order(B, p):
    """
    Find an ordering for which 0 and all partial sums are distinct.
    This is equivalent to every nonempty consecutive block
    having nonzero sum.
    """
    B = tuple(B)
    n = len(B)

    def dfs(remaining, current_sum, seen, order):
        if not remaining:
            return order
        for i, a in enumerate(remaining):
            z = (current_sum + a) % p
            if z in seen:
                continue
            ans = dfs(
                remaining[:i] + remaining[i+1:],
                z,
                seen | {z},
                order + (a,)
            )
            if ans is not None:
                return ans
        return None

    return dfs(B, 0, {0}, tuple())

def verify_small(p):
    nonzero = list(range(1, p))
    for n in range(2, p):
        K, c = K_and_c_vectors(n)
        if all(x % p == 0 for x in c):
            print("Coefficient criterion fails:", p, n)
            continue

        for B in combinations(nonzero, n):
            if sum(B) % p == 0:
                continue
            assert strong_order(B, p) is not None

for p in [3, 5, 7, 11]:
    verify_small(p)
```

## Route Diagnosis

**What worked.**

- The validity polynomial is exactly a Vandermonde in the partial sums.
- The direct central coefficient was shown rigorously to vanish for \(t\equiv0,3\pmod4\).
- The exceptional first position can be exploited by deleting one element \(a\ne\sum A\). This removes the singleton and full-interval factors and leaves exactly one degree of Nullstellensatz slack.
- The resulting coefficient problem has three equivalent forms:
  1. some \(c_{n,k}\not\equiv0\pmod p\);
  2. \(R_n(\partial)\Delta\not\equiv0\pmod p\);
  3. \([R_n]\ne0\) in the type-\(A\) coinvariant algebra over \(\mathbb F_p\).

**What is blocked.**

The missing theorem is
\[
[R_n]\ne0
\quad\text{in}\quad
\mathbb F_p[z_1,\dots,z_n]/(e_1,\dots,e_n)
\]
for every prime \(p\ge n+2\). I found no argument proving this and no computation producing a counterexample. The naïve strengthening that the coefficients are primitive is already false at \(n=5\), where their gcd is \(2\). Establishing that all prime divisors of \(g_n\) are at most \(n+1\) remains unproved and is strong enough to solve the original problem outright.

**Dead ends.**

- The original single central coefficient cannot work uniformly because it vanishes in two residue classes modulo \(4\).
- The conjecture \(c_{n,1}=\pm1\) fails at \(n=5\), where \(c_{5,1}=4\).
- The conjecture \(\gcd(c_{n,1},\dots,c_{n,n})=1\) fails at \(n=5\), where the gcd is \(2\).
- The raw occurrence of a coefficient-\(1\) “right-endpoint” monomial in \(R_n\) does not prove nonvanishing in the coinvariant quotient; reduction by symmetric polynomials can alter its coefficient.

**Best next step.**

Compute and factor \(g_n\) substantially farther. If a prime \(q\ge n+2\) divides \(g_n\), the universal one-coefficient Nullstellensatz route fails concretely and one should inspect lower interpolation coefficients depending on \(A\). If no dangerous primes appear, the most promising theoretical target is a recurrence or \(p\)-local proof for the linear polynomial
\[
R_n(\partial)\Delta.
\]
A flag-variety or Schubert-calculus interpretation of the divisibility of \([R_n]\) may explain why its content has only small prime factors. Without such a theorem, Route 3 remains blocked rather than a complete solution.