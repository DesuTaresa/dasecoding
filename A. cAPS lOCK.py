n = input()
if n[0]==n[0].lower() and n[1:]==n[1:].upper() or n==n.upper():
    print(n.capitalize())
else:
    print(n)