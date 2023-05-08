import sys
input = sys.stdin.readline
n, c = map(int, input().split())
h = [int(input()) for i in range(n)]
h.sort()

start = 1
end = h[-1]-h[0]
answer = 0

while start <= end:
	mid = (start+end) // 2
	h1 = h[0]
	cnt = 1
	for h2 in h[1:]:
		if h2-h1 >= mid:
			h1 = h2
			cnt += 1
	if cnt >= c:
		start = mid+1
		answer = mid
	else:
		end = mid-1
		
print(answer)