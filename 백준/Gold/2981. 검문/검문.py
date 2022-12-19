# 나머지가 같은 수를 구하기 위해서는, 오름차순으로 정렬한 뒤 두 수의 차를 구한다.
# a-b, b-c, c-d
# 이 차들의 최대 공약수를 구한 뒤, 최대 공약수의 약수들을 출력 (1 제외)

import sys
import math

nums = sys.stdin.readlines()
n = int(nums[0])
nums = sorted(map(int, nums[1:]))
sub = []

for i in range(n-1):
    sub.append(nums[i+1] - nums[i])

gcd = math.gcd(*sub)    
f = set()

for j in range(2, int(gcd**0.5)+1):	# 자연수 n의 최대 약수 : sqrt(n)
	if gcd % j == 0:
		f.add(j)
		f.add(gcd//j)

print(*sorted(f), gcd)
