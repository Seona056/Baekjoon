import sys
sequence = map(int, sys.stdin.readlines()[1:])
stack, answer = [], []
temp = 1

for s in sequence:
	while temp <= s:
		stack.append(temp)
		answer.append('+')
		temp += 1
	if stack[-1] == s:
		stack.pop()
		answer.append('-')
	else:
		print('NO')
		answer = 0
		break

if answer:
	print('\n'.join(answer))