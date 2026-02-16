d = input()
r = "a"
Max = 0
for i in d:
    dr = abs(ord(i)-ord(r)) 
    Max += min(dr,26-dr)
    r = i
print(Max)