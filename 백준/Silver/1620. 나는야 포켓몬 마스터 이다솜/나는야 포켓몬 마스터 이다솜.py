m, a, *pokemon = open(0).read().split()

dogam_idx = {i+1:p for i, p in enumerate(pokemon[:int(m)])}
dogam_pokemon = {p:i+1 for i, p in enumerate(pokemon[:int(m)])}

for q in pokemon[int(m):]:
	print(dogam_pokemon[q]) if q.isalpha() == True else print(dogam_idx[int(q)])