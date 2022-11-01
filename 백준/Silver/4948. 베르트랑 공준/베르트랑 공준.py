import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
decimal = [2]

l = [False, False]+[True]*(2*m-1)  # list
for i in range(3, 2*m+1, 2):   # 짝수는 모두 소수가 아니므로, 홀수만 검증
    if l[i]:
        decimal.append(i)
        for j in range(2*i, 2*m+1, i):
            l[j] = False
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, decimal))
    print(len(answer))