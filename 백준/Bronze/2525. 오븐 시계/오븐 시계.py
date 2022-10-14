a, b = map(int, input().split())
c = int(input())

b = b+c

m = b%60
h = b//60

if b >= 60:
    if a + h == 24:
        print(0, m)
    else:
        print((a+h)%24, m)
elif b < 60:
    print(a, b)