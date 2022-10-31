# 첫 번째 답
# 메모리: 30840 KB, 시간: 580 ms

m = int(input())
n = int(input())

numbers = list(_ for _ in range(m, n+1))
decimal = []

for num in numbers:
    if num == 1:
        continue
    
    c = 0
    for i in range(2, num):   # 2부터 자기자신까지 나누어서 소수 판별
        if num % i == 0:
            c = 1
            break
    if c == 0:
        decimal.append(num)

if len(decimal) == 0:
    print(-1)
else:
    print(sum(decimal))
    print(decimal[0])


# 두 번째 답
# 메모리: 30840 KB, 시간: 80 ms
# 어떤 자연수 n의 최대약수는 sprt(n)이므로, 2부터 int(n**0.5)+1 까지 나누어서 판별하면 시간이 절약된다.

m = int(input())
n = int(input())

numbers = list(_ for _ in range(m, n+1))
decimal = []

for num in numbers:
    if num == 1:
        continue
    
    c = 0
    m = int(num**0.5)   # 자연수 n의 최대 약수가 sqrt(n)이므로, 여기까지만 판별
    for i in range(2, m+1):    
        if num % i == 0:
            c = 1
            break
    if c == 0:
        decimal.append(num)

if len(decimal) == 0:
    print(-1)
else:
    print(sum(decimal))
    print(decimal[0])
