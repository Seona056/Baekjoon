n, x = input().split()
A = list(filter(lambda a: int(x) > int(a), input().split()))

for a in A:
    print(int(a), end=' ')