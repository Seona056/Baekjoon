import sys
num, b = sys.stdin.read().split()
d = {str(i):i for i in range(10)}
d.update({chr(s).upper():i+10 for i, s in enumerate(range(ord('a'), ord('z')+1))})

a = 0
for i, n in enumerate(num[::-1]):
	
	a += (int(b)**i) * d[n]

print(a)