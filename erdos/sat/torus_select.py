from sympy import primerange
from math import gcd

def factint(n):
    fs = set(); d = 2
    while d*d <= n:
        while n % d == 0: fs.add(d); n //= d
        d += 1
    if n > 1: fs.add(n)
    return fs

def order(a, n, p):
    o = n
    for q in factint(n):
        while o % q == 0 and pow(a, o // q, p) == 1:
            o //= q
    return o

def mass_for(A, B, pmax=2_000_000):
    tot = 0.0; cnt = 0; heavy = []
    for p in primerange(5, pmax):
        if pow(2, A, p) != 1: continue
        if pow(3, B, p) != 1: continue
        o2 = order(2, A, p); o3 = order(3, B, p)
        idx = o2 * o3 // gcd(o2, o3)
        tot += 1.0 / idx; cnt += 1
        if 1.0 / idx > 0.004:
            heavy.append((p, o2, o3, idx))
    return tot, cnt, heavy

cands = [(5040, 5040), (7920, 7920), (2520, 2520), (10080, 5040), (5040, 10080),
         (4620, 4620), (9240, 9240), (6300, 6300), (8316, 8316), (5544, 5544),
         (7560, 7560), (6930, 6930)]
for A, B in cands:
    tot, cnt, heavy = mass_for(A, B)
    print(f"A={A} B={B}: mass={tot:.4f} primes={cnt} cells={A*B/1e6:.1f}M")
