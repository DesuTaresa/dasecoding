n = input()

if n[1:].isupper() or n.isupper():
    print(n.capitalize())
else:
    print(n)