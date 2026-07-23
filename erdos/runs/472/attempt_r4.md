STATUS: BLOCKED

## Result

Route 4 yields substantial but finite engineering and a strong obstruction to the most natural self-replenishing schemes. Unconditionally, using the Green–Tao–Ziegler theorem on finite systems of affine-linear forms in primes, one can construct arbitrarily long deterministic trajectories from a two-prime seed in which every newly generated term becomes the controller at the next step. However, no fixed seed can follow that Fibonacci-type schedule forever: more generally, every fixed-dimensional periodic linear block-replenishment scheme is eventually forced to produce a composite term by a finite-field recurrence argument. Any infinite trajectory must also use infinitely many distinct controller primes. Thus an affirmative construction would have to use a genuinely aperiodic, unboundedly renewing mechanism; proving primality along such a fixed infinite schedule remains essentially as hard as the original problem.

## Complete Argument

Write
\[
a_n=q_n-1.
\]
Then every generated step has the form
\[
a_{n+1}=a_n+a_{j_n},
\qquad a_k+1\in\mathbb P.
\]

### 1. A finite reservoir cannot support an infinite trajectory

**Lemma 1.** In any infinite trajectory, infinitely many distinct indices are selected. Equivalently, the selected controller values \(q_{j_n}\) are unbounded.

**Proof.** Suppose instead that all controllers selected from some stage onward satisfy
\[
q_{j_n}\le R.
\]
Then
\[
q_{n+1}-q_n=q_{j_n}-1\le R-1,
\]
so for some constant \(C\),
\[
q_n\le C+(R-1)n.
\]
On the other hand, \(q_1<\cdots<q_n\) are \(n\) distinct primes, hence
\[
q_n\ge p_n,
\]
where \(p_n\) is the \(n\)-th prime. The classical estimate \(p_n/n\to\infty\), already following from Chebyshev’s bound \(\pi(x)\ll x/\log x\), contradicts \(q_n=O(n)\). ∎

A quantitative version is immediate. If
\[
R_n=\max_{m\le k<n}(q_{j_k}-1),
\]
then
\[
R_n\ge \frac{q_n-q_m}{n-m}\ge \frac{p_n-q_m}{n-m},
\]
so necessarily \(R_n\to\infty\).

Thus no genuinely finite collection of reservoir primes can work forever.

---

### 2. One fixed controller has a modular lifetime bound

**Lemma 2.** Let \(r\) be a prime already in the sequence. It cannot be selected at \(r\) consecutive stages.

**Proof.** If the current term is \(p\) and the same controller \(r\) is used repeatedly, then the successive proposed outputs are
\[
p+k(r-1),\qquad k=1,2,\ldots.
\]
Modulo \(r\),
\[
p+k(r-1)\equiv p-k\pmod r.
\]
Among \(k=1,\ldots,r\), there is a \(k\) for which \(k\equiv p\pmod r\). The corresponding output is divisible by \(r\). It is strictly larger than \(r\), and hence composite. ∎

This already rules out an infinite block supported by one controller, even if one had somehow arranged a long prime arithmetic progression of difference \(r-1\).

---

### 3. Arbitrarily long exact self-replenishing trajectories exist

The following result shows that finite seed engineering is extremely flexible. It also explains why long computations or arbitrarily long examples are not close to an infinitude proof.

I use the following established consequence of the Green–Tao–Ziegler affine-linear forms theorem.

> **Affine prime-values theorem.**  
> Let \(\psi_1,\ldots,\psi_t:\mathbb Z^d\to\mathbb Z\) be affine-linear forms whose nonconstant linear parts are pairwise nonproportional over \(\mathbb Q\). Suppose that for every prime \(\ell\), there is an \(x\in(\mathbb Z/\ell\mathbb Z)^d\) for which
> \[
> \psi_1(x)\cdots\psi_t(x)\not\equiv0\pmod\ell.
> \]
> Then, in every fixed positive convex region on which all forms are positive, sufficiently large dilates contain integer points at which all the \(\psi_i\) are prime.

**Theorem 3.** For every \(K\ge2\), there is a two-prime seed \(q_1<q_2\) whose deterministic trajectory has at least \(K\) terms and satisfies
\[
a_{n+1}=a_n+a_{n-1}
\qquad(2\le n<K).
\]
Equivalently,
\[
j_n=n-1
\qquad(2\le n<K).
\]
Thus every generated term is used as the controller at the following step.

**Proof.**

Define formal coefficient vectors
\[
V_1=(1,0),\qquad V_2=(0,1),\qquad
V_{n+1}=V_n+V_{n-1}.
\]
For variables \(d,b\), put
\[
a_n=V_n\cdot(d,b).
\]
Thus
\[
a_1=d,\quad a_2=b,\quad a_{n+1}=a_n+a_{n-1}.
\]
Let
\[
L_n(d,b)=a_n+1=V_n\cdot(d,b)+1.
\]
We shall arrange that all \(L_1,\ldots,L_K\) are prime, while for every stage \(n\) and every undesired earlier index \(i<n-1\),
\[
C_{n,i}(d,b)=a_n+a_i+1
=(V_n+V_i)\cdot(d,b)+1
\]
is composite.

#### Step 1: No undesired candidate form equals an intended prime form

For \(n\ge2\),
\[
V_n=(F_{n-2},F_{n-1}),
\]
where \(F_0=0,F_1=1\), apart from the separately defined \(V_1=(1,0)\).

The vectors \(V_1,\ldots,V_K\) are pairwise nonproportional. Indeed, each is primitive, they are distinct, and all have nonnegative coordinates.

We also claim that
\[
V_n+V_i\ne V_k
\]
whenever \(i\le n-2\). For \(n\ge4\), the sum of the two coordinates of \(V_s\) is \(F_s\), and
\[
F_n<F_n+F_i<F_n+F_{n-1}=F_{n+1}.
\]
Therefore \(V_n+V_i\) cannot be another \(V_k\). The only exceptional small case is \(n=3,i=1\), where
\[
V_3+V_1=(2,1)\ne(1,2)=V_4.
\]

#### Step 2: Force every undesired candidate to be composite

For each pair
\[
3\le n<K,\qquad 1\le i\le n-2,
\]
choose a distinct sufficiently large odd prime \(\ell_{n,i}>K\).

Choose it also so that, modulo \(\ell_{n,i}\),
\[
V_n+V_i\ne0
\quad\text{and}\quad
V_n+V_i\ne V_k
\quad(1\le k\le K).
\]
Only finitely many primes are excluded because the corresponding integer vectors are nonzero.

Over \(\mathbb F_{\ell_{n,i}}\), the equation
\[
(V_n+V_i)\cdot(d,b)+1=0
\]
defines a line containing \(\ell_{n,i}\) points. For each \(k\), the forbidden equation
\[
V_k\cdot(d,b)+1=0
\]
removes at most one point from this line: it cannot coincide with the entire line because
\[
V_n+V_i\ne V_k\pmod{\ell_{n,i}}.
\]
Since \(\ell_{n,i}>K\), there is a residue pair
\[
(d_{n,i},b_{n,i})\pmod{\ell_{n,i}}
\]
such that
\[
C_{n,i}(d_{n,i},b_{n,i})\equiv0\pmod{\ell_{n,i}}
\]
but
\[
L_k(d_{n,i},b_{n,i})\not\equiv0\pmod{\ell_{n,i}}
\qquad(1\le k\le K).
\]

Also impose
\[
d\equiv b\equiv0\pmod2.
\]
By the Chinese remainder theorem, there is one residue class
\[
(d,b)\equiv(d_0,b_0)\pmod W,
\qquad
W=2\prod_{n,i}\ell_{n,i},
\]
satisfying all these conditions simultaneously.

Write
\[
d=d_0+WD,\qquad b=b_0+WB.
\]

#### Step 3: Make all intended forms prime

Consider the affine forms in \(D,B\)
\[
\widetilde L_k(D,B)
  =V_k\cdot(d_0+WD,b_0+WB)+1.
\]
Their linear parts are \(W V_k\), hence are pairwise nonproportional.

They have no local obstruction. If \(\ell\mid W\), all \(\widetilde L_k\) are nonzero modulo \(\ell\) by construction. If \(\ell\nmid W\), choose \(D,B\pmod\ell\) so that
\[
d_0+WD\equiv b_0+WB\equiv0\pmod\ell.
\]
Then every \(\widetilde L_k\equiv1\pmod\ell\).

The affine prime-values theorem therefore gives arbitrarily large \(D,B\), in a region with \(0<d<b\), such that
\[
L_1(d,b),\ldots,L_K(d,b)
\]
are all prime. We may make \(d,b\) sufficiently large that every forced divisor \(\ell_{n,i}\) is strictly smaller than its candidate \(C_{n,i}(d,b)\). Hence each undesired candidate is genuinely composite.

Set
\[
q_n=L_n(d,b)=a_n+1.
\]
Then \(q_1<q_2\), and the recurrence makes the intended choices. At stage \(n\), every candidate indexed by \(i<n-1\) is composite, while
\[
q_n+q_{n-1}-1=a_n+a_{n-1}+1=a_{n+1}+1=q_{n+1}
\]
is prime. Thus
\[
j_n=n-1.
\]
This holds through the production of \(q_K\). ∎

This is a genuine self-replenishing finite construction: the controller at stage \(n\) is the term generated at stage \(n-2\).

---

### 4. Fixed linear block replenishment is impossible forever

The Fibonacci construction above cannot be made infinite for one fixed seed. This is an instance of a more general obstruction.

**Theorem 4 (fixed-matrix modular obstruction).**  
Let \(M\in\operatorname{Mat}_D(\mathbb Z)\), let
\[
X_k=M^kX_0\in\mathbb Z^D,
\]
and fix a coordinate \(t\). It is impossible that
\[
(X_k)_t+1
\]
is prime and strictly increasing in \(k\) for every \(k\ge0\).

**Proof.** Assume otherwise and choose \(k\ge D\). Put
\[
p=(X_k)_t+1.
\]
Reduce modulo \(p\), and let
\[
W_p=\operatorname{im}(M^D)\subseteq\mathbb F_p^D.
\]

The descending chain
\[
\mathbb F_p^D\supseteq\operatorname{im}M
 \supseteq\operatorname{im}M^2\supseteq\cdots
\]
must stabilize by exponent \(D\). Consequently,
\[
\operatorname{im}M^D=\operatorname{im}M^{D+1}.
\]
Thus \(M\) maps \(W_p\) surjectively to itself and hence bijectively to itself.

Since
\[
X_k=M^kX_0\in W_p,
\]
the orbit of \(X_k\) under \(M\) is periodic from its first point. Therefore, for some \(s\ge1\),
\[
M^sX_k\equiv X_k\pmod p.
\]
In coordinate \(t\),
\[
(X_{k+s})_t+1\equiv (X_k)_t+1\equiv0\pmod p.
\]
But strict increase gives
\[
(X_{k+s})_t+1>p.
\]
Hence \((X_{k+s})_t+1\) is composite, a contradiction. ∎

This does not require \(M\) to be invertible over \(\mathbb Z\); passage to the stabilized image handles singular matrices.

**Corollary 5.** No fixed-dimensional block scheme
\[
X_{k+1}=MX_k
\]
can replenish blocks of prime-shifted additive states forever if corresponding coordinates represent chronologically later terms.

**Corollary 6.** In an infinite Ulam trajectory, the selected lag
\[
c_n=n-j_n
\]
cannot be eventually periodic.

**Proof.** If \(c_n\) is eventually periodic, it is bounded, say \(0\le c_n\le L\). Define
\[
X_n=(a_{n-L},a_{n-L+1},\ldots,a_n)^T.
\]
For each possible lag \(c\), there is an integer matrix \(M_c\) satisfying
\[
X_{n+1}=M_cX_n
\]
when \(c_n=c\). Over one period \(T\), the same product matrix \(P\) is applied, so at a fixed phase
\[
X_{N+(k+1)T}=PX_{N+kT}.
\]
Each coordinate corresponds to a strictly later \(a\)-term as \(k\) increases, and every coordinate plus one is prime. This contradicts Theorem 4. ∎

In particular, the following all fail:

- perpetual use of the self-candidate \(2q_n-1\);
- perpetual fixed-lag recurrences;
- periodic rotation among finitely many relative controller positions;
- a fixed square block transformation repeated indefinitely.

---

### 5. Precise block

The finite construction in Theorem 3 uses congruences depending on the desired length \(K\), and the resulting seed also depends on \(K\). Theorem 4 proves that the limiting formal Fibonacci schedule cannot work for any fixed seed. Thus no compactness argument can retain those finite realizations as one standard integer seed.

A surviving Route 4 construction must simultaneously satisfy all of the following:

1. use infinitely many distinct controller terms, by Lemma 1;
2. avoid any eventually periodic bounded-lag schedule, by Corollary 6;
3. avoid every fixed-dimensional periodic block transformation, by Theorem 4;
4. prove primality at every stage for one fixed seed, rather than invoke a finite affine-prime theorem whose parameters change with the horizon;
5. control the deterministic minimality condition, or prove an invariant robust under every earlier successful candidate.

I do not know an unconditional theorem capable of the fourth step. It amounts to proving prime values along an infinite adaptive family of linear forms at one fixed integer parameter, which is outside the scope of Green–Tao–Ziegler and current sieve methods.

## Self-Audit

1. **Theorem 3 invokes Green–Tao–Ziegler as a black box.**  
   I have not reproduced that very deep theorem. The application is within its standard finite-complexity scope: there are finitely many affine forms in two variables, their linear parts are pairwise nonproportional, and the local conditions are checked explicitly. This is an unconditional established theorem, not a conjectural prime-tuple assumption.

2. **The fixed-matrix obstruction does not rule out every interpretation of “finite-state invariant.”**  
   It rules out exact periodic linear block evolution and eventually periodic lag schedules. A finite collection of matrices chosen by an arithmetic, nonperiodic rule is not covered. I believe the stated result because the finite-field proof is complete, but its scope must not be enlarged.

3. **The diagnosis of the remaining problem is not an impossibility theorem.**  
   A genuinely aperiodic robust invariant could still exist. The analysis only proves that the obvious fixed-controller, Fibonacci, periodic-lag, and repeated block schemes fail. I therefore make no claim of solving or disproving the original problem.

## Computations To Verify

The following code constructs the CRT conditions used in Theorem 3 and searches for an actual prime realization.

```python
from math import prod
from sympy import nextprime, isprime, factorint
from sympy.ntheory.modular import crt

def fib_vectors(K):
    # 1-based: V[1]=(1,0), V[2]=(0,1)
    V = [None, (1, 0), (0, 1)]
    while len(V) <= K:
        x1, y1 = V[-1]
        x2, y2 = V[-2]
        V.append((x1 + x2, y1 + y2))
    return V

def dot(v, x):
    return v[0]*x[0] + v[1]*x[1]

def build_crt_conditions(K):
    V = fib_vectors(K)
    mods = [2]
    dres = [0]
    bres = [0]
    used = {2}
    ell_cursor = K + 1

    # Bad candidates at stage n are i <= n-2.
    for n in range(3, K):
        for i in range(1, n-1):
            Wvec = (V[n][0] + V[i][0],
                    V[n][1] + V[i][1])

            ell = nextprime(ell_cursor)
            while True:
                if ell in used:
                    ell = nextprime(ell)
                    continue

                good = None
                for d in range(ell):
                    for b in range(ell):
                        # Force this bad candidate divisible by ell.
                        if (dot(Wvec, (d, b)) + 1) % ell != 0:
                            continue
                        # Preserve every intended q_k modulo ell.
                        if all((dot(V[k], (d, b)) + 1) % ell != 0
                               for k in range(1, K+1)):
                            good = (d, b)
                            break
                    if good is not None:
                        break

                if good is not None:
                    break
                ell = nextprime(ell)

            used.add(ell)
            ell_cursor = ell
            mods.append(ell)
            dres.append(good[0])
            bres.append(good[1])

    d0 = int(crt(mods, dres)[0])
    b0 = int(crt(mods, bres)[0])
    modulus = prod(mods)
    return V, d0, b0, modulus, mods

def search_prime_realization(K, search_bound=100000):
    V, d0, b0, W, mods = build_crt_conditions(K)

    # Systematic search; GTZ proves that some sufficiently large pair exists,
    # but does not provide a practical small bound.
    for D in range(1, search_bound):
        d = d0 + W*D
        for B in range(4*D, 5*D + 1):
            b = b0 + W*B
            if not (0 < d < b):
                continue

            Q = [dot(V[k], (d, b)) + 1 for k in range(1, K+1)]
            if all(isprime(q) for q in Q):
                return d, b, Q, mods
    return None
```

Exact simulation and minimality verification:

```python
from sympy import isprime, factorint

def simulate(seed, steps):
    Q = list(seed)
    record = []

    for _ in range(steps):
        p = Q[-1]
        selected = None
        candidates = []

        for i, r in enumerate(Q):
            N = p + r - 1
            candidates.append(N)
            if isprime(N):
                selected = i
                break

        if selected is None:
            return Q, record, ("terminal", [
                (N, factorint(N)) for N in candidates
            ])

        # Factors of all candidates preceding the selected one.
        rejected = [
            (candidates[i], factorint(candidates[i]))
            for i in range(selected)
        ]
        Q.append(candidates[selected])
        record.append({
            "selected_index_1_based": selected + 1,
            "new_prime": candidates[selected],
            "earlier_composite_factors": rejected
        })

    return Q, record, None

def verify_fibonacci_prefix(Q):
    # For a two-term seed, desired choice at state n is j_n=n-1.
    generated, record, terminal = simulate(Q[:2], len(Q)-2)
    assert terminal is None
    assert generated == Q

    for current_length, rec in enumerate(record, start=2):
        expected_zero_based = current_length - 2
        assert rec["selected_index_1_based"] == expected_zero_based + 1

    return True
```

Finite-field verification of Theorem 4:

```python
from sympy import Matrix, isprime

def matrix_obstruction(M, X0, coordinate=0):
    M = Matrix(M)
    X0 = Matrix(X0)
    D = M.rows
    assert M.cols == D and len(X0) == D

    Xk = (M**D) * X0
    p = int(Xk[coordinate] + 1)

    if not isprime(p):
        return {
            "already_composite_at_block": D,
            "value": p
        }

    y = tuple(int(v % p) for v in Xk)
    z = y

    def matvec_mod(v):
        out = []
        for i in range(D):
            out.append(sum(int(M[i, j]) * v[j]
                           for j in range(D)) % p)
        return tuple(out)

    # The orbit lies in a set of size at most p**D.
    for s in range(1, p**D + 1):
        z = matvec_mod(z)
        if z == y:
            Xfuture = (M**s) * Xk
            N = int(Xfuture[coordinate] + 1)
            assert N % p == 0
            return {
                "prime_divisor": p,
                "return_time": s,
                "future_value": N,
                "composite_if_larger": N > p
            }

    raise AssertionError("Finite-field return was not found")
```

For the Fibonacci schedule, use

```python
M = [[0, 1],
     [1, 1]]
```

with \(X_0=(a_1,a_2)^T\).

## Route Diagnosis

**Proved lemmas**

- An infinite trajectory must select infinitely many distinct controller primes.
- A fixed controller \(r\) cannot be used for \(r\) consecutive stages.
- Arbitrarily long exact self-replenishing Fibonacci-style trajectories exist from two-prime seeds, unconditionally via Green–Tao–Ziegler and CRT control of minimality.
- No fixed-matrix block scheme can keep a corresponding coordinate plus one prime forever.
- Consequently, no eventually periodic selected-lag schedule can describe an infinite trajectory.

**Plausible but unproved**

- Every bounded-lag switching schedule may terminate even without eventual periodicity. The fixed-matrix proof does not establish this because arbitrary switching products need not return the initial state modulo an earlier prime.
- A modular obstruction may exist for all products from the finite family of lag matrices. Establishing the needed return uniformly for every switching word is currently missing.

**Dead ends**

- **One fixed reservoir prime:** fails modulo that prime within \(r\) consecutive uses.
- **A finite reservoir:** contradicts the zero density of the primes.
- **Self-candidate or Fibonacci iteration forever:** killed by the fixed-matrix modular return.
- **Periodic block rotation:** also killed by the fixed-matrix theorem.
- **Compactness from arbitrarily long engineered seeds:** the congruence moduli and seed parameters depend on the horizon; Theorem 4 explicitly prevents the formal Fibonacci limit from corresponding to one infinite prime trajectory.

A fresh Route 4 attempt should therefore target a robust, genuinely aperiodic replenishing invariant rather than an exact repeating schedule. Computationally, the most useful next experiment is to search over aperiodic bounded-lag words, use CRT to force their deterministic finite prefixes, and test whether every such word develops a universal modular return obstruction. Without such a new mechanism, Route 4 remains blocked at infinite prime production for one fixed seed.