import sys

a, b, c, = map(int, sys.stdin.readline().split())

if b >= c:         # 가변비용 b보다 c가 크면 절대 고정비용이 줄지 않음
    print(-1)
else:
    print(a//(c-b)+1)