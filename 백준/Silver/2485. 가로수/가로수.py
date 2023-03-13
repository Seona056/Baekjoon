import math
n, *trees = map(int, open(0).readlines())
gap = math.gcd(*[x-y for x,y in zip(trees[1:], trees)])
all = (trees[-1]-trees[0]) // gap + 1
print(all-n)