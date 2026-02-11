n = int(input())
lst = list(map(int, input().split()))
lst1 = list(map(int, input().split()))
lst3 = lst[1:] + lst1[1:]
if len(set(lst3))==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")