# 첫 번째 답
# 메모리: 143400 KB, 시간: 2060 ms
# [1920] 수 찾기, [1654] 랜선 자르기와 동일한 방식으로 풀이

def get_m(m, first, end):
	if first > end:
		return end
	
	mid = (first+end)//2
	left = sum([t-mid for t in trees if t>mid])
	
	if left >= m:
		return get_m(m, mid+1, end)
	else:
		return get_m(m, first, mid-1)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(get_m(m, 0, max(trees)))


---------------------------------------------------------------
# 두 번째 답
# 메모리: 143400 KB, 시간: 2048 ms
# sum()을 실행할 때, sum 괄호 안에 이터레이터가 있지 않아도 된다. 컴프리헨션 사용가능
# 메모리 소요량은 같았지만 시간은 살~~짝 빨리짐

def get_m(m, first, end):
	if first > end:
		return end
	
	mid = (first+end)//2
	left = sum(t-mid for t in trees if t>mid)	# sum(컴프리헨션 사용 가능)
	
	if left >= m:
		return get_m(m, mid+1, end)
	else:
		return get_m(m, first, mid-1)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(get_m(m, 0, max(trees)))


---------------------------------------------------------------
# 세 번째 답
# 메모리: 114800 KB, 시간: 420 ms
# trees 리스트가 아닌 Counter로 만들어서 같은 길이의 나무들의 절단 연산을 줄여준다.

import sys
from collections import Counter
input = sys.stdin.readline

def get_m(m, first, end):
	if first > end:
		return end
	
	mid = (first+end)//2
	left = sum((t-mid)*i for t, i in trees.items() if t>mid)	# 연산할 때는 trees.items()를 사용하여 한 번에 여러 개의 나무 절단 연산을 완료한다.
	
	if left >= m:
		return get_m(m, mid+1, end)
	else:
		return get_m(m, first, mid-1)

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))		# Counter로 trees를 만든다.
print(get_m(m, 0, max(trees)))
