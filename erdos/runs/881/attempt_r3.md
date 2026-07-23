STATUS: BLOCKED

## Result

Route 3 yields a sharp gap-count criterion and an “absorption” mechanism that completely proves the desired conclusion whenever \(A\) contains a tail of an arithmetic progression. In particular, the problem is affirmative for every eventually periodic basis and for the explicit deletion-minimal bases \(A_k=k\mathbb N_0\cup\{1\}\). The general case remains blocked: neither the hypothesis nor numerical sparsity of the deletion currently gives sufficient control over the number or correlation of gaps of \(k(A\setminus B)\). The missing step is precisely to construct an infinite \(B\) for which those gaps cannot contain reflected copies \(n-(A\setminus B)\).

## Complete Argument

### 1. The exact gap-set criterion

For \(C\subseteq\mathbb N_0\), write
\[
G_k(C)=\mathbb N_0\setminus kC
\]
and, for any \(X\subseteq\mathbb N_0\),
\[
X(x)=|X\cap[0,x]|.
\]

#### Lemma 1

For every \(n\ge 0\),
\[
n\notin (k+1)C
\quad\Longleftrightarrow\quad
n-c\in G_k(C)\quad\text{for every }c\in C\cap[0,n].
\]

Consequently,
\[
n\notin (k+1)C\quad\Longrightarrow\quad
G_k(C)(n)\ge C(n).
\]

In particular, if
\[
G_k(C)(n)<C(n)
\]
for every sufficiently large \(n\), then \((k+1)C\) is cofinite.

#### Proof

Since
\[
(k+1)C=C+kC,
\]
we have \(n\in(k+1)C\) exactly when there is \(c\in C\), necessarily \(c\le n\), such that \(n-c\in kC\). Negating this gives the equivalence.

If \(n\notin(k+1)C\), the injective map
\[
c\longmapsto n-c
\]
sends \(C\cap[0,n]\) into \(G_k(C)\cap[0,n]\). Hence
\[
G_k(C)(n)\ge C(n).
\]
The final assertion follows immediately. ∎

This is the basic Route 3 reformulation: a failure of the extra summand forces the \(k\)-gap set to contain the entire reflected copy
\[
n-(C\cap[0,n]).
\]

---

### 2. A general but usually crude carrier bound for deletion-created gaps

Suppose \(kA\) contains every integer at least \(N_0\), let \(B\subseteq A\), and put \(C=A\setminus B\).

#### Lemma 2

For \(k\ge2\),
\[
G_k(C)\cap[N_0,\infty)
\subseteq B+(k-1)A.
\]

Therefore, if for every sufficiently large \(n\),
\[
N_0+\bigl|(B+(k-1)A)\cap[0,n]\bigr|<C(n),
\]
then \((k+1)C\) is cofinite.

#### Proof

Let \(m\ge N_0\) and suppose \(m\notin kC\). Since \(m\in kA\), choose
\[
m=a_1+\cdots+a_k,\qquad a_i\in A.
\]
Not all \(a_i\) can belong to \(C\), so some \(a_i\in B\). Thus
\[
m\in B+(k-1)A.
\]

There are at most \(N_0\) gaps below \(N_0\), so
\[
G_k(C)(n)
\le N_0+\bigl|(B+(k-1)A)\cap[0,n]\bigr|.
\]
The stated inequality and Lemma 1 then imply \(n\in(k+1)C\) for every sufficiently large \(n\). ∎

This bound is rigorously valid but generally too weak. A single translate \(b+(k-1)A\) can be much larger than \(A\), even though only a tiny part of that translate consists of actual gaps.

---

### 3. An absorption lemma exploiting the one extra summand

The following criterion is more effective than the raw carrier bound.

For \(r\ge1\), \(rB\) denotes the exact \(r\)-fold sumset, with repetitions allowed.

#### Lemma 3: Absorption criterion

Suppose \(kA\) is cofinite. Let \(B\subseteq A\), put \(C=A\setminus B\), and suppose there is an element \(a\in C\) such that
\[
a+rB\subseteq (r+1)C
\qquad (1\le r\le k).
\]
Then
\[
(k+1)C
\]
is cofinite.

#### Proof

Let \(N_0\) be such that every \(n\ge N_0\) belongs to \(kA\). Fix \(n\ge N_0\) and choose
\[
n=x_1+\cdots+x_k,\qquad x_i\in A.
\]

Let \(r\) be the number of occurrences among \(x_1,\dots,x_k\) that belong to \(B\), counting multiplicity.

If \(r=0\), then all \(x_i\in C\), and
\[
n=a+x_1+\cdots+x_k\in(k+1)C.
\]

Suppose \(r\ge1\). Write \(s\) for the sum of the \(r\) deleted occurrences. Then \(s\in rB\), so by hypothesis
\[
a+s\in(r+1)C.
\]
The remaining \(k-r\) original summands belong to \(C\). Replacing \(a+s\) by its \(r+1\) retained summands gives a representation of \(n\) using
\[
(r+1)+(k-r)=k+1
\]
elements of \(C\). Thus \(n\in(k+1)C\).

This holds for all \(n\ge N_0\). ∎

The key point is that all deleted summands in a \(k\)-representation are absorbed simultaneously together with one retained anchor. This avoids paying one extra summand for each deleted element.

---

### 4. A sparse subset of an arithmetic progression is absorbable

We now prove a substantial affirmative class.

#### Lemma 4

Fix \(T\ge0\), and let
\[
E_T=\{t\ge T:t\text{ is not a power of }2\}.
\]
Then \(2E_T\) is cofinite. Consequently, \(hE_T\) is cofinite for every \(h\ge2\).

#### Proof

Let \(U\) be large. Consider integers
\[
x\in I_U=
\left[\left\lceil\frac U3\right\rceil,
      \left\lfloor\frac{2U}3\right\rfloor\right].
\]
For sufficiently large \(U\), both \(x\) and \(U-x\) are at least \(T\).

There are at most \(1+\lfloor\log_2U\rfloor\) powers of two in \([0,U]\). Hence at most that many \(x\in I_U\) are forbidden because \(x\) is a power of two, and at most the same number are forbidden because \(U-x\) is a power of two. Since
\[
|I_U|\ge \frac U3-2,
\]
for sufficiently large \(U\) there is an \(x\in I_U\) for which neither \(x\) nor \(U-x\) is a power of two. Thus
\[
U=x+(U-x)\in2E_T.
\]
Therefore \(2E_T\) is cofinite.

Choose any fixed \(e_0\in E_T\). If \(2E_T\) contains every integer at least \(L\), then for \(h\ge2\) and
\[
U\ge L+(h-2)e_0,
\]
we have
\[
U-(h-2)e_0\in2E_T,
\]
and hence \(U\in hE_T\). ∎

#### Theorem 5: Arithmetic-progression reservoir theorem

Let \(A\subseteq\mathbb N_0\) satisfy that \(kA\) is cofinite. Suppose that for some integers \(q\ge1\), \(d\ge0\), and \(T\ge0\),
\[
P=\{d+qt:t\ge T\}\subseteq A.
\]
Then there is an infinite \(B\subseteq P\) such that
\[
(k+1)(A\setminus B)
\]
is cofinite.

If, in addition, \(A\) has exact order \(k\) and satisfies the infinite-deletion minimality premise, then \(A\setminus B\) has exact order \(k+1\).

#### Proof

By Lemma 4, for every \(h=2,\dots,k+1\), there is \(L_h\) such that
\[
[L_h,\infty)\subseteq hE_T.
\]
Let
\[
L=\max_{2\le h\le k+1}L_h.
\]
Choose \(t_0\in E_T\), and put
\[
a=d+qt_0\in P.
\]

Choose \(J\) sufficiently large that
\[
2^J\ge T
\quad\text{and}\quad
t_0+2^J\ge L.
\]
Define
\[
B=\{d+q2^j:j\ge J\}.
\]
Then \(B\subseteq P\subseteq A\), \(B\) is infinite, and \(a\notin B\).

Put \(C=A\setminus B\). We verify the absorption hypothesis of Lemma 3.

Fix \(1\le r\le k\), and take any \(s\in rB\). Counting repetitions, write
\[
s=\sum_{i=1}^r(d+q2^{j_i})
=rd+q\sum_{i=1}^r2^{j_i},
\qquad j_i\ge J.
\]
Thus
\[
a+s
=(r+1)d+qU,
\qquad
U=t_0+\sum_{i=1}^r2^{j_i}.
\]
Since \(r\ge1\),
\[
U\ge t_0+2^J\ge L\ge L_{r+1}.
\]
Therefore \(U\in(r+1)E_T\). Write
\[
U=u_0+\cdots+u_r,\qquad u_i\in E_T.
\]
Then
\[
a+s
=\sum_{i=0}^r(d+qu_i).
\]
Each \(d+qu_i\) belongs to \(P\), and none belongs to \(B\), because \(u_i\) is not a power of two. Hence
\[
a+s\in(r+1)(P\setminus B)\subseteq(r+1)C.
\]
Thus
\[
a+rB\subseteq(r+1)C
\]
for every \(1\le r\le k\).

Lemma 3 now gives that \((k+1)C\) is cofinite.

Finally, suppose \(\operatorname{ord}(A)=k\) and the deletion-minimality premise holds. Since \(B\) is infinite, \(kC\) is not cofinite. Since \((k+1)C\) is cofinite, \(C\) has exact order \(k+1\). ∎

#### Corollary 6

The problem has an affirmative answer for every eventually periodic \(A\).

Indeed, every infinite eventually periodic set contains a tail of an arithmetic progression belonging to one of its eventual residue classes.

More generally, eventual periodicity of all of \(A\) is unnecessary: it suffices that \(A\) contain one complete arithmetic-progression tail.

---

### 5. A nontrivial family satisfying the full premise

For every \(k\ge2\), define
\[
A_k=k\mathbb N_0\cup\{1\}.
\]

#### Proposition 7

For every \(k\ge2\):

1. \(\operatorname{ord}(A_k)=k\);
2. every infinite \(B\subseteq A_k\) destroys the \(k\)-basis property;
3. there is an infinite \(B_0\subseteq A_k\) such that
   \[
   \operatorname{ord}(A_k\setminus B_0)=k+1.
   \]

#### Proof

Any \(h\)-term sum from \(A_k\) contains some number \(j\), \(0\le j\le h\), of occurrences of \(1\), with all other summands divisible by \(k\).

For \(h=k\), every sufficiently large \(n\equiv r\pmod k\), \(0\le r\le k-1\), is represented by taking \(r\) copies of \(1\), one multiple \(n-r\) of \(k\), and enough zero summands to make exactly \(k\) terms. Hence \(kA_k\) is cofinite.

If \(h<k\), every \(h\)-term sum congruent to \(h\pmod k\) must use exactly \(h\) copies of \(1\), and is therefore equal to \(h\). Thus all sufficiently large integers congruent to \(h\pmod k\) are absent from \(hA_k\). Therefore
\[
\operatorname{ord}(A_k)=k.
\]

Now let \(B\subseteq A_k\) be infinite and put \(C=A_k\setminus B\). Since \(1\) is the only element of \(A_k\) not divisible by \(k\), the set \(B\) contains arbitrarily large multiples \(kt\).

If \(1\notin C\), then every element of \(kC\) is divisible by \(k\), so \(kC\) is not cofinite.

If \(1\in C\), take \(kt\in B\). Consider
\[
n=kt+(k-1).
\]
In a \(k\)-term representation of \(n\) by elements of \(A_k\), the number \(j\) of occurrences of \(1\) must satisfy
\[
j\equiv k-1\pmod k,\qquad 0\le j\le k.
\]
Thus \(j=k-1\), and the remaining single summand must be exactly \(kt\). Since \(kt\) was deleted, \(n\notin kC\). Arbitrarily large deleted multiples give arbitrarily large gaps. This proves the premise.

Finally, choose \(J\ge1\) and let
\[
B_0=\{k2^j:j\ge J\}.
\]
The progression \(k\mathbb N_0\) is contained in \(A_k\), so Theorem 5 gives
\[
(k+1)(A_k\setminus B_0)
\]
cofinite. The premise shows that its \(k\)-fold sumset is not cofinite, so its exact order is \(k+1\). ∎

---

### 6. The gap anatomy in the model family

Let
\[
D=\mathbb N_0\setminus\{2^j:j\ge J\},
\qquad
C=\{1\}\cup kD.
\]
For sufficiently large \(n\equiv r\pmod k\):

- if \(r=k-1\), a \(k\)-term representation must use \(k-1\) copies of \(1\) and one multiple \(kt\); hence
  \[
  n\in kC
  \iff
  n=kt+(k-1)\text{ with }t\in D;
  \]
- if \(0\le r\le k-2\), the representation uses \(r\) copies of \(1\) and \(k-r\ge2\) multiples, and \((k-r)D\) is cofinite by Lemma 4.

Thus, apart from finitely many initial values,
\[
G_k(C)=\{k2^j+(k-1):j\ge J\}.
\]
In particular,
\[
G_k(C)(x)=O(\log x),
\qquad
C(x)\sim \frac{x}{k}.
\]
Lemma 1 then directly explains why the extra translate by \(C\) fills the gaps: eventually the gap set is too small to contain a reflected copy of \(C\cap[0,n]\).

This is exactly the Route 3 mechanism sought in the brief.

---

### 7. Precise point where the general route is blocked

For a general thin basis, Lemma 1 reduces the problem to finding an infinite \(B\subseteq A\) such that, with \(C=A\setminus B\),
\[
G_k(C)(n)<C(n)
\]
eventually, or more generally such that \(G_k(C)\) never contains a full reflected copy \(n-C\) for large \(n\).

The premise gives only
\[
G_k(C)\text{ infinite}
\]
for every infinite deletion. It gives no upper bound on \(G_k(C)(n)\), no density information, and no prohibition against the correlations
\[
n-C\subseteq G_k(C).
\]

The natural sparse-deletion estimate
\[
G_k(C)\subseteq B+(k-1)A
\]
does not close the argument: even one translate of \((k-1)A\) may contain far more points than \(C\).

The absorption method would solve the problem if one could always find \(a\in A\setminus B\) and an infinite \(B\subseteq A\) satisfying
\[
a+rB\subseteq(r+1)(A\setminus B)
\qquad(1\le r\le k).
\]
Already for \(k=2\), this requires infinitely many alternate two-term representations of numbers \(a+b\). No such representation redundancy follows from the premise. Attempting to assert it would enter the same territory as difficult representation-function questions.

## Self-Audit

1. **The arithmetic-progression hypothesis is a major restriction.**  
   Theorem 5 does not address thin bases containing no infinite arithmetic progression. I make no claim that every basis has such a reservoir. Within its stated scope, the proof is complete: the deleted powers are absorbed using exact \((r+1)\)-term representations inside the progression.

2. **The absorption proof must handle repeated deleted summands and an arbitrary number \(1\le r\le k\).**  
   This is a potential bookkeeping failure, but it is explicitly covered: occurrences are counted with multiplicity, their sum lies in \(rB\), and replacing \(a+s\) uses exactly \(r+1\) retained terms, leaving a total of exactly \(k+1\).

3. **Cofiniteness of \(hE_T\) must hold uniformly for every \(2\le h\le k+1\).**  
   The two-term case is proved by counting forbidden powers in a linear-size interval. Higher \(h\) follows by adding \(h-2\) copies of one fixed retained element. Since only finitely many \(h\) are needed, a single maximum threshold is legitimate.

## Computations To Verify

```python
# Exact h-fold sumset up to U, with repetitions allowed.
def exact_sumset(S, h, U):
    mask = (1 << (U + 1)) - 1
    bits = 1  # exact 0-fold sumset = {0}
    S = sorted(x for x in S if 0 <= x <= U)
    for _ in range(h):
        nxt = 0
        for s in S:
            nxt |= bits << s
        bits = nxt & mask
    return bits

def contained(bits, n):
    return ((bits >> n) & 1) == 1

def members(bits, U):
    return {n for n in range(U + 1) if contained(bits, n)}
```

Finite verification of the model family \(A_k=k\mathbb N_0\cup\{1\}\):

```python
def model_experiment(k=4, J=4, U=5000):
    A = set(range(0, U + 1, k)) | {1}
    B = {k * (1 << j)
         for j in range(J, 100)
         if k * (1 << j) <= U}
    C = A - B

    kC_bits = exact_sumset(C, k, U)
    kp1C_bits = exact_sumset(C, k + 1, U)

    gaps_k = {n for n in range(U + 1) if not contained(kC_bits, n)}
    gaps_kp1 = {n for n in range(U + 1) if not contained(kp1C_bits, n)}

    predicted = {
        k * (1 << j) + (k - 1)
        for j in range(J, 100)
        if k * (1 << j) + (k - 1) <= U
    }

    print("Large k-gaps not predicted:",
          sorted(n for n in gaps_k - predicted if n >= U // 2))
    print("Predicted witnesses not gaps:",
          sorted(n for n in predicted if n not in gaps_k))
    print("Large (k+1)-gaps:",
          sorted(n for n in gaps_kp1 if n >= U // 2))
    print("Gap-count criterion at U:",
          len(gaps_k), len(C))
```

Verify the deletion-minimality witnesses in the model:

```python
def verify_model_witnesses(k=4, deleted_multiples=(16, 32, 64), U=1000):
    # deleted_multiples should themselves be divisible by k
    A = set(range(0, U + 1, k)) | {1}
    C = A - set(deleted_multiples)
    bits = exact_sumset(C, k, U)

    for b in deleted_multiples:
        n = b + (k - 1)
        if n <= U:
            assert not contained(bits, n), (b, n)
    print("All finite witness checks passed.")
```

Finite check of the absorption criterion:

```python
def check_absorption(A, B, a, k, U):
    A, B = set(A), set(B)
    C = A - B
    assert a in C

    results = {}
    for r in range(1, k + 1):
        rB = exact_sumset(B, r, U)
        rp1C = exact_sumset(C, r + 1, U)

        failures = []
        for s in members(rB, U):
            if a + s <= U and not contained(rp1C, a + s):
                failures.append(a + s)
        results[r] = failures
    return results
```

Finite arithmetic-progression reservoir test:

```python
def progression_experiment(k=3, q=7, d=2, T=5, J=7, U=10000):
    P = {d + q*t for t in range(T, (U-d)//q + 1)}
    # Extra irregular elements can be added; the theorem does not care.
    extras = {n for n in range(U + 1) if n % 19 == 3}
    A = P | extras

    B = {
        d + q*(1 << j)
        for j in range(J, 100)
        if d + q*(1 << j) <= U
    }

    nonpowers = [t for t in range(T, 10*T + 100)
                 if t & (t - 1) != 0]
    t0 = nonpowers[0]
    a = d + q*t0

    failures = check_absorption(A, B, a, k, U)
    for r, bad in failures.items():
        print("r =", r, "first absorption failures =", bad[:20])
```

A direct diagnostic for Route 3:

```python
def gap_diagnostic(A, B, k, U):
    A, B = set(A), set(B)
    C = A - B

    kC = exact_sumset(C, k, U)
    kp1C = exact_sumset(C, k + 1, U)

    gap_count = 0
    c_count = 0
    violations = []

    for n in range(U + 1):
        if n in C:
            c_count += 1
        if not contained(kC, n):
            gap_count += 1

        # If n is a (k+1)-gap, Lemma 1 predicts gap_count >= c_count.
        if not contained(kp1C, n) and gap_count < c_count:
            violations.append(n)

    assert not violations, violations
    return {
        "k_gaps": [n for n in range(U + 1) if not contained(kC, n)],
        "kp1_gaps": [n for n in range(U + 1) if not contained(kp1C, n)],
    }
```

## Route Diagnosis

### Proved ledger

- Exact characterization:
  \[
  n\notin(k+1)C\iff n-(C\cap[0,n])\subseteq G_k(C).
  \]
- Necessary gap-count inequality:
  \[
  n\notin(k+1)C\implies G_k(C)(n)\ge C(n).
  \]
- Deletion-created gap carrier:
  \[
  G_k(A\setminus B)\cap[N_0,\infty)\subseteq B+(k-1)A.
  \]
- Absorption criterion:
  \[
  a+rB\subseteq(r+1)(A\setminus B)\ \forall r\le k
  \implies (k+1)(A\setminus B)\text{ cofinite}.
  \]
- Complete affirmative result when \(A\) contains a tail of an arithmetic progression.
- Complete verification for the deletion-minimal family
  \[
  A_k=k\mathbb N_0\cup\{1\}.
  \]

### Plausible but unproved claims

- A useful global dichotomy may hold: either some sparse deletion has
  \[
  G_k(A\setminus B)(n)<(A\setminus B)(n)
  \]
  eventually, or \(A\) contains an additive reservoir supporting an absorption argument.
- The infinite-deletion premise may impose a barrier or Ramsey-type structure on the finite transversals of the \(k\)-representation hypergraphs. No theorem strong enough to control \((k+1)\)-gaps has been obtained.
- A weaker, non-periodic form of the reservoir theorem may be sufficient, but its existence in arbitrary asymptotic bases is unproved.

### Dead ends

- **Raw density alone:** density one of \(kC\) does not imply cofiniteness of \(C+kC\) when \(C\) is thin.
- **Numerically sparse \(B\):** sparsity of \(B\) does not control the actual gaps, because a sparse collection of vertices may hit all representations of many integers.
- **The carrier bound alone:** \(B+(k-1)A\) can be much larger than \(C\), so Lemma 2 usually cannot trigger Lemma 1.
- **Assuming alternate low-order representations:** for \(k=2\), absorption asks for alternate two-term representations of \(a+b\) for infinitely many \(b\). No such redundancy follows from the premise, and proving it generally risks unresolved representation-function territory.

### Recommended fresh direction

The next serious attempt should seek a structural dichotomy tailored to the reflected-gap obstruction:

1. either construct \(B\) with actual gap count \(G_k(A\setminus B)(n)<(A\setminus B)(n)\);
2. or extract from persistent failures \(n-C\subseteq G_k(C)\) a finite or modular additive reservoir;
3. then apply absorption.

A hypergraph formulation should track not just representation multiplicity, but whether every small transversal forces enough \(k\)-gaps to contain a reflected copy of the survivor set. That correlation issue—not mere density—is the precise unresolved block.