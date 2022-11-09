import sys
n = int(sys.stdin.readline())
pre = 0
f = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n-1):
        pre, f = f, pre+f
    print(f)
