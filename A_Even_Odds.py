n,m = map(int, input().split())
s=[]
d=[]
h=[]
h=s.extend(d)
for i in range(1,n+1):
    if i%2!=0:
        s.append(i)
    elif i%2==0:
        d.append(i)
h=s.extend(d)
print(h)
print(h[m-1])