n = int(input())
m, a = 3, 1

if n == 0:
	print(4)
elif n == 1:
	print(9)
else:
	for i in range(n-1):
		a += a
		m += a
	print(m**2)