n=list(map(int, input().split()))
wsum=0
msum=-1
k=3
for i in range(k):
    wsum+=n[i]
for i in range(k, len(n)):
    wsum=wsum+n[i]-n[i-3]
    msum=max(msum, wsum)
print(msum)