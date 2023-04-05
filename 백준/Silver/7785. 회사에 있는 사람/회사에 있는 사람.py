import sys
input = sys.stdin.readline
log = set()

for i in range(int(input())):
	n, _ = input().split()
	
	if _ == 'enter':
		log.add(n)
	else:
		log.remove(n)
		
print('\n'.join(sorted(log)[::-1]))