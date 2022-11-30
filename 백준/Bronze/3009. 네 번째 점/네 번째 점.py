rect = open(0).read().split()
x, y = 0, 0

for r in rect[::2]:
	x^=int(r)
for r in rect[1::2]:
	y^=int(r)

print(x, y)