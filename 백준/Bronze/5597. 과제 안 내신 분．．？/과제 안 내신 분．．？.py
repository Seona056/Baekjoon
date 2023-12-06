# 내가 푼 답
# 메모리 : 30840 KB, 시간 : 68 ms
# 1~31까지의 리스트를 만들고 확인된 숫자는 리스트에서 삭제하여 2개의 숫자만 남긴다.
# sort 후 인덱스를 통해 출력

import sys

student = list(i for i in range(1, 31))
for i in range(28):
    submit = int(sys.stdin.readline().rstrip())
    student.remove(submit)
    
student.sort()
print(student[0])
print(student[1])


------------------------------------------------------------------------
# 내가 푼 답 (변형)
# 메모리 : 31120 KB, 시간 : 44 ms
# 위의 답에서 sort를 빼고 min, max를 이용해서 출력했다.
# sort가 메모리와 시간을 모두 많이 잡아먹는줄 알았는데, 오히려 메모리는 더 증가했다.

import sys

student = list(i for i in range(1, 31))
for i in range(28):
    submit = int(sys.stdin.readline().rstrip())
    student.remove(submit)
    
print(min(student))
print(max(student))


------------------------------------------------------------------------
# 소연님이 푼 답
# 메모리 : 31120 KB, 시간 : 40 ms
# 0으로 채워진 리스트에 제출한 번호를 채운 뒤, 0을 찾는 방법으로 푸는 방식
# 0을 찾는 방법을 다시 for문을 돌려서 찾는 방식이 신기했다.

n_list = [0]*30

for _ in range(28):
	n = int(input())
	n_list[n-1] = n
	
for i in range(30):
	if n_list[i] == 0:
		print(i+1)


------------------------------------------------------------------------
# 가장 빠른 답
# 메모리 : 31120 KB, 시간 : 40 ms
# 집합의 연산으로 풀이 (대칭차집합)
# '-'연산으로도 같은 답이 나오지 않을까 해서 풀어봤는데 오름차순 정렬을 따로 시켜줘야만 했다.


print(*{*map(int, open(0))}^{*range(1,31)})
