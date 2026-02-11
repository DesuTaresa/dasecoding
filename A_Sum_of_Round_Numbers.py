n = int(input())
for i in range(n):
    m = int(input())
    lst = []
    counter =0
    d =1
    while m>0:
        x = m%10
        if x != 0:
            lst.append(x*d)
            counter +=1
        d *=10
        m//=10
      
    print(counter)
    print(*lst)
        
