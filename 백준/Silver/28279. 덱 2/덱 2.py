from collections import deque

command = open(0).readlines()[1:]
d = deque([])

for c in command:
	c = c.rstrip()
	
	if c[0] == '1':
		c, x = map(int, c.split())
		d.appendleft(x)
	elif c[0] == '2':
		c, x = map(int, c.split())
		d.append(x)
	elif c[0] == '3':
		if d:
			print(d.popleft())
		else:
			print(-1)
	elif c[0] == '4':
		if d:
			print(d.pop())
		else:
			print(-1)
	elif c[0] == '5':
		print(len(d))
	elif c[0] == '6':
		if d:
			print(0)
		else:
			print(1)
	elif c[0] == '7':
		if d:
			print(d[0])
		else:
			print(-1)
	elif c[0] == '8':
		if d:
			print(d[-1])
		else:
			print(-1)