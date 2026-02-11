s = input().strip()

if s == "":
    print(0)
else:
    n = int(s)
    if n >= 0 or abs(n) < 10:
        print(n)
    else:
        st = str(n)
        a = int(st[:-1])
        b = int(st[:-2] + st[-1])
        print(max(a, b))