n = int(input())
i = 2
r = int(n**0.5)   # root

while i <= r:
    while not n % i:   # while not 구문: 조건문이 참이 아닐 동안 반복되는 while문 (n%i==0은 False)
        n //= i
        print(i)
    i += 1
if n > 1:
    print(n)