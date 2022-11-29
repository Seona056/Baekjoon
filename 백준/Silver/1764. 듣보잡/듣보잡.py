import sys
import collections

n, m, *people = open(0).read().split()

a1 = int(n)+int(m) - len(set(people))
print(a1)

no = sorted(collections.Counter(people).most_common(a1))
print('\n'.join(no[i][0] for i in range(a1)))