n = int(input())
s = list(input())
h = "ACGT"
a = s.count("A")
c = s.count("C")
g = s.count("G")
t = s.count("T")
q = s.count("?")
Max =max(a,c,g,t)
if Max<len(s)//4:
    Max =len(s)//4
if n%4!=0 or 4*Max-(a+c+g+t)!=q or (a+c+g+t+q) !=len(s):
    print("===")
else:
    for i in range(4):
        while s.count(h[i])!=Max:
            s[s.index("?")]=h[i]
    print("".join(s))



