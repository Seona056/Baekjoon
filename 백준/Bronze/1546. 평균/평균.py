# 첫 번째 답
# 메모리, 시간 동일

n = int(input())
score = list(map(int, input().split()))
print(sum([s/max(score) * 100 for s in score])/n)


# 두 번째 답
# 메모리, 시간 동일

n = int(input())
score = list(map(int, input().split()))
print(sum([s/max(score) * 100 for s in score])/n)
