n = int(input())
Sum = 0
Max =0
for i in range(n):
    a, b = map(int, input().split())
    Sum -=a
    Sum +=b
    Max = max(Max, Sum)
print(Max)
