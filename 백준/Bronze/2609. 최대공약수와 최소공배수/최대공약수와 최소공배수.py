(a, b) = sorted(tuple(map(int, input().split())))
m = a*b

while True:
	temp = a % b
	if temp == 0:
		print(b)
		break
	a, b = b, temp
	
print(m//b)