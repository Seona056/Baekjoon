import sys
input = sys.stdin.readline

s = int(input())
sangun = set(map(int, input().split()))
input()
card = list(map(int, input().split()))

for c in card:
	print(1, end=' ') if c in sangun else print(0, end=' ')