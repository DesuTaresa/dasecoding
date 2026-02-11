n, m = map(int, input().split())
lst = list(map(int, input().split()))
r = n-1
l =0
lst.sort()
xmax = max(lst)
print(xmax)
while r<m:
    xmax= min( xmax, lst[r]-lst[l])
    r +=1
    l +=1
print(xmax)