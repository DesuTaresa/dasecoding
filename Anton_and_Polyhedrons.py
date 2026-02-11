n=int(input())
s1="Tetrahedron"
s2="Cube"
s3="Octahedron"
s4="Dodecahedron" 
s5="Icosahedron"
total=0
for i in range(n):
    s=input()
    if s==s1:
        total+=4
    elif s==s2:
        total+=6
    elif s==s3:
        total+=8
    elif s==s4:
        total+=12
    elif s==s5:
        total+=20
print( total) 