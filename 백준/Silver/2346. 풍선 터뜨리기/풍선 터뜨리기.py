from sys import stdin
from collections import deque

def order(n, move):
	
	result = [1]
	balloons = deque(range(2, n+1))
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