lst = list(map(int, input().split()))
counter = 0
for i in range(1,4):
    if lst[i]==lst[i-1]:
        counter+=1
print(counter)