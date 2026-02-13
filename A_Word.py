s = input()
up = 0
lo = 0
for i in range(len(s)):
    if s[i] == s[i].upper():
        up += 1
    else:
        lo += 1
if up <= lo :
    print(s.lower())
else:
    print(s.upper())