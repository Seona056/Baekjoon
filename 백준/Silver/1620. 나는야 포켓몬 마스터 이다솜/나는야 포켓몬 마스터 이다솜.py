# 첫 번째 답
# 메모리: 68556 KB, 시간: 228 ms
# 변수명.isalpha() : 문자열인지 판단

m, a, *pokemon = open(0).read().split()

dogam_idx = {i+1:p for i, p in enumerate(pokemon[:int(m)])}
dogam_pokemon = {p:i+1 for i, p in enumerate(pokemon[:int(m)])}
question = pokemon[int(m):]

for q in question:
	print(dogam_pokemon[q]) if q.isalpha() == True else print(dogam_idx[int(q)])


----------------------------------------------------------
# 두 번째 답
# 메모리: 68556 KB, 시간: 228 ms
# question 변수 할당을 하지 않고 바로 pokemon[int(m):]를 for문으로 돌리면 시간이 단축될까 싶어 시도해 봄. 👉 변함 없었음

m, a, *pokemon = open(0).read().split()

dogam_idx = {i+1:p for i, p in enumerate(pokemon[:int(m)])}
dogam_pokemon = {p:i+1 for i, p in enumerate(pokemon[:int(m)])}

for q in pokemon[int(m):]:
	print(dogam_pokemon[q]) if q.isalpha() == True else print(dogam_idx[int(q)])

----------------------------------------------------------
# 마지막 답
# 메모리: 60360 KB, 시간: 200 ms
# dictionary를 2개 만들지않고, 포켓몬 → 인덱스 딕셔너리만 만든다.
# 숫자가 question으로 제시된 경우는 pokemon 리스트에서 인덱스로 찾는다.

m, a, *pokemon = open(0).read().split()

dogam_pokemon = {p:i+1 for i, p in enumerate(pokemon[:int(m)])}

for q in pokemon[int(m):]:
	print(dogam_pokemon[q]) if q.isalpha() == True else print(pokemon[int(q)-1])
