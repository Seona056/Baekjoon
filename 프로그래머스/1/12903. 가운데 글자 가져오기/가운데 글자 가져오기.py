def solution(s):
    l = len(s)
    div = l//2
    
    if l % 2 == 0:
        answer = s[div-1:div+1]
    else:
        answer = s[div]
    
    return answer