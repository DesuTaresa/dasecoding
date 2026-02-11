n = int(input())
for i in range(n): 
    m = int(input())
    a = 1
    b = m-1
    counter =0
    while b>a:
        counter +=1
        a +=1
        b -=1
        
    print(counter)

