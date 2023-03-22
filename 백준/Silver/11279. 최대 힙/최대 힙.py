# 첫 번째 답
# 힙에 대해 아직 공부하기 전이라, sort를 사용하여 풀었더니 시간 초과

arr = []

for x in open(0).read().split()[1:]:
	x = int(x)
	
	if x == 0:
		if arr:
			print(arr.pop())
		else:
			print(0)
		continue
	arr.append(x)
	arr.sort()


------------------------------------------------------------
# 두 번째 답
# 메모리: 44020 KB, 시간: 116 ms
# ⭐ 가장 빠른 답
# heapq 라이브러리에서 제공하는 메서드들은 최소 힙만 지원하므로, 최대 힙을 위해서는 x를 음수로 변환하여 heapq.heappush(리스트, 요소)한다.
# heapq.heappop(리스트)으로 꺼낼 때도 다시 -1을 곱해주어 양수로 만들어 준다.

import heapq

arr = []

for x in open(0).read().split()[1:]:
	x = int(x)
	
	if x == 0:
		if arr:
			print(-1 * heapq.heappop(arr))
		else:
			print(0)
		continue
	heapq.heappush(arr, -x)
	
	
------------------------------------------------------------
# 세 번째 답
# 메모리: 37180 KB, 시간: 120 ms
# for 문을 돌면서 바로바로 입력 받는 것이 메모리가 적게 들 것 같아서 바꾸어 봄
# 메모리 소모는 적게 되었는데, 시간이 조금 늘어남

import sys, heapq

input = sys.stdin.readline
arr = []

for x in range(int(input())):
	x = int(input())
	
	if x == 0:
		if arr:
			print(-1 * heapq.heappop(arr))
		else:
			print(0)
		continue
	heapq.heappush(arr, -x)
