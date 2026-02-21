a, b =map(int, input().split())


for i in range(1, 11):
    if (i * a) % 10 == 0 or (i * a) % 10 == b:
        print(i)
        break