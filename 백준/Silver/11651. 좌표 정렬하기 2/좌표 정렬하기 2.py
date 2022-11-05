import sys

def sort_num(n):
    x, y = n.split()
    return int(x)/10000000 + int(y)

coordinates = sys.stdin.readlines()[1:]
coordinates.sort(key=lambda n: sort_num(n))
print(''.join(coordinates))