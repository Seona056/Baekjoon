import sys
input = sys.stdin.readlines

num = list(map(int, input()))
num = sorted(num[1:])

for n in num:
    print(n)