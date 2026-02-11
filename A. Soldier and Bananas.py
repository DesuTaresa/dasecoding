k , n , w = map(int, input().split())
total = 0
for i in range(1, w+1):
    total += i*k
if n < total:
    print(total-n)
else:
    print("0")
