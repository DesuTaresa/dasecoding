n = input()
r = 198
l=0
s= r+1
while l<r:
    if len(set(n))!=len(n):
        s +=1
        r +=1
        l +=1
print(s)