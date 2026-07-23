STATUS: BLOCKED

## Result

Route 4 gives a clean finite-dimensional \(E\)-function realization of every \(H_k\), but it does not yield the uniform lower bounds needed as \(k\to\infty\). I proved: (i) \(H_k(1)\) is an \(E\)-function value after the pullback \(z\mapsto z^k\); (ii) the resulting functions are linearly independent over \(\mathbb C(z)\); (iii) rationality of \(\alpha\) would produce linear forms in \(1,H_1,\dots,H_K\) of size essentially \(2^{-K}\); and (iv) the generating function aggregating all \(k\) is not D-finite, hence is outside finite \(E\)-function theory. Even finite algebraic independence of all prefixes would not by itself exclude a rational infinite sum. The precise unresolved step is a lower bound, uniform in \(K\), for these special linear forms.

## Complete Argument

### 1. The exact linear forms forced by rationality

Put
\[
G_k:=H_k-2=\sum_{n=2}^{\infty}\frac1{(n!)^k}.
\]
Then
\[
\alpha=\sum_{k=1}^{\infty}G_k.
\]
For \(K\ge1\), define
\[
U_K:=\sum_{k=1}^K G_k,\qquad T_K:=\alpha-U_K.
\]
By Tonelli and the geometric series,
\[
\begin{aligned}
T_K
&=\sum_{n=2}^{\infty}\sum_{k=K+1}^{\infty}\frac1{(n!)^k}\\
&=\sum_{n=2}^{\infty}
\frac{(n!)^{-(K+1)}}{1-(n!)^{-1}}\\
&=\sum_{n=2}^{\infty}\frac1{(n!)^K(n!-1)}.
\end{aligned}
\]
The \(n=2\) term is exactly \(2^{-K}\). For \(n\ge3\),
\[
\frac1{(n!)^K(n!-1)}
\le \frac2{(n!)^{K+1}}
\le \frac{2}{6^K n!}.
\]
Since
\[
\sum_{n=3}^{\infty}\frac1{n!}=e-\frac52<\frac14,
\]
we obtain the explicit estimate
\[
\boxed{\frac1{2^K}<T_K<
\frac1{2^K}+\frac1{2\cdot 6^K}.}
\tag{1}
\]

Suppose now that
\[
\alpha=\frac pq,\qquad p\in\mathbb Z,\quad q\in\mathbb N.
\]
Then
\[
\Lambda_K
:=q\sum_{k=1}^K H_k-(2qK+p)
=qU_K-p
=-qT_K.
\]
Consequently,
\[
\boxed{
\frac q{2^K}<|\Lambda_K|
<
q\left(\frac1{2^K}+\frac1{2\cdot6^K}\right).
}
\tag{2}
\]
Thus rationality would generate, for every \(K\), an exponentially small nonzero linear form in
\[
1,H_1,\dots,H_K
\]
whose coefficients have height only \(O_{p,q}(K)\).

This is the exact quantitative target for Route 4. For example, any estimate
\[
|\Lambda_K|\ge \exp(-o(K))
\tag{3}
\]
for these particular coefficient vectors would contradict (2). More generally, a bound
\[
|\Lambda_K|\ge K^{-C_K}
\]
would suffice if
\[
C_K\log K=o(K).
\]

### 2. Every \(H_k\) is an \(E\)-function value after a pullback

The function
\[
H_k(w)=\sum_{n=0}^{\infty}\frac{w^n}{(n!)^k}
\]
satisfies
\[
\theta_w^kH_k(w)=wH_k(w),
\qquad \theta_w=w\frac d{dw}.
\tag{4}
\]
Indeed, the coefficient of \(w^n\), \(n\ge1\), on the left is
\[
\frac{n^k}{(n!)^k}=\frac1{((n-1)!)^k},
\]
which is the coefficient of \(w^n\) on the right.

For \(k\ge2\), \(H_k(w)\) itself is not an \(E\)-function in the strict Siegel normalization. Writing
\[
H_k(w)=\sum_{n=0}^{\infty}a_n\frac{w^n}{n!}
\]
gives
\[
a_n=\frac1{(n!)^{k-1}}.
\]
A common denominator for \(a_0,\dots,a_n\) must therefore be divisible by \((n!)^{k-1}\), which grows faster than \(C^n\) for every fixed \(C\).

The obstruction disappears after the pullback
\[
f_k(z):=H_k(z^k)
=\sum_{n=0}^{\infty}\frac{z^{kn}}{(n!)^k}.
\]
In exponential-series normalization,
\[
f_k(z)=\sum_{m=0}^{\infty}a_m\frac{z^m}{m!},
\]
where
\[
a_m=
\begin{cases}
\dfrac{(kn)!}{(n!)^k},&m=kn,\\[1ex]
0,&k\nmid m.
\end{cases}
\]
The nonzero \(a_m\) are integers. Moreover,
\[
\frac{(kn)!}{(n!)^k}\le k^{kn}=k^m,
\]
because the multinomial coefficient on the left is one term in the sum of all multinomial coefficients of total degree \(kn\), whose sum is \(k^{kn}\). Hence the coefficients have exponential growth and denominator one.

Using (4),
\[
\theta_z^k f_k(z)
=k^k\theta_w^kH_k(w)\big|_{w=z^k}
=k^kz^k f_k(z).
\]
Therefore
\[
\boxed{(\theta_z^k-k^kz^k)f_k(z)=0.}
\tag{5}
\]
Thus \(f_k\) is an \(E\)-function and
\[
f_k(1)=H_k.
\]

For example,
\[
f_1(z)=e^z,
\]
while
\[
f_2(z)=H_2(z^2)=I_0(2z)
\]
satisfies
\[
z^2f_2''+zf_2'-4z^2f_2=0.
\]

For a finite truncation \(1\le k\le K\), let
\[
Y_{k,j}:=\theta^j f_k,\qquad 0\le j<k.
\]
Then
\[
Y_{k,j}'=\frac1zY_{k,j+1}\quad (j<k-1),
\]
and
\[
Y_{k,k-1}'=k^kz^{k-1}Y_{k,0}.
\]
Together with the constant function \(1\), these form a first-order system of dimension
\[
\boxed{D_K=1+\sum_{k=1}^K k
=1+\frac{K(K+1)}2.}
\tag{6}
\]
The point \(z=1\) is ordinary. Hence each finite family lies genuinely within finite-dimensional \(E\)-function theory. However, both the dimension and the arithmetic complexity of the system grow with \(K\).

### 3. Functional linear independence of the pulled-back functions

The functions
\[
1,f_1,\dots,f_K
\]
are linearly independent over \(\mathbb C(z)\).

First, for \(x>0\),
\[
f_k(x)\le e^{kx}.
\tag{7}
\]
Indeed,
\[
\frac{x^{kn}}{(n!)^k}
\le \frac{(kx)^{kn}}{(kn)!},
\]
and summing these selected terms of \(e^{kx}\) gives (7).

For a lower bound, let \(x\ge2\) and \(n=\lfloor x\rfloor\). Since \(\log t\) is increasing,
\[
\log(n!)
\le \int_1^n\log t\,dt+\log n
=n\log n-n+1+\log n.
\]
Thus
\[
n!\le e\,n^{n+1}e^{-n}.
\]
The \(n\)-th term of \(f_k(x)\) consequently gives
\[
\begin{aligned}
f_k(x)
&\ge \left(\frac{x^n}{n!}\right)^k\\
&\ge \left(\frac{n^n}{n!}\right)^k\\
&\ge e^{k(n-1)}n^{-k}\\
&\ge e^{kx-2k}x^{-k}.
\end{aligned}
\tag{8}
\]

Suppose that
\[
P_0(z)+\sum_{k=1}^K P_k(z)f_k(z)=0
\tag{9}
\]
with polynomials \(P_k\), obtained after clearing denominators from a putative rational-function relation. Let \(r\) be the largest index for which \(P_r\ne0\). For all sufficiently large positive \(x\),
\[
|P_r(x)|\ge c x^d
\]
for suitable \(c>0,d\ge0\). From (8),
\[
|P_r(x)|f_r(x)
\ge c e^{-2r}x^{d-r}e^{rx}.
\tag{10}
\]
On the other hand, by (7), the absolute value of the sum of all lower-index terms in (9) is at most
\[
C x^D e^{(r-1)x}
\]
if \(r\ge2\), and at most a polynomial if \(r=1\). This contradicts (10) as \(x\to+\infty\). Hence every \(P_k\) vanishes, proving the claim.

This is meaningful functional independence, but it does not automatically imply independence of the values at \(z=1\). For example,
\[
g(z)=1+(z-1)e^z
\]
is an \(E\)-function, and \(1,g(z)\) are linearly independent over \(\mathbb C(z)\), yet
\[
g(1)=1.
\]
Thus any use of a Siegel–Shidlovskii theorem must analyze the full differential system and possible specialization relations, not merely the selected functions.

More importantly, even finite algebraic independence of the values would only prove \(\Lambda_K\ne0\). Under the rationality assumption, this is already known from the positive tail. What is needed is a lower bound stronger than (2).

### 4. The aggregation over \(k\) leaves the D-finite category

The ordinary generating function of the corrections \(G_k\) is
\[
A(t):=\sum_{k=1}^{\infty}G_kt^k.
\]
For \(|t|<2\), Tonelli or absolute convergence gives
\[
\begin{aligned}
A(t)
&=\sum_{n=2}^{\infty}\sum_{k=1}^{\infty}
\left(\frac{t}{n!}\right)^k\\
&=\sum_{n=2}^{\infty}\frac{t}{n!-t}.
\end{aligned}
\tag{11}
\]
In particular,
\[
A(1)=\alpha.
\]

Formula (11) provides a meromorphic continuation to the entire complex plane, with simple poles at
\[
t=n!,\qquad n\ge2.
\]
To justify this, let \(C\) be a compact set avoiding these points and let \(R=\max_{t\in C}|t|\). For all sufficiently large \(n\), \(n!>2R\), and then
\[
\left|\frac{t}{n!-t}\right|
\le \frac{2R}{n!}.
\]
The series therefore converges normally on \(C\). At \(t=N!\), the \(N\)-th summand has residue \(-N!\), while every other summand is analytic, so the pole cannot cancel.

A D-finite germ satisfies a linear differential equation with polynomial coefficients and therefore has only finitely many possible finite singularities, namely zeros of the leading coefficient. Since \(A(t)\) has infinitely many finite poles, it follows that
\[
\boxed{A(t)\ \text{is not D-finite}.}
\tag{12}
\]
In particular, it is not an \(E\)-function. Equivalently, the sequence \(G_k\) cannot satisfy a polynomial-coefficient recurrence of fixed order.

Thus the most natural attempt to package all \(H_k\) into one function falls outside standard finite hypergeometric and \(E\)-function theory.

### 5. Qualitative finite algebraic independence would still be insufficient

There exist positive real numbers \(x_1,x_2,\dots\) such that:

1. every finite subset is algebraically independent over \(\mathbb Q\);
2. \(x_n=O(2^{-n})\);
3. \(\sum_{n\ge1}x_n=1\).

Here is a construction. Set \(r_0=1\), and let
\[
\varepsilon_n=2^{-n-3}.
\]
Suppose \(x_1,\dots,x_{n-1}\) have been selected and
\[
r_{n-1}=1-\sum_{j<n}x_j>0.
\]
The algebraic closure of
\[
\mathbb Q(x_1,\dots,x_{n-1})
\]
inside \(\mathbb R\) is countable. Hence one can choose
\[
x_n\in
\left(\left(\frac12-\varepsilon_n\right)r_{n-1},
      \left(\frac12+\varepsilon_n\right)r_{n-1}\right)
\]
outside that algebraic closure. Define
\[
r_n=r_{n-1}-x_n.
\]
Then
\[
\left(\frac12-\varepsilon_n\right)r_{n-1}
<r_n<
\left(\frac12+\varepsilon_n\right)r_{n-1}.
\]
Since \(\sum\varepsilon_n<\infty\), the products
\[
2^nr_n
=\prod_{j=1}^n\left(1+\delta_j\right),
\qquad |\delta_j|<2\varepsilon_j,
\]
remain bounded above and away from zero. Consequently,
\[
r_n\asymp2^{-n},
\qquad x_n=O(2^{-n}).
\]
Also \(r_n\to0\), so \(\sum x_n=1\). By construction, every \(x_n\) is transcendental over the field generated by its predecessors; therefore every finite subset is algebraically independent.

This counterexample shows that even the strongest conceivable qualitative theorem asserting algebraic independence of every finite prefix of the corrections \(G_k\) would not by itself prove that their infinite sum is irrational.

### 6. Precise point of blockage

The finite systems (6) are eligible for fixed-dimensional \(E\)-function methods, but rationality of \(\alpha\) would require excluding the moving family
\[
qH_1+\cdots+qH_K-(2qK+p),
\]
whose size would be approximately \(q2^{-K}\).

A fixed-\(K\) theorem proving this form nonzero is insufficient. A quantitative estimate must remain effective while:

- the number of functions grows like \(K\);
- the full differential-system dimension grows like \(K^2/2\);
- the differential equations have coefficients involving \(k^k\);
- the coefficient height of the particular linear form is only \(O(K)\).

No uniform estimate of strength \(\exp(-o(K))\), or even \(K^{-o(K/\log K)}\), has been obtained here. Establishing such an estimate for these special forms would essentially settle the original problem.

## Self-Audit

1. **The main limitation is that no numerical-value independence theorem is proved.**  
   Functional linear independence of the \(f_k\) does not imply independence of \(H_k=f_k(1)\), as the explicit \(1+(z-1)e^z\) counterexample shows. I have therefore not used that implication anywhere.

2. **Non-D-finiteness only blocks the standard finite-system packaging; it does not prove that every hypergeometric method must fail.**  
   The claim itself is rigorous because the continuation (11) has infinitely many certified simple poles, whereas a D-finite function has only finitely many finite singular points. A more specialized arithmetic theory for such meromorphic partial-fraction sums could still exist.

3. **The assertion that available finite \(E\)-function machinery lacks the required uniformity is a route diagnosis, not an impossibility theorem.**  
   The rigorous content is the exact threshold (2)–(3) and the growing dimension (6). A sufficiently sharp new uniform zero estimate could overcome the block; none is supplied here.

## Computations To Verify

The following code checks the exact truncations, tail estimates, differential equation coefficients, and candidate linear forms.

```python
from fractions import Fraction
from math import factorial

# Certified interval for H_k = sum_{n >= 0} 1/(n!)^k.
def H_interval(k, N):
    s = Fraction(0)
    for n in range(N + 1):
        s += Fraction(1, factorial(n) ** k)

    # First omitted term is n=N+1.
    a = factorial(N + 1)
    rho = Fraction(1, (N + 2) ** k)
    err = Fraction(1, a ** k) / (1 - rho)
    return s, s + err

# Certified interval for
# T_K = sum_{n >= 2} 1 / ((n!)^K (n!-1)).
def T_interval(K, N):
    s = Fraction(0)
    for n in range(2, N + 1):
        a = factorial(n)
        s += Fraction(1, (a ** K) * (a - 1))

    # For omitted n, use
    # 1/(a^K(a-1)) <= 2/a^(K+1).
    a = factorial(N + 1)
    rho = Fraction(1, (N + 2) ** (K + 1))
    err = Fraction(2, a ** (K + 1)) / (1 - rho)
    return s, s + err

# Verify the elementary global bounds
# 2^(-K) < T_K < 2^(-K) + (1/2)6^(-K).
def verify_T_bounds(max_K=30, N=20):
    for K in range(1, max_K + 1):
        lo, hi = T_interval(K, N)
        lower_bound = Fraction(1, 2 ** K)
        upper_bound = lower_bound + Fraction(1, 2 * (6 ** K))
        assert lo > lower_bound
        assert hi < upper_bound
    return True

# Certified interval for Lambda_K =
# q * sum_{k=1}^K H_k - (2qK+p).
def lambda_interval(K, p, q, N):
    lo = Fraction(0)
    hi = Fraction(0)
    for k in range(1, K + 1):
        h_lo, h_hi = H_interval(k, N)
        lo += h_lo
        hi += h_hi

    constant = 2 * q * K + p
    return q * lo - constant, q * hi - constant

# Verify coefficientwise:
# theta^k f_k = k^k z^k f_k,
# where f_k = sum_n z^(kn)/(n!)^k.
def verify_differential_equation(max_k=12, max_n=30):
    for k in range(1, max_k + 1):
        for n in range(1, max_n + 1):
            lhs = Fraction((k * n) ** k, factorial(n) ** k)
            rhs = Fraction(k ** k, factorial(n - 1) ** k)
            assert lhs == rhs
    return True

# Certified interval for alpha from the original n-sum.
def alpha_interval(N):
    s = Fraction(0)
    for n in range(2, N + 1):
        s += Fraction(1, factorial(n) - 1)

    m = N + 1
    fm = factorial(m)

    lower_tail = Fraction(1, fm - 1)
    upper_tail = (
        Fraction(1, 1) / (1 - Fraction(1, fm))
        * Fraction(m + 1, m * fm)
    )
    return s + lower_tail, s + upper_tail

if __name__ == "__main__":
    print("Tail bounds:", verify_T_bounds())
    print("ODE coefficients:", verify_differential_equation())

    lo, hi = alpha_interval(12)
    print("alpha interval:")
    print(float(lo), float(hi))

    for K in range(1, 10):
        loT, hiT = T_interval(K, 15)
        print(K, float(loT * (2 ** K)), float(hiT * (2 ** K)))
```

For direct construction of the finite differential system:

```python
import sympy as sp

def companion_system(K):
    z = sp.symbols('z')
    dim = 1 + K * (K + 1) // 2
    A = sp.zeros(dim, dim)

    # Coordinate 0 is the constant function 1.
    offset = 1
    for k in range(1, K + 1):
        # Coordinates offset+j represent theta^j f_k, 0 <= j < k.
        for j in range(k - 1):
            A[offset + j, offset + j + 1] = 1 / z
        A[offset + k - 1, offset] = k**k * z**(k - 1)
        offset += k

    return A

print(companion_system(3))
```

## Route Diagnosis

**Proved ledger**

- The exact rationality-forced linear forms (2), with error asymptotic to \(q2^{-K}\).
- The strict \(E\)-function realization
  \[
  f_k(z)=H_k(z^k),\qquad f_k(1)=H_k,
  \]
  and its differential equation.
- Linear independence of \(1,f_1,\dots,f_K\) over \(\mathbb C(z)\).
- The aggregate generating function
  \[
  A(t)=\sum_{k\ge1}(H_k-2)t^k
  =\sum_{n\ge2}\frac{t}{n!-t}
  \]
  is not D-finite.
- Finite algebraic independence, even with geometric decay, does not prevent a rational infinite sum.

**Plausible but unproved**

- Strong algebraic-independence statements for fixed finite families of the values \(H_k\).
- A quantitative \(E\)-function lower bound tailored to the equal-coefficient forms \(\Lambda_K\).
- The possibility that the special direct-sum systems possess more favorable uniform estimates than general \(E\)-function systems.

**Dead ends**

- Treating \(H_k(z)\) itself as a strict \(E\)-function for \(k\ge2\): its normalized denominators grow factorially.
- Concluding value independence from functional independence: false by explicit counterexample.
- Packaging all \(H_k\) into a single D-finite function of \(k\): the natural generating function has infinitely many poles.
- Using only qualitative finite transcendence or algebraic independence: logically insufficient for an infinite sum.

A fresh Route 4 attempt should target the very special coefficient vector
\[
(q,\dots,q,-2qK-p)
\]
rather than seek a general algebraic-independence measure in dimension \(K^2/2\). Alternatively, one should exploit the common moment representation
\[
H_k-2=\sum_{n=2}^{\infty}\left(\frac1{n!}\right)^k
\]
or the meromorphic pole structure of \(A(t)\) to construct a uniform linear-form estimate. At present, obtaining the necessary bound is an unproved statement of essentially the same difficulty as the original irrationality problem.