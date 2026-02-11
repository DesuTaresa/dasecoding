s=input()
d=input()
if s.lower()<d.lower():
    print("-1")
elif  d.lower()<s.lower():
    print("1")
elif s.lower()==d.lower():
    print("0")