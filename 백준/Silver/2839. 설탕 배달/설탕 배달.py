n = int(input())

bag = 0

while n >= 0:
    if n % 5 == 0:              # n이 0이 되었을때도 5의 배수(나머지 0)
        print(n//5+bag)
        break
    n -= 3
    bag += 1
else:
    print(-1)
