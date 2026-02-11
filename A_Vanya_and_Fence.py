ni= list(map(int,input().split()))
n=ni[0]
h=ni[1]
ai=list(map(int,input().split()))
w=0
for i in ai:
    if i<=h:
       w+=1
    else:
        w+=2
print(w)
