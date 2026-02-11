n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    h = "Timur"

    if len(s)!= len(h):

        print("NO")
    else:
        counter =0
        for  j in range(len(s)):
            if h[j] in s:
                counter +=1
        if counter ==5:
            print("YES")
        else:
            print("NO")

