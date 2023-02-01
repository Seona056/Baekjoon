import sys
import collections

command = sys.stdin.readlines()[1:]
q = collections.deque([])

for c in command:
	c = c.rstrip()
	
	if ' ' in c:
		x = c.split()
		q.append(x[1])
	elif 'pop' == c:
		if q:
			print(q.popleft())
		else:
			print(-1)
	elif 'size' == c:
		print(len(q))
	elif 'empty' == c:
		if q:
			print(0)
		else:
			print(1)
	elif 'front' == c:
		if q:
			print(q[0])
		else:
			print(-1)
	elif 'back' == c:
		if q:
			print(q[-1])
		else:
			print(-1)