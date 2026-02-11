n = input()
count = 0
for i in range(1,len(n)):
    if n[i] ==n[i-1]  and n[i]  == "4" or n[i]  == n[i-1]  and n[i]  == "7":
        count +=1
    else:
        count +=0
if count !=0  and len(n)>1:
    print("YES")
else:
    print("NO")