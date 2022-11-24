# 첫 번째 답
# 메모리: 50712 KB, 시간: 104 ms
# 리스트의 len을 구하는 방법으로 작성
# 두 번째 답과 시간은 같지만, 메모리가 조금 더 소요됨

import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

print(len([c for c in check if c in S]))


# 두 번째 답
# 메모리: 50580 KB, 시간: 104 ms
# 새로운 리스트를 만들지 않아서 메모리가 조금 적게 소요됨
# 소요시간은 위와 동일

import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

c = 0    # count
for ch in check:
    if ch in S:
        c += 1
print(c)
