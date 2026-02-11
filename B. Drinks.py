n = int(input())
lst = list(map(int, input().split()))
msum = 0
for i in lst:
    msum+=i
print(msum/n)