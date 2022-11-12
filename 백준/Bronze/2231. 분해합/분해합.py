num = int(input())
print(min([n for n in range(max(num-54, num//2), num) if sum(map(int, str(n)))+n == num], default=0))