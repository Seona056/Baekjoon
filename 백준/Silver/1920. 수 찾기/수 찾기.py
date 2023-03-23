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
a = sorted(map(int, input().split()))
input()

if __name__ == '__main__':	
	for i in input().split():
		print(binary(a, int(i), 0, n-1))