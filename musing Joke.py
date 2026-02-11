n = input()
m = input()
d = input()
h = m +n
lst = list(h)
lst.sort()
lst1 = list(d)
lst1.sort()
if len(h) == len(d) and lst == lst1 :
    print("YES")
else:
    print("NO")