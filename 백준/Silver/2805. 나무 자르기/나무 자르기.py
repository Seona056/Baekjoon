import sys
from collections import Counter
input = sys.stdin.readline

def get_m(m, first, end):
	if first > end:
		return end
	
	mid = (first+end)//2
	left = sum((t-mid)*i for t, i in trees.items() if t>mid)
	
	if left >= m:
		return get_m(m, mid+1, end)
	else:
		return get_m(m, first, mid-1)

n, m = map(int, input().split())
trees = Counter(map(int, input().split()))
print(get_m(m, 0, max(trees)))