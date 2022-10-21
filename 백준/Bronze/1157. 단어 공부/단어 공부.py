from collections import Counter

alpha = list(map(str, input().upper()))
count = Counter(alpha).most_common()

if len(alpha) == 1:
    print(alpha[0])
else:     
    if count[0][1] == count[1][1]:
        print('?')
    else:
        print(count[0][0])