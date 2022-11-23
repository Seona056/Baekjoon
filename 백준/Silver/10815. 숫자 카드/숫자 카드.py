import sys
input = sys.stdin.readlines

sangun, card = sys.stdin.read().split('\n')[1::2]	# idx 1, 3 요소를 각각의 변수에 담는다.
sangun = set(sangun.split())
card = card.split()
print(' '.join('1' if c in sangun else '0' for c in card))    # join은 str만 가능하므로 1, 0 str로 설정