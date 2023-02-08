# 첫 번째 답
# 메모리: 31256 KB, 시간: 64 ms
# 3개월 전에 시도하다가 포기한 걸 다시 풀어봄. 엄청 많은 시도 끝에 성공...
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

                
----------------------------------------------------------
# 두 번째 답
# 딕셔너리(해시 테이블)로 다시 시도
# 메모리: 32568 KB, 시간: 92 ms
# 딕셔너리를 쓰면 리스트의 인덱스로 찾는 것 보다 더 빨라질 줄 알았는데, 메모리도 시간도 조금 더 걸렸음
# 대량으로 같은 value의 딕셔너리를 추가하는 ✅dict.fromkeys(리스트, 입력할 값)✅을 배웠다. 
# 입력할 값을 생략하고 리스트만 인자로 넣으면 value는 모두 None으로 동일하게 생성된다.

prime = dict.fromkeys(range(2,10000+1), True)

for i in range(2, 10000+1):
    if prime[i]:
        for j in range(i*2, 10000+1, i):
            prime[j] = False

import sys
test = map(int, sys.stdin.readlines()[1:])
test = [8, 10, 16]

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

               
----------------------------------------------------------
# 세 번째 답
# if t == 4일때를 뺀 코드로 제출 (딕셔너리)
# 메모리: 32568 KB, 시간: 68 ms
# 두 번째 보다 조금 더 빨라졌음

prime = dict.fromkeys(range(2,10000+1), True)

for i in range(2, 10000+1):
    if prime[i]:
        for j in range(i*2, 10000+1, i):
            prime[j] = False

import sys
test = map(int, sys.stdin.readlines()[1:])

for t in test:
    
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

                
----------------------------------------------------------
# 세 번째 답
# 메모리: 31256 KB, 시간: 64 ms
# 첫 번째 답에서 if t == 4를 뺀 코드 (리스트 prime 테이블)
# 가장 빠른 답으로 교체됨


prime = [False, False]+[True]*(10000-1)
for i in range(2,10000+1):
    if prime[i]:
        for j in range(i*2, 10000+1, i):
            prime[j] = False

            
import sys
test = map(int, sys.stdin.readlines()[1:])

for t in test:

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
