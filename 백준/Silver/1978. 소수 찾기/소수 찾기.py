input()
num = list(map(int, input().split()))
answer = 0

for n in num:
    c = 0
    if n == 1:
        c +=1
    elif n == 2:
        pass        
    else:
        for i in range(2,n):
            if n % i == 0:
                c += 1
                continue
    if c == 0:
        answer += 1
print(answer)