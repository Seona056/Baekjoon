# 첫 번째 답
# 메모리: 30840 KB, 시간: 68 ms

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


# 두 번째 답
# 메모리: 30840 KB, 시간: 68 ms

time = input()

alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)]
total = 0

for t in time:
    if t in alpha[:3]:
        total += 3
    elif t in alpha[3:6]:
        total += 4
    elif t in alpha[6:9]:
        total += 5
    elif t in alpha[9:12]:
        total += 6
    elif t in alpha[12:15]:
        total += 7
    elif t in alpha[15:19]:
        total += 8
    elif t in alpha[19:22]:
        total += 9
    else:
        total += 10        
        
print(total)
