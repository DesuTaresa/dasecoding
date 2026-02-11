lst=list(map(int, input().split()))
a=lst[0]
b=lst[1]
c=lst[2]
d=lst[3]
x=min(a,c,d)
y=a-min(a,c,d)
z=min(y,b)
#max=0
if a==1 and b==1 and c==1 and d==1:
    print(256)
else:
    print(x*256 + z*32)
     