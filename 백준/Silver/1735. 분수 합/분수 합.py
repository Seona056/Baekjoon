# 메모리: 39568 KB, 시간: 124 ms
# fractions 모듈 사용 👉 Fraction(x, y) : 분수 x/y의 기약 분수를 반환한다.
# (x/y).numerator : 분모
# (x/y).denominator : 분자

import sys
from fractions import Fraction

input = sys.stdin.readline
f = 0
for i in range(2):
	a, b = map(int, input().split())
	f += Fraction(a, b)
print(f.numerator, f.denominator)
