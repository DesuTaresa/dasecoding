t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    l=0
    r=1
    lst1 =[]
    while r<n:
        lst1.append(max(lst[l],lst[r]))
        l+=1
        r+=1
    
    print(min(lst1)-1)
