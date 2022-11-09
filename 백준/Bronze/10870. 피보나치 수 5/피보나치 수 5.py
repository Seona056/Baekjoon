import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    pre = 0
    f = 1
    for i in range(n-1):
        f += pre
        pre = f-pre
    print(f)