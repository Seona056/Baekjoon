n = int(input())
m, a = 2, 2

if n == 0:
	print(4)
else:
	s = [a**i for i in range(n)]
	print((m+sum(s))**2)