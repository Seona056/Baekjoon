import string

s = input()

for i in list(string.ascii_lowercase):
    if i in s:
        print(s.index(i))
    else:
        print(-1)