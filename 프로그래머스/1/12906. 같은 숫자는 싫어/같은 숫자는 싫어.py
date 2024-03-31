def solution(arr):
    answer, temp = [arr[0]], arr[0]
    
    for a in arr[1:]:
        if temp == a:
            continue
        else:
            answer.append(a)
            temp = a
    
    return answer