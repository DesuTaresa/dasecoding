n=int(input())
for i in range(n):
    m=int(input())
    s=0
    for j in range(m):
        lst=list(map(int, input().split()))
        for i in lst:
            if i!=0:
                s+=m//i
    if s%2==0:
        print("YES")
    else:
        print("NO")