import sys

n, m = map(int, sys.stdin.readline().split())
a_matrix = list(list(map(int, sys.stdin.readline().split())) for i in range(n))  

for a in a_matrix:
    b = list(map(int, sys.stdin.readline().split()))
    for i, j in zip(a, b):
        print(i+j, end=' ')
    print()