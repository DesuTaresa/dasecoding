n = int(input())
for i in range(n):
    s = input()
    if len(s)%2!=0:
        print("NO")
    else:
        if s[:len(s)//2]==s[len(s)//2:]:
            print("YES")
        else:
            print("NO")