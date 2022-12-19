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

for j in range(2, int(gcd**0.5)+1):
	if gcd % j == 0:
		f.add(j)
		f.add(gcd//j)

print(*sorted(f), gcd)