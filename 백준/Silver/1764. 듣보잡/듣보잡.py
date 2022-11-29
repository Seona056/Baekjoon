# 첫 번째 답
# 메모리: 51680 KB, 시간: 140 ms
# 주어진 수 n, m과 set의 len을 이용해 듣보잡의 수를 빠르게 구한다.
# 그 수를 이용하여 most_common을 이용하여 답을 출력

import sys
import collections

n, m, *people = open(0).read().split()

a1 = int(n)+int(m) - len(set(people))
print(a1)

no = sorted(collections.Counter(people).most_common(a1))
print('\n'.join(no[i][0] for i in range(a1)))


----------------------------------------------------------
# 두 번째 답
# 메모리: 45636 KB, 시간: 104 ms
# 가장 빠른 답을 참고
# set에서 교집합과 합집합을 구하는 연산을 사용할 수 있었다!
# 교집합 : set.intersection(set_1, set_2) 또는 set_1 & set_2
# 합집합 : set.union(set_1, set_2) 또는 set_1 | set_2
# 차집합 및 대칭 차집합은 노션에 정리 : https://lovely-sand-5da.notion.site/f04a9ec5c4314a85b0ae981d9ab91391

import sys

n, m, *people = open(0).read().split()

print(int(n)+int(m) - len(set(people)))

no_hear = set(people[:int(n)])
no_see = set(people[int(n):])

print('\n'.join(sorted(set.intersection(no_hear, no_see))))


----------------------------------------------------------
# 마지막 답
# 메모리: 43588 KB, 시간: 100 ms
# intersection(교집합)을 구한 후 len을 출력

n, m, *people = open(0).read().split()

no_hear = set(people[:int(n)])
no_see = set(people[int(n):])
intersection = sorted(no_hear & no_see)

print(len(intersection))
print('\n'.join(intersection))
