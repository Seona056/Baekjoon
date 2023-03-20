marbles = list(map(int, open(0).read().split()))
w = marbles[1::2]
h = marbles[2::2]
print((max(w)-min(w))*(max(h)-min(h)))