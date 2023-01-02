# 첫 번째 답
# 메모리: 30616 KB, 시간: 36 ms
# 제일 단순한 방법으로 l, r을 차례로 카운팅하다가 r이 많아지는 시점에서 break하고 출력
# 생각보다 중간에 break를 걸어놔서 그런지 시간이 오래걸리지 않았음 (정답 랭킹 7위)

import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	l, r = 0, 0
	
	for i in v:
		if i == '(':
			if l >= r:
				l += 1
			else:
				l += 1
				break
		else:
			if l > r:
				r += 1
			else:
				r += 1
				break
	
	if l == r:
		print('YES')
	else:
		print('NO')

		
----------------------------------------------------------
# 두 번째 답
# 메모리: 30616 KB, 시간: 36 ms
# 다른 답을 참고하여 내 스타일대로 코딩
# '()'를 삭제하고 남은 것이 있다면 'NO'를, 없으면 'YES'를 출력하는 아이디어
# 코드길이: 162 B 👉 현재 정답 랭킹 1위 (가장 짧은 코드)

import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	while '()' in v:
		v = v.replace('()', '')
	
	if v:
		print('NO')
	else:
		print('YES')
