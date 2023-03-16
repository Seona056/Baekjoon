def get_prime(n):
	prime = [1]*(n+1)
	
	for i in range(2, int(n**0.5)+1):
		if prime[i]:
			j = 2
			while i*j <= n:
				prime[i*j] = 0
				j += 1
	return prime
	
nums = list(map(int, open(0).readlines()[1:]))
prime = get_prime(max(nums))

for n in nums:
	i, c = 2, 0
	while i <= n//2:
		if prime[i] and prime[n-i]:
			c += 1
		i += 1
	print(c)