n = int(input())
countt =0
for i in range(n):
    s = list(map(int,input().split()))
    x = s.count(1)
    if x>=2:
        countt +=1
print(countt)