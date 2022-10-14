h, m = map(int, input().split())
m = m - 45

if m > 0:
    print(h, m)
elif m < 0:
    if h == 0 and m != 0:
        h = 24
        print(h-1, m%60)
    else:
        print(h-1, m%60)
elif m == 0:
    print(h, 0)