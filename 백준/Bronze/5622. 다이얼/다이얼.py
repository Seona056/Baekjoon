total = input()

alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
time = [i for i in range(3, 11)]*3
time.append(8)
time.append(10)
time.sort()
total_a = 0

for t in total:
    idx = alpha.index(t)
    total_a += time[idx]

print(total_a)
    