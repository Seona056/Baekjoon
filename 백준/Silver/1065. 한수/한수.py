n = int(input())
count = 99

if n == 1000:
    n = 999
    
if n < 100:
    print(n)
elif 100 <= n < 1000:
    for i in range(100, n+1):
        [a, b, c] = map(int, str(i))      
        if b-a == c-b:
            count += 1
    print(count)