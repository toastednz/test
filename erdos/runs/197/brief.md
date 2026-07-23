# Problem Brief: Erdős Problem #197

## 1. Precise statement

Let  
\[
\mathbb N=\{1,2,3,\dots\}.
\]
Using \(\{0,1,2,\dots\}\) instead makes no substantive difference, since translation preserves arithmetic progressions.

For a finite or countably infinite set \(A\subseteq \mathbb N\), a **permutation of \(A\)** means a sequence
\[
(a_i)_{i\in I}
\]
containing every element of \(A\) exactly once, where \(I=\{1,\dots,|A|\}\) if \(A\) is finite and \(I=\mathbb N\) if \(A\) is infinite.

Such a permutation **avoids monotone 3-term arithmetic progressions** if there are no indices
\[
i<j<k
\]
such that
\[
a_j-a_i=a_k-a_j\neq 0.
\]
Equivalently,
\[
a_i+a_k=2a_j.
\]
The common difference may be positive or negative, so both increasing and decreasing progressions are forbidden.

In positional language, if \(x<y<z\) and \(x+z=2y\), and \(p_A(u)\) denotes the position of \(u\) in the permutation of \(A\), the forbidden condition is
\[
\min\{p_A(x),p_A(z)\}<p_A(y)<\max\{p_A(x),p_A(z)\}.
\]
Thus the numerically middle term of every 3-term progression in \(A\) must occur either before both endpoints or after both endpoints.

### Formal problem

Determine whether there exist sets \(A_0,A_1\subseteq\mathbb N\) and permutations
\[
(a_{c,i})_{i\in I_c}\qquad(c\in\{0,1\})
\]
such that:

1. \(A_0\cap A_1=\varnothing\);
2. \(A_0\cup A_1=\mathbb N\);
3. \((a_{c,i})_{i\in I_c}\) lists \(A_c\) exactly once;
4. for each \(c\in\{0,1\}\) and all \(i<j<k\) in \(I_c\),
   \[
   a_{c,i}+a_{c,k}\ne 2a_{c,j}.
   \]

Equivalently, seek a coloring
\[
\chi:\mathbb N\to\{0,1\}
\]
and, for each color \(c\), a bijective rank function
\[
p_c:\chi^{-1}(c)\to I_c
\]
such that for every arithmetic progression \(x<y<z\) with \(x+z=2y\) whose three terms have color \(c\),
\[
p_c(y)\notin\bigl(\min\{p_c(x),p_c(z)\},\max\{p_c(x),p_c(z)\}\bigr).
\]

### Ambiguities and conventions

- The standard reading of “monotone” forbids both increasing and decreasing progressions. If only increasing progressions were intended, the condition would be weaker.
- “Permuted” must mean an enumeration of order type \(\omega\), not merely an arbitrary total order. If arbitrary countable linear orders were allowed, compactness would make the problem essentially trivial even with one set; see §4.
- It is slightly ambiguous whether both parts must be infinite. A robust affirmative solution should make both parts infinite. Under the looser convention, finite or empty parts are allowed, with the empty permutation vacuously valid.

---

## 2. What counts as a solution

### Complete affirmative solution

A complete proof must provide, explicitly or nonconstructively, a partition
\[
\mathbb N=A_0\sqcup A_1
\]
and an enumeration of each part satisfying the avoidance condition.

If the construction is algorithmic or formula-based, the proof must establish all of the following:

1. **Total assignment:** every \(n\in\mathbb N\) belongs to one of the two parts.
2. **Disjointness:** no \(n\) belongs to both.
3. **Enumeration:** every member of \(A_c\) occurs exactly once in its proposed sequence.
4. **No starvation:** every assigned integer appears at a finite position. Merely producing an injective infinite sequence from each part is insufficient.
5. **Avoidance:** for every color \(c\) and every \(i<j<k\),
   \[
   a_{c,i}+a_{c,k}\ne 2a_{c,j}.
   \]
   Equivalently, every monochromatic numerical progression \(x<y<z\) has its middle term \(y\) outside the positional interval between \(x\) and \(z\).

A rigorous probabilistic existence proof also counts, but it must prove with positive probability that the orders are genuine \(\mathbb N\)-indexed enumerations and that all infinitely many avoidance constraints hold simultaneously.

### Complete negative solution

A disproof must establish the formal negation:

> For every partition \(\mathbb N=A_0\sqcup A_1\), and for every choice of enumerations of \(A_0\) and \(A_1\), at least one enumeration contains indices \(i<j<k\) satisfying
> \[
> a_{c,i}+a_{c,k}=2a_{c,j}
> \]
> for some \(c\in\{0,1\}\).

Equivalently, every two-coloring equipped with one \(\omega\)-order on each color class has a monochromatic 3-term arithmetic progression whose numerical middle term is positionally between its endpoints.

Because the statement is existential, there is no single finite “counterexample partition” that disproves it. A negative solution must be a universal obstruction theorem. In fact, every finite subset of \(\mathbb N\) admits an avoiding permutation, so no finite initial segment alone can refute the problem.

If the intended convention requires both color classes to be infinite, the universal quantifier in a disproof need only range over such partitions. A disproof under the more permissive convention, allowing finite parts, would be stronger.

---

## 3. What does not count

The following do not resolve the problem:

1. **Finite versions only.** Constructing valid permutations for every \([N]\), even uniformly in \(N\), does not produce compatible \(\omega\)-orders.
2. **Arbitrarily long injective sequences.** A sequence that avoids progressions but omits infinitely many assigned integers is not a permutation.
3. **Three colors.** This is the known relaxation stated in the database.
4. **Avoiding only consecutive progressions.** The forbidden indices \(i<j<k\) need not be consecutive.
5. **Avoiding only increasing progressions** while permitting decreasing ones.
6. **Producing arbitrary total orders.** The order must be induced by a sequence indexed by \(\mathbb N\).
7. **Orders with infinite initial blocks.** For example, “put all even numbers before all odd numbers” does not define an \(\omega\)-enumeration of \(\mathbb N\): the odd block is never reached.
8. **Setwise 3-AP avoidance.** Requiring each \(A_c\) to contain no 3-term progression at all is much stronger and is impossible for a finite coloring of \(\mathbb N\), by van der Waerden’s theorem.
9. **Asymptotic or density statements.** Showing that only \(o(N^2)\) bad progressions occur, or that bad progressions have zero density, is insufficient: none may occur.
10. **Conditional constructions** depending on an unproved conjecture.
11. **Finite SAT success.** All finite instances are locally satisfiable with one color, so finite feasibility alone says little about the infinite problem.
12. **A nonconvergent limit of finite permutations.** Every element must eventually acquire a fixed finite position; pointwise instability invalidates a limiting argument.

---

## 4. Known results and context

### 4.1 The three-set relaxation is settled

The database commentary states that there is a partition
\[
\mathbb N=A_0\sqcup A_1\sqcup A_2
\]
such that each \(A_c\) has a permutation avoiding monotone 3-term arithmetic progressions. Thus the corresponding problem with three colors has an affirmative answer.

The open issue is whether the number of parts can be reduced from three to two. No citation or construction for the three-color result is supplied in the given commentary, so its precise mechanism should be recovered from the literature before relying on it as a black box.

### 4.2 Every finite set admits an avoiding permutation

A basic but crucial fact is:

**Finite permutation lemma.** Every finite set \(S\subseteq\mathbb Z\) has a permutation containing no monotone 3-term arithmetic progression.

One recursive proof splits \(S\) by parity. First recursively order the even elements after division by \(2\), then recursively order the odd elements after subtracting \(1\) and dividing by \(2\), and concatenate the two blocks.

To verify this, consider an arithmetic progression \(x,y,z\):

- If its common difference is odd, then \(x,z\) have one parity and \(y\) has the other. Since parity classes are contiguous blocks, \(y\) cannot lie positionally between \(x\) and \(z\).
- If its common difference is even, all three terms have the same parity, and the assertion reduces recursively after scaling by \(2\).

The recursion terminates for a finite set.

Consequences:

- No finite subset can serve as a local obstruction.
- Any negative proof must exploit the requirement that the orders have type \(\omega\).
- Compactness arguments must be handled with exceptional care.

### 4.3 Arbitrary linear orders are easy by compactness

The finite lemma and the compactness theorem imply that any countable \(A\subseteq\mathbb Z\) has some total linear order in which no numerical midpoint lies between its progression endpoints.

Indeed, impose variables recording pairwise comparisons, the axioms of a total order, and one non-betweenness constraint for each 3-term progression. Every finite subsystem is satisfiable by the finite lemma, hence the full system is satisfiable by compactness.

However, the resulting order need not have order type \(\omega\). It may have infinite descending chains, dense intervals, or elements with infinitely many predecessors. It therefore need not be realizable as a permutation
\[
a_1,a_2,\dots.
\]

This distinction is central: the problem is not local non-betweenness but simultaneous non-betweenness in two well-founded, discrete orders of type \(\omega\).

### 4.4 Relation to van der Waerden and Roth

Van der Waerden’s theorem implies that every finite coloring of \(\mathbb N\) contains a monochromatic 3-term arithmetic progression. In particular,
\[
W(2,3)=9.
\]
Thus one cannot solve the problem by making both color classes progression-free as unordered sets.

Roth’s theorem likewise implies that every subset of positive upper density contains a 3-term arithmetic progression. These theorems do not directly obstruct the desired permutations because monochromatic progressions are allowed; only the two monotone positional orders are forbidden.

### 4.5 Heredity

If \(A\) has an avoiding permutation and \(B\subseteq A\), then the subsequence induced on \(B\) is an avoiding permutation of \(B\). This observation can be useful when refining a construction or splitting an already sequenceable set.

In particular, a one-set solution for \(\mathbb N\) would immediately solve the two-set problem, even with both parts infinite, by splitting an avoiding sequence into two infinite subsequences. No such conclusion is presently part of the database commentary.

---

## 5. Traps and edge cases

1. **The common difference may be negative.**  
   Both
   \[
   x,y,z\quad\text{and}\quad z,y,x
   \]
   are forbidden when \(x<y<z\) is an arithmetic progression.

2. **The temporal middle is the averaged term.**  
   The relevant equation is
   \[
   a_i+a_k=2a_j
   \]
   for \(i<j<k\). Other temporal arrangements of the same three numerical values are allowed.

3. **Subsequence, not substring.**  
   There may be arbitrarily many entries between \(a_i,a_j,a_k\).

4. **Infinite block concatenation can fail to enumerate.**  
   An instruction such as “list all elements of block \(B_0\), then all of \(B_1\)” works only if each earlier block is finite. Listing one infinite class first prevents later classes from appearing.

5. **An injective real-valued priority does not automatically define a permutation.**  
   Ordering by real priorities may produce a dense order. To give an \(\omega\)-enumeration, every element must have finitely many predecessors, and the entire order must have a first element and successive elements.

6. **No uniform random permutation of \(\mathbb N\) with exchangeable finite restrictions has order type \(\omega\).**  
   Standard i.i.d. continuous priorities yield a dense random order, not a sequence order.

7. **Reversal is not harmless in the infinite case.**  
   Reversing a finite avoiding permutation works, but an \(\omega\)-sequence has no reverse \(\omega\)-enumeration.

8. **Compactness loses well-foundedness.**  
   “Every finite set has a good order” does not imply that the infinite set has a good enumeration.

9. **Coverage is as important as avoidance.**  
   Greedily appending safe unused values easily produces an infinite avoiding injective sequence. It may permanently omit some integer.

10. **Permanent append obstructions.**  
    If a finite sequence already contains \(u\) before \(v\), then appending
    \[
    x=2v-u
    \]
    would create the progression \(u,v,x\). Once this occurs, \(x\) can never later be appended to that sequence unless earlier entries are rearranged.

11. **Processing integers in increasing numerical order is unsuitable.**  
    If each new \(n\) is appended to its color’s sequence when \(n\) is colored, each color sequence is numerically increasing. It would then have to be setwise 3-AP-free, impossible for a two-coloring by van der Waerden’s theorem.

12. **Cross-block progressions are the main danger.**  
    Ordering each finite block correctly does not address progressions with terms in two or three different blocks.

13. **Finite or empty color classes.**  
    State explicitly whether these are allowed. An affirmative construction with two infinite classes avoids this issue entirely.

14. **Translation of \(\mathbb N\).**  
    Starting at \(0\) instead of \(1\) is harmless, but formulas involving 2-adic valuation must treat \(0\) separately.

---

## 6. Verification hooks

### 6.1 Checker for a finite permutation

Given a finite sequence \(a_1,\dots,a_m\), create a map
\[
p(a_i)=i.
\]
For each pair \(x<z\) in the underlying set with \(x+z\) even, let
\[
y=(x+z)/2.
\]
If \(y\) is present, reject precisely when
\[
\min\{p(x),p(z)\}<p(y)<\max\{p(x),p(z)\}.
\]

This can be implemented in \(O(m^2)\) time using a hash map for positions. Alternatively, loop over \(x,d\) and test \(x,x+d,x+2d\).

### 6.2 Checker for a finite two-color candidate

Input:

- a color \(\chi(n)\in\{0,1\}\) for \(1\le n\le N\);
- one permutation of each finite color class.

Check that the lists are disjoint, cover \([N]\), have no repetitions, and satisfy the positional non-betweenness constraints for every monochromatic 3-term progression in \([N]\).

This is useful for testing proposed formulas but cannot by itself establish the infinite result.

### 6.3 Verify the parity-recursive finite lemma

Implement the recursive ordering:

1. recursively order \(S\cap 2\mathbb Z\) after dividing by \(2\);
2. recursively order \(S\cap(2\mathbb Z+1)\) after mapping \(n\mapsto(n-1)/2\);
3. concatenate.

Test all subsets of \([N]\) for modest \(N\). This provides a baseline and catches errors in the interpretation of “monotone.”

### 6.4 Appendability test

For a current finite sequence
\[
b_1,\dots,b_m,
\]
an unused number \(x\) can be appended without immediately forming a forbidden progression exactly when there are no indices \(r<s\) such that
\[
x=2b_s-b_r.
\]

Maintain the forbidden append set
\[
F(b)=\{2b_s-b_r:r<s\}.
\]
For two sequences, a target \(x\) is currently stranded under append-only growth if it lies in both forbidden sets.

This is a concrete diagnostic for priority and greedy constructions.

### 6.5 SAT/SMT encoding

For a finite universe \([N]\), use:

- Boolean variables \(C_x\) for colors;
- integer rank variables \(R_x\);
- all-different rank constraints within each color;
- for every \(x<y<z\) with \(x+z=2y\), impose
  \[
  C_x=C_y=C_z
  \Longrightarrow
  \neg\bigl(R_x<R_y<R_z\ \lor\ R_z<R_y<R_x\bigr).
  \]

Because one color already suffices on finite sets, additional constraints are needed to test meaningful structural conjectures: prescribed rank bounds, block patterns, fixed color formulas, or extendability conditions.

### 6.6 Testing digital or valuation constructions

For a proposed coloring \(\chi(n)\) and rank/key \(K(n)\):

1. enumerate all \(x,d>0\) with \(x+2d\le B\);
2. retain monochromatic triples;
3. test whether \(K(x+d)\) lies between \(K(x)\) and \(K(x+2d)\);
4. separately test that the key order has finite predecessor sets and actually enumerates the color class.

The second test is essential: many attractive 2-adic or lexicographic orders satisfy local constraints but have the wrong order type.

### 6.7 Extension-tree search

Represent a state by two finite avoiding sequences with disjoint entries. Generate children by appending an unused integer to either sequence when legal. Record:

- the largest \(N\) for which all of \([N]\) have appeared;
- the smallest omitted integer;
- whether it is appendable to either sequence;
- the current forbidden append sets.

Search strategies can prioritize coverage of the least omitted integer. Persistent stranded states may reveal the obstruction any priority construction must overcome, though finite failure does not prove global impossibility.

---

## 7. Attack routes

### Route A: Digital or \(p\)-adic coloring with explicit rank functions

**Core mechanism.**  
Color integers according to a binary-digit invariant, such as a function of \(v_2(n)\), the leading binary block, or a finite automaton on the binary expansion. Define the order in each color using a second digital key.

**Key lemma needed.**  
Construct \(\chi:\mathbb N\to\{0,1\}\) and bijective ranks \(p_c\) such that for every monochromatic progression \(x<y<z\),
\[
p_c(y)<\min\{p_c(x),p_c(z)\}
\quad\text{or}\quad
p_c(y)>\max\{p_c(x),p_c(z)\}.
\]

The proof should exploit the first binary digit or valuation level at which the three terms differ.

**Why it might work.**  
The finite parity recursion already solves all local finite instances. A digital construction is the most natural attempt to convert that recursion into a global enumeration while distributing the infinite parity subtrees between two colors.

**Likely failure point.**  
The natural recursive order says “all of one infinite parity subtree before the other.” That produces an infinite initial block and not an \(\omega\)-order. Lexicographic and 2-adic orders often have the same defect.

**Quick blockage test.**

- Compute the proposed color and rank for \(n\le 10^5\).
- Enumerate all progressions in that range.
- Count predecessor sets under the proposed key. If some element has infinitely many formal predecessors, the construction cannot be an enumeration.

---

### Route B: Scale-separated finite blocks

**Core mechanism.**  
Partition \(\mathbb N\) into rapidly growing finite intervals or digital shells. Give each finite block an avoiding permutation using the finite parity lemma, then assign blocks to the two colors and concatenate appropriately.

**Key lemma needed.**  
A two-state block theorem ensuring that every monochromatic progression meeting multiple blocks has its midpoint in a block that is ordered entirely before or entirely after both endpoint blocks, or else reduces to a controlled progression internal to one block.

A useful form would be a finite “block substitution lemma”: replacing every symbol of a good coarse order by a suitably scaled good finite block preserves avoidance.

**Why it might work.**  
Finite blocks avoid the infinite-initial-block defect. Large scale separation may force any progression crossing blocks into a small number of geometric configurations.

**Likely failure point.**  
Exact arithmetic progressions can span very different scales, and the middle term need not lie in the geometrically middle block under the chosen decomposition. Two block types may not provide enough states; the known three-color construction may exploit precisely a third state.

**Quick blockage test.**

- Implement the first 10–20 block levels.
- Exhaustively classify violations by the block indices containing the three terms.
- Determine whether failures recur in a scale-invariant pattern. A recurring three-state cycle would strongly suggest why two colors are difficult.

---

### Route C: Priority construction with finite extension gadgets

**Core mechanism.**  
Build the two sequences in stages while meeting coverage requirements
\[
R_n:\quad n\text{ eventually appears}.
\]
Use large auxiliary integers and finite rearrangement or insertion gadgets to place the least unmet target without creating a forbidden progression.

**Key lemma needed.**  
A finite extension lemma of the following kind:

> From every suitably prepared pair of finite avoiding sequences and every target \(n\), one can extend, or modify only a controlled terminal segment, so that \(n\) appears while all previous requirements remain permanently satisfied.

The lemma must also guarantee convergence: each previously placed integer changes position only finitely often.

**Why it might work.**  
The obstruction is global coverage rather than finite satisfiability. Priority methods are designed to reconcile infinitely many individually finite requirements.

**Likely failure point.**  
Under append-only growth, a target can become permanently forbidden in both sequences. Allowing insertion or rearrangement can destroy previously verified constraints, and uncontrolled injury may prevent positions from stabilizing.

**Quick blockage test.**

- Exhaustively search small finite states.
- For each state and small target \(n\), determine whether some extension by numbers below a reservoir bound can place \(n\).
- Look for unavoidable states in which a target remains blocked regardless of bounded auxiliary choices.
- Test proposed gadgets against all old–old–new, old–new–new, and new–new–new progressions.

---

### Route D: Compactness plus an order-type upgrade

**Core mechanism.**  
Start from the compactness theorem giving progression-avoiding total orders, then add quantitative constraints intended to force order type \(\omega\). Alternatively, build a finitely branching tree of increasingly large coherent finite rank assignments and apply Kőnig’s infinity lemma.

**Key lemma needed.**  
A normalization or bounded-rank theorem, for example:

> Every finite satisfiable system on \([N]\) has a satisfying two-color order in which the rank of each \(n\le N\) is bounded by an explicit function \(f(n)\), independently of later elements.

Such uniform bounds would permit a diagonal limit in which every integer has a finite stable rank.

**Why it might work.**  
All local non-betweenness constraints are already satisfiable. The only missing ingredient is well-foundedness and finite predecessor sets. A quantitative compactness theorem could bridge exactly that gap.

**Likely failure point.**  
Well-foundedness is not first-order compact. Finite witnesses may require old elements to be pushed arbitrarily far to accommodate new ones, so no uniform rank bounds may exist.

**Quick blockage test.**

- Use SAT/SMT to minimize the maximum rank required for \([n]\) while extending to larger universes \([N]\).
- Track whether the minimum possible rank of a fixed small integer tends to infinity with \(N\).
- If so, naive coherent compactness is blocked and a more flexible two-color normalization is needed.

---

### Route E: Probabilistic construction with nonexchangeable priorities

**Core mechanism.**  
Randomly color the integers and assign color-dependent priorities designed to produce genuine \(\omega\)-orders. Use a local lemma, resampling method, or entropy-compression argument to eliminate all bad progression events.

**Key lemma needed.**  
A probability model satisfying both:

1. every color class is enumerated in order type \(\omega\), almost surely;
2. the bad events
   \[
   \{\chi(x)=\chi(y)=\chi(z),\ p(y)\text{ lies between }p(x),p(z)\}
   \]
   can be simultaneously avoided with positive probability.

This likely requires strongly nonuniform priorities so event probabilities decay with scale.

**Why it might work.**  
The constraints are sparse when viewed through suitable scales, and there is substantial freedom in both coloring and ordering. A multiscale random construction might avoid the deterministic infinite-block problem.

**Likely failure point.**  
Independent continuous priorities give a dense order rather than an \(\omega\)-order. Moreover, each integer belongs to infinitely many progression constraints, producing unbounded dependency in a direct Lovász local lemma formulation.

**Quick blockage test.**

- For the proposed distribution, calculate the expected number of bad progressions involving a fixed integer.
- Check whether this sum is finite.
- Verify separately that every element has finitely many predecessors almost surely.
- Run finite resampling experiments and measure whether violations concentrate at large scales rather than disappearing.

---

### Route F: Disproof via an ordered van der Waerden principle

**Core mechanism.**  
Assume a two-coloring and one \(\omega\)-order on each color. Use the finite predecessor structure of the two orders, together with Ramsey or van der Waerden theory, to force a monochromatic progression whose midpoint lies between its endpoints.

One may encode each integer by its color and its comparison pattern with a finite collection of early landmarks in the two orders, then seek a homogeneous arithmetic configuration.

**Key lemma needed.**  
An “ordered van der Waerden” theorem specialized to two \(\omega\)-orders:

> Every two-coloring of \(\mathbb N\), with each color equipped with an \(\omega\)-order, contains a monochromatic progression \(x<y<z\) such that \(y\) is between \(x\) and \(z\) in that color’s order.

A weaker structural lemma forcing many progression endpoints to occur on both sides of some early element could suffice.

**Why it might work.**  
The distinction between arbitrary linear orders and \(\omega\)-orders is precisely that every element has only finitely many predecessors. This one-sided finiteness may be exploitable through repeated progression configurations or recurrence.

**Likely failure point.**  
The orders can be extremely nonuniform and need not respect numerical intervals, density, translation, or any measurable structure. Standard van der Waerden and Ramsey theorems find monochromatic progressions but do not control the order of their positions.

**Quick blockage test.**

- Formulate finite bounded-delay analogues: all integers up to \(N\) must occur within prescribed rank bounds in their color.
- Optimize the smallest forced monotone progression under these constraints.
- If avoiding models persist with very strong rank bounds, elementary ordered-Ramsey arguments are unlikely to suffice.
- Search for comparison-pattern lemmas that fail already on parity-recursive finite permutations.

---

## 8. Verdict on difficulty

This is a deceptively difficult infinite ordering problem. All finite instances are solvable, and compactness supplies arbitrary avoiding total orders, so the obstruction—if one exists—is entirely in forcing two orders to have type \(\omega\). That makes most ordinary finite extremal and compactness methods inadequate without a quantitative stabilization argument.

The known three-set result indicates that the phenomenon is not impossible in principle and suggests that the central issue is a sharp two-versus-three state threshold. Recovering and analyzing the three-color construction should be an early priority: it may reveal either a compressible third state or an invariant obstructing such compression.

No equivalence to a famous major conjecture is apparent from the supplied statement or standard context. In particular, this is not simply Roth’s theorem or van der Waerden’s theorem in disguise. Nevertheless, a complete proof will likely require a genuinely new infinite construction, a quantitative compactness principle, or a new ordered-Ramsey obstruction. The absence of a prize should not be read as evidence that the problem is routine.