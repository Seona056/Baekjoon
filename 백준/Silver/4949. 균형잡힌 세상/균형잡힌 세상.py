import sys
import re
txt = sys.stdin.readlines()[:-1]

for t in txt:
	if t[0] == '.':
		print('no')
		continue
    
	t = re.sub('[a-zA-Z0-9]', '', t)
	t = ''.join(t.split())
    
	while any(i in t for i in ['[]', '()']):
		if '()' in t:
			t = t.replace('()', '')
		if '[]' in t:
			t = t.replace('[]', '')
	
	if t != '.':
		print('no')
	else:
		t = list(t)
		c = 0
		for i in range(int(len(t))//2):
			if t[i] != t.pop():
					c += 1
		if c == 0:
			print('yes')
		else:
			print('no')