n = int(input())
c, series = 7, 6660

if n == 1:
    print(666)
elif 0 < n <= 6:
    print(str(n-1)+'666')
elif n > 6:
    while True:
        if c == n:
            print(series) 
            break
        series += 1
        if '666' in str(series):
            c += 1