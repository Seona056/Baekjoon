import re

def solution(s):

    answer = s  # 이렇게 answer에 s를 할당해 주지 않으면 for문에서 answer 대신 s를 넣었더니 계속 원래 input이 들어가서 제대로 변환되지 않았음

    str2int = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}

    for k, v in str2int.items() :
        
        # answer = re.sub(k, str(v), answer)
        answer = answer.replace(k, str(v))

    return int(answer)