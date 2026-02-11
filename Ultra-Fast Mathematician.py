n = int(input())
m = int(input())
s=str(n)
h=str(m)
c=[]
for i in range(len(s)-1):
    if s[i]!=h[i]:
        c.append("1")
    else:
        c.append("0")
print(("".join(c)))