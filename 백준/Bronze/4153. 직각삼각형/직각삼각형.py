import sys
triangle = sys.stdin.readlines()

for t in triangle[:-1]:

	l = list(map(int, t.split()))	# length : 변의 길이
	c = max(l)
	l.remove(c)
	
	if (l[0]**2) + (l[1]**2) == (c**2):
		print('right')
	else :
		print('wrong')