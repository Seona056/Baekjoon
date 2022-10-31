f, l = map(int, input().split())   # first, last
root = lambda x: int(x**0.5)+1

for n in range(f, l+1):
    if n < 2:
        continue
        
    c = 0
    for i in range(2, root(n)):
        if n % i == 0:
            c = 1
            break
    if c == 0:
        print(n)