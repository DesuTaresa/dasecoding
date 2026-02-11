def addTwoNumbers(l1, l2):
    h1=l1[::-1]
    h2=l2[::-1]
    s1 = "".join(map(str, h1))
    s2 = "".join(map(str, h2))
    s=int(s1)+int(s2)
    lst=list(map(int,str(s)))
    lst.reverse()
    return lst