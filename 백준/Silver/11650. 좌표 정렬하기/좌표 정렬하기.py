coordinates = []

for i in range(int(input())):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates.sort()
for c in coordinates:
    print(*c)