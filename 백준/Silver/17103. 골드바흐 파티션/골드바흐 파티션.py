# 첫 번째 답
# 메모리: 122300 KB, 시간: 220 ms
# 블로그 검색하여 참고한 코드
# 에라토스테네스의 체를 이용하여 입력값 중 가장 큰 값의 prime 리스트를 만들어서 시간 단축
# 자연수 n에 대하여 최대공약수는 n**0.5 이하로만 나타나므로, 그 이후에 나타나는 공약수는 없음
# ⭐map객체는 소비형 개체이므로, 한 번 반복이 실행되면 빈 객체가 된다! 👉 https://lovely-sand-5da.notion.site/15-88cd97556b0541cdbe3ed86f1e099f97

def get_prime(n):
	prime = [1]*(n+1)
	
	for i in range(2, int(n**0.5)+1):
		if prime[i]:
			j = 2
			while i*j <= n:
				prime[i*j] = 0
				j += 1
	return prime
	
nums = list(map(int, open(0).readlines()[1:]))
prime = get_prime(max(nums))

for n in nums:
	i, c = 2, 0
	while i <= n//2:
		if prime[i] and prime[n-i]:
			c += 1
		i += 1
	print(c)

	
----------------------------------------------------------
# 두 번째 답
# 메모리: 138576 KB, 시간: 272 ms
# 맞힌 사람 중 가장 빠른 답을 참고
# prime 리스트를 for문이 아닌, 슬라이싱을 이용하여 불리언 리스트로 만든 뒤(👉prime), 실제 소수가 들어있는 리스트를 하나 더 만든다. (👉 prime_2)
# n-p는 불리언 리스트(👉prime)에서 인덱스를 이용하여 찾는다. if (n-p) in prime_2 는 prime_2의 모든 수와 비교해야하기 때문에 prime에서 인덱싱으로 찾는 것이 더 빠르기 때문

n = 1000000
prime = [1]*(n+1)
prime[4::2] = [0]*(n//2-1)

for i in range(3, int(n**0.5)+1, 2):
	prime[2*i::i] = [0]*(n//i-1)
	
prime_2 = [2]+[i for i in range(3, n+1, 2) if prime[i]]
	
nums = list(map(int, open(0).readlines()[1:]))

for n in nums:
	c = 0
	for p in prime_2:
		if p > (n//2):
			print(c)
			break
		if prime[n-p]:
			c += 1
	
	
----------------------------------------------------------
# 마지막 답
# 메모리: 138568 KB, 시간: 196 ms
# 두 번째 답에서 prime, prime_2 리스트를 max(nums)까지만 구하는 것으로 변경해 봄

def get_prime(n):
	prime = [1]*(n+1)
	prime[4::2] = [0]*(n//2-1)
	
	for i in range(3, int(n**0.5)+1, 2):
		prime[2*i::i] = [0]*(n//i-1)
	
	prime_2 = [2]+[i for i in range(3, n+1, 2) if prime[i]]
	return prime, prime_2
	
nums = list(map(int, open(0).readlines()[1:]))
prime, prime_2 = get_prime(max(nums))

for n in nums:
	c = 0
	for p in prime_2:
		if p > (n//2):
			print(c)
			break
		if prime[n-p]:
			c += 1
