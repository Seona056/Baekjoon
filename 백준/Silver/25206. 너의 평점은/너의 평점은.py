import sys
table = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0, 'P': 0}
ch = sys.stdin.readlines()
total_c, total_p = 0, 0	# credit, point

for a in ch:
	_, c, p = a.split()
	c = float(c)
	total_p += c * table[p]
	if p == 'P':
		c = 0
	total_c += c
	
print(total_p/total_c)