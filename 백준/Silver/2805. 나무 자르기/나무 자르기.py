def get_m(m, first, end):
	if first > end:
		return end
	
	mid = (first+end)//2
	left = sum(t-mid for t in trees if t>mid)
	
	if left >= m:
		return get_m(m, mid+1, end)
	else:
		return get_m(m, first, mid-1)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(get_m(m, 0, max(trees)))