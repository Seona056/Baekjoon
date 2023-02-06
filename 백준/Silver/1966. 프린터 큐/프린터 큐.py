import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
	n, t = map(int, input().split())	# target
	p = deque(map(int, input().split()))	# prior
	d = deque(range(n))	# document index
	a = 0	# answer
	
	while True:
		m = max(p)
		temp_p = p.popleft()
		temp_i = d.popleft()
		
		if temp_p == m:
			a += 1
			if temp_i == t:
				break
			else:
				continue
		else:
			p.append(temp_p)
			d.append(temp_i)	
	print(a)