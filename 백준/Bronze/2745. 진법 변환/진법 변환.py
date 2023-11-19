# 진법 변환 공식이 있음
# n진법은 각 자리수가 n의 거듭제곱을 나타낸다.
# 예 : 123 = (1×10**2)+(2×10**1)+(3×10**0)

------------------------------------------------------------------------
# 내가 푼 답
# dictionary를 이용해서 문제를 풀었다. 
# 메모리: 31252 KB, 시간: 44 ms

import sys
num, b = sys.stdin.read().split()
d = {str(i):i for i in range(10)}
d.update({chr(s).upper():i+10 for i, s in enumerate(range(ord('a'), ord('z')+1))})  # dict.update(dict2), # ord(str) : 해당 문자의 유니코드, # chr(유니코드) : 문자로 변환

a = 0
for i, n in enumerate(num[::-1]):
	a += (int(b)**i) * d[n]
print(a)

------------------------------------------------------------------------
# 블로그에서 참고한 코드
# 메모리: 31252 KB, 시간: 44 ms
# 내 컴퓨터의 인터넷 속도 문제인지 모든 답의 메모리와 속도가 같았다.

import sys
N, b = sys.stdin.read().split()
l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = 0

for i,n in enumerate(N[::-1]):
    a += (int(b)**i)*(l.index(n))
print(a)
------------------------------------------------------------------------
# 가장 빠른 답
# 충격적인 답...
# int()는 10진법의 정수를 출력한다.
# int(n, 진법) : 두 번쨰 인수(base)로 진법을 입력하면 숫자 n은 해당 진법을 따르는 수이다.
# ❓ 하지만 int('ZZZZZ')는 에러가 뜨는데, 어떻게 이런 코드가 작동하는지 궁금해서 좀 더 공부하여 노션에 정리하였다.
# https://lovely-sand-5da.notion.site/18-ac5288cc80144a6886e890aa957baa23?pvs=4

# ✏️ 노션 내용 ✏️
# 1️⃣ int(str, 진법)이 어떻게 가능한가?
# 2️⃣ 👉 n의 각 자리숫자 < 진법 👈 의 규칙을 따라야한다.

n,b=input().split()
print(int(n,int(b)))
