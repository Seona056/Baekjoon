from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    d = defaultdict(lambda : [0,0])
    
    for a, b in edges:
        d[a][0] += 1
        d[b][1] += 1
        
    for node, item in d.items() :
        give = item[0]
        take = item[1]
        
        if give >= 2 and take == 0:
            answer[0] = node
        elif give >= 2 and take >= 2:
            answer[3] += 1
        elif give == 0 and take >= 1:
            answer[2] += 1
    
    a = d[answer[0]][0]
    answer[1] = a - answer[2] - answer[3]
    
    return answer