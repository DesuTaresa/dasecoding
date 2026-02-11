s=input()
lst=["A", "O", "Y", "E","U","I"]
lts=[]
for i in range(len(s)):
    if s[i].upper() not in lst:
        lts.append(".")
        lts.append(s[i])
print("".join(lts).lower())