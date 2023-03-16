def get_prime(n):
	prime = [1]*(n+1)
	prime[4::2] = [0]*(n//2-1)
	
	for i in range(3, int(n**0.5)+1, 2):
		prime[2*i::i] = [0]*(n//i-1)
	
	prime_2 = [2]+[i for i in range(3, n+1, 2) if prime[i]]
	return prime, prime_2
	
nums = list(map(int, open(0).readlines()[1:]))
prime, prime_2 = get_prime(max(nums))

for n in nums:
	c = 0
	for p in prime_2:
		if p > (n//2):
			print(c)
			break
		if prime[n-p]:
			c += 1