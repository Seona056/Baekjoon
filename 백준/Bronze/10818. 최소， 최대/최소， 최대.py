# 첫 번째 답
# 메모리: 149432 KB, 시간: 716 ms

n = input()
nums = sorted(list(map(int, input().split())))

print(nums[0])
print(nums[-1])



# 두 번째 답
# 메모리: 148408 KB, 시간: 408 ms
# 가장 빠른 답
# 리스트 컴프리헨션보다 map이 더 빨랐다.

n = input()
nums = list(map(int, input().split()))

print(min(nums))
print(max(nums))



# 두 번째 답
# 메모리: 149432 KB, 시간: 472 ms

n = input()
nums = [int(i) for i in input().split()]

print(min(nums))
print(max(nums))
