a,b , c, d = map(int, input().split())
ls = input()
counter = 0

for i in range(len(ls)):
    if ls[i] == "1":
        counter += a
    elif ls[i] == "2":
        counter += b
    elif ls[i] == "3":
        counter += c
    elif ls[i] == "4":
        counter += d
print(counter)
    