a, b =map(int,input().split())
counter = 0

while a<=b:
    counter+=1
    a*=3
    b*=2
print(counter)