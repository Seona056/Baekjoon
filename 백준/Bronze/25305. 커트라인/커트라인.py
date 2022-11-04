import sys
input = sys.stdin.readline

n, k = map(int, input().split())
student = sorted(list(map(int, input().split())))

print(student[-k])