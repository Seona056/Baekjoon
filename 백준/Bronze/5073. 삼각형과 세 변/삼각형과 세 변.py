tri = open(0).readlines()[:-1]
for t in tri:
	a, b, c = map(int, t.split())
	m = max(a, b, c)
	t = len({a,b,c})
	if m >= a+b+c-m:
		print('Invalid')
	else:
		if t == 1:
			print('Equilateral')
		elif t == 2:
			print('Isosceles')
		elif t == 3:
			print('Scalene')