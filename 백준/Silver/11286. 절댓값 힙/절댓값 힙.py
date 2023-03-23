import sys, heapq
input = sys.stdin.readline
hq = []

for x in range(int(input())):
	x = int(input())
	if x == 0:
		if hq:
			print(heapq.heappop(hq)[1])
		else:
			print(0)
		continue
	heapq.heappush(hq, (abs(x), x))