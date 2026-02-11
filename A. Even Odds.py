n , m = map(int,input().split())
lst1=[]
lst2=[]
for i in range(1,n+1):
    if i%2!=0:
        lst1.append(i)
    elif i%2==0:
        lst2.append(i)
lst3=lst1 + lst2
for i in range(1, len(lst3)+1):
    if i==m:
        print(i)
        continue
