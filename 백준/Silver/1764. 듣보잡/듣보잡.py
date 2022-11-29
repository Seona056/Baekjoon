import sys

n, m, *people = open(0).read().split()

print(int(n)+int(m) - len(set(people)))

no_hear = set(people[:int(n)])
no_see = set(people[int(n):])

print('\n'.join(sorted(set.intersection(no_hear, no_see))))