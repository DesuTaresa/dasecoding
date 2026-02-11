t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    shft = s[n-1] + s[:n]
    res  = bin(int(s,2)|int(shft,2))[2:]
    move = 0
    while "0" in res:
        move +=1
        shft = shft[n-1]+shft[:n]
        res = bin(int(res, 2)|int(shft,2))[2:]
    print(move)
