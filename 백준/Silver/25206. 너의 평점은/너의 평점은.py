# 첫 번째 답
# 메모리: 31256 KB, 시간: 44 ms

import sys
table = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0, 'P': 0}
ch = sys.stdin.readlines()	# chihoon
total_c, total_p = 0, 0

for a in ch:
	_, c, p = a.split()	# credit, point
	total_p += float(c) * table[p]
	if p == 'P':
		c = 0
	total_c += float(c)
	
print(total_p/total_c)


----------------------------------------------------------
# 두 번째 답
# 메모리: 31256 KB, 시간: 40 ms
# 첫 번째 답과 달라진 것은 for문 안에 c = float(c)를 넣어준 것 뿐인데 시간이 조금 더 빨라졌다. 
# 같은 작업을 두 번 연산하게하는 것이 그만큼 시간을 소요시키는 원인이 된 것이 신기했다... 그저 float()일 뿐인데...

import sys
table = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1, 'F': 0, 'P': 0}
ch = sys.stdin.readlines()
total_c, total_p = 0, 0	# credit, point

for a in ch:
	_, c, p = a.split()
	c = float(c)
	total_p += c * table[p]
	if p == 'P':
		c = 0
	total_c += c
	
print(total_p/total_c)
