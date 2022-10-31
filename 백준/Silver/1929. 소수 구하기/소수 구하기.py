# 첫 번째 답
# 메모리: 30840 KB, 시간: 5720 ms
# [2581번 소수]와 같은 코드 사용
# 메모리는 두 번째 보다 적게 썼지만, 시간이 매우 많이 걸림

f, l = map(int, input().split())   # first, last
root = lambda x: int(x**0.5)+1

for n in range(f, l+1):
    if n < 2:
        continue
        
    c = 0
    for i in range(2, root(n)):
        if n % i == 0:
            c = 1
            break
    if c == 0:
        print(n)


# 두 번째 답
# 메모리: 46188 KB, 시간: 440 ms
# 에라토스테네스의 체 
# 노션에 정리 : https://lovely-sand-5da.notion.site/6481f99f1ac34797837f48c7d29e2440
# 첫 번째 답보다 시간은 1/5가량 줄었지만, 메모리는 조금 더 사용되었다.

f, l = map(int, input().split())   # first, last
decimal = [False, False]+[True]*(l-1)   # index 0, 1을 Fasle로 설정 (소수가 아님)

for i in range(2, l+1):
    if decimal[i]:
        if f <= i:
            print(i)
        for j in range(i*2, l+1, i):  # 소수 i의 배수를 모두 Fasle로 바꾼다.
            decimal[j] = False
