n = int(input())
s = input()
counter = 1
for i in range(n-1):
    d = input()
    if s != d:
        counter += 1
        s = d
print(counter)


