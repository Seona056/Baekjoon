f, l = map(int, input().split())   # first, last
decimal = [False, False]+[True]*(l-1)   # index 0, 1을 Fasle로 설정 (소수가 아님)

for i in range(2, l+1):
    if decimal[i]:
        if f <= i:
            print(i)
        for j in range(i*2, l+1, i):  # 소수 i의 배수를 모두 Fasle로 바꾼다.
            decimal[j] = False