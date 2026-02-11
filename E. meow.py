n = int(input())
for j in range(n):
    m = int(input())
    s = input().lower()

    lst = s[0]
    for i in range(1, m):
        if s[i] != s[i - 1]:
            lst += s[i]

    if lst == "meow":
        print("YES")
    else:
        print("NO")