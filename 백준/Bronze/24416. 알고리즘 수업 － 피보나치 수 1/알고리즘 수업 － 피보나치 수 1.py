n = int(input())
f = [0,1,1]
for i in range(3, n+1):
    f.append(f[-1]+f[-2])
print(f[n], n-2)