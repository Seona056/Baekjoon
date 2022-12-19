import sys
import math

cir = sys.stdin.readlines()
n = int(cir[0]) 
cir = list(map(int, cir[1].split()))

for c in cir[1:]:
	g = math.gcd(cir[0], c)
	print(f'{cir[0]//g}/{c//g}')