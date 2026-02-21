n = int(input())
li = []

for i in range(n):
    a, b = map(int, input().split())
    li.append((a, b))
counter = 0

for i in range(n):
    for j in range(n):
        if i != j and li[i][0] == li[j][1]:
            counter += 1

print(counter)