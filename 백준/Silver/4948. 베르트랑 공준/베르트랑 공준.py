import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
        if n == 0:
            break
        decimal = [False, False]+[True]*(2*n-1)
        c = 0   # count
        for i in range(2, 2*n+1):
            if decimal[i]:
                if i > n:
                    c += 1
                for j in range(2*i, 2*n+1, i):
                    decimal[j] = False
        print(c)
    except:
        break