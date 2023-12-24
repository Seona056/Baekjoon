from sys import stdin

command = stdin.readlines()[1:]
stack = []

for c in command:
	if c[0] == '1':
		_, x = map(int, c.split())
		stack.append(x)
	elif c[0] == '2':
		if stack:
			print(stack.pop())
		else:
			print(-1)
	elif c[0] == '3':
		print(len(stack))
	elif c[0] == '4':
		if stack:
			print(0)
		else:
			print(1)
	elif c[0] == '5':
		if stack:
			print(stack[-1])
		else:
			print(-1)