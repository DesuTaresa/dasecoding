n = int(input())
bi = list(map(int, input().split()))
m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    w = a - 1  
    left_bi = b - 1       
    right_bi = bi[w] - b
    bi[w] = 0

    if w > 0:
        bi[w - 1] += left_bi

    if w < n - 1:
        bi[w + 1] += right_bi

for i in bi:
    print(i)