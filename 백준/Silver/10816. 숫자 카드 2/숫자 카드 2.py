import sys
import collections

stdin = sys.stdin.read().splitlines()
sangun = [*map(int, stdin[1].split())]
card = [*map(int, stdin[3].split())]

b = collections.Counter(sangun)
sangun = set(sangun)

print(' '.join(str(b[c]) if c in sangun else '0' for c in card))