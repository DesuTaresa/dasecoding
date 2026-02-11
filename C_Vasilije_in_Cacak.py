t = int(input())
for i in range(t):
    n, k, x = map(int, input().split())
    Sum_min = k*(k+1)/2
    Sum_max = k*(2*n-k+1)/2
    if Sum_min<=x<=Sum_max:
        print("YES")
    else:
        print("NO")
    