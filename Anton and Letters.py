s = input().strip()
letters = set()
for ch in s:
    if ch.islower():
        letters.add(ch)
print(len(letters))
