# 첫 번째 답
# 메모리: 30840 KB, 시간: 76 ms
# 걸린 시간, 메모리는 동일함

n, x = map(int, input().split())
A = list(filter(lambda a: x > int(a), input().split()))

for a in A:
    print(int(a), end=' ')
    
    
    
# 두 번째 답
# 메모리: 30840 KB, 시간: 76 ms
# 걸린 시간, 메모리는 동일함

n, x = map(int, input().split())
A = [int(i) for i in input().split() if x > int(i)]

for a in A:
    print(int(a), end=' ')
    

    
# 세 번째 답
# 메모리: 30840 KB, 시간: 68 ms

n, x = map(int, input().split())
A = [i for i in input().split() if x > int(i)]
print(' '.join(A))
