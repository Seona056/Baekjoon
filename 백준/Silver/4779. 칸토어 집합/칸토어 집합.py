def get_line(n: int):
	if n == 0:
		return '-'
		
	mid = 3**(n-1)
	if mid > 1:
		return get_line(n-1) + ' '*mid + get_line(n-1)
	else:
		return '-'*mid + ' '*mid + '-'*mid

for n in open(0).readlines():
	print(get_line(int(n)))