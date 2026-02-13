n, m = map(int, input().split())
lst = list(map(int, input().split()))
Max = 1
cur = 1
for i in range(1, n):
    if lst[i] != lst[i-1]:
        cur += 1
    else:
        cur = 1
    
    if cur > Max:
        Max = cur

print(Max)
