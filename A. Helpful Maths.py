n= input()
lst =[]

for i in range(len(n)):
    if n[i] == "1" or n[i] == "2" or n[i] == "3":
        lst.append(n[i])
lst.sort()
lst1 = []
for  i in range(len(lst)):
    if i<len(lst)-1:
        lst1.append(lst[i])
        lst1.append("+")
    elif i == len(lst)-1:
        lst1.append(lst[i])
print("".join(lst1))