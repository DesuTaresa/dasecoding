n = int(input())
s = input().strip()
my_list = list(s)
cont=0
for j in range(n):
    cont+=1
print(cont)
for i in range(1,n+1):
    s = input().strip()
    my_list = list(s)
    if "".join(my_list).lower() == "yes":
        print("YES")
    else:
        print("NO")



