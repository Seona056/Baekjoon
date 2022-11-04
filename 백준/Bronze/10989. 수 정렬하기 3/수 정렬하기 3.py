import sys
input = sys.stdin.buffer.readline

check = [0]*10001   # index 0은 사용x (1~10000)

for i in range(int(input())):
    check[int(input())] += 1

for x in range(10001):
    if check[x] != 0:
        for y in range(check[x]):
            print(x)