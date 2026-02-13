n, m = map(int, input().split())
lst1 = []
lst2 = []
for i in range(m):
    lst = list(map(int, input().split()))
    lst1.append(lst[0])
    lst2.append(lst[1])
while len(lst1)>0 and n>min(lst1):
    x = lst1.index(min(lst1))
    n += lst2[x]
    del lst1[x]
    del lst2[x]
if len(lst2) ==0:
    print("YES")
else:
    print("NO")