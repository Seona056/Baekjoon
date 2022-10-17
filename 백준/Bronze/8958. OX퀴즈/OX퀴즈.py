n = int(input())
score = lambda x: sum([s for s in range(1, x+1)])

for i in range(n):
    OX = input()
    s, total = 0, 0
    
    for ox in OX:
        if ox == 'O':
            s += 1
        elif ox == 'X' and s > 0:
            total += score(s)
            s = 0
        
    if s > 0 :
        total += score(s)
        print(total)        
    else:
        print(total)