n, x = map(int, input().split())
A = list(filter(lambda a: x > int(a), input().split()))

for a in A:
    print(int(a), end=' ')