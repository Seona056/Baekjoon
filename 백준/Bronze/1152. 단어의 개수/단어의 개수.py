import sys

s = sys.stdin.read().strip()   # 양쪽 끝의 공백 제거

if s == '':
    print(0)
else:
    print(s.count(' ')+1)