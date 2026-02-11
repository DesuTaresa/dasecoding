n  = int(input())
d = " I hate "
h =""
s= ""
a = "it"
while n>1:
    if n%2 ==0:
        h += "that I love "
    else:
        s += "that I hate "
    n-=1
print(d+h+s+a)

