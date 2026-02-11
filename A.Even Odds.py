a, b = map(int, input().split())

count = (a + 1) // 2

if b <= count:
    print(2*b - 1)
else:
    print(2*(b - count))