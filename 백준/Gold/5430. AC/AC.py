import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):	
	command = input().strip().replace('RR', '')
	n = int(input())
	arr = deque(input().strip()[1:-1].split(','))
	r, b = 0, 0	# reverse, break
	
	if n == 0:
		arr = deque([])
		
	for c in command:
		if c == 'R':
			r += 1
			if r == 2:
				r = 0
		elif c == 'D':
			if arr:
				if r == 1:
					arr.pop()
				else:
					arr.popleft()
			else:
				b += 1
				print('error')
				break
	if arr:
		if r == 1:
			arr.reverse()
		print('['+ ','.join(arr) +']')
	else:
		if b == 0:
			print('[]')