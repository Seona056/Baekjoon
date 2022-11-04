# 첫 번째 답
# 메모리: 30840 KB, 시간: 9124 ms

import sys
input = sys.stdin.readline

t = int(input())
check = [0]*10001   # index 0은 사용 x (1~10000)

for i in range(t):
    n = int(input())
    check[n] += 1   # n-1의 카운트를 올리면 index값이 n과 달라짐
    
for x in range(10001):
    if check[x] != 0:
        for y in range(check[x]):
            print(x)


# 두 번째 답
# 메모리: 30840 KB, 시간: 8756 ms
# 가장 빠른 답을 참고한 코드

import sys
input = sys.stdin.buffer.readline

check = [0]*10001   # index 0은 사용x (1~10000)

for i in range(int(input())):
    check[int(input())] += 1

for x in range(10001):
    if check[x] != 0:
        for y in range(check[x]):
            print(x)
