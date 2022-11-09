def star(n: int):
    if n == 3:
        return ['***','* *', '***']
    f = [s*3 for s in star(n//3)]   # first
    s = [s+(len(s)*' ')+s for s in star(n//3)]   # second
    return f+s+f

n = int(input())
print('\n'.join(star(n)))