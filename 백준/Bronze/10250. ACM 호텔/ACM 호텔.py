import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())

    if n % h == 0:
        print(int(str(h)+str(n//h).zfill(2)))
    else:
        print(int(str(n%h)+str(n//h+1).zfill(2)))