n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    if a+c ==2*b:
        print("YES")
    else:
        if (2*b-c)/a == (2*b-c)//a and (2*b-c)/a>0 :
            print("YES")
        elif (2*b-a)/c == (2*b-a)//c  and (2*b-a)/c>0:
            print("YES")
        elif (a+c)/(2*b)== (a+c)//(2*b) and (a+c)/(2*b)>0:
            print("YES")
        else:
            print("NO")