import sys
n, m = sys.stdin.readline().split()
basket = [0]*int(n)
case = sys.stdin.readlines()

for c in case:
	i, j, k = map(int, c.split())
	basket[i-1:j] = [k]*(j-i+1)

print(' '.join(str(b) for b in basket))