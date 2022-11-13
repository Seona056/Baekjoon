import sys

bulk = sys.stdin.readlines()
bulk = [tuple(map(int, b.split())) for b in bulk[1:]]

for a, b in bulk:
	rank = 1
	for x, y in bulk:
		if a < x and b < y:
			rank += 1
	print(rank, end=' ')