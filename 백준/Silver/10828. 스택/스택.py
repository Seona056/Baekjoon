import sys
command = sys.stdin.readlines()[1:]
stack = []

for c in command:
	c = c.rstrip()
	if ' ' in c:
		x = c.split()
		stack.append(int(x[1]))
	elif 'pop' == c:
		if len(stack) == 0:
			print(-1)
		else:
			print(stack.pop())
	elif 'size' == c:
		print(len(stack))
	elif 'empty' == c:
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif 'top' == c:
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])