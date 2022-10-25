import math

a, b, v = map(int, input().split())

v = v - a
answer = math.ceil(v/(a-b))   # math.ceil() 올림 :소숫점 수가 나와도 하루에 올라간 높이로 포함
print(answer+1)
