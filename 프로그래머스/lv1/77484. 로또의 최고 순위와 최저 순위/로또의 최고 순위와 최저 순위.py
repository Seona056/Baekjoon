def solution(lottos, win_nums):
    answer = [] # 당첨 가능한 최고순위, 최저 순위

    count = lottos.count(0)
    
    if 0 in lottos:
                
        for i in range(count):
            lottos.remove(0)
    
#     lotto = []

#     for l in lottos:
#         if l in win_nums:
#             lotto.append(l)

    lotto = [l for l in lottos if l in win_nums]
    
    L = len(lotto)

    if count == 6:
        answer = [1, 6]
    elif L == 0 and count <= 1:
        answer.append(6-L-count)
        answer.append(6-L) 
    else:
        answer.append(7-L-count)
        answer.append(7-L)    
           
    return answer