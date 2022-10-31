m = int(input())
n = int(input())

numbers = list(_ for _ in range(m, n+1))
decimal, total = 0, 0

for num in numbers:
    c = 0
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            c += 1
            break
    if c == 0 :
        if decimal == 0:
            decimal = num
            total += num
        else :
            total += num

if decimal != 0:
    print(total)
    print(decimal)
else:
    print(-1)