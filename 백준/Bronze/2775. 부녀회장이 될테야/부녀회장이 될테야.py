import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    f = int(input())   # floor
    r = int(input())   # room
    
    if f == 0:
        print(r)
    else:
        apart = list(_ for _ in range(1, r+1))
        for i in range(f):
            floor = []
            for j in range(1, r+1):
                  floor.append(sum(apart[:j]))
            apart = floor
        print(apart[-1])