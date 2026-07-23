"""#1212: BFS in the near-diagonal band |y-x|<=B, x,y>=2, admissible vertices:
gcd=1, not both prime, both>1. Check flow to large x and measure bottlenecks."""
from math import gcd
from collections import deque
import sys
from sympy import isprime

B = int(sys.argv[1]) if len(sys.argv) > 1 else 8
XMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300000

def adm(x, y):
    if x < 2 or y < 2: return False
    if abs(y - x) > B: return False
    if gcd(x, y) != 1: return False
    if isprime(x) and isprime(y): return False
    return True

start = (899, 900)

seen = {start}
dq = deque([start])
maxx = 0
far = None
while dq:
    v = dq.popleft()
    x, y = v
    if x > maxx:
        maxx = x; far = v
    if x >= XMAX:
        print(f"REACHED x={x} at {v}")
        break
    for w in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if w not in seen and adm(*w):
            seen.add(w); dq.append(w)
print("band B =", B, "max x reached:", maxx, "at", far, "visited:", len(seen))
