t = int(input())
print(t)  
for i in range(t):
    a, b, c = map(int, input().split())
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else: 
        print(a)
 

