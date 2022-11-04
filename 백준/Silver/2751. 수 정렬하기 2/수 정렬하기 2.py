import sys
input = sys.stdin.readlines

num = list(map(int, input()))
num = sorted(num[1:])

print('\n'.join(map(str,num)))   # '구분자'.join(리스트) : 리스트의 요소는 문자열이어야 한다. 👉 하나의 문자열로 반환
