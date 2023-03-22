import heapq

arr = []

for x in open(0).read().split()[1:]:
	x = int(x)
	
	if x == 0:
		if arr:
			print(-1 * heapq.heappop(arr))
		else:
			print(0)
		continue
	heapq.heappush(arr, -x)