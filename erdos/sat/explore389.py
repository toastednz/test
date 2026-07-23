"""Erdos #389: minimal k(n) with n(n+1)...(n+k-1) | (n+k)...(n+2k-1),
i.e. R(n,k) = (n+2k-1)!(n-1)!/((n+k-1)!)^2 in Z.
v_p(R) = sum_i floor((n+2k-1)/p^i) + floor((n-1)/p^i) - 2*floor((n+k-1)/p^i).
Compute minimal k for n up to N, k up to KMAX."""
import sys
from sympy import primerange

N = int(sys.argv[1]) if len(sys.argv) > 1 else 80
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000

def ok(n, k):
    top = n + 2 * k - 1
    for p in primerange(2, top + 1):
        if p > top:
            break
        v = 0
        pi = p
        while pi <= top:
            v += (top // pi) + ((n - 1) // pi) - 2 * ((n + k - 1) // pi)
            pi *= p
        if v < 0:
            return False
    return True

def ok_fast(n, k):
    # quick necessary checks with small primes first
    top = n + 2 * k - 1
    for p in (2, 3, 5, 7, 11, 13):
        if p > top: break
        v = 0
        pi = p
        while pi <= top:
            v += (top // pi) + ((n - 1) // pi) - 2 * ((n + k - 1) // pi)
            pi *= p
        if v < 0:
            return False
    return ok(n, k)

for n in range(1, N + 1):
    found = None
    for k in range(1, KMAX):
        if ok_fast(n, k):
            found = k
            break
    print(n, found, flush=True)
