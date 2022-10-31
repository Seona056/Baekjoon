m = int(input())
n = int(input())

numbers = list(_ for _ in range(m, n+1))
decimal = []

for num in numbers:
    if num == 1:
        continue
    
    c = 0
    for i in range(2, num):
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