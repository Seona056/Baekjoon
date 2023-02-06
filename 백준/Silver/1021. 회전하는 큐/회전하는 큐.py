import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
d = deque(range(1, n+1))
pop_num = deque(map(int, input().split()))
c = 0	# count

for p in pop_num:
	
	while p in d:
		if p == d[0]:
			d.popleft()
		else:
			i = d.index(p)
			
			if i <= (len(d)//2):
				d.rotate(-i)
				d.popleft()
				c += i
			else:
				i = len(d) - i
				d.rotate(i)
				d.popleft()
				c += i
print(c)