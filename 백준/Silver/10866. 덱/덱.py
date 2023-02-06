import sys
from collections import deque

command = sys.stdin.readlines()[1:]
d = deque([])

for c in command:
	c = c.strip()
	
	if ' ' in c:
		temp, x = c.split()
		
		if temp == 'push_front':
			d.appendleft(x)
		elif temp == 'push_back':
			d.append(x)
	elif c == 'empty':
		if d:
			print(0)
		else:
			print(1)
	elif c == 'size':
		print(len(d))
	else:
		if d:
			if c == 'pop_front':
				print(d.popleft())
			elif c == 'pop_back':
				print(d.pop())
			elif c == 'front':
				print(d[0])
			elif c == 'back':
				print(d[-1])
		else:
			print(-1)