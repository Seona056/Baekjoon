# 두 번째 답
# 메모리와 시간은 첫번째 답과 같다.
# xor 연산자 (^) : 서로 같은 것은 0, 서로 다른 것은 0이 아닌 값을 반환

rect = open(0).read().split()
x, y = 0, 0

for r in rect[::2]:
	x^=int(r)
for r in rect[1::2]:
	y^=int(r)

print(x, y)
