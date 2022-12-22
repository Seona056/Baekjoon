def f_count(num, d=2):
	if num < d:
		return 0
	c = 0
	while num >= d:
		c += num // d
		num //= d
	return c

import sys
n, m = map(int, sys.stdin.readline().split())	
	
t = f_count(n) - f_count(m) - f_count(n-m)
f = f_count(n, 5) - f_count(m, 5) - f_count(n-m, 5)
print(min(t, f))