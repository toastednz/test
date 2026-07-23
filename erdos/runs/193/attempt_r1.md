STATUS: BLOCKED
## Result

Route 1 does not presently yield a complete proof or disproof. I established several rigorous reductions for any hypothetical counterexample: it may be chosen uniformly recurrent; every return-word sampling of it is again a rank-three counterexample using at least four distinct return displacements; neither it nor any such derived walk can have bounded equal-length additive discrepancy; and van der Waerden’s theorem forces arbitrarily long modularly renormalized subwalks. For a four-step alphabet of rank three, I also give an exact characterization of collinearity in terms of the primitive integer relation among the four step vectors. These results isolate the obstruction sharply, but the return-word operation does not reduce rank or alphabet size, and the four-letter relation remains an unproved additive-repetition problem of essentially comparable strength to the original problem.

## Complete Argument

### 1. Word notation and accepted inputs

Let \(\mathcal A\) be a finite alphabet and let
\[
\phi:\mathcal A\longrightarrow \mathbb Z^3
\]
assign a step vector to each letter. For a finite word \(U=u_0\cdots u_{r-1}\), write
\[
\Sigma(U)=\sum_{i=0}^{r-1}\phi(u_i).
\]

For an infinite word \(w=w_0w_1\cdots\), define prefix sums
\[
P_0=0,\qquad P_n=\sum_{i=0}^{n-1}\phi(w_i).
\]

Call \(w\) **good** if:

1. the \(P_n\) are pairwise distinct;
2. no three distinct \(P_i,P_j,P_k\) are collinear.

Equivalently, every nonempty factor has nonzero sum, and for every factorization \(UV\) into two nonempty adjacent factors,
\[
\Sigma(U)\times \Sigma(V)\neq 0.
\]

I use the following established results from the problem brief:

- van der Waerden’s theorem for finite colorings of \(\mathbb N\);
- the Gerver–Ramsey theorem in rank at most two;
- every infinite word on at most three letters contains an abelian square.

The arguments below prove all additional claims from these inputs.

---

### 2. Modular block renormalization

#### Lemma 2.1

Let \(w\) be any infinite word with values in \(\mathbb Z^3\). For every \(m\ge 2\) and every \(h\ge 1\), there exist integers \(n\ge 0\) and \(d\ge 1\) such that the \(h\) consecutive blocks
\[
B_r=w_{n+(r-1)d}\cdots w_{n+rd-1},
\qquad 1\le r\le h,
\]
all satisfy
\[
\Sigma(B_r)\in m\mathbb Z^3.
\]

#### Proof

Color \(t\in\mathbb N\) by
\[
P_t\bmod m\mathbb Z^3.
\]
There are at most \(m^3\) colors. By van der Waerden’s theorem, there is a monochromatic arithmetic progression
\[
n,n+d,\ldots,n+hd.
\]
Thus
\[
P_{n+rd}\equiv P_{n+(r-1)d}\pmod{m\mathbb Z^3}
\]
for every \(r\), and hence
\[
\Sigma(B_r)=P_{n+rd}-P_{n+(r-1)d}\in m\mathbb Z^3.
\]
\(\square\)

If \(w\) is good, the points
\[
Q_r=\frac{P_{n+rd}-P_n}{m},\qquad 0\le r\le h,
\]
are distinct lattice points with no collinear triple. Thus every hypothetical counterexample contains arbitrarily long finite subwalks which can be rescaled by arbitrarily large integers and remain triple-free.

This does not give compactness for a fixed rescaled step alphabet: the vectors
\[
\frac{\Sigma(B_r)}m
\]
depend on \(m\) and on the van der Waerden block length \(d\).

#### Corollary 2.2: bounded additive discrepancy is impossible

Suppose there is a constant \(C\) such that for every two equal-length factors \(U,V\) of \(w\),
\[
\|\Sigma(U)-\Sigma(V)\|_\infty\le C.
\]
If the prefix sums of \(w\) are distinct, then \(w\) contains a three-term arithmetic progression among its prefix sums.

#### Proof

Choose \(m>C\) and apply Lemma 2.1 with \(h=2\). We obtain adjacent equal-length blocks \(U,V\) such that
\[
\Sigma(U),\Sigma(V)\in m\mathbb Z^3.
\]
Consequently,
\[
\Sigma(U)-\Sigma(V)\in m\mathbb Z^3.
\]
Every coordinate of this difference has absolute value at most \(C<m\), so the difference is zero:
\[
\Sigma(U)=\Sigma(V).
\]
This common vector is nonzero because a zero-sum factor would repeat a prefix sum. Therefore the three block-boundary prefix sums are
\[
P_n,\qquad P_n+\Sigma(U),\qquad P_n+2\Sigma(U),
\]
three distinct collinear points. \(\square\)

In particular, if \(w\) is balanced in the usual Parikh-vector sense—there is \(C_0\) such that counts of each letter in any two equal-length factors differ by at most \(C_0\)—then
\[
\|\Sigma(U)-\Sigma(V)\|_\infty
 \le C_0\sum_{a\in\mathcal A}\|\phi(a)\|_\infty,
\]
so Corollary 2.2 applies.

Hence every counterexample must have unbounded vector discrepancy between equal-length factors.

There is also a quantitative but insufficient consequence. Let
\[
B=\max_{a\in\mathcal A}\|\phi(a)\|_\infty.
\]
For \(h=2\), write
\[
U=\Sigma(B_1),\qquad V=\Sigma(B_2).
\]
In a good word, \(U\) and \(V\) are nonparallel. Since both belong to \(m\mathbb Z^3\),
\[
U\times V\in m^2\mathbb Z^3\setminus\{0\}.
\]
Thus some coordinate of \(U\times V\) has absolute value at least \(m^2\). On the other hand,
\[
\|U\times V\|_\infty\le 2B^2d^2.
\]
Therefore
\[
d\ge \frac{m}{\sqrt2 B}.
\]
This lower bound is consistent with van der Waerden’s theorem and yields no contradiction.

---

### 3. A hypothetical counterexample can be chosen uniformly recurrent

Uniform recurrence is a genuine reduction: recurrence may be imposed without changing the fixed step alphabet.

#### Lemma 3.1

If a good infinite word exists over a finite vector alphabet, then a uniformly recurrent good infinite word exists over a subset of the same alphabet.

#### Proof

Let \(w\in\mathcal A^{\mathbb N}\) be good and let \(T\) be the one-sided shift. Define
\[
X=\overline{\{T^nw:n\ge 0\}}\subseteq \mathcal A^{\mathbb N}.
\]
This is a nonempty compact set satisfying \(T(X)\subseteq X\).

Choose a minimal nonempty closed forward-invariant subset \(M\subseteq X\). Such a set exists: a nested chain of nonempty closed forward-invariant subsets has nonempty intersection by compactness, so Zorn’s lemma applies.

Every finite factor of every \(x\in X\) occurs as a factor of \(w\). Indeed, a sufficiently long prefix of \(x\) is the eventual common prefix of some sequence of shifts \(T^{n_r}w\).

The property of being bad is witnessed by a finite factor:

- a repetition \(P_i=P_j\) is witnessed by a nonempty zero-sum factor;
- a collinear triple \(P_i,P_j,P_k\) is witnessed by adjacent nonempty factors \(U,V\) with
  \[
  \Sigma(U)\times\Sigma(V)=0.
  \]

Neither kind of factor occurs in \(w\), so neither occurs in any \(x\in X\). Thus every \(x\in M\) is good.

It remains to prove uniform recurrence. Minimality implies \(T(M)=M\), since \(T(M)\) is a nonempty compact forward-invariant subset of \(M\).

Fix \(x\in M\) and a finite factor \(u\) of \(x\). Let
\[
C_u=\{y\in M:y\text{ begins with }u\}.
\]
This is nonempty and relatively open in \(M\). For every \(y\in M\), the forward orbit of \(y\) is dense in \(M\), so it meets \(C_u\). Hence
\[
M=\bigcup_{n\ge0}T^{-n}(C_u).
\]
By compactness, finitely many of these sets cover \(M\). If \(N\) is the largest shift in such a finite subcover, then for every \(t\ge0\), some occurrence of \(u\) in \(x\) begins between positions \(t\) and \(t+N\). Thus occurrences of \(u\) have bounded gaps.

Therefore \(x\) is uniformly recurrent and good. \(\square\)

The resulting word cannot be periodic. If it had period \(L\) and period sum \(d\), then:

- if \(d=0\), \(P_0=P_L\);
- if \(d\neq0\), the points \(P_0,P_L,P_{2L}\) are \(0,d,2d\).

Both contradict goodness.

Uniform recurrence alone is not enough to finish the problem. Since infinite abelian-square-free words on four letters exist, applying the same minimal-subshift argument to their factorial language produces uniformly recurrent abelian-square-free four-letter words.

---

### 4. Return-word renormalization reproduces the full obstruction

Let \(x\) be a uniformly recurrent good word and let \(P_n\) be its prefix sums.

Fix any nonempty factor \(u\) of \(x\), and enumerate the starting positions of all its occurrences:
\[
n_0<n_1<n_2<\cdots.
\]
Uniform recurrence gives a constant \(R(u)\) such that
\[
1\le n_{r+1}-n_r\le R(u)
\]
for every \(r\).

Define the return displacement
\[
D_r=P_{n_{r+1}}-P_{n_r}.
\]

#### Lemma 4.1

The sequence \((P_{n_r})_{r\ge0}\) is itself a good bounded-step walk. Its finite step alphabet
\[
D(u)=\{D_r:r\ge0\}
\]
has the following properties:

1. \(\langle D(u)\rangle_{\mathbb Z}\) has rank \(3\);
2. \(|D(u)|\ge4\).

#### Proof

Because \(n_{r+1}-n_r\le R(u)\), every \(D_r\) is the sum of at most \(R(u)\) original steps. There are only finitely many such words, so \(D(u)\) is finite.

The vertices \(P_{n_r}\) are pairwise distinct and are a subset of the original good set. Therefore they contain no collinear triple. Their consecutive differences are precisely the \(D_r\), so they form a good \(D(u)\)-walk.

If the subgroup generated by \(D(u)\) had rank at most two, the coarse walk would lie in an affine rank-two lattice. The planar Gerver–Ramsey theorem would then produce a collinear triple, a contradiction. Thus the rank is three.

Suppose instead that \(|D(u)|\le3\). Regard \((D_r)\) as a word over the alphabet of distinct vectors in \(D(u)\). The theorem on abelian squares over at most three letters gives adjacent nonempty blocks having the same multiplicity of each vector. Their displacement sums are therefore equal, say to \(E\).

The sum \(E\) is nonzero, since otherwise two occurrence-start vertices would coincide. Hence the three boundary vertices of the two coarse blocks are
\[
Q,\qquad Q+E,\qquad Q+2E,
\]
again a contradiction. Therefore \(|D(u)|\ge4\). \(\square\)

This applies to every factor \(u\), no matter how long. Thus a hypothetical counterexample can be chosen so that every return-word scale again exhibits genuinely rank-three motion with at least four distinct return displacements.

Corollary 2.2 also applies to every return-displacement word. Consequently, at every return scale the equal-length additive discrepancy is unbounded.

This is the central obstruction to a descent argument: return-word renormalization does not force a lower-rank or smaller-alphabet instance. It reproduces the original hard case.

---

### 5. Exact algebra for four step vectors

Suppose the step alphabet consists of four vectors
\[
s_1,s_2,s_3,s_4\in\mathbb Z^3
\]
whose \(\mathbb Q\)-linear span has rank three. Let
\[
M:\mathbb Z^4\to\mathbb Z^3,\qquad
M e_i=s_i.
\]
The integer kernel of \(M\) has rank one. Let
\[
r=(r_1,r_2,r_3,r_4)
\]
be its primitive generator, chosen up to sign:
\[
\ker_{\mathbb Z}M=\mathbb Zr.
\]

For a word \(U\), let \(p(U)\in\mathbb N^4\) be its Parikh vector. Then
\[
\Sigma(U)=Mp(U).
\]

#### Lemma 5.1: four-letter kernel criterion

Let \(U,V\) be nonempty factors with Parikh vectors \(p,q\), and suppose \(Mp\) and \(Mq\) are nonzero. Then \(Mp\) and \(Mq\) are parallel if and only if there exist coprime nonzero integers \(\alpha,\beta\) and an integer \(t\) such that
\[
\alpha p-\beta q=t r.
\]

#### Proof

If \(Mp\) and \(Mq\) are parallel and nonzero, their scalar ratio is rational because both are integer vectors. Thus there are coprime nonzero integers \(\alpha,\beta\) such that
\[
\alpha Mp=\beta Mq.
\]
It follows that
\[
M(\alpha p-\beta q)=0.
\]

It remains to justify that every integer vector in the kernel is an integer multiple of \(r\). Over \(\mathbb Q\), the kernel is one-dimensional, so
\[
\alpha p-\beta q=\lambda r
\]
for some \(\lambda\in\mathbb Q\). Since \(r\) is primitive, there exist integers \(c_i\) with
\[
\sum_{i=1}^4 c_i r_i=1.
\]
Therefore
\[
\lambda=\sum_{i=1}^4c_i(\lambda r_i)\in\mathbb Z.
\]
Thus \(\lambda=t\in\mathbb Z\).

Conversely, if
\[
\alpha p-\beta q=tr,
\]
then applying \(M\) gives
\[
\alpha Mp=\beta Mq,
\]
so the two nonzero vectors are parallel. \(\square\)

This criterion includes positive and negative scalar multiples; the signs of \(\alpha,\beta\) distinguish the two cases.

Let
\[
R=r_1+r_2+r_3+r_4.
\]
Taking coordinate sums in the kernel equation yields
\[
\alpha |U|-\beta |V|=tR.
\]

A useful special case occurs when \(R=0\).

#### Corollary 5.2

Suppose \(R=0\) and \(|U|=|V|\). Then
\[
\Sigma(U)\parallel\Sigma(V)
\quad\Longleftrightarrow\quad
p(U)-p(V)\in\mathbb Zr.
\]
In this situation parallelity actually implies
\[
\Sigma(U)=\Sigma(V).
\]

#### Proof

If the sums are parallel, Lemma 5.1 gives
\[
\alpha p-\beta q=tr.
\]
Taking sums of coordinates and using \(|U|=|V|=L>0\) and \(R=0\) gives
\[
(\alpha-\beta)L=0.
\]
Hence \(\alpha=\beta\). Since they were chosen coprime, after changing the common sign we may take \(\alpha=\beta=1\). Thus
\[
p-q=tr
\]
and \(Mp=Mq\).

The converse follows immediately from \(Mr=0\). \(\square\)

For four vectors, therefore, ordinary abelian squares correspond to \(p=q\), but the geometry also forbids all generalized abelian squares
\[
p-q=tr,\qquad t\neq0.
\]
Known four-letter abelian-square-free constructions control only the case \(t=0\). No unavoidable-pattern theorem known from this route forces one of the other relations.

---

### 6. The monotone hard core: adjacent blocks with equal vector averages

A particularly transparent rank-three subclass is obtained by taking
\[
S=\{(1,t):t\in T\}
\]
for a finite set \(T\subseteq\mathbb Z^2\).

For a word \(t_0,t_1,\ldots\in T\), the prefix points are
\[
P_n=\left(n,\sum_{r=0}^{n-1}t_r\right).
\]
They are automatically pairwise distinct because their first coordinates are distinct.

For \(i<j<k\), put
\[
r=j-i,\qquad s=k-j,
\]
and
\[
A=\sum_{n=i}^{j-1}t_n,\qquad
B=\sum_{n=j}^{k-1}t_n.
\]
The two adjacent displacement vectors are
\[
(r,A),\qquad (s,B).
\]
Since \(r,s>0\), these are parallel exactly when
\[
(s,B)=\frac{s}{r}(r,A),
\]
or equivalently
\[
\frac{A}{r}=\frac{B}{s}.
\]

Thus even the following restricted statement would be enough to rule out all monotone counterexamples:

> Every infinite word over a finite subset \(T\subseteq\mathbb Z^2\) has two adjacent nonempty blocks with equal vector averages.

For scalar-valued \(T\subseteq\mathbb Z\), this is the planar theorem in graph form. For \(T\subseteq\mathbb Z^2\), it is already the unresolved rank-three synchronization phenomenon. Neither abelian-square avoidance nor the modular argument above decides it.

---

### 7. Consolidated necessary structure of a counterexample

If the original assertion is false, then there is a counterexample over a fixed finite step set with all of the following properties:

1. the step word is uniformly recurrent and aperiodic;
2. it uses at least four distinct step vectors and has rank three;
3. it avoids abelian squares;
4. equal-length factor sums have unbounded discrepancy;
5. for every \(m,h\), it contains \(h\) consecutive equal-length blocks whose sums all lie in \(m\mathbb Z^3\);
6. for every factor \(u\), the successive occurrence-start displacements form another good bounded-step walk;
7. every such return-displacement alphabet has rank three and at least four distinct vectors;
8. in the four-letter case, every adjacent pair of Parikh vectors avoids all relations
   \[
   \alpha p-\beta q=tr
   \]
   from Lemma 5.1.

These are rigorous necessary conditions, but they do not contradict one another.

## Self-Audit

1. **Use of three external theorems.**  
   I did not reprove van der Waerden’s theorem, the Gerver–Ramsey planar theorem, or the three-letter abelian-square theorem. They are explicitly accepted in the problem brief and are used only at clearly identified points: Lemma 2.1 and Lemma 4.1.

2. **The one-sided minimal-subshift reduction is the most delicate new step.**  
   One might worry that taking a shift-orbit limit introduces a repeated prefix or a collinear triple not present in the original walk. It cannot: either defect is witnessed by a finite step factor, and every finite factor of a point in the orbit closure occurs in the original word. The proof also establishes bounded gaps directly from compactness and minimality.

3. **The return-displacement conclusion depends on using all consecutive occurrences, including overlapping ones.**  
   Overlap causes no problem: \(P_{n_{r+1}}-P_{n_r}\) is still the sum of the finite factor between the two occurrence starts, and uniform recurrence bounds its length. The occurrence-start vertices are an actual subsequence of the original vertices, so injectivity and noncollinearity are inherited exactly.

The decisive missing point is not being concealed: nothing proved here forces a return alphabet to lose rank or fall below four vectors, nor forces the four-letter kernel relation. That is why the status is BLOCKED.

## Computations To Verify

The following exact Python code performs fixed-\(S\) depth-first search, incremental collinearity checking, finite return-displacement diagnostics, and computation of the primitive four-letter kernel relation.

```python
from math import gcd
from itertools import combinations
from functools import reduce

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def cross(a, b):
    return (
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0],
    )

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def det3(a, b, c):
    # a,b,c are columns
    return dot(a, cross(b, c))

def canonical_direction(v):
    """Primitive direction modulo sign."""
    g = reduce(gcd, (abs(x) for x in v), 0)
    if g == 0:
        raise ValueError("zero direction")
    w = tuple(x // g for x in v)
    for x in w:
        if x != 0:
            if x < 0:
                w = tuple(-y for y in w)
            return w
    raise AssertionError

def extension_witness(path, q):
    """
    path is already injective and triple-free.
    Returns None if q is valid; otherwise a witness.
    """
    if q in path:
        return ("repeat", path.index(q), len(path))

    seen = {}
    for i, p in enumerate(path):
        d = canonical_direction(sub(p, q))
        if d in seen:
            return ("collinear", seen[d], i, len(path))
        seen[d] = i
    return None

def first_failure(steps):
    """Return first repeated vertex/collinear triple in a finite step word."""
    path = [(0, 0, 0)]
    for s in steps:
        q = add(path[-1], s)
        witness = extension_witness(path, q)
        if witness is not None:
            return witness, path + [q]
        path.append(q)
    return None, path

def find_path(S, target_vertices):
    """
    Naive exact DFS for a triple-free injective path with target_vertices.
    S must be a list of integer triples.
    """
    path = [(0, 0, 0)]
    used = {(0, 0, 0)}

    def rec():
        if len(path) == target_vertices:
            return list(path)

        for s in S:
            q = add(path[-1], s)
            if q in used:
                continue
            if extension_witness(path, q) is not None:
                continue

            path.append(q)
            used.add(q)
            ans = rec()
            if ans is not None:
                return ans
            used.remove(q)
            path.pop()

        return None

    return rec()

def prefix_sums(steps):
    P = [(0, 0, 0)]
    for s in steps:
        P.append(add(P[-1], s))
    return P

def occurrence_starts(word, u):
    L = len(u)
    return [
        i for i in range(len(word) - L + 1)
        if tuple(word[i:i+L]) == tuple(u)
    ]

def return_displacements(steps, symbolic_word, u):
    """
    Finite-prefix approximation to return displacements for factor u.
    steps[i] is the vector assigned to symbolic_word[i].
    """
    occ = occurrence_starts(symbolic_word, u)
    P = prefix_sums(steps)
    D = []
    for a, b in zip(occ, occ[1:]):
        D.append(sub(P[b], P[a]))
    return occ, D

def has_rank_three(vectors):
    V = list(set(vectors))
    return any(det3(a, b, c) != 0 for a, b, c in combinations(V, 3))

def primitive_kernel_four(S):
    """
    S = [s1,s2,s3,s4], viewed as columns of a rank-3 matrix.
    Returns primitive r with sum r_i s_i = 0.
    """
    assert len(S) == 4
    r = []
    for j in range(4):
        cols = [S[k] for k in range(4) if k != j]
        r.append(((-1)**j) * det3(cols[0], cols[1], cols[2]))

    g = reduce(gcd, (abs(x) for x in r), 0)
    if g == 0:
        raise ValueError("step matrix has rank less than 3")
    r = [x // g for x in r]

    for x in r:
        if x != 0:
            if x < 0:
                r = [-y for y in r]
            break

    check = tuple(sum(r[i] * S[i][j] for i in range(4))
                  for j in range(3))
    assert check == (0, 0, 0)
    return tuple(r)

def equal_length_discrepancy(steps):
    """
    Maximum, over equal-length factors in this finite word,
    of the l_infinity difference between their sums.
    """
    P = prefix_sums(steps)
    N = len(steps)
    best = 0
    witness = None

    for L in range(1, N + 1):
        sums = [sub(P[i+L], P[i]) for i in range(N-L+1)]
        for coord in range(3):
            lo_i = min(range(len(sums)), key=lambda i: sums[i][coord])
            hi_i = max(range(len(sums)), key=lambda i: sums[i][coord])
            gap = sums[hi_i][coord] - sums[lo_i][coord]
            if gap > best:
                best = gap
                witness = (L, lo_i, hi_i, sums[lo_i], sums[hi_i])
    return best, witness

def iterate_morphism(morphism, seed, levels):
    word = list(seed)
    for _ in range(levels):
        word = [b for a in word for b in morphism[a]]
    return word
```

Concrete experiments:

```python
# Monotone square-label alphabet:
S_square = [
    (1, 0, 0),
    (1, 1, 0),
    (1, 0, 1),
    (1, 1, 1),
]

print("kernel:", primitive_kernel_four(S_square))
# Expected up to sign: (1, -1, -1, 1)

for N in range(5, 40):
    path = find_path(S_square, N)
    print(N, path is not None)
    if path is None:
        break

# A tetrahedral rank-three alphabet:
S_tetra = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (-1, -1, -1),
]

print("kernel:", primitive_kernel_four(S_tetra))
```

For a published four-letter abelian-square-free morphism:

1. generate several substitution levels with `iterate_morphism`;
2. map its letters to `S_square` or other searched vector assignments;
3. run `first_failure`;
4. record the offending adjacent-factor Parikh vectors \(p,q\);
5. compare them with the primitive kernel \(r\) from `primitive_kernel_four`.

A useful automated search should vary small four-vector rank-three alphabets, quotient by \(\mathrm{GL}_3(\mathbb Z)\) where practical, and classify every first failure by the relation
\[
\alpha p-\beta q=tr.
\]
Persistent small families of \((\alpha,\beta,t)\) could suggest a genuinely unavoidable projective-Parikh pattern.

Finite return-word diagnostics should test whether long morphic candidates exhibit:

```python
occ, D = return_displacements(steps, word, chosen_factor)
print("number of observed return displacements:", len(set(D)))
print("observed return rank three:", has_rank_three(D))
```

Failure of either condition in a sufficiently complete recursive construction would refute that construction, though finite-prefix success cannot certify an infinite counterexample.

## Route Diagnosis

### What worked

- Van der Waerden coloring converts equal prefix residues into adjacent blocks with highly divisible sums.
- Bounded additive discrepancy is therefore completely ruled out.
- Compact symbolic dynamics shows that recurrence may be imposed without loss.
- Return-word sampling gives an exact renormalization operation.
- The planar theorem and the three-letter abelian-square theorem force every return scale to retain rank three and at least four displacement vectors.
- For four vectors, all geometric failures are captured exactly by one primitive kernel relation.

### Precise block

The hoped-for descent does not descend. For every factor \(u\), the return-displacement word is again a counterexample candidate of exactly the same hard type: rank three, at least four steps, unbounded additive discrepancy. Proving that some factor must instead have rank-two or three-step return displacements would solve the problem, but no argument obtained here supports that assertion; it is of comparable strength to the original theorem.

Likewise, in the four-letter case one would need an unavoidable-pattern result forcing
\[
\alpha p-\beta q\in\mathbb Zr
\]
for adjacent Parikh vectors. Ordinary abelian-square theory forces this only for alphabets of size at most three and fails at four.

The modular argument also stalls quantitatively. It produces nonzero cross products divisible by \(m^2\), but the block length supplied by van der Waerden can grow much faster than \(m\), so the elementary upper bound \(O(d^2)\) cannot force vanishing.

### Plausible but unproved claims

1. Some factor of every minimal rank-three cocycle has return displacements generating rank at most two.
2. Every four-letter word satisfies one of the projective kernel relations in Lemma 5.1 for every rank-three integer assignment.
3. The modular renormalized blocks can be chosen with determinant growth \(o(m^2)\).

Each would be decisive; none is currently justified.

### Dead ends

- **Plain abelian-square forcing:** dies at four letters.
- **Uniform recurrence alone:** four-letter abelian-square-free uniformly recurrent words exist.
- **Repeated factors:** two separated copies yield a parallelogram, not a collinear triple.
- **Pigeonholing block sums:** equal sums at nonadjacent positions do not produce adjacent equal-sum blocks.
- **Congruence plus size:** van der Waerden gives no favorable relation between modulus and block length.
- **Return-word induction:** reproduces rather than simplifies the rank-three obstruction.

A fresh Route 1 attempt should focus on the minimal/return-word setting and seek an invariant that strictly decreases under some derived-word operation. Computationally, the most concrete target is the monotone four-step alphabet
\[
(1,0,0),(1,1,0),(1,0,1),(1,1,1),
\]
whose kernel relation is
\[
(1,-1,-1,1).
\]
Classifying failures of long abelian-square-free words for this alphabet may reveal whether generalized kernel squares are unavoidable or whether a counterexample construction is plausible.