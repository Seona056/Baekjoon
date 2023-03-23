# 메모리: 31256 KB, 시간: 48 ms

# 풀이
# n == 3 : 1 0 0 👉 1개, 3자리
# n == 4 : 1 0 0 1 👉 2개, 4자리
# n == 5 : 1 0 0 1 0 👉 2개, 5자리
# n == 6 : 1 0 0 1 0 0 👉 2개, 6자리
# n == 7 : 1 0 0 1 0 0 0 👉 2개, 7자리
# n == 8 : 1 0 0 1 0 0 0 0 👉 2개, 8자리
# n == 9 : 1 0 0 1 0 0 0 0 1 👉 3개, 9자리
# 1이 나타나는 주기가 있음. 100 👉 10000 👉 1000000 : 3부터 시작하여 +2씩 늘어나는 수열

def window(n):
	if n == 1 or n == 2:
		return 1
	
	i, c = 1, 3
	while n > c:
		if n-c > 0:
			i += 1
			n -= c
			c += 2
	return i
	
print(window(int(input())))
