import sys
import math

n = int(input())
trees = list(map(int, sys.stdin.readlines()))
gap = []

for i in range(n-1):
	gap.append(trees[i+1] - trees[i])
	
m, c = math.gcd(*gap), 0

for g in gap:
	if g == m:
		continue
	elif g > m:
		c += g//m - 1
		
print(c)