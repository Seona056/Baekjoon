# 첫 번째 답
# 메모리: 31256 KB, 시간: 44 ms
# 문자열을 리스트로 만들고, pop을 이용

word = list(input())
l = len(word)

while l > 1:
	if word.pop() != word.pop(0):
		print(0)
		break
	l -= 2

if l <= 1:
	print(1)

	
----------------------------------------------------------
# 두 번째 답
# 메모리: 31388 KB, 시간: 44 ms
# 리스트로 만들지 않고 인덱스를 이용하여 풀어봄. 역시 메모리가 조금 더 소요됨
# break 전에 l = 0으로 만든 것은 첫 번째 답과 달리, 정상적인 팰린드롬인 경우에는 l의 값이 처음과 변동이 없기 때문에 0(False)로 만들어 준 것

word = input()
l = len(word)

for i in range(l//2):
	if word[i] != word[-1-i]:
		print(0)
		l = 0
		break
	
if l:
	print(1)
