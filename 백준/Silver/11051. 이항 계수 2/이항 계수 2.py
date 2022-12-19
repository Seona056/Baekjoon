# 이항계수 : n!/k!(n-k!)

from math import factorial as f
n, k = map(int, input().split())

print(f(n)//(f(k)*f(n-k))%10007)