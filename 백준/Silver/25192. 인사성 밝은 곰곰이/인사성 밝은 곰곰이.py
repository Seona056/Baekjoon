import sys
input = sys.stdin.readline

gomticon, gom_cnt = set(), 0

for i in range(int(input())):
	_ = input().rstrip()
	
	if _ == 'ENTER':
		if gomticon:
			gom_cnt += len(gomticon)
		gomticon = set()
	else:
		gomticon.add(_)

print(gom_cnt+len(gomticon))