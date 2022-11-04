import sys
input = sys.stdin.readlines

num = list(map(int, input()))
print(sum(num)//len(num))

num.sort()
print(num[len(num)//2])