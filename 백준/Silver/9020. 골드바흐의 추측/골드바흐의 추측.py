prime = [False, False]+[True]*(10000-1)
for i in range(2,10000+1):
    if prime[i]:
        for j in range(i*2, 10000+1, i):
            prime[j] = False

            
import sys
test = map(int, sys.stdin.readlines()[1:])

for t in test:

    half = t//2
    if prime[half]:
        print(half, half)
        continue

    while True:
        half -= 1
        if prime[half]:
            if prime[t-half]:
                print(half, t-half)
                break