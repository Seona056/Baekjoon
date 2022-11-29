n, m, *people = open(0).read().split()

no_hear = set(people[:int(n)])
no_see = set(people[int(n):])
intersection = sorted(no_hear & no_see)

print(len(intersection))
print('\n'.join(intersection))