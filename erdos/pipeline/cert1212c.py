"""#1212 certificate search v3: per-column transfer relations, folded over
x = 0..M-1. T_x[d_in][d_out]=1 iff arriving at (d_in,x) admissible, climbing
[d_in..d_top] all admissible at x, exit E to d_out=d_top-1 (>=1).
Cycle exists iff the M-fold composition has d with R[d][d]=1.
Bitmask rows for speed. Then reconstruct the explicit path.
"""
import sys, json

def primes_of(n):
    ps = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: ps.append(n)
    return ps

def build_adm_col(x, M, Mp, dmax, dprimes):
    """bitmask of admissible d at column x (bit d-1)."""
    mask = 0
    for d in range(1, dmax + 1):
        bad = False
        for p in dprimes[d]:
            if x % p == 0:
                bad = True
                break
        if bad:
            continue
        if d % 2 == 0:
            ok = False
            for p in Mp:
                if x % p == 0 or (x + d) % p == 0:
                    ok = True
                    break
            if not ok:
                continue
        mask |= 1 << (d - 1)
    return mask

def transfer(admx, dmax):
    """T[d_in-1] = bitmask of possible d_out (climb then one E)."""
    T = [0] * dmax
    for din in range(1, dmax + 1):
        if not (admx >> (din - 1)) & 1:
            continue
        outs = 0
        dtop = din
        while True:
            # exit from dtop: d_out = dtop-1 >= 1
            if dtop - 1 >= 1:
                outs |= 1 << (dtop - 2)
            # extend climb
            if dtop + 1 <= dmax and (admx >> dtop) & 1:
                dtop += 1
            else:
                break
        T[din - 1] = outs
    return T

def compose(A, B, dmax):
    """C = A then B: C[i] = union of B[j] for j in A[i]."""
    C = [0] * dmax
    for i in range(dmax):
        a = A[i]
        c = 0
        while a:
            lb = a & -a
            j = lb.bit_length() - 1
            c |= B[j]
            a ^= lb
        C[i] = c
    return C

def run(M, dmax):
    Mp = primes_of(M)
    dprimes = {d: primes_of(d) for d in range(1, dmax + 1)}
    for d in range(1, dmax + 1):
        if not all(p in Mp for p in dprimes[d]):
            print(f"strip break at d={d} (prime not in M); effective dmax={d-1}")
            dmax = d - 1
            break
    I = [1 << i for i in range(dmax)]
    R = I[:]
    Ts = []
    for x in range(M):
        admx = build_adm_col(x, M, Mp, dmax, dprimes)
        T = transfer(admx, dmax)
        Ts.append(T)
        R = compose(R, T, dmax)
        if all(r == 0 for r in R):
            print(f"dead at column {x}: no surviving trajectories")
            return None
    hits = [d + 1 for d in range(dmax) if (R[d] >> d) & 1]
    print("fold complete; fixed-point d's:", hits)
    if not hits:
        return None
    # reconstruct: choose d0 = hits[0]; walk forward greedily maintaining
    # reachability-to-target via suffix products
    d0 = hits[0]
    suffix = [None] * (M + 1)
    suffix[M] = I[:]
    for x in range(M - 1, -1, -1):
        suffix[x] = compose(Ts[x], suffix[x + 1], dmax)
    path = []
    cur = d0
    for x in range(M):
        # choose climb top so that exit d_out can still reach d0 at end
        admx_T = Ts[x]
        outs = admx_T[cur - 1]
        # candidates d_out with (suffix[x+1])[d_out] ∋ d0
        chosen = None
        b = outs
        while b:
            lb = b & -b
            j = lb.bit_length() - 1
            if (suffix[x + 1][j] >> (d0 - 1)) & 1:
                chosen = j + 1
                break
            b ^= lb
        assert chosen is not None, (x, cur)
        # emit vertices: climb cur..chosen+1 at column x, then E
        dtop = chosen + 1
        for d in range(cur, dtop + 1):
            path.append((d, x))
        cur = chosen
    assert cur == d0
    return {"M": M, "dmax": dmax, "d0": d0, "path_dx": path}

if __name__ == "__main__":
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 30030
    dmax = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    res = run(M, dmax)
    if res:
        print(f"*** CYCLE FOUND *** M={res['M']} steps={len(res['path_dx'])}")
        json.dump(res, open(f"cert1212_path_M{res['M']}.json", "w"))
    else:
        print("no certificate at this (M, dmax)")
