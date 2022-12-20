import sys
from math import factorial as f

test = sys.stdin.readlines()[1:]

for t in test:
	k, n = map(int, t.split())    # k <= n
	print(f(n)//(f(k)*f(n-k)))