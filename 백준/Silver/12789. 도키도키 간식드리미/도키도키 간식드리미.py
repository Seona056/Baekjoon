from sys import stdin
from collections import deque

def snack(n, order):
    
    temp, order = [], deque(order)
    
    i = 1
    while order:
        o = order.popleft()
        if i == o:
            i += 1
        else:
            temp.append(o)
        
        while temp:
            t = temp[-1] 
            if t == i:
                temp.pop()
                i += 1
            else:
                break
    
    return 'Nice' if not temp else 'Sad'


input = stdin.readline
print(snack(int(input()), map(int, input().split())))