n , m = map(int, input().split())
count = 0
while n!=0 and m!=0:
    count +=1
    n -=1
    m -=1
if count%2 == 0:
    print("Malvika")
else:
    print("Akshat")