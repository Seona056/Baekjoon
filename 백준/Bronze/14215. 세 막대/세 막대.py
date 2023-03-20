a,b,c = sorted(map(int, open(0).read().split()))
print(a+b+min(c, a+b-1))