n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    if b not in lst:
        print("NO")
    else:
        if a==2:
            print("YES")
        