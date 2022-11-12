n = int(input())
m = n//2

while m < n:
    decomposition = sum(map(int ,str(m))) + m
    if decomposition == n:
        print(m)
        break
    m += 1
else:
    print(0)