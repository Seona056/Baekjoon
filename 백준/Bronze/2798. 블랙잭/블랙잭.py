# 프로그래머스 [12977. 소수 만들기]와 같은 방법으로 풀었음
# ✔ itertools.combinations(리스트, 숫자) ✔
# 더 빠른 답을 찾아보니 3중 for문으로 해결... 너무 원시적인 방법 아닌가 해서 itertools.combinations를 씀
# 내 코드가 마음에 든다👍 깰끔✨

import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

def add(card_list: list):
    num_3 = list(itertools.combinations(card_list, 3))   # 조합 : itertools.combinations(리스트, 숫자)
    return max(filter(lambda x: x <= m, map(sum, num_3)))

print(add(cards))
