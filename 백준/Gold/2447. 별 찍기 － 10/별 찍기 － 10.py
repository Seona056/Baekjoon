def star(n: int):
    if n == 3:
        return ['***','* *', '***']
    return [s*3 for s in star(n//3)]+[s+(len(s)*' ')+s for s in star(n//3)]+[s*3 for s in star(n//3)]

import sys 
n = int(sys.stdin.readline())
print('\n'.join(star(n)))