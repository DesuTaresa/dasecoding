n = int(input())
lst = list(map(int,input().split()))
counter =0
for i in range(1,n):
    if lst[i]>max(lst[:i]) or lst[i]<min(lst[:i]):
        counter +=1
print(counter)