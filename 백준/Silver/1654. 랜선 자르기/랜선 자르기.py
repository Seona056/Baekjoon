def get_lines(n, first, end):
	
	if first > end:
		return end
	
	mid = (end+first)//2
	c = sum(map(lambda x: x//mid, lines))
	
	if c >= n:
		return get_lines(n, mid+1, end)
	else:
		return get_lines(n, first, mid-1)


import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

print(get_lines(n, 1, max(lines)))