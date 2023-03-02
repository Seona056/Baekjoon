import sys
test = sys.stdin.readlines()[1:]
for t in test:
    t = t.rstrip()
    print(f'{t[0]}{t[-1]}')