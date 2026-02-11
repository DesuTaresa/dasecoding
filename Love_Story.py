n=int(input())
st="codeforces"
c=0
i=len(st)
for j in range(1,n+1):
    s=input()
    while i>0:
        if s[i]!=st[i]:
            c+=1
        i-=1
    print(c)
