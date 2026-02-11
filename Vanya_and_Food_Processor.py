ni=list(map(int, input().split()))
n=ni[0]
h=ni[1]
k=ni[2]
counter=0
ai=list(map(int, input().split()))
c=ai[0]
i=1
while c>0 or i<len(ai)-1:
    if i==len(ai)-1:
        counter+=1
        if c>=k:
            c-=k
        else:
            c=0
            i+=1

    elif c+ai[i]<=h and i<=len(ai):
        c+=ai[i]
        if i<=len(ai)-1:
            i+=1
    else:
        counter+=1
        if c>=k:
            c-=k
        else:
            c=0
print(counter)

