n = int(input())
for i in range(n):
    m = int(input())
    s = input()
    while "()" in s:
        s = "".join(s.split("()"))
    print(len(s)//2)