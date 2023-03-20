marbles = open(0).readlines()
w, h = [], []

for m in marbles[1:]:
	x, y = map(int, m.split())
	w.append(x)
	h.append(y)

print((max(w)-min(w))*(max(h)-min(h)))