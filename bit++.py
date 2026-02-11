n = int(input())
counter = 0
for i in range(n):
    x = input()
    if "+" in x:
        counter +=1
    elif "-" in x:
        counter -=1
print(counter)
