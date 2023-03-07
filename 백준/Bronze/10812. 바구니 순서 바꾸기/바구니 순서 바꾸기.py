import sys
input = sys.stdin.readline
n, m = map(int, input().split())
basket = list(range(0, n+1))

for i in range(m):
	b, e, mid = map(int, input().split())
	for t in basket[b:mid]:
		e += 1
		basket.insert(e, t)
	del basket[b:mid]

print(' '.join(map(str, basket[1:])))