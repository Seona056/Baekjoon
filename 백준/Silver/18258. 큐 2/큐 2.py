# 최종 답
# 메모리: 317692 KB, 시간: 1556 ms
# 원래는 q = [] (일반 리스트), pop(0)을 사용 👉 시간 초과
# import collectios로 deque을 사용한 것만으로도 시간 초과가 되지 않음

import sys
import collections

command = sys.stdin.readlines()[1:]
q = collections.deque([])

for c in command:
	c = c.rstrip()
	
	if ' ' in c:
		x = c.split()
		q.append(x[1])    # 👉 deque에서는 appendleft()도 제공되므로 참고
	elif 'pop' == c:
		if q:
			print(q.popleft())    # 👉 deque에서는 popleft(), pop() 모두 제공된다.
		else:
			print(-1)
	elif 'size' == c:
		print(len(q))
	elif 'empty' == c:
		if q:
			print(0)
		else:
			print(1)
	elif 'front' == c:
		if q:
			print(q[0])
		else:
			print(-1)
	elif 'back' == c:
		if q:
			print(q[-1])
		else:
			print(-1)
