import sys

words = set(sys.stdin.readlines()[1:])
words = list(words)
words.sort()
words.sort(key=len)
print(''.join(words))