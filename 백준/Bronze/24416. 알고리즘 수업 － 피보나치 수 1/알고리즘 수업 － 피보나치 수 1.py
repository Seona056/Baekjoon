# 첫 번째 답
# 메모리: 31256 KB, 시간: 40 ms
# 문제에 나와있는 c언어를 그대로 파이썬으로 번역
# 첫 번째 재귀함수는 피보나치 수 만큼 하나하나 다 실행되는거였음...

n = int(input())

def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1) + fib(n-2)
	
def fibonacci(n):
	f = [0, 1] + [1]*(n-1)
	
	for i in range(3, n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

print(fibonacci(n), n+1-3)


----------------------------------------------------------
# 두 번째 답
# 메모리: 31256 KB, 시간: 40 ms
# 위의 코드를 초간단하게 줄여본 것
# 맞힌 사람 랭킹 1위 답이었는데, 내 노트북에서는 40ms나 걸렸음😥

n = int(input())
f = [0,1,1]
for i in range(3, n+1):
    f.append(f[-1]+f[-2])
print(f[n], n-2)
