x, y, w, h = map(int, open(0).read().split())
print(min(x, y, abs(w-x), abs(h-y)))