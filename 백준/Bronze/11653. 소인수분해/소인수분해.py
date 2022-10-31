# 첫 번째 답
# 메모리: 30840 KB, 시간: 1328 ms
# 시간이 너무 오래 걸림

n = int(input())

for i in range(2, n+1):
    if n % i == 0:
        while n % i == 0:
            n /= i
            print(i)
            

# 두 번째 답
# 메모리: 30840 KB, 시간: 80 ms
# 가장 빠른 답을 참고

n = int(input())
i = 2
r = int(n**0.5)   # root

while i <= r:
    while not n % i:   # while not 구문: 조건문이 참이 아닐 동안 반복되는 while문 (n%i==0은 False, n%i==1이 되면 True가 됨)
        n //= i
        print(i)
    i += 1
if n > 1:
    print(n)
