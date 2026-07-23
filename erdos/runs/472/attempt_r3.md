STATUS: BLOCKED

## Result

Route 3 does not currently yield a proof or disproof. I established an exact reduction separating unrestricted prime-pair abundance from the correlation of the trajectory with the relevant lower endpoints. A global Hardy–Littlewood lower bound would suffice only if the trajectory omits fewer primes than the number of available prime-pair endpoints, or if one proves a genuinely subset-sensitive discrepancy estimate. I also proved a strong obstruction: for every \(\varepsilon>0\) and every fixed modulus \(W\), there are arbitrarily large legal terminal seeds containing more than a \(1-\varepsilon\) proportion of all primes below their final term and approximately equidistributed in every reduced residue class modulo \(W\). Thus ordinary density—even density tending to one—and any fixed collection of modular equidistribution tests are insufficient. The remaining subset-correlation estimate is of essentially the same strength as the original problem.

## Complete Argument

All logarithms below are natural.

### 1. Exact prime-pair reduction

At a state
\[
Q_n=\{q_1,\ldots,q_n\},\qquad p=q_n,\qquad h=p-1,
\]
define the unrestricted lower-endpoint set
\[
R(p)=\{r\le p:r\in\mathbb P,\ r+h\in\mathbb P\}.
\]
Also define
\[
C(Q_n,p)=\#\{i\le n:q_i+h\in\mathbb P\}.
\]

#### Lemma 1
The recurrence extends from \(p\) if and only if
\[
Q_n\cap R(p)\ne\varnothing.
\]
Indeed,
\[
C(Q_n,p)=|Q_n\cap R(p)|.
\]

#### Proof
For \(q_i\in Q_n\),
\[
q_i\in R(p)
\iff q_i+p-1\in\mathbb P.
\]
The latter is exactly the condition that index \(i\) supplies a prime candidate. Therefore the candidate set is nonempty exactly when \(Q_n\cap R(p)\) is nonempty. ∎

This isolates the two distinct Route 3 issues:

1. prove that \(R(p)\) is large for the growing shift \(h=p-1\);
2. prove that the adaptive set \(Q_n\) intersects \(R(p)\).

The first is already a uniform prime-pair problem. The second is not implied by the first.

### 2. A rigorous sufficient density threshold

Let
\[
E(Q_n,p)=\pi(p)-n.
\]
Since \(Q_n\) consists of \(n\) distinct primes not exceeding \(p\), this is exactly the number of primes at most \(p\) omitted by the trajectory.

#### Lemma 2
At every state,
\[
C(Q_n,p)\ge |R(p)|-E(Q_n,p).
\]
Consequently, if
\[
|R(p)|>E(Q_n,p),
\]
then the recurrence extends.

#### Proof
Every member of \(R(p)\) which is not in \(Q_n\) belongs to
\[
\{r\le p:r\in\mathbb P\}\setminus Q_n,
\]
a set of cardinality \(E(Q_n,p)\). Hence
\[
|R(p)\setminus Q_n|\le E(Q_n,p).
\]
Therefore
\[
|R(p)\cap Q_n|
=|R(p)|-|R(p)\setminus Q_n|
\ge |R(p)|-E(Q_n,p).
\]
The final assertion follows from Lemma 1. ∎

Thus an unrestricted Hardy–Littlewood lower bound would be useful if paired with an extremely strong trajectory-density statement. For example, suppose one could prove uniformly along a trajectory that
\[
|R(p)|\ge c\,\mathfrak S(p-1)\frac{p}{(\log p)^2}
\]
and
\[
E(Q_n,p)<c\,\mathfrak S(p-1)\frac{p}{(\log p)^2}.
\]
Then Lemma 2 would prove extension at every such state.

This requires the trajectory to contain all but \(O(p/\log^2p)\) of the primes below \(p\), not merely a positive proportion of them.

The omission count has the following exact evolution.

#### Lemma 3
If the recurrence moves from \(p=q_n\) to \(p'=q_{n+1}\), then
\[
E(Q_{n+1},p')
=
E(Q_n,p)+\pi(p')-\pi(p)-1.
\]

#### Proof
Directly,
\[
\begin{aligned}
E(Q_{n+1},p')
&=\pi(p')-(n+1)\\
&=\bigl(\pi(p)-n\bigr)+\pi(p')-\pi(p)-1.
\end{aligned}
\]
∎

Thus omissions are permanent. They increase by precisely the number of ambient primes strictly between \(p\) and the newly generated prime \(p'\).

No available theorem controls this accumulation at the \(p/\log^2p\) scale.

### 3. The exact subset discrepancy required by Route 3

Set
\[
\alpha_n=\frac{n}{\pi(p)}
\]
and define the discrepancy
\[
D(Q_n,p)
=
|Q_n\cap R(p)|-\alpha_n|R(p)|.
\]
This gives the identity
\[
C(Q_n,p)=\alpha_n|R(p)|+D(Q_n,p).
\]

A uniform Hardy–Littlewood prediction for the unrestricted set would have the shape
\[
|R(p)|\sim
\mathfrak S(p-1)\frac{p}{(\log p)^2}.
\]
Using \(\pi(p)\sim p/\log p\), the corresponding representative-subset main term is
\[
\alpha_n|R(p)|
\sim
\mathfrak S(p-1)\frac{n}{\log p}.
\]

Therefore a sufficient Route 3 discrepancy estimate would be, for some fixed \(\eta>0\),
\[
D(Q_n,p)\ge -(1-\eta)\alpha_n|R(p)|.
\]
It would imply
\[
C(Q_n,p)\ge \eta\alpha_n|R(p)|>0.
\]

This is rigorous as an implication, but the discrepancy estimate is unproved and is essentially the desired subset-sensitive prime-pair theorem.

The basic growth bound does not by itself provide an averaging margin.

#### Lemma 4
For a generated trajectory starting at \(q_m\),
\[
q_n<2^{\,n-m}q_m.
\]
Hence, along any infinite trajectory,
\[
\liminf_{n\to\infty}\frac{n}{\log q_n}\ge\frac1{\log 2}.
\]

#### Proof
At every generated step,
\[
q_{k+1}=q_k+q_{j_k}-1\le 2q_k-1<2q_k.
\]
Iteration gives the first assertion. Taking logarithms gives
\[
\log q_n<\log q_m+(n-m)\log 2,
\]
from which the second assertion follows. ∎

Thus the Hardy–Littlewood main term
\[
\mathfrak S(q_n-1)\frac{n}{\log q_n}
\]
need only remain of constant order under the worst allowed growth. It is not forced to tend to infinity. The slow-growth goal \(\log q_n=o(n)\) would create a much stronger margin, but proving that requires the same prime-existence input and is circular.

### 4. Counterexample to density-based Route 3 lemmas

The following result rules out any static theorem based only on high density and equidistribution modulo finitely many fixed moduli.

#### Theorem 5: Dense, fixed-modulus-equidistributed terminal seeds
Let \(W\ge1\) and \(\varepsilon>0\). There exist arbitrarily large primes \(p\) and finite increasing prime seeds
\[
Q=\{q_1<\cdots<q_m=p\}
\]
such that:

1. \(Q\) is terminal at \(p\);
2. \(|Q|>(1-\varepsilon)\pi(p)\);
3. for every reduced residue class \(a\bmod W\),
   \[
   \left|
   \frac{\#\{q\in Q:q\equiv a\pmod W\}}{|Q|}
   -\frac1{\varphi(W)}
   \right|<\varepsilon.
   \]

#### Proof

Choose a finite set \(S\) of odd primes, none dividing \(W\), such that
\[
\delta_S:=\prod_{\ell\in S}\frac{\ell-2}{\ell-1}<\frac{\varepsilon}{2}.
\]
Such a set exists because
\[
\prod_{\ell\in S}\frac{\ell-2}{\ell-1}
=
\prod_{\ell\in S}\left(1-\frac1{\ell-1}\right)
\le
\exp\left(-\sum_{\ell\in S}\frac1{\ell-1}\right),
\]
and the sum of reciprocals of primes remains divergent after removing the finitely many prime divisors of \(2W\).

Choose a distinguished prime \(L\in S\). For each \(\ell\in S\), prescribe a reduced residue \(c_\ell\bmod\ell\) by
\[
c_L=2^{-1}\pmod L,
\qquad
c_\ell=2\pmod\ell\quad(\ell\ne L).
\]
None of these residues is \(0\) or \(1\pmod\ell\). Define
\[
b_\ell=1-c_\ell\pmod\ell.
\]
Each \(b_\ell\) is also nonzero. Moreover,
\[
b_L=1-2^{-1}=2^{-1}=c_L\pmod L.
\]

Let
\[
M=\prod_{\ell\in S}\ell.
\]
Choose any reduced residue \(a_0\bmod W\). By the Chinese remainder theorem, there is a reduced residue \(A\bmod WM\) satisfying
\[
A\equiv a_0\pmod W,
\qquad
A\equiv c_\ell\pmod\ell
\quad(\ell\in S).
\]
Dirichlet’s theorem, or the prime number theorem in arithmetic progressions, gives arbitrarily large primes
\[
p\equiv A\pmod{WM}.
\]
Choose such a \(p>\max S\).

Define
\[
Q=
\left\{
r\le p:r\in\mathbb P,\ 
r\equiv b_\ell\pmod\ell
\text{ for at least one }\ell\in S
\right\}.
\]

Because \(p\equiv c_L=b_L\pmod L\), we have \(p\in Q\), so \(p\) is its largest element.

For every \(r\in Q\), choose \(\ell\in S\) with \(r\equiv b_\ell\pmod\ell\). Then
\[
p+r-1
\equiv
c_\ell+b_\ell-1
\equiv0\pmod\ell.
\]
Also,
\[
p+r-1\ge p+1>\ell.
\]
Thus every candidate \(p+r-1\) is composite. Hence \(Q\) is terminal at \(p\).

It remains to prove density and equidistribution.

Among the \(\varphi(M)=\prod_{\ell\in S}(\ell-1)\) reduced residue classes modulo \(M\), the number which avoid all conditions
\[
r\equiv b_\ell\pmod\ell
\]
is
\[
\prod_{\ell\in S}(\ell-2).
\]
Therefore the proportion of reduced classes modulo \(M\) included in \(Q\) is
\[
1-\delta_S.
\]

Because \((M,W)=1\), this same proportion occurs independently inside every fixed reduced residue class modulo \(W\). Applying the prime number theorem in arithmetic progressions to the fixed modulus \(WM\), we obtain, for every \((a,W)=1\),
\[
\#\{r\le x:r\in Q,\ r\equiv a\pmod W\}
\sim
\frac{1-\delta_S}{\varphi(W)}\operatorname{Li}(x).
\]
Summing over the reduced classes modulo \(W\),
\[
\#\{r\le x:r\in Q\}
\sim
(1-\delta_S)\operatorname{Li}(x).
\]
The finitely many primes dividing \(WM\) do not affect either asymptotic.

Since \(\pi(x)\sim\operatorname{Li}(x)\),
\[
\frac{|Q\cap[1,x]|}{\pi(x)}\longrightarrow1-\delta_S>1-\frac{\varepsilon}{2}.
\]
Also, within \(Q\),
\[
\frac{\#\{r\le x:r\in Q,\ r\equiv a\pmod W\}}
{|Q\cap[1,x]|}
\longrightarrow\frac1{\varphi(W)}.
\]
These asymptotics remain valid when \(x\) is restricted to the arbitrarily large primes \(p\equiv A\pmod{WM}\). Choosing \(p\) sufficiently large gives assertions 2 and 3. ∎

Taking \(W=1\) and \(\varepsilon\to0\) gives a sequence of terminal seeds satisfying
\[
\frac{|Q|}{\pi(p)}\longrightarrow1.
\]

A small instance is
\[
Q=(2,5,11).
\]
Here \(p=11\equiv2\pmod3\), every seed prime is \(2\pmod3\), and
\[
11+2-1=12,\qquad
11+5-1=15,\qquad
11+11-1=21.
\]
Thus this seed is terminal.

Theorem 5 does not disprove the existence problem: these are deliberately engineered initial seeds, not states proved to arise after a long generated trajectory. It does prove that high ordinary density and any fixed amount of modular equidistribution cannot establish the Route 3 key lemma.

### 5. Exact modular form of terminality

#### Lemma 6
Let \(p=q_n\ge3\). If the state is terminal, then for every \(i\le n\) there is a prime
\[
\ell_i<\sqrt{2p}
\]
such that
\[
q_i\equiv1-p\pmod{\ell_i}.
\]

Conversely, if for every \(i\) there is a prime \(\ell_i\) such that
\[
\ell_i\mid p+q_i-1
\quad\text{and}\quad
\ell_i<p+q_i-1,
\]
then the state is terminal.

#### Proof
At a terminal state,
\[
N_i=p+q_i-1
\]
is composite and
\[
N_i\le2p-1<2p.
\]
It therefore has a prime divisor
\[
\ell_i\le\sqrt{N_i}<\sqrt{2p}.
\]
The divisibility condition is equivalent to
\[
q_i\equiv1-p\pmod{\ell_i}.
\]

The converse is immediate: every candidate has a proper prime divisor and hence is composite. ∎

This shows exactly what a dynamic Route 3 argument must rule out: the trajectory terms must not become covered by these moving residue classes. Equidistribution modulo any fixed modulus cannot suffice, because Theorem 5 can place all covering primes outside that modulus.

### 6. Ledger

**Proved lemmas**

- Extension is exactly the intersection condition \(Q_n\cap R(p)\ne\varnothing\).
- The lower bound \(C(Q_n,p)\ge |R(p)|-E(Q_n,p)\).
- The exact omission update formula.
- The exponential growth bound and \(n/\log q_n\) lower bound.
- The modular characterization of a terminal state.
- Existence of arbitrarily dense terminal seeds, equidistributed modulo any prescribed fixed modulus.

**Plausible but unproved claims needed by Route 3**

- A uniform Hardy–Littlewood lower bound for \(h=p-1\) and \(r\le p\).
- A trajectory-specific discrepancy estimate preventing \(Q_n\) from avoiding \(R(p)\).
- Subexponential trajectory growth \(\log q_n=o(n)\).
- An omission bound \(E(Q_n,p)=o(p/\log^2p)\).

**Dead ends**

- Positive density of \(Q_n\) among primes: refuted by Theorem 5.
- Density tending to one without a quantitative rate: refuted by Theorem 5.
- Equidistribution modulo finitely many fixed moduli: refuted by Theorem 5.
- Unrestricted prime-pair abundance alone: insufficient unless omissions or subset discrepancy are also controlled.
- Sieve survival as a substitute for primality: blocked by the parity problem.

## Self-Audit

1. **The dense-terminal-seed theorem uses the prime number theorem in arithmetic progressions rather than proving it from first principles.** This is a non-elementary input, but it is a standard unconditional theorem, applied only to a fixed modulus \(WM\). No uniformity in a growing modulus is used.

2. **The obstruction theorem concerns arbitrary initial seeds, not states generated after many recurrence steps.** Consequently it does not show that a particular natural trajectory has bad correlations. I believe the stated conclusion is nevertheless valid because arbitrary finite seeds are legal under the problem’s quantifiers; the theorem is used only to refute static density/equidistribution lemmas, not to claim universal termination.

3. **The conditional Hardy–Littlewood/discrepancy reductions do not advance past the central unproved correlation estimate.** Their implications are exact consequences of set identities and pigeonhole counting, but the hypotheses themselves are not claimed. This is precisely why the route is marked BLOCKED rather than PARTIAL or SOLVED.

## Computations To Verify

The following code simulates the recurrence and records proof-oriented factors for failed candidates.

```python
from sympy import isprime, factorint, primerange, primepi

def smallest_factor(N):
    return min(factorint(N))

def certified_step(Q):
    """
    Q must be a strictly increasing list of primes.
    Returns a certificate for the next step or terminality.
    """
    p = Q[-1]
    failed = []

    for i, q in enumerate(Q):
        N = p + q - 1
        if isprime(N):
            return {
                "terminal": False,
                "selected_index_0_based": i,
                "selected_q": q,
                "next_prime": N,
                "earlier_composite_certificates": failed,
            }
        failed.append({
            "index_0_based": i,
            "q": q,
            "candidate": N,
            "factor": smallest_factor(N),
        })

    return {
        "terminal": True,
        "terminal_prime": p,
        "composite_certificates": failed,
    }

def simulate(seed, steps):
    Q = list(seed)
    assert Q == sorted(set(Q))
    assert all(isprime(q) for q in Q)

    records = []
    for _ in range(steps):
        cert = certified_step(Q)
        records.append(cert)
        if cert["terminal"]:
            break
        Q.append(cert["next_prime"])
    return Q, records
```

Route 3 statistics can be computed as follows.

```python
def route3_statistics(Q):
    p = Q[-1]
    ambient = list(primerange(2, p + 1))
    h = p - 1

    R = [r for r in ambient if isprime(r + h)]
    C = [q for q in Q if isprime(q + h)]

    E = len(ambient) - len(Q)
    alpha = len(Q) / len(ambient)
    discrepancy = len(C) - alpha * len(R)

    return {
        "p": p,
        "n": len(Q),
        "pi_p": len(ambient),
        "omissions_E": E,
        "global_pair_endpoints_R": len(R),
        "trajectory_pair_endpoints_C": len(C),
        "pigeonhole_margin_R_minus_E": len(R) - E,
        "alpha": alpha,
        "discrepancy": discrepancy,
        "n_over_log_p": len(Q) / __import__("math").log(p),
    }
```

The dense terminal construction can be checked explicitly.

```python
from math import gcd
from itertools import count
from sympy.ntheory.modular import crt

def dense_terminal_seed(W, S, distinguished_L, min_p=1000):
    """
    S: finite list of distinct odd primes, all coprime to W.
    distinguished_L must belong to S.
    """
    assert distinguished_L in S
    assert len(S) == len(set(S))
    assert all(isprime(l) and l % 2 == 1 and gcd(l, W) == 1 for l in S)

    c = {}
    for l in S:
        if l == distinguished_L:
            c[l] = pow(2, -1, l)
        else:
            c[l] = 2 % l

    mods = [W] + list(S)
    residues = [1 % W] + [c[l] for l in S]
    A, period = crt(mods, residues)
    A, period = int(A), int(period)
    A %= period

    k0 = max(0, (max(min_p, max(S) + 1) - A + period - 1) // period)
    for k in count(k0):
        p = A + k * period
        if isprime(p):
            break

    b = {l: (1 - c[l]) % l for l in S}

    Q = [
        r for r in primerange(2, p + 1)
        if any(r % l == b[l] for l in S)
    ]

    assert Q[-1] == p

    covers = []
    for q in Q:
        N = p + q - 1
        l = next(l for l in S if N % l == 0)
        assert 1 < l < N
        covers.append((q, N, l))

    assert all(not isprime(p + q - 1) for q in Q)

    reduced_classes = [a for a in range(W) if gcd(a, W) == 1] if W > 1 else [0]
    class_counts = {
        a: sum(1 for q in Q if q % W == a) if W > 1 else len(Q)
        for a in reduced_classes
    }

    return {
        "p": p,
        "Q": Q,
        "density": len(Q) / int(primepi(p)),
        "class_counts_mod_W": class_counts,
        "cover_certificates": covers,
    }

# Simple terminal example:
assert certified_step([2, 5, 11])["terminal"]

# A denser modular example:
example = dense_terminal_seed(
    W=1,
    S=[3, 5, 7],
    distinguished_L=3,
    min_p=100
)
print(example["p"], example["density"])
```

For the natural seed \((3,5)\), the most informative numerical experiment is to record, at every state:

```python
Q, records = simulate([3, 5], 10000)

for cutoff in [10, 100, 1000, len(Q)]:
    if cutoff <= len(Q):
        print(route3_statistics(Q[:cutoff]))
```

In particular, one should monitor whether:

- \(E(Q_n,q_n)\) is smaller or larger than \(|R(q_n)|\);
- the discrepancy \(D(Q_n,q_n)\) is consistently of smaller order than
  \(\alpha_n|R(q_n)|\);
- \(n/\log q_n\) grows, remains bounded, or decreases toward its exponential-growth lower scale;
- terminal or near-terminal states admit coverings by unusually small prime factors.

For proof-quality finite output, `isprime` and `factorint` should be replaced or supplemented by ECPP/APR-CL primality certificates and explicit nontrivial factors.

## Route Diagnosis

Route 3 separates cleanly into an unrestricted uniform prime-pair theorem and a trajectory-correlation theorem. Neither is presently available. Even proving
\[
R(p)\ne\varnothing
\]
for every sufficiently large prime \(p\) would be a strong growing-shift, bounded-endpoint prime-difference result beyond current sieve methods. Granting that conjectural statement still does not force \(Q_n\cap R(p)\ne\varnothing\). Theorem 5 shows that legal prime sets can be terminal despite density tending to one and despite equidistribution modulo any prescribed finite collection of moduli.

The precise block is therefore a dynamic, parity-sensitive discrepancy estimate for the actual recurrence:
\[
|Q_n\cap R(q_n)|
\approx
\frac{n}{\pi(q_n)}|R(q_n)|.
\]
Proving merely ordinary density or small-modulus equidistribution cannot deliver it. Proving this estimate directly would already imply the desired extension at every stage and is of comparable strength to the original problem.

A fresh attempt should probably not pursue static trajectory density. The more promising alternatives are:

1. seek a Route 4 finite-state seed invariant giving a designated prime candidate for algebraic reasons;
2. investigate a genuinely dynamic anti-covering property for the residues \(q_i\bmod \ell\), with moduli growing with \(q_n\);
3. computationally test whether the natural trajectory has subexponential growth and whether its discrepancy against \(R(q_n)\) is substantially better than worst case, before attempting any transference theorem.