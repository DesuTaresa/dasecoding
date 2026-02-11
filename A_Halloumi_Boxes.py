n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    lst1 = lst.copy()
    lst.sort()
    if lst == lst1:
        print("YES")
        
    else:
        for j in range(1,b):
            if lst1[j]<lst1[j-1]:
                lst1[j-1]=lst1[j]
        x=lst1.copy()
        x.sort()
        print(lst1)
        print(x)
        if lst1==x.sort():
            print("YES")
        else:
            print("NO")