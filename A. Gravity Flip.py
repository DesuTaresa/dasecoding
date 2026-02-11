n = int(input())
lst = list(map(int, input().split()))
lst.sort()
for i in range(n):
    print(lst[i], end =" ")