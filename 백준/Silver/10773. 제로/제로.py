import sys
test = map(int, sys.stdin.readlines()[1:])
answer = []

for t in test:
	if t == 0:
		answer.pop()
	else:
		answer.append(t)
		
print(sum(answer))