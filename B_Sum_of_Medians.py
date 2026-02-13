n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    li=[]
    for j in range(b):
        if a==2:
            li.append(lst[:a])
            del lst[:a]
        else:
            x = lst[0]+lst[]
    counter =0
    for k in li:
        if a%2==0 and a>2:
            counter +=k[a//2+1]
        elif a==2:
            counter +=k[(a//2)]
        else:
            counter +=k[a//2]
    print(counter)