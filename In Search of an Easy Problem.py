n=int(input())
lst=list(map(int,input().split()))
lst1=[]
lst2=[]
for i in range(n):
    if lst[i]==0:
        lst1.append(lst[i])
    elif lst[i]==1:
        lst2.append(lst[i])
if len(lst2)>0:
    print("HARD")
elif len(lst2)==0:
    print("EASY")