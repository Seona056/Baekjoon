import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

def add(card_list: list):
    num_3 = list(itertools.combinations(card_list, 3))   # 조합 : itertools.combinations(리스트, 숫자)
    return max(filter(lambda x: x <= m, map(sum, num_3)))

print(add(cards))