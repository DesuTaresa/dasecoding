n, k=map(int,input().split())
for i in range(k):
    sum=str(n)[-1]
    if sum=="0":
        n//=10
    else:
        n-=1
print(n)