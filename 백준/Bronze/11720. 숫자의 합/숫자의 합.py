# 첫 번째 답
# 메모리: 30840 KB, 시간: 68 ms
# 일반적인 for문

n = input()
nums = input() 
total = 0

for i in nums:
    total += int(i)
print(total)


# 두 번째 답
# 메모리: 30840 KB, 시간: 68 ms
# 시간, 메모리는 똑같음
# 가장 빠른 답을 참고한 코드

input()
print(sum(map(int, input())))
