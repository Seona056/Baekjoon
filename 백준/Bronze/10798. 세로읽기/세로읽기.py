import sys
words = sys.stdin.readlines()
f = list(words[0].strip())	# first

for word in words[1:]:
	word = word.strip()
	i = 0
	for w in word:
		try:
			f[i] += w
		except IndexError:
			f.append(w)
		i += 1
		
print(''.join(f))