import sys, heapq
input = sys.stdin.readline
arr = []

for x in range(int(input())):
	x = int(input())
	
	if x == 0:
		if arr:
			print(heapq.heappop(arr))
		else:
			print(0)
		continue
	heapq.heappush(arr, x)