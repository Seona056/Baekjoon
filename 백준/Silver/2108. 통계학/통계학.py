import sys
input = sys.stdin.buffer.readlines

nums = list(map(int, input()))
n = nums[0]
nums = sorted(nums[1:])

print(round(sum(nums)/n))
print(nums[n//2])

import collections

a = collections.Counter(nums).most_common(2)
if n == 1:
    print(a[0][0])
else:
    if a[0][1] == a[1][1]:
        print(a[1][0])
    else:
        print(a[0][0])
print(abs(max(nums)-min(nums)))