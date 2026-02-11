n=int(input())
msum1=0
msum2=0
msum3=0
for i in range(n):
    a,b,c=map(int, input().split())
    msum1+=a
    msum2+=b
    msum3+=c
if msum1 == msum2 == msum3 == 0:
    print("YES")
else:
    print("NO")