for i in range(1,6):
    lst = list(map(int, input().split()))
    if 1 in lst:
        x= lst.index(1)+1
        print(abs(x-3)+abs(i-3))
        


