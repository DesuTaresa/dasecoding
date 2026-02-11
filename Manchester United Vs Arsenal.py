s=input()
n = 1
m =1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        n += 1
        m = max(m,n)
    else:
        n = 1
if m>=7:
    print("YES")
else:
    print("NO")

