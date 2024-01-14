# 내가 푼 답
# 메모리 : 34068KB, 시간 : 60ms
# collections 모듈의 deque을 사용
# rotate를 사용해서 풀려고 했는데, 헷갈려서... Chat GPT 풀이와 섞음
# index용 deque을 하나 더 만들어서 같이 rotate 시킴
# rotate에서 헷갈렸던 부분은 일반적으로 rotate 메서드에서 사용하는 방향과 문제에서 제시하는 방향이 달랐음
# ⭐ 문제 : 양수일 경우 오른쪽으로, 음수일 경우 왼쪽으로 이동 ➡️ deque의 회전 방향은 반대

from sys import stdin
from collections import deque

def order(n, move):
	
	result = [1]
	balloons = deque(range(2, n+1))      # idx용 deque
	m, move = move[0], deque(move[1:])
	
	for i in range(n-1):
		if m > 0 :
			balloons.rotate(-(m-1))
			move.rotate(-(m-1))
		else:
			balloons.rotate(-m)
			move.rotate(-m)
		
		m = move.popleft()
		result.append(balloons.popleft())
		
	return result
	
	
input = stdin.readline

n = int(input())
move = list(map(int, input().split()))

print(' '.join(str(r) for r in order(n, move)))



----------------------------------------------------------------
# 가장 빠른 답
# 메모리 : 31120KB, 시간 : 40ms
# 그냥 읽어보고 넘어가려고 했는데, 잘 이해가 안되는 부분이 있어서 따라서 써봄


def main():
	count = int(input())
	balloons = [(i+1, delta) for i, delta in enumerate(map(int, input().split()))]
	
	i = 0
	while balloons:
		index, delta = balloons.pop(i)
		
		print(index, end=' ')
		count -= 1    # ⭐ pop을 사용해서 list 요소가 줄어들기 때문에 -1을 해준다.
		
		if not count:
			break
		
		if delta > 0:
			delta -= 1
		i += delta
		i %= count     # ⭐ i + delta는 pop을 반영하지 않으므로, -1길이로 줄어든 count로 나눈 나머지를 i로 재할당한다.
		

if __name__ == '__main__':
	main()
