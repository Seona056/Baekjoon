def solution(dots):
    answer = 0
    line1 = [(0,1), (0,2), (0,3)]
    line2 = [(2,3), (1,3), (1,2)]
    
    for l1, l2 in zip(line1,line2):
        d1 = dots[l1[0]]
        d2 = dots[l1[1]]
        d3 = dots[l2[0]]
        d4 = dots[l2[1]]
        
        a = list(map(lambda x, y: y-x, d1, d2))
        b = list(map(lambda x, y: y-x, d3, d4))
        
        if a[1]/a[0] == b[1]/b[0]:
            return 1
    return answer