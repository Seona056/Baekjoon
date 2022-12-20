# from itertools import groupby를 사용하면 연속된 문자열 그룹을 구할 수 있다.
# for a, b in groupby('012300000')
# 👉 a는 해당 문자 : 0
# 👉 b는 : <itertools._grouper object at 0x14b4081201f0>
# 👉 b를 리스트로 변환 : list(b) = ['0', '0', '0', '0', '0']

from math import factorial as f
from itertools import groupby

zero, c = [], []
for a, b in groupby(str(f(int(input())))):
	zero.append(a)
	c.append(len(list(b)))

if zero[-1] == '0':
	print(c[-1])
else:
	print(0)
