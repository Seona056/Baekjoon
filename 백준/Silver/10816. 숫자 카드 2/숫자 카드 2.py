# 첫 번째 시도 (❌답은 나오지만 시간초과❌)

import collections

sangun, card = open(0).read().split('\n')[1::2]

sangun = [*map(int, sangun.split())]
card = [*map(int, card.split())]

b = collections.Counter(sangun)

print(' '.join(str(b[c]) if c in set(sangun) else '0' for c in card))     # 여기서 set(sangun)


----------------------------------------------------------
# 두 번째 답
# 메모리: 158400 KB, 시간: 800 ms

# 세 번째 답
# 메모리: 263424 KB, 시간: 600 ms
# 같은 코드인데 pypy 3로 제출하니 메모리와 시간이 달라짐

import collections

sangun, card = open(0).read().split('\n')[1::2]

sangun = [*map(int, sangun.split())]
card = [*map(int, card.split())]

b = collections.Counter(sangun)
sangun = set(sangun)      # set으로 변경을 먼저 시켜준다.

print(' '.join(str(b[c]) if c in sangun else '0' for c in card))


----------------------------------------------------------
# 네 번째 답
# 메모리: 267508 KB, 시간: 588 ms
# stdin으로 읽어들이는 방식 변경
# 이 코드를 변경시켜 sys.stdin.readlines()로 변경한 후 시도하니 시간이 더 길어짐

import sys
import collections

stdin = sys.stdin.read().splitlines()
sangun = [*map(int, stdin[1].split())]
card = [*map(int, stdin[3].split())]

b = collections.Counter(sangun)
sangun = set(sangun)

print(' '.join(str(b[c]) if c in sangun else '0' for c in card))
