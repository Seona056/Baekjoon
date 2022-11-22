# 블로그 검색을 한 답
# 내가 짠 코드와 거의 비슷했지만, 크로스로 검증하는 코드에서 제대로 되지 않았다...
# if (a+b) % 2 != 0 이라는 마법의 코드를 배웠다고 생각하자...

import sys

board = sys.stdin.readlines()
n, m = map(int, board[0].split())
board = list(map(lambda x: x.rstrip(), board[1:]))
color_count = []

color_count = []

for i in range(n-7):
	for j in range(m-7):
		c_white, c_black = 0, 0
        
		for a in range(i, i+8):
			for b in range(j, j+8):
				if (a+b) % 2 == 0:                  # 이 조건문으로 각 배열이 두 칸씩, 다음 줄은 크로스로 두 칸씩 검사
					if board[a][b] != 'W':
						c_white += 1
					elif board[a][b] != 'B':
						c_black += 1
				else:
					if board[a][b] != 'B':
						c_white += 1
					elif board[a][b] != 'W':
						c_black += 1
		color_count.append(min(c_white, c_black))

print(min(color_count))
