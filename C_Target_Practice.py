n = int(input())
for i in range(n):
    counter =0
    for j in range(1,6):
        s = input()
        for k in range(1,11):
            if "X"==s[k-1]:
                if k>=j and 11-k>=j:
                    counter +=j
                else:
                    if k<j:
                        counter +=k
                    else:
                        counter +=11-k
        
    for j in range(5,0 , -1):
        s = input()
        for k in range(1,11):
            if  "X"==s[k-1]:
                if k>=j and 11-k>=j:
                    counter +=j
                else:
                    if k<j:
                        counter +=k
                    else:
                        counter +=11-k
    print(counter)
