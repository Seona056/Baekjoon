n, x = map(int, input().split())
A = [i for i in input().split() if x > int(i)]
print(' '.join(A))