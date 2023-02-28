import sys
n, m = input().split()
basket = list(range(1, int(n)+1))
case = sys.stdin.readlines()

for c in case:
	i, j = map(int, c.split())
	i2, j2 = basket[i-1] , basket[j-1]
	basket[i-1] = j2
	basket[j-1] = i2

print(' '.join(str(b) for b in basket))