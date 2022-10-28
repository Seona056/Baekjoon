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