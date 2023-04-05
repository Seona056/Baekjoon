import sys
input = sys.stdin.readline
log = set()

for i in range(int(input())):
	n, e_l = input().split()	# name, enter_leave
	
	if e_l == 'enter':
		log.add(n)
	else:
		log.remove(n)
		
print('\n'.join(sorted(log)[::-1]))