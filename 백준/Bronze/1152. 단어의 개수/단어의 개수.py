# 첫 번째 답
# 메모리: 32796 KB, 시간: 80 ms

import sys

s = list(sys.stdin.readline().split())
print(len(s))


# 두 번째 답
# 메모리: 32796 KB, 시간: 72 ms
# strip()을 사용하여 공백 제거
# len()보다 count()를 사용하는 것이 더 빨랐다.

import sys

s = sys.stdin.read().strip()   # 양쪽 끝의 공백 제거

if s == '':
    print(0)
else:
    print(s.count(' ')+1)
