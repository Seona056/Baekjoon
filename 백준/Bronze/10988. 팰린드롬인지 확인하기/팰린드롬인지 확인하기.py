word = list(input())
l = len(word)

while l > 1:
	if word.pop() != word.pop(0):
		print(0)
		break
	l -= 2

if l <= 1:
	print(1)