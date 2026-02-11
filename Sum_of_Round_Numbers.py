t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    place = 1

    while n > 0:
        digit = n % 10
        if digit != 0:
            res.append(digit * place)
        n //= 10
        place *= 10

    print(len(res))
    print(*res)
