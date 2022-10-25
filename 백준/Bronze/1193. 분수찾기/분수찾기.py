n = int(input())

stage = 1

while n > 0:
    n -= stage
    if n > 0:
        stage += 1

if stage % 2 == 0:
    print(f'{stage+n}/{1-n}')
else:
    print(f'{1-n}/{stage+n}')