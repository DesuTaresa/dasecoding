n=int(input())
mroom=0
for i in range(n):
    a,b=map(int,input().split())
    if a<b:
        mroom+=1
print(mroom)