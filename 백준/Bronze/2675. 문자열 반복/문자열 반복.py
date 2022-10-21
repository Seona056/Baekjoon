t = int(input())

for i in range(t):
    r, s = input().split()
    
    for S in s:
        print(S*int(r), end='')
    print()