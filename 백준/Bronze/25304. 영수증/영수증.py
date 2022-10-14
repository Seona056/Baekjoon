x = int(input())
n = int(input())

for i in range(n):
    
    a, b = map(int, input().split())
    x -= a*b
    
if x == 0:
    print('Yes')
else:
    print('No')
    

# 다른 코드
# total은 x와 같다.
# 0은 False, 0이 아닌 모든 수는 True이다.
# if total : total이 참이면 (0이 아닌 숫자라면) => False

if total :
  print("No")
else :
  print("Yes")
