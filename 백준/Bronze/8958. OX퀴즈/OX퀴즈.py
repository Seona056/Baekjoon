import sys

n = int(sys.stdin.readline())

for i in range(n):
    OX = sys.stdin.readline()
    score, total = 1, 0
    
    for ox in OX:
        if ox == 'O':
            total += score
            score += 1
        else:
            score = 1
            
    print(total)