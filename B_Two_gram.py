n = int(input())
s = input()
if len(s)==2:
    print(s)
else:
    di ={}
    l=0
    r =2
    while r<=n:
        di[s[l:r]] =di.get(s[l:r],0)+1
        l+=1
        r+=1
    for i in di:
        if di[i] ==max(di.values()):
            print(i)
            break