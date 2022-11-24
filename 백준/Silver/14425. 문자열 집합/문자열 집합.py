# 첫 번째 답
# 메모리: 50712 KB, 시간: 104 ms
# 리스트의 len을 구하는 방법으로 작성
# 두 번째 답과 시간은 같지만, 메모리가 조금 더 소요됨

import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

print(len([c for c in check if c in S]))


# 두 번째 답
# 메모리: 50580 KB, 시간: 104 ms
# 새로운 리스트를 만들지 않아서 메모리가 조금 적게 소요됨
# 소요시간은 위와 동일

import sys

S = sys.stdin.read().split()

check = S[int(S[0])+2:]
S = set(S[2:int(S[0])+2])

c = 0    # count
for ch in check:
    if ch in S:
        c += 1
print(c)


# 마지막 답
# 메모리: 50572 KB, 시간: 112 ms
# 랭킹에 있었던 답! 새로운 코드 작성법이라 연습해 보았다.
# open(0).read().split()의 출력 결과를 확인해 보자! 👇👇👇 맨 아래에 👇👇👇

n, _, *words = open(0).read().split()       # ❗💡❗ 새로운 변수 할당법이므로 알아둘 것!

n=int(n)
s ={*words[:n]}

print(sum(w in s for w in words[n:]))	# 👉 True, False를 리스트로 반환

# w for w in words[n:] if w in s 와 다름! 👉 해당 요소를 리스트로 반환
# print(sum(filter(lambda w: w in s, words[n:]))) ❌ 문자열 요소들을 sum할 수 없다.



# ✔ 참고 ✔

# [10815] 숫자카드 문제에서 나왔던 sys.stdin.read()와 같은 동작

# open(0).read()의 출력 ➡ 입력한 그대로 반환

5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

# open(0).read().split()의 출력 ➡ 리스트로 반환된다.

['5', '11', 'baekjoononlinejudge', 'startlink', 'codeplus', 'sundaycoding', 'codingsh', 'baekjoon', 'codeplus', 'codeminus', 'startlink', 'starlink', 'sundaycoding', 'codingsh', 'codinghs', 'sondaycoding', 'startrink', 'icerink']
