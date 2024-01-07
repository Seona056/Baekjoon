import sys

test = map(int, sys.stdin.readlines()[1:])

for t in test:
	q = t//25 
	t %= 25
	
	d = t//10
	t %= 10
	
	n = t//5
	t %= 5
	
	print(q, d, n, t)