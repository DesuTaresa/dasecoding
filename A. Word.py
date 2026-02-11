n=input()
lst1=[]
lst2=[]
for i in range(len(n)):
    if n[i].upper()==n[i]:
        lst1.append(n[i])
    elif n[i].upper()!=n[i]:
        lst2.append(n[i])
if len(lst1)==len(lst2) and len(lst1)<len(lst2):
    print(n.lower())
elif len(lst1)>len(lst2):
    print(n.upper())