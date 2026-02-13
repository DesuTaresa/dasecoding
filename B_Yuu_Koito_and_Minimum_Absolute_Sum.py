n = int(input())
for i in range(n):
    m = int(input())
    lst = list(map(int, input().split()))
    total = 0
    for j in range(1,m):
        if lst[j]==-1:
            lst[j] =0
        if (j!=1 or j!=n-1) and lst[j]!=-1 :
            total += lst[j]-lst[j-1]
    if "-1" not in lst:
        print(total)
        print(*lst)
    elif lst[0]==-1 and lst[m-1]==-1:
        btotal= total-lst[0]+lst[m-2]
        if btotal>0:
            lst[0]=0
            lst[m-1]=abs(btotal)
        elif btotal==0:
            lst[0]=0
            lst[m-1]=0
        else:
            lst[0]=0
            lst[m-1]=btotal

