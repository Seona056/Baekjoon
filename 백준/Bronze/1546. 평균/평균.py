n = int(input())
score = list(map(int, input().split()))
print(sum([s/max(score) * 100 for s in score])/n)