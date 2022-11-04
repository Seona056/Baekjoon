import sys
input = sys.stdin.readline

t = int(input())
check = [0]*10001   # index 0은 사용 x

for i in range(t):
    n = int(input())
    check[n] += 1   # n-1의 카운트를 올리면 index값이 n과 달라짐
    
for x in range(10001):
    if check[x] != 0:
        for y in range(check[x]):
            print(x)