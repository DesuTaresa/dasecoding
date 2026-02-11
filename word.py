x =int(input())
for i in range(x):
    y = input()
    if len(y)<=10:
        print(y)
    else:
        print(y[:1],len(y)-2,y[len(y)-1:]),



