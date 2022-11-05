import sys

def sort_num(n):
    x, y = n.split()
    return int(x) + int(y)/1000000   # 100,000 최고 입력값이므로, 나눴을 때 1 이하가 되도록 0을 하나 더 붙여준다.

coordinates = sys.stdin.readlines()[1:]
coordinates.sort(key=lambda n: sort_num(n))
print(''.join(coordinates))