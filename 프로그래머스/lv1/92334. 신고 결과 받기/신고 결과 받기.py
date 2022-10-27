def solution(id_list, report, k):

    alarm={id : 0 for id in id_list}
    
    answer = [0]*len(id_list)    # 요소가 0인 하나의 리스트가 생겨난다. 👉 [0, 0, 0, 0]
    
    for i in set(report):
         alarm[i.split()[1]] += 1
        
    for j in set(report):
        if alarm[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])]+=1

    return answer