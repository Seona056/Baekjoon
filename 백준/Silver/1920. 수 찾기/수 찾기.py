# 첫 번쨰 답
# 메모리: 44204 KB, 시간: 484 ms
# 이분 탐색을 이용한 찾기 (재귀를 이용한 이분 탐색)
# 이분 탐색을 사용하려면 탐색하려는 배열이 ✔오름차순으로 정렬되어 있어야 한다❗

def binary(a:list, t:int, s:int, e:int):
	'''
	a : list
	t : target
	s : start
	e : end
	m : mid
	'''
	if s > e:
		return 0
	
	m = (s+e)//2
	
	if a[m] == t:
		return 1
	elif a[m] > t:
		return binary(a, t, s, m-1)
	else:
		return binary(a, t, m+1, e)
		
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))   # 오름차순으로 정렬
input()

if __name__ == '__main__':	
	for i in input().split():
		print(binary(a, int(i), 0, n-1))

------------------------------------------------------------
# 두 번쨰 답
# 메모리: 48724 KB, 시간: 144 ms
# 빠른 답을 보니 그냥 in을 사용해서 바로 찾음...
# ❗in을 사용할 때, 리스트가 아닌 집합(set)을 사용해야 한다.❗ 👉 https://www.notion.so/16-77e854a60dee4549b666c06f08810e48?pvs=4#5cc42eb5ea3c4dd1904d26f45d4ca057

a, b = open(0).readlines()[1::2]
a = set(map(int, a.split()))
print('\n'.join(map(str, [1 if int(x) in a else 0 for x in b.split()])))
