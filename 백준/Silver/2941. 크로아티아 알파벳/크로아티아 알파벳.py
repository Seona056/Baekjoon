word = input()

croatia = sorted(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='], key=lambda x: len(x))[::-1]
count = 0

for c in croatia:
    if c in word:
        count += word.count(c)
        word = word.replace(c, '*')

word = word.replace('*', '')
print(len(word)+count)