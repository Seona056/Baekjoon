n = int(input())
count = 99

if n == 1000:
    n = 999
    
if n < 100:
    print(n)
elif 100 <= n < 1000:
    for i in range(100, n+1):
        [a, b, c] = [int(j) for j in str(i)]      # str로 for문은 돌릴 수 있지만, map은 사용 못 함
        if b-a == c-b:
            count += 1
    print(count)