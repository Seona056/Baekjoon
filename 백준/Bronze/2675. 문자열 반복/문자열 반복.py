t = int(input())

for i in range(t):
    r, s = input().split()
    
    for S in s:
        print(S*int(r), end='')
    print()     # 이게 없으면 계속 end = ''가 적용되어 한 줄로 출력되므로 반드시 추가!
