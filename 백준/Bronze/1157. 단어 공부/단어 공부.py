from collections import Counter

s = input().upper()
cnt = Counter(s).most_common(2)

if len(cnt) == 1:
	print(s[0])
else:
	[(a, b), (c, d)] = cnt
	print('?' if b==d else a)