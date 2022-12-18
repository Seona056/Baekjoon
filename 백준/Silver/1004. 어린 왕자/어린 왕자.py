import sys
input = sys.stdin.readline

for i in range(int(input())):
	x1, y1, x2, y2 = map(int, input().split())
	cross = 0
	
	for j in range(int(input())):
		cx, cy, r = map(int, input().split())
		d1 = pow(x1-cx, 2) + pow(y1-cy, 2)
		d2 = pow(x2-cx, 2) + pow(y2-cy, 2)
		
        # 출발, 도착 좌표가 같은 원 안에 있을때는 카운팅하지 않는다.
		if d1 < r**2 < d2:
			cross += 1
		elif d2 < r**2 < d1:
			cross += 1
		
	print(cross)