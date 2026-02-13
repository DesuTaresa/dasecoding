n = int(input())
lst = list(map(int,input().split()))
lst.sort() 
counter =lst.count(4)
cont = lst.count(2)
counter += cont//2
cont -=(counter//2)*2

