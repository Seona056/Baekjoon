from collections import Counter

def solution(friends, gifts):
    this = Counter(gifts)
    friends = {f:0 for f in friends}
    
    for g in gifts:
        a, b = g.split()
        friends[a] += 1
        friends[b] -= 1
    
    answer = []
    for f1 in friends:
        a = 0
        for f2 in friends:
            if f1 == f2:
                continue
            
            key1 = f1 + ' ' + f2
            key2 = f2 + ' ' + f1
            
            # 선물 기록 있다면, 
            if key1 in this:
                if key2 in this:
                    # 더 많은 선물을 준 사람    
                    if this[key1] > this[key2]:
                        a += 1
                    # 주고 받은 선물 수가 같다면
                    elif this[key1] == this[key2]:
                        if friends[f1] > friends[f2]:
                            a += 1
                else:
                    # print(f1, f2)
                    a += 1
            # 선물 기록이 없다면,
            else:
                if key2 not in this:
                    if friends[f1] > friends[f2]:
                        a += 1
        answer.append(a)
    return max(answer)