# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

k, q, l, b, n, p = map(int, input().split())

for b, w in zip([1,1,2,2,2,8], [k,q,l,b,n,p]):
    print(b-w)
    
