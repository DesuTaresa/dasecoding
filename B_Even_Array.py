t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
   
    odd =0
    even =0
    for j in range(n):
        if j%2!=lst[j]%2 :
            if lst[j]%2!=0:
                odd+=1
            else:
                even +=1
    if odd==even:
        print(odd)
    else:
        print(-1)