t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    msum = 0
    for i in lst:
        if i%2!=0:
            msum+=1
    if msum%2 == 0:
        print("YES")
    else:
        print("NO")
