n, m = map(int, input().split())

a = max(n, m)
w = 7 - a  
Max = 6

for i in range(6, 0, -1):
    if w % i == 0 and Max % i == 0:
        w //= i
        Max //= i
        break

print(str(w) + "/" + str(Max))