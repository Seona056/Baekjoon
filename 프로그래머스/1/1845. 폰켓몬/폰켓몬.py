def solution(nums):
    n = len(nums) // 2
    k = len(set(nums))
    
    return n if k > n else k 