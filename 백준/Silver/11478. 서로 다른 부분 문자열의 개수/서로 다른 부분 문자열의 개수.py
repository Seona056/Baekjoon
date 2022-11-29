s = input()

count = set()

for i in range(len(s)+1):
    for j in range(1, len(s)+1):
        temp = s[i:i+j]
        if len(temp) == j:
        	count.add(temp)
        
print(len(count))