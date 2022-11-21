def merge_sort(A : list, l, r, k):          # left, right
    if l < r:
        half = (l+r) // 2           # l과 r의 중간 지점
        merge_sort(A, l, half, k)      # half를 기준으로 앞 부분
        merge_sort(A, half+1, r, k)    # half를 기준으로 뒷 부분
        merge(A, l, half, r, k)
 
    
def merge(A:list, l, half, r, k):
    i, j = l, half+1
    temp = []
    while i <= half and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    while i <= half:
        temp.append(A[i])
        i += 1
    while j <= r:
        temp.append(A[j])
        j += 1
    i, t = l, 0      # t : temp의 index
    global count, result
    
    while i <= r:
        A[i] = temp[t]
        count += 1
        if count == k:
            result = A[i]
            break
        i += 1
        t += 1
 

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
 
count, result = 0, -1
merge_sort(a, 0, n-1, k)
print(result)