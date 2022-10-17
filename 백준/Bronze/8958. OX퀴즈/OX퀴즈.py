# 첫 번째 답
# 메모리: 30840 KB, 시간: 80 ms

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

        
# 두 번째 답
# 메모리: 30840 KB, 시간: 72 ms
# input()보다 sys.stdin.readline()이 8ms나 빨랐다.

import sys

n = int(input())
score = lambda x: sum([s for s in range(1, x+1)])

for i in range(n):
    OX = sys.stdin.readline()
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
        
        
        
# 세 번째 답
# 메모리: 30840 KB, 시간: 68 ms
# 가장 빠른 답을 참고하여 수정한 답
# 람다식이나 if문이 필요하지 않았다...

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
