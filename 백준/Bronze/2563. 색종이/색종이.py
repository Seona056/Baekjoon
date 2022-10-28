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