s=input()
string =""
i=0
while i<len(s):
    if s[i]==".":
        string +="0"
    else:
        if s[i+1]==".":
            string +="1"
        else:
            string +="2"
        i +=1
    i += 1
print(string)