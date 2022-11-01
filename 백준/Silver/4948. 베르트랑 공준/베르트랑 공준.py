import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
r = int((2*m)**0.5)

l = [False, False]+[True]*(2*m-1)  # list
for i in range(3, r+1, 2):   # 홀수만 최대공약수 까지 검증
    if l[i]:
        l[2*i::i] = [False]*((2*m)//i-1)
            
prime = [2] + list(i for i in range(3, 2*m+1, 2) if l[i])          
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, prime))
    print(len(answer))