n=list(int(input()))
m=list(int(input()))
for i in range(1,n):
    for j in range(1,m):
        if i==n[i] and i!=j:
            print( YES)
        else:
            print(NO)