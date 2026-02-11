t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    if n==1:
        print("YES")
    else:
        for i in range(1,n):
            if abs(lst[i]-lst[i-1])>1:
                print("NO")
                break
            if i ==n-1:
                print("YES")