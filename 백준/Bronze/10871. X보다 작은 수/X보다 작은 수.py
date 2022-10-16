# 첫 번째 답 : 걸린 시간, 메모리는 동일함

n, x = map(int, input().split())
A = list(filter(lambda a: x > int(a), input().split()))

for a in A:
    print(int(a), end=' ')
    
    
    
# 두 번째 답 : 걸린 시간, 메모리는 동일함

n, x = input().split()
A = list(filter(lambda a: int(x) > int(a), input().split()))

for a in A:
    print(int(a), end=' ')
