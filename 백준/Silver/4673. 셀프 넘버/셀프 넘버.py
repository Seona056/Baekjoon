# 첫 번째 답
# 메모리: 30840 KB, 시간: 560 ms

def generator(num: int):
    sum_numbers = 0
    for n in str(num):
        sum_numbers += int(n)
    return num + sum_numbers

self_num = []

for i in range(1, 10001):
    new = generator(i)
    self_num.append(new)
    if i in self_num:
        pass
    else:
        print(i)


        
# 두 번째 답
# 메모리: 30840 KB, 시간: 980 ms
# 빈 리스트(self_num)를 생성한 뒤 -> append
# if문에서 set로 바꿨더니 시간이 더 늘어남

def generator(num: int):
    sum_numbers = 0
    for n in str(num):
        sum_numbers += int(n)
    return num + sum_numbers

self_num = []

for i in range(1, 10001):
    new = generator(i)
    self_num.append(new)
    if i in set(self_num):   # set로 변경
        pass
    else:
        print(i)



# 세 번째 답
# 메모리: 30840 KB, 시간: 80 ms
# 가장 빠른 답
# self_num을 set로 생성하는 걸로 바꿨는데 시간이 7분의 1이 됨
# set에서는 append가 아닌 add를 사용한다.

def generator(num: int):
    sum_numbers = 0
    for n in str(num):
        sum_numbers += int(n)
    return num + sum_numbers

self_num = set()   # 빈 set을 생성

for i in range(1, 10001):
    new = generator(i)
    self_num.add(new)   # set에서는 apeend (x), add (o)
    if i in self_num:
        pass
    else:
        print(i)
