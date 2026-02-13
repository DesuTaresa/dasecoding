n = int(input())
counter = 0

for i in range(n):
    lst = list(map(int, input().split()))
    if lst.count(1)>=2:
        counter += 1
print(counter)