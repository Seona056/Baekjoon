import math

a, b, v = map(int, input().split())

v = v - a
answer = math.ceil(v/(a-b))
print(answer+1)