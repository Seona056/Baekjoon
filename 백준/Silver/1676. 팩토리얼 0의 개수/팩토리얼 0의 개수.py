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