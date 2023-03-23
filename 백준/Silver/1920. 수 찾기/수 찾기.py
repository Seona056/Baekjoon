a, b = open(0).readlines()[1::2]
a = set(map(int, a.split()))
print('\n'.join(map(str, [1 if int(x) in a else 0 for x in b.split()])))