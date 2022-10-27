def solution(n, arr1, arr2):
    
    one = [int(bin(i).replace('0b','')) for i in arr1]
    two = [int(bin(i).replace('0b','')) for i in arr2]

    
    answer = [str(one[i]+two[i]).zfill(n) for i in range(n)]

    for i in range(n):
        answer[i]=answer[i].replace('0', ' ')
        answer[i]=answer[i].replace('1', '#')
        answer[i]=answer[i].replace('2', '#')



    return answer