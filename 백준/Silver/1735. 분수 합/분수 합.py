import sys
from fractions import Fraction

input = sys.stdin.readline
f = 0
for i in range(2):
	a, b = map(int, input().split())
	f += Fraction(a, b)
print(f.numerator, f.denominator)