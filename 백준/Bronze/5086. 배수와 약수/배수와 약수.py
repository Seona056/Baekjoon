import sys

test = sys.stdin.readlines()[:-1]

for t in test:
	f, s = map(int, t.split())	# first, second
	
	if s % f == 0:
		print('factor')
	elif f % s == 0:
		print('multiple')
	else:
		print('neither')