import sys

n = int(sys.stdin.readline())
answer = 0

for i in range(n):
    sequence = sys.stdin.readline()
    set_s = set(sequence)
    t = 0

    for s in set_s:
        c = sequence.count(s)
        if s*c not in sequence:
            t += 1

    if t == 0:
        answer += 1

print(answer)