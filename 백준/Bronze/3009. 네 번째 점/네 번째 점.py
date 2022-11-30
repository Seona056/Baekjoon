rect = open(0).read().split()

x = sorted(rect[::2])
y = sorted(rect[1::2])

if x[1] == x[0]:
	print(x[2], end=' ')
else:
	print(x[0], end=' ')
	
if y[1] == y[0]:
	print(y[2])
else:
	print(y[0])