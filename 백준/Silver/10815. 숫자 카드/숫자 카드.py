# 첫번째 답
# 수많은 도전 끝에 정답... 
# sangun을 list로 만들어서 in으로 찾았더니 무조건 시간초과가 뜸
# 이분 탐색법으로도 해 봤지만, list를 쓰면 무조건 통과가 되지 않는다.
# ❗ set이 그만큼 빠르다는 것을 증명하기 위한 문제 ❗

import sys
input = sys.stdin.readline

s = int(input())
sangun = set(map(int, input().split()))
input()
card = list(map(int, input().split()))

for c in card:
	print(1, end=' ') if c in sangun else print(0, end=' ')


----------------------------------------------------------
# 마지막 답
# 메모리: 128012 KB, 시간: 388 ms
# sys.stdin.readlines()와 sys.stdin.read()의 차이점을 알아본다! 👇👇👇 맨 아래에 👇👇👇

import sys

sangun, card = sys.stdin.read().split('\n')[1::2]	# idx 1, 3 요소를 각각의 변수에 담는다.
sangun = set(sangun.split())
card = card.split()
print(' '.join('1' if c in sangun else '0' for c in card))    # join은 str만 가능하므로 1, 0 str로 설정



----------------------------------------------------------
# ✔ 참고 ✔

# 평소에 자주 쓰던 sys.stdin.readlines()의 출력 ➡ 리스트로 반환된다.
# split('\n')을 사용하려면 반환된 리스트를 다시 map으로 돌려야하는 번거로움이 있었다.

['5\n', '6 3 2 10 -10\n', '8\n', '10 9 -5 2 3 4 5 -10']


# sys.stdin.read()의 출력 ➡ 입력 그대로 반환된다.

5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10


# sys.stdin.read().split('\n')를 사용하면 개행 문자가 제거된 리스트를 바로 반환 받을 수 있다.

['5', '6 3 2 10 -10', '8', '10 9 -5 2 3 4 5 -10']
