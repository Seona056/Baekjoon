import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):	
	command = input().strip().replace('RR', '')	# 👉 'RR'은 원래대로 돌아오므로 공백으로 치환한다. 
	n = int(input())
	arr = deque(input().strip()[1:-1].split(','))
	r, b = 0, 0	# reverse, break	# 👉 break 변수를 꼭 만들어 둘 것!
	
	if n == 0:
		arr = deque([])
		
	for c in command:
		if c == 'R':	# 👉 하나하나 reverse를 붙였더니 시간 초과가 뜸
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
				b += 1	# 👉 break로 command for문이 끝났음을 표시한다.
				print('error')
				break
	if arr:
		if r == 1:
			arr.reverse()
		print('['+ ','.join(arr) +']')
	else:
		if b == 0:	# 👉 그냥 if문을 쓰면 break가 걸리지 않은 모든 출력에 대해 '[]'가 붙으므로 반드시 else문 안에 넣는다.
			print('[]')
