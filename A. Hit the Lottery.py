n = int(input())
lst = [1, 5, 10, 20, 100]
countt =0
for i in range(4,-1,-1):
    countt +=n//lst[i]
       
    n -= (n//lst[i])*lst[i]
print(countt)
