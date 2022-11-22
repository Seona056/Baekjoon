import sys

board = sys.stdin.readlines()
n, m = map(int, board[0].split())
board = list(map(lambda x: x.rstrip(),board[1:]))
color_count = []



for a in range(n-7):
    for b in range(m-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        color_count.append(min(index1, index2))

print(min(color_count))