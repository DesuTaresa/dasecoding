n = int(input())
lst = list(map(int,input().split()))
lst.sort()
l = 0
r = 1 
counter = lst.count(4)
while r<(lst.index(4)+1 if 4 in lst else len(lst)+1):
    if sum(lst[l:r+1])>n-lst.count(4)-1 or r == len(lst)-1:
        counter +=1
        l=r
    r+=1
print(counter)

