s = input()

if len(s) == 1:
    print(s.upper())
elif s[0].lower() == s[0] and s[1:].upper() ==s[1:]:
    print(s.capitalize())
elif s.upper() ==s:
    print(s.lower())
else:
    print(s)