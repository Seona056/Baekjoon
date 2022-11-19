def recursion(s, l, r):
	global c
	c += 1
	if l >= r: return [1, c]
	elif s[l] != s[r]: return [0, c]
	else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


import sys
# string = sys.stdin.readlines()[1:]      # 이건 통과 안됨
string = list(map(lambda x: x.rstrip(), sys.stdin.readlines()[1:]))

for s in string:
	c = 0
	print(*isPalindrome(s))