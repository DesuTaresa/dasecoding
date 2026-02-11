s = input()
h = input()
c = ""

for i in range(len(s)):
    if s[i]!=h[i]:
        c += "1"
    else:
        c += "0"

print(c)