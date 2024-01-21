from collections import deque

command = open(0).readlines()[1:]
d = deque([])

for c in command:
	c = c.split()
	if c[0] == '1':
		d.appendleft(int(c[-1]))
	elif c[0] == '2':
		d.append(int(c[-1]))
	elif c[0] == '3':
		print(d.popleft() if d else -1)
	elif c[0] == '4':
		print(d.pop() if d else -1)
	elif c[0]== '5':
		print(len(d))
	elif c[0] == '6':
		print(0 if d else 1)
	elif c[0] == '7':
		print(d[0] if d else -1)
	elif c[0] == '8':
		print(d[-1] if d else -1)