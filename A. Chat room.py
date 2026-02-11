n = input().strip()
h = "hello"

i = 0  

for ch in n:
    if i < len(h) and ch == h[i]:
        i += 1

if i == len(h):
    print("YES")
else:
    print("NO")
