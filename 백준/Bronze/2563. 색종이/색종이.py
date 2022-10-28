# 첫 번째 답
# 메모리: 30840 KB, 시간: 72 ms

import sys

input = sys.stdin.readline

n = int(input())
paper = [tuple(map(int, input().split())) for _ in range(n)]
max_x = max(paper, key=lambda x: x[0])[0]
max_y = max(paper, key=lambda y: y[1])[1]
area = [(max_x+10)*[0] for _ in range(max_y+10)]

for p in paper:
    x, y = p[0]-1, p[1]-1
    for i in range(y, y+10):
        area[i][x:x+10] = [1]*10

black = 0
for a in area:
    black += a.count(1)

print(black)


# 두 번째 답
# 메모리: 30840 KB, 시간: 72 ms

import sys

input = sys.stdin.readline

n = int(input())
X, Y = [], []

for _ in range(n):
    a, b = map(int, input().split())
    X.append(a)
    Y.append(b)

area = [(max(X)+10)*[0] for _ in range(max(Y)+10)]

for x, y in zip(X, Y):
    x, y = x-1, y-1
    for i in range(y, y+10):
        area[i][x:x+10] = [1]*10

black = 0
for a in area:
    black += a.count(1)

print(black)


# 세 번째 답
# 메모리: 30840 KB, 시간: 72 ms

import sys

input = sys.stdin.readline

n = int(input())
area = [[0]*100 for _ in range(100)]
paper = [tuple(map(int, input().split())) for _ in range(n)]

for p in paper:
    x, y = p[0]-1, p[1]-1
    for i in range(y, y+10):
        area[i][x:x+10] = [1]*10

black = 0
for a in area:
    black += a.count(1)

print(black)
