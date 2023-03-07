n, k = map(int, input().split())
i, c = 1, 0

while i <= n:
	if n % i == 0:
		c += 1
	if c == k:
		print(i)
		break
	i += 1

if c < k:
	print(0)