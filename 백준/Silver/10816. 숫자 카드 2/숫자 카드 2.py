import collections

sangun, card = open(0).read().split('\n')[1::2]

sangun = [*map(int, sangun.split())]
card = [*map(int, card.split())]

b = collections.Counter(sangun)
sangun = set(sangun)

print(' '.join(str(b[c]) if c in sangun else '0' for c in card))