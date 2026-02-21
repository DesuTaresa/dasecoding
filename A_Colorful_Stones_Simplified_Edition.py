s = input()
t = input()
counter = 0
for i in t:
    if s[counter] == i:
        counter += 1  

print(counter + 1)