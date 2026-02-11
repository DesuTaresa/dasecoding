x =int(input())
for i in range(1):
    y = input()
    for i in range(x-1):
        if len(y)<=10:
            print(y)
        else:
            print(y[:1]),
            print(len(y)-2),
            print(y[len(y):])


