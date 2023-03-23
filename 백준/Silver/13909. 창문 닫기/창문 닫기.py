def window(n):
	if n == 1 or n == 2:
		return 1
	
	i, c = 1, 3
	while n > c:
		if n-c > 0:
			i += 1
			n -= c
			c += 2
	return i
	
print(window(int(input())))