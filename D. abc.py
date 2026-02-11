n=int(input())
for i in range(n):
    s=input()
    s1=s[2]+s[1]+s[0]
    s2=s[1]+s[0]+s[2]
    s3=s[0]+s[2]+s[1]
    if s=="abc":
        print("yes")
    elif s1=="abc":
        print("yes")
    elif s2=="abc":
        print("yes")
    elif s3=="abc":
        print("yes")
    else:
        print("no")