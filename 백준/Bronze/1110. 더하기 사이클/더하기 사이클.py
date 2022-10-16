origin = input().zfill(2)  # str로 받음
count = 0
n = origin

while True:
    new_num = n[-1] + str(int(n[0])+int(n[-1]))[-1]
    count += 1
    
    if new_num == origin:
        print(count)
        break
    else:
        n = new_num