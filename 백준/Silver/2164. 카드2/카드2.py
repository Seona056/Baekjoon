import collections

n = int(input())
cards = collections.deque(range(2, n+1, 2))

if n == 1:
	print(1)
else:
	if n % 2 != 0:
		cards.append(cards[0])
		cards.popleft()

	while len(cards) > 2:
		cards.append(cards[1])
		for i in range(2):
			cards.popleft()
	print(cards[-1])