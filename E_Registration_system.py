n = int(input())
di = {}
for i in range(n):
    s = input()
    counter = di.get(s, 0)
    if counter == 0:
        print("OK")
        di[s] = 1
    else:
        h = s + str(counter)
        print(h)
        di[s] = counter + 1
        di[h] = 1
