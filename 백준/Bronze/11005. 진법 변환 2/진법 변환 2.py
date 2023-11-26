import sys
n, b = map(int, sys.stdin.read().split())
temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = ''

while n:
	a += temp[n % b]
	n //= b
	
print(a[::-1])