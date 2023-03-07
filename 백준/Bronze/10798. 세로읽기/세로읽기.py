# 첫 번째 답
# 메모리: 31256 KB, 시간: 40 ms
# 리스트에서 IndexError가 나면 ✔try/except✔을 쓰는 것이 효과적!👍

import sys
words = sys.stdin.readlines()
f = list(words[0].strip())	# first

for word in words[1:]:
	word = word.strip()
	i = 0
	for w in word:
		try:
			f[i] += w
		except:
			f.append(w)
		i += 1
		
print(''.join(f))
