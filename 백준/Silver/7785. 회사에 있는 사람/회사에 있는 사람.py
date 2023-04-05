# 첫 번째 답
# 메모리: 43060 KB, 시간: 152 ms
# 다른 풀이도 참고할 겸 봤는데, 시간은 단축될 지 모르겠지만 불필요한 코드가 많았다.

import sys
input = sys.stdin.readline
log = set()

for i in range(int(input())):
	n, _ = input().split()
	
	if _ == 'enter':
		log.add(n)
	else:
		log.remove(n)
		
print('\n'.join(sorted(log)[::-1]))


------------------------------------------------
# 실험
# 메모리: 43840 KB, 시간: 180 ms
# 마지막 부분만 애스터리스크를 사용해 봄
# 메모리나 시간이 줄어들 것을 기대했는데, join을 사용한 것 보다 성능이 더 안좋았다.

print(*sorted(log)[::-1])
