# 메모리: 31256 KB, 시간: 76 ms
# 아주 오래 걸림
# get_lines 함수에서 종료 포인트만 설정하면 될 것 같은데, if first > end 에서 뭘 반환해야할 지 오래 고민함
# 다른 답들은 while문으로 해결(내 코드와 거의 같음)했지만, 함수를 만들어서 풀고싶었기에 장고&폭풍 검색
# 오답 풀이는 맨 아래에 👇👇👇👇👇👇👇

def get_lines(n, first, end):
	
	if first > end:
		return end
	
	mid = (end+first)//2
	c = sum(map(lambda x: x//mid, lines))
	
	if c >= n:
		return get_lines(n, mid+1, end)
	else:
		return get_lines(n, first, mid-1)


import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

print(get_lines(n, 1, max(lines)))


---------------------------------------------------------
# 오답 풀이

def get_lines(n, first, end, pre_mid=False):	# 3️⃣
	
	if first >= end:
		return pre_mid		# 4️⃣
	
	mid = (end+first)//2
	c = sum(map(lambda x: x//mid, lines))
	
	if c == n:				# 2️⃣
		return mid
	elif c > n:
		return get_lines(n, mid+1, end, mid)
	elif c < n:
		return get_lines(n, first, mid-1, mid)


import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

print(get_lines(n, 1, min(lines)))		# 1️⃣




# 1️⃣ : min(lines) 👉 max(lines) 변경
# 문제에서 오해의 소지가 있는 것이, "이미 갖고 있던 k개의 랜선을 이용해 같은 길이의 랜선 n개로 만드는 최대값을 구하라"라는 문제였는데, k개를 모두 사용해야한다고 생각해서 min(lines)를 사용했다
# 질문게시판을 찾아보니, k개의 랜선을 모두 사용하지 않아도 된다고 함. 동일한 길이가 n개 이상이 되는 최대 길이만 찾으면 되는 것
# 문제도 다시 찬찬히 읽어보면 그렇게 읽히기도 해서... 중의적이라고 생각하지만 일단은 이해 완료

# 2️⃣ : if c == n: return mid 👉 삭제 및 if c >= n: return return get_lines(n, mid+1, end)로 변경
# c와 n이 같다면 무조건 조건이 성립되어 바로 mid를 출력하도록 구성했는데, 
# c와 n이 같아지는 경우의 수가 1개가 아니었고, c == n의 경우에서도 가장 큰 값을 반환해야 하기 때문에 다음 재귀로 이어지도록 설계
# 그리고 여기서 mid를 출력하도록 하면 혹시나 c와 n이 딱 맞아 떨어지는 경우가 아닐 경우, 종료 조건이 애매해진다.

# 3️⃣ 함수 인자 pre_mid(또는 pre_end) 삭제
# 2️⃣에서 mid로 반환을 해버리고 나면, 나머지 c > n 만 나올 수 밖에 없는 답에서는 답을 리턴하기가 애매해져서 이전 mid, end등을 if first > end 에서 반환하도록 설계
# 문제가 많이 꼬이지 않았다면 이것으로도 답이 나오는 경우가 많았음
# 하지만 100% 정답이 나오지 않았기 때문에 다른 방법을 찾아야 했다.

# 4️⃣ if first >= end: return pre_end 👉 if first > end: return end
# 이 종료 조건 때문에 엄청 고민을 많이 함. 이 부분이 아닌 내 코드는 다른 정답들과 거의 비슷했는데, 다른 정답들은 이 부분을 while문으로 해결했음
# 나는 이왕 함수로 짠 김에 재귀 함수에 대한 이해도를 높이고 싶어서 서치를 계속함 👉 [1092] 수 찾기 답을 참고한 것인데, 수 찾기에서는 0아니면 1 반환값이어서 이 조건이 간단했음
# first와 end가 같은 상황도 정상적인 상황이 아니라고 판단하여 조건에 넣었는데, first == end일 때도 c > n이어야만 답이 되는 것을 간과함
# 2️⃣로 조건을 변경하면서 first == end and c >= n이면 다음 재귀에서 first=mid+1, end=mid 가 되므로 first와 end가 역전되는 순간이 답이 된다. 
# 👉 여기까지 생각하면 if first >= end: return end 로 바꿔도 된다고 생각할 수 있지만,
# 혹시 first == end and c < n이 된다면 다음 재귀는 first=mid, end=mid-1이 되면서 똑같이 first와 end가 역전되지만, end의 값이 -1이 된다.
# 이 두 가지를 모두 고려해서 종료 조건을 걸어줘야해서 코드 설명을 읽어봤지만 다시 이해하는데에 시간이 더 걸렸음


-----------------------------------
# 반례

4 11
899
799
499
539

