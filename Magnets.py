n = int(input())
s=input()
count=1
for i in range(n-1):
    h=input()
    if h!=s:
        count+=1
        s=h
print(count)




