s = input().strip()
res = []
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        res.append(count)
        count = 1

res.append(count)
print(res)