def solution(quiz):
    answer = []
    
    for q in quiz:
        x, ops, y, _, z = q.split()
        
        if eval(x+ops+y) == int(z):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer