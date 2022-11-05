# 첫 번째 답
# 메모리: 43908 KB, 시간: 312 ms

import sys
input = sys.stdin.readline
coordinates = []

for i in range(int(input())):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates.sort()
for c in coordinates:
    print(*c)


# 두 번째 답
# 메모리: 43332 KB, 시간: 184 ms

import sys

def sort_num(n):
    x, y = n.split()
    return int(x) + int(y)/1000000   # 100,000 최고 입력값이므로, 나눴을 때 1 이하가 되도록 0을 하나 더 붙여준다.

coordinates = sys.stdin.readlines()[1:]
coordinates.sort(key=lambda n: sort_num(n))
print(''.join(coordinates))
