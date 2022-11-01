import sys

numbers = list(map(int, sys.stdin.readlines()))
m = max(numbers)
decimal = []

l = [False, False]+[True]*(2*m-1)  # list
for i in range(2, 2*m+1):
    if l[i]:
        decimal.append(i)
        for j in range(2*i, 2*m+1, i):
            l[j] = False
            
for n in numbers:
    if n == 0:
        break
    answer = list(filter(lambda x: n < x <= 2*n, decimal))
    print(len(answer))