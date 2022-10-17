def generator(num: int):
    sum_numbers = 0
    for n in str(num):
        sum_numbers += int(n)
    return num + sum_numbers

self_num = set()

for i in range(1, 10001):
    new = generator(i)
    self_num.add(new)
    if i in self_num:
        pass
    else:
        print(i)
