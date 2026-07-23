STATUS: BLOCKED

## Result

Route 2 yields an exact and useful local theory, but not a complete solution. The main structural reduction is that a valid ordering of \(A\) is equivalent to a **strong ordering**—one whose partial sums include \(S_0=0\)—of some coatom \(A\setminus\{a\}\). I prove exact insertion and adjacent-exchange criteria, a free-first-element exchange lemma, and a structural theorem for any maximum valid subconfiguration: it contains a strongly ordered core larger than half of \(A\), while every remaining element creates an interval-covering obstruction. However, the natural extension lemmas are false, even for very small examples. Moreover, a single strongly ordered sequence can simultaneously obstruct arbitrarily many external elements from every insertion slot. Thus fixed-chain insertion, bounded obstruction counting, and strictly improving adjacent-swap arguments are blocked. Completing this route requires a genuinely global augmenting-path theorem across different strong orderings; the needed statement is presently of comparable strength to the original problem.

## Complete Argument

All groups and sums below are in \(\mathbb F_p\).

### 1. Strong orderings and the coatom reduction

Call an ordering \(b_1,\dots,b_n\) of a set \(B\) **strong** if, writing
\[
q_0=0,\qquad q_j=b_1+\cdots+b_j,
\]
the \(n+1\) values
\[
q_0,q_1,\dots,q_n
\]
are pairwise distinct.

This differs from the problem’s notion of validity only by including \(q_0\).

#### Lemma 1: Coatom reduction

For every nonempty \(A\subseteq\mathbb F_p^\times\), the following are equivalent:

1. \(A\) has a valid ordering.
2. There is an \(a\in A\) such that \(A\setminus\{a\}\) has a strong ordering.

#### Proof

Suppose
\[
a_1,a_2,\dots,a_t
\]
is a valid ordering of \(A\), with partial sums \(S_1,\dots,S_t\). Put
\[
B=A\setminus\{a_1\},\qquad b_j=a_{j+1}\quad(1\le j\le t-1).
\]
The partial sums of the tail, including its empty partial sum, are
\[
q_j=b_1+\cdots+b_j=S_{j+1}-S_1
\quad(0\le j\le t-1),
\]
where \(q_0=0=S_1-S_1\). Since \(S_1,\dots,S_t\) are pairwise distinct, so are \(q_0,\dots,q_{t-1}\). Thus the tail is strong.

Conversely, suppose \(B=A\setminus\{a\}\) has a strong ordering \(b_1,\dots,b_{t-1}\), with partial sums \(q_0,\dots,q_{t-1}\). Then
\[
a,b_1,\dots,b_{t-1}
\]
has nonempty partial sums
\[
a+q_0,a+q_1,\dots,a+q_{t-1},
\]
which are pairwise distinct. Hence it is a valid ordering of \(A\). ∎

Thus the original conjecture is exactly the assertion that every nonempty \(A\) has a strongly orderable coatom.

A useful immediate consequence is the following endpoint flexibility.

#### Lemma 2: Free first-element exchange

Let \(d_1,\dots,d_n\) be a strong ordering of \(D\). For every
\[
y\in\mathbb F_p^\times\setminus D,
\]
the sequence
\[
y,d_1,\dots,d_n
\]
is a valid ordering of \(D\cup\{y\}\).

It is strong if and only if no partial sum of \(d_1,\dots,d_n\) equals \(-y\).

#### Proof

Let
\[
r_0=0,\qquad r_j=d_1+\cdots+d_j.
\]
The nonempty partial sums after prepending \(y\) are
\[
y+r_0,y+r_1,\dots,y+r_n.
\]
They are pairwise distinct because \(r_0,\dots,r_n\) are pairwise distinct. This proves validity.

The new ordering is strong precisely when none of these values equals \(0\). Since \(y\ne0\), this is equivalent to
\[
r_j\ne-y\qquad(1\le j\le n).
\]
∎

In particular, the first element of a valid ordering can always be replaced by any new element while retaining validity, because the tail of a valid ordering is strong by Lemma 1.

---

### 2. Exact insertion criterion for strong orderings

Let \(b_1,\dots,b_n\) be a strong ordering, with partial sums
\[
q_0=0,q_1,\dots,q_n.
\]
Let \(x\notin\{b_1,\dots,b_n\}\). There are \(n+1\) insertion slots, indexed by \(k=0,\dots,n\), where slot \(k\) means
\[
b_1,\dots,b_k,x,b_{k+1},\dots,b_n.
\]

#### Lemma 3: Interval-cover insertion criterion

For \(0\le i<j\le n\), define the interval of slots
\[
I_{i,j}=\{i,i+1,\dots,j\}.
\]
Insertion of \(x\) into slot \(k\) fails to be strong if and only if there are indices
\[
0\le i<j\le n
\]
such that
\[
q_i-q_j=x
\]
and
\[
k\in I_{i,j}.
\]

Equivalently, define
\[
\mathcal I_x=
\left\{
[i,j]:
0\le i<j\le n,\ 
b_{i+1}+\cdots+b_j=-x
\right\}.
\]
Then \(x\) is not strongly insertable into any slot if and only if
\[
\bigcup_{I\in\mathcal I_x} I=\{0,1,\dots,n\}.
\]

#### Proof

After insertion into slot \(k\), the partial sums including \(0\) are
\[
q_0,\dots,q_k,\ q_k+x,\ q_{k+1}+x,\dots,q_n+x.
\]
The unshifted values \(q_0,\dots,q_k\) are pairwise distinct, and the shifted values
\[
q_k+x,\dots,q_n+x
\]
are pairwise distinct. Thus a collision can only occur between an unshifted value \(q_i\), where \(i\le k\), and a shifted value \(q_j+x\), where \(j\ge k\).

Such a collision is
\[
q_i=q_j+x,
\]
or
\[
q_i-q_j=x.
\]
Since \(x\ne0\), this forces \(i\ne j\). The inequalities \(i\le k\le j\) then imply \(i<j\), and are exactly the condition \(k\in[i,j]\).

Finally,
\[
q_i-q_j=x
\iff
q_j-q_i=-x
\iff
b_{i+1}+\cdots+b_j=-x.
\]
This proves both formulations. ∎

#### Corollary 4: Endpoint obstructions

If \(x\) cannot be strongly inserted anywhere, then:

1. some nonempty prefix sums to \(-x\);
2. some nonempty suffix sums to \(-x\).

More precisely, there are \(j\ge1\) and \(i\le n-1\) such that
\[
q_j=-x,\qquad q_n-q_i=-x.
\]
Consequently,
\[
q_i+q_j=q_n.
\]

#### Proof

Slot \(0\) can only be covered by an interval \([0,j]\), giving \(q_j=-x\). Slot \(n\) can only be covered by an interval \([i,n]\), giving \(q_n-q_i=-x\). Adding the resulting equations gives \(q_i+q_j=q_n\). ∎

The case \(q_n=-x\) is the unavoidable obstruction that the enlarged set has total sum zero. The next example shows that this is not the only obstruction.

#### Example 5: A nontrivial all-slot strong insertion obstruction

Take \(p=7\),
\[
(b_1,b_2,b_3)=(2,4,6),\qquad x=1.
\]
The partial sums of \(b\), including \(0\), are
\[
(q_0,q_1,q_2,q_3)=(0,2,6,5),
\]
so \(b\) is strong.

The intervals
\[
[0,2]\quad\text{and}\quad[2,3]
\]
both correspond to blocks of sum
\[
6=-1.
\]
They cover every slot \(0,1,2,3\). Hence \(x=1\) cannot be strongly inserted anywhere.

This is not a global obstruction: the enlarged set has the strong ordering
\[
(1,2,6,4),
\]
whose partial sums are
\[
0,1,3,2,6.
\]
Also, the enlarged set has total sum \(6\ne0\), so the obstruction is not caused by total sum zero.

Thus the statement

> every strong ordering can be extended by inserting any new element

is false.

---

### 3. Exact insertion criterion for ordinary valid orderings

Let \(b_1,\dots,b_n\) merely be valid, with
\[
q_0=0,\qquad q_j=b_1+\cdots+b_j.
\]
Thus \(q_1,\dots,q_n\) are distinct, but one of them may equal \(q_0\).

#### Lemma 6: Ordinary insertion criterion

For insertion into slot \(k\ge1\), the resulting ordering is invalid if and only if there are
\[
1\le i<j\le n
\]
such that
\[
q_i-q_j=x,\qquad i\le k\le j.
\]

Insertion into slot \(0\) is valid if and only if the original ordering is strong.

#### Proof

For \(k\ge1\), the new nonempty partial sums are
\[
q_1,\dots,q_k,\ q_k+x,\ q_{k+1}+x,\dots,q_n+x.
\]
The same collision calculation as in Lemma 3 applies, except that \(q_0\) is absent from the unshifted list. Hence \(i\ge1\).

For \(k=0\), the new nonempty partial sums are
\[
q_0+x,q_1+x,\dots,q_n+x.
\]
These are pairwise distinct exactly when \(q_0,\dots,q_n\) are pairwise distinct, namely when the original ordering is strong. ∎

#### Example 7: A valid ordering with no valid insertion slot

Take \(p=7\),
\[
(b_1,b_2,b_3)=(1,6,3),\qquad x=5.
\]
The nonempty partial sums of \(b\) are
\[
1,0,3,
\]
so \(b\) is valid but not strong.

All four insertions fail:

\[
\begin{array}{c|c}
\text{ordering}&\text{nonempty partial sums}\\ \hline
(5,1,6,3)&5,6,5,1\\
(1,5,6,3)&1,6,5,1\\
(1,6,5,3)&1,0,5,1\\
(1,6,3,5)&1,0,3,1
\end{array}
\]

Nevertheless, the enlarged set has the valid ordering
\[
(5,1,3,6),
\]
with partial sums
\[
5,6,2,1.
\]

Thus the route-2 hope that every valid ordering locally extends is already false for a set of size \(3\).

---

### 4. Adjacent exchanges

Adjacent exchanges are especially tractable because they alter only one partial sum.

#### Lemma 8: Adjacent-swap criterion

Let \(b_1,\dots,b_n\) have partial sums \(q_0,\dots,q_n\). Swap \(b_i\) and \(b_{i+1}\). Then every partial sum remains unchanged except \(q_i\), which becomes
\[
q_i'=q_{i-1}+b_{i+1}=q_{i+1}-b_i.
\]

Consequently:

- if the original ordering is valid, the swapped ordering is valid exactly when
  \[
  q_i'\notin\{q_j:1\le j\le n,\ j\ne i\};
  \]
- if the original ordering is strong, the swapped ordering is strong exactly when
  \[
  q_i'\notin\{q_j:0\le j\le n,\ j\ne i\}.
  \]

#### Proof

For positions before \(i\), nothing changes. At position \(i\), \(b_{i+1}\) is used instead of \(b_i\), giving
\[
q_{i-1}+b_{i+1}.
\]
At position \(i+1\), both \(b_i\) and \(b_{i+1}\) have been used, so the partial sum returns to its original value \(q_{i+1}\). All later partial sums are consequently unchanged. The validity and strong-validity criteria follow immediately. ∎

A natural potential is the number of distinct values among \(q_0,\dots,q_n\). Strictly improving adjacent swaps do not suffice.

#### Example 9: A local maximum for the distinct-color potential

Take \(p=7\) and
\[
b=(1,2,4,5).
\]
Its partial sums including \(0\) are
\[
0,1,3,0,5.
\]
It is valid but not strong, and has four distinct partial-sum colors.

The three adjacent swaps give:

\[
\begin{array}{c|c|c}
\text{swap}&\text{partial sums including }0&
\text{number of distinct values}\\ \hline
(1,2)&0,2,3,0,5&4\\
(2,3)&0,1,5,0,5&3\\
(3,4)&0,1,3,1,5&4
\end{array}
\]

Thus no adjacent swap strictly increases the number of distinct colors. Nevertheless,
\[
(1,5,4,2)
\]
is a strong ordering, with partial sums
\[
0,1,6,3,5.
\]

Hence a proof based on a strictly increasing “number of colors” potential is blocked even in a four-element example. Plateaux or temporary deterioration are unavoidable.

---

### 5. Structure of a maximum valid subconfiguration

Although arbitrary local extension fails, the free-first-element exchange gives a nontrivial structural result.

#### Theorem 10: Strong core of a maximum valid subset

Let \(A\subseteq\mathbb F_p^\times\), with \(|A|=t\). Let \(B\subsetneq A\) have maximum possible cardinality among valid-orderable subsets of \(A\), and write
\[
|B|=n.
\]
Choose a valid ordering
\[
b_1,\dots,b_n
\]
of \(B\), and put
\[
D=B\setminus\{b_1\},\qquad
C=A\setminus D.
\]
Then:

1. \(d_1,\dots,d_{n-1}:=b_2,\dots,b_n\) is a strong ordering of \(D\);
2. \(|C|=t-n+1\ge2\);
3. no \(y\in C\) can be strongly inserted into any slot of this fixed ordering of \(D\);
4. if
   \[
   r_0=0,\qquad r_j=d_1+\cdots+d_j,\qquad R=r_{n-1},
   \]
   then for every \(y\in C\) there are indices
   \[
   1\le j\le n-1,\qquad 0\le i\le n-2
   \]
   satisfying
   \[
   r_j=-y,\qquad r_i=R+y;
   \]
5. therefore
   \[
   |C|\le n-1
   \]
   and hence
   \[
   n\ge \left\lceil\frac{t+2}{2}\right\rceil.
   \]

#### Proof

Part 1 follows from Lemma 1: the tail of every valid ordering is strong.

Since \(B\subsetneq A\),
\[
|C|=|A|-|D|=t-(n-1)=t-n+1\ge2.
\]

Suppose some \(y\in C\) could be strongly inserted into the displayed ordering of \(D\). This would give a strong ordering \(E\) of \(D\cup\{y\}\). Since \(|C|\ge2\), choose
\[
z\in C\setminus\{y\}.
\]
By Lemma 2, prepending \(z\) to \(E\) gives a valid ordering of
\[
D\cup\{y,z\}\subseteq A.
\]
This set has cardinality
\[
|D|+2=(n-1)+2=n+1,
\]
contradicting maximality of \(|B|=n\). Thus part 3 holds.

Apply Corollary 4 to each \(y\in C\). Since slot \(0\) is blocked, there is a \(j\ge1\) with
\[
r_j=-y.
\]
Since the final slot is blocked, there is an \(i\le n-2\) with
\[
R-r_i=-y,
\]
or
\[
r_i=R+y.
\]
This proves part 4.

The values \(-y\), for \(y\in C\), are distinct and belong to the set
\[
\{r_1,\dots,r_{n-1}\},
\]
which has size \(n-1\). Therefore
\[
|C|\le n-1.
\]
Since \(|C|=t-n+1\),
\[
t-n+1\le n-1,
\]
so
\[
2n\ge t+2.
\]
This proves part 5. ∎

Thus any hypothetical counterexample contains a valid-orderable subset strictly larger than half its size. More significantly, it produces a strong ordered core \(D\) for which every element in a complement \(C\) of size at least two has an interval family of \((-y)\)-sum blocks covering every insertion slot.

The paired endpoint identities also imply
\[
r_i+r_j=R
\]
for every obstructed \(y\), so the visited partial-sum set has many pairs symmetric around \(R/2\).

This is a genuine restriction, but the next result shows that it does not by itself force an augmentation.

---

### 6. Arbitrarily many simultaneous insertion obstructions

The preceding theorem might suggest trying to prove that only one external element can be blocked by a fixed strong ordering. That is false, and the number of simultaneously blocked elements is unbounded.

#### Theorem 11: Unbounded fixed-order obstruction families

For every integer \(m\ge2\), and every sufficiently large prime \(p\), there exist:

- a strong ordering \(e_1,\dots,e_{2m+1}\);
- \(m\) distinct nonzero residues \(x_1,\dots,x_m\), none among the \(e_i\);

such that no \(x_s\) can be strongly inserted into any slot of the displayed ordering.

#### Proof

Choose parameters
\[
T,a_1,\dots,a_m\in\mathbb F_p
\]
and prescribe partial-sum vertices
\[
r_0=0,
\]
\[
r_{2s-1}=a_s,\qquad r_{2s}=T-a_s
\quad(1\le s\le m),
\]
and
\[
r_{2m+1}=T.
\]
Define
\[
e_i=r_i-r_{i-1}.
\]
Explicitly,
\[
e_1=a_1,
\]
\[
e_{2s}=T-2a_s\quad(1\le s\le m),
\]
\[
e_{2s+1}=a_s+a_{s+1}-T
\quad(1\le s<m),
\]
and
\[
e_{2m+1}=a_m.
\]

Define
\[
x_s=a_s-T.
\]
Then
\[
-x_s=T-a_s=r_{2s}.
\]
Hence the prefix interval
\[
[0,2s]
\]
has sum \(-x_s\). Also
\[
r_{2m+1}-r_{2s-1}=T-a_s=-x_s,
\]
so the suffix interval
\[
[2s-1,2m+1]
\]
also has sum \(-x_s\).

The two intervals
\[
[0,2s]\quad\text{and}\quad[2s-1,2m+1]
\]
cover every insertion slot. Lemma 3 therefore shows that \(x_s\) cannot be inserted strongly anywhere.

It remains to choose the parameters so that:

- the vertices \(r_i\) are pairwise distinct;
- the increments \(e_i\) are nonzero and pairwise distinct;
- the \(x_s\) are nonzero and pairwise distinct;
- no \(x_s\) equals any \(e_i\).

Each prohibited equality is the vanishing of a nonzero linear form in
\[
T,a_1,\dots,a_m.
\]
For \(m\ge2\), inspection of the displayed symbolic expressions shows that none of the required inequalities is identically false. For example, the symbolic edge forms are
\[
a_1,\ a_m,\ T-2a_s,\ a_s+a_{s+1}-T,
\]
and these are mutually distinct as linear forms; likewise \(a_s-T\) is not identically equal to any edge form.

Let \(F\) be the product of all these finitely many nonzero linear forms. For every sufficiently large odd prime \(p\), its reduction modulo \(p\) is a nonzero polynomial. If \(M=\deg F\), the Schwartz–Zippel bound gives at most
\[
M p^m
\]
zeros in \(\mathbb F_p^{m+1}\). For \(p>M\), this is less than \(p^{m+1}\), so some parameter choice has \(F\ne0\). Taking \(p\) also larger than \(3m+2\) ensures that the required \(3m+1\) distinct nonzero elements fit in \(\mathbb F_p^\times\).

For such a choice, \(r_0,\dots,r_{2m+1}\) are distinct, so the \(e_i\) form a strong ordering, and all the stated distinctness conditions hold. ∎

#### Explicit two-element instance

Take \(p=17\), \(m=2\), and
\[
T=10,\qquad a_1=2,\qquad a_2=3.
\]
The partial-sum vertices are
\[
0,2,8,3,7,10,
\]
so the increments are
\[
D=(2,6,12,4,3).
\]
They are distinct and nonzero, and the ordering is strong.

The two external elements are
\[
x_1=2-10=9,\qquad x_2=3-10=10.
\]

For \(x_1=9\), the target sum is \(-9=8\), and the intervals
\[
[0,2],\ [1,5]
\]
cover every slot.

For \(x_2=10\), the target sum is \(-10=7\), and the intervals
\[
[0,4],\ [3,5]
\]
cover every slot.

Thus neither \(9\) nor \(10\) can be inserted into the displayed ordering of \(D\).

Nevertheless, one adjacent exchange changes \(D\) to
\[
(2,12,6,4,3),
\]
which is still strong, and now
\[
(9,2,12,6,4,3)
\]
is strong, with partial sums
\[
0,9,11,6,12,16,2.
\]
Prepending \(10\) gives the valid ordering
\[
(10,9,2,12,6,4,3)
\]
of the entire seven-element set, with partial sums
\[
10,2,4,16,5,9,12.
\]

This illustrates both sides of the route:

- fixed-order insertion can be severely obstructed;
- exchanges can repair the obstruction;
- but a theorem guaranteeing such a repair is still missing.

---

### 7. Precise remaining obstruction

Let \(B\) be a maximum valid-orderable proper subset of a hypothetical counterexample \(A\). Theorem 10 produces a strong ordered core \(D\) and a complement \(C\), with \(|C|\ge2\), such that every \(y\in C\) is blocked in every insertion slot of that particular ordering of \(D\).

To finish Route 2, one would need a theorem of approximately the following form.

> **Unproved augmenting-chain statement.**  
> Given a strongly orderable set \(D\) and a disjoint set \(C\) with \(|C|\ge2\), if every \(y\in C\) is blocked in one strong ordering of \(D\), then a finite sequence of legal adjacent exchanges, endpoint replacements, or more general alternating exchanges produces another strong ordering into which some \(y\in C\) can be inserted.

No monotone potential proving this is known here. The examples above show that:

1. the initial order may block every insertion slot;
2. multiple external elements can be blocked simultaneously;
3. their number can grow linearly with the core size;
4. no strictly increasing adjacent-swap potential based only on the number of distinct partial sums can work;
5. a valid ordering may require moving through plateaux or temporarily worse configurations.

At present, proving the quoted augmenting statement would amount to ruling out exactly the kind of closed exchange component that a counterexample would generate. I do not have an invariant or expansion theorem that rules such components out.

## Self-Audit

1. **The generic construction in Theorem 11 uses a nonconstructive finite-field avoidance argument.**  
   The weakest point is the assertion that every forbidden equality is represented by a nonzero linear form. I believe it is correct because all vertex, edge, and external-element forms are explicitly listed, and for \(m\ge2\) no two relevant symbolic coefficient vectors coincide. The Schwartz–Zippel step then applies directly. The explicit \(p=17\) instance independently verifies the first nontrivial case.

2. **Theorem 10 requires a maximum-cardinality valid subset, not merely a chain that is locally maximal under one chosen insertion rule.**  
   This distinction is essential. The proof uses maximum cardinality exactly once: a strong insertion into the core, followed by prepending another complement element, would produce a valid subset of size \(n+1\). Since all sets involved are finite, such a maximum exists, and the contradiction is rigorous.

3. **The route diagnosis does not prove that no augmenting-path theorem exists.**  
   It only proves that several natural versions are false: direct insertion, one-order counting, and strict adjacent-swap hill climbing. A more sophisticated exchange invariant may still solve the problem. I therefore mark the result BLOCKED rather than claiming that Route 2 is impossible.

## Computations To Verify

The following Python code checks every explicit example and can search for stronger local obstructions.

```python
from itertools import combinations, permutations
from collections import deque

def partials(p, seq):
    s = 0
    out = [0]
    for a in seq:
        s = (s + a) % p
        out.append(s)
    return out

def valid(p, seq):
    q = partials(p, seq)
    return len(set(q[1:])) == len(seq)

def strong(p, seq):
    q = partials(p, seq)
    return len(set(q)) == len(seq) + 1

def insert_at(seq, x, k):
    return tuple(seq[:k]) + (x,) + tuple(seq[k:])

def strong_insertion_slots(p, seq, x):
    return [
        k for k in range(len(seq) + 1)
        if strong(p, insert_at(seq, x, k))
    ]

def valid_insertion_slots(p, seq, x):
    return [
        k for k in range(len(seq) + 1)
        if valid(p, insert_at(seq, x, k))
    ]

def adjacent_swaps(seq):
    seq = tuple(seq)
    for i in range(len(seq) - 1):
        z = list(seq)
        z[i], z[i + 1] = z[i + 1], z[i]
        yield tuple(z)

# Example 7: valid ordering with no valid insertion slot.
p = 7
B = (1, 6, 3)
x = 5
assert valid(p, B)
assert not strong(p, B)
assert valid_insertion_slots(p, B, x) == []
assert valid(p, (5, 1, 3, 6))

# Example 5: strong ordering with no strong insertion slot.
D = (2, 4, 6)
x = 1
assert strong(p, D)
assert strong_insertion_slots(p, D, x) == []
assert strong(p, (1, 2, 6, 4))

# Example 9: adjacent-swap potential trap.
B = (1, 2, 4, 5)
score = lambda seq: len(set(partials(7, seq)))
assert valid(7, B)
assert not strong(7, B)
assert score(B) == 4
assert [score(z) for z in adjacent_swaps(B)] == [4, 3, 4]
assert strong(7, (1, 5, 4, 2))

# Explicit simultaneous obstruction over F_17.
p = 17
D = (2, 6, 12, 4, 3)
assert partials(p, D) == [0, 2, 8, 3, 7, 10]
assert strong(p, D)
assert strong_insertion_slots(p, D, 9) == []
assert strong_insertion_slots(p, D, 10) == []

D2 = (2, 12, 6, 4, 3)
assert strong(p, D2)
assert strong(p, (9,) + D2)

A_order = (10, 9, 2, 12, 6, 4, 3)
assert valid(p, A_order)
assert partials(p, A_order)[1:] == [10, 2, 4, 16, 5, 9, 12]
```

Search for fixed-order simultaneous obstructions:

```python
def blocked_external_elements(p, seq):
    used = set(seq)
    return [
        x for x in range(1, p)
        if x not in used and not strong_insertion_slots(p, seq, x)
    ]

def search_max_fixed_obstruction(p, d):
    """
    Exhaustive; practical only for small p,d.
    Returns a strong ordering with the largest number of
    simultaneously blocked external elements.
    """
    best = None
    best_blocked = []
    residues = range(1, p)

    for subset in combinations(residues, d):
        for seq in permutations(subset):
            if not strong(p, seq):
                continue
            blocked = blocked_external_elements(p, seq)
            if len(blocked) > len(best_blocked):
                best = seq
                best_blocked = blocked
                print("new best:", p, d, best, best_blocked)

    return best, best_blocked
```

Search for the distance, in the legal adjacent-swap graph of strong orderings, to an ordering that admits one of a specified set of external elements:

```python
def strong_adjacent_neighbors(p, seq):
    for z in adjacent_swaps(seq):
        if strong(p, z):
            yield z

def exchange_distance_to_insertion(p, start, external):
    """
    BFS through strong orderings of the same fixed label set.
    Returns (distance, ordering, x, slot), or None.
    """
    start = tuple(start)
    external = tuple(external)
    Q = deque([(start, 0)])
    seen = {start}

    while Q:
        seq, dist = Q.popleft()

        for x in external:
            slots = strong_insertion_slots(p, seq, x)
            if slots:
                return dist, seq, x, slots[0]

        for nxt in strong_adjacent_neighbors(p, seq):
            if nxt not in seen:
                seen.add(nxt)
                Q.append((nxt, dist + 1))

    return None

assert exchange_distance_to_insertion(
    17, (2, 6, 12, 4, 3), (9, 10)
)[0] == 1
```

Search for the smallest valid ordering that cannot be extended in any slot even though the enlarged set is valid:

```python
def has_valid_ordering_by_permutations(p, elements):
    for seq in permutations(elements):
        if valid(p, seq):
            return seq
    return None

def search_local_extension_failures(p, max_n):
    residues = tuple(range(1, p))

    for n in range(1, max_n + 1):
        for Bset in combinations(residues, n):
            outside = [x for x in residues if x not in Bset]

            for Bseq in permutations(Bset):
                if not valid(p, Bseq):
                    continue

                for x in outside:
                    if valid_insertion_slots(p, Bseq, x):
                        continue

                    witness = has_valid_ordering_by_permutations(
                        p, Bset + (x,)
                    )
                    if witness is not None:
                        return {
                            "p": p,
                            "base_order": Bseq,
                            "x": x,
                            "enlarged_witness": witness,
                        }

    return None

print(search_local_extension_failures(7, 4))
```

A particularly useful next computation is to determine, for small \(p\), whether there are strong cores \(D\) and blocked sets \(C\) for which **no sequence of legal adjacent swaps of \(D\)** ever makes an element of \(C\) insertable. Such a result would refute adjacent swaps alone and indicate that endpoint replacement or larger block exchanges are essential.

## Route Diagnosis

**Proved ledger**

- A valid ordering of \(A\) is equivalent to a strong ordering of some coatom \(A\setminus\{a\}\).
- The tail of every valid ordering is strong.
- Any external element can freely replace the first element of a valid ordering while preserving validity.
- Strong insertion is governed exactly by a covering of insertion slots by consecutive blocks summing to \(-x\).
- Adjacent swaps alter exactly one partial sum.
- Any maximum proper valid subset of \(A\) has size at least
  \[
  \left\lceil\frac{|A|+2}{2}\right\rceil
  \]
  and yields a strong core with a simultaneous interval-cover obstruction.
- A fixed strong ordering can simultaneously block arbitrarily many external elements.

**Dead ends**

- “Every valid ordering extends”: false by Example 7.
- “Every strong ordering extends unless the enlarged total is zero”: false by Example 5.
- “At most one external element can be blocked”: false, and Theorem 11 gives unboundedly many.
- “A strictly improving adjacent swap always exists”: false by Example 9.
- “Counting endpoint blockers will push greedy extension past the midpoint”: blocked by the symmetric partial-sum configurations in Theorem 11.

**Plausible but unproved**

- A bounded-radius exchange theorem might hold after allowing adjacent swaps, endpoint replacements, and perhaps short block transpositions.
- The graph of strong orderings of a fixed set may have enough expansion that a complement of size at least two cannot remain blocked throughout an entire component.
- A useful potential may need to track the complete interval-cover hypergraph, not merely the number of repeated colors.

**Precise block**

The remaining task is to prove that a simultaneous insertion obstruction for one strong ordering cannot persist across every ordering reachable by suitable exchanges. No monotone invariant or Hall-type alternating-path argument establishing this has been found. A failure of such a global exchange theorem would itself amount to the core of a counterexample, so the route has reduced to an unproved statement of comparable strength.

A fresh Route 2 attempt should computationally classify the exchange graphs of strong orderings for small sets, measure the minimum exchange radius needed to unlock an insertion, and search specifically for components closed under adjacent swaps and endpoint replacements. If bounded-radius exchange fails, the next promising mechanism is a genuine alternating-tree argument whose states include both the ordered core and the blocked external labels.