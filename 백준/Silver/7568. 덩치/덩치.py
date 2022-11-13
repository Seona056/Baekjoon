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
			rank += 1	# 하나의 튜플 a에 대해서, a보다 큰 요소의 수 만큼 더한다. k명이 더 크다면 k+1이 등수
	print(rank, end=' ')