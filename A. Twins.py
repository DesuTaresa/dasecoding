n = int(input())
lst = list(map(int, input().split()))
lst.sort()
total =1
msum = lst[n-1]

for i in range(n):
    if msum <= sum(lst[0:n-1-i]):
        total +=1
        msum += lst[n-2-i]
print(total)