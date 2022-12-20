import sys
input = sys.stdin.readline

for i in range(int(input())):
	items = {}
	
	for j in range(int(input())):
		item, kind = input().split()
		
		if kind in items:
			items[kind] += 1	# 같은 이름의 의상은 존재하지 않음
		else:
			items[kind] = 2		# 하나도 착용하지 않는 경우 +1
		
	comb = 1
	for v in items.values():
		comb *= v
	print(comb-1)	# 아무것도 입지 않는 경우 -1