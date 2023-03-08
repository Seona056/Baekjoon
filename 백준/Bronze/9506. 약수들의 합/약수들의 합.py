import sys
nums = sys.stdin.readlines()[:-1]

for n in nums:
	n = int(n)
	factors = [1]
	i = 2
	while i < (n**0.5):
		if n % i == 0:
			factors.append(i)
			factors.append(n//i)
		i += 1
	if n == sum(factors):
		print(f'{n} = ' + ' + '.join(map(str, sorted(factors))))
	else:
		print(f'{n} is NOT perfect.')