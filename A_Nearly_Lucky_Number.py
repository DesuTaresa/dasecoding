n = int(input())
s = str(n)
print(s)
print(s[2])
lst = [4,7]
counter = 0
for i in s:
    if i in lst:
        counter +=1
print(counter)
if counter==0:
    print("yes")
else:
    print("NO")