s = input()
s =s.lower()
d = input()
d = d.lower()

if s<d:
    print(-1)
elif d<s:
    print(1)
else:
    print(0)