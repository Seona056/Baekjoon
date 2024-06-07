def solution(a, b, c, d):
    answer = 1
    l = sorted([a,b,c,d])
    s = set(l)
    
    if len(s) == 1:
        answer = 1111*a
    elif len(s) == 4:
        answer = l[0]
    elif len(s) == 3:
        for i in s:
            if l.count(i) == 1:
                answer *= i
    elif len(s) == 2:
        temp = l.count(l[0])
        if temp == 2:
            answer = (l[1]+l[2]) * abs(l[1]-l[2])
        else:
            if temp == 1:
                p, q = l[-1], l[0]
            else:
                p, q = l[0], l[-1]
            answer = (10*p+q)**2
    
    return answer