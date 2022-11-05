# 첫 번째 답 (오답: 시간초과)
# 주어진 시간 : 2초
# index를 이용하는 것은 for문 한 번에 시간 복잡도 O(N)가 소요됨 👉 nums 모두 반복문을 돌면 O(N^2)

import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().split()))
nums_idx = list(set(nums))
nums_idx.sort()

for n in nums:
    print(nums_idx.index(n), end=' ')

    
# 두 번째 답
# 메모리: 156812 KB, 시간: 1860 ms
# 새 리스트를 만들어 index를 사용하는 것 보다 딕셔너리를 사용하면 빠르다.
# 딕셔너리에서 원소에 접근 하는 것은 amortized O(1) 소요 👉 nums 리스트를 모두 돌면 O(n)
    
import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().split()))
nums_idx = sorted(list(set(nums)))
nums_dict = {v:i for i, v in enumerate(nums_idx)}

for n in nums:
    print(nums_dict[n], end=' ')  
    
    
# 마지막 답
# 메모리: 199500 KB, 시간: 1724 ms
# buffer 추가
# nums_idx 리스트를 새로 만들지 말고 바로 enumerate로 넣음
# print가 아닌 join연산 ✅ join이 print보다 빠른 듯

import sys
input = sys.stdin.buffer.readline

input()
nums = list(map(int, input().split()))
nums_dict = {v:i for i, v in enumerate(sorted(list(set(nums))))}

print(' '.join(map(str, [nums_dict[n] for n in nums])))   
