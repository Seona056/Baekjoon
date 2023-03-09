# ✔ a와 b의 최소 공배수 = (a*b) // gcd(a, b)
----------------------------------------------------------
# 첫 번째 답
# 메모리: 33376 KB, 시간: 40 ms

import math
a, b = map(int, input().split())
print(math.lcm(a, b))


----------------------------------------------------------
# 두 번째 답
# 메모리: 33376 KB, 시간: 44 ms

import math
print(math.lcm(*map(int, input().split())))
