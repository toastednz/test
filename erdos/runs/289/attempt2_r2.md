STATUS: BLOCKED

## Result

Route 2 does not currently yield a complete construction. I proved a general square-root obstruction for every grouped divisor-coin construction: if \(M\) is a common denominator, every nonempty legal block has integer coin weight strictly exceeding \(2\sqrt M\). Consequently, a \(c\)-block cap for \(1/Q\) must have common denominator \(M>4c^2Q^2\). This explains precisely why ordinary practical-number coverage and the reservoir’s tiny residual do not combine. I also analyzed the practical number \(Q_4=38\,146\,972\,656\) completely and proved that no legal representation of \(1\) exists using only divisors of \(Q_4\), despite several additional consecutive-divisor pairs beyond the reservoir.

## Complete Argument

### 1. A universal square-root gap for grouped divisor coins

Let \(M\) be a positive integer and let \(I=[a,b]_{\mathbb N}\), where \(b\ge a+1\), be an interval such that every \(n\in I\) divides \(M\). Define its integer coin weight by
\[
A_I:=M w(a,b)=\sum_{n=a}^b\frac Mn.
\]

#### Lemma 1
Every such interval satisfies
\[
\boxed{A_I>2\sqrt M.}
\]

#### Proof

Because \(a\mid M\) and \(a+1\mid M\), and \(\gcd(a,a+1)=1\), one has
\[
a(a+1)\mid M.
\]
Write
\[
M=t\,a(a+1),\qquad t\in\mathbb N.
\]
Then
\[
A_I\ge \frac Ma+\frac M{a+1}
=t(a+1)+ta=t(2a+1).
\]
Moreover,
\[
\begin{aligned}
t^2(2a+1)^2-4M
&=t^2(2a+1)^2-4ta(a+1)\\
&=t\bigl(4(t-1)a(a+1)+t\bigr)>0.
\end{aligned}
\]
Thus \(t(2a+1)>2\sqrt M\), proving the claim. ∎

Equivalently, if
\[
q=\frac Ma,\qquad r=\frac M{a+1},
\]
then \(qr=M^2/[a(a+1)]\ge M\), and hence
\[
q+r>2\sqrt{qr}\ge2\sqrt M.
\]

#### Corollary 2
Suppose \(k\) legal intervals, all supported on divisors of \(M\), have total reciprocal weight \(R/M\), where \(R\in\mathbb N\). Then
\[
\boxed{R>2k\sqrt M.}
\]

In particular, if their total weight is \(1\), then
\[
\boxed{k<\frac{\sqrt M}{2}}
\qquad\text{and hence}\qquad
\boxed{M>4k^2.}
\]

#### Proof

Sum Lemma 1 over the \(k\) intervals:
\[
R=\sum_{i=1}^k A_{I_i}>2k\sqrt M.
\]
The specialization \(R=M\) gives the second assertion. ∎

This applies to every hypothetical solution after taking \(M\) to be the least common multiple of its denominators.

---

### 2. Consequence for caps

Consider a cap
\[
\frac1Q=\sum_{i=1}^c w(I_i).
\]
Let
\[
M=\operatorname{lcm}\bigl(Q,\{n:n\in I_1\cup\cdots\cup I_c\}\bigr)
=Qt.
\]
Multiplication by \(M\) gives
\[
t=\sum_{i=1}^c A_{I_i}.
\]

#### Corollary 3
Every \(c\)-block cap for \(1/Q\) satisfies
\[
\boxed{t>4c^2Q}
\qquad\text{and}\qquad
\boxed{M>4c^2Q^2.}
\]

#### Proof

By Corollary 2,
\[
t>2c\sqrt M=2c\sqrt{Qt}.
\]
Squaring and dividing by \(t>0\) gives
\[
t>4c^2Q.
\]
Multiplying by \(Q\) yields \(M>4c^2Q^2\). ∎

Thus a bounded-block cap cannot live in a common denominator only moderately larger than \(Q\). This is a direct obstruction to the most natural practical-number completion of the exact reservoir.

---

### 3. The reservoir is asymptotically extremal for the gap

For \(q\ge1\), put
\[
M=2q(2q+1)=q(4q+2).
\]
The dimer \([2q,2q+1]\) has integer coin weight
\[
\frac M{2q}+\frac M{2q+1}
=(2q+1)+2q=4q+1.
\]
The target integer corresponding to \(1/q\) is
\[
\frac Mq=4q+2.
\]
Hence this dimer misses the target by exactly one integer coin:
\[
M\,d(2q)=\frac Mq-1.
\]

The lower bound from Lemma 1 is nearly attained because
\[
(4q+1)^2-4M=1.
\]
Thus the under-dimer reservoir is not merely an arbitrary near-construction: it produces essentially the smallest possible grouped coin at this common-denominator scale, and the terminal coin of weight \(1\) lies inside the forbidden square-root gap.

For the recurrence
\[
Q_{j+1}=2Q_j(2Q_j+1),
\]
both \(2Q_j\) and \(2Q_j+1\) divide every later \(Q_m\). Multiplying
\[
1=\sum_{j=0}^{m-1}d(2Q_j)+\frac1{Q_m}
\]
by \(Q_m\) therefore gives a grouped divisor-coin representation of \(Q_m-1\), followed by the unattainable singleton coin \(1\).

This formally explains why ordinary practical-number subset-sum coverage does not automatically repair the reservoir: all nonempty legal groups start above \(2\sqrt{Q_m}\), while the deficit is \(1\).

---

### 4. A complete grouped-divisor analysis of \(Q_4\)

The first reservoir denominators are
\[
Q_1=6,\qquad Q_2=156,\qquad Q_3=97656,
\]
and
\[
Q_4=2Q_3(2Q_3+1)=195312\cdot195313.
\]
Now
\[
195312=2^4\cdot3\cdot13\cdot313
\]
and
\[
195313=17\cdot11489.
\]
The integer \(11489\) is prime: trial division by all primes at most
\(\sqrt{11489}<108\) gives nonzero remainders. Therefore
\[
\boxed{
Q_4=2^4\cdot3\cdot13\cdot17\cdot313\cdot11489
=38\,146\,972\,656.
}
\]

Incidentally, \(Q_4\) is practical. Indeed, the Stewart–Sierpiński inequalities for its ordered prime factorization are
\[
\begin{aligned}
3&\le \sigma(2^4)+1=32,\\
13&\le \sigma(2^4\cdot3)+1=125,\\
17&\le \sigma(2^4\cdot3\cdot13)+1=1737,\\
313&\le \sigma(2^4\cdot3\cdot13\cdot17)+1=31249,\\
11489&\le \sigma(2^4\cdot3\cdot13\cdot17\cdot313)+1
=9\,811\,873.
\end{aligned}
\]

Thus this is a concrete test of whether ordinary practicality supplies the required grouped representation.

#### Lemma 4
The complete list of consecutive divisor pairs of \(Q_4\) is
\[
\boxed{
(1,2),(2,3),(3,4),(12,13),(16,17),(51,52),
(312,313),(195312,195313).
}
\]

#### Proof

The odd divisors of \(Q_4\) are
\[
D=B\cup11489B,
\]
where
\[
B=\{1,3,13,17,39,51,221,313,663,939,4069,5321,
12207,15963,69173,207519\}.
\]
Every even divisor is \(2^e v\) for \(1\le e\le4\) and \(v\in D\).

Every pair of consecutive integers contains one odd member \(u\). Direct checking over the displayed finite set \(D\) gives
\[
\left\{
u\in D:
u-1=2^e v,\ 1\le e\le4,\ v\in D
\right\}
=
\{3,13,17,313,195313\},
\]
corresponding respectively to
\[
(2,3),(12,13),(16,17),(312,313),(195312,195313),
\]
and
\[
\left\{
u\in D:
u+1=2^e v,\ 1\le e\le4,\ v\in D
\right\}
=
\{1,3,51\},
\]
corresponding to
\[
(1,2),(3,4),(51,52).
\]
These exhaust all possible odd members of a consecutive divisor pair. ∎

After denominator \(1\) is excluded, the maximal consecutive divisor components are therefore
\[
[2,4],\ [12,13],\ [16,17],\ [51,52],\
[312,313],\ [195312,195313].
\]

Within \([2,4]\), the legal nonempty choices are
\[
[2,3],\qquad [3,4],\qquad [2,4].
\]
The last has weight
\[
w(2,4)=\frac12+\frac13+\frac14=\frac{13}{12}>1,
\]
so it cannot occur in a target-\(1\) representation. Every other component contributes either its entire dimer or nothing.

The relevant exact identities are
\[
d(12)=\frac16-\frac1{156},
\]
\[
d(312)=\frac1{156}-\frac1{97656},
\]
and
\[
d(195312)=\frac1{97656}-\frac1{Q_4}.
\]
Consequently,
\[
d(12)+d(312)+d(195312)
=\frac16-\frac1{Q_4}.
\tag{1}
\]

There is also the exact alternative
\[
\boxed{
d(16)+d(51)=d(12)-\frac1{10608}.
}
\tag{2}
\]
Indeed, with common denominator
\[
10608=2^4\cdot3\cdot13\cdot17,
\]
one has
\[
d(12)=\frac{25}{156}=\frac{1700}{10608},
\]
\[
d(16)=\frac{33}{272}=\frac{1287}{10608},
\]
and
\[
d(51)=\frac{103}{2652}=\frac{412}{10608}.
\]
Thus \(1287+412=1699=1700-1\).

#### Proposition 5
There is no admissible representation of \(1\) all of whose denominators divide \(Q_4\).

#### Proof

The low component cannot contribute \([2,4]\), since that already exceeds \(1\).

Suppose it contributes \([3,4]\), of weight \(d(3)=7/12\). The total weight of all five remaining dimers is, by (1) and (2),
\[
\begin{aligned}
&d(12)+d(16)+d(51)+d(312)+d(195312)\\
&=d(12)+\left(d(12)-\frac1{10608}\right)
+\left(\frac1{156}-\frac1{Q_4}\right)\\
&<2d(12)+\frac1{156}\\
&=2\left(\frac16-\frac1{156}\right)+\frac1{156}
<\frac13.
\end{aligned}
\]
Hence even selecting all of them gives total less than
\[
\frac7{12}+\frac13=\frac{11}{12}<1.
\]

It remains to consider \([2,3]\), whose weight is \(5/6\). The remaining dimers would need to sum exactly \(1/6\).

If \(d(12)\) is selected together with either \(d(16)\) or \(d(51)\), the sum exceeds \(1/6\), since
\[
d(12)=\frac16-\frac1{156}
\]
and both \(d(16)\) and \(d(51)\) exceed \(1/156\).

If \(d(12)\) is selected but neither \(d(16)\) nor \(d(51)\) is selected, then even selecting both larger reservoir dimers gives, by (1),
\[
d(12)+d(312)+d(195312)
=\frac16-\frac1{Q_4}<\frac16.
\]

Finally, if \(d(12)\) is omitted, the maximum possible remaining weight is
\[
\begin{aligned}
d(16)+d(51)+d(312)+d(195312)
&=\left(d(12)-\frac1{10608}\right)
+\left(\frac1{156}-\frac1{Q_4}\right)\\
&=\frac16-\frac1{10608}-\frac1{Q_4}
<\frac16.
\end{aligned}
\]
Thus no subset has weight \(1/6\).

All possible legal choices have been exhausted, so no target-\(1\) representation supported on divisors of \(Q_4\) exists. ∎

This also shows concretely that practicality of \(M\) is far from sufficient: \(Q_4\) represents every ordinary integer target by unrestricted divisor coins, but not the target \(Q_4\) when the complementary denominators must occur in legal consecutive blocks.

## Self-Audit

1. **The exhaustive consecutive-divisor classification for \(Q_4\) is the most computation-sensitive step.**  
   It depends on the displayed factorization and a finite check over 32 odd divisors. The criterion used is exhaustive—every consecutive pair has exactly one odd member—and the supplied code independently reproduces the list.

2. **The assertion that \(11489\) is prime uses trial division rather than a conceptual factorization theorem.**  
   This is nevertheless rigorous because \(\sqrt{11489}<108\), so checking the listed primes up to \(107\) is sufficient. The computational verification below performs exactly that check.

3. **The square-root gap does not rule out Route 2 in full.**  
   An engineered common denominator may be much larger than \(4c^2Q^2\), and target-specific sums of large grouped coins may still hit \(M\). I therefore make no claim that the original problem is disproved; the route is blocked because no cardinality-refined grouped practical architecture meeting this necessary growth condition has been constructed.

## Computations To Verify

```python
from fractions import Fraction
from math import isqrt
from itertools import product

def d(a):
    return Fraction(1, a) + Fraction(1, a + 1)

# Reservoir values
Q = [1]
for _ in range(4):
    q = Q[-1]
    Q.append(2*q*(2*q + 1))

assert Q == [1, 6, 156, 97656, 38146972656]
Q4 = Q[4]

# Exact identities used in the proof
assert d(12) == Fraction(1, 6) - Fraction(1, 156)
assert d(312) == Fraction(1, 156) - Fraction(1, 97656)
assert d(195312) == Fraction(1, 97656) - Fraction(1, Q4)
assert d(16) + d(51) == d(12) - Fraction(1, 10608)

# Trial-division primality check for 11489
def is_prime_trial(n):
    if n < 2:
        return False
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            return False
    return True

assert is_prime_trial(313)
assert is_prime_trial(11489)
assert 195313 == 17 * 11489
assert Q4 == (2**4) * 3 * 13 * 17 * 313 * 11489

# Generate all divisors from a factorization
def divisors_from_factorization(fac):
    ds = [1]
    for p, e in fac.items():
        powers = [p**j for j in range(e + 1)]
        ds = [d0 * pe for d0 in ds for pe in powers]
    return sorted(ds)

fac_Q4 = {2: 4, 3: 1, 13: 1, 17: 1, 313: 1, 11489: 1}
divs = divisors_from_factorization(fac_Q4)
D = set(divs)

pairs = [(n, n + 1) for n in divs if n + 1 in D]
expected_pairs = [
    (1, 2), (2, 3), (3, 4), (12, 13),
    (16, 17), (51, 52), (312, 313),
    (195312, 195313)
]
assert pairs == expected_pairs

# Split divisors >= 2 into maximal consecutive components
positive_divs = [n for n in divs if n >= 2]
components = []
for n in positive_divs:
    if not components or n != components[-1][-1] + 1:
        components.append([n])
    else:
        components[-1].append(n)

nontrivial_components = [c for c in components if len(c) >= 2]
assert nontrivial_components == [
    [2, 3, 4],
    [12, 13],
    [16, 17],
    [51, 52],
    [312, 313],
    [195312, 195313],
]

# Enumerate all legal local states in a consecutive component.
# A state may contain multiple runs, but every run must have length >= 2.
def local_states(component, M):
    L = len(component)
    states = {(0, 0)}  # (integer coin weight, number of runs)

    for mask in range(1, 1 << L):
        runs = []
        i = 0
        legal = True
        while i < L:
            if not (mask >> i) & 1:
                i += 1
                continue
            j = i
            while j + 1 < L and ((mask >> (j + 1)) & 1):
                j += 1
            if j - i + 1 < 2:
                legal = False
                break
            runs.append((i, j))
            i = j + 1

        if legal:
            coin = sum(
                M // component[i]
                for i in range(L)
                if (mask >> i) & 1
            )
            states.add((coin, len(runs)))

    return states

# Exact DP over components
dp = {(0, 0)}
for comp in components:
    states = local_states(comp, Q4)
    new_dp = set()
    for total, count in dp:
        for coin, add_count in states:
            if total + coin <= Q4:
                new_dp.add((total + coin, count + add_count))
    dp = new_dp

reachable_counts_at_one = sorted(
    count for total, count in dp if total == Q4
)
assert reachable_counts_at_one == []

# Verify the square-root inequality without floating point:
# A_I^2 > 4M for every legal block among divisors of Q4.
for comp in nontrivial_components:
    for i in range(len(comp)):
        for j in range(i + 1, len(comp)):
            coin = sum(Q4 // n for n in comp[i:j+1])
            assert coin * coin > 4 * Q4

print("All checks passed.")
```

A broader Route-2 search should use:

```python
def grouped_reachable_counts(M, factorization):
    divs = divisors_from_factorization(factorization)
    divs = [n for n in divs if n >= 2]

    components = []
    for n in divs:
        if not components or n != components[-1][-1] + 1:
            components.append([n])
        else:
            components[-1].append(n)

    dp = {(0, 0)}
    for comp in components:
        states = local_states(comp, M)
        new_dp = set()
        for total, count in dp:
            for coin, dc in states:
                if total + coin <= M:
                    new_dp.add((total + coin, count + dc))
        dp = new_dp

    return sorted(c for total, c in dp if total == M)
```

Priority experiments are:

1. factor \(2Q_m+1\) for \(m\ge4\);
2. enumerate the new consecutive divisor components of \(Q_{m+1}\);
3. compute exact reachable run counts at target \(Q_{m+1}\);
4. search practical \(M\) with unusually many solutions of \(a(a+1)\mid M\);
5. reject cap architectures immediately unless \(M>4c^2Q^2\).

## Route Diagnosis

**Proved ledger.**

- Every legal block coin over common denominator \(M\) is \(>2\sqrt M\).
- Every target-\(1\), \(k\)-block construction has lcm \(M>4k^2\).
- Every \(c\)-block cap for \(1/Q\) has lcm \(M>4c^2Q^2\).
- The reservoir dimer is asymptotically extremal for this inequality and misses its grouped target by exactly one coin unit.
- \(Q_4\) is practical, but no admissible target-\(1\) support consists solely of divisors of \(Q_4\).

**Plausible but unproved.**

- Factoring later \(2Q_m+1\) may generate enough small factors to create a much richer consecutive-divisor graph.
- A target-specific grouped practical theorem might still work with \(M\) far above the square-root lower bound and with many local states per window.
- A successful family would need its attainable run counts at target \(M\) to contain long intervals, not merely isolated values.

**Dead end diagnosed.**

The ordinary Stewart–Sierpiński practical-number theorem cannot be imported directly. Practicality obtains coverage using unrestricted small divisor coins, whereas every legal grouped coin exceeds \(2\sqrt M\). The explicit practical number \(Q_4\) demonstrates that this is not merely a technical mismatch.

**Precise block.**

No explicit infinite family \(M_r\) is known for which the grouped divisor coins hit \(M_r\) in a long interval of run-count layers. Proving such a theorem without specifying a special consecutive-divisor architecture would essentially restate the original problem in integer-coin language. A fresh Route-2 attempt should therefore engineer and recursively preserve many solutions of
\[
a(a+1)\mid M,
\]
while simultaneously proving exact target coverage and cardinality propagation.