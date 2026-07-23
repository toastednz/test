STATUS: PARTIAL

## Result

I prove a finite upper bound by Route 2: there exists a lattice-periodic coloring satisfying \(A(12005)\). Hence Erdős Problem #188 has a finite answer and, combining this construction with Tsaturian’s published lower bound,  
\[
6\le K\le 12005.
\]
The construction is probabilistic but finite and fully pointwise: the torus is partitioned into half-open squares, a random local-minimum rule selects an independent family of red squares, and a finite hyperplane-arrangement count controls all uncountably many unit-step chains simultaneously. This does not determine the exact value of \(K\).

## Complete Argument

### 1. Periodic square partition

Set
\[
k=12005,\qquad \delta=\frac7{10},\qquad L=2k=24010.
\]
Then
\[
n=\frac L\delta=34300
\]
is an integer. Let
\[
T=(\mathbb R/L\mathbb Z)^2.
\]

Partition \(T\) into the \(n^2\) half-open squares
\[
Q_{a,b}=[a\delta,(a+1)\delta)\times[b\delta,(b+1)\delta)
\pmod{L},
\qquad 0\le a,b<n.
\]
Thus every point of \(T\), including every boundary point, belongs to exactly one cell.

Define a finite graph \(G\) on these cells. Distinct cells \(Q,Q'\) are adjacent when there exist lifts \(p,q\in\mathbb R^2\), with residues in \(Q,Q'\), such that
\[
\|p-q\|_2=1.
\]

There are no loops: two points in the same lifted square are at distance less than
\[
\sqrt2\,\delta=\frac{7\sqrt2}{10}<1,
\]
while points in different \(L\mathbb Z^2\)-translates of the same square are at distance at least \(L-\sqrt2\delta>1\).

### 2. The conflict graph has maximum degree at most \(24\)

Fix a cell \(Q\), and choose a lift of its center \(z\). If \(Q'\) is adjacent to \(Q\), choose corresponding lifts of points \(p\in Q\), \(q\in Q'\) with \(\|p-q\|=1\), and let \(z'\) be the center of the lift of \(Q'\) containing \(q\).

Every point of a square is within \(\delta/\sqrt2\) of its center. Therefore
\[
\|z'-z\|
 \le \|z'-q\|+\|q-p\|+\|p-z\|
 \le 1+\sqrt2\,\delta.
\]
The center displacement has the form
\[
z'-z=\delta(m_1,m_2),\qquad m_1,m_2\in\mathbb Z.
\]
Consequently
\[
\sqrt{m_1^2+m_2^2}
 \le \frac1\delta+\sqrt2
 =\frac{10}{7}+\sqrt2<3.
\]
Hence
\[
m_1^2+m_2^2\le8.
\]
There are exactly \(24\) nonzero integer pairs satisfying this:
\[
\#\{(m_1,m_2)\in\mathbb Z^2\setminus\{(0,0)\}:m_1^2+m_2^2\le8\}=24.
\]
Moreover, a fixed torus cell cannot have two relevant lifts, since two such lifts would differ by a nonzero vector of length at least \(L\), while both centers would lie within \(1+\sqrt2\delta<2\) of \(z\).

Thus
\[
\Delta(G)\le24.
\]

### 3. A random independent family of cells

Give every cell \(Q\) an independent random label
\[
\xi_Q\sim\mathrm{Uniform}(0,1).
\]
Select \(Q\) if its label is smaller than the labels of all its neighbors:
\[
Q\in\mathcal R
\quad\Longleftrightarrow\quad
\xi_Q<\xi_{Q'}\quad\text{for every }Q'\sim Q.
\]

Adjacent cells cannot both be selected: if \(Q\sim Q'\), selection of both would require both
\[
\xi_Q<\xi_{Q'}\quad\text{and}\quad \xi_{Q'}<\xi_Q.
\]
Thus \(\mathcal R\) is an independent set in \(G\).

For every cell \(Q\),
\[
\Pr(Q\in\mathcal R)=\frac1{\deg(Q)+1}\ge\frac1{25},
\]
because among the labels on the closed neighborhood
\[
N[Q]=\{Q\}\cup N(Q),
\]
each is equally likely to be the unique minimum.

### 4. Independence of selection events at five-spaced chain positions

Consider any unit-step chain on the torus:
\[
p_i=x+iu\pmod L,\qquad 0\le i<k,\qquad \|u\|=1.
\]
Let \(Q_i\) be the cell containing \(p_i\), and let \(c_i\) be its torus center.

If \(Q'\in N[Q_i]\), then the torus distance between its center and \(c_i\) is at most
\[
R=1+\sqrt2\,\delta.
\]

Suppose \(i<j\), and put \(d=j-i\). The centers \(c_i,c_j\) differ from \(p_i,p_j\), respectively, by at most \(\delta/\sqrt2\). Since \(d\le k-1\) and \(L=2k\), no nonzero period vector gives a shorter comparison than the direct displacement \(du\). Therefore
\[
d_T(c_i,c_j)\ge d-\sqrt2\,\delta.
\]

If \(d\ge5\), then
\[
d_T(c_i,c_j)\ge5-\sqrt2\,\delta.
\]
On the other hand,
\[
5-\sqrt2\,\delta>2+2\sqrt2\,\delta=2R,
\]
because this inequality is equivalent to
\[
1>\sqrt2\,\delta=\frac{7\sqrt2}{10},
\]
which follows by squaring:
\[
1>\frac{98}{100}.
\]

It follows that whenever \(i\ne j\) are multiples of \(5\),
\[
N[Q_i]\cap N[Q_j]=\varnothing.
\]
Indeed, a cell in the intersection would have its center within \(R\) of both \(c_i\) and \(c_j\), forcing \(d_T(c_i,c_j)\le2R\).

The selection event \(\{Q_i\in\mathcal R\}\) depends only on labels in \(N[Q_i]\). Hence, for indices
\[
I=\{0,5,10,\ldots,12000\},
\]
these events are mutually independent. There are
\[
|I|=2401
\]
such indices. Therefore, for any fixed realizable cell sequence,
\[
\begin{aligned}
\Pr(Q_i\notin\mathcal R\text{ for every }i\in I)
&\le \left(1-\frac1{25}\right)^{2401}\\
&\le \exp\left(-\frac{2401}{25}\right)\\
&=\exp(-96.04).
\end{aligned}
\]

### 5. There are only finitely many relevant chain cell-sequences

Write
\[
x=(x_1,x_2)\in[0,L)^2,\qquad u=(a,b),\qquad a^2+b^2=1.
\]
For every \(i\), the cell containing \(x+iu\) is determined by the signs, including possible equality, of affine expressions
\[
x_1+ia-j\delta,\qquad x_2+ib-j\delta
\]
as \(j\) ranges over relevant integers.

Each coordinate of \(x+iu\) lies between \(-k\) and \(L+k\). Hence, for a fixed \(i\) and one coordinate, the number of relevant grid lines is at most
\[
\frac{L+2k}{\delta}+2
=\frac{4k}{7/10}+2
=\frac{40k}{7}+2
\le6k,
\]
where the final inequality holds because \(k\ge7\).

Thus all chain cell-sequences are determined by the sign pattern of at most
\[
s\le2k(6k)=12k^2
\]
affine hyperplanes in the four real parameters \((x_1,x_2,a,b)\).

For completeness, the total number of relatively open faces in an arrangement of \(s\) affine hyperplanes in \(\mathbb R^4\) is at most
\[
\sum_{r=0}^{4}2^r\binom sr.
\]
This follows by the standard induction
\[
F_d(s)\le F_d(s-1)+2F_{d-1}(s-1),
\]
obtained when the \(s\)-th hyperplane subdivides old faces and carries the induced arrangement of the preceding hyperplanes. In particular,
\[
\sum_{r=0}^{4}2^r\binom sr\le(3s)^4.
\]
Restriction to the subset \(a^2+b^2=1\) cannot create additional sign patterns. Therefore the number \(M\) of realizable cell-sequences is at most
\[
M\le(3s)^4\le(36k^2)^4.
\]

This count includes boundary sequences because the full trinary sign pattern—negative, zero, or positive—determines membership in the half-open grid cells.

### 6. The union bound

We claim
\[
(36k^2)^4<e^{96}.
\]
Indeed, \(e>2.7\), for example from the first six terms of its power series. Hence
\[
e^4>2.7^4>36
\]
and
\[
e^{10}>2.7^{10}>12005=k.
\]
Therefore
\[
36k^2<e^4(e^{10})^2=e^{24},
\]
and raising to the fourth power gives the claim.

For every realizable cell-sequence, the probability that all its \(2401\) five-spaced cells are unselected is at most \(e^{-96.04}\). Consequently,
\[
\Pr(\text{some unit-step \(k\)-chain has no selected sampled cell})
\le M e^{-96.04}
<e^{96}e^{-96.04}<1.
\]

Thus there is a realization of the labels for which every unit-step \(12005\)-term chain has at least one selected cell among the indices \(0,5,\ldots,12000\).

Fix such a realization.

### 7. The plane coloring

Let \(R\subseteq\mathbb R^2\) be the periodic lift of the union of selected half-open cells, and color \(R\) red and its complement blue.

If two red points were exactly unit distance apart, their cells would be adjacent in \(G\), contradicting independence of the selected cells. This also covers all cell boundaries because the half-open cells form an actual partition.

For every \(x\in\mathbb R^2\) and every unit vector \(u\), the chain
\[
x,x+u,\ldots,x+12004u
\]
has at least one term whose torus cell is selected. That point is red. Hence there is no all-blue unit-step \(12005\)-term progression.

Therefore
\[
A(12005)
\]
holds. In particular, \(K\) is finite and
\[
K\le12005.
\]
Using Tsaturian’s published result \(\neg A(5)\), one obtains
\[
6\le K\le12005.
\]

## Self-Audit

1. **Continuum-to-finite reduction.**  
   The most delicate point is that uncountably many \((x,u)\) yield only finitely many cell-sequences. This holds because every cell membership is determined by signs of an explicitly finite collection of affine forms, including zero signs for boundary points. The hyperplane-face count covers all such sign patterns.

2. **Independence of the five-spaced selection events.**  
   Merely having distant chain points would not suffice; the entire closed conflict neighborhoods must be disjoint. The proof establishes the stronger center-distance inequality
   \[
   d_T(c_i,c_j)>2(1+\sqrt2\delta),
   \]
   which directly rules out a common conflict-neighbor.

3. **Periodic copies and boundary points.**  
   Exact-distance constructions often fail here. Periodic copies are included in the definition of the conflict graph, and the large period \(L=2k\) makes the relevant short lift unique. Half-open squares assign every grid boundary point to exactly one cell, while each individual square has diameter strictly below \(1\).

## Computations To Verify

```python
from math import sqrt, log, exp

k = 12005
delta = 7 / 10
L = 2 * k
n = L / delta

assert n == 34300

# Candidate center offsets for conflict-neighbors.
threshold = (1 / delta + sqrt(2))**2
offsets = [
    (m, n)
    for m in range(-10, 11)
    for n in range(-10, 11)
    if (m, n) != (0, 0) and m*m + n*n <= threshold
]
print("threshold squared:", threshold)
print("candidate offsets:", len(offsets), offsets)
assert threshold < 9
assert len(offsets) == 24

# Five-spaced sampled indices.
sample_indices = list(range(0, k, 5))
assert len(sample_indices) == 2401
assert sample_indices[-1] == 12000

# Separation inequality for conflict neighborhoods.
R = 1 + sqrt(2) * delta
assert 5 - sqrt(2) * delta > 2 * R

# Hyperplane-arrangement and union-bound estimates.
s_bound = 12 * k**2
log_M_bound = 4 * log(36 * k**2)
fixed_sequence_exponent = len(sample_indices) / 25

print("log M bound:", log_M_bound)
print("fixed-sequence exponent:", fixed_sequence_exponent)
print("union bound:", exp(log_M_bound - fixed_sequence_exponent))

assert log_M_bound < 96
assert fixed_sequence_exponent == 96.04
assert exp(log_M_bound - fixed_sequence_exponent) < 1
```

A more direct finite implementation of the construction would be conceptually:

```python
# Not computationally practical at full n=34300, but exact in principle.

cells = [(a, b) for a in range(n) for b in range(n)]

# Candidate graph offsets are among the 24 offsets above.
# For each offset, one can exactly test whether the corresponding
# two half-open squares contain points at distance exactly 1.
neighbors = build_exact_conflict_graph(cells, offsets, modulus=n)

labels = independent_continuous_random_labels(cells)

selected = {
    Q for Q in cells
    if all(labels[Q] < labels[W] for W in neighbors[Q])
}

assert all(
    not (Q in selected and W in selected)
    for Q in cells for W in neighbors[Q]
)
```

## Route Diagnosis

**Proved ledger.**

- A periodic half-open square partition with side \(7/10\) has a unit-conflict graph of maximum degree at most \(24\).
- Random local minima in that graph form an independent red family, with every cell selected with probability at least \(1/25\).
- Along any unit-step chain, closed conflict neighborhoods at indices differing by at least \(5\) are disjoint.
- All length-\(k\) chain cell-sequences are controlled by at most \(12k^2\) affine hyperplanes and hence number at most \((36k^2)^4\).
- These facts and the union bound prove \(A(12005)\).

**Dead ends encountered.**

- A periodic array consisting of one small disk per fundamental cell fails in rational torus directions: entire parallel orbit cosets can avoid the disks forever.
- Pure stripe constructions fail because a positive-width red stripe contains red points exactly unit distance apart along the stripe.
- A small-period random construction is vulnerable to short periodic torus orbits. Taking period \(L=2k\) removes all such recurrence within the chain length under consideration.

**Plausible but unproved improvements.**

- Hexagonal cells should reduce the conflict degree and likely improve the numerical upper bound.
- Using the intrinsic three-dimensional parameter space \((x_1,x_2,\theta)\), rather than the ambient four-dimensional hyperplane count, should reduce the entropy estimate.
- Neither improvement appears remotely sufficient by itself to reach \(k=6\).

**Precise block.**

Route 2 successfully proves finiteness but does not identify the minimum. The probabilistic entropy argument requires thousands of terms and offers no mechanism for proving \(A(6)\), while the supplied lower-bound record only gives \(\neg A(5)\). A fresh exact-resolution attempt should now target either a highly structured periodic construction for \(k=6\), with exact CAD/SMT verification, or finite exact SAT obstructions for \(k\ge6\).