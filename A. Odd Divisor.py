import math
n = int(input())
for i in range(n):
    d = int(input())
    if math.log(d,2) == int(math.log(d,2)):
        print("NO")
    else:
        print("YES")