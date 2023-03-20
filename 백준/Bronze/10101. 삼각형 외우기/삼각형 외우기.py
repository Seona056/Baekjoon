a, b, c = map(int, open(0).read().split())

if a+b+c == 180:
	tri = len({a,b,c})
	if tri == 1:
		print('Equilateral')
	elif tri == 2:
		print('Isosceles')
	else:
		print('Scalene')
else:
	print('Error')