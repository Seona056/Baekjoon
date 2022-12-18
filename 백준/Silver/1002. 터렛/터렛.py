import sys
import math

test = sys.stdin.readlines()[1:]

for t in test:
	x1, y1, r1, x2, y2, r2 = map(int, t.split())
	d = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))	# distance
	
	if (x1, y1, r1) == (x2, y2, r2):
		print(-1)
		continue
	
	if r1+r2 < d:	# 서로의 외부에 위치
		print(0)
	elif r1+r2 == d:	# 외접
		print(1)
	elif abs(r1-r2) < d < r1+r2:	# 서로 다른 두 점에서 만난다.
		print(2)
	elif abs(r1-r2) == d:	# 내접
		print(1)
	elif abs(r1-r2) > d and r1 != r2:	# 한 원의 내부에 위치
		print(0)