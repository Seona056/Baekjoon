# 여러 시도만에 겨우 성공
# 처음에 짠 코드가 거의 맞았으나, 마지막 디테일이 부족했음
# 빈 arr도 join문으로 표기가 될 줄알고 그냥 뒀던 것이 계속 오답이 되었다.
# 그리고 처음에 reverse를 하나하나 했더니, command와 n의 길이가 너무 길어서 시간초과가 떴다. (1 <= command <= 100,000 / 0 <= n <= 100,000)
# break문으로 'error'를 출력하고 마친 것과, command를 정상적으로 실행하고 빈 arr가 되는 것의 구분이 필요했음!
# ❗ 디테일이 중요 ❗

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
