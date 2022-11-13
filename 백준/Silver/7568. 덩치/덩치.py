# 최종 정답
# 블로그 검색한 코드. 전혀 다른 방식으로 짜고 있어서 이해하는데에 시간이 오래걸렸음
# "k명이 더 크다면 k+1이 등수"라는 것을 이용함

import sys

bulk = sys.stdin.readlines()
n = int(bulk[0])
bulk = [tuple(map(int, b.split())) for b in bulk[1:]]

for b_1 in bulk:
	rank = 1
	(a, b) = b_1
	for b_2 in bulk:
		(x, y) = b_2
		if a < x and b < y:
			rank += 1	# 하나의 튜플 a에 대해서, a보다 큰 요소의 수 만큼 더한다. 
	print(rank, end=' ')
	

	
# 내가 원래 구상했던 코드 (❌오답❌)
# index를 딕셔너리로 해서 접근하는 방식을 구상했는데, 
# 같은 원소가 있는 경우 여러 개 중 하나만 dict으로 저장되어서 아무리해도 오답이었음😥🙃😥
# 내가 꼭 맞추고 싶었는데...

import sys

bulk = sys.stdin.readlines()
n = int(bulk[0])
bulk_1 = [tuple(map(int, b.split())) for b in bulk[1:]]
idx = {v:i for i, v in enumerate(bulk_1)}
bulk_2 = sorted(bulk_1, key=lambda x: (x[0], x[1]))[::-1]

c_1, c_2 = 1, 1
rank = [0]*n

for i in range(n-1):
	(a, b), (x, y) = bulk_2[i], bulk_2[i+1]
	if a > x and b < y:
		rank[idx[(a, b)]] = c_1
		rank[idx[(x, y)]] = c_1
		c_2 += 1
	elif a < x and b > y:
		rank[idx[(a, b)]] = c_1
		rank[idx[(x, y)]] = c_1
		c_2 += 1
	elif a == x and b == y:
		rank[idx[(a, b)]] = c_1
		rank[bulk_1.index((x,y))] = c_1
		c_2 += 1
	else:
		rank[idx[(a, b)]] = c_1
		c_2 += 1
		rank[idx[(x, y)]] = c_2
		c_1 = c_2
		
print(' '.join(map(str, rank)))
