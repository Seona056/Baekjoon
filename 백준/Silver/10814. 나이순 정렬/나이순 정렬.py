import sys

def sort_age(x):
    a, n = x.split()   # age, name
    return a.zfill(3)

user = sys.stdin.readlines()[1:]
user.sort(key=lambda x: sort_age(x))
print(''.join(user))