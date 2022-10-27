import itertools

def solution(nums):
    
    nums_3 = list(itertools.combinations(nums, 3))
    sum_nums = map(sum, nums_3)
    answer = [n for n in sum_nums if all(map(lambda x : n % x, range(2,n)))]
    
    return len(answer)