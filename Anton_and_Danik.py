n=int(input())
s=input()
lst1=[]
lst2=[]
for i in range(n):
    if s[i]=="A":
        lst1.append(s[i])
    elif s[i]=="D":
        lst2.append(s[i])
if len(lst1)>len(lst2):
    print("Anton")
elif len(lst2)>len(lst1):
    print("Danik")
elif len(lst1)==len(lst2):
    print("friendship")