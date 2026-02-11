t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    x=0
    if x%2==0:
        if x<0:
            print(x+b)
        else:
            print(x+b)
        x=a-b
       
    else:
        if x<0:
            print(x-b)
        else:
            print(x+b)
        x+= b
