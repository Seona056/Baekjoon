import sys

n = int(sys.stdin.readline())

for i in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:])/score[0]
    
    count = 0
    for s in score[1:]:
        if s > avg:
            count += 1

    print(f'{(count/score[0]*100):.3f}%')        
    
    