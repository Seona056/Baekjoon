from collections import deque

n, k = map(int, input().split())
circle = deque(range(1, n+1))
a = deque([])	# answer

while len(a) != n:
	
	for i in range(k):
		temp_c = circle.popleft()
		if i+1 < k:
			circle.append(temp_c)
		else:
			a.append(temp_c)
			
print('<'+ ', '.join(map(str, a)) +'>')