n = int(input())
for i in range(n):
    m = int(input())
    lst = list(map(int, input().split()))
    if pow(sum(lst),1/2) == int(pow(sum(lst), 1/2)):
        print("YES")
    else:
        print("NO")