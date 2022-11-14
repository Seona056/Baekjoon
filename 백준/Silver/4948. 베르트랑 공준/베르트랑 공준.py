# 첫 번째 답
# 메모리: 36980 KB, 시간: 3672 ms
# EOF 종료조건 이용
# 노션 : https://www.notion.so/0755a6a1c4924ddabf2845cb5afab8fa (EOF 종료조건)

import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        if n == 0:
            break
        prime = [False, False]+[True]*(2*n-1)
        c = 0   # count
        for i in range(2, 2*n+1):
            if prime[i]:
                if i > n:
                    c += 1
                for j in range(2*i, 2*n+1, i):
                    prime[j] = False
        print(c)
    except:
        break


# 두 번째 답
# 메모리: 36980 KB, 시간: 3704 ms
# EOF 종료조건을 뺀 평범한 while문으로 작성 👉 시간이 조금 더 걸림

import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    prime = [False, False]+[True]*(2*n-1)
    c = 0   # count
    for i in range(2, 2*n+1):
        if prime[i]:
            if i > n:
                c += 1
            for j in range(2*i, 2*n+1, i):
                prime[j] = False
    print(c)

    
# 세 번째 답
# 메모리: 36980 KB, 시간: 3776 ms
# 입력들을 모두 한 번에 받아 numbers 리스트를 생성 👉 리스트의 요소를 하나하나 꺼내는 for문 작성
# 시간이 가장 오래 걸렸음

import sys

numbers = list(map(int, sys.stdin.readlines()))

for n in numbers:
    if n == 0:
        break
    prime = [False, False]+[True]*(2*n-1)
    c = 0   # count
    for i in range(2, 2*n+1):
        if prime[i]:
            if i > n:
                c += 1
            for j in range(2*i, 2*n+1, i):
                prime[j] = False
    print(c)
    

# 네 번째 답
# 메모리: 34700 KB, 시간: 804 ms
# 가장 큰 수로 prime 목록을 만들어 놓고, 각 수의 범위 (n보다 크고 2n보다 이하)에 맞춰 필터링

import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
prime = []

l = [False, False]+[True]*(2*m-1)  # list
for i in range(2, 2*m+1):
    if l[i]:
        prime.append(i)
        for j in range(2*i, 2*m+1, i):
            l[j] = False
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, prime))
    print(len(answer))


# 다섯번째 답
# 메모리: 34700 KB, 시간: 780 ms
# 2를 제외한 짝수는 모두 소수가 아니므로, 홀수만 검증한다.

import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
prime = [2]

l = [False, False]+[True]*(2*m-1)  # list
for i in range(3, 2*m+1, 2):   # 짝수는 모두 소수가 아니므로, 홀수만 검증
    if l[i]:
        prime.append(i)
        for j in range(2*i, 2*m+1, i):
            l[j] = False
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, prime))
    print(len(answer))


# 마지막 답
# 메모리: 34700 KB, 시간: 724 ms
# 홀수만 최대공약수 까지 검증 👉 False로 바꾸는 건 리스트 끝까지 바꾼다.

import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
r = int((2*m)**0.5)

l = [False, False]+[True]*(2*m-1)  # list
for i in range(3, r+1, 2):   # 홀수만 최대공약수 까지 검증
    if l[i]:
        l[2*i::i] = [False]*((2*m)//i-1)   # False의 갯수를 맞춰준다.
            
prime = [2] + list(i for i in range(3, 2*m+1, 2) if l[i])          
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, prime))
    print(len(answer))
    
    

# ✔ 참고 ✔
    
# 입력 최대값 m=123456의 prime 리스트를 만들어두고 필터링하는 방법도 시도해 보았으나, 
# numbers 리스트에서 max를 구하는 방식보다 시간이 더 많이 걸렸다.
