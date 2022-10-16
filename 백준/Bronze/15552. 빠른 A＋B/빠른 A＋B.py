import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip('\n').split())
    print(a+b)