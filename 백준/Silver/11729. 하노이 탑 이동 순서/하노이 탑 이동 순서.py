# 인터넷 검색으로 코드를 짰다.

def hanoi(n, first, last, middle):

    if n == 1:
        return print(first, last)
    
    hanoi(n-1, first, middle, last)
    print(first, last)
    hanoi(n-1, middle, last, first)

n = int(input())
print(2**n -1)
hanoi(n, 1, 3, 2)

--------------------------------------------------------------------------------------------------
# print문이 찍히는 순서는 첫 번째 재귀가 먼저 실행되고 그 재귀의 재귀 재귀 재귀 --- n==1이 가장 먼저 출력
# 재귀 다음의 print가 출력
# 그 다음 마지막 재귀가 출력됨
# print문에 f'{n} :'를 추가해서 출력해보면 
1 : 1 3
2 : 1 2
1 : 3 2
3 : 1 3
1 : 2 1
2 : 2 3
1 : 1 3
