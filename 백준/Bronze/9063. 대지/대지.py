# 첫 번째 답
# 메모리: 39096 KB, 시간: 96 ms

marbles = open(0).readlines()
w, h = [], []

for m in marbles[1:]:
	x, y = map(int, m.split())
	w.append(x)
	h.append(y)

print((max(w)-min(w))*(max(h)-min(h)))


----------------------------------------------------------
# 두 번째 답
# 메모리: 42172 KB, 시간: 72 ms
# 맞힌 사람 중 가장 빠른 답을 참고
# open(0).read()로 읽어 온 것을 split()해야 각 라인의 입력과 관계없이 각 숫자마다 split()을 할 수 있다. (❌readlines()는 각 줄 마다 다시 반복문을 돌려야한다.)
# 슬라이싱을 이용해 w, h 리스트를 손쉽게 만들 수 있다.

marbles = list(map(int, open(0).read().split()))
w = marbles[1::2]
h = marbles[2::2]
print((max(w)-min(w))*(max(h)-min(h)))
