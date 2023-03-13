# 첫 번째 답
# 메모리: 44160 KB, 시간: 116 ms

import sys
import math

n = int(input())
trees = list(map(int, sys.stdin.readlines()))
gap = []

for i in range(n-1):
	gap.append(trees[i+1] - trees[i])
	
m, c = math.gcd(*gap), 0

for g in gap:
	if g == m:
		continue
	elif g > m:
		c += g//m - 1
		
print(c)


----------------------------------------------------------
# 마지막 답
# 메모리: 44160 KB, 시간: 84 ms
# 가장 빠른 답을 참고
# ⭐ 나무 사이 거리들을 zip을 이용한 for문으로 구한다. 👉 리스트 각 요소별 차를 구할 때 사용할 수 있도록 숙지할 것❗
# 첫번째 나무와 마지막 나무 사이를 총 거리의 길이로 봤을 때, 나무가 총 몇 그루 심어져 있는지를 구한다.
# 총 나무의 수에서 이미 심어져 있는 나무의 갯수를 뺀다.

import math
n, *trees = map(int, open(0).readlines())
gap = math.gcd(*[x-y for x,y in zip(trees[1:], trees)])
all = (trees[-1]-trees[0]) // gap + 1
print(all-n)
