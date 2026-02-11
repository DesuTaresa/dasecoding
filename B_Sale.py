n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
total =0
for i in range(m):
    if lst[i]<0:
        total+=abs(lst[i])
print(total)
