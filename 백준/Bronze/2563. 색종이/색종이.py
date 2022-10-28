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