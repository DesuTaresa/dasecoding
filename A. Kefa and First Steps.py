n = int(input())
lst = list(map(int, input().split()))
m = curr = 1

for i in range(1, len(lst)):
    if lst[i] >= lst[i - 1]:
        curr += 1
        m = max(m , curr)
    else:
        curr = 1

print(m)