s = input().strip()

max_run = curr = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        curr += 1
        max_run = max(max_run, curr)
    else:
        curr = 1

print(max_run)