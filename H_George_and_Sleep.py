s = input().split(":")
t = input().split(":")
h1, m1 = int(s[0]), int(s[1])
h2, m2 = int(t[0]), int(t[1])
mm = m1 - m2
if mm< 0:
    mm += 60
    h1 -= 1
hh = h1 - h2
if hh < 0:
    hh += 24
if hh < 10:
    hh = "0" + str(hh)
else:
    hh = str(hh)

if mm < 10:
    mm = "0" + str(mm)
else:
    mm = str(mm)

print(hh + ":" + mm)