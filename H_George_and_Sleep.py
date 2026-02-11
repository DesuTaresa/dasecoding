s = input().split(":")
t = input().split(":")
h1, m1 = int(s[0]), int(s[1])
h2, m2 = int(t[0]), int(t[1])
m = m1 - m2
if m < 0:
    m += 60
    h1 -= 1
h = h1 - h2
if h < 0:
    h += 24
if h < 10:
    h = "0" + str(h)
else:
    h = str(h)

if m < 10:
    m = "0" + str(m)
else:
    m = str(m)

print(h + ":" + m)