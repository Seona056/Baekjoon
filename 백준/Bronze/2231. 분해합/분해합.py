# 첫 번째 답
# 메모리: 30840 KB, 시간: 1352 ms

n = int(input())
m = 1

while m < n:
    decomposition = sum(map(int ,str(m))) + m
    if decomposition == n:
        print(m)
        break
    m += 1
else:
    print(0)
    

# 두 번째 답
# 메모리: 30840 KB, 시간: 744 ms
# 탐색을 시작하는 m값을 나누기 2를 해서 m//2 탐색 시간을 줄임
# 나오는 답을 보니.. 절반 이하로 내려가진 않는 것 같아서ㅋㅋㅋㅋ

n = int(input())
m = n//2   # 절반으로 변경

while m < n:
    decomposition = sum(map(int ,str(m))) + m
    if decomposition == n:
        print(m)
        break
    m += 1
else:
    print(0)


# 세 번째 답
# 메모리: 30840 KB, 시간: 68 ms
# 가장 빠른 답을 참고 👉 ❗ 변형 ❗ max(num-54, num//2)로 바꿈. 원래는 max(num-54, 1)이었음
# num-54를 하는 이유는❓ 입력 최댓값이 1,000,000인데, 각 자리수 가장 최대로 더할 수 있는 값이 999,999일때 9*6=54이다.
# ✔ min(리스트, default=0) ✔ : 디폴트 값을 정할 수 있는 것을 처음 알았다

num = int(input())
print(min([n for n in range(max(num-54, num//2), num) if sum(map(int, str(n)))+n == num], default=0))
