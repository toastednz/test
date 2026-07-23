# Problem Brief: Erdős Problem #472 — Ulam’s Prime Recurrence

## 1. Precise statement

Let \(\mathbb P=\{2,3,5,7,\dots\}\) denote the set of positive primes.

Choose an integer \(m\ge 1\) and a finite strictly increasing sequence of primes
\[
q_1<q_2<\cdots<q_m.
\]
The initial terms are arbitrary; they are not required to have been produced by the recurrence.

Suppose \(q_1,\dots,q_n\) have been defined for some \(n\ge m\). Define
\[
I_n=\left\{i\in\{1,\dots,n\}:q_n+q_i-1\in\mathbb P\right\}.
\]
If \(I_n\neq\varnothing\), let
\[
j_n=\min I_n
\]
and set
\[
q_{n+1}=q_n+q_{j_n}-1.
\]
If \(I_n=\varnothing\), the process terminates at \(q_n\).

Because \(q_1<\cdots<q_n\), the candidate values
\[
q_n+q_1-1<q_n+q_2-1<\cdots<q_n+q_n-1
\]
are strictly increasing. Thus choosing \(j_n=\min I_n\) is exactly the same as choosing the smallest prime among the candidate values.

The problem asks whether
\[
\exists m\ge1\ \exists q_1<\cdots<q_m\in\mathbb P\ 
\forall n\ge m,\quad I_n\neq\varnothing.
\]
Equivalently: does there exist a finite prime seed for which the deterministic recursion is defined forever?

### Standard interpretation and alternatives

The standard reading is that \(i\) ranges over all currently available indices \(1\le i\le n\), including \(i=n\). This brief adopts that convention.

Two less likely alternatives are:

1. \(1\le i<n\), excluding the current term \(q_n\);
2. \(1\le i\le m\), allowing only the original seed terms as increments.

These are materially different problems. In particular, under the standard \(i\le n\) convention, the one-term seed \((2)\) begins
\[
2,3,5,7,11,13,17,\dots.
\]
Under \(i<n\), the seed \((2)\) cannot even be extended at its first step.

### Equivalent additive formulation

Set
\[
a_n=q_n-1.
\]
Then \(a_n+1\) is prime and the recurrence becomes
\[
a_{n+1}=a_n+a_{j_n},
\]
where \(j_n\) is the least \(i\le n\) for which
\[
a_n+a_i+1
\]
is prime. Except for \(q=2\), all \(a_i\) are positive even integers.

### Prime-pair formulation

If \(q_{n+1}\) is produced using \(q_i\), then
\[
q_{n+1}-q_i=q_n-1.
\]
Thus, at each step, the even integer \(q_n-1\) must occur as the difference of two primes \(q_i\) and \(q_{n+1}\), with the lower prime \(q_i\) already present in the sequence. The recurrence chooses the smallest available lower endpoint \(q_i\).

---

## 2. What counts as a solution

### Complete proof of existence

A complete affirmative solution must exhibit, or prove the existence of, a finite seed
\[
q_1<\cdots<q_m
\]
such that for every \(n\ge m\), at least one index \(i\le n\) satisfies
\[
q_n+q_i-1\in\mathbb P.
\]

It is not necessary to give a closed formula for every \(q_n\), but the argument must establish nontermination for all \(n\), not merely for a very large computed range.

If the proof identifies the exact selected index \(j_n\) or an explicit formula for \(q_{n+1}\), it must also establish the minimality condition:
\[
q_n+q_i-1\notin\mathbb P\qquad(1\le i<j_n).
\]
If the proof only establishes that some candidate is prime and its invariant is valid regardless of which earlier candidate is selected, then identifying \(j_n\) is unnecessary.

### Complete disproof

A complete negative solution must prove the universal statement
\[
\forall m\ge1\ \forall q_1<\cdots<q_m\in\mathbb P\ 
\exists N\ge m
\]
such that the recursion is defined through \(q_N\) and
\[
q_N+q_i-1\notin\mathbb P
\qquad\text{for every }1\le i\le N.
\]

A single terminating seed does **not** disprove the problem, because the problem is existential.

A finite exhaustive computation could constitute a disproof only if accompanied by a rigorous theorem reducing all possible infinite seeds to a finite, explicitly searched class. The search must then provide checkable primality and compositeness certificates.

### Verification of finite claims

For a proposed finite trajectory, verification requires:

- primality certificates for all terms;
- for each generated \(q_{n+1}=q_n+q_j-1\), compositeness certificates for all earlier candidates
  \[
  q_n+q_i-1,\qquad i<j;
  \]
- a primality certificate for the selected candidate.

For a terminal state, one needs a compositeness certificate, such as a nontrivial factor, for every candidate \(q_n+q_i-1\).

---

## 3. What does not count

None of the following resolves the problem:

- showing that the seed \((3,5)\), \((2)\), or any other seed continues for finitely many terms;
- showing that every seed up to a numerical bound continues for a long time;
- finding arbitrarily long finite trajectories with seeds depending on the desired length;
- proving that a positive proportion, density-one set, or “almost all” stages are extendable;
- proving a better lower bound for the stopping time;
- proving that the process is infinite under the Hardy–Littlewood conjecture, Schinzel’s hypothesis, a random-prime model, or another unproved hypothesis;
- proving that among all primes \(r\le q_n\), some \(q_n+r-1\) is prime, unless one also proves that such an \(r\) occurs among the earlier sequence terms;
- invoking Bertrand’s postulate merely to find a prime between \(q_n\) and \(2q_n\);
- proving that every even integer is a difference of two primes without controlling the lower endpoint and its membership in the sequence;
- presenting numerical evidence or probabilistic heuristics without a rigorous all-\(n\) argument.

In particular, compactness does not automatically convert arbitrarily long examples into one infinite example: the space of possible prime seeds has unbounded, infinite branching.

---

## 4. Known results and context

The problem is due to Ulam and is listed as open.

The database gives the seed
\[
3,5,
\]
for which the sequence begins
\[
3,5,7,11,13,17,\dots.
\]
Indeed:
\[
\begin{aligned}
5+3-1&=7,\\
7+3-1&=9\quad\text{and}\quad 7+5-1=11,\\
11+3-1&=13,\\
13+3-1&=15\quad\text{and}\quad 13+5-1=17.
\end{aligned}
\]

Under the standard convention, the seed \((2)\) generates
\[
2,3,5,7,11,13,17,\dots.
\]
Once the current term is odd, the candidate arising from \(q_i=2\) is
\[
q_n+1,
\]
an even integer greater than \(2\), hence composite. Therefore the non-\(2\) tail of the trajectory from \((2)\) agrees with the trajectory from \((3,5)\). Proving this particular trajectory infinite would solve the problem affirmatively, although another seed could conceivably work even if this one terminates.

### Elementary structural facts

Whenever the process extends,
\[
q_n<q_{n+1}\le 2q_n-1.
\]
The strict lower inequality follows from parity:

- if \(q_n=2\), the standard self-candidate gives \(3\);
- if \(q_n\) is odd, the term \(q_i=2\), if present, gives an even composite, while every successful \(q_i\) is odd and gives \(q_{n+1}\ge q_n+2\).

Consequently, generated trajectories are strictly increasing and cannot cycle. Also,
\[
q_{n+1}<2q_n,
\]
so growth is at most exponential.

### Relation to prime-pair problems

At a stage with \(q_n=p\), extension requires an earlier sequence prime \(r\le p\) such that
\[
r+(p-1)
\]
is prime. Thus one is seeking a prime pair with prescribed, growing even difference \(p-1\), and with its lower endpoint constrained to a sparse, adaptively generated set.

The Hardy–Littlewood prime-pair heuristic predicts that, among all primes \(r\le p\), the number for which \(r+p-1\) is prime should be roughly
\[
\mathfrak S(p-1)\frac{p}{(\log p)^2},
\]
where \(\mathfrak S(p-1)\) is the relevant singular series. This suggests abundance when all primes \(r\le p\) are available. The actual recurrence has only the earlier sequence primes available, and their distribution is part of the problem.

Relevant classical results do not settle this:

- **Bertrand–Chebyshev:** a prime exists between \(p\) and \(2p\), but it need not equal \(p+q_i-1\) for an earlier \(q_i\).
- **Dirichlet’s theorem:** concerns primes in fixed arithmetic progressions, not simultaneous primality of \(r\) and \(r+p-1\) with a changing gap.
- **Brun and sieve methods:** give upper bounds and almost-prime information for prime pairs, but the parity problem obstructs the required lower bound.
- **Maynard–Tao bounded-gap theorems:** produce infinitely many prime pairs with some bounded gap, not pairs with each prescribed growing gap \(p-1\).
- **Polignac-type conjectures:** even the assertion that every even number occurs infinitely often as a prime gap would not immediately solve the recurrence, because the lower endpoint must be at most \(p\) and must already belong to the trajectory.

No part of the full existential question is presently known to be settled from the supplied database information.

---

## 5. Traps and edge cases

1. **The index range matters.**  
   Including \(i=n\) permits the candidate \(2q_n-1\). Excluding it changes the process.

2. **“Smallest prime” does not mean the next prime after \(q_n\).**  
   Only the finite candidate set
   \[
   \{q_n+q_i-1:1\le i\le n\}
   \]
   is searched.

3. **Minimality must be checked.**  
   To claim that a particular \(q_i\) produces \(q_{n+1}\), all candidates from smaller indices must be composite.

4. **The seed is arbitrary.**  
   It need not itself satisfy the recurrence before index \(m\). Any argument for universal termination must handle all finite increasing prime seeds, including sparse and highly engineered ones.

5. **The prime \(2\) is exceptional.**  
   It is active only at the first step of the seed \((2)\). Thereafter its candidate is even and composite.

6. **Bertrand’s postulate is insufficient.**  
   If \(P\in(q_n,2q_n)\) is prime, representing it as
   \[
   P=q_n+q_i-1
   \]
   requires \(P-q_n+1\) itself to be an earlier sequence prime.

7. **Prime-gap arguments need the correct direction.**  
   The required identity is
   \[
   q_{n+1}-q_i=q_n-1,
   \]
   not a statement about the consecutive gap \(q_{n+1}-q_n\).

8. **Fixed-gap conjectures are not uniform enough.**  
   Here the gap \(q_n-1\) grows with the state. Pointwise results or conjectures for each fixed gap do not automatically supply a lower endpoint below \(q_n\).

9. **Candidate primality events are correlated.**  
   They share the common summand \(q_n-1\), and their residues modulo small primes are inherited from the trajectory. Treating them as independent random integers can be seriously misleading.

10. **Long computation is not an infinitude proof.**  
    Since the values are strictly increasing, there is no finite-state cycle that could certify nontermination.

11. **A failed seed is not a counterexample.**  
    It refutes only the claim that that particular seed is infinite.

12. **An arbitrary prime between \(q_n\) and \(2q_n\) may correspond to a composite increment.**  
    If \(P-q_n+1\) is not a prime already in the sequence, then \(P\) is irrelevant.

---

## 6. Verification hooks

### A. Exact simulator

Maintain an array \(Q=[q_1,\dots,q_n]\). At each stage:

```text
p = Q[n]
for i = 1,...,n:
    N = p + Q[i] - 1
    if N is prime:
        append N to Q
        record selected index i
        continue to next stage
if no candidate is prime:
    declare terminal
```

Use certified primality testing for proof-quality output:

- trial division or deterministic Miller–Rabin in ranges where its bases are proven sufficient;
- APR-CL, ECPP, or Pratt certificates for larger values;
- explicit nontrivial factors for compositeness.

### B. Prefix certificates

For every generated step, store:

- the selected index \(j_n\);
- a primality certificate for \(q_n+q_{j_n}-1\);
- a factor of \(q_n+q_i-1\) for each \(i<j_n\).

This independently verifies both the recurrence and its minimality rule.

### C. Terminal certificates

At a claimed stopping state \(q_n\), factor or provide a compositeness certificate for every
\[
q_n+q_i-1,\qquad 1\le i\le n.
\]
Since each candidate is below \(2q_n\), every composite candidate has a prime factor at most \(\sqrt{2q_n}\).

### D. Statistics worth recording

For each step, record:

- \(j_n\), the selected index;
- the increment \(q_{j_n}-1\);
- \(q_n/n\), \(q_n/(n\log n)\), and \(\log q_n/n\);
- the number of prime candidates among all \(i\le n\), not merely the first;
- the number of candidates surviving sieving by primes up to \(z\);
- the number of distinct indices ever selected;
- residue distributions of \(q_i\) modulo small primes.

These data directly test growth, density, and residue-covering hypotheses.

### E. Exhaustive bounded seed search

For bounds \(m\le M\) and \(q_m\le B\), enumerate all increasing prime seeds and simulate each for a prescribed number of generated steps. This can find:

- unusually long trajectories;
- terminal seeds;
- seeds with slow or fast growth;
- possible self-replenishing patterns.

Such a search is not a proof unless paired with a theorem reducing the unrestricted problem to the bounded search.

### F. Residue-covering certificates

At a state \(q_n=p\), attempt to assign to every \(i\le n\) a small prime \(\ell_i\) such that
\[
p+q_i-1\equiv0\pmod{\ell_i}
\quad\text{and}\quad
p+q_i-1>\ell_i.
\]
A complete assignment proves the state terminal. SAT or integer-programming methods can search for small-prime covering patterns and candidate modular invariants.

### G. Compare conventions

Implement both \(i\le n\) and \(i<n\). This avoids accidentally reporting data for the wrong recurrence, especially when the self-candidate \(2q_n-1\) is selected.

---

## 7. Attack routes

### Route 1: Additive-recurrence bootstrap and growth control

Work with
\[
a_n=q_n-1,\qquad a_{n+1}=a_n+a_{j_n},
\]
subject to \(a_k+1\) prime.

**Key lemma needed.**  
Prove a self-reinforcing estimate showing that along a suitable seed, enough of the translates
\[
a_n+a_i+1
\]
contain primes to force \(j_n\) to remain sufficiently small. This should imply subexponential growth, ideally
\[
\log q_n=o(n),
\]
and then feed back into an abundance-of-candidates estimate.

**Why it might work.**  
The recurrence always chooses the earliest successful increment. If successful indices are usually \(O(\log q_n)\), growth may remain near polynomial rather than exponential, leaving \(n\) candidates for integers of size only \(n^{O(1)}\).

**Likely failure point.**  
There is no unconditional theorem guaranteeing a prime in an arbitrary adaptive set of \(n\) translates. Growth control and prime existence are circular: slow growth would make primes likely, but prime existence is needed to prove slow growth.

**Quick obstruction test.**  
Compute \(j_n\), \(\log q_n/n\), and the empirical distribution of \(j_n/\log q_n\). Large sustained selected indices or positive limiting \(\log q_n/n\) would weaken this route.

---

### Route 2: Sieve or transference on the earlier-prime set

At stage \(p=q_n\), consider
\[
A_n=\{q_i-1:1\le i\le n\}.
\]
The goal is to prove that \(p+a\) is prime for at least one \(a\in A_n\).

**Key lemma needed.**  
A lower-bound sieve or transference theorem tailored to sets \(A_n\) produced by the recurrence, showing
\[
\#\{i\le n:p+q_i-1\in\mathbb P\}>0
\]
under a verifiable density or equidistribution hypothesis.

**Why it might work.**  
For each small prime \(\ell\), only one residue class of \(q_i\bmod\ell\) makes \(p+q_i-1\) divisible by \(\ell\). If the earlier terms are sufficiently equidistributed, small-prime divisibility should not cover every candidate.

**Likely failure point.**  
Surviving all small-prime sieves is not the same as being prime. The classical parity problem is exactly the obstacle to obtaining a positive lower bound for prime values in this type of two-prime correlation. Moreover, the set \(A_n\) is sparse and adaptive.

**Quick obstruction test.**  
For large computed states, sieve all candidates by primes up to \(q_n^\theta\). Determine whether the number of survivors tracks the expected sieve main term or collapses because the trajectory concentrates in unfavorable residue classes.

---

### Route 3: Uniform Hardy–Littlewood prime-pair theory plus trajectory density

Use the identity
\[
q_{n+1}-q_i=q_n-1.
\]

**Key lemma needed.**  
A uniform lower bound, for the growing even shift \(h=p-1\), of the form
\[
\#\{i\le n:q_i+h\in\mathbb P\}
   \gg \frac{n\,\mathfrak S(h)}{\log p},
\]
valid for the adaptively generated set \(\{q_1,\dots,q_n\}\).

**Why it might work.**  
The unrestricted Hardy–Littlewood heuristic predicts about
\[
\mathfrak S(p-1)\frac{p}{(\log p)^2}
\]
prime pairs \(r,r+p-1\) with \(r\le p\). If the trajectory retains a sufficiently representative subset of the primes below \(p\), at least one lower endpoint should belong to the sequence.

**Likely failure point.**  
This requires much more than the usual fixed-shift Hardy–Littlewood conjecture: the shift grows with \(p\), the lower endpoints are restricted to a sparse adaptive subset, and uniform error terms are essential. Standard bounded-gap results do not approach this.

**Quick obstruction test.**  
At computed states, count all earlier \(q_i\) for which \(q_i+q_n-1\) is prime and compare with
\[
n\,\mathfrak S(q_n-1)/\log q_n.
\]
Also compare the sequence subset with all primes \(r\le q_n\) having the required partner.

---

### Route 4: Engineer a self-replenishing seed or reservoir

Exploit the freedom to choose an arbitrary finite seed. Attempt to construct a finite collection of “reservoir” primes whose shifts guarantee a controlled block of future terms, while the newly generated terms replenish the reservoir for later blocks.

**Key lemma needed.**  
A finite-state invariant \(\mathcal P\) such that:

1. some finite prime seed satisfies \(\mathcal P\);
2. every state satisfying \(\mathcal P\) has a prime candidate;
3. after the deterministic smallest-candidate choice, the new state again satisfies \(\mathcal P\).

An alternative is an explicit scheduling identity that produces provably prime outputs indefinitely.

**Why it might work.**  
Unlike a recurrence with a fixed starting value, this problem allows a highly engineered initial configuration. It may be possible to encode several increment scales or residue classes and rotate between them.

**Likely failure point.**  
Most explicit schemes reduce to proving infinitely many primes in a thin family, such as repeated values of \(2p-1\), or to an infinite system of prime-tuple conditions. Minimality is also dangerous: an unintended earlier prime candidate changes the planned schedule.

**Quick obstruction test.**  
Use beam search or SAT-guided seed search to maximize continuation length while enforcing a proposed finite-state pattern. Check whether the pattern repeatedly breaks because a designated output is composite or because an earlier candidate unexpectedly becomes prime.

---

### Route 5: Disproof by eventual congruence covering or a terminal-trap theorem

Seek a universal mechanism forcing every trajectory into a state where all candidates are composite.

**Key lemma needed.**  
Prove that for every finite seed there is some later state \(p=q_n\) and a finite set of small primes \(L\) such that for every earlier \(q_i\), some \(\ell\in L\) satisfies
\[
p+q_i-1\equiv0\pmod\ell
\]
with \(p+q_i-1>\ell\).

A more structural version would identify a monotone residue invariant or Lyapunov quantity that forces such a covering.

**Why it might work.**  
The additive recurrence strongly constrains residues:
\[
a_{n+1}\equiv a_n+a_{j_n}\pmod M.
\]
Finite residue systems can develop covering patterns even while the actual integers grow. A universal modular trap would provide a genuine negative solution.

**Likely failure point.**  
There is no evident monotonicity modulo \(M\), and arbitrary initial seeds can be chosen to avoid any fixed finite collection of residue patterns. The process may continually introduce new residue classes and new usable increments.

**Quick obstruction test.**  
Search long trajectories modulo products of small primes and use SAT/model checking to determine whether every modular state reaches a covered state. Any realizable modular cycle avoiding coverage blocks a proof based solely on that modulus, though it does not itself produce an infinite prime trajectory.

---

## 8. Verdict on difficulty

This appears to be a genuinely difficult open problem. Even a single-step extension at a general state asks for a prime pair with the growing prescribed difference \(q_n-1\), with the lower prime constrained to the earlier trajectory. Existing theorems on primes in intervals, bounded prime gaps, or fixed arithmetic progressions do not provide this.

The problem is not known to be equivalent to Goldbach, the twin-prime conjecture, or Polignac’s conjecture. Those conjectures do not directly handle the adaptive lower-endpoint restriction. A sufficiently strong, uniform, subset-sensitive Hardy–Littlewood prime-pair theorem would likely settle a well-behaved trajectory, but such a result is far beyond current unconditional methods.

The most promising concrete directions are:

1. establish unexpectedly strong slow-growth and equidistribution properties for the \((2)\) or \((3,5)\) trajectory;
2. exploit the freedom of the seed to construct a self-replenishing invariant;
3. search for a universal modular terminal trap as a disproof strategy.

Any claimed elementary proof should be examined especially carefully for misuse of Bertrand’s postulate, omission of the smallest-candidate condition, or an unjustified assumption that the earlier sequence contains all relevant primes.