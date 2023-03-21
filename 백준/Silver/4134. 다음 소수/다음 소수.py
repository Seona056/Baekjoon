import sys
input =  sys.stdin.readline

def is_prime(n):
	if n == 0 or n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

T = int(input())
for t in range(T):
	n = int(input())
	while True:
		if is_prime(n):
			print(n)
			break
		else:
			n += 1