n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    l=0
    r=1
    d =1
    while r<m:
        if abs(lst[r]-lst[r-1])<=k:
            curr =r-l+1
            d= max(d,curr)
            r+=1
        else:
            l=r
            r=l+1
    print(len(lst)-d)