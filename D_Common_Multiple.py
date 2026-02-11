n = int(input())
for i in range(n):
    m = int(input())
    lst = list(map(int, input().split()))
    li =[]
    for j in range(m):
        if lst[j] not in li:
            li.append(lst[j])
    print(len(li))