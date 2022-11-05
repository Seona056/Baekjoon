import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().split()))
nums_idx = sorted(list(set(nums)))
nums_dict = {v:i for i, v in enumerate(nums_idx)}

for n in nums:
    print(nums_dict[n], end=' ')    