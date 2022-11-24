import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

c = 0    # count
for ch in check:
    if ch in S:
        c += 1
print(c)