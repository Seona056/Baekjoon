def hanoi(n, first, last, middle):

    if n == 1:
        return print(first, last)
    
    hanoi(n-1, first, middle, last)
    print(first, last)
    hanoi(n-1, middle, last, first)

n = int(input())
print(2**n -1)
hanoi(n, 1, 3, 2)