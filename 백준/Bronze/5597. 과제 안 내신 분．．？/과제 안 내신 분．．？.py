n_list = [0]*30

for _ in range(28):
	n = int(input())
	n_list[n-1] = n
	
for i in range(30):
	if n_list[i] == 0:
		print(i+1)