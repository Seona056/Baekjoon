# 첫 번째 답
# 시간 초과
# groupby를 사용하여 zero, c 리스트에 저장하여 답을 도출

import sys
from math import factorial as f
from itertools import groupby
n, k = map(int, sys.stdin.readline().split())

zero, c = [], []
for a, b in groupby(str(f(n)//(f(k)*f(n-k)))):
	zero.append(a)
	c.append(len(list(b)))
	
if zero[-1] == '0':
	print(c[-1])
else:
	print(0)

	
----------------------------------------------------------
# 두 번째 답
# 시간 초과
# 첫 번째 답이 시간초과가 나서 딕셔너리를 활용함

import sys
from math import factorial as f
from itertools import groupby
n, k = map(int, sys.stdin.readline().split())
s = str(f(n)//(f(k)*f(n-k)))

if s[-1] == '0':
	c = {a:len(list(b)) for a, b in groupby(s) if a == '0'}
	print(c['0'])
else:
	print(0)
	

----------------------------------------------------------
# 세 번째 답
# 시간 초과
# 딕셔너리도 시간초과가 나서 groupby를 for문으로 돌리는 횟수를 줄여보고자 함

import sys
from math import factorial as f
from itertools import groupby
n, k = map(int, sys.stdin.readline().split())
s = str(f(n)//(f(k)*f(n-k)))[::-1]

if s[0] == '0':
	for a, b in groupby(s):
		if a == '0':
			print(len(list(b)))
		else:
			break
else:
	print(0)
	
	
----------------------------------------------------------
# 네 번째 답
# 메모리: 30748 KB, 시간: 36 ms
# 블로그를 참고 : 팩토리얼로 풀면 무조건 시간 초과가 난다고 함.
# 주어진 두 수를 소인수분해를 해서 2와 5의 지수를 이용하여 푸는 방법
# 자연수 n의 팩토리얼의 소인수 a의 지수를 구하는 방법을 f_count 함수로 구현 (사실 이해는 잘 안되지만 공식이라고 하니...)

def f_count(num, d=2):
	if num < d:
		return 0
	c = 0
	while num >= d:
		c += num // d
		num //= d
	return c

import sys
n, m = map(int, sys.stdin.readline().split())	
	
t = f_count(n) - f_count(m) - f_count(n-m)
f = f_count(n, 5) - f_count(m, 5) - f_count(n-m, 5)
print(min(t, f))
