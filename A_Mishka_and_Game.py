n = int(input())
m, c =0,0
for i in range(n):
    a, k = map(int, input().split())
    if a>k:
        m+=1
    elif k>a:
        c+=1
if m>c:
    print("Mishka")
elif c>m:
    print("Chris")
else:
    print("Friendship is magic!^^")