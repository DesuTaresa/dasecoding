n = int(input())
lst = list(map(int, input().split()))
serej =0
dima = 0
l=0
r =n-1
i = 1
while l<=r:
    
    if lst[l]>lst[r]:
        if i%2 !=0:
            serej +=lst[l]
        else:
            dima +=lst[l]
        l+=1
    else:
        if i%2 !=0:
            serej +=lst[r]
        else:
            dima +=lst[r]
        r-=1
    i+=1
print(serej , dima)