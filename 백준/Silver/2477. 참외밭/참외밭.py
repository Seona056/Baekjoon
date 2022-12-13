import sys

input = sys.stdin.readline
k = int(input())
direct, m = [], [] 

for _ in range(6):
	a, b = map(int, input().split())
	direct.append(a)
	m.append(b)

total, extra = 1, 1

for i in range(4):
	if direct.count(i+1) == 1:
		idx = direct.index(i+1)
		total *= m[idx]
		if idx >= 3:
			extra *= m[abs(3-idx)]
		else:
			extra *= m[idx+3]
			
print(k*(total-extra))