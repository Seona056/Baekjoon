import sys
input = sys.stdin.readlines

num = list(map(int, input()))
num = sorted(num[1:])

print('\n'.join(map(str,num)))