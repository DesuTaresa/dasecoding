a, b, c, d = map(int, input().split())
h = input()
counter = 0
for i in h:
    if i == "1":
        counter += a
    elif i == "2":
        counter += b
    elif i == "3":
        counter += c
    elif i == "4":
        counter += d
print(counter)