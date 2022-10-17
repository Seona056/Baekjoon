import sys

n = int(sys.stdin.readline())
score = lambda x: sum([s for s in range(1, x+1)])

for i in range(n):
    OX = sys.stdin.readline()
    s, total = 1, 0
    
    for ox in OX:
        if ox == 'O':
            total += s
            s += 1
        else:
            s = 1
            
    print(total)