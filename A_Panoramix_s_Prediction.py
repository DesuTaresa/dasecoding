a, b = map(int, input().split())

def is_prime(x):
    for i in range(2, int(pow(x,1/2))+1):
        if x%i==0:
            return False
    return True
if a==2:
    if b==3:
        print("YES")
    else:
        print("NO")
else:
    y=a+2
    while  not is_prime(y):
        y+=2
    if y==b:
        print("YES")
    else:
        print("NO")

