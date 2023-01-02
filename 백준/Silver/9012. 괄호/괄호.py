import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	l, r = 0, 0
	
	for i in v:
		if i == '(':
			if l >= r:
				l += 1
			else:
				l += 1
				break
		else:
			if l > r:
				r += 1
			else:
				r += 1
				break
	
	if l == r:
		print('YES')
	else:
		print('NO')