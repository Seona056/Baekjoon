import sys
input = sys.stdin.buffer.readline

input()
nums = list(map(int, input().split()))
nums_dict = {v:i for i, v in enumerate(sorted(list(set(nums))))}

print(' '.join(map(str, [nums_dict[n] for n in nums])))   