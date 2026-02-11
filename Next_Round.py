score=list(map(int,input().split()))
n=int(input())
k=int(input())
c=0
for i in range(k,n):
    if score[i]==score[i+1]:
        c=c+k+1
        print(c)
    elif score[i]!=score[i+1]:
        c=c+k
        print(c)