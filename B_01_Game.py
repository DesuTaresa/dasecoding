n = int(input())
for i in range(n):
    s = list(input())

    if len(set(s))==1:
        print("NET")
    else:
        counter =0
        j =1
        while len(set(s))>1:
            if s[j]!=s[j-1]:
                del s[j]
                del s[j-1]
                counter +=1
                j=0
            j+=1
            
        if counter%2!=0:
            print("DA")
        else:
            print("NET")
        