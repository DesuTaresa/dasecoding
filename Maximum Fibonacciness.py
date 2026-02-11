t = int(input())
for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    num = [a1 + a2, a4 - a2, a5 - a4]
    max_fibo = 0
    for a3 in num:
        count = 0
        if a3 == a1 + a2:
            count += 1
        if a4 == a2 + a3:
            count += 1
        if a5 == a3 + a4:
            count += 1
        max_fibo = max(max_fibo, count)
    
    print(max_fibo)
