import sys
input = lambda: sys.stdin.readline()
most = []

for i in range(9):
    l = list(map(int, input().split()))
    most.append((max(l), l.index(max(l))+1))

a = max(most, key=lambda x: x[0])
print(a[0])
print(most.index(a)+1, a[1])