n = int(input())
ls = list(map(int, input().split()))

po = 0
cr = 0

for i in ls:
    if i > 0:
        po += i
    else:
        if po > 0:
            po -= 1
        else:
            cr += 1

print(cr)
