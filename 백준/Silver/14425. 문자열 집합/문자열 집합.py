import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

print(len([c for c in check if c in S]))