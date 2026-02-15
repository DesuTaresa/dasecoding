s = input()

h = 'a'
counter = 0

for i in s:
    d = abs(ord(i) - ord(h))
    counter += min(d, 26 - d)
    h = i

print(counter)
