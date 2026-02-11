n = int(input())
for i in range(n):
    rating = input()
    if int(rating)>=1900:
        print("Division 1")
    elif 1600<=int(rating)<=1899:
        print("Division 2")
    elif 1400<=int(rating)<=1599:
        print("Division 3")
    elif int(rating)<=1399:
        print("Division 4")