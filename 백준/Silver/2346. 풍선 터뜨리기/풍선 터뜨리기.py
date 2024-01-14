def main():
	count = int(input())
	balloons = [(i+1, delta) for i, delta in enumerate(map(int, input().split()))]
	
	i = 0
	while balloons:
		index, delta = balloons.pop(i)
		
		print(index, end=' ')
		count -= 1
		
		if not count:
			break
		
		if delta > 0:
			delta -= 1
		i += delta
		i %= count
		

if __name__ == '__main__':
	main()