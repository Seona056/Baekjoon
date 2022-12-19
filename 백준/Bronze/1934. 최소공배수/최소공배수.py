import sys
import math

for t in sys.stdin.readlines()[1:]:
	a, b = map(int, t.split())
	print(math.lcm(a,b))