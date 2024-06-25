def solution(num, total):
    s = sum(range(num+1))
    d = total - s
    gap = d//num
    
    return list(i for i in range(1+gap, num+1+gap))

