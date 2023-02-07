# 3개월 전에 시도하다가 포기한 걸 다시 풀어봄
# 엄청 많은 시도 끝에 성공...
# n의 최대 숫자로 미리 prime 테이블을 만들어놓고 시작하는 것이 정답이었다. (4 <= n <= 10,000 )
# 인덱스 번호로 해당 숫자가 소수인지 아닌지를 판별할 수 있어서 편리
# 테스트 케이스 10 👉 5 5 처럼 절반이 소수인 경우부터 차례로 소수 검정을 하는 식으로 구성
# 이전 제출한 코드들도 아이디어는 비슷했지만, prime테이블이 아닌 에라토스테네스의 체로 코드를 짜서 시간초과로 통과하지 못했었음

prime = [False, False]+[True]*(10000-1)
for i in range(2,10000+1):
    if prime[i]:
        for j in range(i*2, 10000+1, i):
            prime[j] = False

            
import sys
test = map(int, sys.stdin.readlines()[1:])

for t in test:

    if t == 4:
        print(2, 2)
        continue

    half = t//2
    if prime[half]:
        print(half, half)
        continue

    while True:
        half -= 1
        if prime[half]:
            if prime[t-half]:
                print(half, t-half)
                break
